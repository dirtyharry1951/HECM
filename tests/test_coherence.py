from hecm.core import coherence_1d, coherence_1d_phase
import math
import pytest


def test_coherence_1d_perfect_alignment():
    field = [1.0, 1.0, 1.0]
    c = coherence_1d(field)
    assert math.isclose(c, 1.0)


def test_coherence_1d_partial_cancellation():
    field = [1.0, -1.0, 1.0]
    c = coherence_1d(field)
    assert 0.0 < c < 1.0


def test_coherence_1d_all_zero_raises():
    with pytest.raises(ValueError):
        coherence_1d([0.0, 0.0])


def test_coherence_1d_phase_perfect_alignment():
    field = [1 + 0j, 1 + 0j, 1 + 0j]
    c = coherence_1d_phase(field)
    assert math.isclose(c, 1.0)


def test_coherence_1d_phase_incoherent():
    # roughly canceling phases
    field = [1 + 0j, -1 + 0j]
    c = coherence_1d_phase(field)
    assert math.isclose(c, 0.0)
