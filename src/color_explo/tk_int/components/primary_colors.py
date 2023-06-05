import tkinter as tk
from typing import Any, Callable, List

from typing_extensions import Literal

from color_explo.tk_int.button_generator import ColorChosingButton
from color_explo.utils.color import Color
from color_explo.utils.xkcd_infos import colors_dict


class PrimaryColorBar:

    COLORS = [
        "red",
        "blood orange",
        "pumpkin orange",
        "marigold",
        "sunny yellow",
        "yellowish green",
        "green",
        "jungle green",
        "teal blue",
        "electric blue",
        "purpley",
        "warm purple",
        "hot magenta",
    ]

    def __init__(
        self, frame: tk.Frame, chosen_color: Color, update_fn: Callable, *args, **kwargs
    ):
        super().__init__(*args, **kwargs)

        self.chosen_color = chosen_color
        self.update_fn = update_fn
        self.frame = frame

        self.buttons: List[ColorChosingButton] = []
        title_frame = tk.Frame(self.frame)
        tk.Label(title_frame, text="Primary").pack(side=tk.LEFT, expand=True)
        title_frame.pack(expand=True)
        buttons_frame = tk.Frame(
            self.frame,
        )
        for rc in [colors_dict[cname] for cname in self.COLORS]:
            button = ColorChosingButton(
                master=buttons_frame,
                chosen_color=chosen_color,
                chosing_color=rc,
                update_func=self.update_fn,
                add_text=False,
            )
            button.pack(expand=True, side=tk.LEFT)
            self.buttons.append(button)
        buttons_frame.pack()
        # light_frame.pack(side=tk.LEFT)

    def update_buttons(self):
        pass
