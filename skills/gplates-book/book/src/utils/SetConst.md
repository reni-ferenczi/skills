# SetConst

[Book TOC](../../TOC.md) · [utils](../../components/utils.md) · cluster Community 189 · tier 2

| Source file | Kind | Lines |
|---|---|---|
| `src/utils/SetConst.h` | C++ | 53 |

## Overview

`SetConst<T, Const>::type` normalizes the top-level const-ness of `T` to match the boolean `Const`: `true` yields `boost::add_const<T>::type`, `false` (the primary template) yields `boost::remove_const<T>::type`. It is a small building block for templates that are parameterized on a `Const` flag and need to declare a pointer, reference or parameter type whose constness tracks that flag — for example generating both a mutable and a const-visitor from the same template body, which is how the `LayerParamsVisitor`, `VisualLayerParamsVisitor` and `ColourPaletteVisitor` families use it to avoid duplicating a visitor class for its const and non-const variants.

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

*None.*

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
