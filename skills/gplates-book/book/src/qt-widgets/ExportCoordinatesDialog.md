# ExportCoordinatesDialog

[Book TOC](../../TOC.md) · [qt-widgets](../../components/qt-widgets.md) · cluster Community 1110 · tier 3

| Source file | Kind | Lines |
|---|---|---|
| `src/qt-widgets/ExportCoordinatesDialog.h` | C++ | 163 |
| `src/qt-widgets/ExportCoordinatesDialog.cc` | C++ | 437 |
| `src/qt-widgets/ExportCoordinatesDialogUi.ui` | Qt form | 524 |

## Overview

`ExportCoordinatesDialog` is a modal dialog for exporting a single geometry (point, line, or polygon) to a coordinate file in one of six formats: PLATES4, GMT, OGR GMT, Shapefile, WKT, or CSV. The user supplies a geometry via `set_geometry_and_display()`, selects a format and output file from the dialog, and clicks Export.

The dialog delegates to `GeometryExporter` subclasses (e.g., `GMTFormatGeometryExporter`, `OgrGeometryExporter`) to handle the actual encoding. Options like coordinate order (latitude-longitude vs. longitude-latitude) are available as checkboxes, and polygon terminating points can be toggled with an explanatory information dialog.

## Declared types

| Name | Kind | Bases | Template | Subclasses | Description |
|---|---|---|---|---|---|
| [`(anonymous)::geometry_opt_ptr_type`](#anonymousgeometry_opt_ptr_type) | typedef | — | — | 0 | This typedef is used wherever geometry (of some unknown type) is expected. |
| [`GPlatesQtWidgets::ExportCoordinatesDialog`](#gplatesqtwidgetsexportcoordinatesdialog) | class | `QDialog`<br>`Ui_ExportCoordinatesDialog` | — | 0 | — |

## Members

### `(anonymous)::geometry_opt_ptr_type`

*None.*

### `GPlatesQtWidgets::ExportCoordinatesDialog`

| Member | Kind | Type | Access | Description |
|---|---|---|---|---|
| `OutputFormat` | enum | `None` | public | Enumeration for the possible formats to export to. |
| `ExportCoordinatesDialog( GPlatesPresentation::ViewState &view_state, QWidget *parent_ = NULL)` | constructor | `None` | public | — |
| `set_geometry_and_display( GPlatesMaths::GeometryOnSphere::non_null_ptr_to_const_type geometry_)` | method | `bool` | public | Rather than simply exec()ing the dialog, you should call this method to ensure you are feeding the ExportCoordinatesDialog some valid geometry at the same time. |
| `handle_format_selection( int idx)` | method | `void` | private | Fired when user (or code..) selects a format from the combobox. |
| `handle_export()` | method | `void` | private | The slot that gets called when the user clicks the Export button. |
| `CoordinateOrder` | enum | `None` | private | Enumeration for the order of coordinates to export with. |
| `d_geometry_opt_ptr` | field | `boost::optional<GPlatesMaths::GeometryOnSphere::non_null_ptr_to_const_type>` | private | The geometry that is to be exported when the user clicks the Export button and triggers the handle\_export() slot. |
| `d_view_state_ref` | field | `GPlatesPresentation::ViewState` | private | — |
| `d_terminating_point_information_dialog` | field | `InformationDialog` | private | The small information dialog that pops up to explain the reason for the checkbox\_polygon\_terminating\_point option. |
| `s_terminating_point_information_text` | field | `QString` | private | The text of the terminating point information dialog. |
| `export_geometry_to_file( OutputFormat format, QString &filename)` | method | `void` | private | Export geometry in specified format. |
| `export_geometry_to_text_stream( OutputFormat format, QTextStream &text_stream)` | method | `void` | private | Export geometry in specified format. |

## Free functions and macros

| Name | Kind | Type / body | Description |
|---|---|---|---|
| `get_filter_list_from_format( const GPlatesQtWidgets::ExportCoordinatesDialog::OutputFormat &format)` | function | `GPlatesQtWidgets::SaveFileDialog::filter_list_type` | — |
| `get_filters()` | function | `GPlatesQtWidgets::SaveFileDialog::filter_list_type` | — |
| `s_terminating_point_information_text` | variable | `QString` | — |
| `GPLATES_QTWIDGETS_EXPORTCOORDINATESDIALOG_H` | macro | `None` | — |

## Notes

*None.*

## Used by

| Unit | Component | References |
|---|---|---|
| [gui/TopologyTools](../gui/TopologyTools.md) | gui | 1 |
| [qt-widgets/DigitisationWidget](DigitisationWidget.md) | qt-widgets | 1 |

## Related

**Qt Designer forms**

| Form class | Base widget | Title | Widgets |
|---|---|---|---|
| `ExportCoordinatesDialog` | `QDialog` | Export Coordinates | 28 |

**Qt signal/slot connections** (3 in this unit)

| Sender | Signal | Receiver | Slot |
|---|---|---|---|
| `combobox_format` | `currentIndexChanged(int)` | `this` | `handle_format_selection(int)` |
| `button_explain_terminating_point` | `clicked()` | `d_terminating_point_information_dialog` | `show()` |
| `buttonbox_export` | `accepted()` | `this` | `handle_export()` |


## Explore

Run these from the `gplates-code` skill directory:

```bash
python scripts/gpq.py file src/qt-widgets/ExportCoordinatesDialog.h
python scripts/gpq.py def GPlatesQtWidgets::ExportCoordinatesDialog --body
python scripts/gpq.py uses ExportCoordinatesDialog --kind class
python scripts/gpq.py hier ExportCoordinatesDialog
```
