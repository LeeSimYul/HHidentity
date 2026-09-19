
"""
Generates the media team asset set (2026 edition)

Every file under media-team/overlays, media-team/badges and
media-team/templates/guides is derived from the vector sources in logo/ by
this script. Do not hand-edit the generated files -- change the constants
below and re-run:

    python media-team/generate.py
"""

import dataclasses
import io
import pathlib

import cairosvg
from PIL import Image, ImageDraw, ImageFont


CWD = pathlib.Path(__file__).parent
ROOT = CWD.parent
LOGO_FOLDER = ROOT / 'logo'

OVERLAY_FOLDER = CWD / 'overlays'
BADGE_FOLDER = CWD / 'badges'
GUIDE_FOLDER = CWD / 'templates' / 'guides'

# Supersampling factor used when rasterising plates and guide lines
SUPERSAMPLE: int = 4

# Alpha applied to the corner watermark overlays (see MEDIA_GUIDELINES.md)
WATERMARK_ALPHA: float = 0.70

# Scrim plates the logo sits on when it has to survive arbitrary footage
DARK_PLATE = (11, 18, 24, 184)
LIGHT_PLATE = (255, 255, 255, 219)

# Fraction of a badge occupied by the logo; the remainder is clear space
BADGE_LOGO_RATIO: float = 0.68

# Margin and minimum logo size expressed against the short edge of a layout
MARGIN_RATIO: float = 0.06
LOGO_MIN_RATIO: float = 0.08

GUIDE_LINE = (255, 61, 122, 200)
GUIDE_SAFE = (50, 145, 211, 180)
GUIDE_BOX = (77, 206, 125, 220)
GUIDE_TEXT = (11, 18, 24, 230)


def render_svg(name: str, size: int) -> Image.Image:
    """Rasterises one of the vector sources in logo/ to a square RGBA image."""

    content = cairosvg.svg2png(
        url=str(LOGO_FOLDER / f'{name}.svg'),
        output_width=size,
        output_height=size,
    )

    return Image.open(io.BytesIO(content)).convert('RGBA')


def recolor(image: Image.Image, color: tuple[int, int, int]) -> Image.Image:
    """Replaces every opaque pixel with a flat color, keeping the alpha mask."""

    flat = Image.new('RGBA', image.size, (*color, 0))
    flat.putalpha(image.getchannel('A'))

    return flat


def with_alpha(image: Image.Image, alpha: float) -> Image.Image:
    faded = image.copy()
    faded.putalpha(image.getchannel('A').point(lambda value: round(value * alpha)))

    return faded


def export(image: Image.Image, path: pathlib.Path, webp: bool = True) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)

    image.save(path.with_suffix('.png'), optimize=True)
    print(f'Wrote {path.with_suffix(".png").relative_to(ROOT)}')

    if webp:
        image.save(path.with_suffix('.webp'), lossless=True, quality=100, method=6)
        print(f'Wrote {path.with_suffix(".webp").relative_to(ROOT)}')


# --- Overlays ---------------------------------------------------------------

OVERLAY_SIZES: tuple[int, ...] = (256, 512, 1024)

# Each entry maps an exported overlay name onto its vector source
OVERLAY_SOURCES: dict[str, str] = {
    # Full color mark, for dark or busy backgrounds
    'logo': 'logo',
    # Same mark without the clip mask; holds up better at small raster sizes
    'logo_precomposed': 'logo_precomposed',
    # Single color mark for light backgrounds, as recommended by GUIDELINES.md
    'logo_positive_space': 'logo_positive_space',
    # Outlined hands, for the rare case the mark must sit directly on white
    'hands_outlined': 'hands_outlined',
}


def build_overlays() -> None:
    for name, source in OVERLAY_SOURCES.items():
        for size in OVERLAY_SIZES:
            export(render_svg(source, size), OVERLAY_FOLDER / f'{name}_{size}')

    # Corner watermarks ship pre-faded so editors do not have to guess an opacity
    for size in (256, 512):
        export(
            with_alpha(render_svg('logo', size), WATERMARK_ALPHA),
            OVERLAY_FOLDER / f'watermark_logo_{size}',
        )
        export(
            with_alpha(recolor(render_svg('logo_positive_space', size), (255, 255, 255)), WATERMARK_ALPHA),
            OVERLAY_FOLDER / f'watermark_mono_light_{size}',
        )


# --- Badges -----------------------------------------------------------------

AVATAR_SIZES: tuple[int, ...] = (128, 256, 512)

# (width, height) of the lower third plates, for 1080p and 4K timelines
LOWER_THIRD_SIZES: tuple[tuple[int, int], ...] = ((960, 160), (1440, 240))


@dataclasses.dataclass(frozen=True)
class BadgeStyle:
    name: str
    plate: tuple[int, int, int, int]
    logo_source: str

    def logo(self, size: int) -> Image.Image:
        return render_svg(self.logo_source, size)


BADGE_STYLES: tuple[BadgeStyle, ...] = (
    BadgeStyle('dark', DARK_PLATE, 'logo'),
    BadgeStyle('light', LIGHT_PLATE, 'logo_positive_space'),
)


def build_avatar_badges() -> None:
    for style in BADGE_STYLES:
        for size in AVATAR_SIZES:
            scale = size * SUPERSAMPLE

            plate = Image.new('RGBA', (scale, scale), (0, 0, 0, 0))
            ImageDraw.Draw(plate).ellipse((0, 0, scale - 1, scale - 1), fill=style.plate)
            canvas = plate.resize((size, size), Image.Resampling.LANCZOS)

            diameter = round(size * BADGE_LOGO_RATIO)
            offset = round((size - diameter) / 2)
            canvas.alpha_composite(style.logo(diameter), (offset, offset))

            export(canvas, BADGE_FOLDER / f'badge_avatar_{style.name}_{size}')


