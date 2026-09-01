# Select

[Book TOC](../../TOC.md) · [utils](../../components/utils.md) · cluster Community 472 · tier 3

| Source file | Kind | Lines |
|---|---|---|
| `src/utils/Select.h` | C++ | 53 |

## Overview

[[[PROSE overview unit=utils/Select tier=3]]]
Replace this whole block, markers included, with 1-3 paragraphs: what this unit is, why it exists, and how it fits the surrounding design. Do not restate the tables below.
[[[/PROSE]]]

## Declared types

| Name | Kind | Bases | Template | Subclasses | Description |
|---|---|---|---|---|---|
| [`GPlatesUtils::Select`](#gplatesutilsselect) | struct | — | `<bool Condition, typename TrueType, typename FalseType>` | 0 | Select allows for compile-time type selection based on the value of a compile-time boolean expression. |
| [`GPlatesUtils::Select<false, TrueType, FalseType>`](#gplatesutilsselectfalse-truetype-falsetype) | struct | — | `<typename TrueType, typename FalseType>` | 0 | — |

## Members

### `GPlatesUtils::Select`

| Member | Kind | Type | Access | Description |
|---|---|---|---|---|
| `result` | typedef | `TrueType` | public | — |

### `GPlatesUtils::Select<false, TrueType, FalseType>`

| Member | Kind | Type | Access | Description |
|---|---|---|---|---|
| `result` | typedef | `FalseType` | public | — |

## Free functions and macros

| Name | Kind | Type / body | Description |
|---|---|---|---|
| `GPLATES_UTILS_SELECT_H` | macro | `None` | — |

## Notes

[[[PROSE notes unit=utils/Select tier=3]]]
Replace this whole block, markers included, with invariants, ownership, threading or gotchas that are not visible in the tables. Write *None.* if there is nothing worth saying.
[[[/PROSE]]]

## Used by

| Unit | Component | References |
|---|---|---|
| [gui/ColourPaletteAdapter](../gui/ColourPaletteAdapter.md) | gui | 3 |
| [qt-widgets/HellingerSegmentDialog](../qt-widgets/HellingerSegmentDialog.md) | qt-widgets | 2 |
| [qt-widgets/SearchResultsDockWidget](../qt-widgets/SearchResultsDockWidget.md) | qt-widgets | 2 |
| [qt-widgets/SelectionWidget](../qt-widgets/SelectionWidget.md) | qt-widgets | 2 |
| [utils/TypeTraits](TypeTraits.md) | utils | 2 |
| [gui/ColourPalette](../gui/ColourPalette.md) | gui | 1 |
| [gui/CptColourPalette](../gui/CptColourPalette.md) | gui | 1 |

## Related

*None.*

## Explore

Run these from the `gplates-code` skill directory:

```bash
python scripts/gpq.py file src/utils/Select.h
python scripts/gpq.py def GPlatesUtils::Select --body
python scripts/gpq.py uses Select --kind struct
python scripts/gpq.py hier Select
```
