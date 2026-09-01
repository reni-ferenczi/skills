# VisualLayerGroup

[Book TOC](../../TOC.md) · [presentation](../../components/presentation.md) · cluster Community 3 · tier 3

| Source file | Kind | Lines |
|---|---|---|
| `src/presentation/VisualLayerGroup.h` | C++ | 57 |

## Overview

[[[PROSE overview unit=presentation/VisualLayerGroup tier=3]]]
Replace this whole block, markers included, with 1-3 paragraphs: what this unit is, why it exists, and how it fits the surrounding design. Do not restate the tables below.
[[[/PROSE]]]

## Declared types

| Name | Kind | Bases | Template | Subclasses | Description |
|---|---|---|---|---|---|
| [`GPlatesPresentation::VisualLayerGroup::Type`](#gplatespresentationvisuallayergrouptype) | enum | — | — | 0 | — |

## Members

### `GPlatesPresentation::VisualLayerGroup::Type`

| Member | Kind | Type | Access | Description |
|---|---|---|---|---|
| `SCALAR_FIELDS` | enumerator | `None` | — | — |
| `RASTERS` | enumerator | `None` | — | — |
| `DERIVED_DATA` | enumerator | `None` | — | — |
| `BASIC_DATA` | enumerator | `None` | — | — |
| `NUM_GROUPS` | enumerator | `None` | — | — |

## Free functions and macros

| Name | Kind | Type / body | Description |
|---|---|---|---|
| `GPLATES_PRESENTATION_VISUALLAYERGROUP_H` | macro | `None` | — |

## Notes

[[[PROSE notes unit=presentation/VisualLayerGroup tier=3]]]
Replace this whole block, markers included, with invariants, ownership, threading or gotchas that are not visible in the tables. Write *None.* if there is nothing worth saying.
[[[/PROSE]]]

## Used by

| Unit | Component | References |
|---|---|---|
| [presentation/VisualLayerRegistry](VisualLayerRegistry.md) | presentation | 31 |

## Related

*None.*

## Explore

Run these from the `gplates-code` skill directory:

```bash
python scripts/gpq.py file src/presentation/VisualLayerGroup.h
python scripts/gpq.py def GPlatesPresentation::VisualLayerGroup::Type --body
python scripts/gpq.py uses Type --kind enum
```
