from pathlib import Path
from ._defination import _ICONS, _FUNC_NAMES_CLASS_ICONS, _FUNCTOOL_NAMES

STUB_PATH_ICON = Path(__file__).with_name("icons.pyi")

def generate_stub_icons():
    lines: list[str] = [
        "import pygame",
        "from .type import IconType",
        "",
        "class Icons:",
        ""
    ]

    for name_icon in sorted(list(_ICONS)):
        lines.append(f"\t{name_icon}: IconType")
    lines.append("")

    for name_func in sorted(_FUNC_NAMES_CLASS_ICONS):
        lines.append(f"\tdef {name_func}(cls, *icons: IconType): ...")
    lines.append("")

    for name_func in sorted(_FUNCTOOL_NAMES):
        lines.append(f"def {name_func}")
    lines.append("")

    STUB_PATH_ICON.write_text("\n".join(lines), encoding="utf-8")

