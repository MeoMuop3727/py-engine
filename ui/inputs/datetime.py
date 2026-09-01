import pygame
from dataclasses import dataclass, field
from datetime import date
import calendar
from copy import copy

from ..ui import UserInterfaceType, CSS_StyleType
from ..actions import ButtonText, StyleButtonText, ButtonImage, StyleButtonImage
# from .textbox import TextBoxInput, StyleTextBoxInput
# from icons import Icons, icon2png
from libs.pce.systems import FontStyle, Transform, AnimationTexture, TreeAnimation
from libs.pce.utils import apply_instance

@dataclass(slots=True)
class StyleDatetime(CSS_StyleType):
    """"""
    # ---- general attribute ----
    font_style: FontStyle = field(default_factory=FontStyle)
    size_box: tuple[int, int] = (800, 350)
    rate_region: tuple[float, float] = (.6, .4)     # Include the width of space `mm/dd/yyyy` and `--:-- --`
    padding: tuple[int, int, int, int] = (10, 10, 10, 10)

    # ---- date attribute ----
    date_gap: int = 10
    date_bg_color: pygame.color.Color = (255, 255, 255, 255)
    date_border_width: int = 1
    date_border_radius: tuple[int, int, int, int] = (0, 0, 0, 0)     # Topleft - Topright - Bottomright - Bottomleft
    date_border_color: pygame.color.Color = (0, 0, 0, 255)

    # ---- date-button-choose attribute ----
    date_button_choose_bg_color: pygame.color.Color = (255, 255, 255, 255)
    date_button_choose_border_width: int = 0
    date_button_choose_border_radius: tuple[int, int, int, int] = (0, 0, 0, 0)     
    date_button_choose_border_color: pygame.color.Color = (0, 0, 0, 255)
    
    # ---- date-button attribute ----
    date_button_bg_color: pygame.color.Color = (255, 255, 255, 255)
    date_button_border_width: int = 0
    date_button_border_radius: tuple[int, int, int, int] = (0, 0, 0, 0)     
    date_button_border_color: pygame.color.Color = (0, 0, 0, 255)

    # Today
    date_today_button_bg_color: pygame.color.Color = (215, 216, 215, 255)

    # ---- time attribute ----
    time_gap: int = 10
    time_bg_color: pygame.color.Color = (255, 255, 255, 255)
    time_border_width: int = 0
    time_border_radius: tuple[int, int, int, int] = (0, 0, 0, 0)     
    time_border_color: pygame.color.Color = (0, 0, 0, 255)

    # ---- time-button attribute ----
    time_button_bg_color: pygame.color.Color = (255, 255, 255, 255)
    time_button_border_width: int = 0
    time_button_border_radius: tuple[int, int, int, int] = (0, 0, 0, 0)     
    time_button_border_color: pygame.color.Color = (0, 0, 0, 255)

    # ---- Optional buttions ----
    # 1. Reset button
    reset_button_bg_color: pygame.color.Color = (255, 255, 255, 255)
    reset_button_border_color: pygame.color.Color = (0, 0, 0, 255)
    reset_button_border_radius: tuple[int, int, int, int] = (0, 0, 0, 0)
    reset_button_border_width: int = 0
    reset_button_font_style: FontStyle = field(default_factory=FontStyle)
    # 2. Up button
    up_button_bg_color: pygame.color.Color = (255, 255, 255, 255)
    up_button_border_color: pygame.color.Color = (0, 0, 0, 255)
    up_button_border_radius: tuple[int, int, int, int] = (0, 0, 0, 0)
    up_button_border_width: int = 1
    # 2. Down button
    down_button_bg_color: pygame.color.Color = (255, 255, 255, 255)
    down_button_border_color: pygame.color.Color = (0, 0, 0, 255)
    down_button_border_radius: tuple[int, int, int, int] = (0, 0, 0, 0)
    down_button_border_width: int = 1

    # ---- TextBox Input Apply Month/Year ----
    # title_content_text_box_apply: str = "Apply Month/Year"
    # apply_box_size: tuple[int, int] = (400, 200)
    # apply_box_bg_color: pygame.color.Color = (255, 255, 255, 255)
    # apply_box_border_color: pygame.color.Color = (0, 0, 0, 255),
    # apply_box_border_width: int = 1
    # apply_box_border_radius: tuple[int, int, int, int] = (0, 0, 0, 0)
    # button_apply_bg_color: pygame.color.Color = (255, 255, 255, 255)
    # button_apply_border_color: pygame.color.Color = (0, 0, 0, 255)
    # button_apply_border_width: int = 0
    # button_apply_border_radius: tuple[int, int, int, int] = (0, 0, 0, 0)
    # button_cancle_bg_color: pygame.color.Color = (255, 255, 255, 255)
    # button_cancle_border_color: pygame.color.Color = (0, 0, 0, 255)
    # button_cancle_border_width: int = 0
    # button_cancle_border_radius: tuple[int, int, int, int] = (0, 0, 0, 0)
    # style_text_box_apply: StyleTextBoxInput = field(default_factory=StyleTextBoxInput)
    # apply_box_offset: tuple[int, int] = (50, 50)
    # apply_box_font_style: FontStyle = field(default_factory=FontStyle)
    # apply_box_padding: tuple[int, int, int, int] = (10, 10, 10, 10)

