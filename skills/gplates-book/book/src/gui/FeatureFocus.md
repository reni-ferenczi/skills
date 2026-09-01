# FeatureFocus

[Book TOC](../../TOC.md) · [gui](../../components/gui.md) · cluster Community 642 · tier 1

| Source file | Kind | Lines |
|---|---|---|
| `src/gui/FeatureFocus.h` | C++ | 306 |
| `src/gui/FeatureFocus.cc` | C++ | 424 |

## Overview

[[[PROSE overview unit=gui/FeatureFocus tier=1]]]
Replace this whole block, markers included, with 1-3 paragraphs: what this unit is, why it exists, and how it fits the surrounding design. Do not restate the tables below.
[[[/PROSE]]]

## Declared types

| Name | Kind | Bases | Template | Subclasses | Description |
|---|---|---|---|---|---|
| [`(anonymous)::FocusedFeatureDeactivatedCallback`](#anonymousfocusedfeaturedeactivatedcallback) | class | [`GPlatesModel::WeakReferenceCallback<GPlatesModel::FeatureHandle>`](../model/WeakReferenceCallback.md) | — | 0 | Feature handle weak ref callback to unset the focused feature if it gets deactivated in the model. |
| [`(anonymous)::ReconstructionGeometryLocator`](#anonymousreconstructiongeometrylocator) | class | [`GPlatesAppLogic::ConstReconstructionGeometryVisitor`](../app-logic/ReconstructionGeometry.md) | — | 0 | — |
| [`GPlatesGui::FeatureFocus`](#gplatesguifeaturefocus) | class | `QObject` | — | 0 | This class is used to store the notion of which feature currently has the focus. |

## Members

### `(anonymous)::FocusedFeatureDeactivatedCallback`

| Member | Kind | Type | Access | Description |
|---|---|---|---|---|
| `FocusedFeatureDeactivatedCallback( GPlatesGui::FeatureFocus &feature_focus)` | constructor | `None` | public | — |
| `publisher_deactivated( const weak_reference_type &, const deactivated_event_type &)` | method | `void` | public | — |
| `d_feature_focus` | field | `GPlatesGui::FeatureFocus` | private | — |

### `(anonymous)::ReconstructionGeometryLocator`

| Member | Kind | Type | Access | Description |
|---|---|---|---|---|
| `get_location()` | method | `boost::optional<GPlatesMaths::LatLonPoint>` | public | — |
| `visit( const GPlatesUtils::non_null_intrusive_ptr<reconstructed_feature_geometry_type> &rfg)` | method | `void` | private | Derivations of ReconstructedFeatureGeometry default to its implementation... |
| `visit( const GPlatesUtils::non_null_intrusive_ptr<resolved_topological_geometry_type> &rtg)` | method | `void` | private | Derivations of ResolvedTopologicalGeometry default to its implementation... |
| `visit( const GPlatesUtils::non_null_intrusive_ptr<resolved_topological_network_type> &rtn)` | method | `void` | private | — |
| `d_location` | field | `boost::optional<GPlatesMaths::LatLonPoint>` | private | — |

### `GPlatesGui::FeatureFocus`

| Member | Kind | Type | Access | Description |
|---|---|---|---|---|
| `FeatureFocus( GPlatesViewOperations::RenderedGeometryCollection &rendered_geometry_collection)` | constructor | `None` | public | — |
| `~FeatureFocus()` | destructor | `None` | public | — |
| `focused_feature()` | method | `GPlatesModel::FeatureHandle::weak_ref` | public | Accessor for the currently-focused feature. |
| `is_valid()` | method | `bool` | public | Return whether the current focus is valid. |
| `associated_reconstruction_geometry()` | method | `GPlatesAppLogic::ReconstructionGeometry::maybe_null_ptr_to_const_type` | public | Accessor for the ReconstructGeometry associated with the currently-focused feature (if there is one). |
| `set_focus( GPlatesModel::FeatureHandle::weak_ref new_feature_ref, GPlatesAppLogic::ReconstructionGeometry::non_null_ptr_to_const_type new_associated_rg)` | method | `void` | public | Change which feature is currently focused, also specifying an associated ReconstructionGeometry. |
| `set_focus( GPlatesModel::FeatureHandle::weak_ref new_feature_ref, GPlatesModel::FeatureHandle::iterator new_associated_property)` | method | `void` | public | Change which feature is currently focused, also specifying an associated property iterator. |
| `set_focus( GPlatesModel::FeatureHandle::weak_ref new_feature_ref)` | method | `void` | public | Change which feature is currently focused, without specifying any geometry property. |
| `unset_focus()` | method | `void` | public | Clear the focus. |
| `announce_modification_of_focused_feature()` | method | `void` | public | Call this method when you have modified the properties of the currently-focused feature. |
| `announce_deletion_of_focused_feature()` | method | `void` | public | Call this method when you have deleted the currently-focused feature from the model (i.e. the Delete Feature action). |
| `handle_rendered_geometry_collection_update()` | method | `void` | public | Notification of an update to the rendered geometry collection - we use this to find a new associated reconstruction geometry for the focused feature (if any) - the rendered geometry collection contains only the visible geometries. |
| `focus_changed( GPlatesGui::FeatureFocus &feature_focus)` | method | `void` | public | Emitted when a new feature has been clicked on, or the current focus has been cleared. |
| `focused_feature_modified( GPlatesGui::FeatureFocus &feature_focus)` | method | `void` | public | Emitted when the currently-focused feature has been modified. |
| `focused_feature_deleted( GPlatesGui::FeatureFocus &feature_focus)` | method | `void` | public | Emitted when the currently-focused feature has been deleted. |
| `d_focused_feature` | field | `GPlatesModel::FeatureHandle::weak_ref` | private | The currently-focused feature. |
| `d_callback_focused_feature` | field | `GPlatesModel::FeatureHandle::weak_ref` | private | Keep another reference to the currently focused feature to contain our model callback. |
| `d_associated_reconstruction_geometry` | field | `GPlatesAppLogic::ReconstructionGeometry::maybe_null_ptr_to_const_type` | private | The ReconstructionGeometry associated with the currently-focused feature. |
| `d_associated_geometry_property` | field | `GPlatesModel::FeatureHandle::iterator` | private | The geometry property used by the ReconstructionGeometry associated with the currently-focused feature. |
| `d_rendered_geometry_collection` | field | `GPlatesViewOperations::RenderedGeometryCollection` | private | Used to find the visible reconstruction geometries as a short-list for searching for the focused feature geometry because we don't want to pick up any old or invisible reconstruction geometries. |
| `find_new_associated_reconstruction_geometry()` | method | `void` | private | Find the new associated ReconstructionGeometry for the currently-focused feature (if any). |

## Free functions and macros

| Name | Kind | Type / body | Description |
|---|---|---|---|
| `GPLATES_GUI_FEATUREFOCUS_H` | macro | `None` | — |
| `locate_focus()` | function | `boost::optional<GPlatesMaths::LatLonPoint>` | — |

## Notes

[[[PROSE notes unit=gui/FeatureFocus tier=1]]]
Replace this whole block, markers included, with invariants, ownership, threading or gotchas that are not visible in the tables. Write *None.* if there is nothing worth saying.
[[[/PROSE]]]

## Used by

| Unit | Component | References |
|---|---|---|
| [presentation/ViewState](../presentation/ViewState.md) | presentation | 102 |
| [gui/TopologyTools](TopologyTools.md) | gui | 78 |
| [gui/TopologySectionsTable](TopologySectionsTable.md) | gui | 50 |
| [gui/FeatureTableModel](FeatureTableModel.md) | gui | 28 |
| [qt-widgets/ModifyReconstructionPoleWidget](../qt-widgets/ModifyReconstructionPoleWidget.md) | qt-widgets | 28 |
| [gui/FeaturePropertyTableModel](FeaturePropertyTableModel.md) | gui | 23 |
| [view-operations/SplitFeatureGeometryOperation](../view-operations/SplitFeatureGeometryOperation.md) | view-operations | 17 |
| [view-operations/SplitFeatureUndoCommand](../view-operations/SplitFeatureUndoCommand.md) | view-operations | 14 |
| [gui/GeometryFocusHighlight](GeometryFocusHighlight.md) | gui | 13 |
| [qt-widgets/GenerateDeformingMeshPointsDialog](../qt-widgets/GenerateDeformingMeshPointsDialog.md) | qt-widgets | 13 |
| [view-operations/FocusedFeatureGeometryManipulator](../view-operations/FocusedFeatureGeometryManipulator.md) | view-operations | 13 |
| [qt-widgets/EditFeaturePropertiesWidget](../qt-widgets/EditFeaturePropertiesWidget.md) | qt-widgets | 12 |
| [canvas-tools/BuildTopology](../canvas-tools/BuildTopology.md) | canvas-tools | 11 |
| [canvas-tools/EditTopology](../canvas-tools/EditTopology.md) | canvas-tools | 11 |
| [qt-widgets/FeaturePropertiesDialog](../qt-widgets/FeaturePropertiesDialog.md) | qt-widgets | 11 |
| [view-operations/MoveVertexGeometryOperation](../view-operations/MoveVertexGeometryOperation.md) | view-operations | 11 |
| [qt-widgets/AssignReconstructionPlateIdsDialog](../qt-widgets/AssignReconstructionPlateIdsDialog.md) | qt-widgets | 9 |
| [qt-widgets/MovePoleWidget](../qt-widgets/MovePoleWidget.md) | qt-widgets | 9 |
| [qt-widgets/FeatureSummaryWidget](../qt-widgets/FeatureSummaryWidget.md) | qt-widgets | 8 |
| [qt-widgets/KinematicGraphsDialog](../qt-widgets/KinematicGraphsDialog.md) | qt-widgets | 8 |

*... and 28 more units.*

## Related

**Qt signal/slot connections** (1 in this unit)

| Sender | Signal | Receiver | Slot |
|---|---|---|---|
| `&d_rendered_geometry_collection` | `collection_was_updated( GPlatesViewOperations::RenderedGeometryCollection &, GPlatesViewOperations::RenderedGeometryCollection::main_layers_update_type)` | `this` | `handle_rendered_geometry_collection_update()` |


## Explore

Run these from the `gplates-code` skill directory:

```bash
python scripts/gpq.py file src/gui/FeatureFocus.h
python scripts/gpq.py def GPlatesGui::FeatureFocus --body
python scripts/gpq.py uses FeatureFocus --kind class
python scripts/gpq.py hier FeatureFocus
```
