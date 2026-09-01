# GlobeAndMapWidget

[Book TOC](../../TOC.md) · [qt-widgets](../../components/qt-widgets.md) · cluster Community 444 · tier 2

| Source file | Kind | Lines |
|---|---|---|
| `src/qt-widgets/GlobeAndMapWidget.h` | C++ | 294 |
| `src/qt-widgets/GlobeAndMapWidget.cc` | C++ | 548 |

## Overview

`GlobeAndMapWidget` owns both a `GlobeCanvas` and a `MapView` inside a `QStackedLayout` and switches which one is visible whenever the projection changes: `ViewportProjection`'s `projection_type_changed`/`central_meridian_changed` signals drive `change_projection()`, which reconfigures the map's projection, chooses the globe for `ORTHOGRAPHIC` and the map otherwise, and re-applies the camera position captured just beforehand in `about_to_change_projection()` so the switch feels seamless to the user. `get_active_view()`/`is_globe_active()`/`is_map_active()` let callers query which `SceneView` is current without caring which concrete widget backs it.

The private cloning constructor and `clone_with_shared_opengl_context()` build a second `GlobeAndMapWidget` that shares the original's OpenGL context and copies which view is active, for use where a second, independently rendered view onto the same OpenGL resources is needed (for example an export preview). Because a `ColourScheme` is threaded through many of the constructors it clones from but is not actually needed for this shared-context clone, the `.cc` file's `DummyColourScheme` (a trivial `SingleColourScheme` subclass) is passed in purely to satisfy those call signatures.

## Declared types

