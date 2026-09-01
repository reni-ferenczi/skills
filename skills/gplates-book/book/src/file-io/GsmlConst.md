# GsmlConst

[Book TOC](../../TOC.md) · [file-io](../../components/file-io.md) · cluster Community 1200 · tier 3

| Source file | Kind | Lines |
|---|---|---|
| `src/file-io/GsmlConst.h` | C++ | 70 |

## Overview

A collection of XML namespace declarations for GeoSciML and related standards (GML, WFS, OGC sampling) as string constants. These are prepended to XQuery expressions when parsing GeoSciML documents, allowing queries to reference elements in those namespaces by their declared prefixes.

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

*None.*

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
