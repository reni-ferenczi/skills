# Globe

[Book TOC](../../TOC.md) · [gui](../../components/gui.md) · cluster Community 643 · tier 2

| Source file | Kind | Lines |
|---|---|---|
| `src/gui/Globe.h` | C++ | 268 |
| `src/gui/Globe.cc` | C++ | 588 |

## Overview

`GPlatesGui::Globe` draws the 3D globe view: the star field, the opaque earth
sphere, the lat/lon `SphericalGrid`, and every visible `RenderedGeometry` on
top, delegating the last of these to a `GlobeRenderedGeometryCollectionPainter`
it owns. `paint()` takes four projection matrices differing only in far-clip
distance — one each for the front hemisphere, the rear hemisphere, the full
globe, and a long one for the stars — because the front and rear halves of the
globe are rendered as separate passes to get correct depth ordering against
sub-surface geometry.

The globe's current attitude is held in a `SimpleGlobeOrientation`, mutated
through `set_new_handle_pos()`/`update_handle_pos()` as the user drags, and
`orient()` maps a screen-space point back through that orientation onto the
sphere. `d_stars`, `d_sphere` and `d_grid` are `boost::optional` because they
own OpenGL resources that cannot be constructed before `initialiseGL()` runs
against a bound context; the second constructor clones an existing `Globe`
into a new OpenGL context (sharing orientation and geometry state) rather than
rebuilding it from scratch, which is how the globe and map canvases stay in
sync when a view is duplicated.

## Declared types

