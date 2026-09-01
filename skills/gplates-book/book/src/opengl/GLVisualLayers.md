# GLVisualLayers

[Book TOC](../../TOC.md) · [opengl](../../components/opengl.md) · cluster Community 79 · tier 1

| Source file | Kind | Lines |
|---|---|---|
| `src/opengl/GLVisualLayers.h` | C++ | 1005 |
| `src/opengl/GLVisualLayers.cc` | C++ | 1864 |

## Overview

This is the bridge between app-logic layer identity and GPU-resident state, and
the place where the rendering backend keeps everything that must survive from one
frame to the next. Rasters, cube-mapped rasters, age grids, normal maps, 3D
scalar fields and reconstructed polygon meshes are all far too expensive to
rebuild per frame, so they are cached here, keyed by the
`GPlatesAppLogic::LayerProxy` that produced them. The public surface is
deliberately tiny — three render entry points and a slot — and it is the only way
the painters reach these objects: `GPlatesGui::LayerPainter`,
`GPlatesGui::Globe` and `GPlatesGui::MapRenderedGeometryLayerPainter` call in,
while `GPlatesQtWidgets::GlobeCanvas` and `GPlatesQtWidgets::MapView` own the
instances.

Internally there are two indexing levels. `GLLayers` maps each layer proxy to a
`GLLayer`, and each `GLLayer` holds one lazily created slot per
`LayerUsage::Type`. A "layer usage" is one *way* of consuming a layer's output,
and each subclass is a self-rebuilding pipeline stage: it keeps
`GPlatesUtils::ObserverToken`s against the layer proxy's subject tokens, and each
`get_*` call first asks whether it is still up to date, then tries the cheap
in-place update (`GLVisualRasterSource::change_raster`,
`GLScalarField3D::change_scalar_field`) and only falls back to discarding and
rebuilding the expensive object when that fails. The usages chain within a
layer — `RasterLayerUsage` feeds `CubeRasterLayerUsage` feeds
`StaticPolygonReconstructedRasterLayerUsage` feeds `MapRasterLayerUsage` — but
the age grid, normal map and reconstructed-polygon usages come from *other*
layers, which the user can rewire at any moment. That is why they are not wired
at construction: `render_raster` re-pushes them through
`set_reconstructing_layer_inputs` or `set_non_reconstructing_layer_inputs` on
every single call, and those methods compare the incoming usages against the
stored ones and invalidate the reconstructed raster when they differ.

The `NonListObjects` / `ListObjects` split exists because two OpenGL contexts may
or may not share "list" objects — textures, display lists, vertex buffer objects.
Non-list objects are always shared between `GLVisualLayers` instances; the
second `create` overload shares `ListObjects` only when both contexts report the
same `GLContext::SharedState`, and otherwise builds a second set. `ListObjects`
is also where the expensive-but-layer-independent singletons live: the
`GLMultiResolutionCubeMesh` (roughly 50 MB), the `GLMultiResolutionMapCubeMesh`,
the `GLFilledPolygonsGlobeView` and `GLFilledPolygonsMapView` renderers, and the
`GLLight`. All are created on first use and shared across every layer, because
none of them carries state specific to what a layer draws with them.

## Declared types

