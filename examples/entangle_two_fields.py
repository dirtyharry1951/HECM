# examples/entangle_two_fields.py

import numpy as np
from qf_entangle_beam import qf_entangle_beam

field_a = np.array([0.2, 0.4, 0.6, 0.8])
field_b = np.array([0.8, 0.6, 0.4, 0.2])

print("Initial fields:")
print("A:", field_a)
print("B:", field_b)

new_a, new_b = qf_entangle_beam(field_a, field_b, strength=0.25)

print("\nAfter entanglement:")
print("A:", new_a)
print("B:", new_b)
