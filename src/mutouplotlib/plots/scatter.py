"""Scatter plotting utilities for mutouplotlib.
"""
from __future__ import annotations
from typing import Sequence
import matplotlib.pyplot as plt
from matplotlib.axes import Axes
from ..style import PALETTE, apply_publication_style
from ..utils import _as_1d_array, _require


def scatter(
    ax: Axes,
    x: Sequence[float],
    y: Sequence[float],
    label: str | None = None,
    color: str | None = None,
    size: float = 50,
    alpha: float = 0.7
) -> None:
    """Renders a publication-style scatter plot."""
    x_arr = _as_1d_array("x", x)
    y_arr = _as_1d_array("y", y)
    _require(len(x_arr) == len(y_arr), "Length mismatch in scatter")

    ax.scatter(x_arr, y_arr, s=size, label=label,
               color=color or PALETTE["blue_main"], alpha=alpha, edgecolors="white", lw=0.5)
    if label:
        ax.legend()
    return ax
