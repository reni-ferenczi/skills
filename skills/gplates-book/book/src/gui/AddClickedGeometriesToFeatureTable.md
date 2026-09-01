# AddClickedGeometriesToFeatureTable

[Book TOC](../../TOC.md) · [gui](../../components/gui.md) · cluster Community 1483 · tier 2

| Source file | Kind | Lines |
|---|---|---|
| `src/gui/AddClickedGeometriesToFeatureTable.h` | C++ | 177 |
| `src/gui/AddClickedGeometriesToFeatureTable.cc` | C++ | 181 |

## Overview

[[[PROSE overview unit=gui/AddClickedGeometriesToFeatureTable tier=2]]]
Replace this whole block, markers included, with 1-3 paragraphs: what this unit is, why it exists, and how it fits the surrounding design. Do not restate the tables below.
[[[/PROSE]]]

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

[[[PROSE notes unit=gui/AddClickedGeometriesToFeatureTable tier=2]]]
Replace this whole block, markers included, with invariants, ownership, threading or gotchas that are not visible in the tables. Write *None.* if there is nothing worth saying.
[[[/PROSE]]]

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
