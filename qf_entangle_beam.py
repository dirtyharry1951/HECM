# qf_entangle_beam.py

import numpy as np

def qf_entangle_beam(field_i, field_j, strength=0.1, kernel=None):
    """
    Minimal entanglement operator for HECM v0.2.0.
    
    Parameters
    ----------
    field_i : np.ndarray
        First coherence field.
    field_j : np.ndarray
        Second coherence field.
    strength : float
        Coupling strength (0 < strength < 1).
    kernel : callable or None
        Optional transform applied to the partner field before mixing.
        If None, identity transform is used.

    Returns
    -------
    new_i, new_j : np.ndarray
        Updated fields after symmetric entanglement.
    """

    if kernel is None:
        kernel = lambda x: x

    assert field_i.shape == field_j.shape, "Fields must have same shape."

    influence_i = kernel(field_j)
    influence_j = kernel(field_i)

    new_i = (1 - strength) * field_i + strength * influence_i
    new_j = (1 - strength) * field_j + strength * influence_j

    return new_i, new_j
