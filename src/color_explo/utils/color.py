from __future__ import annotations

from colorsys import hsv_to_rgb, rgb_to_hsv
from typing import List, Optional, Tuple, Union

import numpy as np

from color_explo.utils.color_fmt_conversion import hex_to_rgb, rgb_to_hex

RGBTuple = Tuple[int, int, int]
HSVTuple = Tuple[float, float, float]
HexString = str


class BaseColor(object):
    def __init__(self, hex_or_rgb_color: Union[HexString, RGBTuple]) -> None:

        if isinstance(hex_or_rgb_color, str):
            self.hex = hex_or_rgb_color
        else:
            self.rgb = hex_or_rgb_color

    @property
    def rgb(self) -> RGBTuple:
        return hex_to_rgb(self.hex)

    @rgb.setter
    def rgb(self, new_value: RGBTuple) -> None:
        self.hex = rgb_to_hex(new_value)

    @property
    def hsv(self) -> HSVTuple:
        return rgb_to_hsv(*self.rgb)

    @hsv.setter
    def hsv(self, new_value: HSVTuple):
        h, s, v = new_value
        if not 0 <= h <= 1:
            raise ValueError()

        if not 0 <= s <= 1:
            raise ValueError()

        if not 0 <= v <= 255 and isinstance(v, int):
            raise ValueError()

        self.rgb = tuple([int(v) for v in hsv_to_rgb(*new_value)])

    def rgb_dist(color1: Color, color2: Color):
        r1, g1, b1 = color1.rgb
        r2, g2, b2 = color2.rgb
        return ((r1 - r2) ** 2 + (g1 - g2) ** 2 + (b1 - b2) ** 2) ** 0.5

    def copy(self) -> BaseColor:
        return BaseColor(self.hex)

    def get_light_palette(self, n=5) -> List[BaseColor]:
        h, s, _ = self.hsv
        return [
            BaseColor(tuple([int(v) for v in hsv_to_rgb(h, s, int(v_step))]))
            for v_step in np.linspace(0, 255, n)
        ]

    def get_sat_palette(self, n=5) -> List[BaseColor]:
        h, _, v = self.hsv
        return [
            BaseColor(tuple([int(v) for v in hsv_to_rgb(h, s_step, v)]))
            for s_step in np.linspace(0, 1, n)
        ]


class Color(BaseColor):
    def darken(self, darken_step=0.1) -> Color:
        h, s, v = self.hsv
        v = max(0, v - int(255 * darken_step))
        self.hsv = (h, s, v)
        return self

    def lighten(self, lighten_step=0.1) -> Color:
        h, s, v = self.hsv
        v = min(255, v + int(255 * lighten_step))
        self.hsv = (h, s, v)
        return self

    def increase_sat(self, rate=0.1) -> Color:
        h, s, v = self.hsv
        s = min(s + rate, 1)
        self.hsv = (h, s, v)
        return self

    def decrease_sat(self, rate=0.1) -> Color:
        h, s, v = self.hsv
        s = max(s - rate, 0)
        self.hsv = (h, s, v)
        return self

    def get_light_palette(self, n=5) -> List[Color]:
        return [Color(c.hex) for c in super().get_light_palette(n)]

    def get_sat_palette(self, n=5) -> List[Color]:
        return [Color(c.hex) for c in super().get_sat_palette(n)]

    def copy(self) -> Color:
        return Color(self.hex)


class XKCDColor(Color):
    def __init__(self, hex_or_rgb_color: HexString | RGBTuple, name: str) -> None:
        super().__init__(hex_or_rgb_color)
        self.name = name

    def get_light_palette(self, n=5) -> List[Color]:
        return [Color(c.hex) for c in super().get_light_palette(n)]

    def get_sat_palette(self, n=5) -> List[Color]:
        return [Color(c.hex) for c in super().get_sat_palette(n)]

    def copy(self) -> XKCDColor:
        return XKCDColor(self.hex, self.name)

    @staticmethod
    def get_nclosest_xkcd_colors(n: int, color: Color) -> List[XKCDColor]:
        from color_explo.utils.xkcd_infos import colors_dict

        xkcd_colors_dist_tuples = sorted(
            [(c, c.rgb_dist(color)) for c in colors_dict.values()], key=lambda t: t[1]
        )
        return [c for c, _ in xkcd_colors_dist_tuples[:n]]
