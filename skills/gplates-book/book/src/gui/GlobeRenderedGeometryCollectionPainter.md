# GlobeRenderedGeometryCollectionPainter

[Book TOC](../../TOC.md) · [gui](../../components/gui.md) · cluster Community 813 · tier 2

| Source file | Kind | Lines |
|---|---|---|
| `src/gui/GlobeRenderedGeometryCollectionPainter.h` | C++ | 237 |
| `src/gui/GlobeRenderedGeometryCollectionPainter.cc` | C++ | 314 |

## Overview

`GlobeRenderedGeometryCollectionPainter` walks a `RenderedGeometryCollection`
via the `ConstRenderedGeometryCollectionVisitor` double-dispatch interface and
draws each active, non-empty `RenderedGeometryLayer` onto the globe with a
per-layer `GlobeRenderedGeometryLayerPainter`, accumulating the results
through a shared `LayerPainter`. It is used from `Globe` in two passes:
`paint_surface()` for geometries on the sphere's surface, and
`paint_sub_surface()` for geometries below it (currently 3D scalar fields),
which needs a `surface_occlusion_texture` of the already-rendered front
surface to occlude sub-surface detail correctly and can be told to reduce
quality while the globe is being dragged. `get_custom_child_layers_order()`
overrides the default child-layer traversal for `RECONSTRUCTION_LAYER`,
substituting the user-configured order from `VisualLayers::get_layer_order()`
(optionally reversed via `set_visual_layers_reversed()`) in place of the
collection's own layer sequence, since visual layer stacking order is a
user-visible drawing-order preference rather than a property of the
underlying data.

The anonymous-namespace helper `HasRenderableSubSurfaceLayers` is a second,
throwaway visitor used only to answer
`has_renderable_sub_surface_geometries()`: it stops early if it finds any
`RenderedResolvedScalarField3D`, since sub-surface rendering may be
unavailable if the runtime GPU lacks OpenGL 3 support.

## Declared types

