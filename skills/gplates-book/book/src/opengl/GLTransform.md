# GLTransform

[Book TOC](../../TOC.md) · [opengl](../../components/opengl.md) · cluster Community 1131 · tier 2

| Source file | Kind | Lines |
|---|---|---|
| `src/opengl/GLTransform.h` | C++ | 171 |

## Overview

`GLTransform` is a thin, reference-counted wrapper around a `GLMatrix`,
giving a 4x4 transform (model-view, projection, or a tile/cube-face
adjustment on top of one) a shared-pointer identity that can be passed around
and cached without copying the underlying matrix. It can be built as an
identity matrix, from an existing `GLMatrix`, from a raw column-major
`GLdouble[16]` array, or from a `GPlatesMaths::UnitQuaternion3D` (which fills
in only the 3x3 rotation submatrix, leaving the rest zeroed) — the last of
these is how a plate rotation becomes an OpenGL transform. Because
`ReferenceCount` makes the class non-copy-constructible, `clone()` is the
supported way to get an independent copy.

## Declared types

| Name | Kind | Bases | Template | Subclasses | Description |
|---|---|---|---|---|---|
| [`GPlatesOpenGL::GLTransform`](#gplatesopenglgltransform) | class | [`GPlatesUtils::ReferenceCount<GLTransform>`](../utils/ReferenceCount.md) | — | 0 | Simply contains a 4x4 matrix allocated on the heap and managed by reference-counted shared pointers. |

## Members

### `GPlatesOpenGL::GLTransform`

| Member | Kind | Type | Access | Description |
|---|---|---|---|---|
| `non_null_ptr_type` | typedef | `GPlatesUtils::non_null_intrusive_ptr<GLTransform>` | public | A convenience typedef for a shared pointer to a non-const GLTransform. |
| `non_null_ptr_to_const_type` | typedef | `GPlatesUtils::non_null_intrusive_ptr<const GLTransform>` | public | A convenience typedef for a shared pointer to a const GLTransform. |
| `create()` | method | `non_null_ptr_type` | public | Constructs identity matrix. |
| `create( const GLMatrix &matrix)` | method | `non_null_ptr_type` | public | Constructs arbitrary matrix. |
| `create( const GLdouble *matrix)` | method | `non_null_ptr_type` | public | Constructs arbitrary matrix. |
| `create( const GPlatesMaths::UnitQuaternion3D &quaternion)` | method | `non_null_ptr_type` | public | Constructs 4x4 matrix from specified unit quaternion (note only the 3x3 rotation part of the matrix is initialised - the rest is set to zero). |
| `clone()` | method | `non_null_ptr_type` | public | Returns a clone of 'this' transform. |
| `d_matrix` | field | `GLMatrix` | private | — |
| `GLTransform()` | constructor | `None` | private | Default constructor. |
| `GLTransform( const GLMatrix &matrix)` | constructor | `None` | private | Constructor. |
| `GLTransform( const GLdouble *matrix)` | constructor | `None` | private | Constructor. |
| `GLTransform( const GPlatesMaths::UnitQuaternion3D &quaternion)` | constructor | `None` | private | Constructor. |

## Free functions and macros

| Name | Kind | Type / body | Description |
|---|---|---|---|
| `GPLATES_OPENGL_GLTRANSFORM_H` | macro | `None` | — |

## Notes

- Constructing from a `UnitQuaternion3D` only initialises the 3x3 rotation
  block; the remaining entries (translation column, bottom row, and scale)
  are zero, not identity — treat the result as a pure rotation matrix, not a
  general transform.
- `get_matrix()` returns a mutable reference to the internal `GLMatrix`, so a
  `GLTransform` shared through a `non_null_ptr_type` can be mutated in place
  by any holder; use `non_null_ptr_to_const_type` where that must not happen.

## Used by

| Unit | Component | References |
|---|---|---|
| [opengl/GLRasterCoRegistration](GLRasterCoRegistration.md) | opengl | 27 |
| [opengl/GLTileRender](GLTileRender.md) | opengl | 15 |
| [opengl/GLMultiResolutionCubeRaster](GLMultiResolutionCubeRaster.md) | opengl | 12 |
| [opengl/GLCubeSubdivision](GLCubeSubdivision.md) | opengl | 11 |
| [opengl/GLMultiResolutionRasterMapView](GLMultiResolutionRasterMapView.md) | opengl | 10 |
| [opengl/GLCubeSubdivisionCache](GLCubeSubdivisionCache.md) | opengl | 8 |
| [gui/FeedbackOpenGLToQPainter](../gui/FeedbackOpenGLToQPainter.md) | gui | 7 |
| [opengl/GLFilledPolygonsGlobeView](GLFilledPolygonsGlobeView.md) | opengl | 5 |
| [opengl/GLMultiResolutionCubeReconstructedRaster](GLMultiResolutionCubeReconstructedRaster.md) | opengl | 4 |
| [opengl/GLScalarField3DGenerator](GLScalarField3DGenerator.md) | opengl | 4 |
| [gui/LayerPainter](../gui/LayerPainter.md) | gui | 3 |
| [gui/ExportRasterAnimationStrategy](../gui/ExportRasterAnimationStrategy.md) | gui | 1 |
| [gui/MapBackground](../gui/MapBackground.md) | gui | 1 |
| [gui/OpaqueSphere](../gui/OpaqueSphere.md) | gui | 1 |
| [opengl/GLReconstructedStaticPolygonMeshes](GLReconstructedStaticPolygonMeshes.md) | opengl | 1 |
| [qt-widgets/GlobeCanvas](../qt-widgets/GlobeCanvas.md) | qt-widgets | 1 |
| [qt-widgets/MapCanvas](../qt-widgets/MapCanvas.md) | qt-widgets | 1 |

## Related

*None.*

## Explore

Run these from the `gplates-code` skill directory:

```bash
python scripts/gpq.py file src/opengl/GLTransform.h
python scripts/gpq.py def GPlatesOpenGL::GLTransform --body
python scripts/gpq.py uses GLTransform --kind class
python scripts/gpq.py hier GLTransform
```
