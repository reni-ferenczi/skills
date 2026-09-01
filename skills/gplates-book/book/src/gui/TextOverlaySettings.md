# TextOverlaySettings

[Book TOC](../../TOC.md) · [gui](../../components/gui.md) · cluster Community 378 · tier 2

| Source file | Kind | Lines |
|---|---|---|
| `src/gui/TextOverlaySettings.h` | C++ | 208 |
| `src/gui/TextOverlaySettings.cc` | C++ | 84 |

## Overview

[[[PROSE overview unit=gui/TextOverlaySettings tier=2]]]
Replace this whole block, markers included, with 1-3 paragraphs: what this unit is, why it exists, and how it fits the surrounding design. Do not restate the tables below.
[[[/PROSE]]]

## Declared types

| Name | Kind | Bases | Template | Subclasses | Description |
|---|---|---|---|---|---|
| [`GPlatesGui::TextOverlaySettings`](#gplatesguitextoverlaysettings) | class | `boost::equality_comparable<TextOverlaySettings>` | — | 0 | — |

## Members

### `GPlatesGui::TextOverlaySettings`

| Member | Kind | Type | Access | Description |
|---|---|---|---|---|
| `Anchor` | enum | `None` | public | — |
| `TextOverlaySettings()` | constructor | `None` | public | Constructs a TextOverlaySettings with default values. |
| `set_text( const QString &text)` | method | `void` | public | — |
| `get_decimal_places()` | method | `int` | public | — |
| `set_decimal_places( int dp)` | method | `void` | public | — |
| `set_font( const QFont &font)` | method | `void` | public | — |
| `set_colour( const GPlatesGui::Colour &colour)` | method | `void` | public | — |
| `get_anchor()` | method | `Anchor` | public | — |
| `set_anchor( Anchor anchor)` | method | `void` | public | — |
| `get_x_offset()` | method | `int` | public | — |
| `set_x_offset( int x_offset)` | method | `void` | public | — |
| `get_y_offset()` | method | `int` | public | — |
| `set_y_offset( int y_offset)` | method | `void` | public | — |
| `is_enabled()` | method | `bool` | public | — |
| `set_enabled( bool enabled)` | method | `void` | public | — |
| `has_shadow()` | method | `bool` | public | — |
| `set_shadow( bool shadow)` | method | `void` | public | — |
| `DEFAULT_TEXT` | field | `char` | public | — |
| `DEFAULT_DECIMAL_PLACES` | field | `int` | public | — |
| `DEFAULT_COLOUR` | field | `GPlatesGui::Colour` | public | — |
| `DEFAULT_ANCHOR` | field | `Anchor` | public | — |
| `DEFAULT_X_OFFSET` | field | `int` | public | — |
| `DEFAULT_Y_OFFSET` | field | `int` | public | — |
| `DEFAULT_IS_ENABLED` | field | `bool` | public | — |
| `DEFAULT_HAS_SHADOW` | field | `bool` | public | — |
| `d_text` | field | `QString` | private | — |
| `d_decimal_places` | field | `int` | private | — |
| `d_font` | field | `QFont` | private | — |
| `d_colour` | field | `GPlatesGui::Colour` | private | — |
| `d_anchor` | field | `Anchor` | private | — |
| `d_x_offset` | field | `int` | private | — |
| `d_y_offset` | field | `int` | private | — |
| `d_is_enabled` | field | `bool` | private | — |
| `d_has_shadow` | field | `bool` | private | — |

## Free functions and macros

| Name | Kind | Type / body | Description |
|---|---|---|---|
| `DEFAULT_TEXT` | variable | `char` | — |
| `DEFAULT_DECIMAL_PLACES` | variable | `int` | — |
| `DEFAULT_COLOUR` | variable | `GPlatesGui::Colour` | — |
| `DEFAULT_ANCHOR` | variable | `GPlatesGui::TextOverlaySettings::Anchor` | — |
| `DEFAULT_X_OFFSET` | variable | `int` | — |
| `DEFAULT_Y_OFFSET` | variable | `int` | — |
| `DEFAULT_IS_ENABLED` | variable | `bool` | — |
| `DEFAULT_HAS_SHADOW` | variable | `bool` | — |
| `get_default_font()` | function | `QFont` | — |
| `GPLATES_GUI_TEXTOVERLAYSETTINGS_H` | macro | `None` | — |

## Notes

[[[PROSE notes unit=gui/TextOverlaySettings tier=2]]]
Replace this whole block, markers included, with invariants, ownership, threading or gotchas that are not visible in the tables. Write *None.* if there is nothing worth saying.
[[[/PROSE]]]

## Used by

| Unit | Component | References |
|---|---|---|
| [qt-widgets/ConfigureTextOverlayDialog](../qt-widgets/ConfigureTextOverlayDialog.md) | qt-widgets | 23 |
| [gui/TextOverlay](TextOverlay.md) | gui | 14 |
| [presentation/ViewState](../presentation/ViewState.md) | presentation | 4 |

## Related

*None.*

## Explore

Run these from the `gplates-code` skill directory:

```bash
python scripts/gpq.py file src/gui/TextOverlaySettings.h
python scripts/gpq.py def GPlatesGui::TextOverlaySettings --body
python scripts/gpq.py uses TextOverlaySettings --kind class
python scripts/gpq.py hier TextOverlaySettings
```
