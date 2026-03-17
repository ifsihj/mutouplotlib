"""Utility functions for mutouplotlib.
"""
from __future__ import annotations

from typing import Any,Final, Sequence, TYPE_CHECKING
import numpy as np
import numpy.typing as npt
from pathlib import Path
import logging
import matplotlib.pyplot as plt
from matplotlib.figure import Figure

_VECTOR_FORMATS: Final[set[str]] = {"pdf", "svg", "eps"}
_RASTER_FORMATS: Final[set[str]] = {"png", "jpg", "jpeg", "tif", "tiff"}
_SUPPORTED_FORMATS: Final[set[str]] = _VECTOR_FORMATS | _RASTER_FORMATS

def _require(condition: bool, message: str) -> None:
    """Internal assertion-style validator."""
    if not condition:
        raise ValueError(f"[scientific_figure_pro] {message}")


def _as_1d_array(name: str, values: Any) -> npt.NDArray[np.float64]:
    """Ensures input is a 1D numpy array of floats."""
    arr = np.asarray(values, dtype=np.float64)
    _require(arr.ndim == 1, f"'{name}' must be 1D, got shape {arr.shape}")
    _require(arr.size > 0, f"'{name}' cannot be empty")
    return arr


def _as_2d_array(name: str, values: Any) -> npt.NDArray[np.float64]:
    """Ensures input is a 2D numpy array of floats."""
    arr = np.asarray(values, dtype=np.float64)
    _require(arr.ndim == 2, f"'{name}' must be 2D, got shape {arr.shape}")
    _require(arr.size > 0, f"'{name}' cannot be empty")
    return arr

def finalize_figure(
    fig: Figure,
    out_path: str | Path,
    formats: Sequence[str] | None = None,
    dpi: int = 300,
    close: bool = True,
    pad: float = 0.05,
    **kwargs: Any
) -> list[Path]:
    """Saves the figure in multiple formats and closes it.

    If no formats are provided, it defaults to (pdf, svg, eps) unless the out_path
    already contains an extension.

    Args:
        fig: The matplotlib Figure object.
        out_path: Filename or directory path.
        formats: List of extensions (e.g., ['png', 'pdf']).
        dpi: Resolution for raster formats.
        close: Whether to call plt.close(fig) after saving.
        pad: Padding in inches.
        **kwargs: Passed to fig.savefig.

    Returns:
        List of Paths to the saved files.
    """
    path = Path(out_path)
    exts = formats

    if not exts:
        exts = [path.suffix.lstrip(".")] if path.suffix else ["pdf", "svg", "eps"]

    base = path.with_suffix("") if path.suffix else path
    base.parent.mkdir(parents=True, exist_ok=True)

    saved: list[Path] = []
    for ext in exts:
        ext = ext.lower().strip(".")
        _require(ext in _SUPPORTED_FORMATS, f"Unsupported format: {ext}")

        target = base.with_suffix(f".{ext}")
        save_params = {"format": ext, "bbox_inches": "tight", "pad_inches": pad}
        if ext in _RASTER_FORMATS:
            save_params["dpi"] = dpi
        save_params.update(kwargs)

        fig.savefig(target, **save_params)
        saved.append(target)

    if close:
        plt.close(fig)

    logger.info(f"Saved figure to: {', '.join(p.name for p in saved)}")
    return saved