| Name | Kind | Bases | Template | Subclasses | Description |
|---|---|---|---|---|---|
| [`DummyColourScheme`](#dummycolourscheme) | class | [`GPlatesGui::SingleColourScheme`](../gui/SingleColourScheme.md) | — | 0 | — |
| [`GPlatesQtWidgets::GlobeAndMapWidget`](#gplatesqtwidgetsglobeandmapwidget) | class | `QWidget`<br>[`GPlatesViewOperations::QueryProximityThreshold`](../view-operations/QueryProximityThreshold.md) | — | 0 | This class is responsible for creating and holding the globe and the map, and for switching between them as appropriate. |

## Members

### `DummyColourScheme`

*None.*

### `GPlatesQtWidgets::GlobeAndMapWidget`

| Member | Kind | Type | Access | Description |
|---|---|---|---|---|
| `GlobeAndMapWidget( GPlatesPresentation::ViewState &view_state, QWidget *parent_ = NULL)` | constructor | `None` | public | Use this constructor if you're constructing a fresh GlobeAndMapWidget from scratch. |
| `GlobeAndMapWidget( const GlobeAndMapWidget *existing_globe_and_map_widget_ptr, GPlatesGui::ColourScheme::non_null_ptr_type colour_scheme, QWidget *parent_ = NULL)` | constructor | `None` | public | Use this constructor if you want to make a clone of an existing GlobeAndMapWidget. |
| `clone_with_shared_opengl_context( QWidget *parent_ = NULL)` | method | `GlobeAndMapWidget` | public | — |
| `~GlobeAndMapWidget()` | destructor | `None` | public | — |
| `get_globe_canvas` | field | `GlobeCanvas` | public | — |
| `get_map_view` | field | `MapView` | public | — |
| `get_active_view` | field | `SceneView` | public | — |
| `is_globe_active()` | method | `bool` | public | — |
| `is_map_active()` | method | `bool` | public | — |
| `get_camera_llp()` | method | `boost::optional<GPlatesMaths::LatLonPoint>` | public | — |
| `sizeHint()` | method | `QSize` | public | — |
| `get_viewport_size()` | method | `QSize` | public | Returns the dimensions of the viewport in device \*independent\* pixels (ie, widget size). |
| `render_to_qimage( const QSize &image_size_in_device_independent_pixels, const GPlatesGui::Colour &image_clear_colour)` | method | `QImage` | public | Renders the scene to a QImage of the dimensions specified by image\_size. |
| `get_active_gl_context()` | method | `GPlatesGlobal::PointerTraits<GPlatesOpenGL::GLContext>::non_null_ptr_type` | public | Returns the OpenGL context for the active view. |
| `get_active_gl_visual_layers()` | method | `GPlatesGlobal::PointerTraits<GPlatesOpenGL::GLVisualLayers>::non_null_ptr_type` | public | Returns the OpenGL layers used to filled polygons, render rasters and scalar fields. |
| `update_canvas()` | method | `void` | public | — |
| `current_proximity_inclusion_threshold( const GPlatesMaths::PointOnSphere &click_pos_on_globe)` | method | `double` | public | — |
| `set_zoom_enabled( bool enabled)` | method | `void` | public | — |
| `update_tools_and_status_message()` | method | `void` | public | — |
| `resized( int new_width, int new_height)` | method | `void` | public | — |
| `repainted( bool mouse_down)` | method | `void` | public | — |
| `event( QEvent *ev)` | method | `bool` | protected | — |
| `resizeEvent( QResizeEvent *resize_event)` | method | `void` | protected | — |
| `wheelEvent( QWheelEvent *event)` | method | `void` | protected | This is a virtual override of the function in QWidget. |
| `init()` | method | `void` | private | — |
| `handle_zoom_change()` | method | `void` | private | — |
| `about_to_change_projection( const GPlatesGui::ViewportProjection &view_projection)` | method | `void` | private | — |
| `change_projection( const GPlatesGui::ViewportProjection &view_projection)` | method | `void` | private | — |
| `handle_globe_or_map_repainted( bool mouse_down)` | method | `void` | private | — |
| `GlobeAndMapWidget( const GlobeAndMapWidget *existing_widget, QWidget *parent_ = NULL)` | constructor | `None` | private | — |
| `make_signal_slot_connections()` | method | `void` | private | — |
| `d_view_state` | field | `GPlatesPresentation::ViewState` | private | — |
| `d_globe_canvas_ptr` | field | `boost::scoped_ptr<GlobeCanvas>` | private | — |
| `d_map_view_ptr` | field | `boost::scoped_ptr<MapView>` | private | — |
| `d_layout` | field | `QStackedLayout` | private | — |
| `d_active_view_ptr` | field | `SceneView` | private | Which of globe and map is currently active. |
| `d_active_camera_llp` | field | `boost::optional<GPlatesMaths::LatLonPoint>` | private | The camera position of the currently active view. |
| `d_zoom_enabled` | field | `bool` | private | Whether zooming (via mouse wheel or pinch gesture) is enabled. |
| `viewport_zoom_at_start_of_pinch` | field | `boost::optional<double>` | private | The viewport zoom percentage at the start of a pinch gesture. |

## Free functions and macros

| Name | Kind | Type / body | Description |
|---|---|---|---|
| `GPLATES_QTWIDGETS_GLOBEANDMAPWIDGET_H` | macro | `None` | — |
| `GPLATES_PINCH_ZOOM_ENABLED` | macro | `None` | — |

## Notes

`d_map_view_ptr` must be declared after `d_globe_canvas_ptr` in the class (the map view is constructed using the globe canvas's OpenGL context, so the globe canvas must already exist). `get_viewport_size()` and `render_to_qimage()` work in device-*independent* pixels; OpenGL-side sizes use device pixels and differ by the device pixel ratio. Pinch-zoom handling (`event()` override, `viewport_zoom_at_start_of_pinch`) is compiled in only under `GPLATES_PINCH_ZOOM_ENABLED`, which is defined for macOS only.

## Used by

| Unit | Component | References |
|---|---|---|
| [qt-widgets/ReconstructionViewWidget](ReconstructionViewWidget.md) | qt-widgets | 24 |
| [qt-widgets/ColouringDialog](ColouringDialog.md) | qt-widgets | 5 |
| [qt-widgets/ExportImageResolutionOptionsWidget](ExportImageResolutionOptionsWidget.md) | qt-widgets | 5 |
| [qt-widgets/ViewportWindow](ViewportWindow.md) | qt-widgets | 5 |
| [gui/ExportImageAnimationStrategy](../gui/ExportImageAnimationStrategy.md) | gui | 4 |
| [gui/ExportRasterAnimationStrategy](../gui/ExportRasterAnimationStrategy.md) | gui | 4 |
| [gui/CommandServer](../gui/CommandServer.md) | gui | 3 |
| [qt-widgets/DrawStyleDialog](DrawStyleDialog.md) | qt-widgets | 3 |
| [qt-widgets/ImportScalarField3DDialog](ImportScalarField3DDialog.md) | qt-widgets | 3 |
| [qt-widgets/LightingWidget](LightingWidget.md) | qt-widgets | 3 |
| [api/PyCoregistrationLayerProxy](../api/PyCoregistrationLayerProxy.md) | api | 2 |
| [gui/ExportCoRegistrationAnimationStrategy](../gui/ExportCoRegistrationAnimationStrategy.md) | gui | 2 |
| [presentation/ScalarField3DVisualLayerParams](../presentation/ScalarField3DVisualLayerParams.md) | presentation | 2 |
| [qt-widgets/CoRegistrationLayerConfigurationDialog](CoRegistrationLayerConfigurationDialog.md) | qt-widgets | 2 |
| [qt-widgets/CoRegistrationResultTableDialog](CoRegistrationResultTableDialog.md) | qt-widgets | 2 |
| [gui/DigitisationCanvasToolWorkflow](../gui/DigitisationCanvasToolWorkflow.md) | gui | 1 |
| [gui/FeatureInspectionCanvasToolWorkflow](../gui/FeatureInspectionCanvasToolWorkflow.md) | gui | 1 |
| [gui/PoleManipulationCanvasToolWorkflow](../gui/PoleManipulationCanvasToolWorkflow.md) | gui | 1 |
| [gui/SmallCircleCanvasToolWorkflow](../gui/SmallCircleCanvasToolWorkflow.md) | gui | 1 |
| [gui/TopologyCanvasToolWorkflow](../gui/TopologyCanvasToolWorkflow.md) | gui | 1 |

*... and 1 more units.*

## Related

**Qt signal/slot connections** (6 in this unit)

| Sender | Signal | Receiver | Slot |
|---|---|---|---|
| `&vzoom` | `zoom_changed()` | `this` | `handle_zoom_change()` |
| `&vprojection` | `projection_type_about_to_change(const GPlatesGui::ViewportProjection &)` | `this` | `about_to_change_projection(const GPlatesGui::ViewportProjection &)` |
| `&vprojection` | `projection_type_changed(const GPlatesGui::ViewportProjection &)` | `this` | `change_projection(const GPlatesGui::ViewportProjection &)` |
| `&vprojection` | `central_meridian_changed(const GPlatesGui::ViewportProjection &)` | `this` | `change_projection(const GPlatesGui::ViewportProjection &)` |
| `d_globe_canvas_ptr.get()` | `repainted(bool)` | `this` | `handle_globe_or_map_repainted(bool)` |
| `d_map_view_ptr.get()` | `repainted(bool)` | `this` | `handle_globe_or_map_repainted(bool)` |


## Explore

Run these from the `gplates-code` skill directory:

```bash
python scripts/gpq.py file src/qt-widgets/GlobeAndMapWidget.h
python scripts/gpq.py def GPlatesQtWidgets::GlobeAndMapWidget --body
python scripts/gpq.py uses GlobeAndMapWidget --kind class
python scripts/gpq.py hier GlobeAndMapWidget
```
