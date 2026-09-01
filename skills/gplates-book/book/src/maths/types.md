# types

[Book TOC](../../TOC.md) · [maths](../../components/maths.md) · cluster Community 5 · tier 1

| Source file | Kind | Lines |
|---|---|---|
| `src/maths/types.h` | C++ | 49 |

## Overview

Two unrelated aliases in a header that contains no code of its own. The one
that matters is `real_t`, the name by which the whole of `GPlatesMaths` refers
to `GPlatesMaths::Real` — the wrapper around `double` whose comparison
operators are tolerant to within `GPlatesMaths::EPSILON` (1.0e-12) rather than
exact. Every scalar stored by a geometry class in this module is a `real_t`:
the components of `Vector3D` and `UnitVector3D`, the scalar part of
`UnitQuaternion3D`, the cosine and sine cached by `AngularExtent`. This header
is the reason those files can write `#include "types.h"  /* real_t */` and pull
in `Real.h` and nothing else; the comment appears verbatim at almost every
include site.

`rot_id_t` is a leftover. Nothing in the tree uses it except
`FiniteRotationSnapshotTable.h`, and its own comment says it was meant to
replace `GPlatesGlobal::rid_t` and to become `std::size_t`. Plate IDs in
current code are `GPlatesModel::integer_plate_id_type`, not this.

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

`real_t` is not a transparent alias for `double`, and treating it as one is the
standard way to get subtly wrong results here. `Real::operator<` is defined as
`r2 - r1 > EPSILON`, and Boost's `equivalent` derives `==` from it, so equality
means "within 1.0e-12 absolute" — which is *not transitive*, and is an absolute
tolerance that does not scale with magnitude. Sorting or using `real_t` as a
map key is therefore unsound. Code that wants plain IEEE semantics calls
`.dval()` explicitly, as the arithmetic in `Vector3D` and `GenericVectorOps3D`
does throughout (their comments record that this also generates markedly better
assembly than operating on `Real`).

Changing this typedef would silently change the comparison semantics of every
geometry class in `maths`, including the invariant checks in `UnitVector3D` and
`UnitQuaternion3D`, which are written as `mag_sqrd != 1.0` and depend on the
tolerance being there.

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
