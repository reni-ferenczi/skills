# AnimationController

[Book TOC](../../TOC.md) · [gui](../../components/gui.md) · cluster Community 25 · tier 1

| Source file | Kind | Lines |
|---|---|---|
| `src/gui/AnimationController.h` | C++ | 519 |
| `src/gui/AnimationController.cc` | C++ | 708 |

## Overview

[[[PROSE overview unit=gui/AnimationController tier=1]]]
Replace this whole block, markers included, with 1-3 paragraphs: what this unit is, why it exists, and how it fits the surrounding design. Do not restate the tables below.
[[[/PROSE]]]

## Declared types

| Name | Kind | Bases | Template | Subclasses | Description |
|---|---|---|---|---|---|
| [`GPlatesGui::AnimationController`](#gplatesguianimationcontroller) | class | `QObject` | — | 0 | The behind-the-scenes logic for the AnimateDialog and AnimateControlWidget. |

## Members

### `GPlatesGui::AnimationController`

| Member | Kind | Type | Access | Description |
|---|---|---|---|---|
| `frame_index_type` | typedef | `long` | public | Typedef for frame index numbers used by set\_view\_frame() etc. |
| `AnimationController( GPlatesAppLogic::ApplicationState &application_state)` | constructor | `None` | public | — |
| `~AnimationController()` | destructor | `None` | public | — |
| `init_default_time_range()` | method | `void` | public | Sets the start, end, and time increment based on the user's preferences. |
| `view_time` | field | `double` | public | Returns the current reconstruction time the View is looking at. |
| `start_time` | field | `double` | public | The time that the animation should begin at. |
| `end_time` | field | `double` | public | The time that the animation should end at. |
| `time_increment()` | method | `double` | public | Returns the user-friendly 'increment' value, which will always be a positive number. |
| `raw_time_increment()` | method | `double` | public | Returns the actual 'increment' value which needs to be applied to move from start\_time() to end\_time(). |
| `is_playing()` | method | `bool` | public | — |
| `frames_per_second` | field | `double` | public | — |
| `duration_in_frames()` | method | `frame_index_type` | public | Returns the number of frames between start\_time() and end\_time(). |
| `duration_in_ma()` | method | `double` | public | Returns the distance between start\_time() and whatever time we would finish on if we counted duration\_in\_frame from the start. |
| `starting_frame_time()` | method | `double` | public | Returns the time that the first frame of animation will use. |
| `ending_frame_time()` | method | `double` | public | Returns the time that the last frame of animation will use. |
| `calculate_time_for_frame( GPlatesGui::AnimationController::frame_index_type frame)` | method | `double` | public | Given the currently-configured range and increment, plus a target frame number, calculates what reconstruction time will correspond to the given frame. if we should\_finish\_exactly\_on\_end\_time() and the animation duration does not divide ... |
| `get_sequence()` | method | `GPlatesUtils::AnimationSequence::SequenceInfo` | public | Returns complete information about the configured animation sequence. |
| `should_finish_exactly_on_end_time()` | method | `bool` | public | — |
| `should_loop()` | method | `bool` | public | — |
| `should_adjust_bounds_to_contain_current_time()` | method | `bool` | public | — |
| `min_reconstruction_time()` | method | `double` | public | — |
| `max_reconstruction_time()` | method | `double` | public | — |
| `is_valid_reconstruction_time( const double &time)` | method | `bool` | public | — |
| `play()` | method | `void` | public | Initiates the animation. |
| `pause()` | method | `void` | public | Ceases animation. |
| `set_play_or_pause( bool lets_play)` | method | `void` | public | Convenience function to call play() or pause() depending on bool. |
| `step_forward()` | method | `void` | public | Increments or decrements the view time so as to progress forwards through the animation by one time\_increment(). |
| `step_back()` | method | `void` | public | Increments or decrements the view time so as to progress backwards through the animation by one time\_increment(). |
| `seek_beginning()` | method | `void` | public | Moves the view time to match the animation's start time. |
| `seek_end()` | method | `void` | public | Moves the view time to match the animation's end time. |
| `set_view_time( const double new_time)` | method | `void` | public | Modifies the view time as requested by a dialog's widget such as a slider or part of the animation process and ensures signals are emitted to the Qt dialogs and widgets accordingly. |
| `set_view_frame( GPlatesGui::AnimationController::frame_index_type frame)` | method | `void` | public | Modifies the view time to correspond to the given frame of animation; frame 0 is the same as start\_time(), and subsequent frame numbers are incremented to approach end\_time(). if we should\_finish\_exactly\_on\_end\_time() and the animation ... |
| `set_start_time( const double new_time)` | method | `void` | public | — |
| `set_end_time( const double new_time)` | method | `void` | public | — |
| `set_time_increment( const double new_abs_increment)` | method | `void` | public | Sets the geological time increment between frames. |
| `set_frames_per_second( const double fps)` | method | `void` | public | — |
| `set_should_finish_exactly_on_end_time( bool finish_exactly)` | method | `void` | public | — |
| `set_should_loop( bool loop)` | method | `void` | public | — |
| `set_should_adjust_bounds_to_contain_current_time( bool adjust_bounds)` | method | `void` | public | — |
| `ensure_current_time_lies_within_bounds()` | method | `void` | public | FIXME: Should this really be public and dialog-called, or should it be private and inscrutable? |
| `ensure_bounds_contain_current_time()` | method | `void` | public | Modify the boundary times, if necessary, to ensure that they contain the current time. |
| `swap_start_and_end_times()` | method | `void` | public | — |
| `view_time_changed( double new_time)` | method | `void` | public | — |
| `start_time_changed( double new_time)` | method | `void` | public | — |
| `end_time_changed( double new_time)` | method | `void` | public | — |
| `time_increment_changed( double new_increment)` | method | `void` | public | — |
| `frames_per_second_changed( double fps)` | method | `void` | public | — |
| `finish_exactly_on_end_time_changed( bool finish_exactly_on_end_time)` | method | `void` | public | — |
| `should_loop_changed( bool should_loop)` | method | `void` | public | — |
| `should_adjust_bounds_to_contain_current_time_changed( bool adjust_bounds)` | method | `void` | public | — |
| `animation_started()` | method | `void` | public | — |
| `animation_paused()` | method | `void` | public | — |
| `animation_state_changed( bool is_playing)` | method | `void` | public | Convenience signal which is emitted at the same time that animation\_started() and animation\_paused() are, to aid signal/slot connections that would ideally like a bool. |
| `react_animation_playback_step()` | method | `void` | private | Triggered whenever the internal QTimer ticks. |
| `react_view_time_changed( GPlatesAppLogic::ApplicationState &application_state)` | method | `void` | private | Triggered whenever the view time changes, either by our animation or by the user from the time-control buttons. |
| `d_application_state_ptr` | field | `GPlatesAppLogic::ApplicationState` | private | This performs the reconstructions and is used to query and modify the current reconstruction time. |
| `d_timer` | field | `QTimer` | private | This QTimer instance triggers the frame updates during animation playback. |
| `d_start_time` | field | `double` | private | This is the starting time of the animation. |
| `d_end_time` | field | `double` | private | This is the ending time of the animation. |
| `d_time_increment` | field | `double` | private | This is the increment applied to the current time in successive frames of the animation. |
| `d_frames_per_second` | field | `double` | private | This is the number of frames to display per second. |
| `d_finish_exactly_on_end_time` | field | `bool` | private | This option controls whether animations whose duration is not an exact multiple of the increment should end their animation on the last valid time-step, or jump directly to the specified end time at the conclusion of the animation. |
| `d_loop` | field | `bool` | private | This option controls whether animations should loop or simply stop once they reach the end time. |
| `d_adjust_bounds_to_contain_current_time` | field | `bool` | private | This option controls whether start and end times should be adjusted to contain the current time whenever the current time lies outside the bounds. |
| `start_animation_timer()` | method | `void` | private | Does the work of configuring and starting the timer, beginning the animation and emitting an appropriate signal. |
| `stop_animation_timer()` | method | `void` | private | Stops the timer, pausing the animation and emitting an appropriate signal. |
| `recalculate_increment()` | method | `void` | private | Double-checks the value of the member datum d\_time\_increment. |

## Free functions and macros

| Name | Kind | Type / body | Description |
|---|---|---|---|
| `GPLATES_GUI_ANIMATIONCONTROLLER_H` | macro | `None` | — |

## Notes

[[[PROSE notes unit=gui/AnimationController tier=1]]]
Replace this whole block, markers included, with invariants, ownership, threading or gotchas that are not visible in the tables. Write *None.* if there is nothing worth saying.
[[[/PROSE]]]

## Used by

| Unit | Component | References |
|---|---|---|
| [presentation/ViewState](../presentation/ViewState.md) | presentation | 66 |
| [qt-widgets/ViewportWindow](../qt-widgets/ViewportWindow.md) | qt-widgets | 55 |
| [gui/ExternalSyncController](ExternalSyncController.md) | gui | 42 |
| [gui/CommandServer](CommandServer.md) | gui | 35 |
| [qt-widgets/ExportAnimationDialog](../qt-widgets/ExportAnimationDialog.md) | qt-widgets | 31 |
| [qt-widgets/AnimateDialog](../qt-widgets/AnimateDialog.md) | qt-widgets | 29 |
| [qt-widgets/KinematicGraphsDialog](../qt-widgets/KinematicGraphsDialog.md) | qt-widgets | 20 |
| [gui/ExportAnimationContext](ExportAnimationContext.md) | gui | 19 |
| [gui/ExportRasterAnimationStrategy](ExportRasterAnimationStrategy.md) | gui | 19 |
| [qt-widgets/AnimateControlWidget](../qt-widgets/AnimateControlWidget.md) | qt-widgets | 18 |
| [gui/ExportVelocityAnimationStrategy](ExportVelocityAnimationStrategy.md) | gui | 17 |
| [gui/ExportAnimationStrategy](ExportAnimationStrategy.md) | gui | 11 |
| [gui/ExportCitcomsResolvedTopologyAnimationStrategy](ExportCitcomsResolvedTopologyAnimationStrategy.md) | gui | 8 |
| [gui/ExportStageRotationAnimationStrategy](ExportStageRotationAnimationStrategy.md) | gui | 8 |
| [qt-widgets/TimeControlWidget](../qt-widgets/TimeControlWidget.md) | qt-widgets | 8 |
| [gui/ExportDeformationAnimationStrategy](ExportDeformationAnimationStrategy.md) | gui | 7 |
| [gui/ExportFlowlineAnimationStrategy](ExportFlowlineAnimationStrategy.md) | gui | 7 |
| [gui/ExportMotionPathAnimationStrategy](ExportMotionPathAnimationStrategy.md) | gui | 7 |
| [gui/ExportScalarCoverageAnimationStrategy](ExportScalarCoverageAnimationStrategy.md) | gui | 7 |
| [presentation/TranscribeSession](../presentation/TranscribeSession.md) | presentation | 7 |

*... and 9 more units.*

## Related

**Qt signal/slot connections** (2 in this unit)

| Sender | Signal | Receiver | Slot |
|---|---|---|---|
| `&d_timer` | `timeout()` | `this` | `react_animation_playback_step()` |
| `d_application_state_ptr` | `reconstruction_time_changed(GPlatesAppLogic::ApplicationState &, const double &)` | `this` | `react_view_time_changed(GPlatesAppLogic::ApplicationState &)` |


## Explore

Run these from the `gplates-code` skill directory:

```bash
python scripts/gpq.py file src/gui/AnimationController.h
python scripts/gpq.py def GPlatesGui::AnimationController --body
python scripts/gpq.py uses AnimationController --kind class
python scripts/gpq.py hier AnimationController
```
