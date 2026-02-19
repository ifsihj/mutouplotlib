# SPDX-FileCopyrightText: 2026-present U.N. Owen <void@some.where>
#
# SPDX-License-Identifier: MIT
"""mutouplotlib: Publication-quality matplotlib wrapper."""

from .style import (
    FigureStyle,
    apply_publication_style,
    PALETTE,
    DEFAULT_COLORS,
    get_default_colors,
)

from .plots import plot, plot_ci, heatmap, bar, barh, scatter

__all__ = [
    "FigureStyle",
    "apply_publication_style",
    "PALETTE",
    "DEFAULT_COLORS",
    "get_default_colors",
    "plot",
    "plot_ci",
    "heatmap",
    "bar",
    "barh",
    "scatter"
]

__version__ = "0.0.1"
