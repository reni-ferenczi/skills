# TopologyGeometryResolver

[Book TOC](../../TOC.md) · [app-logic](../../components/app-logic.md) · cluster Community 571 · tier 2

| Source file | Kind | Lines |
|---|---|---|
| `src/app-logic/TopologyGeometryResolver.h` | C++ | 318 |
| `src/app-logic/TopologyGeometryResolver.cc` | C++ | 810 |

## Overview

[[[PROSE overview unit=app-logic/TopologyGeometryResolver tier=2]]]
Replace this whole block, markers included, with 1-3 paragraphs: what this unit is, why it exists, and how it fits the surrounding design. Do not restate the tables below.
[[[/PROSE]]]

## Declared types

| Name | Kind | Bases | Template | Subclasses | Description |
|---|---|---|---|---|---|
| [`GPlatesAppLogic::TopologyGeometryResolver`](#gplatesapplogictopologygeometryresolver) | class | [`GPlatesModel::FeatureVisitor`](../model/FeatureVisitor.md)<br>`boost::noncopyable` | — | 0 | Finds all topological geometry features such as topological closed plate boundaries or topological lines, in the features visited, that exist at a particular reconstruction time and creates ResolvedTopologicalBoundary and/or ... |

## Members

### `GPlatesAppLogic::TopologyGeometryResolver`

| Member | Kind | Type | Access | Description |
|---|---|---|---|---|
| `TopologyGeometryResolver( std::vector<ResolvedTopologicalLine::non_null_ptr_type> &resolved_topological_lines, ReconstructHandle::type reconstruct_handle, const ReconstructionTreeCreator &reconstruction_tree_creator, const double &reconstruction_time, boost::optional<const std::vector<ReconstructHandle::type> &> topolo ...` | constructor | `None` | public | The resolved topological \*lines\* are appended to resolved\_topological\_lines. the subset, of all reconstruction geometries observing the topological section features, that should be searched when resolving the topological geometries. |
| `TopologyGeometryResolver( std::vector<ResolvedTopologicalBoundary::non_null_ptr_type> &resolved_topological_boundaries, ReconstructHandle::type reconstruct_handle, const ReconstructionTreeCreator &reconstruction_tree_creator, const double &reconstruction_time, boost::optional<const std::vector<ReconstructHandle::type> ...` | constructor | `None` | public | The resolved topological \*boundaries\* are appended to resolved\_topological\_boundaries. the subset, of all reconstruction geometries observing the topological section features, that should be searched when resolving the topological ... |
| `TopologyGeometryResolver( std::vector<ResolvedTopologicalLine::non_null_ptr_type> &resolved_topological_lines, std::vector<ResolvedTopologicalBoundary::non_null_ptr_type> &resolved_topological_boundaries, ReconstructHandle::type reconstruct_handle, const ReconstructionTreeCreator &reconstruction_tree_creator, const dou ...` | constructor | `None` | public | The resolved topological \*lines\* are appended to resolved\_topological\_lines and the resolved topological \*boundaries\* are appended to resolved\_topological\_boundaries. the subset, of all reconstruction geometries observing the topological ... |
| `~TopologyGeometryResolver()` | destructor | `None` | public | — |
| `initialise_pre_feature_properties( GPlatesModel::FeatureHandle &feature_handle)` | method | `bool` | public | — |
| `visit_gpml_constant_value( GPlatesPropertyValues::GpmlConstantValue &gpml_constant_value)` | method | `void` | public | — |
| `visit_gpml_piecewise_aggregation( GPlatesPropertyValues::GpmlPiecewiseAggregation &gpml_piecewise_aggregation)` | method | `void` | public | — |
| `visit_gpml_time_window( GPlatesPropertyValues::GpmlTimeWindow &gpml_time_window)` | method | `void` | public | — |
| `visit_gpml_topological_polygon( GPlatesPropertyValues::GpmlTopologicalPolygon &gpml_topological_polygon)` | method | `void` | public | — |
| `visit_gpml_topological_line( GPlatesPropertyValues::GpmlTopologicalLine &gpml_topological_line)` | method | `void` | public | — |
| `visit_gpml_topological_line_section( GPlatesPropertyValues::GpmlTopologicalLineSection &gpml_topological_line_section)` | method | `void` | public | — |
| `visit_gpml_topological_point( GPlatesPropertyValues::GpmlTopologicalPoint &gpml_topological_point)` | method | `void` | public | — |
| `ResolvedGeometry` | class | `None` | private | Stores/builds information from iterating over GpmlTopologicalSection objects. |
| `ResolveGeometryType` | enum | `None` | private | The type of topological geometry to resolve. |
| `d_resolved_topological_lines` | field | `boost::optional<std::vector<ResolvedTopologicalLine::non_null_ptr_type> &>` | private | The resolved topological \*lines\* we're generating (if requested). |
| `d_resolved_topological_boundaries` | field | `boost::optional<std::vector<ResolvedTopologicalBoundary::non_null_ptr_type> &>` | private | The resolved topological \*boundaries\* we're generating (if requested). |
| `d_reconstruct_handle` | field | `ReconstructHandle::type` | private | The reconstruction identifier placed in all resolved topological geometries. |
| `d_reconstruction_tree_creator` | field | `ReconstructionTreeCreator` | private | The reconstruction tree creator associated with the resolved topological geometries. |
| `d_reconstruction_tree` | field | `ReconstructionTree::non_null_ptr_to_const_type` | private | The reconstruction tree associated with the resolved topological geometries being generated. |
| `d_topological_sections_reconstruct_handles` | field | `boost::optional<std::vector<ReconstructHandle::type> >` | private | A list of reconstruct handles that identifies the subset, of all reconstruction geometries observing the topological section features, that should be searched when resolving the topological geometry. |
| `d_currently_visited_feature` | field | `GPlatesModel::FeatureHandle::weak_ref` | private | The current feature being visited. |
| `d_current_resolved_geometry_type` | field | `boost::optional<ResolveGeometryType>` | private | The current resolved geometry property type being visited. |
| `d_reconstruction_params` | field | `ReconstructionFeatureProperties` | private | Gathers some useful reconstruction parameters. |
| `d_resolved_geometry` | field | `ResolvedGeometry` | private | Used to help build the resolved geometry of the current topological geometry. |
| `create_resolved_topological_boundary()` | method | `void` | private | Create a \*polygon\* ResolvedTopologicalBoundary from information gathered from the most recently visited topological polygon (stored in d\_resolved\_geometry). |
| `create_resolved_topological_line()` | method | `void` | private | Create a \*polyline\* ResolvedTopologicalLine from information gathered from the most recently visited topological line (stored in d\_resolved\_geometry). |
| `record_topological_sections( const TopologicalSectionsIterator &sections_begin, const TopologicalSectionsIterator &sections_end)` | method | `void` | private | — |
| `record_topological_section_reconstructed_geometry( const GPlatesModel::FeatureId &source_feature_id, const GPlatesPropertyValues::GpmlPropertyDelegate &geometry_delegate, bool reverse_hint)` | method | `boost::optional<ResolvedGeometry::Section>` | private | — |
| `process_resolved_boundary_topological_section_intersections()` | method | `void` | private | — |
| `process_resolved_boundary_topological_section_intersection( const std::size_t current_section_index, const bool two_sections = false)` | method | `void` | private | — |
| `process_resolved_line_topological_section_intersections()` | method | `void` | private | — |
| `process_resolved_line_topological_section_intersection( const std::size_t current_section_index)` | method | `void` | private | — |
| `debug_output_topological_section_feature_id( const GPlatesModel::FeatureId &section_feature_id)` | method | `void` | private | — |

## Free functions and macros

| Name | Kind | Type / body | Description |
|---|---|---|---|
| `GPLATES_APP_LOGIC_TOPOLOGY_GEOMETRY_RESOLVER_H` | macro | `None` | — |

## Notes

[[[PROSE notes unit=app-logic/TopologyGeometryResolver tier=2]]]
Replace this whole block, markers included, with invariants, ownership, threading or gotchas that are not visible in the tables. Write *None.* if there is nothing worth saying.
[[[/PROSE]]]

## Used by

| Unit | Component | References |
|---|---|---|
| [app-logic/TopologyUtils](TopologyUtils.md) | app-logic | 18 |

## Related

*None.*

## Explore

Run these from the `gplates-code` skill directory:

```bash
python scripts/gpq.py file src/app-logic/TopologyGeometryResolver.h
python scripts/gpq.py def GPlatesAppLogic::TopologyGeometryResolver --body
python scripts/gpq.py uses TopologyGeometryResolver --kind class
python scripts/gpq.py hier TopologyGeometryResolver
```
