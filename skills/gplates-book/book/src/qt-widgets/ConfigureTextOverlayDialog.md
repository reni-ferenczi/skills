# ConfigureTextOverlayDialog

[Book TOC](../../TOC.md) · [qt-widgets](../../components/qt-widgets.md) · cluster Community 1008 · tier 3

| Source file | Kind | Lines |
|---|---|---|
| `src/qt-widgets/ConfigureTextOverlayDialog.h` | C++ | 86 |
| `src/qt-widgets/ConfigureTextOverlayDialog.cc` | C++ | 112 |
| `src/qt-widgets/ConfigureTextOverlayDialogUi.ui` | Qt form | 269 |

## Overview

[[[PROSE overview unit=qt-widgets/ConfigureTextOverlayDialog tier=3]]]
Replace this whole block, markers included, with 1-3 paragraphs: what this unit is, why it exists, and how it fits the surrounding design. Do not restate the tables below.
[[[/PROSE]]]

## Declared types

| Name | Kind | Bases | Template | Subclasses | Description |
|---|---|---|---|---|---|
| [`GPlatesQtWidgets::ConfigureTextOverlayDialog`](#gplatesqtwidgetsconfiguretextoverlaydialog) | class | [`GPlatesDialog`](GPlatesDialog.md)<br>`Ui_ConfigureTextOverlayDialog` | — | 0 | — |

## Members

### `GPlatesQtWidgets::ConfigureTextOverlayDialog`

| Member | Kind | Type | Access | Description |
|---|---|---|---|---|
| `ConfigureTextOverlayDialog( QWidget *parent_ = NULL)` | constructor | `None` | public | — |
| `exec( GPlatesGui::TextOverlaySettings &settings)` | method | `int` | public | Shows the dialog modal to allow the user to modify the text overlay settings passed in as a mutable reference, settings. |
| `populate( const GPlatesGui::TextOverlaySettings &settings)` | method | `void` | private | — |
| `save( GPlatesGui::TextOverlaySettings &settings)` | method | `void` | private | — |
| `d_colour_button` | field | `ChooseColourButton` | private | — |
| `d_font_button` | field | `ChooseFontButton` | private | — |

## Free functions and macros

| Name | Kind | Type / body | Description |
|---|---|---|---|
| `GPLATES_QTWIDGETS_CONFIGURETEXTOVERLAYDIALOG_H` | macro | `None` | — |

## Notes

[[[PROSE notes unit=qt-widgets/ConfigureTextOverlayDialog tier=3]]]
Replace this whole block, markers included, with invariants, ownership, threading or gotchas that are not visible in the tables. Write *None.* if there is nothing worth saying.
[[[/PROSE]]]

## Used by

| Unit | Component | References |
|---|---|---|
| [gui/Dialogs](../gui/Dialogs.md) | gui | 1 |

## Related

**Qt Designer forms**

| Form class | Base widget | Title | Widgets |
|---|---|---|---|
| `ConfigureTextOverlayDialog` | `QDialog` | Configure Text Overlay | 21 |

**Qt signal/slot connections** (2 in this unit)

| Sender | Signal | Receiver | Slot |
|---|---|---|---|
| `main_buttonbox` | `accepted()` | `this` | `accept()` |
| `main_buttonbox` | `rejected()` | `this` | `reject()` |


## Explore

Run these from the `gplates-code` skill directory:

```bash
python scripts/gpq.py file src/qt-widgets/ConfigureTextOverlayDialog.h
python scripts/gpq.py def GPlatesQtWidgets::ConfigureTextOverlayDialog --body
python scripts/gpq.py uses ConfigureTextOverlayDialog --kind class
python scripts/gpq.py hier ConfigureTextOverlayDialog
```
