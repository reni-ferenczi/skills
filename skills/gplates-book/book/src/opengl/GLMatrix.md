# GLMatrix

[Book TOC](../../TOC.md) · [opengl](../../components/opengl.md) · cluster Community 1508 · tier 1

| Source file | Kind | Lines |
|---|---|---|
| `src/opengl/GLMatrix.h` | C++ | 303 |
| `src/opengl/GLMatrix.cc` | C++ | 477 |

## Overview

A plain 4x4 double-precision matrix value in OpenGL's column-major layout, and
the only matrix type GPlates has. The header states the policy that explains its
scope: the rest of GPlates does its transformation maths with quaternions
(`GPlatesMaths::UnitQuaternion3D`, and `FiniteRotation` above it) and converts to
matrix form only at the OpenGL boundary. `GLMatrix` *is* that boundary, so
everything it computes is view- or projection-related — camera placement, globe
orientation, cube-face subdivision frusta, texture coordinate generation — never
plate reconstruction. The header also records the intended refactor: move the
arithmetic into a row-major `GPlatesMaths` class and leave `GLMatrix` as a
wrapper.

The method names mirror the fixed-function GL and GLU entry points, and they
behave the same way: everything except `gl_load_*` post-multiplies, matching
OpenGL's convention, which for column-major storage is the same operation as
pre-multiplying a row-major matrix. But nothing here calls OpenGL. The whole
class is CPU arithmetic on a member array, which is what lets `GLState` and
`GLStateSets` keep the modelview, projection and per-texture-unit matrices as
shadow state: `GLLoadMatrixStateSet::apply_state` compares the incoming
`GLMatrix` against the last applied one and issues `glLoadMatrixd` only when they
differ. `GLProjectionUtils` (project/unproject and pixel-size estimation),
`GLProgramObject` (matrix uniforms) and the culling code in `GLCubeSubdivision`
and `GLMultiResolutionCubeRaster` consume the same values. Every mutator returns
`*this`, so the call sites read as a chained transform build-up.

## Declared types

