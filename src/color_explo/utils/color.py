from __future__ import annotations

from colorsys import hsv_to_rgb, rgb_to_hsv
from typing import Optional, Tuple, Union

from color_explo.utils.color_fmt_conversion import hex_to_rgb, rgb_to_hex

RGBTuple = Tuple[int, int, int]
HSVTuple = Tuple[float, float, float]
HexString = str


class Color(object):
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

        self.rgb = tuple([int(v) for v in hsv_to_rgb(*new_value)])

    def rgb_dist(color1: Color, color2: Color):
        r1, g1, b1 = color1.rgb
        r2, g2, b2 = color2.rgb
        return ((r1 - r2) ** 2 + (g1 - g2) ** 2 + (b1 - b2) ** 2) ** 0.5


class XKCDColor(Color):
    def __init__(self, hex_or_rgb_color: HexString | RGBTuple, name: str) -> None:
        super().__init__(hex_or_rgb_color)
        self.name = name
