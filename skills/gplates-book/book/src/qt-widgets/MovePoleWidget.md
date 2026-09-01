# MovePoleWidget

[Book TOC](../../TOC.md) · [qt-widgets](../../components/qt-widgets.md) · cluster Community 220 · tier 2

| Source file | Kind | Lines |
|---|---|---|
| `src/qt-widgets/MovePoleWidget.h` | C++ | 180 |
| `src/qt-widgets/MovePoleWidget.cc` | C++ | 547 |
| `src/qt-widgets/MovePoleWidgetUi.ui` | Qt form | 363 |

## Overview

[[[PROSE overview unit=qt-widgets/MovePoleWidget tier=2]]]
Replace this whole block, markers included, with 1-3 paragraphs: what this unit is, why it exists, and how it fits the surrounding design. Do not restate the tables below.
[[[/PROSE]]]

## Declared types

| Name | Kind | Bases | Template | Subclasses | Description |
|---|---|---|---|---|---|
| [`GPlatesQtWidgets::MovePoleWidget`](#gplatesqtwidgetsmovepolewidget) | class | [`TaskPanelWidget`](TaskPanelWidget.md)<br>`Ui_MovePoleWidget` | — | 0 | — |

## Members

### `GPlatesQtWidgets::MovePoleWidget`

| Member | Kind | Type | Access | Description |
|---|---|---|---|---|
| `MovePoleWidget( GPlatesPresentation::ViewState &view_state, QWidget *parent_ = NULL)` | constructor | `None` | public | — |
| `~MovePoleWidget()` | destructor | `None` | public | — |
| `handle_activation()` | method | `void` | public | — |
| `get_pole()` | method | `boost::optional<GPlatesMaths::PointOnSphere>` | public | Returns pole (if enabled). |
| `can_change_pole()` | method | `bool` | public | Returns true if the pole can currently be changed with set\_pole. |
| `set_pole( boost::optional<GPlatesMaths::PointOnSphere> pole = boost::none)` | method | `void` | public | Sets pole (also enables/disables pole). |
| `pole_changed( boost::optional<GPlatesMaths::PointOnSphere> pole)` | method | `void` | public | Emitted when the pole has changed (including enabled/disabled). |
| `activate()` | method | `void` | public | — |
| `deactivate()` | method | `void` | public | — |
| `set_focus()` | method | `void` | private | — |
| `handle_reconstruction()` | method | `void` | private | — |
| `react_enable_pole_check_box_changed()` | method | `void` | private | — |
| `react_latitude_spinbox_changed()` | method | `void` | private | — |
| `react_longitude_spinbox_changed()` | method | `void` | private | — |
| `react_north_pole_pushbutton_clicked()` | method | `void` | private | — |
| `react_stage_pole_pushbutton_clicked()` | method | `void` | private | — |
| `react_keep_stage_pole_constrained_checkbox_changed()` | method | `void` | private | — |
| `d_feature_focus` | field | `GPlatesGui::FeatureFocus` | private | — |
| `d_pole` | field | `boost::optional<GPlatesMaths::PointOnSphere>` | private | — |
| `make_signal_slot_connections( GPlatesPresentation::ViewState &view_state)` | method | `void` | private | — |
| `update_stage_pole_moving_fixed_plate_ids()` | method | `void` | private | — |
| `get_focused_feature_geometry()` | method | `boost::optional<GPlatesAppLogic::ReconstructedFeatureGeometry::non_null_ptr_to_const_type>` | private | — |
| `get_stage_pole_plate_pair( const GPlatesAppLogic::ReconstructedFeatureGeometry &rfg)` | method | `boost::optional< std::pair< GPlatesModel::integer_plate_id_type/*moving*/, GPlatesModel::integer_plate_id_type/*fixed*/> >` | private | — |
| `get_stage_pole_location()` | method | `boost::optional<GPlatesMaths::PointOnSphere>` | private | — |
| `set_stage_pole_location()` | method | `void` | private | — |
| `set_pole_internal( boost::optional<GPlatesMaths::PointOnSphere> pole)` | method | `void` | private | — |

## Free functions and macros

| Name | Kind | Type / body | Description |
|---|---|---|---|
| `GPLATES_QT_WIDGETS_MOVEPOLEWIDGET_H` | macro | `None` | — |

## Notes

[[[PROSE notes unit=qt-widgets/MovePoleWidget tier=2]]]
Replace this whole block, markers included, with invariants, ownership, threading or gotchas that are not visible in the tables. Write *None.* if there is nothing worth saying.
[[[/PROSE]]]

## Used by

| Unit | Component | References |
|---|---|---|
| [view-operations/MovePoleOperation](../view-operations/MovePoleOperation.md) | view-operations | 12 |
| [qt-widgets/ModifyReconstructionPoleWidget](ModifyReconstructionPoleWidget.md) | qt-widgets | 10 |
| [app-logic/ReconstructionGraphBuilder](../app-logic/ReconstructionGraphBuilder.md) | app-logic | 1 |
| [app-logic/ReconstructionTree](../app-logic/ReconstructionTree.md) | app-logic | 1 |
| [qt-widgets/TaskPanel](TaskPanel.md) | qt-widgets | 1 |

## Related

**Qt Designer forms**

| Form class | Base widget | Title | Widgets |
|---|---|---|---|
| `MovePoleWidget` | `QWidget` | Form | 24 |

**Qt signal/slot connections** (11 in this unit)

| Sender | Signal | Receiver | Slot |
|---|---|---|---|
| `&view_state.get_feature_focus()` | `focus_changed(GPlatesGui::FeatureFocus &)` | `this` | `set_focus()` |
| `&view_state.get_application_state()` | `reconstructed(GPlatesAppLogic::ApplicationState &)` | `this` | `handle_reconstruction()` |
| `enable_pole_checkbox` | `stateChanged(int)` | `this` | `react_enable_pole_check_box_changed()` |
| `latitude_spinbox` | `valueChanged(double)` | `this` | `react_latitude_spinbox_changed()` |
| `longitude_spinbox` | `valueChanged(double)` | `this` | `react_longitude_spinbox_changed()` |
| `north_pole_pushbutton` | `clicked(bool)` | `this` | `react_north_pole_pushbutton_clicked()` |
| `constrain_to_stage_pole_pushbutton` | `clicked(bool)` | `this` | `react_stage_pole_pushbutton_clicked()` |
| `keep_stage_pole_constrained_checkbox` | `stateChanged(int)` | `this` | `react_keep_stage_pole_constrained_checkbox_changed()` |
| `enable_pole_checkbox` | `stateChanged(int)` | `this` | `react_enable_pole_check_box_changed()` |
| `latitude_spinbox` | `valueChanged(double)` | `this` | `react_latitude_spinbox_changed()` |
| `longitude_spinbox` | `valueChanged(double)` | `this` | `react_longitude_spinbox_changed()` |


## Explore

Run these from the `gplates-code` skill directory:

```bash
python scripts/gpq.py file src/qt-widgets/MovePoleWidget.h
python scripts/gpq.py def GPlatesQtWidgets::MovePoleWidget --body
python scripts/gpq.py uses MovePoleWidget --kind class
python scripts/gpq.py hier MovePoleWidget
```
