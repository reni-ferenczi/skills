# GMTColourNames

[Book TOC](../../TOC.md) · [gui](../../components/gui.md) · cluster Community 1265 · tier 3

| Source file | Kind | Lines |
|---|---|---|
| `src/gui/GMTColourNames.h` | C++ | 50 |
| `src/gui/GMTColourNames.cc` | C++ | 696 |

## Overview

A singleton `ColourNameSet` that maps GMT color names (as defined in `man gmtcolors`) to their RGB values. The class populates itself in its constructor with the complete set of GMT named colors, providing a lookup table for applications that need to parse color specifications from GMT color palette (`.cpt`) files or other GMT-compatible data sources.

## Declared types

| Name | Kind | Bases | Template | Subclasses | Description |
|---|---|---|---|---|---|
| [`GPlatesGui::GMTColourNames`](#gplatesguigmtcolournames) | class | [`ColourNameSet`](ColourNameSet.md)<br>[`GPlatesUtils::Singleton<GMTColourNames>`](../utils/Singleton.md) | — | 0 | This class maps colour names used by GMT to colours. |

## Members

### `GPlatesGui::GMTColourNames`

*None.*

## Free functions and macros

| Name | Kind | Type / body | Description |
|---|---|---|---|
| `GPLATES_GUI_GMTCOLOURNAMES_H` | macro | `None` | — |

## Notes

*None.*

## Used by

| Unit | Component | References |
|---|---|---|
| [file-io/CptReader](../file-io/CptReader.md) | file-io | 3 |
| [gui/Palette](Palette.md) | gui | 2 |

## Related

*None.*

## Explore

Run these from the `gplates-code` skill directory:

```bash
python scripts/gpq.py file src/gui/GMTColourNames.h
python scripts/gpq.py def GPlatesGui::GMTColourNames --body
python scripts/gpq.py uses GMTColourNames --kind class
python scripts/gpq.py hier GMTColourNames
```
