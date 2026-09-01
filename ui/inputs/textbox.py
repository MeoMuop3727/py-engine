import pygame
from copy import copy
from dataclasses import dataclass, field
from typing import Optional

from libs.pce.systems import FontStyle, Transform
from libs.pce.utils import apply_instance
from ..ui import UserInterfaceType, CSS_StyleType
from utils import apply_value

@dataclass(slots=True)
class StyleTextBoxInput(CSS_StyleType):
    """"""
    font_style: FontStyle = field(default_factory=FontStyle)
    size_box: tuple[int, int] = (500, 500)
    bg_color: pygame.color.Color = (255, 255, 255, 255)
    border_width: int = 1
    border_radius: tuple[int, int, int, int] = (0, 0, 0, 0)             # Topleft - Topright - Bottomright - Bottomleft
    border_color: pygame.color.Color = (0, 0, 0, 255)
    padding: tuple[int, int, int, int] = (10, 10, 10, 10)               # Top - Right - Bottom - Left
    cursor_width: int = 5
    cursor_color: pygame.color.Color = (0, 0, 0, 255)
    cursor_border_radius: tuple[int, int, int, int] = (0, 0, 0, 0)      # Topleft - Topright - Bottomright - Bottomleft
    cursor_time_show: float = 1.
    line_height: int = 12
    typing_speed: float = 30.                                           # The number of chars will appear in one second

