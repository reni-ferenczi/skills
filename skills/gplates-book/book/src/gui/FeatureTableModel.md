# FeatureTableModel

[Book TOC](../../TOC.md) · [gui](../../components/gui.md) · cluster Community 218 · tier 2

| Source file | Kind | Lines |
|---|---|---|
| `src/gui/FeatureTableModel.h` | C++ | 374 |
| `src/gui/FeatureTableModel.cc` | C++ | 922 |

## Overview

`FeatureTableModel` is the `QAbstractTableModel` behind the search-results and clicked-feature tables: each row is a `ReconstructionGeometryRow` wrapping a `GPlatesAppLogic::ReconstructionGeometry`, held in `d_sequence`, with columns such as feature type, plate ID, name and time range computed on demand by per-column accessor functions (`get_feature_type`, `get_plate_id`, `get_name`, `get_time_begin`, ...) driven by the static `column_heading_info_table` dispatch table. It always reports itself as flat/tabular (`parent()`/`index()`/`hasChildren()` are overridden to deny any tree structure) even though `QAbstractTableModel` never asks for a hierarchy, purely to make Views that probe for tree-ness behave.

The model tracks two independent kinds of change: `handle_feature_modified`, wired to `FeatureFocus::focused_feature_modified`, refreshes rows whose feature was just edited; `handle_rendered_geometry_collection_update`, wired to the `RenderedGeometryCollection`'s `collection_was_updated` signal, re-resolves each row's `ReconstructionGeometry` against the newly computed reconstruction (since a `ReconstructionGeometry` is only valid for the reconstruction it came from) by matching against the `RECONSTRUCTION_LAYER`'s current geometries via `find_reconstruction_geometries_observing_feature`, using `d_rendered_geometry_collection` as the short-list to avoid picking up stale or invisible geometries. Callers that mutate `geometry_sequence()` directly must bracket the change with the `sequence_about_to_be_changed`/`sequence_changed` or `begin_insert_features`/`end_insert_features` (and remove equivalents) pairs so Qt's views stay consistent.

## Declared types

