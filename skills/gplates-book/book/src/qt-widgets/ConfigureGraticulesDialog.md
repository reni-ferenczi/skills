# ConfigureGraticulesDialog

[Book TOC](../../TOC.md) · [qt-widgets](../../components/qt-widgets.md) · cluster Community 1500 · tier 3

| Source file | Kind | Lines |
|---|---|---|
| `src/qt-widgets/ConfigureGraticulesDialog.h` | C++ | 85 |
| `src/qt-widgets/ConfigureGraticulesDialog.cc` | C++ | 99 |
| `src/qt-widgets/ConfigureGraticulesDialogUi.ui` | Qt form | 176 |

## Overview

[[[PROSE overview unit=qt-widgets/ConfigureGraticulesDialog tier=3]]]
Replace this whole block, markers included, with 1-3 paragraphs: what this unit is, why it exists, and how it fits the surrounding design. Do not restate the tables below.
[[[/PROSE]]]

## Declared types

| Name | Kind | Bases | Template | Subclasses | Description |
|---|---|---|---|---|---|
| [`GPlatesQtWidgets::ConfigureGraticulesDialog`](#gplatesqtwidgetsconfiguregraticulesdialog) | class | [`GPlatesDialog`](GPlatesDialog.md)<br>`Ui_ConfigureGraticulesDialog` | — | 0 | — |

## Members

### `GPlatesQtWidgets::ConfigureGraticulesDialog`

| Member | Kind | Type | Access | Description |
|---|---|---|---|---|
| `ConfigureGraticulesDialog( QWidget *parent_ = NULL)` | constructor | `None` | public | — |
| `exec( GPlatesGui::GraticuleSettings &settings)` | method | `int` | public | Shows the dialog modal to allow the user to modify the graticule settings passed in as a mutable reference, settings. |
| `populate( const GPlatesGui::GraticuleSettings &settings)` | method | `void` | private | — |
| `save( GPlatesGui::GraticuleSettings &settings)` | method | `void` | private | — |
| `d_colour_button` | field | `ChooseColourButton` | private | — |

## Free functions and macros

| Name | Kind | Type / body | Description |
|---|---|---|---|
| `GPLATES_QTWIDGETS_CONFIGUREGRATICULESDIALOG_H` | macro | `None` | — |

## Notes

[[[PROSE notes unit=qt-widgets/ConfigureGraticulesDialog tier=3]]]
Replace this whole block, markers included, with invariants, ownership, threading or gotchas that are not visible in the tables. Write *None.* if there is nothing worth saying.
[[[/PROSE]]]

## Used by

| Unit | Component | References |
|---|---|---|
| [gui/Dialogs](../gui/Dialogs.md) | gui | 10 |

## Related

**Qt Designer forms**

| Form class | Base widget | Title | Widgets |
|---|---|---|---|
| `ConfigureGraticulesDialog` | `QDialog` | Configure Graticules | 12 |

**Qt signal/slot connections** (2 in this unit)

| Sender | Signal | Receiver | Slot |
|---|---|---|---|
| `main_buttonbox` | `accepted()` | `this` | `accept()` |
| `main_buttonbox` | `rejected()` | `this` | `reject()` |


## Explore

Run these from the `gplates-code` skill directory:

```bash
python scripts/gpq.py file src/qt-widgets/ConfigureGraticulesDialog.h
python scripts/gpq.py def GPlatesQtWidgets::ConfigureGraticulesDialog --body
python scripts/gpq.py uses ConfigureGraticulesDialog --kind class
python scripts/gpq.py hier ConfigureGraticulesDialog
```