# TODO: Make Box choose month and year
# class _InputMonthYear(UserInterfaceType):
#     """"""
#     def __init__(self, surface, style=None):
#         super().__init__(surface, style, None, None, None)

#         # Datatime
#         self.__today = date.today()
#         self.__data = [self.__today.month, self.__today.year]

#         self._style: StyleDatetime = apply_instance(StyleDatetime(), style)
#         self._modified_style: StyleDatetime = apply_instance(StyleDatetime(), style)

#         # Border
#         self._border = pygame.Rect(
#             (
#                 self._modified_style.transform.position[0] - self._modified_style.apply_box_border_width + self._modified_style.apply_box_offset[0],
#                 self._modified_style.transform.position[1] - self._modified_style.apply_box_border_width + self._modified_style.apply_box_offset[1]
#             ),
#             (
#                 self._modified_style.apply_box_size[0] + self._modified_style.apply_box_border_width * 2,
#                 self._modified_style.apply_box_size[1] + self._modified_style.apply_box_border_width * 2
#             )
#         )

#         # Box
#         self._pos_box = (
#             self._modified_style.transform.position[0] + self._modified_style.apply_box_offset[0],
#             self._modified_style.transform.position[1] + self._modified_style.apply_box_offset[1]
#         )
#         self._box = pygame.Rect(
#             self._pos_box,
#             self._modified_style.apply_box_size
#         )

#         # Title
#         self._title = copy(self._modified_style.apply_box_font_style)
#         self._title.content = self._modified_style.title_content_text_box_apply

#         # Text Box Input - Month
#         _ADJUST_DISTANCE_TEXT_BOX = 25
#         self._style_text_box_month = copy(self._modified_style.style_text_box_apply)
#         self._style_text_box_month.transform = Transform(
#             position=(
#                 self._pos_box[0] + self._modified_style.padding[3],
#                 self._pos_box[1] + self._modified_style.padding[0] + self._title.get_size()[1] + _ADJUST_DISTANCE_TEXT_BOX
#             )
#         )
#         self._text_box_month = TextBoxInput(
#             surface=self._surface,
#             style=self._style_text_box_month
#         )
        
#     @property
#     def data(self) -> list[int, int]:
#         return self.__data  

#     def pressed(self, style, /):
#         self._text_box_month.pressed(copy(style).style_text_box_apply)

#     def _render(self, event: pygame.event.Event):
#         if self._modified_style.apply_box_border_width >= 0:
#             pygame.draw.rect(
#                 surface=self._surface,
#                 color=self._modified_style.apply_box_border_color,
#                 rect=self._border,
#                 border_top_left_radius=self._modified_style.apply_box_border_radius[0],
#                 border_top_right_radius=self._modified_style.apply_box_border_radius[1],
#                 border_bottom_right_radius=self._modified_style.apply_box_border_radius[2],
#                 border_bottom_left_radius=self._modified_style.apply_box_border_radius[3]
#             )

#         pygame.draw.rect(
#             surface=self._surface,
#             color=self._modified_style.apply_box_bg_color,
#             rect=self._box,
#             border_top_left_radius=self._modified_style.apply_box_border_radius[0],
#             border_top_right_radius=self._modified_style.apply_box_border_radius[1],
#             border_bottom_right_radius=self._modified_style.apply_box_border_radius[2],
#             border_bottom_left_radius=self._modified_style.apply_box_border_radius[3]
#         )