class TextBoxInput(UserInterfaceType):
    """"""
    def __init__(self, surface, style = None):
        super().__init__(surface, style, None, None, None)

        # TODO: Two vars use in _get_wrapped_text()
        self._cached_wrapped_text = None
        self._cached_visible_chars = -1

        self._pressed = False
        self._focused = False

        self._content = ""
        self._visible_chars: float = 0.

        self._style: StyleTextBoxInput = apply_instance(StyleTextBoxInput(), style)
        self._modified_style: StyleTextBoxInput = apply_instance(StyleTextBoxInput(), style)

        # Font
        # Just assign to get size of the font
        # So the content is not necessary
        self._style.font_style.content = "a"
        self._modified_style.font_style.content = "a"

        # Box
        self._box = pygame.Rect(self._modified_style.transform.position, self._modified_style.size_box)

        # Border
        self._border = pygame.Rect(
            (
                self._modified_style.transform.position[0] - self._modified_style.border_width,
                self._modified_style.transform.position[1] - self._modified_style.border_width
            ), 
            (
                self._modified_style.size_box[0] + self._modified_style.border_width * 2,
                self._modified_style.size_box[1] + self._modified_style.border_width * 2
            )
        )

        # Cursor
        self._elapsed_time = 0.0
        self._visible_cursor = False    # To render the cursor onto the screen
        self._cursor_show = True        # To apply appear - disappear animation of the cursor
        self._position_cursor = (
            self._modified_style.transform.position[0] + self._modified_style.padding[3],
            self._modified_style.transform.position[1] + self._modified_style.padding[0]
        )
        self._size_cursor = (self._modified_style.cursor_width, self._modified_style.font_style.get_size()[1])
        self._cursor = pygame.Rect(self._position_cursor, self._size_cursor)

    @property
    def content(self) -> str:
        return self._content
    
    def input(self, input: pygame.event.Event):
        if not self._focused: return

        if input.type == pygame.KEYDOWN:
            if input.key == pygame.K_BACKSPACE:
                self._content = self._content[:-1]
            elif input.key in (pygame.K_RETURN, pygame.K_KP_ENTER):
                self._content += "\n"
            else:
                self._content += input.unicode

    # TODO: Will consider later, complete to optimize the performane to avoid decreasing FPS
    # def _get_wrapped_text(self) -> list[str]:
    #     if self._cached_visible_chars != int(self._visible_chars):
    #         self._cached_visible_chars = int(self._visible_chars)
    #         self._cached_wrapped_text = self.wrap_content(self._content[:self._cached_visible_chars])
    #     return self._cached_wrapped_text

    def wrap_content(self, content: Optional[str] = None) -> list[str]:
        content = apply_value(self._content, content)

        s = copy(self._style.font_style)    # The copy font style, to get the size of font
        current_txt: str = ""               # To restore the content, it will reset until the length >= max_length
        list_wrapped_text: list[str] = []

        # size_box_x - (padding_right + padding_left)
        max_length = self._modified_style.size_box[0] - (self._modified_style.padding[1] + self._modified_style.padding[3])

        for _, word in enumerate(self._content.split()):
            temp_txt = word if not current_txt else current_txt + " " + word
            s.content = temp_txt
            w = s.get_size()[0]

            if w >= max_length:
                list_wrapped_text.append(current_txt)
                current_txt = word
            else:
                current_txt = temp_txt

        if current_txt:
            list_wrapped_text.append(current_txt)

        return list_wrapped_text

    def hovered(self, style, /):
        if not isinstance(style, CSS_StyleType):
            raise TypeError(f"The value must be CSS_StyleType, not {type(style).__name__!r}")
        
        mouse_pos = pygame.mouse.get_pos()

        is_hover = self._box.collidepoint(mouse_pos) or self._border.collidepoint(mouse_pos)

        if not is_hover:
            self._modified_style = self._style
        else:
            self._modified_style = style

    def pressed(self, style, /):
        if not isinstance(style, CSS_StyleType):
            raise TypeError(f"The value must be CSS_StyleType, not {type(style).__name__!r}")
        
        mouse_pos = pygame.mouse.get_pos()
        
        is_hover = self._box.collidepoint(mouse_pos) or self._border.collidepoint(mouse_pos)
        is_pressed = pygame.mouse.get_pressed()[0]

        if not is_hover:
            if is_pressed:
                self._focused = False

            self._modified_style = self._style
            self._pressed = False
        elif is_hover and is_pressed:
            if not self._pressed:
                self._pressed = True
                self._focused = True

            self._modified_style = style

        if self._focused: 
            self._visible_cursor = True
        else:
            self._visible_cursor = False
    
    def focused(self, style, /):
        if not isinstance(style, CSS_StyleType):
            raise TypeError(f"The value must be CSS_StyleType, not {type(style).__name__!r}")

        if not self._focused: 
            self._modified_style = self._style
        else:
            self._modified_style = style

    def _render(self):
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
            rect=self._box,
            border_top_left_radius=self._modified_style.border_radius[0],
            border_top_right_radius=self._modified_style.border_radius[1],
            border_bottom_right_radius=self._modified_style.border_radius[2],
            border_bottom_left_radius=self._modified_style.border_radius[3]
        )

        # LOGIC: Typewriter effect
        visible_content = self._content[:int(self._visible_chars)]
        wrapped_text = self.wrap_content(visible_content)
        line_h = 0

        if wrapped_text:
            line_h = self._style.font_style.get_size()[1]

            for r, txt in enumerate(wrapped_text):
                s = copy(self._style.font_style)
                s.content = txt
                s.render(
                    surface=self._surface,
                    transform=Transform(
                        position=(
                            self._modified_style.transform.position[0] + self._modified_style.padding[0],
                            self._modified_style.transform.position[1] + (line_h + self._modified_style.line_height) * r + self._modified_style.padding[3]
                        )
                    ),
                    anchor="topleft"
                ) 

        # LOGIC: Moving cursor effect
        if wrapped_text:
            last_line_index = len(wrapped_text) - 1
            last_line_text = wrapped_text[last_line_index]   

            s = copy(self._style.font_style)
            s.content = last_line_text
            last_line_width = s.get_size()[0] 
        else:
            last_line_index = 0
            last_line_width = 0

        cursor_x = self._modified_style.transform.position[0] + self._modified_style.padding[3] + last_line_width
        cursor_y = self._modified_style.transform.position[1] + (line_h + self._modified_style.line_height) * last_line_index + self._modified_style.padding[0]

        self._position_cursor = (cursor_x, cursor_y)
        self._cursor = pygame.Rect(self._position_cursor, self._size_cursor)

        if self._visible_cursor and self._cursor_show:
            pygame.draw.rect(
                surface=self._surface,
                color=self._modified_style.cursor_color,
                rect=self._cursor,
                border_top_left_radius=self._modified_style.cursor_border_radius[0],
                border_top_right_radius=self._modified_style.cursor_border_radius[1],
                border_bottom_right_radius=self._modified_style.cursor_border_radius[2],
                border_bottom_left_radius=self._modified_style.cursor_border_radius[3]
            )

    def update(self, dt: float = .05, speed: float = 1.):
        # Typewriter effect
        if self._visible_chars < len(self._content):
            self._visible_chars += self._modified_style.typing_speed * dt * speed
            self._visible_chars = min(self._visible_chars, len(self._content))

        # Cursor blink
        if self._visible_cursor:
            self._elapsed_time += dt * speed
            if self._elapsed_time >= self._modified_style.cursor_time_show:
                self._elapsed_time = 0.
                self._cursor_show = not self._cursor_show

        self._render()
