# ColourSchemeInfo

[Book TOC](../../TOC.md) · [gui](../../components/gui.md) · cluster Community 713 · tier 2

| Source file | Kind | Lines |
|---|---|---|
| `src/gui/ColourSchemeInfo.h` | C++ | 83 |

## Overview

[[[PROSE overview unit=gui/ColourSchemeInfo tier=2]]]
Replace this whole block, markers included, with 1-3 paragraphs: what this unit is, why it exists, and how it fits the surrounding design. Do not restate the tables below.
[[[/PROSE]]]

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

[[[PROSE notes unit=gui/ColourSchemeInfo tier=2]]]
Replace this whole block, markers included, with invariants, ownership, threading or gotchas that are not visible in the tables. Write *None.* if there is nothing worth saying.
[[[/PROSE]]]

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
