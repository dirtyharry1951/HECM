"""
Minimal example demonstrating use of the HECM coherence operators.
"""

from hecm.core import coherence_1d, coherence_1d_phase

def main():
    field_real = [1.0, 0.8, 0.9, 1.0]
    field_complex = [1+0j, 0.8+0.1j, 0.9-0.1j, 1+0j]

    c_real = coherence_1d(field_real)
    c_complex = coherence_1d_phase(field_complex)

    print("Real-field coherence:", c_real)
    print("Complex-field coherence:", c_complex)

if __name__ == "__main__":
    main()

## Citation

If you use HECM in academic work, please cite the Zenodo DOI and the metadata
in `CITATION.cff`.

## License

see `LICENSE`.
