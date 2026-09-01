# python-examples

[Book TOC](../../TOC.md) · [python-examples](../../components/python-examples.md) · cluster Community 667 · tier 3

| Source file | Kind | Lines |
|---|---|---|
| `scripts/CoRegDemo.py` | Python | 64 |
| `scripts/camera_demo.py` | Python | 70 |
| `scripts/feature_collection_demo.py` | Python | 61 |
| `scripts/hellinger.py` | Python | 1372 |
| `scripts/hellinger_maths.py` | Python | 2257 |
| `scripts/interpolation_test.py` | Python | 19 |
| `scripts/reconstruct.py` | Python | 33 |

## Overview

Standalone Python scripts that demonstrate the `pygplates` module API, ranging from simple reconstruction examples to complex plate motion analysis. Scripts include basic geometric reconstruction at a specified time (`reconstruct.py`), interpolation testing (`interpolation_test.py`), interactive camera controls for the main window (`camera_demo.py`), co-registration workflows (`CoRegDemo.py`), and feature collection manipulation (`feature_collection_demo.py`). The pair `hellinger.py` and `hellinger_maths.py` implement a complete Python port of the FORTRAN Hellinger method for estimating tectonic plate rotations from ship track crossing data, including quaternion operations, matrix decomposition, and minimization routines. These scripts serve as worked examples and integration tests for users learning to extend GPlates through its Python API.

## Declared types

*None.*

## Members

*None.*

## Free functions and macros

*None.*

## Notes

*None.*

## Used by

*Nothing in the tree references this unit.*

## Related

*None.*

## Explore

Run these from the `gplates-code` skill directory:

```bash
python scripts/gpq.py file scripts/CoRegDemo.py
```
