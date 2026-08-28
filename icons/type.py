from dataclasses import dataclass

@dataclass(slots=True, frozen=True)
class IconType:
    name: str = ""
    path: str = ""
