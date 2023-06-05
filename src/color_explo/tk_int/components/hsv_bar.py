import tkinter as tk
from typing import Any, Callable, List

from typing_extensions import Literal

from color_explo.tk_int.button_generator import ColorChosingButton
from color_explo.utils.color import Color


class HSVBar:

    N_CHOICES = 7

    def __init__(
        self, frame: tk.Frame, chosen_color: Color, update_fn: Callable, *args, **kwargs
    ):
        super().__init__(*args, **kwargs)

        self.chosen_color = chosen_color
        self.update_fn = update_fn
        self.frame = frame

        self.light_buttons: List[ColorChosingButton] = []
        light_frame = tk.Frame(self.frame)
        title_frame = tk.Frame(light_frame)
        tk.Label(title_frame, text="Light").pack(side=tk.LEFT, expand=True)
        title_frame.pack(expand=True)
        buttons_frame = tk.Frame(
            light_frame,
        )
        for rc in chosen_color.get_light_palette(n=self.N_CHOICES):
            button = ColorChosingButton(
                master=buttons_frame,
                chosen_color=chosen_color,
                chosing_color=rc,
                update_func=self.update_fn,
                add_text=False,
            )
            button.pack(expand=True, side=tk.LEFT)
            self.light_buttons.append(button)
        buttons_frame.pack()
        light_frame.pack(side=tk.LEFT)

        self.sat_buttons: List[ColorChosingButton] = []
        sat_frame = tk.Frame(self.frame)
        title_frame = tk.Frame(sat_frame)
        tk.Label(title_frame, text="Saturation").pack(side=tk.LEFT, expand=True)
        title_frame.pack(expand=True)
        buttons_frame = tk.Frame(
            sat_frame,
        )
        for rc in chosen_color.get_sat_palette(n=self.N_CHOICES):
            button = ColorChosingButton(
                master=buttons_frame,
                chosen_color=chosen_color,
                chosing_color=rc,
                update_func=self.update_fn,
                add_text=False,
            )
            button.pack(expand=True, side=tk.LEFT)
            self.sat_buttons.append(button)
        buttons_frame.pack()
        sat_frame.pack(side=tk.LEFT)

    def update_buttons(self):
        for color_var, button in zip(
            self.chosen_color.get_light_palette(self.N_CHOICES), self.light_buttons
        ):
            button.chosing_color = color_var
        for color_var, button in zip(
            self.chosen_color.get_sat_palette(self.N_CHOICES), self.sat_buttons
        ):
            button.chosing_color = color_var
