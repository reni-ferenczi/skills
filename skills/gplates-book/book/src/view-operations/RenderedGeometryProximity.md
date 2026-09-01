# RenderedGeometryProximity

[Book TOC](../../TOC.md) · [view-operations](../../components/view-operations.md) · cluster Community 921 · tier 2

| Source file | Kind | Lines |
|---|---|---|
| `src/view-operations/RenderedGeometryProximity.h` | C++ | 140 |
| `src/view-operations/RenderedGeometryProximity.cc` | C++ | 251 |

## Overview

[[[PROSE overview unit=view-operations/RenderedGeometryProximity tier=2]]]
Replace this whole block, markers included, with 1-3 paragraphs: what this unit is, why it exists, and how it fits the surrounding design. Do not restate the tables below.
[[[/PROSE]]]

## Declared types

| Name | Kind | Bases | Template | Subclasses | Description |
|---|---|---|---|---|---|
| [`GPlatesViewOperations::(anonymous)::RenderedGeometryLayerProximity`](#gplatesviewoperationsanonymousrenderedgeometrylayerproximity) | struct | — | — | 0 | Tests proximity to RenderedGeometry objects in an active RenderedGeometryLayer. |
| [`GPlatesViewOperations::RenderedGeometryProximityHit`](#gplatesviewoperationsrenderedgeometryproximityhit) | struct | — | — | 0 | Results of a single proximity hit. |
| [`GPlatesViewOperations::sorted_rendered_geometry_proximity_hits_type`](#gplatesviewoperationssorted_rendered_geometry_proximity_hits_type) | typedef | — | — | 0 | Sequence of hit detection results (one for each RenderedGeometry object hit). |

## Members

### `GPlatesViewOperations::(anonymous)::RenderedGeometryLayerProximity`

| Member | Kind | Type | Access | Description |
|---|---|---|---|---|
| `RenderedGeometryLayerProximity( sorted_rendered_geometry_proximity_hits_type &sorted_proximity_seq, const GPlatesMaths::ProximityCriteria &proximity_criteria, bool test_vertices_only = false)` | constructor | `None` | public | — |
| `operator()( const RenderedGeometryLayer &rendered_geom_layer)` | operator | `void` | public | — |
| `d_sorted_proximity_seq` | field | `sorted_rendered_geometry_proximity_hits_type` | public | — |
| `d_proximity_criteria` | field | `GPlatesMaths::ProximityCriteria` | public | — |
| `d_test_vertices_only` | field | `bool` | public | — |

### `GPlatesViewOperations::RenderedGeometryProximityHit`

| Member | Kind | Type | Access | Description |
|---|---|---|---|---|
| `RenderedGeometryProximityHit( RenderedGeometryLayer::rendered_geometry_index_type, const RenderedGeometryLayer *rendered_geom_layer, GPlatesMaths::ProximityHitDetail::non_null_ptr_type)` | constructor | `None` | public | — |
| `d_rendered_geom_index` | field | `RenderedGeometryLayer::rendered_geometry_index_type` | public | — |
| `d_rendered_geom_layer` | field | `RenderedGeometryLayer` | public | — |
| `d_proximity_hit_detail` | field | `GPlatesMaths::ProximityHitDetail::non_null_ptr_type` | public | — |

### `GPlatesViewOperations::sorted_rendered_geometry_proximity_hits_type`

*None.*

## Free functions and macros

| Name | Kind | Type / body | Description |
|---|---|---|---|
| `proximity_hit_closeness_compare( const RenderedGeometryProximityHit &lhs, const RenderedGeometryProximityHit &rhs)` | function | `bool` | Compare based on proximity closeness. |
| `sort_proximity_by_closeness( sorted_rendered_geometry_proximity_hits_type &sorted_proximity_seq)` | function | `void` | Sorts proximity hits by closeness. |
| `GPLATES_VIEWOPERATIONS_RENDEREDGEOMETRYPROXIMITY_H` | macro | `None` | — |
| `test_proximity( sorted_rendered_geometry_proximity_hits_type &sorted_proximity_hits, const GPlatesMaths::ProximityCriteria &, const RenderedGeometryLayer &)` | function | `bool` | Performs hit detection on the RenderedGeometry objects in the specified RenderedGeometryLayer. |
| `test_proximity( sorted_rendered_geometry_proximity_hits_type &sorted_proximity_hits, const RenderedGeometryCollection &rendered_geom_collection, const GPlatesMaths::ProximityCriteria &, const RenderedGeometryCollection::main_layers_update_type main_layers_to_test = RenderedGeometryCollection::ALL_MAIN_LAYERS, bool only ...` | function | `bool` | Performs hit detection on the RenderedGeometry objects in the specified RenderedGeometryLayer. |
| `test_vertex_proximity( sorted_rendered_geometry_proximity_hits_type &sorted_proximity_hits, const RenderedGeometryCollection &rendered_geom_collection, const RenderedGeometryCollection::main_layers_update_type main_layers_to_test, const GPlatesMaths::ProximityCriteria &, bool only_if_main_layer_active = true)` | function | `bool` | — |
| `test_proximity( sorted_rendered_geometry_proximity_hits_type &sorted_proximity_hits, const RenderedGeometryCollection &rendered_geom_collection, const GPlatesMaths::ProximityCriteria &proximity_criteria, const RenderedGeometryCollection::MainLayerType main_layer_to_test, bool only_if_main_layer_active = true)` | function | `bool` | Performs hit detection on the RenderedGeometry objects in the specified RenderedGeometryLayer. |
| `test_vertex_proximity( sorted_rendered_geometry_proximity_hits_type &sorted_proximity_hits, const RenderedGeometryCollection &rendered_geom_collection, const RenderedGeometryCollection::MainLayerType main_layer_to_test, const GPlatesMaths::ProximityCriteria &proximity_criteria, bool only_if_main_layer_active = true)` | function | `bool` | — |

## Notes

[[[PROSE notes unit=view-operations/RenderedGeometryProximity tier=2]]]
Replace this whole block, markers included, with invariants, ownership, threading or gotchas that are not visible in the tables. Write *None.* if there is nothing worth saying.
[[[/PROSE]]]

## Used by

| Unit | Component | References |
|---|---|---|
| [canvas-tools/SelectHellingerGeometries](../canvas-tools/SelectHellingerGeometries.md) | canvas-tools | 10 |
| [canvas-tools/AdjustFittedPoleEstimate](../canvas-tools/AdjustFittedPoleEstimate.md) | canvas-tools | 8 |
| [view-operations/MoveVertexGeometryOperation](MoveVertexGeometryOperation.md) | view-operations | 8 |
| [view-operations/SplitFeatureGeometryOperation](SplitFeatureGeometryOperation.md) | view-operations | 7 |
| [view-operations/RenderedGeometryUtils](RenderedGeometryUtils.md) | view-operations | 5 |
| [canvas-tools/MeasureDistance](../canvas-tools/MeasureDistance.md) | canvas-tools | 3 |
| [gui/AddClickedGeometriesToFeatureTable](../gui/AddClickedGeometriesToFeatureTable.md) | gui | 3 |
| [view-operations/InsertVertexGeometryOperation](InsertVertexGeometryOperation.md) | view-operations | 3 |
| [view-operations/DeleteVertexGeometryOperation](DeleteVertexGeometryOperation.md) | view-operations | 2 |
| [canvas-tools/BuildTopology](../canvas-tools/BuildTopology.md) | canvas-tools | 1 |
| [view-operations/AddPointGeometryOperation](AddPointGeometryOperation.md) | view-operations | 1 |
| [view-operations/ChangeLightDirectionOperation](ChangeLightDirectionOperation.md) | view-operations | 1 |
| [view-operations/MovePoleOperation](MovePoleOperation.md) | view-operations | 1 |

## Related

*None.*

## Explore

Run these from the `gplates-code` skill directory:

```bash
python scripts/gpq.py file src/view-operations/RenderedGeometryProximity.h
python scripts/gpq.py def GPlatesViewOperations::(anonymous)::RenderedGeometryLayerProximity --body
python scripts/gpq.py uses RenderedGeometryLayerProximity --kind struct
python scripts/gpq.py hier RenderedGeometryLayerProximity
```
