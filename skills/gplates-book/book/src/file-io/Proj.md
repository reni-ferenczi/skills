# Proj

[Book TOC](../../TOC.md) · [file-io](../../components/file-io.md) · cluster Community 0 · tier 3

| Source file | Kind | Lines |
|---|---|---|
| `src/file-io/Proj.h` | C++ | 51 |

## Overview

A compatibility wrapper for the PROJ cartographic projection library. PROJ went through a major API redesign from version 4 to 5+, and this header detects the build configuration and includes the appropriate header: `proj.h` for PROJ 5+, or `proj_api.h` as a fallback for older PROJ 4 installations. It defines `GPLATES_USING_PROJ4` when the older API is in use.

## Declared types

*None.*

## Members

*None.*

## Free functions and macros

| Name | Kind | Type / body | Description |
|---|---|---|---|
| `GPLATES_FILEIO_PROJ_H` | macro | `None` | — |

## Notes

*None.*

## Used by

| Unit | Component | References |
|---|---|---|
| [file-io/StandaloneBundle](StandaloneBundle.md) | file-io | 1 |
| [gui/MapProjection](../gui/MapProjection.md) | gui | 1 |

## Related

*None.*

## Explore

Run these from the `gplates-code` skill directory:

```bash
python scripts/gpq.py file src/file-io/Proj.h
```
