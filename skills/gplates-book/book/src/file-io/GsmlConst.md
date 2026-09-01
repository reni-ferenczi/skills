# GsmlConst

[Book TOC](../../TOC.md) · [file-io](../../components/file-io.md) · cluster Community 1200 · tier 3

| Source file | Kind | Lines |
|---|---|---|
| `src/file-io/GsmlConst.h` | C++ | 70 |

## Overview

[[[PROSE overview unit=file-io/GsmlConst tier=3]]]
Replace this whole block, markers included, with 1-3 paragraphs: what this unit is, why it exists, and how it fits the surrounding design. Do not restate the tables below.
[[[/PROSE]]]

## Declared types

*None.*

## Members

*None.*

## Free functions and macros

| Name | Kind | Type / body | Description |
|---|---|---|---|
| `GPLATES_FILEIO_GSMLCONST_H` | macro | `None` | — |
| `xsi_ns` | variable | `QString` | define GeoSciML namespace |
| `gml_ns` | variable | `QString` | — |
| `wfs_ns` | variable | `QString` | — |
| `gsml_ns` | variable | `QString` | — |
| `sa_ns` | variable | `QString` | — |
| `om_ns` | variable | `QString` | — |
| `cgu_ns` | variable | `QString` | — |
| `xlink_ns` | variable | `QString` | — |
| `gpml_ns` | variable | `QString` | — |
| `all_namespaces()` | function | `QString` | — |
| `declare_idx` | variable | `QString` | — |

## Notes

[[[PROSE notes unit=file-io/GsmlConst tier=3]]]
Replace this whole block, markers included, with invariants, ownership, threading or gotchas that are not visible in the tables. Write *None.* if there is nothing worth saying.
[[[/PROSE]]]

## Used by

| Unit | Component | References |
|---|---|---|
| [utils/XQueryUtils](../utils/XQueryUtils.md) | utils | 17 |
| [file-io/GsmlFeatureHandlers](GsmlFeatureHandlers.md) | file-io | 3 |
| [file-io/GsmlPropertyHandlers](GsmlPropertyHandlers.md) | file-io | 2 |
| [file-io/GsmlFeaturesDef](GsmlFeaturesDef.md) | file-io | 1 |
| [file-io/GsmlPropertyDef](GsmlPropertyDef.md) | file-io | 1 |

## Related

*None.*

## Explore

Run these from the `gplates-code` skill directory:

```bash
python scripts/gpq.py file src/file-io/GsmlConst.h
```
