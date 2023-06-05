import tkinter as tk
from typing import Callable

from color_explo.utils.color import Color


def make_top_bar(
    master: tk.Tk,
    update_app: Callable,
    chosen_color: Color,
) -> tk.Tk:
    def lighten():
        chosen_color.lighten()
        update_app()

    def darken():
        chosen_color.darken()
        update_app()

    def increase_sat():
        chosen_color.increase_sat()
        update_app()

    def decrease_sat():
        chosen_color.decrease_sat()
        update_app()

    btn_darken = tk.Button(master=master, command=darken, text="light [-]")
    btn_darken.pack(side=tk.LEFT)
    btn_lighten = tk.Button(master=master, command=lighten, text="light [+]")
    btn_lighten.pack(side=tk.LEFT)
    btn_sat_dec = tk.Button(master=master, command=decrease_sat, text="sat [-]")
    btn_sat_dec.pack(side=tk.LEFT)
    btn_sat_inc = tk.Button(master=master, command=increase_sat, text="sat [+]")
    btn_sat_inc.pack(side=tk.LEFT)

    return {
        "light-": btn_darken,
        "light+": btn_lighten,
        "sat-": btn_sat_dec,
        "sat+": btn_sat_inc,
    }
