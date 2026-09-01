# RasterPropertiesDialog

[Book TOC](../../TOC.md) · [qt-widgets](../../components/qt-widgets.md) · cluster Community 259 · tier 3

| Source file | Kind | Lines |
|---|---|---|
| `src/qt-widgets/RasterPropertiesDialog.h` | C++ | 122 |
| `src/qt-widgets/RasterPropertiesDialog.cc` | C++ | 503 |
| `src/qt-widgets/RasterPropertiesDialogUi.ui` | Qt form | 350 |

## Overview

Dialog for viewing and configuring raster properties and appearance. It displays basic raster information (filename, format, no-data value, statistics), allows users to set the spatial extent via an affine transform or lat-lon bounds, and provides controls for selecting or changing color maps (via CPT files or built-in defaults). Context-sensitive help is available for each section. The dialog is currently tightly coupled to `ViewState`; a FIXME indicates future refactoring to move raster management out of the presentation layer.

## Declared types

| Name | Kind | Bases | Template | Subclasses | Description |
|---|---|---|---|---|---|
| [`GPlatesQtWidgets::RasterPropertiesDialog`](#gplatesqtwidgetsrasterpropertiesdialog) | class | `QDialog`<br>`Ui_RasterPropertiesDialog` | — | 0 | — |

## Members

### `GPlatesQtWidgets::RasterPropertiesDialog`

| Member | Kind | Type | Access | Description |
|---|---|---|---|---|
| `RasterPropertiesDialog( GPlatesPresentation::ViewState *view_state, QWidget *parent_ = NULL)` | constructor | `None` | public | — |
| `populate_from_data()` | method | `void` | public | — |
| `handle_colour_map_lineedit_editing_finished()` | method | `void` | private | — |
| `handle_use_default_colour_map_button_clicked()` | method | `void` | private | — |
| `handle_open_cpt_button_clicked()` | method | `void` | private | — |
| `handle_extent_help_button_clicked()` | method | `void` | private | — |
| `handle_properties_help_button_clicked()` | method | `void` | private | — |
| `handle_colour_map_help_button_clicked()` | method | `void` | private | — |
| `handle_main_buttonbox_clicked( QAbstractButton *button)` | method | `void` | private | — |
| `make_signal_slot_connections()` | method | `void` | private | — |
| `enable_all_groupboxes( bool enabled)` | method | `void` | private | — |
| `set_raster_colour_map_filename( const QString &filename)` | method | `void` | private | — |
| `HelpContext` | enum | `None` | private | — |
| `show_help_dialog( HelpContext context)` | method | `void` | private | — |
| `d_view_state` | field | `GPlatesPresentation::ViewState` | private | FIXME: Remove after rasters are moved out of ViewState. |
| `d_georeferencing_widget` | field | `EditAffineTransformGeoreferencingWidget` | private | Memory managed by Qt. |
| `d_colour_map_lineedit` | field | `FriendlyLineEdit` | private | — |
| `d_help_dialog` | field | `InformationDialog` | private | — |

## Free functions and macros

| Name | Kind | Type / body | Description |
|---|---|---|---|
| `PROPERTIES_HELP_DIALOG_TITLE` | variable | `QString` | — |
| `PROPERTIES_HELP_DIALOG_TEXT` | variable | `QString` | — |
| `EXTENT_HELP_DIALOG_TITLE` | variable | `QString` | — |
| `EXTENT_HELP_DIALOG_TEXT` | variable | `QString` | — |
| `COLOUR_MAP_HELP_DIALOG_TITLE` | variable | `QString` | — |
| `COLOUR_MAP_HELP_DIALOG_TEXT` | variable | `QString` | — |
| `create_treewidget_item( const QString &property, const QString &value, bool set_tool_tip = false)` | function | `QTreeWidgetItem` | — |
| `create_numeric_treewidget_item( const QString &property, const boost::optional<double> &value, const QString &none_string = "(unknown)")` | function | `QTreeWidgetItem` | — |
| `GPLATES_QTWIDGETS_RASTERPROPERTIESDIALOG_H` | macro | `None` | — |

## Notes

The `ViewState` pointer must remain valid for the dialog's lifetime; see FIXME comment on `d_view_state`. The georeferencing widget is currently disabled (compiled out with `#if 0`). The `populate_from_data()` method must be called to populate the dialog before display.

## Used by

*Nothing in the tree references this unit.*

## Related

**Qt Designer forms**

| Form class | Base widget | Title | Widgets |
|---|---|---|---|
| `RasterPropertiesDialog` | `QDialog` | Raster Properties | 20 |

**Qt signal/slot connections** (7 in this unit)

| Sender | Signal | Receiver | Slot |
|---|---|---|---|
| `d_colour_map_lineedit` | `editingFinished()` | `this` | `handle_colour_map_lineedit_editing_finished()` |
| `use_default_colour_map_button` | `clicked()` | `this` | `handle_use_default_colour_map_button_clicked()` |
| `open_cpt_button` | `clicked()` | `this` | `handle_open_cpt_button_clicked()` |
| `extent_help_button` | `clicked()` | `this` | `handle_extent_help_button_clicked()` |
| `properties_help_button` | `clicked()` | `this` | `handle_properties_help_button_clicked()` |
| `colour_map_help_button` | `clicked()` | `this` | `handle_colour_map_help_button_clicked()` |
| `main_buttonbox` | `clicked(QAbstractButton *)` | `this` | `handle_main_buttonbox_clicked(QAbstractButton *)` |


## Explore

Run these from the `gplates-code` skill directory:

```bash
python scripts/gpq.py file src/qt-widgets/RasterPropertiesDialog.h
python scripts/gpq.py def GPlatesQtWidgets::RasterPropertiesDialog --body
python scripts/gpq.py uses RasterPropertiesDialog --kind class
python scripts/gpq.py hier RasterPropertiesDialog
```