| Name | Kind | Bases | Template | Subclasses | Description |
|---|---|---|---|---|---|
| [`(anonymous)::ColumnHeadingInfo`](#anonymouscolumnheadinginfo) | struct | — | — | 0 | — |
| [`(anonymous)::GeometryOnSphereSummaryAsStringVisitor`](#anonymousgeometryonspheresummaryasstringvisitor) | class | [`GPlatesMaths::ConstGeometryOnSphereVisitor`](../maths/ConstGeometryOnSphereVisitor.md) | — | 0 | This is a Visitor to obtain a summary of the geometry-on-sphere as a string. |
| [`GPlatesGui::FeatureTableModel`](#gplatesguifeaturetablemodel) | class | `QAbstractTableModel` | — | 0 | This class is used by Qt to map a FeatureWeakRefSequence to a QTableView. |

## Members

### `(anonymous)::ColumnHeadingInfo`

| Member | Kind | Type | Access | Description |
|---|---|---|---|---|
| `label` | field | `char` | public | — |
| `tooltip` | field | `char` | public | — |
| `width` | field | `int` | public | — |
| `resize_mode` | field | `QHeaderView::ResizeMode` | public | — |
| `accessor` | field | `table_cell_accessor_type` | public | — |
| `alignment` | field | `QFlags<Qt::AlignmentFlag>` | public | — |

### `(anonymous)::GeometryOnSphereSummaryAsStringVisitor`

| Member | Kind | Type | Access | Description |
|---|---|---|---|---|
| `GeometryOnSphereSummaryAsStringVisitor()` | constructor | `None` | public | — |
| `~GeometryOnSphereSummaryAsStringVisitor()` | destructor | `None` | public | — |
| `visit_multi_point_on_sphere( GPlatesMaths::MultiPointOnSphere::non_null_ptr_to_const_type multi_point_on_sphere)` | method | `void` | public | Override this function in your own derived class. |
| `visit_point_on_sphere( GPlatesMaths::PointGeometryOnSphere::non_null_ptr_to_const_type point_on_sphere)` | method | `void` | public | Override this function in your own derived class. |
| `visit_polygon_on_sphere( GPlatesMaths::PolygonOnSphere::non_null_ptr_to_const_type polygon_on_sphere)` | method | `void` | public | Override this function in your own derived class. |
| `visit_polyline_on_sphere( GPlatesMaths::PolylineOnSphere::non_null_ptr_to_const_type polyline_on_sphere)` | method | `void` | public | Override this function in your own derived class. |
| `d_string` | field | `QString` | private | — |

### `GPlatesGui::FeatureTableModel`

| Member | Kind | Type | Access | Description |
|---|---|---|---|---|
| `ReconstructionGeometryRow` | struct | `None` | public | A reconstruction geometry and information associated with it. |
| `geometry_sequence_type` | typedef | `std::vector<ReconstructionGeometryRow>` | public | Typedef for a sequence of reconstruction geometry rows. |
| `FeatureTableModel( FeatureFocus &feature_focus, GPlatesViewOperations::RenderedGeometryCollection &rendered_geometry_collection, QObject *parent_ = NULL)` | constructor | `None` | public | — |
| `rowCount( const QModelIndex &parent_ = QModelIndex())` | method | `int` | public | Qt Model/View function used to access row count, which will depend on the number of features in the FeatureWeakRefSequence. |
| `columnCount( const QModelIndex &parent_ = QModelIndex())` | method | `int` | public | Qt Model/View function used to access column count, which will be a fixed number. |
| `flags( const QModelIndex &idx)` | method | `Qt::ItemFlags` | public | Qt Model/View function used to access editable/selectable/etc status of cells. |
| `headerData( int section, Qt::Orientation orientation, int role = Qt::DisplayRole)` | method | `QVariant` | public | Qt Model/View function used to access header data, both horizontal and vertical. |
| `data( const QModelIndex &idx, int role)` | method | `QVariant` | public | Qt Model/View function used to access individual cells of data. |
| `parent( const QModelIndex &)` | method | `QModelIndex` | public | Even though we're not displaying tree-like data, we should re-implement parent() and index() to inform Views that our data is strictly tabular (even in a tree context) |
| `index( int row, int column, const QModelIndex &parentidx = QModelIndex())` | method | `QModelIndex` | public | Even though we're not displaying tree-like data, we should re-implement parent() and index() to inform Views that our data is strictly tabular (even in a tree context) |
| `hasChildren( const QModelIndex &parentidx = QModelIndex())` | method | `bool` | public | — |
| `clear()` | method | `void` | public | Convenience function which will clear() the FeatureWeakRefSequence and notify any QTableViews of the change in layout. |
| `sequence_about_to_be_changed()` | method | `void` | public | If you are modifying the underlying FeatureWeakRefSequence directly, call this function before any major changes to the table data happen. |
| `sequence_changed()` | method | `void` | public | If you are modifying the underlying FeatureWeakRefSequence directly, call this function after any major changes to the table data happen. |
| `begin_insert_features(int first, int last)` | method | `void` | public | If you are modifying the underlying FeatureWeakRefSequence directly, call this function before features are inserted. \[first, last\] is an inclusive range, and correspond to the row numbers the new features will have after they have been ... |
| `end_insert_features()` | method | `void` | public | If you are modifying the underlying FeatureWeakRefSequence directly, call this function after features have been inserted. |
| `begin_remove_features(int first, int last)` | method | `void` | public | If you are modifying the underlying FeatureWeakRefSequence directly, call this function before features are removed. \[first, last\] is an inclusive range, and correspond to the row numbers the features will be removed from. |
| `end_remove_features()` | method | `void` | public | If you are modifying the underlying FeatureWeakRefSequence directly, call this function after features have been removed. |
| `set_default_resize_modes( QHeaderView &header)` | method | `void` | public | Convenience function to initialise a QHeaderView with the suggested resize mode appropriate for each column. |
| `get_index_for_feature( GPlatesModel::FeatureHandle::weak_ref feature_ref)` | method | `QModelIndex` | public | Searches the table for the given FeatureHandle::weak\_ref. |
| `get_index_for_geometry( GPlatesAppLogic::ReconstructionGeometry::non_null_ptr_to_const_type reconstruction_geometry)` | method | `QModelIndex` | public | As get\_index\_for\_feature, but looking for a specific geometry in the table. |
| `handle_selection_change( const QItemSelection &selected, const QItemSelection &deselected)` | method | `void` | public | ViewportWindow connects the QTableView's selection model's change event to this slot, so that the model can use it to focus the corresponding geometry. |
| `handle_feature_modified( GPlatesGui::FeatureFocus &feature_focus)` | method | `void` | public | Lets the model know that a feature has been modified. |
| `handle_rendered_geometry_collection_update()` | method | `void` | public | Update the internal ReconstructionGeometries when the rendered geometry collection is updated. |
| `current_index()` | method | `QModelIndex` | public | — |
| `d_feature_focus_ptr` | field | `FeatureFocus` | private | — |
| `d_rendered_geometry_collection` | field | `GPlatesViewOperations::RenderedGeometryCollection` | private | Used to find the visible reconstruction geometries as a short-list for searching for new reconstruction geometries for a new reconstruction because we don't want to pick up any old or invisible reconstruction geometries. |
| `d_sequence` | field | `geometry_sequence_type` | private | — |
| `d_current_index` | field | `QModelIndex` | private | — |

## Free functions and macros

| Name | Kind | Type / body | Description |
|---|---|---|---|
| `NUM_ELEMS` | macro_function | `(sizeof(a) / sizeof((a)[0]))` | — |
| `null_table_accessor( GPlatesAppLogic::ReconstructionGeometry::non_null_ptr_to_const_type geometry)` | function | `QVariant` | Accessor functions for table cells: |
| `get_feature_weak_ref_if_valid( GPlatesAppLogic::ReconstructionGeometry::non_null_ptr_to_const_type geometry)` | function | `boost::optional<GPlatesModel::FeatureHandle::weak_ref>` | — |
| `get_feature_type( GPlatesAppLogic::ReconstructionGeometry::non_null_ptr_to_const_type geometry)` | function | `QVariant` | — |
| `get_reconstruction_plate_id_from_properties( const GPlatesModel::FeatureHandle::weak_ref &feature, bool should_print_debugging_message = false)` | function | `QVariant` | — |
| `get_plate_id( GPlatesAppLogic::ReconstructionGeometry::non_null_ptr_to_const_type geometry)` | function | `QVariant` | — |
| `format_time_instant( const GPlatesPropertyValues::GmlTimeInstant &time_instant)` | function | `QString` | — |
| `format_time_period( const GPlatesPropertyValues::GmlTimePeriod &time_period)` | function | `QString` | — |
| `get_time_begin( GPlatesAppLogic::ReconstructionGeometry::non_null_ptr_to_const_type geometry)` | function | `QVariant` | — |
| `get_time_end( GPlatesAppLogic::ReconstructionGeometry::non_null_ptr_to_const_type geometry)` | function | `QVariant` | — |
| `get_name( GPlatesAppLogic::ReconstructionGeometry::non_null_ptr_to_const_type geometry)` | function | `QVariant` | — |
| `get_description( GPlatesAppLogic::ReconstructionGeometry::non_null_ptr_type geometry)` | function | `QVariant` | — |
| `format_point_or_vertex( const GPlatesMaths::PointOnSphere &point_or_vertex)` | function | `QString` | — |
| `format_geometry_point( GPlatesMaths::PointGeometryOnSphere::non_null_ptr_to_const_type point)` | function | `QString` | — |
| `format_geometry_multi_point( GPlatesMaths::MultiPointOnSphere::non_null_ptr_to_const_type multi_point)` | function | `QString` | — |
| `format_geometry_polygon( GPlatesMaths::PolygonOnSphere::non_null_ptr_to_const_type polygon)` | function | `QString` | — |
| `format_geometry_polyline( GPlatesMaths::PolylineOnSphere::non_null_ptr_to_const_type polyline)` | function | `QString` | — |
| `get_geometry_property_if_valid( ReconstructionGeometryPointer geometry)` | function | `boost::optional<GPlatesModel::FeatureHandle::iterator>` | — |
| `get_present_day_geometry( GPlatesAppLogic::ReconstructionGeometry::non_null_ptr_to_const_type geometry)` | function | `QVariant` | — |
| `get_clicked_geometry_property( GPlatesAppLogic::ReconstructionGeometry::non_null_ptr_to_const_type geometry)` | function | `QVariant` | — |
| `get_creation_time( GPlatesAppLogic::ReconstructionGeometry::non_null_ptr_to_const_type geometry)` | function | `QVariant` | — |
| `column_heading_info_table` | variable | `ColumnHeadingInfo` | The dispatch table for the above functions: |
| `get_column_heading( int column)` | function | `QString` | — |
| `get_column_tooltip( int column)` | function | `QString` | — |
| `get_column_width( int column)` | function | `int` | — |
| `get_column_accessor( int column)` | function | `table_cell_accessor_type` | — |
| `get_column_alignment( int column)` | function | `QFlags<Qt::AlignmentFlag>` | — |
| `GPLATES_GUI_FEATURETABLEMODEL_H` | macro | `None` | — |

## Notes

- The model is currently non-editable; `get_index_for_feature` is compiled out (`#if 0`) as "not as easy to implement right now", so lookups by feature are done via `get_index_for_geometry` instead.
- If a row's `ReconstructionGeometry` can no longer be matched to the current reconstruction (e.g. the reconstruction time moved outside the feature's valid time range), `handle_rendered_geometry_collection_update` deliberately leaves the stale row in place rather than removing it, so the row can re-highlight if the time changes back.
- When the same feature is reconstructed by two different layers, `handle_rendered_geometry_collection_update` picks whichever matching `ReconstructionGeometry` is found first and cannot guarantee it belongs to the same layer as the original — a known limitation noted in the source.

## Used by

| Unit | Component | References |
|---|---|---|
| [gui/TopologyTools](TopologyTools.md) | gui | 36 |
| [gui/AddClickedGeometriesToFeatureTable](AddClickedGeometriesToFeatureTable.md) | gui | 9 |
| [qt-widgets/SearchResultsDockWidget](../qt-widgets/SearchResultsDockWidget.md) | qt-widgets | 5 |
| [presentation/ViewState](../presentation/ViewState.md) | presentation | 4 |
| [canvas-tools/BuildTopology](../canvas-tools/BuildTopology.md) | canvas-tools | 1 |
| [canvas-tools/ClickGeometry](../canvas-tools/ClickGeometry.md) | canvas-tools | 1 |
| [canvas-tools/EditTopology](../canvas-tools/EditTopology.md) | canvas-tools | 1 |

## Related

**Qt signal/slot connections** (2 in this unit)

| Sender | Signal | Receiver | Slot |
|---|---|---|---|
| `&d_rendered_geometry_collection` | `collection_was_updated( GPlatesViewOperations::RenderedGeometryCollection &, GPlatesViewOperations::RenderedGeometryCollection::main_layers_update_type)` | `this` | `handle_rendered_geometry_collection_update()` |
| `d_feature_focus_ptr` | `focused_feature_modified(GPlatesGui::FeatureFocus &)` | `this` | `handle_feature_modified(GPlatesGui::FeatureFocus &)` |


## Explore

Run these from the `gplates-code` skill directory:

```bash
python scripts/gpq.py file src/gui/FeatureTableModel.h
python scripts/gpq.py def GPlatesGui::FeatureTableModel --body
python scripts/gpq.py uses FeatureTableModel --kind class
python scripts/gpq.py hier FeatureTableModel
```
