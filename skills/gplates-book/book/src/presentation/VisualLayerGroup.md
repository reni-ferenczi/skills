# VisualLayerGroup

[Book TOC](../../TOC.md) · [presentation](../../components/presentation.md) · cluster Community 3 · tier 3

| Source file | Kind | Lines |
|---|---|---|
| `src/presentation/VisualLayerGroup.h` | C++ | 57 |

## Overview

Defines an enumeration of visual layer categories—`SCALAR_FIELDS`, `RASTERS`, `DERIVED_DATA`, `BASIC_DATA`—used to organize how layers appear on screen. The enumeration order is significant: it determines the order in which layers are added to the `VisualLayers` collection and, inversely, their visual stacking (since `VisualLayers` stores layers in reverse display order, the first enum group appears at the bottom on screen).

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

The enumeration order is significant and aligns with the visual stacking of layers on screen. When adding a new group, remember that `VisualLayers` stores layers in reverse display order, so early enum values visually appear at the bottom. `NUM_GROUPS` must remain the last entry.

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
