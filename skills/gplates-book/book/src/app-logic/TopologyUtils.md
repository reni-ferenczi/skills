# TopologyUtils

[Book TOC](../../TOC.md) · [app-logic](../../components/app-logic.md) · cluster Community 315 · tier 2

| Source file | Kind | Lines |
|---|---|---|
| `src/app-logic/TopologyUtils.h` | C++ | 313 |
| `src/app-logic/TopologyUtils.cc` | C++ | 1919 |

## Overview

[[[PROSE overview unit=app-logic/TopologyUtils tier=2]]]
Replace this whole block, markers included, with 1-3 paragraphs: what this unit is, why it exists, and how it fits the surrounding design. Do not restate the tables below.
[[[/PROSE]]]

## Declared types

| Name | Kind | Bases | Template | Subclasses | Description |
|---|---|---|---|---|---|
| [`GPlatesAppLogic::(anonymous)::ResolvedSubSegmentInfo`](#gplatesapplogicanonymousresolvedsubsegmentinfo) | struct | — | — | 0 | Associates a resolved topological sub-segment with its owning resolved topology. |
| [`GPlatesAppLogic::(anonymous)::topological_section_compare_type`](#gplatesapplogicanonymoustopological_section_compare_type) | typedef | — | — | 0 | Type used to compare reconstruction geometries. |
| [`GPlatesAppLogic::(anonymous)::resolved_section_to_sharing_resolved_topologies_map_type`](#gplatesapplogicanonymousresolved_section_to_sharing_resolved_topologies_map_type) | typedef | — | — | 0 | Map of each topological section to all the resolved topologies that use it for a sub-segment. |
| [`GPlatesAppLogic::(anonymous)::ResolvedSubSegmentMarker`](#gplatesapplogicanonymousresolvedsubsegmentmarker) | struct | — | — | 0 | The start or end of a sub-segment within the section geometry. |
| [`GPlatesAppLogic::(anonymous)::SortResolvedSubSegmentMarkers`](#gplatesapplogicanonymoussortresolvedsubsegmentmarkers) | class | — | — | 0 | Predicate to sort ResolvedSubSegmentMarker from beginning to end of the section geometry. |
| [`GPlatesAppLogic::TopologyUtils::resolved_topological_boundaries_networks_to_shared_sub_segments_map_type`](#gplatesapplogictopologyutilsresolved_topological_boundaries_networks_to_shared_sub_segments_map_type) | typedef | — | — | 0 | Typedef for a mapping from resolved topological boundaries and networks to their shared boundary sub-segments. |

## Members

### `GPlatesAppLogic::(anonymous)::ResolvedSubSegmentInfo`

| Member | Kind | Type | Access | Description |
|---|---|---|---|---|
| `ResolvedSubSegmentInfo( const ResolvedTopologicalGeometrySubSegment::non_null_ptr_type &sub_segment_, const ReconstructionGeometry::non_null_ptr_to_const_type &resolved_topology_)` | constructor | `None` | public | — |
| `sub_segment` | field | `ResolvedTopologicalGeometrySubSegment::non_null_ptr_type` | public | — |
| `resolved_topology` | field | `ReconstructionGeometry::non_null_ptr_to_const_type` | public | The resolved topology that owns the sub-segment... |

### `GPlatesAppLogic::(anonymous)::topological_section_compare_type`

*None.*

### `GPlatesAppLogic::(anonymous)::resolved_section_to_sharing_resolved_topologies_map_type`

*None.*

### `GPlatesAppLogic::(anonymous)::ResolvedSubSegmentMarker`

| Member | Kind | Type | Access | Description |
|---|---|---|---|---|
| `ResolvedSubSegmentMarker( const ResolvedTopologicalSharedSubSegment::ResolvedTopologyInfo &resolved_topology_info_, unsigned int num_vertices_in_section_, const boost::optional<ResolvedSubSegmentRangeInSection::IntersectionOrRubberBand> &intersection_or_rubber_band_, bool is_start_of_section_, bool is_start_of_sub_segm ...` | constructor | `None` | public | — |
| `is_start_rubber_band()` | method | `bool` | public | — |
| `is_end_rubber_band()` | method | `bool` | public | — |
| `is_equivalent_to( const ResolvedSubSegmentMarker &other)` | method | `bool` | public | Compare markers. |
| `resolved_topology_info` | field | `ResolvedTopologicalSharedSubSegment::ResolvedTopologyInfo` | public | The resolved topology that owns the sub-segment (and its geometry reversal flag)... |
| `num_vertices_in_section` | field | `unsigned int` | public | Number of vertices in the section geometry (point, multi-point or polyline). |
| `intersection_or_rubber_band` | field | `boost::optional<ResolvedSubSegmentRangeInSection::IntersectionOrRubberBand>` | public | Either (optional) start intersection/rubber-band if is\_start\_of\_section is true, or (optional) end intersection/rubber-band if is\_start\_of\_section is false. |
| `is_start_of_section` | field | `bool` | public | Whether this marker is the start or end of the \*section\*. |
| `is_start_of_sub_segment` | field | `bool` | public | This marker is either the \*sub-segment\* start or end. |

### `GPlatesAppLogic::(anonymous)::SortResolvedSubSegmentMarkers`

| Member | Kind | Type | Access | Description |
|---|---|---|---|---|
| `operator()( const ResolvedSubSegmentMarker &lhs, const ResolvedSubSegmentMarker &rhs)` | operator | `bool` | public | — |
| `d_point_on_sphere_predicate` | field | `GPlatesMaths::PointOnSphereMapPredicate` | private | — |

### `GPlatesAppLogic::TopologyUtils::resolved_topological_boundaries_networks_to_shared_sub_segments_map_type`

*None.*

## Free functions and macros

| Name | Kind | Type / body | Description |
|---|---|---|---|
| `map_resolved_topological_sections_to_resolved_topologies( resolved_section_to_sharing_resolved_topologies_map_type &resolved_section_to_sharing_resolved_topologies_map, const ReconstructionGeometry::non_null_ptr_to_const_type &resolved_topology, const sub_segment_seq_type &section_sub_segments)` | function | `void` | Maps each resolved topological section to all the resolved topologies that use it for a sub-segment. |
| `get_topological_section_compare( const ReconstructionGeometry::non_null_ptr_to_const_type &section_reconstruction_geometry)` | function | `boost::optional<topological_section_compare_type>` | Convert a section reconstruction geometry to a pair containing section feature and geometry property iterator. |
| `add_shared_sub_segment( shared_sub_segment_seq_type &shared_sub_segments, const ResolvedSubSegmentMarker &start_sub_segment_marker, const ResolvedSubSegmentMarker &end_sub_segment_marker, const std::vector<ResolvedTopologicalSharedSubSegment::ResolvedTopologyInfo> &sharing_resolved_topologies, const GPlatesMaths::Geome ...` | function | `void` | Create and add a shared sub-segment defined by the specified start and end markers. |
| `add_or_remove_marker_topology( std::vector<ResolvedTopologicalSharedSubSegment::ResolvedTopologyInfo> &sharing_resolved_topologies, const ResolvedSubSegmentMarker &sub_segment_marker)` | function | `void` | Add marker's topology to list of topologies if a start marker, otherwise remove from list. |
| `find_resolved_topological_section_sub_segment_markers( std::vector<ResolvedSubSegmentMarker> &resolved_sub_segment_marker_seq, const std::vector<ResolvedSubSegmentInfo> &section_sub_segment_infos, unsigned int num_points_in_section_geometry)` | function | `void` | Record the start/end point locations of each sub-segment within the section geometry. |
| `handle_rubber_band_sub_segment_markers( std::vector<ResolvedSubSegmentMarker> &markers, const GPlatesMaths::GeometryOnSphere::non_null_ptr_to_const_type &section_geometry)` | function | `void` | Handle start/end rubber band markers. |
| `get_resolved_topological_section_shared_sub_segments( shared_sub_segment_seq_type &shared_sub_segments, const std::vector<ResolvedSubSegmentMarker> &resolved_sub_segment_marker_seq, const GPlatesMaths::GeometryOnSphere::non_null_ptr_to_const_type &section_geometry, const ReconstructionGeometry::non_null_ptr_to_const_ty ...` | function | `void` | Iterate over the resolved section polyline segment markers and emit shared sub-segments for the section. |
| `GPLATES_APP_LOGIC_TOPOLOGYUTILS_H` | macro | `None` | — |
| `is_topological_feature( const GPlatesModel::FeatureHandle::const_weak_ref &feature)` | function | `bool` | Returns true if feature is topological. |
| `has_topological_features( const GPlatesModel::FeatureCollectionHandle::const_weak_ref &feature_collection)` | function | `bool` | Returns true if any feature in feature\_collection is topological. |
| `get_topological_geometry_type( const GPlatesModel::FeatureHandle::const_weak_ref &feature)` | function | `boost::optional<TopologyGeometry::Type>` | Returns the type of topological geometry represented in the specified feature. |
| `is_topological_line_feature( const GPlatesModel::FeatureHandle::const_weak_ref &feature)` | function | `bool` | Returns true if feature contains a topological line geometry. |
| `has_topological_line_features( const GPlatesModel::FeatureCollectionHandle::const_weak_ref &feature_collection)` | function | `bool` | Returns true if feature\_collection contains topological line features. |
| `resolve_topological_lines( std::vector<ResolvedTopologicalLine::non_null_ptr_type> &resolved_topological_lines, const std::vector<GPlatesModel::FeatureCollectionHandle::weak_ref> &topological_line_features_collection, const ReconstructionTreeCreator &reconstruction_tree_creator, const double &reconstruction_time, boost ...` | function | `ReconstructHandle::type` | Create and return a sequence of ResolvedTopologicalLine objects by resolving topological lines in topological\_line\_features\_collection. |
| `resolve_topological_lines( std::vector<ResolvedTopologicalLine::non_null_ptr_type> &resolved_topological_lines, const std::vector<GPlatesModel::FeatureHandle::weak_ref> &topological_line_features, const ReconstructionTreeCreator &reconstruction_tree_creator, const double &reconstruction_time, boost::optional<const std: ...` | function | `ReconstructHandle::type` | An overload of resolve\_topological\_lines accepting a vector of features instead of a feature collection. |
| `is_topological_boundary_feature( const GPlatesModel::FeatureHandle::const_weak_ref &feature)` | function | `bool` | Returns true if feature contains a topological polygon geometry. |
| `has_topological_boundary_features( const GPlatesModel::FeatureCollectionHandle::const_weak_ref &feature_collection)` | function | `bool` | Returns true if feature\_collection contains topological polygon features. |
| `resolve_topological_boundaries( std::vector<ResolvedTopologicalBoundary::non_null_ptr_type> &resolved_topological_boundaries, const std::vector<GPlatesModel::FeatureCollectionHandle::weak_ref> &topological_closed_plate_polygon_features_collection, const ReconstructionTreeCreator &reconstruction_tree_creator, const doub ...` | function | `ReconstructHandle::type` | Create and return a sequence of ResolvedTopologicalBoundary objects by resolving topological closed plate boundaries in topological\_closed\_plate\_polygon\_features\_collection. |
| `resolve_topological_boundaries( std::vector<ResolvedTopologicalBoundary::non_null_ptr_type> &resolved_topological_boundaries, const std::vector<GPlatesModel::FeatureHandle::weak_ref> &topological_closed_plate_polygon_features, const ReconstructionTreeCreator &reconstruction_tree_creator, const double &reconstruction_ti ...` | function | `ReconstructHandle::type` | An overload of resolve\_topological\_boundaries accepting a vector of features instead of a feature collection. |
| `is_topological_network_feature( const GPlatesModel::FeatureHandle::const_weak_ref &feature)` | function | `bool` | Returns true if feature is a topological network feature. |
| `has_topological_network_features( const GPlatesModel::FeatureCollectionHandle::const_weak_ref &feature_collection)` | function | `bool` | Returns true if feature\_collection contains topological network features. |
| `resolve_topological_networks( std::vector<ResolvedTopologicalNetwork::non_null_ptr_type> &resolved_topological_networks, const double &reconstruction_time, const std::vector<GPlatesModel::FeatureCollectionHandle::weak_ref> &topological_network_features_collection, boost::optional<const std::vector<ReconstructHandle::ty ...` | function | `ReconstructHandle::type` | Create and return a sequence of ResolvedTopologicalNetwork objects by resolving topological networks in topological\_network\_features\_collection. |
| `resolve_topological_networks( std::vector<ResolvedTopologicalNetwork::non_null_ptr_type> &resolved_topological_networks, const double &reconstruction_time, const std::vector<GPlatesModel::FeatureHandle::weak_ref> &topological_network_features, boost::optional<const std::vector<ReconstructHandle::type> &> topological_ge ...` | function | `ReconstructHandle::type` | An overload of resolve\_topological\_networks accepting a vector of features instead of a feature collection. |
| `find_resolved_topological_sections( std::vector<ResolvedTopologicalSection::non_null_ptr_type> &resolved_topological_sections, const std::vector<ResolvedTopologicalBoundary::non_null_ptr_to_const_type> &resolved_topological_boundaries, const std::vector<ResolvedTopologicalNetwork::non_null_ptr_to_const_type> &resolved_ ...` | function | `void` | Finds all sub-segments shared by resolved topology boundaries and network boundaries. |
| `map_resolved_topological_boundaries_networks_to_shared_sub_segments( resolved_topological_boundaries_networks_to_shared_sub_segments_map_type &resolved_topological_shared_sub_segments_map, const std::vector<ResolvedTopologicalSection::non_null_ptr_type> &resolved_topological_sections)` | function | `void` | Takes a sequence of resolved topological sections and creates a mapping from resolved topological boundaries and networks to their shared boundary sub-segments. |

## Notes

[[[PROSE notes unit=app-logic/TopologyUtils tier=2]]]
Replace this whole block, markers included, with invariants, ownership, threading or gotchas that are not visible in the tables. Write *None.* if there is nothing worth saying.
[[[/PROSE]]]

## Used by

| Unit | Component | References |
|---|---|---|
| [app-logic/Reconstruction](Reconstruction.md) | app-logic | 11 |
| [app-logic/GeometryCookieCutter](GeometryCookieCutter.md) | app-logic | 7 |
| [app-logic/TopologyGeometryResolverLayerProxy](TopologyGeometryResolverLayerProxy.md) | app-logic | 7 |
| [presentation/ReconstructionGeometryRenderer](../presentation/ReconstructionGeometryRenderer.md) | presentation | 7 |
| [app-logic/TopologyGeometryResolverLayerTask](TopologyGeometryResolverLayerTask.md) | app-logic | 5 |
| [app-logic/TopologyNetworkResolverLayerProxy](TopologyNetworkResolverLayerProxy.md) | app-logic | 5 |
| [file-io/CitcomsResolvedTopologicalBoundaryExport](../file-io/CitcomsResolvedTopologicalBoundaryExport.md) | file-io | 5 |
| [gui/GeometryFocusHighlight](../gui/GeometryFocusHighlight.md) | gui | 5 |
| [app-logic/ResolvedSubSegmentRangeInSection](ResolvedSubSegmentRangeInSection.md) | app-logic | 3 |
| [app-logic/TopologyNetworkResolverLayerTask](TopologyNetworkResolverLayerTask.md) | app-logic | 3 |
| [canvas-tools/EditTopology](../canvas-tools/EditTopology.md) | canvas-tools | 3 |
| [file-io/FeatureCollectionFileFormatClassify](../file-io/FeatureCollectionFileFormatClassify.md) | file-io | 3 |
| [gui/FeatureInspectionCanvasToolWorkflow](../gui/FeatureInspectionCanvasToolWorkflow.md) | gui | 3 |
| [gui/PoleManipulationCanvasToolWorkflow](../gui/PoleManipulationCanvasToolWorkflow.md) | gui | 3 |
| [gui/TopologyCanvasToolWorkflow](../gui/TopologyCanvasToolWorkflow.md) | gui | 3 |
| [view-operations/VisibleReconstructionGeometryExport](../view-operations/VisibleReconstructionGeometryExport.md) | view-operations | 3 |
| [app-logic/LayerProxyUtils](LayerProxyUtils.md) | app-logic | 2 |
| [app-logic/AssignPlateIds](AssignPlateIds.md) | app-logic | 1 |
| [app-logic/PlateVelocityUtils](PlateVelocityUtils.md) | app-logic | 1 |
| [app-logic/ReconstructLayerProxy](ReconstructLayerProxy.md) | app-logic | 1 |

*... and 8 more units.*

## Related

*None.*

## Explore

Run these from the `gplates-code` skill directory:

```bash
python scripts/gpq.py file src/app-logic/TopologyUtils.h
python scripts/gpq.py def GPlatesAppLogic::(anonymous)::ResolvedSubSegmentMarker --body
python scripts/gpq.py uses ResolvedSubSegmentMarker --kind struct
python scripts/gpq.py hier ResolvedSubSegmentMarker
```
