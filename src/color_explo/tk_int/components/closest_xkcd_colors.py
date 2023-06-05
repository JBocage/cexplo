import random as rd
import tkinter as tk
from typing import Any, Callable, List

from typing_extensions import Literal

from color_explo.tk_int.button_generator import ColorChosingButton
from color_explo.utils.color import Color
from color_explo.utils.xkcd_infos import colors_dict


class ClosestXKCDColorsFrame:

    N_ROWS = 6
    N_COLS = 2

    def __init__(
        self, frame: tk.Frame, chosen_color: Color, update_fn: Callable, *args, **kwargs
    ):
        super().__init__(*args, **kwargs)

        self.chosen_color = chosen_color
        self.update_fn = update_fn
        self.frame = frame

        self.buttons: List[ColorChosingButton] = []
        title_frame = tk.Frame(self.frame)
        tk.Label(title_frame, text="Random Colors").pack(side=tk.LEFT, expand=True)
        title_frame.pack(expand=True)
        buttons_frame = tk.Frame(self.frame)
        for row_id in range(self.N_ROWS):
            buttons_row_frame = tk.Frame(buttons_frame)
            for rc in chosen_color.get_light_palette(n=self.N_COLS):
                button = ColorChosingButton(
                    master=buttons_row_frame,
                    chosen_color=chosen_color,
                    chosing_color=rc,
                    update_func=self.update_fn,
                    add_text=False,
                )
                button.pack(expand=True, side=tk.LEFT)
                self.buttons.append(button)
            buttons_row_frame.pack()
        buttons_frame.pack()

    def update_buttons(self):
        for color_var, button in zip(
            rd.sample(list(colors_dict.values()), self.N_COLS * self.N_ROWS),
            self.buttons,
        ):
            button.chosing_color = color_var
