# SmallCircleWidget

[Book TOC](../../TOC.md) · [qt-widgets](../../components/qt-widgets.md) · cluster Community 594 · tier 2

| Source file | Kind | Lines |
|---|---|---|
| `src/qt-widgets/SmallCircleWidget.h` | C++ | 180 |
| `src/qt-widgets/SmallCircleWidget.cc` | C++ | 232 |
| `src/qt-widgets/SmallCircleWidgetUi.ui` | Qt form | 189 |

## Overview

[[[PROSE overview unit=qt-widgets/SmallCircleWidget tier=2]]]
Replace this whole block, markers included, with 1-3 paragraphs: what this unit is, why it exists, and how it fits the surrounding design. Do not restate the tables below.
[[[/PROSE]]]

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

[[[PROSE notes unit=qt-widgets/SmallCircleWidget tier=2]]]
Replace this whole block, markers included, with invariants, ownership, threading or gotchas that are not visible in the tables. Write *None.* if there is nothing worth saying.
[[[/PROSE]]]

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
