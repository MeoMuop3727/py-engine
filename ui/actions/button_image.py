import pygame
from dataclasses import dataclass, field

from ..ui import UserInterfaceType, CSS_StyleType
from libs.pce.utils import apply_instance
from libs.pce.systems import Transform, AnimationSheet

@dataclass(slots=True)
class StyleButtonImage(CSS_StyleType):
    size_button: tuple[int, int] = (32, 32)

class ButtonImage(UserInterfaceType):
    def __init__(self, surface, style=None, audios=None, animations=None, connections=None):
        super().__init__(surface, style, audios, animations, connections)

        self._pressed = False

        self._style: StyleButtonImage = apply_instance(StyleButtonImage(), style)
        self._modified_style: StyleButtonImage = apply_instance(StyleButtonImage(), style)

    # States
    def hovered(self, style, /):
        if not isinstance(style, CSS_StyleType):
            raise TypeError(f"The value must be CSS_StyleType, not {type(style).__name__!r}")

        mouse_pos = pygame.mouse.get_pos()
        
        is_hovered = self._border.collidepoint(mouse_pos) or self._button.collidepoint(mouse_pos)

        if not is_hovered:
            self._modified_style = self._style
            self._animations.switch("default")
        else:
            self._modified_style = style
            self._animations.switch("hovered")

    def pressed(self, style, /):
        if not isinstance(style, CSS_StyleType):
            raise TypeError(f"The value must be CSS_StyleType, not {type(style).__name__!r}")
        
        mouse_pos = pygame.mouse.get_pos()

        is_hovered = self._border.collidepoint(mouse_pos) or self._button.collidepoint(mouse_pos)
        is_pressed = pygame.mouse.get_pressed()[0]

        if not is_hovered: 
            self._modified_style = self._style
            self._animations.switch("default")
            self._pressed = False
        elif is_hovered and is_pressed:
            if not self._pressed:
                self._pressed = True

                if self._audios is not None: 
                    self._audios.play()
                if self.func is not None or self.func is not isinstance(self.func, ...):
                    self.func()

            self._animations.switch("pressed")

    def _render(self, speed: float = 1.):
        self._animations.update(speed)

    def update(self, speed: float = 1.):
        self._render(speed)