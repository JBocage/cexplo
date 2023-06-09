def hex_to_rgb(value):
    """Convert hex color string to rgb tuple"""
    value = value.lstrip("#")
    lv = len(value)
    return tuple(int(value[i : i + lv // 3], 16) for i in range(0, lv, lv // 3))


def rgb_to_hex(rgb):
    """Converts rgb tuple to hex color string"""
    return "#%02x%02x%02x" % rgb
