# TimeControlWidget

[Book TOC](../../TOC.md) · [qt-widgets](../../components/qt-widgets.md) · cluster Community 1338 · tier 3

| Source file | Kind | Lines |
|---|---|---|
| `src/qt-widgets/TimeControlWidget.h` | C++ | 125 |
| `src/qt-widgets/TimeControlWidget.cc` | C++ | 134 |
| `src/qt-widgets/TimeControlWidgetUi.ui` | Qt form | 133 |

## Overview

[[[PROSE overview unit=qt-widgets/TimeControlWidget tier=3]]]
Replace this whole block, markers included, with 1-3 paragraphs: what this unit is, why it exists, and how it fits the surrounding design. Do not restate the tables below.
[[[/PROSE]]]

## Declared types

| Name | Kind | Bases | Template | Subclasses | Description |
|---|---|---|---|---|---|
| [`GPlatesQtWidgets::TimeControlWidget`](#gplatesqtwidgetstimecontrolwidget) | class | `QWidget`<br>`Ui_TimeControlWidget` | — | 0 | This widget resides inside the AwesomeBar at the top of the ReconstructionViewWidget. |

## Members

### `GPlatesQtWidgets::TimeControlWidget`

| Member | Kind | Type | Access | Description |
|---|---|---|---|---|
| `create_as_qdockwidget( GPlatesGui::AnimationController &animation_controller)` | method | `QDockWidget` | public | — |
| `TimeControlWidget( GPlatesGui::AnimationController &animation_controller, QWidget *parent_)` | constructor | `None` | public | — |
| `~TimeControlWidget()` | destructor | `None` | public | — |
| `editing_finished()` | method | `void` | public | Emitted when the user has entered a new time value in the spinbox. |
| `activate_time_spinbox()` | method | `void` | public | Focuses the spinbox and highlights text, ready to be replaced. |
| `show_step_buttons( bool show_)` | method | `void` | public | Sets whether you want the \<\< / \>\> buttons shown or hidden. |
| `show_label( bool show_)` | method | `void` | public | Sets whether you want the "Time:" label shown or hidden. |
| `handle_time_spinbox_editing_finished()` | method | `void` | private | — |
| `handle_view_time_changed( double new_time)` | method | `void` | private | — |
| `d_animation_controller_ptr` | field | `GPlatesGui::AnimationController` | private | This is the animation controller, which holds the state of any animation set up in the application. |

## Free functions and macros

| Name | Kind | Type / body | Description |
|---|---|---|---|
| `GPLATES_QTWIDGETS_TIMECONTROLWIDGET_H` | macro | `None` | — |

## Notes

[[[PROSE notes unit=qt-widgets/TimeControlWidget tier=3]]]
Replace this whole block, markers included, with invariants, ownership, threading or gotchas that are not visible in the tables. Write *None.* if there is nothing worth saying.
[[[/PROSE]]]

## Used by

| Unit | Component | References |
|---|---|---|
| [qt-widgets/ReconstructionViewWidget](ReconstructionViewWidget.md) | qt-widgets | 1 |

## Related

**Qt Designer forms**

| Form class | Base widget | Title | Widgets |
|---|---|---|---|
| `TimeControlWidget` | `QWidget` | Form | 6 |

**Qt signal/slot connections** (4 in this unit)

| Sender | Signal | Receiver | Slot |
|---|---|---|---|
| `button_reconstruction_increment` | `clicked()` | `d_animation_controller_ptr` | `step_back()` |
| `button_reconstruction_decrement` | `clicked()` | `d_animation_controller_ptr` | `step_forward()` |
| `spinbox_current_time` | `editingFinished()` | `this` | `handle_time_spinbox_editing_finished()` |
| `d_animation_controller_ptr` | `view_time_changed(double)` | `this` | `handle_view_time_changed(double)` |


## Explore

Run these from the `gplates-code` skill directory:

```bash
python scripts/gpq.py file src/qt-widgets/TimeControlWidget.h
python scripts/gpq.py def GPlatesQtWidgets::TimeControlWidget --body
python scripts/gpq.py uses TimeControlWidget --kind class
python scripts/gpq.py hier TimeControlWidget
```
