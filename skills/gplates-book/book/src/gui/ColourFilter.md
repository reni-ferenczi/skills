# ColourFilter

[Book TOC](../../TOC.md) · [gui](../../components/gui.md) · cluster Community 640 · tier 3

| Source file | Kind | Lines |
|---|---|---|
| `src/gui/ColourFilter.h` | C++ | 60 |

## Overview

An abstract base class for colour transformation filters used within the colour proxy system. Concrete subclasses implement the pure virtual `change_colour()` method to apply custom colour transformations to the output of `ColourScheme` objects. This allows composable modifications to colours without coupling the colour schemes themselves to specific filtering logic.

## Declared types

| Name | Kind | Bases | Template | Subclasses | Description |
|---|---|---|---|---|---|
| [`GPlatesGui::ColourFilter`](#gplatesguicolourfilter) | class | — | — | 0 | Base class for classes that modify the output from ColourSchemes. |

## Members

### `GPlatesGui::ColourFilter`

| Member | Kind | Type | Access | Description |
|---|---|---|---|---|
| `~ColourFilter()` | destructor | `None` | public | Virtual destructor |
| `change_colour` | field | `Colour` | public | Maps input\_colour to another colour. |

## Free functions and macros

| Name | Kind | Type / body | Description |
|---|---|---|---|
| `GPLATES_GUI_COLOURFILTER_H` | macro | `None` | — |

## Notes

*None.*

## Used by

| Unit | Component | References |
|---|---|---|
| [gui/ColourProxy](ColourProxy.md) | gui | 8 |

## Related

*None.*

## Explore

Run these from the `gplates-code` skill directory:

```bash
python scripts/gpq.py file src/gui/ColourFilter.h
python scripts/gpq.py def GPlatesGui::ColourFilter --body
python scripts/gpq.py uses ColourFilter --kind class
python scripts/gpq.py hier ColourFilter
```
