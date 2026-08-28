import io, cairosvg, pygame
from pathlib import Path
from functools import lru_cache

from .type import IconType
from ._register import IconRegister

class _IconMeta(type):
    _icon_register = IconRegister()

    def __new__(cls, name, bases, namespace, /, **kwds):
        return super().__new__(cls, name, bases, namespace, **kwds)

    def __getattr__(cls, name):
        return cls._icon_register.get_icon(name)

class Icons(metaclass=_IconMeta):
    @classmethod
    def register(cls, *icons: IconType):

        """
        Register one or more icons into the shared icon registry.

        Once registered, an icon can be accessed directly as an attribute
        (e.g. `Icons.MENU`) via `_IconMeta.__getattr__`.

        Args:
            *icons: One or more `IconType` instances to register.
        """

        cls._icon_register.register(*icons)

    @classmethod
    def unregister(cls, *icons: IconType):

        """
        Unregister (remove) one or more icons from the shared registry.

        After removal, accessing the icon via `Icons.<ICON_NAME>` will no
        longer be valid.

        Args:
            *icons: One or more `IconType` instances to remove.
        """

        cls._icon_register.unregister(*icons)

@lru_cache(maxsize=10)
def svg2png(path: str, /, size: int = 32) -> pygame.Surface:

    """
    Render an SVG file on disk into a `pygame.Surface`.

    The result is cached by `(path, size)` to avoid re-rendering with the
    same input parameters.

    Args:
        path: Filesystem path to a `.svg` file.
        size: Width and height (in pixels) of the output surface.
            Defaults to 32.

    Returns:
        A `pygame.Surface` with alpha already converted, ready to `blit`.

    Raises:
        FileNotFoundError: If `path` does not point to an existing file.
    """

    if not Path(path).exists():
        raise FileNotFoundError(f"Cannot find svg file at: {path!r}")

    w, h = size, size
    png_bytes = cairosvg.svg2png(path, output_width=w, output_height=h)

    return pygame.image.load(io.BytesIO(png_bytes)).convert_alpha()

# ERROR: Cannot use this func in current
# It cannot find and download source svg in the internet

# @lru_cache(maxsize=10)
# def url2png(url: str, /, size: int = 32) -> pygame.Surface:

#     """
#     Fetch and render an SVG from a URL into a `pygame.Surface`.

#     The result is cached by `(url, size)` to avoid re-fetching/re-rendering
#     with the same input parameters.

#     Args:
#         url: URL pointing to an `.svg` resource.
#         size: Width and height (in pixels) of the output surface.
#             Defaults to 32.

#     Returns:
#         A `pygame.Surface` with alpha already converted, ready to `blit`.
#     """

#     w, h = size, size
#     png_bytes = cairosvg.svg2png(url=url, output_width=w, output_height=h)

#     return pygame.image.load(io.BytesIO(png_bytes)).convert_alpha()

@lru_cache(maxsize=10)
def code2png(source: str, /, size: int = 32, fill: str = "#FFFFFF", color: str = "#000000") -> pygame.Surface:

    """
    Render a raw SVG markup string into a `pygame.Surface`.

    Replaces the `stroke='currentColor'` and `fill='currentColor'`
    placeholders in `source` with the given colors before rendering,
    allowing icons to be recolored at runtime without needing a separate
    SVG file per color.

    The result is cached by `(source, size, fill, color)`.

    Args:
        source: Full SVG markup string, not a file path or URL.
        size: Width and height (in pixels) of the output surface.
            Defaults to 32.
        fill: Replacement color for `fill='currentColor'`. Defaults to
            `"#FFFFFF"`.
        color: Replacement color for `stroke='currentColor'`. Defaults to
            `"#000000"`.

    Returns:
        A `pygame.Surface` with alpha already converted, ready to `blit`.
    """

    source = source.replace("stroke='currentColor'", f"stroke={color}")
    source = source.replace("fill='currentColor'", f"fill={fill}")
    
    w, h = size, size
    png_bytes = cairosvg.svg2png(bytestring=source.encode("utf-8"), output_width=w, output_height=h)

    return pygame.image.load(io.BytesIO(png_bytes)).convert_alpha()

@lru_cache(maxsize=10)
def icon2png(icon: IconType, /, size: int = 32, fill: str = "#FFFFFF", color: str = "#000000") -> pygame.Surface:

    """
    Render an `IconType` (registered or ad-hoc) into a `pygame.Surface`.

    Thin wrapper around `code2png`: pulls the SVG markup from `icon.path`
    and renders/recolors it the same way.

    Note: `IconType` must be hashable (e.g. a dataclass declared with
    `frozen=True`) to be usable as an `lru_cache` key, otherwise this
    raises `TypeError: unhashable type`.

    Args:
        icon: The `IconType` instance to render; `icon.path` holds the
            SVG markup.
        size: Width and height (in pixels) of the output surface.
            Defaults to 32.
        fill: Replacement color for `fill='currentColor'`. Defaults to
            `"#FFFFFF"`.
        color: Replacement color for `stroke='currentColor'`. Defaults to
            `"#000000"`.

    Returns:
        A `pygame.Surface` with alpha already converted, ready to `blit`.
    """

    return code2png(icon.path, size, fill, color)

