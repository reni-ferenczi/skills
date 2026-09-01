# ColourNameSet

[Book TOC](../../TOC.md) · [gui](../../components/gui.md) · cluster Community 1265 · tier 2

| Source file | Kind | Lines |
|---|---|---|
| `src/gui/ColourNameSet.h` | C++ | 87 |
| `src/gui/ColourNameSet.cc` | C++ | 64 |

## Overview

A small base class for a static, named colour table — the pattern used by
`GMTColourNames` and `HTMLColourNames` to expose their large hard-coded lists
of colour-name-to-RGB mappings (GMT's and HTML/CSS's, respectively) behind a
common lookup interface. Subclasses populate the table once, in their
constructor, via repeated `insert_colour(name, r, g, b)` calls; callers then
look a name up with `get_colour()`, which returns `boost::none` for an
unrecognised name rather than throwing.

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

`insert_colour` writes into two parallel maps: `colours` (as a `Colour`, with
components normalised from 0-255 ints to floats) and `d_color_name_table`
(the raw `{r, g, b}` ints, exposed read-only via `get_name_map()`). Both are
kept in sync only because every entry goes through `insert_colour` — a
subclass that touches either map directly would desynchronise them.

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
