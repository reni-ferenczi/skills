# gplates-lib_pch

[Book TOC](../../TOC.md) · [entry-points](../../components/entry-points.md) · cluster Community 0 · tier 3

| Source file | Kind | Lines |
|---|---|---|
| `src/gplates-lib_pch.h` | C++ | 405 |

## Overview

A precompiled header that brings together the most frequently used external and standard headers across the GPlates library. Includes standard C/C++ library headers, Python, OpenGL, Boost, Qt, CGAL, and OGR/GDAL headers. Including this in the build precompiles these headers once, reducing overall compilation time across all translation units that reference it.

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
python scripts/gpq.py file src/gplates-lib_pch.h
```
