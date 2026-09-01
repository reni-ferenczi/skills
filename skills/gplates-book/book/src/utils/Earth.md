# Earth

[Book TOC](../../TOC.md) · [utils](../../components/utils.md) · cluster Community 1729 · tier 2

| Source file | Kind | Lines |
|---|---|---|
| `src/utils/Earth.h` | C++ | 54 |
| `src/utils/Earth.cc` | C++ | 31 |

## Overview

[[[PROSE overview unit=utils/Earth tier=2]]]
Replace this whole block, markers included, with 1-3 paragraphs: what this unit is, why it exists, and how it fits the surrounding design. Do not restate the tables below.
[[[/PROSE]]]

## Declared types

| Name | Kind | Bases | Template | Subclasses | Description |
|---|---|---|---|---|---|
| [`GPlatesUtils::Earth`](#gplatesutilsearth) | class | — | — | 0 | Various Earth-related parameters. |

## Members

### `GPlatesUtils::Earth`

| Member | Kind | Type | Access | Description |
|---|---|---|---|---|
| `EQUATORIAL_RADIUS_KMS` | field | `double` | public | Equatorial radius (in kms) - in WGS-84 coordinate system. |
| `POLAR_RADIUS_KMS` | field | `double` | public | Polar radius (in kms) - in WGS-84 coordinate system. |
| `MEAN_RADIUS_KMS` | field | `double` | public | Mean radius (in kms) - in WGS-84 coordinate system. |

## Free functions and macros

| Name | Kind | Type / body | Description |
|---|---|---|---|
| `EQUATORIAL_RADIUS_KMS` | variable | `double` | — |
| `POLAR_RADIUS_KMS` | variable | `double` | — |
| `MEAN_RADIUS_KMS` | variable | `double` | — |
| `GPLATES_UTILS_EARTH_H` | macro | `None` | — |

## Notes

[[[PROSE notes unit=utils/Earth tier=2]]]
Replace this whole block, markers included, with invariants, ownership, threading or gotchas that are not visible in the tables. Write *None.* if there is nothing worth saying.
[[[/PROSE]]]

## Used by

| Unit | Component | References |
|---|---|---|
| [data-mining/DataMiningUtils](../data-mining/DataMiningUtils.md) | data-mining | 7 |
| [maths/CalculateVelocity](../maths/CalculateVelocity.md) | maths | 7 |
| [app-logic/ResolvedTriangulationDelaunay2](../app-logic/ResolvedTriangulationDelaunay2.md) | app-logic | 4 |
| [canvas-tools/MeasureDistanceState](../canvas-tools/MeasureDistanceState.md) | canvas-tools | 4 |
| [app-logic/ResolvedTriangulationNetwork](../app-logic/ResolvedTriangulationNetwork.md) | app-logic | 3 |
| [data-mining/DataSelector](../data-mining/DataSelector.md) | data-mining | 3 |
| [data-mining/RegionOfInterestFilter](../data-mining/RegionOfInterestFilter.md) | data-mining | 3 |
| [maths/PolygonMesh](../maths/PolygonMesh.md) | maths | 3 |
| [qt-widgets/ImportScalarField3DDialog](../qt-widgets/ImportScalarField3DDialog.md) | qt-widgets | 3 |
| [app-logic/TopologyReconstruct](../app-logic/TopologyReconstruct.md) | app-logic | 2 |

## Related

*None.*

## Explore

Run these from the `gplates-code` skill directory:

```bash
python scripts/gpq.py file src/utils/Earth.h
python scripts/gpq.py def GPlatesUtils::Earth --body
python scripts/gpq.py uses Earth --kind class
python scripts/gpq.py hier Earth
```
