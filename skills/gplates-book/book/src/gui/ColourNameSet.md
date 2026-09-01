# ColourNameSet

[Book TOC](../../TOC.md) · [gui](../../components/gui.md) · cluster Community 1265 · tier 2

| Source file | Kind | Lines |
|---|---|---|
| `src/gui/ColourNameSet.h` | C++ | 87 |
| `src/gui/ColourNameSet.cc` | C++ | 64 |

## Overview

[[[PROSE overview unit=gui/ColourNameSet tier=2]]]
Replace this whole block, markers included, with 1-3 paragraphs: what this unit is, why it exists, and how it fits the surrounding design. Do not restate the tables below.
[[[/PROSE]]]

## Declared types

| Name | Kind | Bases | Template | Subclasses | Description |
|---|---|---|---|---|---|
| [`GPlatesGui::ColourNameSet`](#gplatesguicolournameset) | class | `boost::noncopyable` | — | 2 | ColourNameSet is a base class for classes that map colour names to Colours. |

## Members

### `GPlatesGui::ColourNameSet`

| Member | Kind | Type | Access | Description |
|---|---|---|---|---|
| `~ColourNameSet()` | destructor | `None` | public | Destructor |
| `get_colour( const std::string &name)` | method | `boost::optional<Colour>` | public | Retrieves a colour by name. |
| `insert_colour( const std::string &name, int r, int g, int b)` | method | `void` | protected | — |
| `colours` | field | `std::map<std::string, Colour>` | private | — |
| `d_color_name_table` | field | `std::map<std::string, std::vector<int> >` | private | — |

## Free functions and macros

| Name | Kind | Type / body | Description |
|---|---|---|---|
| `GPLATES_GUI_COLOURNAMESET_H` | macro | `None` | — |

## Notes

[[[PROSE notes unit=gui/ColourNameSet tier=2]]]
Replace this whole block, markers included, with invariants, ownership, threading or gotchas that are not visible in the tables. Write *None.* if there is nothing worth saying.
[[[/PROSE]]]

## Used by

| Unit | Component | References |
|---|---|---|
| [gui/GMTColourNames](GMTColourNames.md) | gui | 666 |
| [gui/HTMLColourNames](HTMLColourNames.md) | gui | 142 |
| [unit-test/CptPaletteTest](../unit-test/CptPaletteTest.md) | unit-test | 5 |
| [file-io/CptReader](../file-io/CptReader.md) | file-io | 1 |

## Related

*None.*

## Explore

Run these from the `gplates-code` skill directory:

```bash
python scripts/gpq.py file src/gui/ColourNameSet.h
python scripts/gpq.py def GPlatesGui::ColourNameSet --body
python scripts/gpq.py uses ColourNameSet --kind class
python scripts/gpq.py hier ColourNameSet
```
