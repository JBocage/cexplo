import random as rd
import tkinter as tk
import tkinter.colorchooser
from ast import Dict
from typing import List, Optional

from color_explo.tk_int.button_generator import ColorChosingButton
from color_explo.tk_int.components.closest_colors import ClosestColorsFrame
from color_explo.tk_int.components.hsv_bar import HSVBar
from color_explo.tk_int.components.primary_colors import PrimaryColorBar
from color_explo.tk_int.components.random_colors import RandomColorsFrame
from color_explo.tk_int.make_top_bar import make_top_bar
from color_explo.utils.color import Color, XKCDColor
from color_explo.utils.xkcd_infos import colors_dict


def main():
    root = tk.Tk()
    root.title("CPKR")
    # root.geometry("300x150")

    color_chosing_frame = tk.Frame(root)

    chosen_color = Color("#000000")

    buttons: List[ColorChosingButton] = []

    primary_colors: Optional[PrimaryColorBar] = None
    hsvbar: Optional[HSVBar] = None
    random_colors: Optional[RandomColorsFrame] = None
    closest_colors: Optional[ClosestColorsFrame] = None

    middle_frame = tk.Frame(root, name="middle_frame")

    def update_app():
        nonlocal root, chosen_color, color_chosing_frame, hsvbar, random_colors, closest_colors, primary_colors
        root.configure(bg=chosen_color.hex)

        # Init
        if primary_colors is None:
            primary_colors = PrimaryColorBar(
                frame=tk.Frame(root, name="primary_colors"),
                chosen_color=chosen_color,
                update_fn=update_app,
            )
        if hsvbar is None:
            hsvbar = HSVBar(
                frame=tk.Frame(root, name="frm_hsv"),
                chosen_color=chosen_color,
                update_fn=update_app,
            )
        if random_colors is None:
            random_colors = RandomColorsFrame(
                frame=tk.Frame(middle_frame, name="random_colors"),
                chosen_color=chosen_color,
                update_fn=update_app,
            )
        if closest_colors is None:
            closest_colors = ClosestColorsFrame(
                frame=tk.Frame(middle_frame, name="closest_colors"),
                chosen_color=chosen_color,
                update_fn=update_app,
            )

        hsvbar.update_buttons()
        random_colors.update_buttons()
        closest_colors.update_buttons()

    update_app()

    hsvbar: HSVBar
    random_colors: RandomColorsFrame
    primary_colors.frame.pack()
    hsvbar.frame.pack()
    random_colors.frame.pack(side=tk.LEFT)
    closest_colors.frame.pack(side=tk.LEFT)
    middle_frame.pack()

    root.mainloop()
