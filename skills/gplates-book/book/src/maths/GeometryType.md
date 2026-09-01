# GeometryType

[Book TOC](../../TOC.md) · [maths](../../components/maths.md) · cluster Community 1956 · tier 2

| Source file | Kind | Lines |
|---|---|---|
| `src/maths/GeometryType.h` | C++ | 47 |

## Overview

`GeometryType::Value` is a lightweight runtime tag for the four concrete
`GeometryOnSphere` shapes (point, multi-point, polyline, polygon), plus
`NONE` for "no geometry". It exists so code that needs to know or store which
kind of geometry it is dealing with — GUI widgets picking a digitisation tool,
geometry builders tracking what the user is constructing, feature-geometry
lookups — can do so with a plain enum comparison or switch, instead of
dispatching through a `ConstGeometryOnSphereVisitor` or testing dynamic types
every time. Its very wide fan-in across `view-operations`, `gui`,
`qt-widgets` and `app-logic` reflects that it is the common vocabulary these
layers use to talk about "what kind of geometry is this" without depending on
the geometry classes themselves.

## Declared types

| Name | Kind | Bases | Template | Subclasses | Description |
|---|---|---|---|---|---|
| [`GPlatesMaths::GeometryType::Value`](#gplatesmathsgeometrytypevalue) | enum | — | — | 0 | Types of GeometryOnSphere. |

## Members

### `GPlatesMaths::GeometryType::Value`

| Member | Kind | Type | Access | Description |
|---|---|---|---|---|
| `NONE` | enumerator | `None` | — | — |
| `POINT` | enumerator | `None` | — | — |
| `MULTIPOINT` | enumerator | `None` | — | — |
| `POLYLINE` | enumerator | `None` | — | — |
| `POLYGON` | enumerator | `None` | — | — |

## Free functions and macros

| Name | Kind | Type / body | Description |
|---|---|---|---|
| `GPLATES_MATHS_GEOMETRYTYPE_H` | macro | `None` | — |

## Notes

*None.*

## Used by

| Unit | Component | References |
|---|---|---|
| [app-logic/GeometryUtils](../app-logic/GeometryUtils.md) | app-logic | 63 |
| [view-operations/InternalGeometryBuilder](../view-operations/InternalGeometryBuilder.md) | view-operations | 45 |
| [view-operations/GeometryBuilder](../view-operations/GeometryBuilder.md) | view-operations | 38 |
| [qt-widgets/EditGeometryWidget](../qt-widgets/EditGeometryWidget.md) | qt-widgets | 35 |
| [gui/DigitisationCanvasToolWorkflow](../gui/DigitisationCanvasToolWorkflow.md) | gui | 32 |
| [presentation/ReconstructionGeometryRenderer](../presentation/ReconstructionGeometryRenderer.md) | presentation | 30 |
| [gui/FeatureInspectionCanvasToolWorkflow](../gui/FeatureInspectionCanvasToolWorkflow.md) | gui | 27 |
| [view-operations/InsertVertexGeometryOperation](../view-operations/InsertVertexGeometryOperation.md) | view-operations | 26 |
| [qt-widgets/LatLonCoordinatesTable](../qt-widgets/LatLonCoordinatesTable.md) | qt-widgets | 18 |
| [utils/GeometryCreationUtils](../utils/GeometryCreationUtils.md) | utils | 17 |
| [view-operations/AddPointGeometryOperation](../view-operations/AddPointGeometryOperation.md) | view-operations | 17 |
| [canvas-tools/DigitiseGeometry](../canvas-tools/DigitiseGeometry.md) | canvas-tools | 14 |
| [view-operations/DeleteVertexGeometryOperation](../view-operations/DeleteVertexGeometryOperation.md) | view-operations | 14 |
| [view-operations/SplitFeatureGeometryOperation](../view-operations/SplitFeatureGeometryOperation.md) | view-operations | 12 |
| [app-logic/PartitionFeatureUtils](../app-logic/PartitionFeatureUtils.md) | app-logic | 10 |
| [app-logic/ReconstructUtils](../app-logic/ReconstructUtils.md) | app-logic | 9 |
| [canvas-tools/MeasureDistance](../canvas-tools/MeasureDistance.md) | canvas-tools | 9 |
| [data-mining/deprecated/IsInRegionOfInterestVisitor](../data-mining/deprecated/IsInRegionOfInterestVisitor.md) | data-mining | 9 |
| [view-operations/FocusedFeatureGeometryManipulator](../view-operations/FocusedFeatureGeometryManipulator.md) | view-operations | 8 |
| [canvas-tools/MeasureDistanceState](../canvas-tools/MeasureDistanceState.md) | canvas-tools | 7 |

*... and 10 more units.*

## Related

*None.*

## Explore

Run these from the `gplates-code` skill directory:

```bash
python scripts/gpq.py file src/maths/GeometryType.h
python scripts/gpq.py def GPlatesMaths::GeometryType::Value --body
python scripts/gpq.py uses Value --kind enum
```
