# MovePoleWidget

[Book TOC](../../TOC.md) · [qt-widgets](../../components/qt-widgets.md) · cluster Community 220 · tier 2

| Source file | Kind | Lines |
|---|---|---|
| `src/qt-widgets/MovePoleWidget.h` | C++ | 180 |
| `src/qt-widgets/MovePoleWidget.cc` | C++ | 547 |
| `src/qt-widgets/MovePoleWidgetUi.ui` | Qt form | 363 |

## Overview

The task panel widget for the "move pole" canvas tool: it lets the user specify a pivot point (`d_pole`, an optional `GPlatesMaths::PointOnSphere`) that geometry is rotated about, either by typing lat/lon directly, by resetting to the north pole, or by locking it to the focused feature's current stage pole. Because the actual rotation is driven by [`view-operations/MovePoleOperation`](../view-operations/MovePoleOperation.md), this class only owns the pole value and its UI; every change funnels through `set_pole_internal`, which updates the checkbox/spinboxes without re-triggering their own change slots and then emits `pole_changed` exactly once per change.

"Stage pole" mode (`keep_stage_pole_constrained_checkbox`) computes the pole from the focused feature's plate circuit rather than from user input: `get_stage_pole_plate_pair` reads the moving/fixed plate IDs off the relevant `ReconstructionTree::Edge`, `get_stage_pole_location` calls `GPlatesAppLogic::RotationUtils::get_stage_pole` between the reconstruction time and time+1, and rotates the resulting axis into the moving plate's reference frame (the comment block in `get_stage_pole_location` derives why that extra rotation by the fixed plate's absolute rotation is needed). While this mode is active, `can_change_pole` returns false and `pole_location_groupbox`/`vgp_constraints_groupbox` are disabled, since the pole is being driven by the reconstruction rather than by the user; the widget re-derives it on every `set_focus()` and `handle_reconstruction()` signal from `ViewState`.

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

`set_pole` asserts `can_change_pole()` via `PreconditionViolationError` — callers must check `can_change_pole()` (false while the stage-pole constraint is active) before calling it. `react_latitude_spinbox_changed`, `react_longitude_spinbox_changed` and `react_north_pole_pushbutton_clicked` all assert `d_pole` is set (`AssertionFailureException`), since the UI only lets those controls fire while the pole is enabled. When updating the pole from `set_pole_internal`, the enable-checkbox and spinbox signals are temporarily disconnected so that programmatic updates emit `pole_changed` exactly once instead of once per widget touched.

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
