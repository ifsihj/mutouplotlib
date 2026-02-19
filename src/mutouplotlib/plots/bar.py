"""Bar plotting utilities for mutouplotlib.
"""
from __future__ import annotations
from typing import Sequence
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.axes import Axes
from matplotlib.container import BarContainer
from ..style import DEFAULT_COLORS
from ..utils import _as_2d_array, _require
from ..style import apply_publication_style


# ============================================================
# Core API
# ============================================================

def annotate_bars(
    ax: Axes,
    bars: BarContainer,
    fmt: str = "{:.2f}",
    fontsize: int = 10,
    padding: float = 3
) -> None:
    """Adds text labels above bars in a BarContainer."""
    for bar in bars:
        height = bar.get_height()
        ax.annotate(fmt.format(height),
                    xy=(bar.get_x() + bar.get_width() / 2, height),
                    xytext=(0, padding),
                    textcoords="offset points",
                    ha='center', va='bottom', fontsize=fontsize)


def annotate_bars_h(
    ax: Axes,
    bars: BarContainer,
    fmt: str = "{:.2f}",
    fontsize: int = 10,
    padding: float = 3
) -> None:
    """Adds text labels to the left of bars in a BarContainer."""
    for bar in bars:
        width = bar.get_width()
        ax.annotate(fmt.format(width),
                    xy=(width, bar.get_y() + bar.get_height() / 2),
                    xytext=(padding, 0),
                    textcoords="offset points",
                    ha='left', va='center', fontsize=fontsize)

def bar(
    ax: Axes = None,
    categories: Sequence[str] = None,
    series: Sequence[Sequence[float]] = None,
    labels: Sequence[str] = None,
    ylabel: str = "Value",
    colors: Sequence[str] | None = None,
    annotate: bool = False,
    annotate_kwargs: dict = None,
    title: str = None,
    apply_style: bool = True,
) -> BarContainer:
    """Renders a high-contrast grouped bar chart."""
    if apply_style:
        apply_publication_style()
    if ax is None:
        fig, ax = plt.subplots()

    data = _as_2d_array("series", series)
    n_series, n_cats = data.shape
    _require(len(categories) == n_cats, "Category count mismatch")

    x = np.arange(n_cats)
    total_width = 0.8
    width = total_width / n_series
    color_map = colors or DEFAULT_COLORS

    last_bars = None
    for i in range(n_series):
        offset = (i - (n_series - 1) / 2) * width
        bars = ax.bar(x + offset, data[i], width, label=labels[i],
                      color=color_map[i % len(color_map)], edgecolor="white", lw=0.5)
        last_bars = bars
        if annotate:
            annotate_bars(ax, bars)

    if title:
        ax.set_title(title)
    
    ax.set_xticks(x)
    ax.set_xticklabels(categories)
    ax.set_ylabel(ylabel)
    ax.legend()
    return last_bars

def barh(
    ax: Axes = None,
    categories: Sequence[str] = None,
    series: Sequence[Sequence[float]] = None,
    labels: Sequence[str] = None,
    xlabel: str = "Value",
    colors: Sequence[str] | None = None,
    annotate: bool = False,
    annotate_kwargs: dict = None,
    title: str = None,
    apply_style: bool = True,
) -> BarContainer:
    """Renders a high-contrast horizontal bar chart."""
    if apply_style:
        apply_publication_style()
    if ax is None:
        fig, ax = plt.subplots()
    data = _as_2d_array("series", series)
    n_series, n_cats = data.shape
    _require(len(categories) == n_cats, "Category count mismatch")
    x = np.arange(n_cats)
    total_width = 0.8
    width = total_width / n_series
    color_map = colors or DEFAULT_COLORS
    last_bars = None
    for i in range(n_series):
        offset = (i - (n_series - 1) / 2) * width
        bars = ax.barh(x + offset, data[i], width, label=labels[i],
                      color=color_map[i % len(color_map)], edgecolor="white", lw=0.5)
        last_bars = bars
        if annotate:
            annotate_bars_h(ax, bars)
    if title:
        ax.set_title(title)
    ax.set_yticks(x)
    ax.set_yticklabels(categories)
    ax.set_xlabel(xlabel)
    ax.legend()
    return last_bars