# ResolvedTopologicalGeometry

[Book TOC](../../TOC.md) · [app-logic](../../components/app-logic.md) · cluster Community 498 · tier 2

| Source file | Kind | Lines |
|---|---|---|
| `src/app-logic/ResolvedTopologicalGeometry.h` | C++ | 317 |

## Overview

[[[PROSE overview unit=app-logic/ResolvedTopologicalGeometry tier=2]]]
Replace this whole block, markers included, with 1-3 paragraphs: what this unit is, why it exists, and how it fits the surrounding design. Do not restate the tables below.
[[[/PROSE]]]

## Declared types

| Name | Kind | Bases | Template | Subclasses | Description |
|---|---|---|---|---|---|
| [`GPlatesAppLogic::ResolvedTopologicalGeometry`](#gplatesapplogicresolvedtopologicalgeometry) | class | [`ReconstructionGeometry`](ReconstructionGeometry.md)<br>[`GPlatesModel::WeakObserver<GPlatesModel::FeatureHandle>`](../model/WeakObserver.md) | — | 2 | Abstract base class for ResolvedTopologicalBoundary and ResolvedTopologicalLine. |

## Members

### `GPlatesAppLogic::ResolvedTopologicalGeometry`

| Member | Kind | Type | Access | Description |
|---|---|---|---|---|
| `non_null_ptr_type` | typedef | `GPlatesUtils::non_null_intrusive_ptr<ResolvedTopologicalGeometry>` | public | A convenience typedef for a shared pointer to a non-const ResolvedTopologicalGeometry. |
| `non_null_ptr_to_const_type` | typedef | `GPlatesUtils::non_null_intrusive_ptr<const ResolvedTopologicalGeometry>` | public | A convenience typedef for a shared pointer to a non-const ResolvedTopologicalGeometry. |
| `maybe_null_ptr_type` | typedef | `boost::intrusive_ptr<ResolvedTopologicalGeometry>` | public | A convenience typedef for boost::intrusive\_ptr\<ResolvedTopologicalGeometry\>. |
| `maybe_null_ptr_to_const_type` | typedef | `boost::intrusive_ptr<const ResolvedTopologicalGeometry>` | public | A convenience typedef for boost::intrusive\_ptr\<const ResolvedTopologicalGeometry\>. |
| `WeakObserverType` | typedef | `GPlatesModel::WeakObserver<GPlatesModel::FeatureHandle>` | public | A convenience typedef for the WeakObserver base class of this class. |
| `resolved_topology_geometry_ptr_type` | typedef | `GPlatesMaths::GeometryOnSphere::non_null_ptr_to_const_type` | public | A convenience typedef for the geometry of this ResolvedTopologicalGeometry. |
| `~ResolvedTopologicalGeometry()` | destructor | `None` | public | — |
| `resolved_topology_geometry()` | method | `resolved_topology_geometry_ptr_type` | public | Access the resolved topology geometry. |
| `get_non_null_pointer_to_const()` | method | `non_null_ptr_to_const_type` | public | Get a non-null pointer to a const ResolvedTopologicalGeometry which points to this instance. |
| `get_non_null_pointer()` | method | `non_null_ptr_type` | public | Get a non-null pointer to a ResolvedTopologicalGeometry which points to this instance. |
| `get_reconstruction_tree()` | method | `ReconstructionTree::non_null_ptr_to_const_type` | public | Access the ReconstructionTree that was used to reconstruct this ReconstructionGeometry. |
| `get_reconstruction_tree_creator()` | method | `ReconstructionTreeCreator` | public | Gets the reconstruction tree creator that uses the same anchor plate and reconstruction features as used to create the tree returned by get\_reconstruction\_tree. |
| `references( const GPlatesModel::FeatureHandle &that_feature_handle)` | method | `bool` | public | Return whether this RTG references that\_feature\_handle. |
| `feature_handle_ptr()` | method | `GPlatesModel::FeatureHandle` | public | Return the pointer to the FeatureHandle. |
| `is_valid()` | method | `bool` | public | Return whether this pointer is valid to be dereferenced (to obtain a FeatureHandle). |
| `get_feature_ref()` | method | `GPlatesModel::FeatureHandle::weak_ref` | public | Return a weak-ref to the feature whose resolved topological geometry this RTG contains, or an invalid weak-ref, if this pointer is not valid to be dereferenced. |
| `property()` | method | `GPlatesModel::FeatureHandle::iterator` | public | Access the topological geometry feature property used to generate the resolved topological geometry. |
| `accept_visitor( ConstReconstructionGeometryVisitor &visitor)` | method | `void` | public | Accept a ConstReconstructionGeometryVisitor instance. |
| `accept_visitor( ReconstructionGeometryVisitor &visitor)` | method | `void` | public | Accept a ReconstructionGeometryVisitor instance. |
| `accept_weak_observer_visitor( GPlatesModel::WeakObserverVisitor<GPlatesModel::FeatureHandle> &visitor)` | method | `void` | public | Accept a WeakObserverVisitor instance. |
| `ResolvedTopologicalGeometry( const ReconstructionTree::non_null_ptr_to_const_type &reconstruction_tree_, const ReconstructionTreeCreator &reconstruction_tree_creator, GPlatesModel::FeatureHandle &feature_handle, GPlatesModel::FeatureHandle::iterator property_iterator_, boost::optional<GPlatesModel::integer_plate_id_typ ...` | constructor | `None` | protected | Instantiate a resolved topological geometry with an optional reconstruction plate ID and an optional time of formation. |
| `d_reconstruction_tree` | field | `ReconstructionTree::non_null_ptr_to_const_type` | private | The reconstruction tree used to reconstruct us. |
| `d_reconstruction_tree_creator` | field | `ReconstructionTreeCreator` | private | Used to create reconstruction trees similar that the tree used to reconstruction 'this' reconstruction geometry (the only difference being the reconstruction time). |
| `d_property_iterator` | field | `GPlatesModel::FeatureHandle::iterator` | private | This is an iterator to the (topological-geometry-valued) property from which this RTG was derived. |
| `d_plate_id` | field | `boost::optional<GPlatesModel::integer_plate_id_type>` | private | The cached plate ID, if it exists. |
| `d_time_of_formation` | field | `boost::optional<GPlatesPropertyValues::GeoTimeInstant>` | private | The cached time of formation of the feature, if it exists. |

## Free functions and macros

| Name | Kind | Type / body | Description |
|---|---|---|---|
| `GPLATES_APP_LOGIC_RESOLVEDTOPOLOGICALGEOMETRY_H` | macro | `None` | — |

## Notes

[[[PROSE notes unit=app-logic/ResolvedTopologicalGeometry tier=2]]]
Replace this whole block, markers included, with invariants, ownership, threading or gotchas that are not visible in the tables. Write *None.* if there is nothing worth saying.
[[[/PROSE]]]

## Used by

| Unit | Component | References |
|---|---|---|
| [app-logic/ResolvedTopologicalLine](ResolvedTopologicalLine.md) | app-logic | 3 |
| [app-logic/ScalarField3DLayerProxy](ScalarField3DLayerProxy.md) | app-logic | 3 |
| [app-logic/ResolvedTopologicalBoundary](ResolvedTopologicalBoundary.md) | app-logic | 2 |
| [app-logic/ReconstructionGeometryFinder](ReconstructionGeometryFinder.md) | app-logic | 1 |
| [gui/ExportNetRotationAnimationStrategy](../gui/ExportNetRotationAnimationStrategy.md) | gui | 1 |
| [gui/FeatureFocus](../gui/FeatureFocus.md) | gui | 1 |
| [gui/TopologyTools](../gui/TopologyTools.md) | gui | 1 |
| [presentation/LayerOutputRenderer](../presentation/LayerOutputRenderer.md) | presentation | 1 |
| [presentation/ReconstructionGeometryRenderer](../presentation/ReconstructionGeometryRenderer.md) | presentation | 1 |
| [view-operations/FocusedFeatureGeometryManipulator](../view-operations/FocusedFeatureGeometryManipulator.md) | view-operations | 1 |

## Related

*None.*

## Explore

Run these from the `gplates-code` skill directory:

```bash
python scripts/gpq.py file src/app-logic/ResolvedTopologicalGeometry.h
python scripts/gpq.py def GPlatesAppLogic::ResolvedTopologicalGeometry --body
python scripts/gpq.py uses ResolvedTopologicalGeometry --kind class
python scripts/gpq.py hier ResolvedTopologicalGeometry
```
