import pygame
from copy import copy
from typing import Optional
from dataclasses import dataclass, field

from ..ui import UserInterfaceType, CSS_StyleType
from libs.pce.utils import apply_instance
from utils import apply_value
from libs.pce.systems import Transform, FontStyle

@dataclass(slots=True)
class StyleCheckbox(CSS_StyleType):
    """"""
    content: str = ""
    font_style: FontStyle = field(default_factory=FontStyle)
    size_button: int = 11
    gap: int = 10
    border_radius: tuple[int, int, int, int] = (0, 0, 0, 0)
    border_width: int = 2
    border_color: pygame.color.Color = (0, 0, 0, 255)
    bg_color: pygame.color.Color = (255, 255, 255, 255)

class Checkbox(UserInterfaceType):
    """"""
    def __init__(self, surface, style=None, audios=None, connections=None):
        super().__init__(surface, style, audios, None, connections)

        self._focused = False
        self._pressed = False

        self._style: StyleCheckbox = apply_instance(StyleCheckbox(), style)
        self._modified_style: StyleCheckbox = apply_instance(StyleCheckbox(), style)

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
                self._focused = True

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

class ListCheckboxes:
    def __init__(self,
                 surface: pygame.Surface,
                 contents: Optional[list[str]] = None,
                 style: Optional[CSS_StyleType] = None,
                 rows: Optional[int] = 10,
                 columns: Optional[int] = None,
                 active: Optional[int] = None,
                 gap: int = 10):
        self._surface = surface
        self._style: StyleCheckbox = style   # Default state of radio buttons

        self.contents = apply_value([], contents)
        self.rows = apply_value(1, rows)
        self.columns = apply_value(1, columns)
        self.active = apply_value(-1, active)
        self.gap = gap                          # Distance among radio buttons

        self._list_checkboxes: list[Checkbox] = self._apply_list_checkboxes()  # Default list radio buttons

        self._list_actives: list[bool] = [False] * len(self._list_checkboxes)
        if self.active != -1: 
            self._list_actives[self.active] = True

    @property
    def list_actives(self) -> list[bool]:
        return self._list_actives

    def _apply_list_checkboxes(self) -> list[Checkbox]:
        count: int = 0
        list_checkboxes: list[Checkbox] = []

        for r in range(0, self.rows):
            for c in range(0, self.columns):
                index = count % len(self.contents)

                # Assign content for font style to get the size of the content
                self._style.font_style.content = self.contents[index]   

                size_rect_w = self._style.size_button + self._style.gap + self._style.font_style.get_size()[0]
                size_rect_h = max(self._style.size_button, self._style.font_style.get_size()[1]) + self._style.gap

                cb = Checkbox(
                    surface=self._surface,
                    style=StyleCheckbox(
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

                if index == self.active:
                    cb._focused = True

                list_checkboxes.append(cb)

                count += 1

        return list_checkboxes
    
    def hovered(self, style: CSS_StyleType, /):
        for index, cb in enumerate(self._list_checkboxes):
            s = copy(style)
            s.font_style = copy(style.font_style)
            s.content = self.contents[index]
            cb.hovered(s)

    def pressed(self, style: CSS_StyleType, /):
        clicked_int: Optional[int] = None

        for index, cb in enumerate(self._list_checkboxes):
            was_focused = cb._focused   # Save the state before calling pressed()

            s = copy(style)
            s.font_style = copy(style.font_style)
            s.content = self.contents[index]
            cb.pressed(s)

            # If this checkbox just has changed from False -> True  in this pressed time
            # Save the index
            if cb._focused and not was_focused:
                clicked_int = index

        # If it is having a checkbox turned on, turn off all others
        if clicked_int is not None:
            for index, cb in enumerate(self._list_checkboxes):
                if index != clicked_int:
                    cb._focused = False
                    cb._pressed = False

        # Reupdate _list_active immediately
        # Do not need to wait the update() in the next frame
        for index, cb in enumerate(self._list_checkboxes):
            self._list_actives[index] = cb._focused

    def focused(self, style: CSS_StyleType, /):
        # Apply focused state for buttons have been actived
        for index, active in enumerate(self._list_actives):
            if not active: continue

            s = copy(style)
            s.font_style = copy(style.font_style)
            s.content = self._list_checkboxes[index]._style.content
            self._list_checkboxes[index].focused(s)

        # Apply forcused state for buttons clicked
        for index, cb in enumerate(self._list_checkboxes):
            s = copy(style)
            s.font_style = copy(style.font_style)
            s.content = self.contents[index]
            cb.focused(s)

    def update(self):
        for index, cb in enumerate(self._list_checkboxes):
            self._list_actives[index] = cb._focused
            cb.update()
