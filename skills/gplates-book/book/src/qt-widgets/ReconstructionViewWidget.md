# ReconstructionViewWidget

[Book TOC](../../TOC.md) · [qt-widgets](../../components/qt-widgets.md) · cluster Community 295 · tier 2

| Source file | Kind | Lines |
|---|---|---|
| `src/qt-widgets/ReconstructionViewWidget.h` | C++ | 241 |
| `src/qt-widgets/ReconstructionViewWidget.cc` | C++ | 723 |
| `src/qt-widgets/ReconstructionViewWidgetUi.ui` | Qt form | 55 |

## Overview

[[[PROSE overview unit=qt-widgets/ReconstructionViewWidget tier=2]]]
Replace this whole block, markers included, with 1-3 paragraphs: what this unit is, why it exists, and how it fits the surrounding design. Do not restate the tables below.
[[[/PROSE]]]

## Declared types

| Name | Kind | Bases | Template | Subclasses | Description |
|---|---|---|---|---|---|
| [`GPlatesQtWidgets::ReconstructionViewWidget`](#gplatesqtwidgetsreconstructionviewwidget) | class | `QWidget`<br>`Ui_ReconstructionViewWidget` | — | 0 | — |

## Members

### `GPlatesQtWidgets::ReconstructionViewWidget`

| Member | Kind | Type | Access | Description |
|---|---|---|---|---|
| `ReconstructionViewWidget( ViewportWindow &viewport_window, GPlatesPresentation::ViewState &view_state, QWidget *parent_ = NULL)` | constructor | `None` | public | — |
| `WidgetIndex` | enum | `None` | public | — |
| `insert_task_panel( GPlatesQtWidgets::TaskPanel *task_panel)` | method | `void` | public | The Task Panel is created, and initialised by ViewportWindow. |
| `globe_canvas` | field | `GlobeCanvas` | public | — |
| `map_view` | field | `MapView` | public | — |
| `active_view` | field | `SceneView` | public | — |
| `globe_and_map_widget` | field | `GlobeAndMapWidget` | public | — |
| `globe_is_active()` | method | `bool` | public | — |
| `map_is_active()` | method | `bool` | public | — |
| `camera_llp()` | method | `boost::optional<GPlatesMaths::LatLonPoint>` | public | — |
| `activate_time_spinbox()` | method | `void` | public | — |
| `recalc_camera_position()` | method | `void` | public | — |
| `update_mouse_pointer_position( const GPlatesMaths::PointOnSphere &new_virtual_pos, bool is_on_globe)` | method | `void` | public | — |
| `update_mouse_pointer_position( const boost::optional<GPlatesMaths::LatLonPoint> &new_lat_lon_pos, bool is_on_map)` | method | `void` | public | — |
| `activate_zoom_spinbox()` | method | `void` | public | — |
| `handle_update_tools_and_status_message()` | method | `void` | public | — |
| `update_tools_and_status_message()` | method | `void` | public | — |
| `send_camera_pos_to_stdout( double, double)` | method | `void` | public | — |
| `send_orientation_to_stdout( GPlatesMaths::Rotation &)` | method | `void` | public | — |
| `handle_projection_type_changed( const GPlatesGui::ViewportProjection &viewport_projection)` | method | `void` | private | — |
| `construct_awesomebar_one( GPlatesGui::AnimationController &animation_controller, GPlatesQtWidgets::ViewportWindow &main_window)` | method | `std::unique_ptr<QWidget>` | private | — |
| `construct_awesomebar_two( GPlatesGui::ViewportZoom &vzoom, GPlatesGui::ViewportProjection &vprojection)` | method | `std::unique_ptr<QWidget>` | private | — |
| `construct_viewbar( GPlatesGui::ViewportZoom &vzoom)` | method | `std::unique_ptr<QWidget>` | private | — |
| `construct_viewbar_with_projections( GPlatesGui::ViewportZoom &vzoom, GPlatesGui::ViewportProjection &vprojection)` | method | `std::unique_ptr<QWidget>` | private | Experiment with adding the proj combo-box to the lower toolbar. |
| `d_view_state` | field | `GPlatesPresentation::ViewState` | private | — |
| `d_splitter_widget` | field | `QSplitter` | private | The QSplitter responsible for dividing the interface between canvas and TaskPanel. |
| `d_label_camera_coords` | field | `QLabel` | private | The camera coordinates label. |
| `d_label_mouse_coords` | field | `QLabel` | private | The mouse coordinates label. |
| `d_globe_and_map_widget_ptr` | field | `GlobeAndMapWidget` | private | Holds the globe and the map. |
| `d_animate_control_widget_ptr` | field | `AnimateControlWidget` | private | — |
| `d_zoom_control_widget_ptr` | field | `ZoomControlWidget` | private | — |
| `d_time_control_widget_ptr` | field | `TimeControlWidget` | private | — |
| `d_zoom_slider_widget` | field | `ZoomSliderWidget` | private | — |
| `d_projection_control_widget_ptr` | field | `ProjectionControlWidget` | private | — |
| `d_gmenu_button_ptr` | field | `GMenuButton` | private | — |

## Free functions and macros

| Name | Kind | Type / body | Description |
|---|---|---|---|
| `DEFAULT_MOUSE_COORDS_LABEL_TEXT_FOR_GLOBE` | variable | `QString` | — |
| `DEFAULT_MOUSE_COORDS_LABEL_TEXT_FOR_MAP` | variable | `QString` | — |
| `DEFAULT_CAMERA_COORDS_LABEL_TEXT` | variable | `QString` | — |
| `wrap_with_frame( QWidget *widget)` | function | `QFrame` | Wraps Qt widget up inside a frame suitably styled for ReconstructionViewWidget. |
| `wrap_with_frame( QLayoutItem *item)` | function | `QFrame` | Wraps Qt layout (or spacer) up inside a frame suitably styled for ReconstructionViewWidget. |
| `cram_widget_into_widget( QWidget *inner_widget, QWidget *outer_widget)` | function | `void` | This function is a bit of a hack, but we need this hack in enough places in our hybrid Designer/C++ laid-out ReconstructionViewWidget that it's worthwhile compressing it into an anonymous namespace function. |
| `new_horizontal_spacer()` | function | `QSpacerItem` | Slightly less awkward way to summon a horizontal spacer. |
| `new_camera_coords_label()` | function | `QLabel` | Creates the label used for camera coordinate display. |
| `new_mouse_coords_label()` | function | `QLabel` | Creates the label used for mouse coordinate display. |
| `GPLATES_QTWIDGETS_RECONSTRUCTIONVIEWWIDGET_H` | macro | `None` | — |

## Notes

[[[PROSE notes unit=qt-widgets/ReconstructionViewWidget tier=2]]]
Replace this whole block, markers included, with invariants, ownership, threading or gotchas that are not visible in the tables. Write *None.* if there is nothing worth saying.
[[[/PROSE]]]

## Used by

| Unit | Component | References |
|---|---|---|
| [gui/DigitisationCanvasToolWorkflow](../gui/DigitisationCanvasToolWorkflow.md) | gui | 37 |
| [gui/FeatureInspectionCanvasToolWorkflow](../gui/FeatureInspectionCanvasToolWorkflow.md) | gui | 31 |
| [qt-widgets/ViewportWindow](ViewportWindow.md) | qt-widgets | 29 |
| [gui/TopologyCanvasToolWorkflow](../gui/TopologyCanvasToolWorkflow.md) | gui | 23 |
| [gui/PoleManipulationCanvasToolWorkflow](../gui/PoleManipulationCanvasToolWorkflow.md) | gui | 15 |
| [gui/ViewCanvasToolWorkflow](../gui/ViewCanvasToolWorkflow.md) | gui | 15 |
| [gui/ExternalSyncController](../gui/ExternalSyncController.md) | gui | 7 |
| [gui/SmallCircleCanvasToolWorkflow](../gui/SmallCircleCanvasToolWorkflow.md) | gui | 7 |
| [gui/Dialogs](../gui/Dialogs.md) | gui | 4 |
| [api/PyViewportWindow](../api/PyViewportWindow.md) | api | 3 |
| [gui/CommandServer](../gui/CommandServer.md) | gui | 3 |
| [gui/ExportRasterAnimationStrategy](../gui/ExportRasterAnimationStrategy.md) | gui | 3 |
| [gui/ExportSvgAnimationStrategy](../gui/ExportSvgAnimationStrategy.md) | gui | 3 |
| [qt-widgets/DrawStyleDialog](DrawStyleDialog.md) | qt-widgets | 3 |
| [qt-widgets/ExportImageResolutionOptionsWidget](ExportImageResolutionOptionsWidget.md) | qt-widgets | 3 |
| [api/PyCoregistrationLayerProxy](../api/PyCoregistrationLayerProxy.md) | api | 2 |
| [gui/ExportCoRegistrationAnimationStrategy](../gui/ExportCoRegistrationAnimationStrategy.md) | gui | 2 |
| [gui/ExportImageAnimationStrategy](../gui/ExportImageAnimationStrategy.md) | gui | 2 |
| [presentation/ScalarField3DVisualLayerParams](../presentation/ScalarField3DVisualLayerParams.md) | presentation | 2 |
| [qt-widgets/CoRegistrationLayerConfigurationDialog](CoRegistrationLayerConfigurationDialog.md) | qt-widgets | 2 |

*... and 5 more units.*

## Related

**Qt Designer forms**

| Form class | Base widget | Title | Widgets |
|---|---|---|---|
| `ReconstructionViewWidget` | `QWidget` | Form | 3 |

**Qt signal/slot connections** (10 in this unit)

| Sender | Signal | Receiver | Slot |
|---|---|---|---|
| `&(d_globe_and_map_widget_ptr->get_globe_canvas().globe().orientation())` | `orientation_changed()` | `this` | `recalc_camera_position()` |
| `&(view_state.get_map_transform())` | `transform_changed(const GPlatesGui::MapTransform &)` | `this` | `recalc_camera_position()` |
| `&(d_globe_and_map_widget_ptr->get_globe_canvas())` | `mouse_pointer_position_changed(const GPlatesMaths::PointOnSphere &, bool)` | `this` | `update_mouse_pointer_position(const GPlatesMaths::PointOnSphere &, bool)` |
| `&(d_globe_and_map_widget_ptr->get_map_view())` | `mouse_pointer_position_changed(const boost::optional<GPlatesMaths::LatLonPoint> &, bool)` | `this` | `update_mouse_pointer_position(const boost::optional<GPlatesMaths::LatLonPoint> &, bool)` |
| `&(view_state.get_viewport_projection())` | `projection_type_changed(const GPlatesGui::ViewportProjection &)` | `this` | `handle_projection_type_changed(const GPlatesGui::ViewportProjection &)` |
| `d_globe_and_map_widget_ptr` | `update_tools_and_status_message()` | `this` | `handle_update_tools_and_status_message()` |
| `this` | `update_tools_and_status_message()` | `&viewport_window` | `update_tools_and_status_message()` |
| `d_time_control_widget_ptr` | `editing_finished()` | `&(d_globe_and_map_widget_ptr->get_globe_canvas())` | `setFocus()` |
| `d_zoom_control_widget_ptr` | `editing_finished()` | `&(d_globe_and_map_widget_ptr->get_globe_canvas())` | `setFocus()` |
| `d_zoom_control_widget_ptr` | `editing_finished()` | `&(d_globe_and_map_widget_ptr->get_globe_canvas())` | `setFocus()` |


## Explore

Run these from the `gplates-code` skill directory:

```bash
python scripts/gpq.py file src/qt-widgets/ReconstructionViewWidget.h
python scripts/gpq.py def GPlatesQtWidgets::ReconstructionViewWidget --body
python scripts/gpq.py uses ReconstructionViewWidget --kind class
python scripts/gpq.py hier ReconstructionViewWidget
```
