# HTMLColourNames

[Book TOC](../../TOC.md) · [gui](../../components/gui.md) · cluster Community 1265 · tier 2

| Source file | Kind | Lines |
|---|---|---|
| `src/gui/HTMLColourNames.h` | C++ | 50 |
| `src/gui/HTMLColourNames.cc` | C++ | 173 |

## Overview

[[[PROSE overview unit=gui/HTMLColourNames tier=2]]]
Replace this whole block, markers included, with 1-3 paragraphs: what this unit is, why it exists, and how it fits the surrounding design. Do not restate the tables below.
[[[/PROSE]]]

## Declared types

| Name | Kind | Bases | Template | Subclasses | Description |
|---|---|---|---|---|---|
| [`GPlatesGui::HTMLColourNames`](#gplatesguihtmlcolournames) | class | [`ColourNameSet`](ColourNameSet.md)<br>[`GPlatesUtils::Singleton<HTMLColourNames>`](../utils/Singleton.md) | — | 0 | This class maps colour names used by HTML to colours. |

## Members

### `GPlatesGui::HTMLColourNames`

*None.*

## Free functions and macros

| Name | Kind | Type / body | Description |
|---|---|---|---|
| `GPLATES_GUI_HTMLCOLOURNAMES_H` | macro | `None` | — |

## Notes

[[[PROSE notes unit=gui/HTMLColourNames tier=2]]]
Replace this whole block, markers included, with invariants, ownership, threading or gotchas that are not visible in the tables. Write *None.* if there is nothing worth saying.
[[[/PROSE]]]

## Used by

| Unit | Component | References |
|---|---|---|
| [gui/FeatureTypeColourPalette](FeatureTypeColourPalette.md) | gui | 20 |
| [gui/ColourSchemeContainer](ColourSchemeContainer.md) | gui | 6 |
| [presentation/VisualLayerRegistry](../presentation/VisualLayerRegistry.md) | presentation | 3 |
| [gui/Palette](Palette.md) | gui | 2 |
| [qt-widgets/ColouringDialog](../qt-widgets/ColouringDialog.md) | qt-widgets | 2 |
| [gui/DrawStyleManager](DrawStyleManager.md) | gui | 1 |
| [gui/PlateIdColourPalettes](PlateIdColourPalettes.md) | gui | 1 |
| [qt-widgets/DrawStyleDialog](../qt-widgets/DrawStyleDialog.md) | qt-widgets | 1 |

## Related

*None.*

## Explore

Run these from the `gplates-code` skill directory:

```bash
python scripts/gpq.py file src/gui/HTMLColourNames.h
python scripts/gpq.py def GPlatesGui::HTMLColourNames --body
python scripts/gpq.py uses HTMLColourNames --kind class
python scripts/gpq.py hier HTMLColourNames
```
