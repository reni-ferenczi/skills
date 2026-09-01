# AnimateControlWidget

[Book TOC](../../TOC.md) · [qt-widgets](../../components/qt-widgets.md) · cluster Community 368 · tier 3

| Source file | Kind | Lines |
|---|---|---|
| `src/qt-widgets/AnimateControlWidget.h` | C++ | 151 |
| `src/qt-widgets/AnimateControlWidget.cc` | C++ | 243 |
| `src/qt-widgets/AnimateControlWidgetUi.ui` | Qt form | 183 |

## Overview

Playback controls for geological time animation. The widget provides play/pause, seek-to-beginning, step-forward/backward buttons and a time slider for navigation within a defined animation time range. It stores a pointer to `AnimationController`, which holds the shared animation state, and responds to controller signals for time changes and animation state transitions. The slider maps between slider units and geological time (Ma). Can be created as a standalone QDockWidget and supports toggling between combined and separate play/pause buttons.

## Declared types

| Name | Kind | Bases | Template | Subclasses | Description |
|---|---|---|---|---|---|
| [`GPlatesQtWidgets::AnimateControlWidget`](#gplatesqtwidgetsanimatecontrolwidget) | class | `QWidget`<br>`Ui_AnimateControlWidget` | — | 0 | This widget resides inside a QDockWidget. |

## Members

### `GPlatesQtWidgets::AnimateControlWidget`

| Member | Kind | Type | Access | Description |
|---|---|---|---|---|
| `create_as_qdockwidget( GPlatesGui::AnimationController &animation_controller)` | method | `QDockWidget` | public | — |
| `AnimateControlWidget( GPlatesGui::AnimationController &animation_controller, QWidget *parent_)` | constructor | `None` | public | — |
| `~AnimateControlWidget()` | destructor | `None` | public | — |
| `use_combined_play_pause_button( bool combined)` | method | `void` | public | Sets whether you want a single button for play and pause (the default), or two separate buttons. |
| `show_step_buttons( bool show_)` | method | `void` | public | Sets whether you want the \<\< / \>\> buttons shown or hidden. |
| `handle_play_or_pause_clicked()` | method | `void` | private | — |
| `handle_seek_beginning_clicked()` | method | `void` | private | — |
| `set_current_time_from_slider( int slider_pos)` | method | `void` | private | — |
| `handle_view_time_changed( double new_time)` | method | `void` | private | — |
| `handle_start_time_changed( double new_time)` | method | `void` | private | — |
| `handle_end_time_changed( double new_time)` | method | `void` | private | — |
| `handle_animation_started()` | method | `void` | private | — |
| `handle_animation_paused()` | method | `void` | private | — |
| `ma_to_slider_units( const double &ma)` | method | `int` | private | — |
| `slider_units_to_ma( const int &slider_pos)` | method | `double` | private | — |
| `recalculate_slider()` | method | `void` | private | — |
| `update_button_states()` | method | `void` | private | — |
| `d_animation_controller_ptr` | field | `GPlatesGui::AnimationController` | private | This is the animation controller, which holds the state of any animation set up in the application. |

## Free functions and macros

| Name | Kind | Type / body | Description |
|---|---|---|---|
| `GPLATES_QTWIDGETS_ANIMATECONTROLWIDGET_H` | macro | `None` | — |

## Notes

The `AnimationController` pointer is not owned; the caller manages its lifetime. The widget is typically added to a QDockWidget that is initially hidden and shown by the application when animation starts.

## Used by

| Unit | Component | References |
|---|---|---|
| [qt-widgets/ReconstructionViewWidget](ReconstructionViewWidget.md) | qt-widgets | 2 |

## Related

**Qt Designer forms**

| Form class | Base widget | Title | Widgets |
|---|---|---|---|
| `AnimateControlWidget` | `QWidget` | Animation Control | 8 |

**Qt signal/slot connections** (12 in this unit)

| Sender | Signal | Receiver | Slot |
|---|---|---|---|
| `button_play` | `clicked()` | `this` | `handle_play_or_pause_clicked()` |
| `button_pause` | `clicked()` | `this` | `handle_play_or_pause_clicked()` |
| `button_play_or_pause` | `clicked()` | `this` | `handle_play_or_pause_clicked()` |
| `button_seek_beginning` | `clicked()` | `this` | `handle_seek_beginning_clicked()` |
| `button_step_backwards` | `clicked()` | `d_animation_controller_ptr` | `step_back()` |
| `button_step_forwards` | `clicked()` | `d_animation_controller_ptr` | `step_forward()` |
| `slider_current_time` | `valueChanged(int)` | `this` | `set_current_time_from_slider(int)` |
| `d_animation_controller_ptr` | `view_time_changed(double)` | `this` | `handle_view_time_changed(double)` |
| `d_animation_controller_ptr` | `start_time_changed(double)` | `this` | `handle_start_time_changed(double)` |
| `d_animation_controller_ptr` | `end_time_changed(double)` | `this` | `handle_end_time_changed(double)` |
| `d_animation_controller_ptr` | `animation_started()` | `this` | `handle_animation_started()` |
| `d_animation_controller_ptr` | `animation_paused()` | `this` | `handle_animation_paused()` |


## Explore

Run these from the `gplates-code` skill directory:

```bash
python scripts/gpq.py file src/qt-widgets/AnimateControlWidget.h
python scripts/gpq.py def GPlatesQtWidgets::AnimateControlWidget --body
python scripts/gpq.py uses AnimateControlWidget --kind class
python scripts/gpq.py hier AnimateControlWidget
```