| Name | Kind | Bases | Template | Subclasses | Description |
|---|---|---|---|---|---|
| [`GPlatesGui::Globe`](#gplatesguiglobe) | class | — | — | 0 | — |

## Members

### `GPlatesGui::Globe`

| Member | Kind | Type | Access | Description |
|---|---|---|---|---|
| `cache_handle_type` | typedef | `boost::shared_ptr<void>` | public | Typedef for an opaque object that caches a particular painting. |
| `Globe( GPlatesPresentation::ViewState &view_state, const GPlatesOpenGL::GLVisualLayers::non_null_ptr_type &gl_visual_layers, GPlatesViewOperations::RenderedGeometryCollection &rendered_geom_collection, const GPlatesPresentation::VisualLayers &visual_layers, const GlobeVisibilityTester &visibility_tester, ColourScheme:: ...` | constructor | `None` | public | — |
| `Globe( Globe &existing_globe, const GPlatesOpenGL::GLVisualLayers::non_null_ptr_type &gl_visual_layers, const GlobeVisibilityTester &visibility_tester, ColourScheme::non_null_ptr_type colour_scheme, int device_pixel_ratio)` | constructor | `None` | public | To clone a Globe |
| `~Globe()` | destructor | `None` | public | — |
| `initialiseGL( GPlatesOpenGL::GLRenderer &renderer)` | method | `void` | public | Initialise any OpenGL state. |
| `set_new_handle_pos( const GPlatesMaths::PointOnSphere &pos)` | method | `void` | public | — |
| `update_handle_pos( const GPlatesMaths::PointOnSphere &pos, bool in_mouse_drag = false)` | method | `void` | public | in\_mouse\_drag should be set to true when the mouse button (left) is pressed (down) and the mouse is moving and if it is set to true then it should subsequently be set back to false when the mouse button (left) is released (up). |
| `orient( const GPlatesMaths::PointOnSphere &pos)` | method | `GPlatesMaths::PointOnSphere` | public | — |
| `paint( GPlatesOpenGL::GLRenderer &renderer, const double &viewport_zoom_factor, const double &device_independent_pixel_to_world_space_ratio, float scale, const GPlatesOpenGL::GLMatrix &projection_transform_include_front_half_globe, const GPlatesOpenGL::GLMatrix &projection_transform_include_rear_half_globe, const GPlat ...` | method | `cache_handle_type` | public | Paint the globe and all the visible features and rasters on it. |
| `d_view_state` | field | `GPlatesPresentation::ViewState` | private | — |
| `d_gl_visual_layers` | field | `GPlatesOpenGL::GLVisualLayers::non_null_ptr_type` | private | Keeps track of OpenGL-related objects that persist from one render to the next. |
| `d_rendered_geom_collection` | field | `GPlatesViewOperations::RenderedGeometryCollection` | private | The collection of RenderedGeometry objects we need to paint. |
| `d_visual_layers` | field | `GPlatesPresentation::VisualLayers` | private | — |
| `d_stars` | field | `boost::optional<Stars>` | private | Stars in the background, behind the Earth. |
| `d_sphere` | field | `boost::optional<OpaqueSphere>` | private | The solid earth. |
| `d_grid` | field | `boost::optional<SphericalGrid>` | private | Lines of lat and lon on surface of earth. |
| `d_globe_orientation_ptr` | field | `boost::shared_ptr<SimpleGlobeOrientation>` | private | The accumulated orientation of the globe. |
| `d_globe_orientation_changing_during_mouse_drag` | field | `bool` | private | Is true when the mouse button (left) is pressed (down) and mouse is moving. |
| `d_rendered_geom_collection_painter` | field | `GlobeRenderedGeometryCollectionPainter` | private | Painter used to draw RenderedGeometry objects on the globe. |
| `d_device_pixel_ratio` | field | `int` | private | Multiplier for point sizes and line widths (due to a device \*independent\* pixel containing multiple device pixels). |
| `get_globe_orientation_transform( GPlatesOpenGL::GLMatrix &transform)` | method | `void` | private | Calculate tranform to ransform the view according to the current globe orientation. |
| `set_scene_lighting( GPlatesOpenGL::GLRenderer &renderer, const GPlatesOpenGL::GLMatrix &view_orientation)` | method | `void` | private | — |
| `render_stars( GPlatesOpenGL::GLRenderer &renderer, const GPlatesOpenGL::GLMatrix &projection_transform_include_stars)` | method | `void` | private | — |
| `render_sphere_background( GPlatesOpenGL::GLRenderer &renderer, const GPlatesOpenGL::GLMatrix &projection_transform_include_full_globe)` | method | `void` | private | — |
| `render_globe_hemisphere_surface( GPlatesOpenGL::GLRenderer &renderer, std::vector<cache_handle_type> &cache_handle, const double &viewport_zoom_factor, const double &device_independent_pixel_to_world_space_ratio, const GPlatesOpenGL::GLMatrix &projection_transform, bool is_front_half_globe)` | method | `void` | private | — |
| `render_front_globe_hemisphere_surface_texture( GPlatesOpenGL::GLRenderer &renderer, const GPlatesOpenGL::GLTexture::shared_ptr_to_const_type &front_globe_surface_texture)` | method | `void` | private | — |
| `render_globe_sub_surface( GPlatesOpenGL::GLRenderer &renderer, std::vector<cache_handle_type> &cache_handle, const double &viewport_zoom_factor, const double &device_independent_pixel_to_world_space_ratio, const GPlatesOpenGL::GLMatrix &projection_transform_include_full_globe, boost::optional<GPlatesOpenGL::GLTexture:: ...` | method | `void` | private | — |

## Free functions and macros

| Name | Kind | Type / body | Description |
|---|---|---|---|
| `STARS_COLOUR` | variable | `GPlatesGui::Colour` | — |
| `GPLATES_GUI_GLOBE_H` | macro | `None` | — |

## Notes

`paint()` can temporarily overwrite the view's background colour: if any
sub-surface geometry needs rendering and the background is currently opaque,
it forces the background alpha to 0.3 (via `ViewState::set_background_colour()`)
so the rear of the globe reads as translucent, leaving that changed colour in
place afterwards rather than restoring the original. `d_globe_orientation_changing_during_mouse_drag`
is read elsewhere to temporarily reduce the sampling rate of 3D scalar-field
iso-surfaces while the user is actively dragging the globe.

## Used by

| Unit | Component | References |
|---|---|---|
| [qt-widgets/GlobeCanvas](../qt-widgets/GlobeCanvas.md) | qt-widgets | 137 |
| [qt-widgets/GlobeAndMapWidget](../qt-widgets/GlobeAndMapWidget.md) | qt-widgets | 20 |
| [gui/VelocityLegendOverlay](VelocityLegendOverlay.md) | gui | 18 |
| [gui/GlobeCanvasTool](GlobeCanvasTool.md) | gui | 9 |
| [gui/TopologyTools](TopologyTools.md) | gui | 9 |
| [qt-widgets/LightingWidget](../qt-widgets/LightingWidget.md) | qt-widgets | 9 |
| [gui/HellingerCanvasToolWorkflow](HellingerCanvasToolWorkflow.md) | gui | 7 |
| [gui/SmallCircleCanvasToolWorkflow](SmallCircleCanvasToolWorkflow.md) | gui | 5 |
| [qt-widgets/DrawStyleDialog](../qt-widgets/DrawStyleDialog.md) | qt-widgets | 4 |
| [canvas-tools/MovePoleGlobe](../canvas-tools/MovePoleGlobe.md) | canvas-tools | 3 |
| [gui/ViewCanvasToolWorkflow](ViewCanvasToolWorkflow.md) | gui | 3 |
| [gui/deprecated/GLCanvas](deprecated/GLCanvas.md) | gui | 3 |
| [qt-widgets/ViewportWindow](../qt-widgets/ViewportWindow.md) | qt-widgets | 3 |
| [canvas-tools/ChangeLightDirectionGlobe](../canvas-tools/ChangeLightDirectionGlobe.md) | canvas-tools | 2 |
| [canvas-tools/ZoomGlobe](../canvas-tools/ZoomGlobe.md) | canvas-tools | 2 |
| [gui/GlobeVisibilityTester](GlobeVisibilityTester.md) | gui | 1 |
| [qt-widgets/ReconstructionViewWidget](../qt-widgets/ReconstructionViewWidget.md) | qt-widgets | 1 |

## Related

*None.*

## Explore

Run these from the `gplates-code` skill directory:

```bash
python scripts/gpq.py file src/gui/Globe.h
python scripts/gpq.py def GPlatesGui::Globe --body
python scripts/gpq.py uses Globe --kind class
python scripts/gpq.py hier Globe
```
