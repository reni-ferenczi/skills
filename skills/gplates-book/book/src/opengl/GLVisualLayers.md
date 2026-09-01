# GLVisualLayers

[Book TOC](../../TOC.md) · [opengl](../../components/opengl.md) · cluster Community 79 · tier 1

| Source file | Kind | Lines |
|---|---|---|
| `src/opengl/GLVisualLayers.h` | C++ | 1005 |
| `src/opengl/GLVisualLayers.cc` | C++ | 1864 |

## Overview

[[[PROSE overview unit=opengl/GLVisualLayers tier=1]]]
Replace this whole block, markers included, with 1-3 paragraphs: what this unit is, why it exists, and how it fits the surrounding design. Do not restate the tables below.
[[[/PROSE]]]

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

[[[PROSE notes unit=opengl/GLVisualLayers tier=1]]]
Replace this whole block, markers included, with invariants, ownership, threading or gotchas that are not visible in the tables. Write *None.* if there is nothing worth saying.
[[[/PROSE]]]

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
