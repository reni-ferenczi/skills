# AnimateDialog

[Book TOC](../../TOC.md) · [qt-widgets](../../components/qt-widgets.md) · cluster Community 759 · tier 3

| Source file | Kind | Lines |
|---|---|---|
| `src/qt-widgets/AnimateDialog.h` | C++ | 160 |
| `src/qt-widgets/AnimateDialog.cc` | C++ | 324 |
| `src/qt-widgets/AnimateDialogUi.ui` | Qt form | 489 |

## Overview

Configuration dialog for geological time animations. Provides spinboxes for start time, end time, time increment, and current time, plus a time slider for scrubbing. Buttons allow setting animation bounds from the current view time, reversing the animation, and toggling playback. Checkboxes control whether animation loops and whether it finishes exactly on the end time; a spinbox sets frames per second. Communicates bidirectionally with `AnimationController` to read and write all animation parameters, sharing control with `AnimateControlWidget`.

## Declared types

| Name | Kind | Bases | Template | Subclasses | Description |
|---|---|---|---|---|---|
| [`GPlatesQtWidgets::AnimateDialog`](#gplatesqtwidgetsanimatedialog) | class | [`GPlatesDialog`](GPlatesDialog.md)<br>`Ui_AnimateDialog` | — | 0 | — |

## Members

### `GPlatesQtWidgets::AnimateDialog`

| Member | Kind | Type | Access | Description |
|---|---|---|---|---|
| `AnimateDialog( GPlatesGui::AnimationController &animation_controller, QWidget *parent_ = NULL)` | constructor | `None` | public | — |
| `~AnimateDialog()` | destructor | `None` | public | — |
| `view_time` | field | `double` | public | — |
| `set_start_time_value_to_view_time()` | method | `void` | public | — |
| `set_end_time_value_to_view_time()` | method | `void` | public | — |
| `toggle_animation_playback_state()` | method | `void` | public | — |
| `rewind()` | method | `void` | public | — |
| `current_time_changed( double new_value)` | method | `void` | public | — |
| `react_start_time_spinbox_changed( double new_val)` | method | `void` | private | — |
| `react_end_time_spinbox_changed( double new_val)` | method | `void` | private | — |
| `react_time_increment_spinbox_changed( double new_val)` | method | `void` | private | — |
| `react_current_time_spinbox_changed( double new_val)` | method | `void` | private | — |
| `handle_start_time_changed( double new_val)` | method | `void` | private | — |
| `handle_end_time_changed( double new_val)` | method | `void` | private | — |
| `handle_time_increment_changed( double new_val)` | method | `void` | private | — |
| `handle_current_time_changed( double new_val)` | method | `void` | private | — |
| `handle_options_changed()` | method | `void` | private | (Re)sets checkboxes according to animation controller state. |
| `handle_animation_started()` | method | `void` | private | — |
| `handle_animation_paused()` | method | `void` | private | — |
| `set_current_time_from_slider( int slider_pos)` | method | `void` | private | — |
| `d_animation_controller_ptr` | field | `GPlatesGui::AnimationController` | private | This is the animation controller, which holds the state of any animation set up in the application. |
| `set_start_button_state( bool animation_is_playing)` | method | `void` | private | Updates button label & icon. |
| `ma_to_slider_units( const double &ma)` | method | `int` | private | — |
| `slider_units_to_ma( const int &slider_pos)` | method | `double` | private | — |
| `recalculate_slider()` | method | `void` | private | — |

## Free functions and macros

| Name | Kind | Type / body | Description |
|---|---|---|---|
| `GPLATES_QTWIDGETS_ANIMATEDIALOG_H` | macro | `None` | — |

## Notes

The `AnimationController` pointer is not owned; the caller manages its lifetime. The dialog emits `current_time_changed(double)` when the user modifies time through the UI, broadcasting changes to other components.

## Used by

| Unit | Component | References |
|---|---|---|
| [gui/Dialogs](../gui/Dialogs.md) | gui | 1 |

## Related

**Qt Designer forms**

| Form class | Base widget | Title | Widgets |
|---|---|---|---|
| `AnimateDialog` | `QDialog` | Configure Animation | 30 |

**Qt signal/slot connections** (22 in this unit)

| Sender | Signal | Receiver | Slot |
|---|---|---|---|
| `button_Use_View_Time_start_time` | `clicked()` | `this` | `set_start_time_value_to_view_time()` |
| `button_Use_View_Time_end_time` | `clicked()` | `this` | `set_end_time_value_to_view_time()` |
| `widget_start_time` | `valueChanged(double)` | `this` | `react_start_time_spinbox_changed(double)` |
| `widget_end_time` | `valueChanged(double)` | `this` | `react_end_time_spinbox_changed(double)` |
| `widget_time_increment` | `valueChanged(double)` | `this` | `react_time_increment_spinbox_changed(double)` |
| `widget_current_time` | `valueChanged(double)` | `this` | `react_current_time_spinbox_changed(double)` |
| `button_Reverse_the_Animation` | `clicked()` | `d_animation_controller_ptr` | `swap_start_and_end_times()` |
| `slider_current_time` | `valueChanged(int)` | `this` | `set_current_time_from_slider(int)` |
| `button_Start` | `clicked()` | `this` | `toggle_animation_playback_state()` |
| `button_Rewind` | `clicked()` | `this` | `rewind()` |
| `widget_Frames_per_second` | `valueChanged(double)` | `d_animation_controller_ptr` | `set_frames_per_second(double)` |
| `checkbox_Finish_animation_on_end_time` | `clicked(bool)` | `d_animation_controller_ptr` | `set_should_finish_exactly_on_end_time(bool)` |
| `checkbox_Loop` | `clicked(bool)` | `d_animation_controller_ptr` | `set_should_loop(bool)` |
| `d_animation_controller_ptr` | `view_time_changed(double)` | `this` | `handle_current_time_changed(double)` |
| `d_animation_controller_ptr` | `start_time_changed(double)` | `this` | `handle_start_time_changed(double)` |

*... and 7 more connections.*


## Explore

Run these from the `gplates-code` skill directory:

```bash
python scripts/gpq.py file src/qt-widgets/AnimateDialog.h
python scripts/gpq.py def GPlatesQtWidgets::AnimateDialog --body
python scripts/gpq.py uses AnimateDialog --kind class
python scripts/gpq.py hier AnimateDialog
```
