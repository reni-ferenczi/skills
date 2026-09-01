# SetConst

[Book TOC](../../TOC.md) · [utils](../../components/utils.md) · cluster Community 189 · tier 2

| Source file | Kind | Lines |
|---|---|---|
| `src/utils/SetConst.h` | C++ | 53 |

## Overview

[[[PROSE overview unit=utils/SetConst tier=2]]]
Replace this whole block, markers included, with 1-3 paragraphs: what this unit is, why it exists, and how it fits the surrounding design. Do not restate the tables below.
[[[/PROSE]]]

## Declared types

| Name | Kind | Bases | Template | Subclasses | Description |
|---|---|---|---|---|---|
| [`GPlatesUtils::SetConst`](#gplatesutilssetconst) | struct | — | `<class T, bool Const>` | 0 | SetConst adds top level const-ness to T if Const is true, and removes any top level const-ness from T if Const is false. |
| [`GPlatesUtils::SetConst<T, true>`](#gplatesutilssetconstt-true) | struct | — | `<class T>` | 0 | — |

## Members

### `GPlatesUtils::SetConst`

| Member | Kind | Type | Access | Description |
|---|---|---|---|---|
| `type` | typedef | `typename boost::remove_const<T>::type` | public | — |

### `GPlatesUtils::SetConst<T, true>`

| Member | Kind | Type | Access | Description |
|---|---|---|---|---|
| `type` | typedef | `typename boost::add_const<T>::type` | public | — |

## Free functions and macros

| Name | Kind | Type / body | Description |
|---|---|---|---|
| `GPLATES_UTILS_SETCONST_H` | macro | `None` | — |

## Notes

[[[PROSE notes unit=utils/SetConst tier=2]]]
Replace this whole block, markers included, with invariants, ownership, threading or gotchas that are not visible in the tables. Write *None.* if there is nothing worth saying.
[[[/PROSE]]]

## Used by

| Unit | Component | References |
|---|---|---|
| [app-logic/LayerParamsVisitor](../app-logic/LayerParamsVisitor.md) | app-logic | 25 |
| [presentation/VisualLayerParamsVisitor](../presentation/VisualLayerParamsVisitor.md) | presentation | 22 |
| [gui/ColourPaletteVisitor](../gui/ColourPaletteVisitor.md) | gui | 19 |
| [gui/CptColourPalette](../gui/CptColourPalette.md) | gui | 10 |

## Related

*None.*

## Explore

Run these from the `gplates-code` skill directory:

```bash
python scripts/gpq.py file src/utils/SetConst.h
python scripts/gpq.py def GPlatesUtils::SetConst --body
python scripts/gpq.py uses SetConst --kind struct
python scripts/gpq.py hier SetConst
```
