# AnimationController

[Book TOC](../../TOC.md) · [gui](../../components/gui.md) · cluster Community 25 · tier 1

| Source file | Kind | Lines |
|---|---|---|
| `src/gui/AnimationController.h` | C++ | 519 |
| `src/gui/AnimationController.cc` | C++ | 708 |

## Overview

`AnimationController` is the single, widget-free home for "what time is the view
showing, and how do we walk it through a range". It exists because at least four
separate pieces of UI — `AnimateDialog`, `AnimateControlWidget`,
`TimeControlWidget` and `ExportAnimationDialog` — all need to read and drive the
same animation settings, and none of them should own that state. `ViewState`
constructs exactly one (`boost::scoped_ptr<AnimationController>
d_animation_controller`) and hands out references through
`get_animation_controller()`; everything else, including the export machinery and
the external-control paths (`ExternalSyncController`, `CommandServer`), talks to
that one instance. The class comment notes it arguably belongs in the
presentation tier — it is a `QObject` purely for signals and slots, with no
widget of its own.

The crucial design decision is that the controller keeps *no copy of the current
time*. `view_time()` reads
`GPlatesAppLogic::ApplicationState::get_current_reconstruction_time()` and
`set_view_time()` writes back through `set_reconstruction_time()`, which
performs a reconstruction. The controller's own `view_time_changed` signal is
emitted only from the `react_view_time_changed` slot, which is wired to
`ApplicationState::reconstruction_time_changed`. So a time change made anywhere —
by the animation timer, by a slider, by a Python script — travels out to
app-logic and comes back through the same signal, and every animation widget
updates identically. `ApplicationState` is the single source of truth for the
time; the controller owns only the *range* (`d_start_time`, `d_end_time`,
`d_time_increment`, `d_frames_per_second`) and the three behaviour flags.

Playback itself is a plain `QTimer` on the GUI event loop: `start_animation_timer`
sets the interval to `1000 / d_frames_per_second`, and each `timeout()` runs
`react_animation_playback_step`, which decides between "step by the increment",
"snap to the end time", "loop back to the start" and "stop". Everything about
*frame arithmetic*, however, is delegated to
`GPlatesUtils::AnimationSequence::calculate_sequence()` — the shared helper whose
whole point (per its own namespace comment) is that
`ExportTemplateFilenameSequence` and this class must agree on frame counts.
`duration_in_frames`, `duration_in_ma`, `ending_frame_time`,
`calculate_time_for_frame` and `get_sequence` are all thin wrappers over it.
That is why `ExportAnimationContext` can snapshot a `SequenceInfo` once at
construction and then drive frames by calling `set_view_time()` directly,
bypassing the timer entirely.

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

**Start may be later or earlier than end.** This is the invariant most new code
gets wrong. `d_start_time > d_end_time` is perfectly legal — it just means the
animation runs forwards in real time. `d_time_increment` therefore carries a
sign, maintained by `recalculate_increment()` (called from `play()`,
`set_start_time()` and `set_end_time()`), while `time_increment()` returns
`fabs()` of it for the UI. Read `raw_time_increment()` if you are doing
arithmetic and `time_increment()` if you are showing a number. Note also that
`recalculate_increment()` deliberately does *not* emit `time_increment_changed`,
on the reasoning that only the sign changed — so a widget that caches the raw
increment will go stale after a range edit.

**Playing state lives in the timer.** `is_playing()` is just
`d_timer.isActive()`; there is no separate flag to fall out of sync. Both
`start_animation_timer()` and `stop_animation_timer()` emit unconditionally, so
calling `pause()` when already paused still fires `animation_paused()` and
`animation_state_changed(false)`. `play()`, by contrast, returns early when
already playing, and also silently does nothing when the increment exceeds the
total range — a "nothing happened" case with no signal and no diagnostic.

**Each frame is a synchronous reconstruction.** `set_view_time()` calls
`ApplicationState::set_reconstruction_time()` on the GUI thread, so the requested
frames-per-second is only an upper bound; with a heavy layer graph the timer
simply falls behind. There is no threading here at all — the whole class assumes
the Qt main thread.

**Feedback loops are real but bounded.** `react_view_time_changed` calls
`ensure_bounds_contain_current_time()` when
`d_adjust_bounds_to_contain_current_time` is set, which can call
`set_start_time`/`set_end_time` and hence `recalculate_increment()` — so simply
scrubbing the time can move the animation range under a dialog's feet. The
converse path, `ensure_current_time_lies_within_bounds()`, changes the view time
and so re-enters via the signal; it terminates because the second pass finds the
time already inside the bounds. `swap_start_and_end_times()` exists solely to
dodge one of these loops: it first sets both endpoints to the current time so the
intermediate state cannot trigger a clamp, then assigns the swapped values. Both
it and `ensure_current_time_lies_within_bounds` carry FIXMEs and are the fragile
part of this file.

Smaller traps:

- `set_view_time()` silently ignores any time failing `is_valid_reconstruction_time`
  (outside 0–10000 Ma) and, separately, ignores changes smaller than
  `GPlatesMaths::are_geo_times_approximately_equal` — so no signal is emitted for
  sub-epsilon steps. `is_valid_reconstruction_time` itself has a copy-paste bug:
  the upper-bound branch compares against `min_reconstruction_time()` rather than
  `max_reconstruction_time()`. It is harmless today only because no time can be
  both above 10000 and approximately 0.
- `step_forward()` and `step_back()` clamp the result at 0.0 rather than at the
  animation bounds, so stepping cannot walk into negative (future) times even
  when the range would allow it.
- `calculate_sequence()` throws `AnimationSequence::TimeIncrementZero` on a zero
  increment, and every accessor here (`duration_in_frames`, `get_sequence`,
  `ending_frame_time`, `calculate_time_for_frame`) calls it. None of them guard,
  so a zero increment turns ordinary-looking getters into throwing calls.
- Those same accessors each recompute the whole sequence from scratch. Calling
  `calculate_time_for_frame()` in a loop is quadratic-ish; grab one `SequenceInfo`
  from `get_sequence()` and use `GPlatesUtils::AnimationSequence::calculate_time_for_frame`
  on it, as `ExportAnimationContext` does.
- `init_default_time_range()` is not called by the constructor. Constructor
  defaults are 250 → 0 Ma at 1 Ma and 5 fps; the `UserPreferences` keys
  (`view/animation/default_time_range_*`) are only applied when a caller invokes
  it, and doing so also resets the reconstruction time to `end_time()`.
- `duration_in_frames()` still carries a large `#if 0` block of the original
  hand-rolled frame arithmetic, kept for its commentary on the floating-point
  fencepost cases. It is dead; the live answer comes from `calculate_sequence`.

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
