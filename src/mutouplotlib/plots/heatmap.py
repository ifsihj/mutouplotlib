"""Heatmap plotting utilities for mutouplotlib.
"""
from __future__ import annotations

from typing import Sequence

import matplotlib.pyplot as plt
import numpy as np

from matplotlib.axes import Axes
from matplotlib.image import AxesImage

from ..style import apply_publication_style
from ..utils import _as_2d_array

# ============================================================
# Core API
# ============================================================

def heatmap(
    ax: Axes,
    matrix: Sequence[Sequence[float]],
    title: str | None = None,
    xlabels: Sequence[str] | None = None,
    ylabels: Sequence[str] | None = None,
    cmap: str = "magma",
    cbar_label: str | None = None,
    annotate: bool = False,
    apply_style: bool = True,
) -> AxesImage:
    """Renders a cleaned heatmap with optional text annotations."""
    if apply_style:
        apply_publication_style()
    if ax is None:
        fig, ax = plt.subplots()

    data = _as_2d_array("matrix", matrix)
    im = ax.imshow(data, cmap=cmap, aspect="auto", interpolation="nearest")

    if xlabels:
        ax.set_xticks(np.arange(len(xlabels)))
        ax.set_xticklabels(xlabels, rotation=45, ha="right")
    if ylabels:
        ax.set_yticks(np.arange(len(ylabels)))
        ax.set_yticklabels(ylabels)

    if cbar_label:
        cbar = ax.figure.colorbar(im, ax=ax)
        cbar.set_label(cbar_label)

    if annotate:
        threshold = (data.max() + data.min()) / 2
        for i in range(data.shape[0]):
            for j in range(data.shape[1]):
                val = data[i, j]
                color = "white" if val < threshold else "black"
                ax.text(j, i, f"{val:.2f}", ha="center", va="center", color=color, fontsize=9)
    
    if title:
        ax.set_title(title)

    return im
