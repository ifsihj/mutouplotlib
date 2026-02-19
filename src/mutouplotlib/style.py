"""
Global style configuration for mutouplotlib.
"""

from __future__ import annotations

import logging
from dataclasses import dataclass
from typing import Final, Sequence

import matplotlib.pyplot as plt

logger = logging.getLogger(__name__)

# ============================================================
# Color System
# ============================================================

PALETTE: Final[dict[str, str]] = {
    "blue_main": "#0F4D92",
    "blue_secondary": "#3775BA",
    "green_light": "#DDF3DE",
    "green_main": "#8BCF8B",
    "red_light": "#F6CFCB",
    "red_main": "#B64342",
    "neutral": "#CFCECE",
    "highlight": "#FFD700",
    "teal": "#42949E",
    "violet": "#9A4D8E",
}

DEFAULT_COLORS: Final[list[str]] = [
    PALETTE["blue_main"],
    PALETTE["green_main"],
    PALETTE["red_main"],
    PALETTE["teal"],
    PALETTE["violet"],
    PALETTE["neutral"],
]


# ============================================================
# Style Definition
# ============================================================

@dataclass(frozen=True)
class FigureStyle:
    """Immutable configuration for matplotlib styling.

    Attributes
    ----------
    font_size:
        Base font size in points.

    axes_linewidth:
        Width of axes spines.

    use_tex:
        Whether to use LaTeX rendering.

    font_family:
        Primary sans-serif font priority list.

    chinese_font_family:
        Chinese font fallback priority list.
    """

    font_size: int = 16

    axes_linewidth: float = 2.2

    use_tex: bool = False

    font_family: tuple[str, ...] = (
        "DejaVu Sans",
        "Helvetica",
        "Arial",
        "sans-serif",
    )

    chinese_font_family: tuple[str, ...] = (
        "simsun",
        "Songti SC",
        "STSong",
        "NSimSun",
    )


# ============================================================
# Core API
# ============================================================

def apply_publication_style(style: FigureStyle | None = None) -> None:
    """Apply publication-quality matplotlib rcParams.

    This function configures matplotlib to produce consistent,
    submission-ready figures suitable for academic journals.

    Parameters
    ----------
    style:
        Optional FigureStyle instance.
    """

    s = style or FigureStyle()

    plt.rcParams.update({

        # Text rendering
        "text.usetex": s.use_tex,

        # Font system
        "font.family": "sans-serif",

        "font.sans-serif": [
            *s.font_family,
            *s.chinese_font_family,      
        ],

        "axes.unicode_minus": False,

        # Font sizes
        "font.size": s.font_size,

        "axes.labelsize": s.font_size,

        "axes.titlesize": s.font_size + 2,

        "xtick.labelsize": s.font_size - 2,

        "ytick.labelsize": s.font_size - 2,

        "legend.fontsize": s.font_size - 2,

        # Axes styling
        "axes.linewidth": s.axes_linewidth,

        "axes.spines.top": False,

        "axes.spines.right": False,

        # Tick styling
        "xtick.direction": "out",

        "ytick.direction": "out",

        "xtick.major.width": s.axes_linewidth * 0.6,

        "ytick.major.width": s.axes_linewidth * 0.6,

        # Legend styling
        "legend.frameon": False,

        "legend.handlelength": 2.4,

        # Export settings
        "pdf.fonttype": 42,

        "ps.fonttype": 42,

        "svg.fonttype": "none",

        "savefig.bbox": "tight",

        "savefig.transparent": False,

    })

    logger.debug("mutouplotlib publication style applied.")


# ============================================================
# Utility
# ============================================================

def get_default_colors(n: int) -> list[str]:
    """Return n colors from the default palette."""

    return [
        DEFAULT_COLORS[i % len(DEFAULT_COLORS)]
        for i in range(n)
    ]


def use_style(style: FigureStyle) -> None:
    """Alias for apply_publication_style."""

    apply_publication_style(style)
