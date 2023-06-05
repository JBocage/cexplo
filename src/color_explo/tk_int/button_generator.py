import tkinter as tk
from typing import Callable, Optional, Union

from color_explo.utils.color import Color, XKCDColor


class ColorChosingButton(tk.Button):
    def __init__(
        self,
        chosen_color: Color,
        chosing_color: Union[XKCDColor, Color],
        update_func: Callable,
        add_text: bool = True,
        *args,
        **kwargs,
    ):
        super().__init__(*args, **kwargs)
        self._chosing_color = None
        self.add_text = add_text
        self.chosen_color = chosen_color
        self.update_func = update_func

        self.chosing_color = chosing_color

    @property
    def chosing_color(self) -> Union[XKCDColor, Color]:
        return self._chosing_color

    @chosing_color.setter
    def chosing_color(self, new_value: Union[XKCDColor, Color]):
        self._chosing_color = new_value

        def on_left_click(event):
            self.chosen_color.hex = self.chosing_color.hex
            self.update_func()

        def on_right_click(event):
            if isinstance(self.chosing_color, XKCDColor):
                print(
                    f"color name='xkcd:{self.chosing_color.name}', hex='{self.chosing_color.hex}'"
                )
            else:
                print(f"hex='{self.chosing_color.hex}'")
            # print(self.chosing_color.hsv)

        if self.add_text:
            self.configure(
                bg=self.chosing_color.hex,
                text=self.chosing_color.name
                if isinstance(self.chosing_color, XKCDColor)
                else self.chosing_color.hex,
            )
        else:
            self.configure(bg=self.chosing_color.hex, height=1, width=1)

        self.bind("<Button-1>", on_left_click)
        self.bind("<Button-2>", on_right_click)
        self.bind("<Button-3>", on_right_click)
