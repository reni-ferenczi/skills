# SmallCircleWidget

[Book TOC](../../TOC.md) · [qt-widgets](../../components/qt-widgets.md) · cluster Community 594 · tier 2

| Source file | Kind | Lines |
|---|---|---|
| `src/qt-widgets/SmallCircleWidget.h` | C++ | 180 |
| `src/qt-widgets/SmallCircleWidget.cc` | C++ | 232 |
| `src/qt-widgets/SmallCircleWidgetUi.ui` | Qt form | 189 |

## Overview

`SmallCircleWidget` is the `TaskPanelWidget` for the "Create Small Circle" canvas tool (`GPlatesCanvasTools::CreateSmallCircle`): it holds the centre point and radii the user has specified, draws them on the globe/map through a dedicated `GPlatesViewOperations::RenderedGeometryLayer` (the `SMALL_CIRCLE_CANVAS_TOOL_WORKFLOW_LAYER`), and drives feature creation once the user is satisfied. It is disabled by default and only becomes usable when the canvas tool activates it via `handle_activation()`, so a task panel present at startup cannot be interacted with before its matching tool is selected.

The widget owns a non-modal `CreateSmallCircleDialog` (used to type a centre/radius by hand rather than by clicking the globe) and closes it in `hideEvent()` whenever the task panel itself is hidden, since the tool being deactivated should take the helper dialog down with it. Circles the user has built up are kept in `d_small_circles`; `handle_create_feature()` hands that collection to a separate `CreateSmallCircleFeatureDialog` to actually construct model features, and on acceptance emits `feature_created()`, which is wired directly to `ApplicationState::reconstruct()` to refresh the reconstruction.

## Declared types

| Name | Kind | Bases | Template | Subclasses | Description |
|---|---|---|---|---|---|
| [`GPlatesQtWidgets::SmallCircleWidget`](#gplatesqtwidgetssmallcirclewidget) | class | [`TaskPanelWidget`](TaskPanelWidget.md)<br>`Ui_SmallCircleWidget` | — | 0 | — |

## Members

### `GPlatesQtWidgets::SmallCircleWidget`

| Member | Kind | Type | Access | Description |
|---|---|---|---|---|
| `small_circle_collection_type` | typedef | `std::vector<GPlatesMaths::SmallCircle>` | public | — |
| `SmallCircleWidget( GPlatesPresentation::ViewState &view_state, QWidget *parent_ = NULL)` | constructor | `None` | public | — |
| `handle_activation()` | method | `void` | public | — |
| `set_centre( const GPlatesMaths::LatLonPoint &centre)` | method | `void` | public | — |
| `update_small_circle_layer()` | method | `void` | public | — |
| `update_current_centre( const GPlatesMaths::PointOnSphere &current_centre)` | method | `void` | public | Update the centre part of the current\_circles group box. |
| `update_current_radius( const GPlatesMaths::Real &radius_in_radians)` | method | `void` | public | — |
| `update_radii( boost::optional<double> current_radius = boost::none)` | method | `void` | public | Update the radii of the current\_circles group box from small circles collection d\_small\_circles. |
| `update_circles( small_circle_collection_type &small_circle_collection)` | method | `void` | public | — |
| `feature_created()` | method | `void` | public | For triggering a reconstruction. |
| `clear_geometries()` | method | `void` | public | — |
| `set_default_states()` | method | `void` | private | — |
| `hideEvent( QHideEvent *)` | method | `void` | private | Override the QWidget's hideEvent so that we can close the associated (non-modal) CalculateSmallCircle dialog as well. |
| `update_buttons()` | method | `void` | private | — |
| `update_current_circles()` | method | `void` | private | — |
| `handle_create_feature()` | method | `void` | private | — |
| `handle_clear()` | method | `void` | private | — |
| `handle_specify()` | method | `void` | private | — |
| `d_application_state_ptr` | field | `GPlatesAppLogic::ApplicationState` | private | — |
| `d_create_small_circle_dialog_ptr` | field | `CreateSmallCircleDialog` | private | — |
| `d_small_circle_layer` | field | `GPlatesViewOperations::RenderedGeometryLayer` | private | — |
| `d_small_circles` | field | `small_circle_collection_type` | private | — |

## Free functions and macros

| Name | Kind | Type / body | Description |
|---|---|---|---|
| `GPLATES_QTWIDGETS_SMALLCIRCLEWIDGET_H` | macro | `None` | — |

## Notes

- The widget is constructed disabled (`setEnabled(false)`) and relies on the canvas tool calling `handle_activation()` to enable it; code that reuses this widget outside the small-circle tool's workflow must replicate that activation step or it will render inert.
- `hideEvent()` closes `d_create_small_circle_dialog_ptr` unconditionally whenever the task panel is hidden, including on ordinary panel switches — not just when the tool itself is deactivated.

## Used by

| Unit | Component | References |
|---|---|---|
| [canvas-tools/CreateSmallCircle](../canvas-tools/CreateSmallCircle.md) | canvas-tools | 18 |
| [qt-widgets/deprecated/SmallCircleManager](deprecated/SmallCircleManager.md) | qt-widgets | 15 |
| [qt-widgets/CreateSmallCircleDialog](CreateSmallCircleDialog.md) | qt-widgets | 7 |
| [qt-widgets/deprecated/CalculateStagePoleDialog](deprecated/CalculateStagePoleDialog.md) | qt-widgets | 6 |
| [qt-widgets/TaskPanel](TaskPanel.md) | qt-widgets | 2 |

## Related

**Qt Designer forms**

| Form class | Base widget | Title | Widgets |
|---|---|---|---|
| `SmallCircleWidget` | `QWidget` | Form | 9 |

**Qt signal/slot connections** (2 in this unit)

| Sender | Signal | Receiver | Slot |
|---|---|---|---|
| `this` | `feature_created()` | `d_application_state_ptr` | `reconstruct()` |
| `button_specify` | `clicked()` | `this` | `handle_specify()` |


## Explore

Run these from the `gplates-code` skill directory:

```bash
python scripts/gpq.py file src/qt-widgets/SmallCircleWidget.h
python scripts/gpq.py def GPlatesQtWidgets::SmallCircleWidget --body
python scripts/gpq.py uses SmallCircleWidget --kind class
python scripts/gpq.py hier SmallCircleWidget
```
