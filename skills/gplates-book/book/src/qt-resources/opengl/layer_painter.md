# layer_painter

[Book TOC](../../../TOC.md) · [shaders](../../../components/shaders.md) · tier 2

| Source file | Kind | Lines |
|---|---|---|
| `src/qt-resources/opengl/layer_painter/render_axially_symmetric_mesh_lighting_fragment_shader.glsl` | GLSL | 71 |
| `src/qt-resources/opengl/layer_painter/render_axially_symmetric_mesh_lighting_vertex_shader.glsl` | GLSL | 62 |
| `src/qt-resources/opengl/layer_painter/render_point_line_polygon_lighting_fragment_shader.glsl` | GLSL | 59 |
| `src/qt-resources/opengl/layer_painter/render_point_line_polygon_lighting_vertex_shader.glsl` | GLSL | 51 |

## Overview

These two shader pairs give `LayerPainter` a directional-lighting option for the geometry it batches onto the globe and map. The point/line/polygon pair lights ordinary rendered geometry: the vertex shader passes through the interpolated position (used directly as the sphere normal, since geometry sits on the unit globe) and the fragment shader runs a Lambert diffuse term against it, blended with an ambient contribution. Under `MAP_VIEW` this collapses to a single precomputed `ambient_and_diffuse_lighting` uniform, because the map's surface normal is constant across the scene and does not need a per-fragment dot product.

The axially-symmetric-mesh pair lights meshes such as velocity arrows and small-circle discs, which are built by rotating a 2D profile around an axis rather than sitting flush on the sphere. Because the true surface normal is not the sphere normal, the fragment shader reconstructs it by blending a radial (x, y) normal with the mesh's own axial (z) direction, using per-vertex weights, then transforms that model-space normal into world-space with a per-vertex local frame (`world_space_x_axis`/`y_axis`/`z_axis`) carried from the vertex shader. The resulting lambert term is further clamped based on the *unperturbed* sphere normal so that a mesh on the far side of the globe does not appear lit through it.

## Declared types

*None.*

## Members

*None.*

## Free functions and macros

*None.*

## Notes

Both fragment shaders use `clamp`/`max` with float literals rather than integer overloads, because some driver GLSL compilers fail to resolve the integer overload of these built-ins and crash. Both vertex shaders write `gl_FrontColor` and `gl_BackColor` identically since the geometry is drawn without back-face culling.

## Used by

*Nothing in the tree references this unit.*

## Related

**Compiled by**

| Unit | Component |
|---|---|
| [gui/LayerPainter](../../gui/LayerPainter.md) | gui |


## Explore

Run these from the `gplates-code` skill directory:

```bash
python scripts/gpq.py file src/qt-resources/opengl/layer_painter/render_axially_symmetric_mesh_lighting_fragment_shader.glsl
python scripts/gpq.py grep uniform --category shader --path src/qt-resources/opengl/layer_painter
```
