"""
Core operators for the Holographic Entangled Coherence Model (HECM).

This module defines the first concrete HECM operator: a simple coherence
metric over a 1D real-valued field. It is intentionally minimal and
implementation-focused, serving as a starting point for richer operators.
"""

from typing import Sequence
import math


def coherence_1d(field: Sequence[float]) -> float:
    """
    Compute a simple coherence score for a 1D field.

    Intuition:
    - Treat `field` as samples of a signal.
    - Measure how "aligned" the samples are by comparing:
        - the magnitude of the sum vector
        - to the sum of magnitudes
    - Return a value in [0, 1], where:
        - 1.0  => perfectly aligned (all same sign and magnitude)
        - 0.0  => maximally incoherent (perfect cancellation)

    This is a deliberately simple, implementation-ready placeholder for
    more sophisticated HECM coherence operators.

    Parameters
    ----------
    field : Sequence[float]
        A non-empty sequence of real values.

    Returns
    -------
    float
        Coherence score in [0.0, 1.0].

    Raises
    ------
    ValueError
        If the field is empty or all values are zero.
    """
    if not field:
        raise ValueError("coherence_1d: field must not be empty")

    sum_abs = sum(abs(x) for x in field)
    if sum_abs == 0:
        raise ValueError("coherence_1d: field must not be all zeros")

    sum_val = sum(field)
    # normalized coherence: magnitude of sum vs sum of magnitudes
    return abs(sum_val) / sum_abs


def coherence_1d_phase(field: Sequence[complex]) -> float:
    """
    Coherence operator for a 1D complex field.

    Same idea as coherence_1d, but now the field is complex-valued and
    we explicitly use vector addition in the complex plane.

    Parameters
    ----------
    field : Sequence[complex]
        A non-empty sequence of complex values.

    Returns
    -------
    float
        Coherence score in [0.0, 1.0].

    Raises
    ------
    ValueError
        If the field is empty or all values are zero.
    """
    if not field:
        raise ValueError("coherence_1d_phase: field must not be empty")

    sum_abs = sum(abs(z) for z in field)
    if sum_abs == 0:
        raise ValueError("coherence_1d_phase: field must not be all zeros")

    sum_vec = sum(field)
    return abs(sum_vec) / sum_abs
