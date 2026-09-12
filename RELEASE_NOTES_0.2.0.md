# EcoPy 0.2.0

EcoPy 0.2.0 is a compatibility-focused revival of the EcoPy ecological data-analysis library for modern Python 3.

## Highlights

- Updated legacy Python 2 / early Python 3 code for modern Python 3.
- Tested with Python 3.14.
- Updated compatibility with modern NumPy, SciPy, pandas, matplotlib, and patsy.
- Replaced the mandatory native isotonic-regression extension with a pure-Python/NumPy implementation for normal installation.
- Retained the original Cython implementation (`isoFunc.pyx`) as optional development code.
- EcoPy can now be installed without Microsoft Visual C++ or another C/C++ compiler.
- The release preserves the original EcoPy API and ecological methods as far as practical.

## Validation

The 0.2.0 development baseline was tested with the project's modern regression/smoke suite:

    Ran 11 tests
    OK

The wheel is a pure-Python distribution:

    ecopy-0.2.0-py3-none-any.whl

Further numerical and methodological auditing will continue in subsequent 0.2.x development releases.
