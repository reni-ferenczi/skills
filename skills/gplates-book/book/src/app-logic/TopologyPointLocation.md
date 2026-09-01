# TopologyPointLocation

[Book TOC](../../TOC.md) · [app-logic](../../components/app-logic.md) · cluster Community 492 · tier 2

| Source file | Kind | Lines |
|---|---|---|
| `src/app-logic/TopologyPointLocation.h` | C++ | 269 |

## Overview

`TopologyPointLocation` records where a single point sits relative to resolved topologies at one instant: outside everything, inside a `ResolvedTopologicalBoundary`, or inside a `ResolvedTopologicalNetwork` at a particular delaunay face or rigid block (`network_location_type`). It exists purely to keep this per-point, per-time-slot record small — a `boost::variant` over the four private location structs, reached only through `boost::apply_visitor`, packs into 24 bytes on 64-bit builds versus 40 for the equivalent `boost::optional<boost::variant<...>>` — because `TopologyReconstruct` stores one of these for every point of every geometry at every time slot in a topological reconstruction's history, so the per-point overhead multiplies across the whole reconstructed time span.

## Declared types

| Name | Kind | Bases | Template | Subclasses | Description |
|---|---|---|---|---|---|
| [`GPlatesAppLogic::TopologyPointLocation`](#gplatesapplogictopologypointlocation) | class | — | — | 0 | Optional location of a point in a resolved topological boundary or network. |

## Members

### `GPlatesAppLogic::TopologyPointLocation`

| Member | Kind | Type | Access | Description |
|---|---|---|---|---|
| `network_location_type` | typedef | `std::pair< ResolvedTopologicalNetwork::non_null_ptr_type, ResolvedTriangulation::Network::PointLocation>` | public | Location in a network (delaunay face or rigid block). |
| `TopologyPointLocation()` | constructor | `None` | public | Point is not located inside resolved boundaries/networks (ie, is outside all resolved boundaries/networks). |
| `TopologyPointLocation( const ResolvedTopologicalBoundary::non_null_ptr_type &boundary)` | constructor | `None` | public | Point located inside resolved boundary. |
| `TopologyPointLocation( const ResolvedTopologicalNetwork::non_null_ptr_type &network, const ResolvedTriangulation::Network::PointLocation &network_point_location)` | constructor | `None` | public | Point located inside resolved network. |
| `not_located()` | method | `bool` | public | Returns true if point is not located inside resolved boundaries/networks (ie, is outside all resolved boundaries/networks). |
| `located_in_resolved_boundary()` | method | `boost::optional<ResolvedTopologicalBoundary::non_null_ptr_type>` | public | Returns resolved boundary that point is located in (otherwise returns none). |
| `located_in_resolved_network()` | method | `boost::optional<network_location_type>` | public | Returns resolved network location that point is located in (otherwise returns none). |
| `NoLocation` | struct | `None` | private | — |
| `BoundaryLocation` | struct | `None` | private | — |
| `NetworkDelaunayFaceLocation` | struct | `None` | private | — |
| `NetworkRigidBlockLocation` | struct | `None` | private | — |
| `location_type` | typedef | `boost::variant< NoLocation, BoundaryLocation, NetworkDelaunayFaceLocation, NetworkRigidBlockLocation >` | private | Typedef for location of a point. |
| `ConstructNetworkVisitor` | struct | `None` | private | Construct a 'location\_type' from a 'ResolvedTriangulation::Network::location\_type'. |
| `NoLocationVisitor` | struct | `None` | private | Returns true if point not located in resolved boundaries/networks. |
| `BoundaryLocationVisitor` | struct | `None` | private | Returns resolved boundary that point is located in (otherwise returns none). |
| `NetworkLocationVisitor` | struct | `None` | private | Returns resolved network location that point is located in (otherwise returns none). |
| `d_location` | field | `location_type` | private | The location of the point. |

## Free functions and macros

| Name | Kind | Type / body | Description |
|---|---|---|---|
| `GPLATES_APP_LOGIC_TOPOLOGYPOINTLOCATION_H` | macro | `None` | — |

## Notes

The compact representation is the whole point of this class: changing it to store anything larger than the current 24 bytes defeats the memory optimisation `TopologyReconstruct` relies on when it keeps one location per point per time slot.

## Used by

| Unit | Component | References |
|---|---|---|
| [app-logic/TopologyReconstruct](TopologyReconstruct.md) | app-logic | 52 |
| [app-logic/ReconstructMethodByPlateId](ReconstructMethodByPlateId.md) | app-logic | 7 |
| [app-logic/TopologyReconstructedFeatureGeometry](TopologyReconstructedFeatureGeometry.md) | app-logic | 2 |

## Related

*None.*

## Explore

Run these from the `gplates-code` skill directory:

```bash
python scripts/gpq.py file src/app-logic/TopologyPointLocation.h
python scripts/gpq.py def GPlatesAppLogic::TopologyPointLocation --body
python scripts/gpq.py uses TopologyPointLocation --kind class
python scripts/gpq.py hier TopologyPointLocation
```
