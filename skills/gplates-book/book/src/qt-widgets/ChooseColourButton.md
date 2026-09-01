# ChooseColourButton

[Book TOC](../../TOC.md) · [qt-widgets](../../components/qt-widgets.md) · cluster Community 1713 · tier 2

| Source file | Kind | Lines |
|---|---|---|
| `src/qt-widgets/ChooseColourButton.h` | C++ | 81 |
| `src/qt-widgets/ChooseColourButton.cc` | C++ | 84 |

## Overview

[[[PROSE overview unit=qt-widgets/ChooseColourButton tier=2]]]
Replace this whole block, markers included, with 1-3 paragraphs: what this unit is, why it exists, and how it fits the surrounding design. Do not restate the tables below.
[[[/PROSE]]]

## Declared types

| Name | Kind | Bases | Template | Subclasses | Description |
|---|---|---|---|---|---|
| [`GPlatesQtWidgets::ChooseColourButton`](#gplatesqtwidgetschoosecolourbutton) | class | `QToolButton` | — | 0 | — |

## Members

### `GPlatesQtWidgets::ChooseColourButton`

| Member | Kind | Type | Access | Description |
|---|---|---|---|---|
| `ChooseColourButton( QWidget *parent_ = NULL)` | constructor | `None` | public | — |
| `set_colour( const GPlatesGui::Colour &colour)` | method | `void` | public | Set the colour. |
| `colour_changed( GPlatesQtWidgets::ChooseColourButton &)` | method | `void` | public | Emitted if user changes colour via GUI or if set\_colour is explicitly called. |
| `handle_clicked()` | method | `void` | private | — |
| `d_colour` | field | `GPlatesGui::Colour` | private | — |

## Free functions and macros

| Name | Kind | Type / body | Description |
|---|---|---|---|
| `GPLATES_QTWIDGETS_CHOOSECOLOURBUTTON_H` | macro | `None` | — |

## Notes

[[[PROSE notes unit=qt-widgets/ChooseColourButton tier=2]]]
Replace this whole block, markers included, with invariants, ownership, threading or gotchas that are not visible in the tables. Write *None.* if there is nothing worth saying.
[[[/PROSE]]]

## Used by

| Unit | Component | References |
|---|---|---|
| [qt-widgets/ConfigureCanvasToolGeometryRenderParametersDialog](ConfigureCanvasToolGeometryRenderParametersDialog.md) | qt-widgets | 24 |
| [qt-widgets/ConfigureGraticulesDialog](ConfigureGraticulesDialog.md) | qt-widgets | 6 |
| [qt-widgets/ConfigureTextOverlayDialog](ConfigureTextOverlayDialog.md) | qt-widgets | 6 |

## Related

**Qt signal/slot connections** (1 in this unit)

| Sender | Signal | Receiver | Slot |
|---|---|---|---|
| `this` | `clicked()` | `this` | `handle_clicked()` |


## Explore

Run these from the `gplates-code` skill directory:

```bash
python scripts/gpq.py file src/qt-widgets/ChooseColourButton.h
python scripts/gpq.py def GPlatesQtWidgets::ChooseColourButton --body
python scripts/gpq.py uses ChooseColourButton --kind class
python scripts/gpq.py hier ChooseColourButton
```
