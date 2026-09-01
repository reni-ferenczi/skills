# pygplates_pch

[Book TOC](../../TOC.md) · [entry-points](../../components/entry-points.md) · cluster Community 0 · tier 3

| Source file | Kind | Lines |
|---|---|---|
| `src/pygplates_pch.h` | C++ | 405 |

## Overview

A precompiled header for the pyGPlates Python extension module build. It collects all the common dependencies: C++ standard library headers, Boost libraries (including `boost/python.hpp` for bindings), Qt GUI components, CGAL computational geometry, QWT plotting, and GDAL spatial reference systems. Precompiling this single header once speeds up compilation of the many `.cc` files in the API module by avoiding repeated parsing of the same included headers. This is specific to the pyGPlates standalone module build (controlled by the `GPLATES_BUILD_GPLATES` CMake flag) and is distinct from the main GPlates application executable.

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
python scripts/gpq.py file src/pygplates_pch.h
```
