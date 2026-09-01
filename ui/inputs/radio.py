import pygame
from copy import copy
from typing import Optional
from dataclasses import dataclass, field

from ..ui import UserInterfaceType, CSS_StyleType
from libs.pce.utils import apply_instance
from utils import apply_value
from libs.pce.systems import Transform, FontStyle

@dataclass(slots=True)
class StyleRadioButton(CSS_StyleType):
    """"""
    content: str = ""
    font_style: FontStyle = field(default_factory=FontStyle)
    size_button: int = 11
    gap: int = 10
    border_radius: tuple[int, int, int, int] = (0, 0, 0, 0)
    border_width: int = 2
    border_color: pygame.color.Color = (0, 0, 0, 255)
    bg_color: pygame.color.Color = (255, 255, 255, 255)

class RadioButton(UserInterfaceType):
    """"""
    def __init__(self, surface, style=None, audios=None, connections=None):
        super().__init__(surface, style, audios, None, connections)

        self._focused = False
        self._pressed = False

        self._style: StyleRadioButton = apply_instance(StyleRadioButton(), style)
        self._modified_style: StyleRadioButton = apply_instance(StyleRadioButton(), style)

        # Font
        self._style.font_style.content = self._style.content
        self._modified_style.font_style.content = self._modified_style.content

        # Button
        self.size_button = (self._modified_style.size_button, self._modified_style.size_button)
        self._radio_button = pygame.Rect(self._modified_style.transform.position, self.size_button)

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

        # Leftmid point of font to render font
        self._lmx = self._modified_style.transform.position[0] + self.size_button[0] + self._modified_style.gap
        self._lmy = self._modified_style.transform.position[1] + self.size_button[1] / 2 

    @property
    def active(self) -> bool:
        return self._focused
    @active.setter
    def active(self, active: bool):
        self._focused = active

    # States
    def hovered(self, style, /):
        if not isinstance(style, CSS_StyleType):
            raise TypeError(f"The value must be CSS_StyleType, not {type(style).__name__!r}")

        mouse_pos = pygame.mouse.get_pos()

        is_hovered = self._border.collidepoint(mouse_pos) or self._radio_button.collidepoint(mouse_pos)

        if not is_hovered:
            self._modified_style = copy(self._style)
            self._modified_style.font_style.content = self._style.content
        else:
            self._modified_style = style
            self._modified_style.font_style.content = style.content

    def pressed(self, style, /):
        if not isinstance(style, CSS_StyleType):
            raise TypeError(f"The value must be CSS_StyleType, not {type(style).__name__!r}")
        
        mouse_pos = pygame.mouse.get_pos()

        is_hovered = self._border.collidepoint(mouse_pos) or self._radio_button.collidepoint(mouse_pos)
        is_pressed = pygame.mouse.get_pressed()[0]

        if not is_hovered: 
            self._modified_style = copy(self._style)
            self._modified_style.font_style.content = self._style.content
            self._pressed = False
        elif is_hovered and is_pressed:
            if not self._pressed:
                self._pressed = True

                self._focused = not self._focused

                if self._audios is not None: 
                    self._audios.play()

            self._modified_style = style
            self._modified_style.font_style.content = style.content

    def focused(self, style, /):
        if not isinstance(style, CSS_StyleType):
            raise TypeError(f"The value must be CSS_StyleType, not {type(style).__name__!r}")

        if self._focused:
            self._modified_style = style
            self._modified_style.font_style.content = style.content
        else:
            self._modified_style = self._style
            self._modified_style.font_style.content = self._style.content

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

        pygame.draw.rect(
            surface=self._surface,
            color=self._modified_style.bg_color,
            rect=self._radio_button,
            border_top_left_radius=self._modified_style.border_radius[0],
            border_top_right_radius=self._modified_style.border_radius[1],
            border_bottom_right_radius=self._modified_style.border_radius[2],
            border_bottom_left_radius=self._modified_style.border_radius[3]
        )

        self._modified_style.font_style.render(
            surface=self._surface,
            transform=Transform(
                position=(self._lmx, self._lmy),
                scale=self._modified_style.transform.scale,
                rotation=self._modified_style.transform.rotation
            ),
            anchor="midleft"
        )

    def update(self):
        self._render()

class ListRadioButtons:
    def __init__(self,
                 surface: pygame.Surface,
                 contents: Optional[list[str]] = None,
                 style: Optional[CSS_StyleType] = None,
                 rows: Optional[int] = 10,
                 columns: Optional[int] = None,
                 actives: Optional[list[int]] = None,
                 gap: int = 10):
        self._surface = surface
        self._style: StyleRadioButton = style   # Default state of radio buttons

        self.contents = apply_value([], contents)
        self.rows = apply_value(1, rows)
        self.columns = apply_value(1, columns)
        self.actives = apply_value([], actives)
        self.gap = gap                          # Distance among radio buttons

        self._list_radio_buttons: list[RadioButton] = self._apply_list_radio_buttons()  # Default list radio buttons

        self._list_actives: list[bool] = [
            rb._focused for rb in self._list_radio_buttons
        ]

    @property
    def list_actives(self) -> list[bool]:
        return self._list_actives

    def _apply_list_radio_buttons(self) -> list[RadioButton]:
        count: int = 0
        list_radio_buttons: list[RadioButton] = []

        for r in range(0, self.rows):
            for c in range(0, self.columns):
                index = count % len(self.contents)

                # Assign content for font style to get the size of the content
                self._style.font_style.content = self.contents[index]   

                size_rect_w = self._style.size_button + self._style.gap + self._style.font_style.get_size()[0]
                size_rect_h = max(self._style.size_button, self._style.font_style.get_size()[1]) + self._style.gap

                rb = RadioButton(
                    surface=self._surface,
                    style=StyleRadioButton(
                        transform=Transform(
                            position=(
                                self._style.transform.position[0] + (size_rect_w + self.gap) * c,
                                self._style.transform.position[1] + (size_rect_h + self.gap) * r
                            )
                        ),
                        content=self.contents[index],
                        font_style=copy(self._style.font_style),
                        size_button=self._style.size_button,
                        gap=self._style.gap,
                        border_radius=self._style.border_radius,
                        border_width=self._style.border_width,
                        border_color=self._style.border_color,
                        bg_color=self._style.bg_color
                    )
                )

                if index in self.actives:
                    rb._focused = True

                list_radio_buttons.append(rb)

                count += 1

        return list_radio_buttons
    
    def hovered(self, style: CSS_StyleType, /):
        for index, radio in enumerate(self._list_radio_buttons):
            s = copy(style)
            s.font_style = copy(style.font_style)
            s.content = self.contents[index]
            radio.hovered(s)

    def pressed(self, style: CSS_StyleType, /):
        for index, radio in enumerate(self._list_radio_buttons):
            s = copy(style)
            s.font_style = copy(style.font_style)
            s.content = self.contents[index]
            radio.pressed(s)

    def focused(self, style: CSS_StyleType, /):
        # Apply focused state for buttons have been actived
        for index, active in enumerate(self._list_actives):
            if not active: continue

            s = copy(style)
            s.font_style = copy(style.font_style)
            s.content = self._list_radio_buttons[index]._style.content
            self._list_radio_buttons[index].focused(s)

        # Apply forcused state for buttons clicked
        for index, radio in enumerate(self._list_radio_buttons):
            s = copy(style)
            s.font_style = copy(style.font_style)
            s.content = self.contents[index]
            radio.focused(s)

    def update(self):
        for index, radio in enumerate(self._list_radio_buttons):
            self._list_actives[index] = radio._focused
            radio.update()
