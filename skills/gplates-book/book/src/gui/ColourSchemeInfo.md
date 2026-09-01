# ColourSchemeInfo

[Book TOC](../../TOC.md) · [gui](../../components/gui.md) · cluster Community 713 · tier 2

| Source file | Kind | Lines |
|---|---|---|
| `src/gui/ColourSchemeInfo.h` | C++ | 83 |

## Overview

`ColourSchemeInfo` is a plain-data record pairing a `ColourScheme::non_null_ptr_type` with the metadata `ColourSchemeContainer` needs to present it in the UI: a short label for the colouring dialog's preview caption, a longer description for its tooltip, and an `is_built_in` flag distinguishing schemes shipped with GPlates (which cannot be removed) from user-created ones. It exists purely to keep this bundle together as a single value inside `ColourSchemeContainer`'s per-category maps.

## Declared types

| Name | Kind | Bases | Template | Subclasses | Description |
|---|---|---|---|---|---|
| [`GPlatesGui::ColourSchemeInfo`](#gplatesguicolourschemeinfo) | struct | — | — | 0 | A convenience structure for use by ColourSchemeContainer to hold information about a loaded colour scheme. |

## Members

### `GPlatesGui::ColourSchemeInfo`

| Member | Kind | Type | Access | Description |
|---|---|---|---|---|
| `ColourSchemeInfo( ColourScheme::non_null_ptr_type colour_scheme_ptr_, QString short_description_, QString long_description_, bool is_built_in_)` | constructor | `None` | public | Constructs a ColourSchemeInfo. |
| `colour_scheme_ptr` | field | `ColourScheme::non_null_ptr_type` | public | A pointer to the colour scheme. |
| `short_description` | field | `QString` | public | A short, human-readable description of the colour scheme. |
| `long_description` | field | `QString` | public | A longer, human-readable description of the colour scheme. |
| `is_built_in` | field | `bool` | public | True if the colour scheme is a built-in scheme. |

## Free functions and macros

| Name | Kind | Type / body | Description |
|---|---|---|---|
| `GPLATES_GUI_COLOURSCHEMEINFO_H` | macro | `None` | — |

## Notes

*None.*

## Used by

| Unit | Component | References |
|---|---|---|
| [qt-widgets/ColouringDialog](../qt-widgets/ColouringDialog.md) | qt-widgets | 16 |
| [gui/ColourSchemeContainer](ColourSchemeContainer.md) | gui | 10 |

## Related

*None.*

## Explore

Run these from the `gplates-code` skill directory:

```bash
python scripts/gpq.py file src/gui/ColourSchemeInfo.h
python scripts/gpq.py def GPlatesGui::ColourSchemeInfo --body
python scripts/gpq.py uses ColourSchemeInfo --kind struct
python scripts/gpq.py hier ColourSchemeInfo
```
