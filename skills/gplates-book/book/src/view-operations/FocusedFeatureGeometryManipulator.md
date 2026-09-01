# FocusedFeatureGeometryManipulator

[Book TOC](../../TOC.md) · [view-operations](../../components/view-operations.md) · cluster Community 1019 · tier 3

| Source file | Kind | Lines |
|---|---|---|
| `src/view-operations/FocusedFeatureGeometryManipulator.h` | C++ | 257 |
| `src/view-operations/FocusedFeatureGeometryManipulator.cc` | C++ | 471 |

## Overview

[[[PROSE overview unit=view-operations/FocusedFeatureGeometryManipulator tier=3]]]
Replace this whole block, markers included, with 1-3 paragraphs: what this unit is, why it exists, and how it fits the surrounding design. Do not restate the tables below.
[[[/PROSE]]]

## Declared types

| Name | Kind | Bases | Template | Subclasses | Description |
|---|---|---|---|---|---|
| [`GPlatesViewOperations::(anonymous)::SetGeometryInBuilder`](#gplatesviewoperationsanonymoussetgeometryinbuilder) | class | [`GPlatesMaths::ConstGeometryOnSphereVisitor`](../maths/ConstGeometryOnSphereVisitor.md) | — | 0 | Visitor gets a sequence of PointOnSphere objects from a GeometryOnSphere derived object and sets the geometry in a GeometryBuilder. |
| [`GPlatesViewOperations::FocusedFeatureGeometryManipulator`](#gplatesviewoperationsfocusedfeaturegeometrymanipulator) | class | `QObject` | — | 0 | Transfers focused feature geometry changes made by a GeometryBuilder to the feature containing the geometry. |

## Members

### `GPlatesViewOperations::(anonymous)::SetGeometryInBuilder`

| Member | Kind | Type | Access | Description |
|---|---|---|---|---|
| `SetGeometryInBuilder( GeometryBuilder *geom_builder)` | constructor | `None` | public | — |
| `set_geometry_in_builder( GPlatesMaths::GeometryOnSphere::non_null_ptr_to_const_type geometry)` | method | `GeometryBuilder::UndoOperation` | public | — |
| `visit_multi_point_on_sphere( GPlatesMaths::MultiPointOnSphere::non_null_ptr_to_const_type multi_point_on_sphere)` | method | `void` | private | — |
| `visit_point_on_sphere( GPlatesMaths::PointGeometryOnSphere::non_null_ptr_to_const_type point_on_sphere)` | method | `void` | private | — |
| `visit_polygon_on_sphere( GPlatesMaths::PolygonOnSphere::non_null_ptr_to_const_type polygon_on_sphere)` | method | `void` | private | — |
| `visit_polyline_on_sphere( GPlatesMaths::PolylineOnSphere::non_null_ptr_to_const_type polyline_on_sphere)` | method | `void` | private | — |
| `d_geom_builder` | field | `GeometryBuilder` | private | — |
| `d_undo_operation` | field | `GeometryBuilder::UndoOperation` | private | — |

### `GPlatesViewOperations::FocusedFeatureGeometryManipulator`

| Member | Kind | Type | Access | Description |
|---|---|---|---|---|
| `FocusedFeatureGeometryManipulator( GeometryBuilder &focused_feature_geom_builder, GPlatesPresentation::ViewState &view_state)` | constructor | `None` | public | — |
| `geometry_builder_stopped_updating_geometry()` | method | `void` | public | GeometryBuilder has done a group of one or more updates. |
| `move_point_in_current_geometry( GPlatesViewOperations::GeometryBuilder::PointIndex point_index, const GPlatesMaths::PointOnSphere &new_oriented_pos_on_globe, bool is_intermediate_move)` | method | `void` | public | GeometryBuilder has moved a vertex. |
| `set_focus( GPlatesGui::FeatureFocus &feature_focus)` | method | `void` | public | Changed which reconstruction geometry is currently focused. |
| `BlockInfiniteSignalSlotLoop` | struct | `None` | private | Convenience structure for calling begin\_block\_infinite\_signal\_slot\_loop and end\_block\_infinite\_signal\_slot\_loop. |
| `d_focused_feature_geom_builder` | field | `GeometryBuilder` | private | Used to set initial focused feature geometry and get final geometry. |
| `d_feature_focus` | field | `GPlatesGui::FeatureFocus` | private | Used to announce modifications of focused feature. |
| `d_application_state` | field | `GPlatesAppLogic::ApplicationState` | private | Used to get access to current reconstruction tree. |
| `d_feature` | field | `GPlatesModel::FeatureHandle::weak_ref` | private | The feature which contains the geometry whose RFG is the currently-focused reconstruction geometry. |
| `d_focused_geometry` | field | `GPlatesAppLogic::ReconstructionGeometry::maybe_null_ptr_to_const_type` | private | The reconstruction geometry which is focused. |
| `d_ignore_geom_builder_update` | field | `bool` | private | Is true if we've received an update signal from GeometryBuilder but have chosen to ignore it. |
| `d_block_infinite_signal_slot_loop_depth` | field | `int` | private | Counts depth of nested calls to begin\_block\_infinite\_signal\_slot\_loop and end\_block\_infinite\_signal\_slot\_loop. |
| `connect_to_geometry_builder()` | method | `void` | private | — |
| `connect_to_feature_focus()` | method | `void` | private | — |
| `convert_geom_from_feature_to_builder()` | method | `void` | private | Gets focused feature geometry and sets it in the GeometryBuilder. |
| `get_geometry_from_feature()` | method | `boost::optional<GPlatesMaths::GeometryOnSphere::non_null_ptr_to_const_type>` | private | Returns the geometry of the focused feature (either an RFG or resolved topological boundary). |
| `convert_geom_from_builder_to_feature()` | method | `void` | private | Gets geometry from GeometryBuilder and sets it in the focused feature. |
| `convert_secondary_geometries_to_features()` | method | `void` | private | Gets any secondary geometries from the GeometryBuilder and sets the corresponding features. |
| `reverse_reconstruct( GPlatesMaths::GeometryOnSphere::non_null_ptr_to_const_type geometry_on_sphere, const GPlatesModel::FeatureHandle::weak_ref &feature_ref)` | method | `GPlatesMaths::GeometryOnSphere::non_null_ptr_to_const_type` | private | Reverse reconstructs the specified geometry using the currently focused feature. |
| `reconstruct_test( GPlatesMaths::GeometryOnSphere::non_null_ptr_to_const_type geometry_on_sphere, bool reverse_reconstruct)` | method | `GPlatesMaths::GeometryOnSphere::non_null_ptr_to_const_type` | private | Reconstructs the specified geometry forward or backward in time using current reconstruction tree and plate\_id of currently focused feature. |
| `begin_block_infinite_signal_slot_loop()` | method | `void` | private | Starts blocking of set\_focus. |
| `end_block_infinite_signal_slot_loop()` | method | `void` | private | Finishes blocking of set\_focus. |
| `is_infinite_signal_slot_loop_blocked()` | method | `bool` | private | — |
| `get_plate_id_from_feature()` | method | `boost::optional<GPlatesModel::integer_plate_id_type>` | private | Gets the plate id from the focused feature. |

## Free functions and macros

| Name | Kind | Type / body | Description |
|---|---|---|---|
| `GPLATES_VIEWOPERATIONS_FOCUSEDFEATUREGEOMETRYMANIPULATOR_H` | macro | `None` | — |

## Notes

[[[PROSE notes unit=view-operations/FocusedFeatureGeometryManipulator tier=3]]]
Replace this whole block, markers included, with invariants, ownership, threading or gotchas that are not visible in the tables. Write *None.* if there is nothing worth saying.
[[[/PROSE]]]

## Used by

| Unit | Component | References |
|---|---|---|
| [presentation/ViewState](../presentation/ViewState.md) | presentation | 1 |

## Related

**Qt signal/slot connections** (3 in this unit)

| Sender | Signal | Receiver | Slot |
|---|---|---|---|
| `d_focused_feature_geom_builder` | `stopped_updating_geometry()` | `this` | `geometry_builder_stopped_updating_geometry()` |
| `d_focused_feature_geom_builder` | `moved_point_in_current_geometry( GPlatesViewOperations::GeometryBuilder::PointIndex, const GPlatesMaths::PointOnSphere &, bool)` | `this` | `move_point_in_current_geometry( GPlatesViewOperations::GeometryBuilder::PointIndex, const GPlatesMaths::PointOnSphere &, bool)` |
| `d_feature_focus` | `focus_changed( GPlatesGui::FeatureFocus &)` | `this` | `set_focus( GPlatesGui::FeatureFocus &)` |


## Explore

Run these from the `gplates-code` skill directory:

```bash
python scripts/gpq.py file src/view-operations/FocusedFeatureGeometryManipulator.h
python scripts/gpq.py def GPlatesViewOperations::FocusedFeatureGeometryManipulator --body
python scripts/gpq.py uses FocusedFeatureGeometryManipulator --kind class
python scripts/gpq.py hier FocusedFeatureGeometryManipulator
```
