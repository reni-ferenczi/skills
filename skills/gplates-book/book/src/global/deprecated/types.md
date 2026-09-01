# types

[Book TOC](../../../TOC.md) · [global](../../../components/global.md) · cluster Community 1691 · tier 3 · **deprecated**

| Source file | Kind | Lines |
|---|---|---|
| `src/global/deprecated/types.h` | C++ | 83 |

## Overview

A collection of deprecated type aliases and enumerations that were used throughout earlier versions of GPlates for basic type identification. The unit provides convenient type names for rotation IDs (`rid_t`), integral values (`integer_t`), and array indices (`index_t`), as well as enumerations to classify geometry features (`FeatureTypes`) and topology structures (`TopologyTypes`). This header was designed to support control flow and optimisation decisions based on geometry and topology types, but is now superseded by the modern type model in the `model` and `property-values` modules.

## Declared types

| Name | Kind | Bases | Template | Subclasses | Description |
|---|---|---|---|---|---|
| [`GPlatesGlobal::rid_t`](#gplatesglobalrid_t) | typedef | — | — | 0 | The type internally for rotation ids. |
| [`GPlatesGlobal::integer_t`](#gplatesglobalinteger_t) | typedef | — | — | 0 | The integral type. |
| [`GPlatesGlobal::index_t`](#gplatesglobalindex_t) | typedef | — | — | 0 | The index for the subscript operator. index\_t has integral semantics, but is always non-negative. |
| [`GPlatesGlobal::FeatureTypes`](#gplatesglobalfeaturetypes) | enum | — | — | 0 | Basic feature types. |
| [`GPlatesGlobal::TopologyTypes`](#gplatesglobaltopologytypes) | enum | — | — | 0 | — |

## Members

### `GPlatesGlobal::rid_t`

*None.*

### `GPlatesGlobal::integer_t`

*None.*

### `GPlatesGlobal::index_t`

*None.*

### `GPlatesGlobal::FeatureTypes`

| Member | Kind | Type | Access | Description |
|---|---|---|---|---|
| `NONE_FEATURE` | enumerator | `None` | — | — |
| `POINT_FEATURE` | enumerator | `None` | — | — |
| `LINE_FEATURE` | enumerator | `None` | — | — |
| `POLYGON_FEATURE` | enumerator | `None` | — | — |
| `MULTIPOINT_FEATURE` | enumerator | `None` | — | — |
| `TOPOLOGY_FEATURE` | enumerator | `None` | — | — |
| `MESH_FEATURE` | enumerator | `None` | — | — |
| `GRID_FEATURE` | enumerator | `None` | — | — |
| `UNKNOWN_FEATURE` | enumerator | `None` | — | — |

### `GPlatesGlobal::TopologyTypes`

| Member | Kind | Type | Access | Description |
|---|---|---|---|---|
| `UNKNOWN_TOPOLOGY` | enumerator | `None` | — | — |
| `PLATE_POLYGON` | enumerator | `None` | — | — |
| `SLAB_POLYGON` | enumerator | `None` | — | — |
| `DEFORMING_POLYGON` | enumerator | `None` | — | — |
| `NETWORK` | enumerator | `None` | — | — |

## Free functions and macros

| Name | Kind | Type / body | Description |
|---|---|---|---|
| `GPLATES_GLOBAL_TYPES_H` | macro | `None` | — |

## Notes

*None.*

## Used by

| Unit | Component | References |
|---|---|---|
| [deprecated/controls/Reconstruct](../../deprecated/controls/Reconstruct.md) | deprecated | 9 |
| [file-io/deprecated/NetCDFReader](../../file-io/deprecated/NetCDFReader.md) | file-io | 8 |
| [maths/deprecated/RotationSequence](../../maths/deprecated/RotationSequence.md) | maths | 8 |
| [deprecated/controls/File](../../deprecated/controls/File.md) | deprecated | 6 |
| [maths/deprecated/GridOnSphere](../../maths/deprecated/GridOnSphere.md) | maths | 5 |
| [file-io/deprecated/NetCDFWriter](../../file-io/deprecated/NetCDFWriter.md) | file-io | 4 |
| [file-io/deprecated/GPlatesReader](../../file-io/deprecated/GPlatesReader.md) | file-io | 2 |

## Related

*None.*

## Explore

Run these from the `gplates-code` skill directory:

```bash
python scripts/gpq.py file src/global/deprecated/types.h
python scripts/gpq.py def GPlatesGlobal::FeatureTypes --body
python scripts/gpq.py uses FeatureTypes --kind enum
```
