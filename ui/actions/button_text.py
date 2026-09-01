import pygame
from dataclasses import dataclass, field

from ..ui import UserInterfaceType, CSS_StyleType
from libs.pce.utils import apply_instance
from libs.pce.systems import FontStyle, Transform

@dataclass(slots=True)
class StyleButtonText(CSS_StyleType):
    """"""
    content: str = ""
    font_style: FontStyle = field(default_factory=FontStyle)
    size_button: tuple[int, int] = (100, 50)
    bg_color: pygame.color.Color = (255, 255, 255, 255)
    border_width: int = 0
    border_radius: tuple[int, int, int, int] = (0, 0, 0, 0)     # Topleft - Topright - Bottomright - Bottomleft
    border_color: pygame.color.Color = (0, 0, 0, 255)

class ButtonText(UserInterfaceType):
    """"""
    def __init__(self, surface, style=None, audios=None, animations=None, connections=None):
        super().__init__(surface, style, audios, animations, connections)

        self._pressed = False
        
        self._style: StyleButtonText = apply_instance(StyleButtonText(), style)
        self._modified_style: StyleButtonText = apply_instance(StyleButtonText(), style)

        # Font
        self._style.font_style.content = self._style.content
        self._modified_style.font_style.content = self._modified_style.font_style.content

        # Button
        if self._modified_style.size_button[0] <= 0 or self._modified_style.size_button[1] <= 0:
            self.size_button = self._modified_style.font_style.get_size()
        else:
            self.size_button = self._modified_style.size_button
        self._button = pygame.Rect(self._modified_style.transform.position, self.size_button)

        # Border
        self._border = pygame.Rect(
            (
                self._modified_style.transform.position[0] - self._modified_style.border_width,
                self._modified_style.transform.position[1] - self._modified_style.border_width
            ),
            (
                self.size_button[0] + self._modified_style.border_width * 2,
                self.size_button[1] + self._modified_style.border_width * 2
            )
        )

        # Center point of button to render font
        self._cx = self._modified_style.transform.position[0] + self.size_button[0] / 2
        self._cy = self._modified_style.transform.position[1] + self.size_button[1] / 2

    # States
    def hovered(self, style, /):
        if not isinstance(style, CSS_StyleType):
            raise TypeError(f"The value must be CSS_StyleType, not {type(style).__name__!r}")
        
        mouse_pos = pygame.mouse.get_pos()

        is_hovered = self._border.collidepoint(mouse_pos) or self._button.collidepoint(mouse_pos)

        if not is_hovered: 
            self._modified_style = self._style
            self._modified_style.font_style.content = self._style.content
        else:
            self._modified_style = style
            self._modified_style.font_style.content = style.content

    def pressed(self, style, /):
        if not isinstance(style, CSS_StyleType):
            raise TypeError(f"The value must be CSS_StyleType, not {type(style).__name__!r}")
        
        mouse_pos = pygame.mouse.get_pos()

        is_hovered = self._border.collidepoint(mouse_pos) or self._button.collidepoint(mouse_pos)
        is_pressed = pygame.mouse.get_pressed()[0]

        if not is_hovered: 
            self._modified_style = self._style
            self._modified_style.font_style.content = self._style.content
            self._pressed = False
        elif is_hovered and is_pressed:
            if not self._pressed:
                self._pressed = True

                if self._audios is not None: 
                    self._audios.play()
                if self.func is not None:
                    self.func()

            self._modified_style = style
            self._modified_style.font_style.content = style.content

    def _render(self):
        if not self._modified_style.visible: return

        if self._modified_style.border_width >= 0: 
            pygame.draw.rect(
                surface=self._surface,
                color=self._modified_style.border_color,
                rect=self._border,
                border_top_left_radius=self._modified_style.border_radius[0],
                border_top_right_radius=self._modified_style.border_radius[1],
                border_bottom_right_radius=self._modified_style.border_radius[2],
                border_bottom_left_radius=self._modified_style.border_radius[3]
            )

        if not (self._modified_style.size_button[0] <= 0 or self._modified_style.size_button[1] <= 0):
            pygame.draw.rect(
                surface=self._surface,
                color=self._modified_style.bg_color,
                rect=self._button,
                border_top_left_radius=self._modified_style.border_radius[0],
                border_top_right_radius=self._modified_style.border_radius[1],
                border_bottom_right_radius=self._modified_style.border_radius[2],
                border_bottom_left_radius=self._modified_style.border_radius[3]
            )

        self._modified_style.font_style.render(
            surface=self._surface,
            transform=Transform(
                position=(self._cx, self._cy),
                scale=self._modified_style.transform.scale,
                rotation=self._modified_style.transform.rotation
            ),
            anchor="center"
        )

    def update(self):
        self._render()
        