#         # Title
#         self._title.render(
#             surface=self._surface,
#             transform=Transform(
#                 position=(
#                     self._pos_box[0] + self._box.width // 2 + self._modified_style.padding[3] - self._modified_style.padding[1],
#                     self._pos_box[1] + self._title.get_size()[1] + self._modified_style.padding[0]
#                 )
#             ),
#             anchor="center"
#         )

#         # Text box
#         # 1. Month
#         self._text_box_month.update()
#         print(self._text_box_month.content)
#         # 2. Year

#     def update(self, event: pygame.event.Event):
#         self._render(event)

class DateBox(UserInterfaceType):
    """"""
    def __init__(self, surface, style=None):
        super().__init__(surface, style, None, None, None)

        self.__click_locked = False     # Prevent multi-trigger when rebuild calender grid
                                        # It will lock immediate to prevent all other triggers until mouse is unpressed

        # ==== Current day ====
        self.__today = date.today()

        # ==== Datatime ==== 
        self.__day = self.__today.day
        self.__month = self.__today.month
        self.__year = self.__today.year 
        self.__datatime = [self.__month, self.__day, self.__year]

        # ==== Cached datatime mm/yyyy ====
        # 1. Month
        self.__cached_month_current = self.__today.month
        # 2. Year
        self.__cached_year_current = self.__today.year   

        # Margin top
        # Distance among buttons choose mm/yyyy, dd and option buttons
        self._margin_top = 10

        self._style: StyleDatetime = apply_instance(StyleDatetime(), style)
        self._modified_style: StyleDatetime = apply_instance(StyleDatetime(), style)

        # ==== Date box ====
        _size_date_box = (
            int(self._modified_style.size_box[0] * self._modified_style.rate_region[0]),
            self._modified_style.size_box[1]
        )
        self._date_box = pygame.Rect(self._modified_style.transform.position, _size_date_box)

        #  ==== The max width in the frame days, eg Su, Mo, Tu, ... ====
        self._max_width_frame_days = self._date_box.width - (self._modified_style.padding[1] + self._modified_style.padding[3])

        # ==== Border ====
        self._border = pygame.Rect(
            (
                self._modified_style.transform.position[0] - self._modified_style.date_border_width,
                self._modified_style.transform.position[1] - self._modified_style.date_border_width
            ),
            (
                _size_date_box[0] + self._modified_style.date_border_width * 2,
                _size_date_box[1] + self._modified_style.date_border_width * 2
            )
        )

        # ==== Button choose mm/yyyy ====
        self._size_button_choose_date = (100, 50)
        self._button_choose_date = ButtonText(
            surface=self._surface,
            style=StyleButtonText(
                transform=Transform(
                    position=(
                        self._modified_style.transform.position[0] + self._modified_style.padding[3],
                        self._modified_style.transform.position[1] + self._modified_style.padding[0]
                    )
                ),
                content=f"{self.__month}/{self.__year}",
                font_style=copy(self._modified_style.font_style),
                size_button=self._size_button_choose_date,
                bg_color=self._modified_style.date_button_choose_bg_color,
                border_radius=self._modified_style.date_button_choose_border_radius,
                border_width=self._modified_style.date_button_choose_border_width,
                border_color=self._modified_style.date_button_choose_border_color
            )
        )

        # ==== Label all days in a week ====
        self._list_days: list[ButtonText] = self.__apply_list_days()

        # ==== Calendar grid ====
        self._calendar_grid: list[list[ButtonText]] = self.__apply_calender_grid()

        # ==== Buttons option ====

        # 1. Button reset
        self._button_reset_date_to_default = ButtonText(
            surface=self._surface,
            style=StyleButtonText(
                transform=Transform(
                    position=(
                        self._modified_style.transform.position[0] + self._modified_style.padding[3],
                        _size_date_box[1] - self._modified_style.padding[2] + 50
                    )
                ),
                content="Reset",
                font_style=self._modified_style.reset_button_font_style,
                size_button=(100, 50),
                bg_color=self._modified_style.reset_button_bg_color,
                border_color=self._modified_style.reset_button_border_color,
                border_radius=self._modified_style.reset_button_border_radius,
                border_width=self._modified_style.reset_button_border_width
            )
        )
        self._button_reset_date_to_default.func = lambda: self.__reset_date_into_default_date()

        # 2. Button UP/DOWN
        _size_icon = 32
        _gap_btn_arrow = 10
        _ADJUST_POS_BUTTONS_UP_DOWN = 65
        # 2.1. Button - arrow up
        self._button_arrow_up = ButtonText(
            surface=self._surface,
            style=StyleButtonText(
                transform=Transform(
                    position=(
                        _size_date_box[0] - self._modified_style.padding[1] - _size_icon - _gap_btn_arrow + _ADJUST_POS_BUTTONS_UP_DOWN,
                        self._modified_style.transform.position[1] + self._modified_style.padding[1]
                    )
                ),
                content="U",
                font_style=copy(self._modified_style.font_style),
                size_button=(_size_icon, _size_icon),
                border_width=self._modified_style.up_button_border_width,
                border_color=self._modified_style.up_button_border_color,
                border_radius=self._modified_style.up_button_border_radius,
                bg_color=self._modified_style.up_button_bg_color
            )
        )
        self._button_arrow_up.func = lambda: self.__increase_month()
        # 2.2. Button - arrow down
        self._button_arrow_down = ButtonText(
            surface=self._surface,
            style=StyleButtonText(
                transform=Transform(
                    position=(
                        _size_date_box[0] - self._modified_style.padding[1] + _ADJUST_POS_BUTTONS_UP_DOWN,
                        self._modified_style.transform.position[1] + self._modified_style.padding[1]
                    )
                ),
                content="D",
                font_style=copy(self._modified_style.font_style),
                size_button=(_size_icon, _size_icon),
                border_width=self._modified_style.down_button_border_width,
                border_color=self._modified_style.down_button_border_color,
                border_radius=self._modified_style.down_button_border_radius,
                bg_color=self._modified_style.down_button_bg_color
            )
        )
        self._button_arrow_down.func = lambda: self.__decrease_month()

    @property
    def datatime(self) -> list[int, int, int]:
        return self.__datatime
    
    # Refesh UI DateBox
    def _refesh(self):
        # Update cached
        self.__cached_month_current = self.__month
        self.__cached_year_current = self.__year

        # Update new mm/yyyy for button choose date
        self._button_choose_date._style.content = f"{self.__month}/{self.__year}"
        self._button_choose_date._modified_style.content = f"{self.__month}/{self.__year}"

        # Update new days in calender
        self._calendar_grid = self.__apply_calender_grid()

    # Increase month/year (Button arrow up)
    def __increase_month(self):
        self.__click_locked = True

        self.__month += 1

        if self.__month > 12:
            self.__month = 1
            self.__year += 1

        self.__datatime[0] = self.__month
        self.__datatime[2] = self.__year

        self._refesh()

    # Decrease month/year (Button arrow down)
    def __decrease_month(self):
        self.__click_locked = True

        self.__month -= 1

        if self.__month < 1:
            self.__month = 12
            self.__year -= 1

        self.__datatime[0] = self.__month
        self.__datatime[2] = self.__year

        self._refesh()

    # Reset date into default date
    def __reset_date_into_default_date(self):
        self.__click_locked = True

        # Reset to default
        self.__day = self.__today.day
        self.__month = self.__today.month
        self.__year = self.__today.year

        self._refesh()

    # Func write data time
    def __write_day_month_year(self, daymonth: dict):
        self.__click_locked = True      

        self.__day = daymonth["day"]

        month = self.__cached_month_current + daymonth["month_offset"]
        year = self.__cached_year_current 

        year += (month - 1) // 12
        month = (month - 1) % 12 + 1

        self.__month = month
        self.__year = year

        self.__datatime = [self.__month, self.__day, self.__year]

        # current_month is False
        if daymonth["month_offset"] != 0:
            self._refesh()

    @staticmethod
    def first_weekday_sunday_based(year: int, month: int) -> int:
        """ 0 = Sunday, 1 = Monday, ..., 6 = Saturday """
        wd = date(year, month, 1).weekday()     # Python: 0=Mon, ..., 6=Sun
        return (wd + 1) % 7                     # Transform to 0=Sun, ..., 6=Sat

    def __build_calendar_grid(self, year: int, month: int) -> list[list[dict]]:
        # The number of days in the current month
        days_in_month = calendar.monthrange(year, month)[1]

        # Day of the week, day 1, (0=Sunday ... 6=Saturday)
        start_weekday = self.first_weekday_sunday_based(year, month)

        # 1. Start date of the period (end of last month) 
        prev_month = month - 1 if month > 1 else 12
        prev_year = year if month > 1 else year - 1
        days_in_prev_month = calendar.monthrange(prev_year, prev_month)[1]

        leading_days = [
            {"day": days_in_prev_month - i, "current_month": False, "month_offset": -1}
            for i in range(start_weekday - 1, -1, -1)
        ]

        # 2. Day of the current month
        current_days = [
            {"day": d, "current_month": True, "month_offset": 0}
            for d in range(1, days_in_month + 1)
        ]

        # 3. Faded date at the bottom of the table (start of the following month): fill in to complete the multiple of 7.
        total_so_far = len(leading_days) + len(current_days)
        trailing_count = (7 - total_so_far % 7) % 7

        if trailing_count == 0: 
            trailing_count += 7

        trailing_days = [
            {"day": i + 1, "current_month": False, "month_offset": 1}
            for i in range(trailing_count)
        ]

        all_days = leading_days + current_days + trailing_days

        # 4. Divide into 7-day rows.
        grid = [all_days[i:i+7] for i in range(0, len(all_days), 7)]

        return grid

    def __apply_calender_grid(self) -> list[list[ButtonText]]:
        calen = self.__build_calendar_grid(self.__year, self.__month)

        calender_grid: list[list[ButtonText]] = []

        cell_size = (self._max_width_frame_days // 7, 32)

        for row_idx, row in enumerate(calen):
            list_row_days: list[ButtonText] = []

            for col_idx, cell in enumerate(row):
                cx = self._modified_style.transform.position[0] - (self._modified_style.padding[1] + self._modified_style.padding[3]) + (col_idx) * cell_size[0] + cell_size[0] // 2
                cy = self._modified_style.transform.position[1] + self._modified_style.padding[0] + self._size_button_choose_date[1] + self._margin_top + (row_idx + 1) * cell_size[1]

                is_today = self.__today.day is not None and cell["current_month"] and cell["day"] == self.__today.day

                if is_today:
                    list_row_days.append(ButtonText(
                        surface=self._surface,
                        style=StyleButtonText(
                            transform=Transform(
                                position=(cx, cy)
                            ),
                            content=f"{cell["day"]}",
                            font_style=copy(self._modified_style.font_style),
                            size_button=cell_size,
                            bg_color=self._modified_style.date_today_button_bg_color
                        )
                    ))
                else:
                    list_row_days.append(ButtonText(
                        surface=self._surface,
                        style=StyleButtonText(
                            transform=Transform(
                                position=(cx, cy)
                            ),
                            content=f"{cell["day"]}",
                            font_style=copy(self._modified_style.font_style),
                            size_button=cell_size,
                            bg_color=self._modified_style.date_button_bg_color
                        )
                    ))

                # Apply func write data time for all date buttons
                list_row_days[-1].func = lambda dm=cell: self.__write_day_month_year(dm)

            calender_grid.append(list_row_days)

        return calender_grid

    def __apply_list_days(self) -> list[ButtonText]:
        list_days: list[ButtonText] = []

        days = ["Su", "Mo", "Tu", "We", "Th", "Fr", "Sa"]
        size_button = (self._max_width_frame_days // 7, 32)

        for index, day in enumerate(days):
            list_days.append(ButtonText(
                surface=self._surface,
                style=StyleButtonText(
                    transform=Transform(
                        position=(
                            self._modified_style.transform.position[0] + self._modified_style.padding[3] + size_button[0] * index,
                            self._modified_style.transform.position[1] + self._modified_style.padding[0] + self._size_button_choose_date[1] + self._margin_top
                        )
                    ),
                    content=day,
                    size_button=size_button,
                    font_style=copy(self._modified_style.font_style)
                )
            ))

        return list_days

    def _render(self):
        if self._modified_style.date_border_width >= 0:
            pygame.draw.rect(
                surface=self._surface,
                color=self._modified_style.date_border_color,
                rect=self._border,
                border_top_left_radius=self._modified_style.date_border_radius[0],
                border_top_right_radius=self._modified_style.date_border_radius[1],
                border_bottom_right_radius=self._modified_style.date_border_radius[2],
                border_bottom_left_radius=self._modified_style.date_border_radius[3]
            )

        pygame.draw.rect(
            surface=self._surface,
            color=self._modified_style.date_bg_color,
            rect=self._date_box,
            border_top_left_radius=self._modified_style.date_border_radius[0],
            border_top_right_radius=self._modified_style.date_border_radius[1],
            border_bottom_right_radius=self._modified_style.date_border_radius[2],
            border_bottom_left_radius=self._modified_style.date_border_radius[3]
        )

        # Button choose date
        self._button_choose_date.update()

        # Button ARROW UP/ARROW DOWN
        self._button_arrow_up.update()
        self._button_arrow_down.update()

        # List days
        for day in self._list_days:
            day.update() 

        # Calender
        for r in self._calendar_grid:
            for c in r:
                c.update() 

        # Optional buttons
        # 1. Reset button
        self._button_reset_date_to_default.update()  

    def hovered(self, style, /):
        if not isinstance(style, CSS_StyleType):
            raise TypeError(f"The value must be CSS_StyleType, not {type(style).__name__!r}")

        # Apply state hovered for date buttons
        for r in self._calendar_grid:
            for day in r:
                day.hovered(StyleButtonText(
                    transform=style.transform,
                    content=f"{day._style.content}",
                    font_style=copy(style.font_style),
                    size_button=day._style.size_button,
                    bg_color=style.date_button_bg_color,
                    border_width=style.date_button_border_width,
                    border_color=style.date_button_border_color,
                    border_radius=style.date_button_border_radius
                ))

        # Apply state hovered for choosing date button 
        self._button_choose_date.hovered(StyleButtonText(
            transform=style.transform,
            content=f"{self._button_choose_date._style.content}",
            font_style=copy(style.font_style),
            size_button=self._size_button_choose_date,
            bg_color=style.date_button_choose_bg_color,
            border_color=style.date_button_choose_border_color,
            border_radius=style.date_button_choose_border_radius,
            border_width=style.date_button_choose_border_width
        ))

    def pressed(self, style, /):
        if not isinstance(style, CSS_StyleType):
            raise TypeError(f"The value must be CSS_StyleType, not {type(style).__name__!r}")

        is_mouse_down = pygame.mouse.get_pressed()[0]

        # If the mouse was unpressed -> Unlock to allow the next click
        if not is_mouse_down:
            self.__click_locked = False

        # Apply pressed state pressed for date buttons
        # If it is being locked (just has trigger once) -> pass 
        if not self.__click_locked:
            for r in self._calendar_grid:
                for day in r:
                    day.pressed(StyleButtonText(
                        transform=style.transform,
                        content=f"{day._style.content}",
                        font_style=copy(style.font_style),
                        size_button=day._style.size_button,
                        bg_color=style.date_button_bg_color,
                        border_width=style.date_button_border_width,
                        border_color=style.date_button_border_color,
                        border_radius=style.date_button_border_radius
                    ))

        # Apply pressed state for choosing date button 
        self._button_choose_date.pressed(StyleButtonText(
            transform=style.transform,
            content=f"{self._button_choose_date._style.content}",
            font_style=copy(style.font_style),
            size_button=self._size_button_choose_date,
            bg_color=style.date_button_choose_bg_color,
            border_color=style.date_button_choose_border_color,
            border_radius=style.date_button_choose_border_radius,
            border_width=style.date_button_choose_border_width
        ))

        # Apply pressed state for reset button
        self._button_reset_date_to_default.pressed(
            StyleButtonText(
                transform=style.transform,
                content=f"{self._button_reset_date_to_default._style.content}",
                font_style=copy(style.font_style),
                size_button=self._button_reset_date_to_default.size_button,
                bg_color=style.reset_button_bg_color,
                border_color=style.reset_button_border_color,
                border_radius=style.reset_button_border_radius,
                border_width=style.reset_button_border_width
            )
        )

        # Apply pressed state for UP/DOWN button
        # 1. UP Button
        self._button_arrow_up.pressed(
            StyleButtonText(
                transform=style.transform,
                content=f"{self._button_arrow_up._style.content}",
                font_style=copy(style.font_style),
                size_button=self._button_arrow_up.size_button,
                bg_color=style.up_button_bg_color,
                border_color=style.up_button_border_color,
                border_radius=style.up_button_border_radius,
                border_width=style.up_button_border_width
            )
        )
        # 2. DOWN Button
        self._button_arrow_down.pressed(
            StyleButtonText(
                transform=style.transform,
                content=f"{self._button_arrow_down._style.content}",
                font_style=copy(style.font_style),
                size_button=self._button_arrow_down.size_button,
                bg_color=style.down_button_bg_color,
                border_color=style.down_button_border_color,
                border_radius=style.down_button_border_radius,
                border_width=style.down_button_border_width
            )
        )

    def update(self):
        self._render()

# TODO: Make TimeBox
# class TimeBox(UserInterfaceType):
#     def __init__(self, surface, style = None):
#         super().__init__(surface, style, None, None, None)
