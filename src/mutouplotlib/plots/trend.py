"""Trend plotting utilities for mutouplotlib.
"""

from __future__ import annotations

from typing import Iterable, Sequence

import matplotlib.pyplot as plt
import numpy as np

from ..style import apply_publication_style, get_default_colors


# ============================================================
# Core API
# ============================================================

def trend(
    x: Sequence[float],
    y: Sequence[float] | Sequence[Sequence[float]],
    *,
    labels: Sequence[str] | None = None,
    colors: Sequence[str] | None = None,
    markers: bool = False,
    linewidth: float = 2.5,
    markersize: float = 6,
    alpha: float = 1.0,
    xlabel: str | None = None,
    ylabel: str | None = None,
    title: str | None = None,
    ax=None,
    apply_style: bool = True,
):
    """Create publication-quality trend plot.

    Supports single or multiple lines.

    Parameters
    ----------
    x : array-like
        X-axis values

    y : array-like or list of array-like
        Y values. Can be:
        - single sequence
        - list of sequences for multiple lines

    labels : list of str, optional

    colors : list of str, optional

    markers : bool, default False

    linewidth : float

    xlabel, ylabel, title : str

    ax : matplotlib axis, optional

    apply_style : bool
        Apply mutouplotlib publication style automatically

    Returns
    -------
    ax : matplotlib axis
    """

    if apply_style:
        apply_publication_style()

    if ax is None:
        fig, ax = plt.subplots()

    x = np.asarray(x)

    # normalize y to list
    if isinstance(y[0], (list, tuple, np.ndarray)):
        ys = [np.asarray(v) for v in y]
    else:
        ys = [np.asarray(y)]

    n_lines = len(ys)

    if colors is None:
        colors = get_default_colors(n_lines)

    if labels is None:
        labels = [None] * n_lines

    marker_style = "o" if markers else None

    for i in range(n_lines):

        ax.plot(
            x,
            ys[i],
            label=labels[i],
            color=colors[i],
            linewidth=linewidth,
            marker=marker_style,
            markersize=markersize,
            alpha=alpha,
        )

    # labels
    if xlabel:
        ax.set_xlabel(xlabel)

    if ylabel:
        ax.set_ylabel(ylabel)

    if title:
        ax.set_title(title)

    if any(labels):
        ax.legend()

    return ax


# ============================================================
# Confidence interval version
# ============================================================

def trend_ci(
    x,
    y,
    y_lower,
    y_upper,
    *,
    color=None,
    label=None,
    alpha_line=1.0,
    alpha_band=0.2,
    linewidth=2.5,
    ax=None,
    apply_style=True,
):
    """Trend plot with confidence interval band."""

    if apply_style:
        apply_publication_style()

    if ax is None:
        fig, ax = plt.subplots()

    x = np.asarray(x)
    y = np.asarray(y)

    if color is None:
        color = get_default_colors(1)[0]

    ax.plot(
        x,
        y,
        color=color,
        linewidth=linewidth,
        alpha=alpha_line,
        label=label,
    )

    ax.fill_between(
        x,
        y_lower,
        y_upper,
        color=color,
        alpha=alpha_band,
        linewidth=0,
    )

    if label:
        ax.legend()

    return ax
