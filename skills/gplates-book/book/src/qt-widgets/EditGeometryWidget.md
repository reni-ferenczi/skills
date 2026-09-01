# EditGeometryWidget

[Book TOC](../../TOC.md) · [qt-widgets](../../components/qt-widgets.md) · cluster Community 377 · tier 2

| Source file | Kind | Lines |
|---|---|---|
| `src/qt-widgets/EditGeometryWidget.h` | C++ | 215 |
| `src/qt-widgets/EditGeometryWidget.cc` | C++ | 1052 |
| `src/qt-widgets/EditGeometryWidgetUi.ui` | Qt form | 290 |

## Overview

[[[PROSE overview unit=qt-widgets/EditGeometryWidget tier=2]]]
Replace this whole block, markers included, with 1-3 paragraphs: what this unit is, why it exists, and how it fits the surrounding design. Do not restate the tables below.
[[[/PROSE]]]

## Declared types

| Name | Kind | Bases | Template | Subclasses | Description |
|---|---|---|---|---|---|
| [`(anonymous)::geometry_opt_ptr_type`](#anonymousgeometry_opt_ptr_type) | typedef | — | — | 0 | This typedef is used wherever geometry (of some unknown type) is expected. |
| [`(anonymous)::polyline_type`](#anonymouspolyline_type) | typedef | — | — | 0 | FIXME: If the DigitisationWidget is any indication, ideally, we won't have to deal with specific GeometryOnSphere derivations at all - we'd just handle it with GeometryCreationUtils and maybe some visitors (for getting things into a ... |
| [`(anonymous)::polyline_ptr_type`](#anonymouspolyline_ptr_type) | typedef | — | — | 0 | — |
| [`(anonymous)::LatLonColumnLayout`](#anonymouslatloncolumnlayout) | enum | — | — | 0 | — |
| [`(anonymous)::TableRowValidity`](#anonymoustablerowvalidity) | enum | — | — | 0 | Enumeration of possible problems that may be encountered when converting table contents to GPlates geometry. |
| [`(anonymous)::InvalidTableRow`](#anonymousinvalidtablerow) | struct | — | — | 0 | Struct to pair a problem with the table row it was encountered on, for highlighting purposes. |
| [`(anonymous)::PolylineConstructionProblems`](#anonymouspolylineconstructionproblems) | struct | — | — | 0 | Struct to be passed around when constructing polylines to accumulate all problems encountered when converting the QTableWidget to geometry. |
| [`GPlatesQtWidgets::EditGeometryWidget`](#gplatesqtwidgetseditgeometrywidget) | class | [`AbstractEditWidget`](AbstractEditWidget.md)<br>[`EditTableWidget`](EditTableWidget.md)<br>`Ui_EditGeometryWidget` | — | 0 | — |

## Members

### `(anonymous)::geometry_opt_ptr_type`

*None.*

### `(anonymous)::polyline_type`

*None.*

### `(anonymous)::polyline_ptr_type`

*None.*

### `(anonymous)::LatLonColumnLayout`

| Member | Kind | Type | Access | Description |
|---|---|---|---|---|
| `COLUMN_LAT` | enumerator | `None` | — | — |
| `COLUMN_LON` | enumerator | `None` | — | — |
| `COLUMN_ACTION` | enumerator | `None` | — | — |

### `(anonymous)::TableRowValidity`

| Member | Kind | Type | Access | Description |
|---|---|---|---|---|
| `VALID` | enumerator | `None` | — | — |
| `UNPARSEABLE_LAT` | enumerator | `None` | — | — |
| `UNPARSEABLE_LON` | enumerator | `None` | — | — |
| `INVALID_TABLE_ITEM_LAT` | enumerator | `None` | — | — |
| `INVALID_TABLE_ITEM_LON` | enumerator | `None` | — | — |
| `INVALID_LAT_LON_POINT` | enumerator | `None` | — | — |

### `(anonymous)::InvalidTableRow`

| Member | Kind | Type | Access | Description |
|---|---|---|---|---|
| `row` | field | `int` | public | — |
| `reason` | field | `TableRowValidity` | public | — |

### `(anonymous)::PolylineConstructionProblems`

| Member | Kind | Type | Access | Description |
|---|---|---|---|---|
| `polyline_validity` | field | `GPlatesMaths::PolylineOnSphere::ConstructionParameterValidity` | public | — |
| `validity` | field | `GPlatesUtils::GeometryConstruction::GeometryConstructionValidity` | public | — |
| `invalid_rows` | field | `std::vector<InvalidTableRow>` | public | — |

### `GPlatesQtWidgets::EditGeometryWidget`

| Member | Kind | Type | Access | Description |
|---|---|---|---|---|
| `EditGeometryWidget( QWidget *parent_ = NULL)` | constructor | `None` | public | — |
| `reset_widget_to_default_values()` | method | `void` | public | — |
| `configure_for_property_value_type( const GPlatesPropertyValues::StructuralType &property_value_type)` | method | `void` | public | — |
| `update_widget_from_line_string( GPlatesPropertyValues::GmlLineString &gml_line_string)` | method | `void` | public | — |
| `update_widget_from_multi_point( GPlatesPropertyValues::GmlMultiPoint &gml_multi_point)` | method | `void` | public | — |
| `update_widget_from_point( GPlatesPropertyValues::GmlPoint &gml_point)` | method | `void` | public | — |
| `update_widget_from_polygon( GPlatesPropertyValues::GmlPolygon &gml_polygon)` | method | `void` | public | — |
| `create_property_value_from_widget()` | method | `GPlatesModel::PropertyValue::non_null_ptr_type` | public | — |
| `update_property_value_from_widget()` | method | `bool` | public | — |
| `handle_insert_row_above( const EditTableActionWidget *action_widget)` | method | `void` | public | — |
| `handle_insert_row_below( const EditTableActionWidget *action_widget)` | method | `void` | public | — |
| `handle_delete_row( const EditTableActionWidget *action_widget)` | method | `void` | public | — |
| `append_point_to_table( double lat, double lon)` | method | `void` | public | Adds a new point to end of the current geometry in the table. |
| `handle_cell_changed(int row, int column)` | method | `void` | private | Fired when the data of a cell has been modified. |
| `append_point_clicked()` | method | `void` | private | Manages data entry focus for the "Append Point" widgets. |
| `handle_current_cell_changed( int currentRow, int currentColumn, int previousRow, int previousColumn)` | method | `void` | private | Creates an EditTableActionWidget item in the current row. |
| `get_row_for_action_widget( const EditTableActionWidget *action_widget)` | method | `int` | private | Finds the current table row associated with the EditTableActionWidget. |
| `insert_blank_point_into_table( int row)` | method | `void` | private | Adds a new blank point to the current geometry in the table. |
| `delete_point_from_table( int row)` | method | `void` | private | Removes a single point from the current geometry in the table. |
| `test_geometry_validity()` | method | `bool` | private | Does appropriate tests for the current geometry of the table, and updates the interface to provide feedback to the user. |
| `set_geometry_for_property_value()` | method | `bool` | private | Creates GeometryOnSphere and uses setters to place it inside the current PropertyValue being edited. |
| `d_geometry_type` | field | `GPlatesMaths::GeometryType::Value` | private | The type of geometry being edited. |
| `d_property_value_ptr` | field | `boost::intrusive_ptr<GPlatesModel::PropertyValue>` | private | This boost::intrusive\_ptr is used to remember the property value which was last loaded into this editing widget. |

## Free functions and macros

| Name | Kind | Type / body | Description |
|---|---|---|---|
| `get_action_widget_for_row( QTableWidget &table, int row)` | function | `GPlatesQtWidgets::EditTableActionWidget` | Fetches the appropriate action widget given a row number. |
| `ensure_table_size( QTableWidget &table, int rows)` | function | `int` | Uses rowCount() and setRowCount() to ensure the table has at least rows rows available. |
| `populate_table_row_from_lat_lon( GPlatesQtWidgets::EditGeometryWidget &geometry_widget, QTableWidget &table, int row, double lat, double lon)` | function | `void` | Allocates QTableWidgetItems and populates a QTableWidget from a lat,lon pair. |
| `populate_table_row_with_blank_point( GPlatesQtWidgets::EditGeometryWidget *geometry_widget, QTableWidget &table, int row)` | function | `void` | Allocates QTableWidgetItems and populates a QTableWidget from a GPlatesMaths::PointOnSphere. |
| `populate_table_rows_from_polyline( GPlatesQtWidgets::EditGeometryWidget &geometry_widget, QTableWidget &table, int offset, GPlatesMaths::PolylineOnSphere::non_null_ptr_to_const_type polyline)` | function | `void` | Allocates QTableWidgetItems and populates a QTableWidget from a GPlatesMaths::PolylineOnSphere. |
| `populate_table_rows_from_multi_point( GPlatesQtWidgets::EditGeometryWidget &geometry_widget, QTableWidget &table, int offset, GPlatesMaths::MultiPointOnSphere::non_null_ptr_to_const_type multipoint)` | function | `void` | Allocates QTableWidgetItems and populates a QTableWidget from a GPlatesMaths::MultiPointOnSphere. |
| `populate_table_rows_from_point( GPlatesQtWidgets::EditGeometryWidget &geometry_widget, QTableWidget &table, int offset, const GPlatesMaths::PointOnSphere &point)` | function | `void` | Allocates QTableWidgetItems and populates a QTableWidget from a GPlatesMaths::PointOnSphere. |
| `populate_table_rows_from_polygon( GPlatesQtWidgets::EditGeometryWidget &geometry_widget, QTableWidget &table, int offset, GPlatesMaths::PolygonOnSphere::non_null_ptr_to_const_type polygon)` | function | `void` | Allocates QTableWidgetItems and populates a QTableWidget from a GPlatesMaths::PolygonOnSphere. |
| `build_points_from_table_rows( QTableWidget &table, int start_row, int length, std::vector<InvalidTableRow> &invalid_rows)` | function | `std::vector<GPlatesMaths::PointOnSphere>` | Goes through the points in the table and attempts to build a vector of PointOnSphere out of them. |
| `highlight_invalid_table_cells( QTableWidget &table, const std::vector<InvalidTableRow> &invalid_rows)` | function | `void` | Highlights any problematic table cells. |
| `display_validity_problems( QTableWidget &table, QLabel &label_error_feedback, const PolylineConstructionProblems &problems)` | function | `void` | Highlights table cells and updates labels to provide feedback to the user about GeometryOnSphere validity. |
| `create_geometry_on_sphere( const std::vector<GPlatesMaths::PointOnSphere> &points, GPlatesUtils::GeometryConstruction::GeometryConstructionValidity &validity, GPlatesMaths::GeometryType::Value geometry_type)` | function | `geometry_opt_ptr_type` | validity is a reference to a GeometryConstructionValidity that should be created by the caller and will be set by this function. |
| `test_polyline_on_sphere_validity( std::vector<GPlatesMaths::PointOnSphere> &points, PolylineConstructionProblems &problems)` | function | `bool` | Goes through the points in the table and tests if they make a valid PolylineOnSphere. |
| `work_around_table_graphical_glitch( GPlatesQtWidgets::EditGeometryWidget &edit_geometry_widget, QTableWidget &table)` | function | `void` | Work around a graphical glitch, where the EditTableActionWidgets around the recently scrolled-to row appear to be misaligned. |
| `GPLATES_QTWIDGETS_EDITGEOMETRYWIDGET_H` | macro | `None` | — |

## Notes

[[[PROSE notes unit=qt-widgets/EditGeometryWidget tier=2]]]
Replace this whole block, markers included, with invariants, ownership, threading or gotchas that are not visible in the tables. Write *None.* if there is nothing worth saying.
[[[/PROSE]]]

## Used by

| Unit | Component | References |
|---|---|---|
| [gui/FeaturePropertyTableModel](../gui/FeaturePropertyTableModel.md) | gui | 8 |
| [data-mining/DataSelector](../data-mining/DataSelector.md) | data-mining | 7 |
| [file-io/GpmlStructuralTypeReaderUtils](../file-io/GpmlStructuralTypeReaderUtils.md) | file-io | 7 |
| [gui/ConfigModel](../gui/ConfigModel.md) | gui | 6 |
| [qt-widgets/EditWidgetGroupBox](EditWidgetGroupBox.md) | qt-widgets | 6 |
| [app-logic/LogModel](../app-logic/LogModel.md) | app-logic | 5 |
| [qt-widgets/HellingerSegmentDialog](HellingerSegmentDialog.md) | qt-widgets | 5 |
| [qt-widgets/deprecated/CreateFeatureIdListModel](deprecated/CreateFeatureIdListModel.md) | qt-widgets | 5 |
| [app-logic/ReconstructMethodByPlateId](../app-logic/ReconstructMethodByPlateId.md) | app-logic | 4 |
| [gui/FeatureTableModel](../gui/FeatureTableModel.md) | gui | 4 |
| [qt-widgets/CoRegistrationResultTableDialog](CoRegistrationResultTableDialog.md) | qt-widgets | 4 |
| [qt-widgets/HellingerPickWidget](HellingerPickWidget.md) | qt-widgets | 4 |
| [qt-widgets/MergeReconstructionLayersDialog](MergeReconstructionLayersDialog.md) | qt-widgets | 4 |
| [qt-widgets/ScalarField3DDepthLayersPage](ScalarField3DDepthLayersPage.md) | qt-widgets | 4 |
| [qt-widgets/TimeDependentRasterPage](TimeDependentRasterPage.md) | qt-widgets | 4 |
| [app-logic/CoRegistrationLayerTask](../app-logic/CoRegistrationLayerTask.md) | app-logic | 3 |
| [app-logic/GenerateVelocityDomainTerra](../app-logic/GenerateVelocityDomainTerra.md) | app-logic | 3 |
| [data-mining/CoRegConfigurationTable](../data-mining/CoRegConfigurationTable.md) | data-mining | 3 |
| [qt-widgets/CreateFeaturePropertiesPage](CreateFeaturePropertiesPage.md) | qt-widgets | 3 |
| [qt-widgets/RasterBandPage](RasterBandPage.md) | qt-widgets | 3 |

*... and 14 more units.*

## Related

**Qt Designer forms**

| Form class | Base widget | Title | Widgets |
|---|---|---|---|
| `EditGeometryWidget` | `QWidget` | Form | 9 |

**Qt signal/slot connections** (3 in this unit)

| Sender | Signal | Receiver | Slot |
|---|---|---|---|
| `table_points` | `cellActivated(int, int)` | `this` | `handle_cell_changed(int, int)` |
| `button_append_point` | `clicked()` | `this` | `append_point_clicked()` |
| `table_points` | `currentCellChanged(int,int,int,int)` | `this` | `handle_current_cell_changed(int,int,int,int)` |


## Explore

Run these from the `gplates-code` skill directory:

```bash
python scripts/gpq.py file src/qt-widgets/EditGeometryWidget.h
python scripts/gpq.py def GPlatesQtWidgets::EditGeometryWidget --body
python scripts/gpq.py uses EditGeometryWidget --kind class
python scripts/gpq.py hier EditGeometryWidget
```