| Name | Kind | Bases | Template | Subclasses | Description |
|---|---|---|---|---|---|
| [`GPlatesGui::(anonymous)::HasRenderableSubSurfaceLayers`](#gplatesguianonymoushasrenderablesubsurfacelayers) | class | [`GPlatesViewOperations::ConstRenderedGeometryCollectionVisitor<>`](../view-operations/RenderedGeometryCollectionVisitor.md) | — | 0 | Visits a RenderedGeometryCollection and determines if any of its rendered layers contain sub-surface geometries that can be rendered. |
| [`GPlatesGui::GlobeRenderedGeometryCollectionPainter`](#gplatesguigloberenderedgeometrycollectionpainter) | class | [`GPlatesViewOperations::ConstRenderedGeometryCollectionVisitor< GPlatesPresentation::VisualLayers::rendered_geometry_layer_seq_type>`](../view-operations/RenderedGeometryCollectionVisitor.md)<br>`boost::noncopyable` | — | 0 | Draws rendered geometries (in a RenderedGeometryCollection) onto a 3D orthographic view of the globe using OpenGL. |

## Members

### `GPlatesGui::(anonymous)::HasRenderableSubSurfaceLayers`

| Member | Kind | Type | Access | Description |
|---|---|---|---|---|
| `HasRenderableSubSurfaceLayers( GPlatesOpenGL::GLRenderer &renderer)` | constructor | `None` | public | — |
| `has_renderable_sub_surface_layers()` | method | `bool` | public | — |
| `visit_rendered_geometry_layer( const GPlatesViewOperations::RenderedGeometryLayer &rendered_geometry_layer)` | method | `bool` | public | — |
| `visit_rendered_resolved_scalar_field_3d( const GPlatesViewOperations::RenderedResolvedScalarField3D &rrsf)` | method | `void` | public | — |
| `d_renderer` | field | `GPlatesOpenGL::GLRenderer` | private | — |
| `d_has_renderable_sub_surface_layers` | field | `bool` | private | — |

### `GPlatesGui::GlobeRenderedGeometryCollectionPainter`

| Member | Kind | Type | Access | Description |
|---|---|---|---|---|
| `cache_handle_type` | typedef | `boost::shared_ptr<void>` | public | Typedef for an opaque object that caches a particular painting. |
| `GlobeRenderedGeometryCollectionPainter( const GPlatesViewOperations::RenderedGeometryCollection &rendered_geometry_collection, const GPlatesOpenGL::GLVisualLayers::non_null_ptr_type &gl_visual_layers, const GPlatesPresentation::VisualLayers &visual_layers, const GlobeVisibilityTester &visibility_tester, ColourScheme::n ...` | constructor | `None` | public | — |
| `initialise( GPlatesOpenGL::GLRenderer &renderer)` | method | `void` | public | Initialise objects requiring GLRenderer. |
| `has_renderable_sub_surface_geometries( GPlatesOpenGL::GLRenderer &renderer)` | method | `bool` | public | Returns true if any rendered layer has sub-surface geometries that can be rendered. |
| `paint_surface( GPlatesOpenGL::GLRenderer &renderer, const double &viewport_zoom_factor, const double &device_independent_pixel_to_world_space_ratio, boost::optional<Colour> vector_geometries_override_colour = boost::none)` | method | `cache_handle_type` | public | Draw the rendered geometries on the surface of the globe. |
| `paint_sub_surface( GPlatesOpenGL::GLRenderer &renderer, const double &viewport_zoom_factor, const double &device_independent_pixel_to_world_space_ratio, boost::optional<GPlatesOpenGL::GLTexture::shared_ptr_to_const_type> surface_occlusion_texture, bool improve_performance_reduce_quality_hint = false)` | method | `cache_handle_type` | public | Draw globe sub-surface rendered geometries that exist below the surface of the globe. |
| `set_scale( float scale)` | method | `void` | public | — |
| `get_custom_child_layers_order( GPlatesViewOperations::RenderedGeometryCollection::MainLayerType parent_layer)` | method | `boost::optional<GPlatesPresentation::VisualLayers::rendered_geometry_layer_seq_type>` | public | — |
| `set_visual_layers_reversed( bool reversed)` | method | `void` | public | — |
| `visit_main_rendered_layer( const GPlatesViewOperations::RenderedGeometryCollection &rendered_geometry_collection, GPlatesViewOperations::RenderedGeometryCollection::MainLayerType main_rendered_layer_type)` | method | `bool` | private | — |
| `visit_rendered_geometry_layer( const GPlatesViewOperations::RenderedGeometryLayer &rendered_geometry_layer)` | method | `bool` | private | — |
| `base_type` | typedef | `GPlatesViewOperations::ConstRenderedGeometryCollectionVisitor< GPlatesPresentation::VisualLayers::rendered_geometry_layer_seq_type>` | private | Typedef for the base class. |
| `PaintParams` | struct | `None` | private | Parameters that are only available when paint\_surface or paint\_sub\_surface is called. |
| `d_paint_params` | field | `boost::optional<PaintParams>` | private | Parameters that are only available when paint\_surface or paint\_sub\_surface is called. |
| `d_rendered_geometry_collection` | field | `GPlatesViewOperations::RenderedGeometryCollection` | private | — |
| `d_gl_visual_layers` | field | `GPlatesOpenGL::GLVisualLayers::non_null_ptr_type` | private | Keeps track of OpenGL-related objects that persist from one render to the next. |
| `d_visual_layers` | field | `GPlatesPresentation::VisualLayers` | private | — |
| `d_layer_painter` | field | `LayerPainter` | private | Used to paint the layers. |
| `d_visibility_tester` | field | `GlobeVisibilityTester` | private | Used for determining whether a particular point on the globe is visible |
| `d_colour_scheme` | field | `ColourScheme::non_null_ptr_type` | private | For assigning colours to RenderedGeometry |
| `d_scale` | field | `float` | private | When rendering globes that are meant to be a scale copy of another |
| `d_visual_layers_reversed` | field | `bool` | private | If true, renders child layers in the RECONSTRUCTION\_LAYER in reverse order. |

## Free functions and macros

| Name | Kind | Type / body | Description |
|---|---|---|---|
| `GPLATES_GUI_GLOBERENDEREDGEOMETRYPAINTER_H` | macro | `None` | — |

## Notes

`d_paint_params` is only populated for the duration of a single
`paint_surface()`/`paint_sub_surface()` call and reset to `boost::none`
immediately afterwards; visitor callbacks (`visit_main_rendered_layer`,
`visit_rendered_geometry_layer`) dereference it unconditionally, so they must
never be invoked outside of a paint call.

## Used by

| Unit | Component | References |
|---|---|---|
| [gui/Globe](Globe.md) | gui | 9 |

## Related

*None.*

## Explore

Run these from the `gplates-code` skill directory:

```bash
python scripts/gpq.py file src/gui/GlobeRenderedGeometryCollectionPainter.h
python scripts/gpq.py def GPlatesGui::GlobeRenderedGeometryCollectionPainter --body
python scripts/gpq.py uses GlobeRenderedGeometryCollectionPainter --kind class
python scripts/gpq.py hier GlobeRenderedGeometryCollectionPainter
```
