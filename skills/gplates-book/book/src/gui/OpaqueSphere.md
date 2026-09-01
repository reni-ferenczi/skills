# OpaqueSphere

[Book TOC](../../TOC.md) · [gui](../../components/gui.md) · cluster Community 965 · tier 3

| Source file | Kind | Lines |
|---|---|---|
| `src/gui/OpaqueSphere.h` | C++ | 94 |
| `src/gui/OpaqueSphere.cc` | C++ | 410 |

## Overview

Renders the background sphere (globe surface) of the 3D globe view. It renders the sphere as a flat disk on the z=0 plane, which allows proper depth testing to occlude geometries on the far side of the globe while avoiding depth artifacts from geometries clipping through the surface. The rendering can use a fixed color or the background color from `ViewState`. For translucent rendering, varying alpha values from center to edge simulate the appearance of a 3D sphere using integration to calculate per-ring material thickness.

## Declared types

| Name | Kind | Bases | Template | Subclasses | Description |
|---|---|---|---|---|---|
| [`(anonymous)::vertex_type`](#anonymousvertex_type) | typedef | — | — | 0 | — |
| [`(anonymous)::vertex_element_type`](#anonymousvertex_element_type) | typedef | — | — | 0 | — |
| [`(anonymous)::stream_primitives_type`](#anonymousstream_primitives_type) | typedef | — | — | 0 | — |
| [`(anonymous)::double_pair`](#anonymousdouble_pair) | typedef | — | — | 0 | — |
| [`GPlatesGui::OpaqueSphere`](#gplatesguiopaquesphere) | class | `boost::noncopyable` | — | 0 | — |

## Members

### `(anonymous)::vertex_type`

*None.*

### `(anonymous)::vertex_element_type`

*None.*

### `(anonymous)::stream_primitives_type`

*None.*

### `(anonymous)::double_pair`

*None.*

### `GPlatesGui::OpaqueSphere`

| Member | Kind | Type | Access | Description |
|---|---|---|---|---|
| `OpaqueSphere( GPlatesOpenGL::GLRenderer &renderer, const Colour &colour)` | constructor | `None` | public | Constructs an OpaqueSphere with a fixed colour. |
| `OpaqueSphere( GPlatesOpenGL::GLRenderer &renderer, const GPlatesPresentation::ViewState &view_state)` | constructor | `None` | public | Constructs an OpaqueSphere that uses the background colour of view\_state, as it changes from time to time. |
| `paint( GPlatesOpenGL::GLRenderer &renderer, const GPlatesMaths::UnitVector3D &axis, double angle_in_deg)` | method | `void` | public | Paints sphere. |
| `d_view_state` | field | `GPlatesPresentation::ViewState` | private | — |
| `d_colour` | field | `Colour` | private | — |
| `d_vertex_array` | field | `GPlatesOpenGL::GLVertexArray::shared_ptr_type` | private | — |
| `d_compiled_draw_state` | field | `GPlatesOpenGL::GLCompiledDrawState::non_null_ptr_to_const_type` | private | — |

## Free functions and macros

| Name | Kind | Type / body | Description |
|---|---|---|---|
| `RADIUS` | variable | `double` | — |
| `NUM_SLICES` | variable | `unsigned int` | — |
| `compute_sin_cos_angles( unsigned int num_slices)` | function | `std::vector<double_pair>` | Computes the sin and cos of: 2 \* PI \* i / num\_slices for 0 \<= i \<= num\_slices. |
| `stream_disk( stream_primitives_type &stream, double inner_radius, double outer_radius, const std::vector<double_pair> &sin_cos_angles, const GPlatesGui::rgba8_t &inner_colour, const GPlatesGui::rgba8_t &outer_colour)` | function | `void` | Creates a donut-shaped drawable on the z = 0 plane. |
| `eval_integral( double x, double r)` | function | `double` | Evaluates the integral of sqrt(r^2 - x^2) with respect to x for a given value of r and x (ignoring the constant of integration). |
| `stream_translucent_sphere( stream_primitives_type &stream, const GPlatesGui::rgba8_t &colour)` | function | `void` | Draws a disk on the z = 0 plane with varying translucency from centre to edge, that simulates what a real translucent sphere would look like. |
| `stream_opaque_sphere( stream_primitives_type &stream, const GPlatesGui::rgba8_t &colour)` | function | `void` | Draws a disk on the z = 0 plane with a fixed colour. |
| `compile_sphere_draw_state( GPlatesOpenGL::GLRenderer &renderer, GPlatesOpenGL::GLVertexArray &vertex_array, const GPlatesGui::rgba8_t &colour)` | function | `GPlatesOpenGL::GLCompiledDrawState::non_null_ptr_to_const_type` | Creates a compiled draw state that renders the sphere to the screen. |
| `undo_rotation( GPlatesOpenGL::GLMatrix &transform, const GPlatesMaths::UnitVector3D &axis, double angle_in_deg)` | function | `void` | — |
| `GPLATES_GUI_OPAQUESPHERE_H` | macro | `None` | — |

## Notes

The ViewState pointer (when used) is not owned and must remain valid for the lifetime of the OpaqueSphere. The translucent version uses 150 radial steps and 72 angular slices. The disk is rendered with 72 slices around the circumference. The paint() method takes an axis and angle to rotate the sphere before rendering.

## Used by

| Unit | Component | References |
|---|---|---|
| [gui/Globe](Globe.md) | gui | 2 |

## Related

*None.*

## Explore

Run these from the `gplates-code` skill directory:

```bash
python scripts/gpq.py file src/gui/OpaqueSphere.h
python scripts/gpq.py def GPlatesGui::OpaqueSphere --body
python scripts/gpq.py uses OpaqueSphere --kind class
python scripts/gpq.py hier OpaqueSphere
```