def build_lower_third_badges() -> None:
    for style in BADGE_STYLES:
        for width, height in LOWER_THIRD_SIZES:
            scale = SUPERSAMPLE

            plate = Image.new('RGBA', (width * scale, height * scale), (0, 0, 0, 0))
            ImageDraw.Draw(plate).rounded_rectangle(
                (0, 0, width * scale - 1, height * scale - 1),
                radius=height * scale / 2,
                fill=style.plate,
            )
            canvas = plate.resize((width, height), Image.Resampling.LANCZOS)

            # The logo is locked to the left cap; the rest of the plate is the
            # text area documented in badges/README.md
            diameter = round(height * 0.72)
            inset = round(height * 0.14)
            canvas.alpha_composite(style.logo(diameter), (inset, inset))

            export(canvas, BADGE_FOLDER / f'badge_lower_third_{style.name}_{width}x{height}')


# --- Template guides --------------------------------------------------------

@dataclasses.dataclass(frozen=True)
class TemplateGuide:
    name: str
    width: int
    height: int
    label: str

    @property
    def short_edge(self) -> int:
        return min(self.width, self.height)

    @property
    def margin(self) -> int:
        return round(self.short_edge * MARGIN_RATIO)

    @property
    def logo_box(self) -> int:
        return round(self.short_edge * LOGO_MIN_RATIO)


TEMPLATE_GUIDES: tuple[TemplateGuide, ...] = (
    TemplateGuide('thumbnail_1280x720', 1280, 720, 'Video thumbnail 16:9'),
    TemplateGuide('thumbnail_1920x1080', 1920, 1080, 'Video frame / thumbnail 16:9'),
    TemplateGuide('poster_a3_1754x2480', 1754, 2480, 'Poster A3 portrait, 150 dpi'),
    TemplateGuide('cardnews_1080x1080', 1080, 1080, 'Card news 1:1'),
    TemplateGuide('cardnews_1080x1350', 1080, 1350, 'Card news 4:5'),
    TemplateGuide('story_1080x1920', 1080, 1920, 'Story / shorts 9:16'),
)


def dashed_rectangle(draw: ImageDraw.ImageDraw, box, color, width: int, dash: int) -> None:
    left, top, right, bottom = box

    for x in range(left, right, dash * 2):
        draw.line((x, top, min(x + dash, right), top), fill=color, width=width)
        draw.line((x, bottom, min(x + dash, right), bottom), fill=color, width=width)

    for y in range(top, bottom, dash * 2):
        draw.line((left, y, left, min(y + dash, bottom)), fill=color, width=width)
        draw.line((right, y, right, min(y + dash, bottom)), fill=color, width=width)


def build_template_guides() -> None:
    for guide in TEMPLATE_GUIDES:
        canvas = Image.new('RGBA', (guide.width, guide.height), (0, 0, 0, 0))
        draw = ImageDraw.Draw(canvas)

        stroke = max(2, round(guide.short_edge / 360))

        margin = guide.margin
        dashed_rectangle(
            draw,
            (margin, margin, guide.width - margin, guide.height - margin),
            GUIDE_LINE,
            stroke,
            dash=max(8, round(guide.short_edge / 60)),
        )

        # Type safe area: one further margin in from the trim margin
        safe = margin * 2
        dashed_rectangle(
            draw,
            (safe, safe, guide.width - safe, guide.height - safe),
            GUIDE_SAFE,
            max(1, stroke // 2),
            dash=max(6, round(guide.short_edge / 90)),
        )

        # Minimum brand block, anchored to the bottom right of the trim margin
        box = guide.logo_box
        clear = round(box * 0.25)
        box_left = guide.width - margin - box
        box_top = guide.height - margin - box
        draw.rectangle(
            (box_left, box_top, box_left + box, box_top + box),
            outline=GUIDE_BOX,
            width=stroke,
        )
        draw.rectangle(
            (box_left - clear, box_top - clear, box_left + box + clear, box_top + box + clear),
            outline=GUIDE_BOX,
            width=max(1, stroke // 2),
        )
        canvas.alpha_composite(with_alpha(render_svg('logo', box), 0.55), (box_left, box_top))

        caption = (
            f'{guide.label} - {guide.width}x{guide.height} px | '
            f'margin {margin} px | logo min {box} px | clear space {clear} px'
        )

        # Shrink the caption until it fits between the left and right margins
        size = max(12, round(guide.short_edge / 36))
        while size > 12:
            font = ImageFont.load_default(size=size)
            if draw.textlength(caption, font=font) <= guide.width - margin * 2:
                break
            size -= 1

        left, top, right, bottom = draw.textbbox((0, 0), caption, font=font)
        pad = round(size * 0.4)
        origin = (margin, max(pad, margin - (bottom - top) - pad * 3))

        # A light plate keeps the caption readable whichever artwork it sits on
        draw.rounded_rectangle(
            (
                origin[0] - pad,
                origin[1] - pad,
                origin[0] + (right - left) + pad,
                origin[1] + (bottom - top) + pad * 2,
            ),
            radius=pad,
            fill=(255, 255, 255, 214),
        )
        draw.text(origin, caption, fill=GUIDE_TEXT, font=font)

        export(canvas, GUIDE_FOLDER / f'{guide.name}_guide', webp=False)


if __name__ == '__main__':
    build_overlays()
    build_avatar_badges()
    build_lower_third_badges()
    build_template_guides()
