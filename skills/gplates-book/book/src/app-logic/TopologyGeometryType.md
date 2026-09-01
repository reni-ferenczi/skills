# TopologyGeometryType

[Book TOC](../../TOC.md) · [app-logic](../../components/app-logic.md) · cluster Community 2 · tier 2

| Source file | Kind | Lines |
|---|---|---|
| `src/app-logic/TopologyGeometryType.h` | C++ | 56 |

## Overview

`TopologyGeometry::Type` distinguishes the three ways a topological feature can be resolved — as a line, a boundary polygon, or a network triangulation — independently of the feature's own GPGIM feature type. Code that builds or edits topologies, such as `TopologyInternalUtils` and the `gui::TopologyTools` canvas workflow, uses it to decide which resolving and editing logic applies to a given topological feature.

## Declared types

| Name | Kind | Bases | Template | Subclasses | Description |
|---|---|---|---|---|---|
| [`GPlatesAppLogic::TopologyGeometry::Type`](#gplatesapplogictopologygeometrytype) | enum | — | — | 0 | The type of topological geometry represented in a feature. |

## Members

### `GPlatesAppLogic::TopologyGeometry::Type`

| Member | Kind | Type | Access | Description |
|---|---|---|---|---|
| `LINE` | enumerator | `None` | — | Resolves to form a polyline. |
| `BOUNDARY` | enumerator | `None` | — | Resolves to form a polygon (with optional interior holes/boundaries). |
| `NETWORK` | enumerator | `None` | — | Resolves to form a triangulation within a polygon (and its optional interior constraints). |

## Free functions and macros

| Name | Kind | Type / body | Description |
|---|---|---|---|
| `GPLATES_APP_LOGIC_TOPOLOGYGEOMETRYTYPE_H` | macro | `None` | — |

## Notes

*None.*

## Used by

| Unit | Component | References |
|---|---|---|
| [gui/TopologyTools](../gui/TopologyTools.md) | gui | 44 |
| [app-logic/TopologyGeometryResolverLayerProxy](TopologyGeometryResolverLayerProxy.md) | app-logic | 28 |
| [app-logic/TopologyInternalUtils](TopologyInternalUtils.md) | app-logic | 15 |
| [canvas-tools/BuildTopology](../canvas-tools/BuildTopology.md) | canvas-tools | 14 |
| [qt-widgets/TopologyToolsWidget](../qt-widgets/TopologyToolsWidget.md) | qt-widgets | 10 |
| [app-logic/TopologyUtils](TopologyUtils.md) | app-logic | 9 |
| [app-logic/TopologyNetworkResolverLayerProxy](TopologyNetworkResolverLayerProxy.md) | app-logic | 8 |
| [canvas-tools/EditTopology](../canvas-tools/EditTopology.md) | canvas-tools | 8 |
| [gui/TopologyCanvasToolWorkflow](../gui/TopologyCanvasToolWorkflow.md) | gui | 6 |
| [app-logic/DependentTopologicalSectionLayers](DependentTopologicalSectionLayers.md) | app-logic | 5 |
| [app-logic/ReconstructLayerProxy](ReconstructLayerProxy.md) | app-logic | 2 |
| [qt-widgets/CreateFeatureDialog](../qt-widgets/CreateFeatureDialog.md) | qt-widgets | 1 |

## Related

*None.*

## Explore

Run these from the `gplates-code` skill directory:

```bash
python scripts/gpq.py file src/app-logic/TopologyGeometryType.h
python scripts/gpq.py def GPlatesAppLogic::TopologyGeometry::Type --body
python scripts/gpq.py uses Type --kind enum
```
