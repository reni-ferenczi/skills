# ResolvedTopologicalNetwork

[Book TOC](../../TOC.md) · [app-logic](../../components/app-logic.md) · cluster Community 446 · tier 2

| Source file | Kind | Lines |
|---|---|---|
| `src/app-logic/ResolvedTopologicalNetwork.h` | C++ | 390 |
| `src/app-logic/ResolvedTopologicalNetwork.cc` | C++ | 124 |

## Overview

[[[PROSE overview unit=app-logic/ResolvedTopologicalNetwork tier=2]]]
Replace this whole block, markers included, with 1-3 paragraphs: what this unit is, why it exists, and how it fits the surrounding design. Do not restate the tables below.
[[[/PROSE]]]

## Declared types

| Name | Kind | Bases | Template | Subclasses | Description |
|---|---|---|---|---|---|
| [`GPlatesAppLogic::ResolvedTopologicalNetwork`](#gplatesapplogicresolvedtopologicalnetwork) | class | [`ReconstructionGeometry`](ReconstructionGeometry.md)<br>[`GPlatesModel::WeakObserver<GPlatesModel::FeatureHandle>`](../model/WeakObserver.md) | — | 0 | — |

## Members

### `GPlatesAppLogic::ResolvedTopologicalNetwork`

| Member | Kind | Type | Access | Description |
|---|---|---|---|---|
| `non_null_ptr_type` | typedef | `GPlatesUtils::non_null_intrusive_ptr<ResolvedTopologicalNetwork>` | public | A convenience typedef for a non-null intrusive ptr to ResolvedTopologicalNetwork. |
| `non_null_ptr_to_const_type` | typedef | `GPlatesUtils::non_null_intrusive_ptr<const ResolvedTopologicalNetwork>` | public | A convenience typedef for a non-null intrusive ptr to ResolvedTopologicalNetwork. |
| `WeakObserverType` | typedef | `GPlatesModel::WeakObserver<GPlatesModel::FeatureHandle>` | public | A convenience typedef for the WeakObserver base class of this class. |
| `boundary_polygon_ptr_type` | typedef | `GPlatesMaths::PolygonOnSphere::non_null_ptr_to_const_type` | public | A convenience typedef for the polygon boundary of this ResolvedTopologicalNetwork. |
| `boundary_sub_segment_seq_type` | typedef | `sub_segment_seq_type` | public | Typedef for a sequence of ResolvedTopologicalGeometrySubSegment objects. |
| `rigid_block_const_iterator` | typedef | `ResolvedTriangulation::Network::rigid_block_seq_type::const_iterator` | public | The type used to const\_iterate over the interior rigid blocks. |
| `~ResolvedTopologicalNetwork()` | destructor | `None` | public | — |
| `create( const double &reconstruction_time_, const ResolvedTriangulation::Network::non_null_ptr_type &triangulation_network, GPlatesModel::FeatureHandle &feature_handle, GPlatesModel::FeatureHandle::iterator property_iterator_, BoundarySubSegmentForwardIter boundary_sub_segment_sequence_begin, BoundarySubSegmentForwardI ...` | method | `non_null_ptr_type` | public | Create a ResolvedTopologicalNetwork instance. |
| `boundary_polygon()` | method | `boundary_polygon_ptr_type` | public | Access the boundary polygon of this resolved topology network. |
| `boundary_polygon_with_rigid_block_holes()` | method | `boundary_polygon_ptr_type` | public | Access the boundary polygon (including rigid block holes) of this resolved topology network. |
| `get_boundary_vertex_source_infos` | field | `resolved_vertex_source_info_seq_type` | public | Returns the boundary per-vertex source reconstructed feature geometries. |
| `get_non_null_pointer_to_const()` | method | `non_null_ptr_to_const_type` | public | Get a non-null pointer to a const ResolvedTopologicalNetwork which points to this instance. |
| `get_non_null_pointer()` | method | `non_null_ptr_type` | public | Get a non-null pointer to a ResolvedTopologicalNetwork which points to this instance. |
| `references( const GPlatesModel::FeatureHandle &that_feature_handle)` | method | `bool` | public | Return whether this RTN references that\_feature\_handle. |
| `feature_handle_ptr()` | method | `GPlatesModel::FeatureHandle` | public | Return the pointer to the FeatureHandle. |
| `is_valid()` | method | `bool` | public | Return whether this pointer is valid to be dereferenced (to obtain a FeatureHandle). |
| `get_feature_ref()` | method | `GPlatesModel::FeatureHandle::weak_ref` | public | Return a weak-ref to the feature whose resolved topological geometry this RTN contains, or an invalid weak-ref, if this pointer is not valid to be dereferenced. |
| `property()` | method | `GPlatesModel::FeatureHandle::iterator` | public | Access the topological polygon feature property used to generate the resolved topological geometry. |
| `accept_visitor( ConstReconstructionGeometryVisitor &visitor)` | method | `void` | public | Accept a ConstReconstructionGeometryVisitor instance. |
| `accept_visitor( ReconstructionGeometryVisitor &visitor)` | method | `void` | public | Accept a ReconstructionGeometryVisitor instance. |
| `accept_weak_observer_visitor( GPlatesModel::WeakObserverVisitor<GPlatesModel::FeatureHandle> &visitor)` | method | `void` | public | Accept a WeakObserverVisitor instance. |
| `INCLUDE_SUB_SEGMENT_RUBBER_BAND_POINTS_IN_RESOLVED_NETWORK_BOUNDARY` | field | `bool` | public | Whether rubber band points of this resolved topological network's boundary sub-segments contributed to its boundary geometry. |
| `d_property_iterator` | field | `GPlatesModel::FeatureHandle::iterator` | private | This is an iterator to the (topological-geometry-valued) property from which this RTN was derived. |
| `d_plate_id` | field | `boost::optional<GPlatesModel::integer_plate_id_type>` | private | The cached plate ID, if it exists. |
| `d_time_of_formation` | field | `boost::optional<GPlatesPropertyValues::GeoTimeInstant>` | private | The cached time of formation of the feature, if it exists. |
| `d_boundary_sub_segment_seq` | field | `boundary_sub_segment_seq_type` | private | The sequence of SubSegment objects that form the resolved topology geometry \*boundary\*. |
| `d_triangulation_network` | field | `ResolvedTriangulation::Network::non_null_ptr_type` | private | The triangulation network. |
| `d_boundary_vertex_source_infos` | field | `boost::optional<resolved_vertex_source_info_seq_type>` | private | Each point in the boundary of the resolved topological network can potentially reference a different source reconstructed feature geometry. |
| `ResolvedTopologicalNetwork( const double &reconstruction_time_, const ResolvedTriangulation::Network::non_null_ptr_type &triangulation_network, GPlatesModel::FeatureHandle &feature_handle, GPlatesModel::FeatureHandle::iterator property_iterator_, BoundarySubSegmentForwardIter boundary_sub_segment_sequence_begin, Bounda ...` | constructor | `None` | private | Instantiate a network with an optional reconstruction plate ID and an optional time of formation. |
| `calc_boundary_vertex_source_infos()` | method | `void` | private | — |

## Free functions and macros

| Name | Kind | Type / body | Description |
|---|---|---|---|
| `GPLATES_APP_LOGIC_RESOLVEDTOPOLOGICALNETWORK_H` | macro | `None` | — |

## Notes

[[[PROSE notes unit=app-logic/ResolvedTopologicalNetwork tier=2]]]
Replace this whole block, markers included, with invariants, ownership, threading or gotchas that are not visible in the tables. Write *None.* if there is nothing worth saying.
[[[/PROSE]]]

## Used by

| Unit | Component | References |
|---|---|---|
| [app-logic/ReconstructionGeometryUtils](ReconstructionGeometryUtils.md) | app-logic | 7 |
| [app-logic/TopologyNetworkResolver](TopologyNetworkResolver.md) | app-logic | 4 |
| [app-logic/ScalarField3DLayerProxy](ScalarField3DLayerProxy.md) | app-logic | 3 |
| [app-logic/TopologyNetworkResolverLayerProxy](TopologyNetworkResolverLayerProxy.md) | app-logic | 3 |
| [app-logic/TopologyReconstruct](TopologyReconstruct.md) | app-logic | 3 |
| [app-logic/GeometryCookieCutter](GeometryCookieCutter.md) | app-logic | 2 |
| [app-logic/TopologyUtils](TopologyUtils.md) | app-logic | 2 |
| [gui/FeatureFocus](../gui/FeatureFocus.md) | gui | 2 |
| [presentation/ReconstructionGeometryRenderer](../presentation/ReconstructionGeometryRenderer.md) | presentation | 2 |
| [view-operations/FocusedFeatureGeometryManipulator](../view-operations/FocusedFeatureGeometryManipulator.md) | view-operations | 2 |
| [app-logic/AssignPlateIds](AssignPlateIds.md) | app-logic | 1 |
| [app-logic/PlateVelocityUtils](PlateVelocityUtils.md) | app-logic | 1 |
| [app-logic/ReconstructLayerProxy](ReconstructLayerProxy.md) | app-logic | 1 |
| [app-logic/ReconstructionGeometryFinder](ReconstructionGeometryFinder.md) | app-logic | 1 |
| [app-logic/TopologyPointLocation](TopologyPointLocation.md) | app-logic | 1 |
| [app-logic/VelocityFieldCalculatorLayerProxy](VelocityFieldCalculatorLayerProxy.md) | app-logic | 1 |
| [file-io/GMTFormatResolvedTopologicalGeometryExport](../file-io/GMTFormatResolvedTopologicalGeometryExport.md) | file-io | 1 |
| [file-io/ResolvedTopologicalGeometryExport](../file-io/ResolvedTopologicalGeometryExport.md) | file-io | 1 |
| [gui/ExportCitcomsResolvedTopologyAnimationStrategy](../gui/ExportCitcomsResolvedTopologyAnimationStrategy.md) | gui | 1 |
| [gui/ExportNetRotationAnimationStrategy](../gui/ExportNetRotationAnimationStrategy.md) | gui | 1 |

*... and 3 more units.*

## Related

*None.*

## Explore

Run these from the `gplates-code` skill directory:

```bash
python scripts/gpq.py file src/app-logic/ResolvedTopologicalNetwork.h
python scripts/gpq.py def GPlatesAppLogic::ResolvedTopologicalNetwork --body
python scripts/gpq.py uses ResolvedTopologicalNetwork --kind class
python scripts/gpq.py hier ResolvedTopologicalNetwork
```
