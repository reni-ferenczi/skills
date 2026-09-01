# TopologyGeometryType

[Book TOC](../../TOC.md) · [app-logic](../../components/app-logic.md) · cluster Community 2 · tier 2

| Source file | Kind | Lines |
|---|---|---|
| `src/app-logic/TopologyGeometryType.h` | C++ | 56 |

## Overview

[[[PROSE overview unit=app-logic/TopologyGeometryType tier=2]]]
Replace this whole block, markers included, with 1-3 paragraphs: what this unit is, why it exists, and how it fits the surrounding design. Do not restate the tables below.
[[[/PROSE]]]

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

[[[PROSE notes unit=app-logic/TopologyGeometryType tier=2]]]
Replace this whole block, markers included, with invariants, ownership, threading or gotchas that are not visible in the tables. Write *None.* if there is nothing worth saying.
[[[/PROSE]]]

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
