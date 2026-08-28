from ._stub_generate import generate_stub_icons
generate_stub_icons()

from .type import IconType
from .icons import Icons, svg2png, code2png, icon2png

__all__ = ["IconType", "Icons", "svg2png", "code2png", "icon2png"]