| Name | Kind | Bases | Template | Subclasses | Description |
|---|---|---|---|---|---|
| [`GPlatesOpenGL::GLVisualLayers`](#gplatesopenglglvisuallayers) | class | `QObject`<br>[`GPlatesUtils::ReferenceCount<GLVisualLayers>`](../utils/ReferenceCount.md) | — | 0 | Keeps track of any OpenGL-related objects that are persistent beyond one rendering frame. |

## Members

### `GPlatesOpenGL::GLVisualLayers`

| Member | Kind | Type | Access | Description |
|---|---|---|---|---|
| `non_null_ptr_type` | typedef | `GPlatesUtils::non_null_intrusive_ptr<GLVisualLayers>` | public | A convenience typedef for a shared pointer to a non-const GLVisualLayers. |
| `non_null_ptr_to_const_type` | typedef | `GPlatesUtils::non_null_intrusive_ptr<const GLVisualLayers>` | public | A convenience typedef for a shared pointer to a const GLVisualLayers. |
| `cache_handle_type` | typedef | `boost::shared_ptr<void>` | public | Typedef for an opaque object that caches a particular render (eg, raster or filled polygons). |
| `create( const GLContext::non_null_ptr_type &opengl_context, GPlatesAppLogic::ApplicationState &application_state)` | method | `non_null_ptr_type` | public | Creates a new GLVisualLayers object. |
| `create( const GLContext::non_null_ptr_type &opengl_context, const GLVisualLayers::non_null_ptr_type &objects_from_another_context, GPlatesAppLogic::ApplicationState &application_state)` | method | `non_null_ptr_type` | public | Creates a GLVisualLayers object and that always shares the non-list objects and only shares the list objects if objects\_from\_another\_context uses a context that shares the same shared state as opengl\_context. |
| `get_light( GLRenderer &renderer)` | method | `boost::optional<GLLight::non_null_ptr_type>` | public | Returns the light used for surface lighting or false if not supported on run-time system. |
| `render_raster( GLRenderer &renderer, const GPlatesAppLogic::ResolvedRaster::non_null_ptr_to_const_type &source_resolved_raster, const GPlatesGui::RasterColourPalette::non_null_ptr_to_const_type &source_raster_colour_palette, const GPlatesGui::Colour &source_raster_modulate_colour = GPlatesGui::Colour::get_white(), floa ...` | method | `cache_handle_type` | public | Renders the possibly reconstructed multi-resolution raster. |
| `render_scalar_field_3d( GLRenderer &renderer, const GPlatesAppLogic::ResolvedScalarField3D::non_null_ptr_to_const_type &source_resolved_scalar_field, const GPlatesViewOperations::ScalarField3DRenderParameters &render_parameters, boost::optional<GLTexture::shared_ptr_to_const_type> surface_occlusion_texture)` | method | `cache_handle_type` | public | Renders the 3D scalar field according as an isosurface or cross-sections. render\_parameters determines how to render the scalar field. surface\_occlusion\_texture is a viewport-size 2D texture containing the RGBA rendering of the surface ... |
| `render_filled_polygons( GLRenderer &renderer, const GLFilledPolygonsGlobeView::filled_drawables_type &filled_polygons)` | method | `void` | public | Renders filled polygons to the 3D globe view. |
| `render_filled_polygons( GLRenderer &renderer, const GLFilledPolygonsMapView::filled_drawables_type &filled_polygons)` | method | `void` | public | An overload of render\_filled\_polygons that renders filled polygons to a 2D map view. |
| `handle_layer_about_to_be_removed( GPlatesAppLogic::ReconstructGraph &reconstruct_graph, GPlatesAppLogic::Layer layer)` | method | `void` | public | Called when an existing layer is about to be removed. |
| `LayerUsage` | class | `None` | private | Base class for all layer usages. |
| `ScalarField3DLayerUsage` | class | `None` | private | A 3D scalar field (can be time-dependent). |
| `RasterLayerUsage` | class | `None` | private | A regular, unreconstructed coloured raster (can be time-dependent). |
| `CubeRasterLayerUsage` | class | `None` | private | A regular, unreconstructed coloured raster mapped into a cube map. |
| `AgeGridLayerUsage` | class | `None` | private | A present-day floating-point raster used to age-mask another reconstructed raster. |
| `NormalMapLayerUsage` | class | `None` | private | A normal map raster used to add surface lighting detail to another raster. |
| `ReconstructedStaticPolygonMeshesLayerUsage` | class | `None` | private | A group of reconstructed static polygon meshes. |
| `StaticPolygonReconstructedRasterLayerUsage` | class | `None` | private | A raster reconstructed using static polygons (and optionally an age-grid). |
| `MapRasterLayerUsage` | class | `None` | private | A map-view of a (possibly reconstructed) raster. |
| `GLLayer` | class | `None` | private | Represents OpenGL objects (in the various layer usage classes) associated with a layer. |
| `GLLayers` | class | `None` | private | Associates each GLLayer with a layer proxy (the output of an application-logic layer). |
| `NonListObjects` | struct | `None` | private | Any objects that do \*not\* use textures, display lists, vertex buffer objects, etc can go here, otherwise use ListObjects. |
| `ListObjects` | struct | `None` | private | Any objects that use textures, display lists, vertex buffer objects, etc should go here, otherwise use NonListObjects. |
| `d_non_list_objects` | field | `boost::shared_ptr<NonListObjects>` | private | NOTE: The non-list objects \*must\* be declared \*before\* the list objects (construction order). |
| `d_list_objects` | field | `boost::shared_ptr<ListObjects>` | private | — |
| `GLVisualLayers( const GLContext::non_null_ptr_type &opengl_context, GPlatesAppLogic::ApplicationState &application_state)` | constructor | `None` | private | Constructor. |
| `GLVisualLayers( const GLContext::non_null_ptr_type &opengl_context, const GLVisualLayers::non_null_ptr_type &objects_from_another_context, GPlatesAppLogic::ApplicationState &application_state)` | constructor | `None` | private | Constructor. |
| `make_signal_slot_connections( GPlatesAppLogic::ReconstructGraph &reconstruct_graph)` | method | `void` | private | — |

## Free functions and macros

| Name | Kind | Type / body | Description |
|---|---|---|---|
| `GPLATES_OPENGL_GLVISUALLAYERS_H` | macro | `None` | — |

## Notes

- `cache_handle_type` is `boost::shared_ptr<void>`: an opaque keep-alive token,
  not a value to inspect. The contract is that the caller holds the previous
  frame's handle *while* rendering the current frame and only then drops it — see
  `GlobeCanvas::d_gl_frame_cache_handle`. Dropping it immediately silently
  defeats frame-to-frame caching; never dropping it pins texture memory
  indefinitely.
- Invalidation is by pointer identity, not by value. Every downstream stage stores
  the upstream object it last saw and compares
  (`d_multi_resolution_cube_raster != multi_resolution_cube_raster`) to decide
  whether to rebuild. If you ever add a path that mutates one of these objects in
  place instead of replacing it, every downstream stage will keep using stale
  results without noticing.
- The layer-removal path is the whole reason this class is a `QObject`. Layer
  usages hold strong references to layer proxies, including proxies belonging to
  *other* layers, so without `handle_layer_about_to_be_removed` (connected to
  `ReconstructGraph::layer_about_to_be_removed`) a removed layer would stay alive
  along with its GPU memory. The two-tier response matters: if
  `is_required_direct_or_indirect_dependency` is true the whole usage slot is
  dropped, otherwise `removing_layer` gives the usage a chance to drop just that
  optional input and rebuild. A new layer usage with a new optional dependency
  must override `removing_layer` or it will hold a dangling-in-spirit reference.
- Declaration order in this class is load-bearing twice over, and both places
  carry a comment. `d_non_list_objects` must precede `d_list_objects` because
  `ListObjects` stores a `const NonListObjects &`; inside `ListObjects`,
  `d_filled_polygons_globe_view` must follow `d_multi_resolution_cube_mesh`
  because it is built from it.
- `GLLayer::d_layer_usages` is a flat vector indexed directly by
  `LayerUsage::Type` and sized by `NUM_TYPES`, so the enumerator order is part of
  the data structure. Adding a usage means adding an enumerator before
  `NUM_TYPES` and a matching `get_*` accessor.
- The `get_*_layer_usage` accessors `dynamic_pointer_cast` the layer proxy to the
  concrete proxy type and will throw (abort in debug builds) if it does not
  match. That is intentional — asking a non-raster layer for its raster usage is
  a programming error, not a user error.
- Almost every other failure is silent. Unsupported hardware
  (`GLScalarField3D::is_supported`,
  `GLMultiResolutionStaticPolygonReconstructedRaster::is_supported`,
  `GLLight::is_supported`) and missing data (no georeferencing, no colour
  palette, no proxied raster) all return `boost::none`, and `render_raster` then
  falls through reconstructed-globe to unreconstructed-globe and renders nothing
  at all if neither is available. Only failure to obtain an age grid or normal
  map logs a `qWarning`.
- `get_static_polygon_reconstructed_raster` deliberately returns `boost::none`
  when there are no reconstructed polygons, no age grid, no normal map and raster
  lighting is disabled, so that callers fall back to the cheaper plain
  `GLMultiResolutionRaster`. Conversely all raster lighting is routed through the
  "reconstructed" path even when nothing is being reconstructed, specifically to
  avoid applying lighting twice.
- `NormalMapLayerUsage` keys its `NormalRaster` objects by height-field scale
  factor in a map of `boost::weak_ptr`, pruning expired entries on every
  `get_normal_map` call. So one normal map is shared by all consumers using the
  same scale factor and is destroyed when the last of them lets go; a UI control
  that varies the scale factor continuously will churn these.
- `RasterLayerUsage` builds its `GLMultiResolutionRaster` with
  `CACHE_TILE_TEXTURES_NONE` on purpose, because `GLVisualRasterSource` already
  insulates it from the file system. Re-enabling that cache would multiply
  texture memory use for no gain.
- The map view builds its own cube raster rather than sharing the globe's,
  because the map's world transform depends on the map projection's central
  meridian and would re-orient a shared object.
- Every entry point here, including the `ListObjects` getters, requires an active
  OpenGL context and takes a `GLRenderer &`. None of this is safe to touch
  outside rendering.

## Used by

| Unit | Component | References |
|---|---|---|
| [gui/LayerPainter](../gui/LayerPainter.md) | gui | 26 |
| [gui/Globe](../gui/Globe.md) | gui | 7 |
| [gui/MapRenderedGeometryLayerPainter](../gui/MapRenderedGeometryLayerPainter.md) | gui | 7 |
| [gui/ExportRasterAnimationStrategy](../gui/ExportRasterAnimationStrategy.md) | gui | 6 |
| [qt-widgets/MapView](../qt-widgets/MapView.md) | qt-widgets | 6 |
| [gui/Map](../gui/Map.md) | gui | 5 |
| [qt-widgets/GlobeCanvas](../qt-widgets/GlobeCanvas.md) | qt-widgets | 5 |
| [gui/GlobeRenderedGeometryCollectionPainter](../gui/GlobeRenderedGeometryCollectionPainter.md) | gui | 4 |
| [gui/MapRenderedGeometryCollectionPainter](../gui/MapRenderedGeometryCollectionPainter.md) | gui | 4 |
| [gui/GlobeRenderedGeometryLayerPainter](../gui/GlobeRenderedGeometryLayerPainter.md) | gui | 3 |
| [qt-widgets/MapCanvas](../qt-widgets/MapCanvas.md) | qt-widgets | 3 |
| [gui/VelocityLegendOverlay](../gui/VelocityLegendOverlay.md) | gui | 2 |
| [qt-widgets/GlobeAndMapWidget](../qt-widgets/GlobeAndMapWidget.md) | qt-widgets | 1 |

## Related

**Qt signal/slot connections** (1 in this unit)

| Sender | Signal | Receiver | Slot |
|---|---|---|---|
| `&reconstruct_graph` | `layer_about_to_be_removed( GPlatesAppLogic::ReconstructGraph &, GPlatesAppLogic::Layer)` | `this` | `handle_layer_about_to_be_removed( GPlatesAppLogic::ReconstructGraph &, GPlatesAppLogic::Layer)` |


## Explore

Run these from the `gplates-code` skill directory:

```bash
python scripts/gpq.py file src/opengl/GLVisualLayers.h
python scripts/gpq.py def GPlatesOpenGL::GLVisualLayers --body
python scripts/gpq.py uses GLVisualLayers --kind class
python scripts/gpq.py hier GLVisualLayers
```