| Name | Kind | Bases | Template | Subclasses | Description |
|---|---|---|---|---|---|
| [`GPlatesOpenGL::GLMatrix`](#gplatesopenglglmatrix) | class | `boost::equality_comparable<GLMatrix>` | — | 0 | A 4x4 matrix in OpenGL column-major format. |

## Members

### `GPlatesOpenGL::GLMatrix`

| Member | Kind | Type | Access | Description |
|---|---|---|---|---|
| `IDENTITY` | field | `GLMatrix` | public | The identity matrix. |
| `GLMatrix()` | constructor | `None` | public | Constructor - creates identity matrix. |
| `GLMatrix( const GLdouble *matrix)` | constructor | `None` | public | Constructs an arbitrary 4x4 matrix. |
| `GLMatrix( const GPlatesMaths::UnitQuaternion3D &quaternion)` | constructor | `None` | public | Constructs 4x4 matrix from specified unit quaternion (note only the 3x3 rotation part of the matrix is initialised - the rest is set to zero). |
| `gl_load_identity` | field | `GLMatrix` | public | Performs function of similarly named OpenGL function. |
| `gl_load_matrix` | field | `GLMatrix` | public | Loads an arbitrary 4x4 matrix. |
| `gl_mult_matrix` | field | `GLMatrix` | public | Post-multiplies matrix matrix with the current internal matrix. |
| `gl_translate` | field | `GLMatrix` | public | Performs function of similarly named OpenGL function (including post-multiplication). |
| `gl_rotate` | field | `GLMatrix` | public | Performs function of similarly named OpenGL function (including post-multiplication). |
| `gl_scale` | field | `GLMatrix` | public | Performs function of similarly named OpenGL function (including post-multiplication). |
| `gl_ortho` | field | `GLMatrix` | public | Performs function of similarly named OpenGL function (including post-multiplication). |
| `gl_frustum` | field | `GLMatrix` | public | Performs function of similarly named OpenGL function (including post-multiplication). |
| `glu_look_at` | field | `GLMatrix` | public | Performs function of similarly named OpenGL function (including post-multiplication). |
| `glu_perspective` | field | `GLMatrix` | public | Performs function of similarly named OpenGL function (including post-multiplication). |
| `get_matrix()` | method | `GLdouble` | public | Returns internal matrix in OpenGL column-major format. |
| `matrix_type` | typedef | `GLdouble` | private | Typedef for a contiguous array of 16 doubles (in 4x4 format). |
| `d_matrix` | field | `matrix_type` | private | — |

## Free functions and macros

| Name | Kind | Type / body | Description |
|---|---|---|---|
| `IDENTITY` | variable | `GPlatesOpenGL::GLMatrix` | — |
| `GPLATES_OPENGL_GLMATRIX_H` | macro | `None` | — |

## Notes

- **`gl_rotate` does not actually normalise its axis.** It computes
  `mag_xyz = x*x + y*y + z*z` — the *squared* magnitude, no `sqrt` — and then
  scales by `1.0 / mag_xyz`. The result is only correct for an axis that is
  already unit length. Every current call site (`Globe`, `OpaqueSphere`,
  `SphericalGrid`) passes the components of a `GPlatesMaths::UnitVector3D` or a
  literal axis, so the defect is masked; passing an arbitrary vector will
  silently produce a wrong rotation. The zero-axis guard compares that squared
  magnitude against `1e-12` and warns under the class's former name,
  `GLTransform::gl_rotate`.
- **Equality is epsilon-based, and that is load-bearing.** `operator==` compares
  all 16 elements with `GPlatesMaths::are_almost_exactly_equal`, i.e. within
  `GPlatesMaths::EPSILON`, not bitwise. Because `GLLoadMatrixStateSet` and
  `GLLoadTextureMatrixStateSet` use that comparison to decide whether to skip a
  `glLoadMatrixd`, two matrices differing by less than epsilon per element are
  the same GL state as far as the renderer is concerned.
- **`get_element(row, column)` reverses its arguments internally**
  (`d_matrix[column][row]`), and `get_matrix()` hands out a raw pointer into the
  member array in column-major order. The non-const overload lets a caller write
  through it, which is how the implementation-facing users fill a matrix in
  place.
- **Storage is `GLdouble`.** Anything feeding a shader has to narrow to float
  itself; `GLMatrix` never does.
- The quaternion constructor's Doxygen says only the 3x3 rotation part is
  initialised and the rest zeroed, but the code also sets `m[3][3] = 1.0`, so it
  produces a complete affine rotation matrix that can be fed straight to
  `gl_mult_matrix`.
- `gl_mult_matrix` accumulates into a local and copies back, so
  `m.gl_mult_matrix(m)` is safe.
- `IDENTITY` is a namespace-scope object with a dynamically-run constructor, so
  it is subject to static initialisation order across translation units.

## Used by

| Unit | Component | References |
|---|---|---|
| [qt-widgets/GlobeCanvas](../qt-widgets/GlobeCanvas.md) | qt-widgets | 55 |
| [qt-widgets/MapCanvas](../qt-widgets/MapCanvas.md) | qt-widgets | 37 |
| [gui/Globe](../gui/Globe.md) | gui | 34 |
| [opengl/GLMultiResolutionStaticPolygonReconstructedRaster](GLMultiResolutionStaticPolygonReconstructedRaster.md) | opengl | 30 |
| [opengl/GLRenderer](GLRenderer.md) | opengl | 30 |
| [opengl/GLUtils](GLUtils.md) | opengl | 30 |
| [opengl/GLStateSets](GLStateSets.md) | opengl | 29 |
| [opengl/GLProjectionUtils](GLProjectionUtils.md) | opengl | 23 |
| [opengl/GLFilledPolygonsGlobeView](GLFilledPolygonsGlobeView.md) | opengl | 21 |
| [opengl/GLLight](GLLight.md) | opengl | 15 |
| [opengl/GLMultiResolutionCubeRaster](GLMultiResolutionCubeRaster.md) | opengl | 14 |
| [opengl/GLProgramObject](GLProgramObject.md) | opengl | 14 |
| [gui/SceneLightingParameters](../gui/SceneLightingParameters.md) | gui | 13 |
| [gui/LayerPainter](../gui/LayerPainter.md) | gui | 12 |
| [opengl/GLScalarField3DGenerator](GLScalarField3DGenerator.md) | opengl | 12 |
| [opengl/GLMultiResolutionRasterMapView](GLMultiResolutionRasterMapView.md) | opengl | 11 |
| [gui/ExportRasterAnimationStrategy](../gui/ExportRasterAnimationStrategy.md) | gui | 10 |
| [gui/OpaqueSphere](../gui/OpaqueSphere.md) | gui | 10 |
| [opengl/GLRasterCoRegistration](GLRasterCoRegistration.md) | opengl | 10 |
| [opengl/GLCubeSubdivision](GLCubeSubdivision.md) | opengl | 8 |

*... and 22 more units.*

## Related

*None.*

## Explore

Run these from the `gplates-code` skill directory:

```bash
python scripts/gpq.py file src/opengl/GLMatrix.h
python scripts/gpq.py def GPlatesOpenGL::GLMatrix --body
python scripts/gpq.py uses GLMatrix --kind class
python scripts/gpq.py hier GLMatrix
```
