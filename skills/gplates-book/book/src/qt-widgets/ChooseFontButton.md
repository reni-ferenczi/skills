# ChooseFontButton

[Book TOC](../../TOC.md) · [qt-widgets](../../components/qt-widgets.md) · cluster Community 1650 · tier 3

| Source file | Kind | Lines |
|---|---|---|
| `src/qt-widgets/ChooseFontButton.h` | C++ | 68 |
| `src/qt-widgets/ChooseFontButton.cc` | C++ | 73 |

## Overview

Tool button for selecting a font, displaying the current font family and size on the button label. When clicked, opens a `QFontDialog` to choose a new font. Upon selection, updates the label with the new font details and visually previews the font on the button itself by setting the button's font to the selected font family with the application's default size (to prevent the button from becoming too large).

## Declared types

| Name | Kind | Bases | Template | Subclasses | Description |
|---|---|---|---|---|---|
| [`GPlatesQtWidgets::ChooseFontButton`](#gplatesqtwidgetschoosefontbutton) | class | `QToolButton` | — | 0 | — |

## Members

### `GPlatesQtWidgets::ChooseFontButton`

| Member | Kind | Type | Access | Description |
|---|---|---|---|---|
| `ChooseFontButton( QWidget *parent_ = NULL)` | constructor | `None` | public | — |
| `set_font( const QFont &font_)` | method | `void` | public | — |
| `handle_clicked()` | method | `void` | private | — |
| `d_font` | field | `QFont` | private | — |

## Free functions and macros

| Name | Kind | Type / body | Description |
|---|---|---|---|
| `GPLATES_QTWIDGETS_CHOOSEFONTBUTTON_H` | macro | `None` | — |

## Notes

*None.*

## Used by

| Unit | Component | References |
|---|---|---|
| [qt-widgets/ConfigureVelocityLegendOverlayDialog](ConfigureVelocityLegendOverlayDialog.md) | qt-widgets | 3 |
| [qt-widgets/ConfigureTextOverlayDialog](ConfigureTextOverlayDialog.md) | qt-widgets | 2 |

## Related

**Qt signal/slot connections** (1 in this unit)

| Sender | Signal | Receiver | Slot |
|---|---|---|---|
| `this` | `clicked()` | `this` | `handle_clicked()` |


## Explore

Run these from the `gplates-code` skill directory:

```bash
python scripts/gpq.py file src/qt-widgets/ChooseFontButton.h
python scripts/gpq.py def GPlatesQtWidgets::ChooseFontButton --body
python scripts/gpq.py uses ChooseFontButton --kind class
python scripts/gpq.py hier ChooseFontButton
```
