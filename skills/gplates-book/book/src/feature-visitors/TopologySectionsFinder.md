# TopologySectionsFinder

[Book TOC](../../TOC.md) · [feature-visitors](../../components/feature-visitors.md) · cluster Community 496 · tier 2

| Source file | Kind | Lines |
|---|---|---|
| `src/feature-visitors/TopologySectionsFinder.h` | C++ | 187 |
| `src/feature-visitors/TopologySectionsFinder.cc` | C++ | 343 |

## Overview

[[[PROSE overview unit=feature-visitors/TopologySectionsFinder tier=2]]]
Replace this whole block, markers included, with 1-3 paragraphs: what this unit is, why it exists, and how it fits the surrounding design. Do not restate the tables below.
[[[/PROSE]]]

## Declared types

| Name | Kind | Bases | Template | Subclasses | Description |
|---|---|---|---|---|---|
| [`GPlatesFeatureVisitors::TopologySectionsFinder`](#gplatesfeaturevisitorstopologysectionsfinder) | class | [`GPlatesModel::ConstFeatureVisitor`](../model/FeatureVisitor.md)<br>`boost::noncopyable` | — | 0 | — |

## Members

### `GPlatesFeatureVisitors::TopologySectionsFinder`

| Member | Kind | Type | Access | Description |
|---|---|---|---|---|
| `TopologySectionsFinder()` | constructor | `None` | public | — |
| `~TopologySectionsFinder()` | destructor | `None` | public | — |
| `initialise_pre_feature_properties( const GPlatesModel::FeatureHandle &feature_handle)` | method | `bool` | public | — |
| `visit_gpml_constant_value( const GPlatesPropertyValues::GpmlConstantValue &gpml_constant_value)` | method | `void` | public | — |
| `visit_gpml_piecewise_aggregation( const GPlatesPropertyValues::GpmlPiecewiseAggregation &gpml_piecewise_aggregation)` | method | `void` | public | — |
| `process_gpml_time_window( const GPlatesPropertyValues::GpmlTimeWindow &gpml_time_window)` | method | `void` | public | — |
| `visit_gpml_topological_line( const GPlatesPropertyValues::GpmlTopologicalLine &gpml_topological_line)` | method | `void` | public | — |
| `visit_gpml_topological_network( const GPlatesPropertyValues::GpmlTopologicalNetwork &gpml_topological_network)` | method | `void` | public | — |
| `visit_gpml_topological_network_interior( const GPlatesPropertyValues::GpmlPropertyDelegate &gpml_topological_network_interior)` | method | `void` | public | — |
| `visit_gpml_topological_polygon( const GPlatesPropertyValues::GpmlTopologicalPolygon &gpml_topological_polygon)` | method | `void` | public | — |
| `visit_gpml_topological_line_section( const GPlatesPropertyValues::GpmlTopologicalLineSection &gpml_topological_line_section)` | method | `void` | public | — |
| `visit_gpml_topological_point( const GPlatesPropertyValues::GpmlTopologicalPoint &gpml_topological_point)` | method | `void` | public | — |
| `report()` | method | `void` | public | — |
| `boundary_sections_begin()` | method | `GPlatesGui::TopologySectionsContainer::const_iterator` | public | accesor functions for the boundary |
| `boundary_sections_end()` | method | `GPlatesGui::TopologySectionsContainer::const_iterator` | public | — |
| `number_of_boundary_sections()` | method | `int` | public | — |
| `interior_sections_begin()` | method | `GPlatesGui::TopologySectionsContainer::const_iterator` | public | accesor functions for the interior |
| `interior_sections_end()` | method | `GPlatesGui::TopologySectionsContainer::const_iterator` | public | — |
| `number_of_interior_sections()` | method | `int` | public | — |
| `d_seq_num` | field | `int` | private | controls which container |
| `d_boundary_sections` | field | `GPlatesGui::TopologySectionsContainer::container_type` | private | Collections of TableRows built from this feature's Topology data |
| `d_interior_sections` | field | `GPlatesGui::TopologySectionsContainer::container_type` | private | — |

## Free functions and macros

| Name | Kind | Type / body | Description |
|---|---|---|---|
| `GPLATES_FEATUREVISITORS_TOPOLOGY_SECTIONS_FINDER_H` | macro | `None` | — |

## Notes

[[[PROSE notes unit=feature-visitors/TopologySectionsFinder tier=2]]]
Replace this whole block, markers included, with invariants, ownership, threading or gotchas that are not visible in the tables. Write *None.* if there is nothing worth saying.
[[[/PROSE]]]

## Used by

| Unit | Component | References |
|---|---|---|
| [gui/TopologyTools](../gui/TopologyTools.md) | gui | 47 |
| [qt-widgets/TopologyToolsWidget](../qt-widgets/TopologyToolsWidget.md) | qt-widgets | 10 |
| [api/PyTopologyTools](../api/PyTopologyTools.md) | api | 7 |

## Related

*None.*

## Explore

Run these from the `gplates-code` skill directory:

```bash
python scripts/gpq.py file src/feature-visitors/TopologySectionsFinder.h
python scripts/gpq.py def GPlatesFeatureVisitors::TopologySectionsFinder --body
python scripts/gpq.py uses TopologySectionsFinder --kind class
python scripts/gpq.py hier TopologySectionsFinder
```
