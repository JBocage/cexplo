from typing import Union

import numpy as np
import plotly.graph_objects as go
import streamlit as st

from color_explo.utils.color import Color, XKCDColor
from color_explo.utils.xkcd_infos import colors_dict, get_xkcd_color_dist_df

st.set_page_config(layout="wide")


N_PER_COL = 5
NCOLS = 5

N = N_PER_COL * NCOLS

sidebar = st.sidebar
sidebar.title("")

c = sidebar.color_picker("Pick a color")


chosen_color = Color(c)


color_choosing = st.expander("explo")


# fig = go.Figure()

# fig.add_shape(
#     type="rect",
#     fillcolor=chosen_color.hex,

# )

fig = go.Figure(
    [
        go.Scatter(
            x=[0, 1, 1, 0],
            y=[0, 0, 1, 1],
            fill="toself",
            fillcolor=chosen_color.hex,
            hovertext="chosen color!",
            text="",
        ),
        go.Scatter(
            x=[1.5, 2.5, 2.5, 1.5],
            y=[1.5, 1.5, 2.5, 2.5],
            fill="toself",
            fillcolor=chosen_color.hex,
        ),
    ]
)
st.plotly_chart(fig)


# cols = color_choosing.columns(tuple(1 for _ in range(NCOLS)))


# def display_color(color: Union[Color, XKCDColor], container: st.container):
#     r, g, b = color.rgb
#     if isinstance(color, XKCDColor):
#         container.text(f"xkcd:{color.name}\n" f"{color.hex}\n" f"{color.rgb}")

#     container.image(
#         np.stack(
#             (
#                 np.full((50, 50), r),
#                 np.full((50, 50), g),
#                 np.full((50, 50), b),
#             )
#         ).transpose([1, 2, 0])
#     )


# # sidebar
# cname, cobj = min(colors_dict.items(), key=lambda c: chosen_color.rgb_dist(c[1]))
# sidebar.text(f"Closest color:")
# display_color(cobj, sidebar)

# # c2
# df = get_xkcd_color_dist_df()

# closest_colors = df.loc[df.index.get_level_values("color_from") == cname].sort_values(
#     "rgb_dist"
# )


# for i, stcol in enumerate(cols):
#     for _, col in closest_colors.index[i + 1 : 1 + N : NCOLS]:
#         display_color(colors_dict[col], stcol)
