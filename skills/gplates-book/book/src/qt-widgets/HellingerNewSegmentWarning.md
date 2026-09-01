# HellingerNewSegmentWarning

[Book TOC](../../TOC.md) · [qt-widgets](../../components/qt-widgets.md) · cluster Community 915 · tier 3

| Source file | Kind | Lines |
|---|---|---|
| `src/qt-widgets/HellingerNewSegmentWarning.h` | C++ | 87 |
| `src/qt-widgets/HellingerNewSegmentWarning.cc` | C++ | 115 |
| `src/qt-widgets/HellingerNewSegmentWarningUi.ui` | Qt form | 162 |

## Overview

Warning dialog that appears during Hellinger segment picking when the user attempts to create a segment that already exists. The dialog offers three options: add picks to the existing segment, replace the segment's picks entirely, or insert the new segment at that position and renumber the following segments. The user selects an action via radio buttons and the dialog returns the choice as a `NewSegmentActionType` enum value.

The `initialise()` method is called before displaying the dialog to configure the radio button labels with the specific segment number and reset the selection to a default state (insert by default). The dialog enforces that the user makes an explicit choice by initially leaving all buttons unchecked; the OK button becomes enabled only after a radio button is clicked.

## Declared types

| Name | Kind | Bases | Template | Subclasses | Description |
|---|---|---|---|---|---|
| [`GPlatesQtWidgets::NewSegmentActionType`](#gplatesqtwidgetsnewsegmentactiontype) | enum | — | — | 0 | — |
| [`GPlatesQtWidgets::HellingerNewSegmentWarning`](#gplatesqtwidgetshellingernewsegmentwarning) | class | `QDialog`<br>`Ui_HellingerNewSegmentWarning` | — | 0 | — |

## Members

### `GPlatesQtWidgets::NewSegmentActionType`

| Member | Kind | Type | Access | Description |
|---|---|---|---|---|
| `ACTION_ADD_TO_EXISTING_SEGMENT` | enumerator | `None` | — | — |
| `ACTION_REPLACE_SEGMENT` | enumerator | `None` | — | — |
| `ACTION_INSERT_NEW_SEGMENT` | enumerator | `None` | — | — |
| `ACTION_CANCEL` | enumerator | `None` | — | — |

### `GPlatesQtWidgets::HellingerNewSegmentWarning`

| Member | Kind | Type | Access | Description |
|---|---|---|---|---|
| `HellingerNewSegmentWarning( QWidget *parent_ = NULL)` | constructor | `None` | public | — |
| `error_type_new_segment()` | method | `int` | public | — |
| `initialise( int segment_number)` | method | `void` | public | initialise\_buttons Uncheck all the radio buttons so the user is forced to make a choice. |
| `handle_ok()` | method | `void` | private | — |
| `handle_radio_button_clicked()` | method | `void` | private | — |
| `handle_cancel()` | method | `void` | private | — |
| `d_type_error_new_segment` | field | `int` | private | — |
| `d_radio_button_group` | field | `QButtonGroup` | private | — |

## Free functions and macros

| Name | Kind | Type / body | Description |
|---|---|---|---|
| `GPLATES_QTWIDGETS_HELLINGERNEWSEGMENTWARNING_H` | macro | `None` | — |

## Notes

*None.*

## Used by

| Unit | Component | References |
|---|---|---|
| [qt-widgets/HellingerSegmentDialog](HellingerSegmentDialog.md) | qt-widgets | 11 |

## Related

**Qt Designer forms**

| Form class | Base widget | Title | Widgets |
|---|---|---|---|
| `HellingerNewSegmentWarning` | `QDialog` | New Segment Warning | 7 |

**Qt signal/slot connections** (3 in this unit)

| Sender | Signal | Receiver | Slot |
|---|---|---|---|
| `button_ok` | `clicked()` | `this` | `handle_ok()` |
| `button_cancel` | `clicked()` | `this` | `handle_cancel()` |
| `&d_radio_button_group` | `buttonClicked(QAbstractButton*)` | `this` | `handle_radio_button_clicked()` |


## Explore

Run these from the `gplates-code` skill directory:

```bash
python scripts/gpq.py file src/qt-widgets/HellingerNewSegmentWarning.h
python scripts/gpq.py def GPlatesQtWidgets::HellingerNewSegmentWarning --body
python scripts/gpq.py uses HellingerNewSegmentWarning --kind class
python scripts/gpq.py hier HellingerNewSegmentWarning
```
