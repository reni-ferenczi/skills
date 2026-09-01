# HTMLColourNames

[Book TOC](../../TOC.md) · [gui](../../components/gui.md) · cluster Community 1265 · tier 2

| Source file | Kind | Lines |
|---|---|---|
| `src/gui/HTMLColourNames.h` | C++ | 50 |
| `src/gui/HTMLColourNames.cc` | C++ | 173 |

## Overview

`HTMLColourNames` is a `ColourNameSet` populated, entirely in its
constructor, with the standard set of CSS/HTML named colours (`"aliceblue"`,
`"antiquewhite"`, ... through the X11/HTML colour keyword list), each
registered via `insert_colour(name, r, g, b)`. As a `GPlatesUtils::Singleton`
it is constructed once and looked up by name wherever a colour palette needs
to resolve a colour keyword — feature-type and draw-style colouring in
particular.

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

*None.*

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
