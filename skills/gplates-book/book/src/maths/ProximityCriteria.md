# ProximityCriteria

[Book TOC](../../TOC.md) · [maths](../../components/maths.md) · cluster Community 27 · tier 3

| Source file | Kind | Lines |
|---|---|---|
| `src/maths/ProximityCriteria.h` | C++ | 82 |
| `src/maths/ProximityCriteria.cc` | C++ | 38 |

## Overview

A parameter object encapsulating the criteria for proximity queries on the sphere. It stores a test point and a closeness threshold (supplied as a cosine value and converted to an `AngularExtent`). The threshold provides both a closeness inclusion limit and a latitude exclusion limit — the sine and cosine components of the angular extent — allowing both angular distance and latitudinal constraints to be applied uniformly in proximity tests across different geometry types.

## Declared types

| Name | Kind | Bases | Template | Subclasses | Description |
|---|---|---|---|---|---|
| [`GPlatesMaths::ProximityCriteria`](#gplatesmathsproximitycriteria) | class | — | — | 0 | This class contains the parameters for the various proximity criteria. |

## Members

### `GPlatesMaths::ProximityCriteria`

| Member | Kind | Type | Access | Description |
|---|---|---|---|---|
| `ProximityCriteria( const PointOnSphere &test_point_, const double &closeness_inclusion_threshold_)` | constructor | `None` | public | — |
| `d_test_point` | field | `PointOnSphere` | private | — |
| `d_closeness_angular_extent_threshold` | field | `AngularExtent` | private | — |

## Free functions and macros

| Name | Kind | Type / body | Description |
|---|---|---|---|
| `GPLATES_MATHS_PROXIMITYCRITERIA_H` | macro | `None` | — |

## Notes

*None.*

## Used by

| Unit | Component | References |
|---|---|---|
| [view-operations/RenderedGeometryProximity](../view-operations/RenderedGeometryProximity.md) | view-operations | 2 |
| [canvas-tools/MeasureDistance](../canvas-tools/MeasureDistance.md) | canvas-tools | 1 |
| [data-mining/deprecated/IsInRegionOfInterestVisitor](../data-mining/deprecated/IsInRegionOfInterestVisitor.md) | data-mining | 1 |
| [data-mining/deprecated/RegionOfInterestAssociationOperator](../data-mining/deprecated/RegionOfInterestAssociationOperator.md) | data-mining | 1 |
| [feature-visitors/TopologySectionsFinder](../feature-visitors/TopologySectionsFinder.md) | feature-visitors | 1 |
| [gui/AddClickedGeometriesToFeatureTable](../gui/AddClickedGeometriesToFeatureTable.md) | gui | 1 |
| [gui/TopologyTools](../gui/TopologyTools.md) | gui | 1 |
| [maths/MultiPointOnSphere](MultiPointOnSphere.md) | maths | 1 |
| [maths/PointOnSphere](PointOnSphere.md) | maths | 1 |
| [maths/PolygonOnSphere](PolygonOnSphere.md) | maths | 1 |
| [maths/PolylineOnSphere](PolylineOnSphere.md) | maths | 1 |
| [view-operations/AddPointGeometryOperation](../view-operations/AddPointGeometryOperation.md) | view-operations | 1 |
| [view-operations/DeleteVertexGeometryOperation](../view-operations/DeleteVertexGeometryOperation.md) | view-operations | 1 |
| [view-operations/InsertVertexGeometryOperation](../view-operations/InsertVertexGeometryOperation.md) | view-operations | 1 |
| [view-operations/MoveVertexGeometryOperation](../view-operations/MoveVertexGeometryOperation.md) | view-operations | 1 |
| [view-operations/RenderedColouredPolygonOnSphere](../view-operations/RenderedColouredPolygonOnSphere.md) | view-operations | 1 |
| [view-operations/RenderedColouredPolylineOnSphere](../view-operations/RenderedColouredPolylineOnSphere.md) | view-operations | 1 |
| [view-operations/RenderedColouredTriangleSurfaceMesh](../view-operations/RenderedColouredTriangleSurfaceMesh.md) | view-operations | 1 |
| [view-operations/RenderedGeometry](../view-operations/RenderedGeometry.md) | view-operations | 1 |
| [view-operations/RenderedPolygonOnSphere](../view-operations/RenderedPolygonOnSphere.md) | view-operations | 1 |

*... and 3 more units.*

## Related

*None.*

## Explore

Run these from the `gplates-code` skill directory:

```bash
python scripts/gpq.py file src/maths/ProximityCriteria.h
python scripts/gpq.py def GPlatesMaths::ProximityCriteria --body
python scripts/gpq.py uses ProximityCriteria --kind class
python scripts/gpq.py hier ProximityCriteria
```
