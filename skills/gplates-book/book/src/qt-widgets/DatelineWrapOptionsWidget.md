# DatelineWrapOptionsWidget

[Book TOC](../../TOC.md) · [qt-widgets](../../components/qt-widgets.md) · cluster Community 235 · tier 2

| Source file | Kind | Lines |
|---|---|---|
| `src/qt-widgets/DatelineWrapOptionsWidget.h` | C++ | 74 |
| `src/qt-widgets/DatelineWrapOptionsWidget.cc` | C++ | 94 |
| `src/qt-widgets/DatelineWrapOptionsWidgetUi.ui` | Qt form | 81 |

## Overview

`DatelineWrapOptionsWidget` is a small, reusable options panel — a single
checkbox plus a help button — embedded by several export option widgets
(`ExportFlowlineOptionsWidget`, `ExportResolvedTopologyOptionsWidget` and others)
to let the user opt into clipping polyline and polygon geometries at the dateline
and wrapping the pieces to the other side. Its own `InformationDialog`, wired to
`push_button_help_dateline_wrap`, explains that wrapping is meant for ArcGIS
compatibility and is irreversible once a file is saved with it applied. The widget
holds no other state: `get_wrap_to_dateline()` reads the checkbox directly and
`set_options()`/`reset_options()` write it, so callers persist the option
themselves (typically in an export configuration).

## Declared types

| Name | Kind | Bases | Template | Subclasses | Description |
|---|---|---|---|---|---|
| [`GPlatesQtWidgets::DatelineWrapOptionsWidget`](#gplatesqtwidgetsdatelinewrapoptionswidget) | class | `QWidget`<br>`Ui_DatelineWrapOptionsWidget` | — | 0 | — |

## Members

### `GPlatesQtWidgets::DatelineWrapOptionsWidget`

| Member | Kind | Type | Access | Description |
|---|---|---|---|---|
| `DatelineWrapOptionsWidget( QWidget *parent_, bool wrap_to_dateline)` | constructor | `None` | public | — |
| `set_options( bool wrap_to_dateline)` | method | `void` | public | Set the initial options. |
| `get_wrap_to_dateline()` | method | `bool` | public | Get the wrap-to-dateline option. |
| `reset_options()` | method | `void` | public | Reset the options to their default values. |
| `d_help_dateline_wrap_dialog` | field | `InformationDialog` | private | — |

## Free functions and macros

| Name | Kind | Type / body | Description |
|---|---|---|---|
| `HELP_DATELINE_WRAP_DIALOG_TITLE` | variable | `QString` | — |
| `HELP_DATELINE_WRAP_DIALOG_TEXT` | variable | `QString` | — |
| `GPLATES_QT_WIDGETS_DATELINEWRAPOPTIONSWIDGET_H` | macro | `None` | — |

## Notes

*None.*

## Used by

| Unit | Component | References |
|---|---|---|
| [qt-widgets/ShapefileFileFormatConfigurationDialog](ShapefileFileFormatConfigurationDialog.md) | qt-widgets | 10 |
| [qt-widgets/ExportCitcomsResolvedTopologyOptionsWidget](ExportCitcomsResolvedTopologyOptionsWidget.md) | qt-widgets | 7 |
| [qt-widgets/ExportFlowlineOptionsWidget](ExportFlowlineOptionsWidget.md) | qt-widgets | 4 |
| [qt-widgets/ExportMotionPathOptionsWidget](ExportMotionPathOptionsWidget.md) | qt-widgets | 4 |
| [qt-widgets/ExportReconstructedGeometryOptionsWidget](ExportReconstructedGeometryOptionsWidget.md) | qt-widgets | 4 |
| [qt-widgets/ExportResolvedTopologyOptionsWidget](ExportResolvedTopologyOptionsWidget.md) | qt-widgets | 4 |
| [qt-widgets/ExportNetRotationOptionsWidget](ExportNetRotationOptionsWidget.md) | qt-widgets | 1 |

## Related

**Qt Designer forms**

| Form class | Base widget | Title | Widgets |
|---|---|---|---|
| `DatelineWrapOptionsWidget` | `QWidget` | Form | 4 |

**Qt signal/slot connections** (1 in this unit)

| Sender | Signal | Receiver | Slot |
|---|---|---|---|
| `push_button_help_dateline_wrap` | `clicked()` | `d_help_dateline_wrap_dialog` | `show()` |


## Explore

Run these from the `gplates-code` skill directory:

```bash
python scripts/gpq.py file src/qt-widgets/DatelineWrapOptionsWidget.h
python scripts/gpq.py def GPlatesQtWidgets::DatelineWrapOptionsWidget --body
python scripts/gpq.py uses DatelineWrapOptionsWidget --kind class
python scripts/gpq.py hier DatelineWrapOptionsWidget
```
