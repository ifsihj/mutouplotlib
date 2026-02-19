"""Utility functions for mutouplotlib.
"""
from __future__ import annotations

from typing import Any
import numpy as np
import numpy.typing as npt

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

