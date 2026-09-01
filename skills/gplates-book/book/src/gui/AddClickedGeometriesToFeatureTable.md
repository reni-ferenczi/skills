# AddClickedGeometriesToFeatureTable

[Book TOC](../../TOC.md) · [gui](../../components/gui.md) · cluster Community 1483 · tier 2

| Source file | Kind | Lines |
|---|---|---|
| `src/gui/AddClickedGeometriesToFeatureTable.h` | C++ | 177 |
| `src/gui/AddClickedGeometriesToFeatureTable.cc` | C++ | 181 |

## Overview

A small set of free functions that turn a mouse click on the globe or map into
rows in the "Clicked" feature table. `get_clicked_geometries` runs
proximity-hit testing (via `GPlatesViewOperations::test_proximity`) against the
currently rendered geometries and reduces the hits to their unique
`GPlatesAppLogic::ReconstructionGeometry` objects, optionally filtered by a
caller-supplied `filter_reconstruction_geometry_predicate_type` predicate (the
default accepts everything). `add_clicked_geometries_to_feature_table` then
populates a `GPlatesGui::FeatureTableModel` from that sequence, updates the
`GPlatesQtWidgets::ViewportWindow` status bar, and drives which row gets
highlighted in the search results dock. `get_and_add_clicked_geometries_to_feature_table`
is a convenience wrapper chaining the two, and
`add_geometry_to_top_of_feature_table` is used separately to prepend a single
already-known geometry (for tools that add a feature programmatically rather
than through a click).

This unit exists to give every canvas tool that reacts to clicking on
geometry (`ClickGeometry`, `BuildTopology`, `EditTopology`, and others) a
single shared implementation, so hit-testing, table population and focus
handling stay consistent across tools instead of being reimplemented per
tool.

## Declared types

| Name | Kind | Bases | Template | Subclasses | Description |
|---|---|---|---|---|---|
| [`GPlatesGui::filter_reconstruction_geometry_predicate_type`](#gplatesguifilter_reconstruction_geometry_predicate_type) | typedef | — | — | 0 | Typedef for a boost function (predicate) used to filter reconstruction geometries. |

## Members

### `GPlatesGui::filter_reconstruction_geometry_predicate_type`

*None.*

## Free functions and macros

| Name | Kind | Type / body | Description |
|---|---|---|---|
| `GPLATES_GUI_ADDCLICKEDGEOMETRIESTOFEATURETABLE_H` | macro | `None` | — |
| `default_filter_reconstruction_geometry_predicate( const GPlatesAppLogic::ReconstructionGeometry::non_null_ptr_to_const_type &)` | function | `bool` | The default reconstruction geoemetry filter always returns true. |
| `get_clicked_geometries( std::vector<GPlatesAppLogic::ReconstructionGeometry::non_null_ptr_to_const_type> &clicked_geom_seq, const GPlatesMaths::PointOnSphere &click_point_on_sphere, double proximity_inclusion_threshold, GPlatesViewOperations::RenderedGeometryCollection &rendered_geometry_collection, filter_reconstructi ...` | function | `void` | Returns a sequence of clicked geometries given a click position. |
| `add_clicked_geometries_to_feature_table( const std::vector<GPlatesAppLogic::ReconstructionGeometry::non_null_ptr_to_const_type> &clicked_geom_seq, GPlatesQtWidgets::ViewportWindow &view_state, GPlatesGui::FeatureTableModel &clicked_table_model, GPlatesGui::FeatureFocus &feature_focus, const GPlatesAppLogic::Reconstruct ...` | function | `void` | Adds the clicked geometries in clicked\_geom\_seq to the clicked feature table. |
| `get_and_add_clicked_geometries_to_feature_table( const GPlatesMaths::PointOnSphere &click_point_on_sphere, double proximity_inclusion_threshold, GPlatesQtWidgets::ViewportWindow &view_state, GPlatesGui::FeatureTableModel &clicked_table_model, GPlatesGui::FeatureFocus &feature_focus, GPlatesViewOperations::RenderedGeome ...` | function | `void` | Combines the above two functions (get\_clicked\_geometries and add\_clicked\_geometries\_to\_feature\_table). |
| `add_geometry_to_top_of_feature_table( GPlatesAppLogic::ReconstructionGeometry::non_null_ptr_to_const_type reconstruction_geometry_ptr, GPlatesGui::FeatureTableModel &clicked_table_model, const GPlatesAppLogic::ReconstructGraph &reconstruct_graph)` | function | `void` | Inserts a new feature/geometry entry reconstruction\_geometry\_ptr into the clicked\_table\_model at the top (row 0) of the table, moving all other entries down one row. |

## Notes

`add_clicked_geometries_to_feature_table` always clears the clicked-table
model first, and unsets the feature focus entirely if nothing survives the
predicate filter. Whether the first clicked feature is force-highlighted or
the previously focused feature is re-highlighted instead is controlled by
`highlight_first_clicked_feature_in_table`; the "restore previous state"
(`false`) path calls `FeatureTableModel::handle_rendered_geometry_collection_update()`
before re-highlighting because the reconstruction geometries in the newly
cleared table may otherwise be stale pointers from a different
reconstruction time than the currently focused feature.

## Used by

| Unit | Component | References |
|---|---|---|
| [canvas-tools/ClickGeometry](../canvas-tools/ClickGeometry.md) | canvas-tools | 42 |
| [canvas-tools/BuildTopology](../canvas-tools/BuildTopology.md) | canvas-tools | 27 |
| [qt-widgets/SearchResultsDockWidget](../qt-widgets/SearchResultsDockWidget.md) | qt-widgets | 24 |
| [canvas-tools/EditTopology](../canvas-tools/EditTopology.md) | canvas-tools | 23 |
| [gui/FeatureInspectionCanvasToolWorkflow](FeatureInspectionCanvasToolWorkflow.md) | gui | 1 |

## Related

*None.*

## Explore

Run these from the `gplates-code` skill directory:

```bash
python scripts/gpq.py file src/gui/AddClickedGeometriesToFeatureTable.h
python scripts/gpq.py def GPlatesGui::filter_reconstruction_geometry_predicate_type --body
python scripts/gpq.py uses filter_reconstruction_geometry_predicate_type --kind typedef
```
