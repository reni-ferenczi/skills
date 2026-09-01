# types

[Book TOC](../../../TOC.md) · [global](../../../components/global.md) · cluster Community 1691 · tier 3 · **deprecated**

| Source file | Kind | Lines |
|---|---|---|
| `src/global/deprecated/types.h` | C++ | 83 |

## Overview

[[[PROSE overview unit=global/deprecated/types tier=3]]]
Replace this whole block, markers included, with 1-3 paragraphs: what this unit is, why it exists, and how it fits the surrounding design. Do not restate the tables below.
[[[/PROSE]]]

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

[[[PROSE notes unit=global/deprecated/types tier=3]]]
Replace this whole block, markers included, with invariants, ownership, threading or gotchas that are not visible in the tables. Write *None.* if there is nothing worth saying.
[[[/PROSE]]]

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
