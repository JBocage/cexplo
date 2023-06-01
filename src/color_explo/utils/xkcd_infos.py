import pandas as pd

from color_explo.utils.color import Color, XKCDColor
from color_explo.utils.paths import PackagePaths


def get_color_df() -> pd.DataFrame:
    return pd.read_pickle(PackagePaths.DATA / "xkcd_colors.pkl")


def get_xkcd_color_dist_df() -> pd.DataFrame:
    return pd.read_pickle(PackagePaths.DATA / "xkcd_colors_dist.pkl")


df = get_color_df()
colors_dict = {cn: XKCDColor(df.loc[cn]["color_hex"], cn) for cn in df.index}
del df
