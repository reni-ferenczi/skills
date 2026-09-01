# types

[Book TOC](../../TOC.md) · [maths](../../components/maths.md) · cluster Community 5 · tier 1

| Source file | Kind | Lines |
|---|---|---|
| `src/maths/types.h` | C++ | 49 |

## Overview

[[[PROSE overview unit=maths/types tier=1]]]
Replace this whole block, markers included, with 1-3 paragraphs: what this unit is, why it exists, and how it fits the surrounding design. Do not restate the tables below.
[[[/PROSE]]]

## Declared types

| Name | Kind | Bases | Template | Subclasses | Description |
|---|---|---|---|---|---|
| [`GPlatesMaths::real_t`](#gplatesmathsreal_t) | typedef | — | — | 0 | A floating-point approximation to the field of reals. |
| [`GPlatesMaths::rot_id_t`](#gplatesmathsrot_id_t) | typedef | — | — | 0 | The type used to identify plate rotations. |

## Members

### `GPlatesMaths::real_t`

*None.*

### `GPlatesMaths::rot_id_t`

*None.*

## Free functions and macros

| Name | Kind | Type / body | Description |
|---|---|---|---|
| `GPLATES_MATHS_TYPES_H` | macro | `None` | — |

## Notes

[[[PROSE notes unit=maths/types tier=1]]]
Replace this whole block, markers included, with invariants, ownership, threading or gotchas that are not visible in the tables. Write *None.* if there is nothing worth saying.
[[[/PROSE]]]

## Used by

| Unit | Component | References |
|---|---|---|
| [app-logic/ResolvedTriangulationNetwork](../app-logic/ResolvedTriangulationNetwork.md) | app-logic | 57 |
| [maths/CartesianConvMatrix3D](CartesianConvMatrix3D.md) | maths | 41 |
| [maths/GreatCircleArc](GreatCircleArc.md) | maths | 35 |
| [maths/GeometryInterpolation](GeometryInterpolation.md) | maths | 34 |
| [maths/FiniteRotation](FiniteRotation.md) | maths | 33 |
| [maths/UnitQuaternion3D](UnitQuaternion3D.md) | maths | 32 |
| [gui/deprecated/GLCanvas](../gui/deprecated/GLCanvas.md) | gui | 30 |
| [maths/CalculateVelocity](CalculateVelocity.md) | maths | 29 |
| [maths/PolygonOnSphere](PolygonOnSphere.md) | maths | 29 |
| [maths/UnitVector3D](UnitVector3D.md) | maths | 26 |
| [app-logic/TopologyNetworkParams](../app-logic/TopologyNetworkParams.md) | app-logic | 25 |
| [gui/GlobeRenderedGeometryLayerPainter](../gui/GlobeRenderedGeometryLayerPainter.md) | gui | 25 |
| [maths/AngularExtent](AngularExtent.md) | maths | 25 |
| [maths/SphericalArea](SphericalArea.md) | maths | 22 |
| [app-logic/TopologyGeometryResolverLayerProxy](../app-logic/TopologyGeometryResolverLayerProxy.md) | app-logic | 18 |
| [maths/SmallCircle](SmallCircle.md) | maths | 18 |
| [maths/deprecated/GridOnSphere](deprecated/GridOnSphere.md) | maths | 18 |
| [maths/Vector3D](Vector3D.md) | maths | 17 |
| [opengl/GLMultiResolutionRaster](../opengl/GLMultiResolutionRaster.md) | opengl | 16 |
| [maths/PolylineOnSphere](PolylineOnSphere.md) | maths | 13 |

*... and 77 more units.*

## Related

*None.*

## Explore

Run these from the `gplates-code` skill directory:

```bash
python scripts/gpq.py file src/maths/types.h
python scripts/gpq.py def GPlatesMaths::real_t --body
python scripts/gpq.py uses real_t --kind typedef
```
