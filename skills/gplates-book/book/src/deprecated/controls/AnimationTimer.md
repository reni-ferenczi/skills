# AnimationTimer

[Book TOC](../../../TOC.md) · [deprecated](../../../components/deprecated.md) · cluster Community 365 · tier 3 · **deprecated**

| Source file | Kind | Lines |
|---|---|---|
| `src/deprecated/controls/AnimationTimer.h` | C++ | 178 |
| `src/deprecated/controls/AnimationTimer.cc` | C++ | 182 |

## Overview

A singleton wxTimer subclass that manages frame-by-frame playback of geological-time animations. On each timer tick, it invokes a caller-provided warp function to update the display at the next animation frame, stepping through geological time in configurable increments. The timer supports both forward and backward playback and can be stopped or restarted at any point during animation.

`AnimationTimer` coordinates with `GuiCalls` to manage the application's operational mode when animation is active and to handle graceful termination if an exception occurs during playback—which is critical since `Notify()` runs in wxWindows' event loop and cannot propagate exceptions normally.

## Declared types

| Name | Kind | Bases | Template | Subclasses | Description |
|---|---|---|---|---|---|
| [`GPlatesControls::AnimationTimer`](#gplatescontrolsanimationtimer) | class | `wxTimer` | — | 0 | An animation-timer controls the rate of execution of an animation. |

## Members

### `GPlatesControls::AnimationTimer`

| Member | Kind | Type | Access | Description |
|---|---|---|---|---|
| `StartNew(WarpFn warp_to_time, GPlatesGlobal::fpdata_t start_time, GPlatesGlobal::fpdata_t end_time, GPlatesGlobal::fpdata_t time_delta, bool finish_on_end, int milli_secs)` | method | `bool` | public | Create a new singleton animation-timer instance and start it running. |
| `exists()` | method | `bool` | public | Return whether a singleton instance exists. |
| `isRunning()` | method | `bool` | public | Return whether an animation is currently in progress. |
| `RestartTimer(int milli_secs)` | method | `bool` | public | Restart the animation-timer. |
| `StopTimer()` | method | `void` | public | Stop the animation timer. |
| `Notify()` | method | `void` | public | The virtual function which is invoked by wxWindows to perform each update. |
| `_instance` | field | `AnimationTimer` | private | The singleton instance. |
| `AnimationTimer(WarpFn warp_to_time, GPlatesGlobal::fpdata_t start_time, GPlatesGlobal::fpdata_t end_time, GPlatesGlobal::fpdata_t time_delta, bool finish_on_end)` | constructor | `None` | private | A private constructor to ensure the singleton invariant. |
| `_warp_to_time` | field | `WarpFn` | private | A pointer to the function which will be invoked to update the screen during the course of the animation. |
| `_curr_t` | field | `GPlatesMaths::real_t` | private | — |
| `_end_t` | field | `GPlatesMaths::real_t` | private | — |
| `_time_delta` | field | `GPlatesMaths::real_t` | private | — |
| `_finish_on_end` | field | `bool` | private | — |
| `_sense` | field | `GPlatesMaths::real_t` | private | — |

## Free functions and macros

| Name | Kind | Type / body | Description |
|---|---|---|---|
| `_instance` | variable | `GPlatesControls::AnimationTimer` | — |
| `_GPLATES_CONTROLS_ANIMATIONTIMER_H_` | macro | `None` | — |

## Notes

The singleton pattern and static member data expose threading hazards: the class is not thread-safe and will fail if threading is introduced or if multiple main windows exist. The `Notify()` override catches all `GPlatesGlobal::Exception` objects and terminates the program via `Lifetime::instance()->terminate()` because exceptions cannot propagate from wxWindows timer callbacks. Animation direction (forward or backward) is determined at construction based on the relationship between start and end times and is tracked in the `_sense` field.

## Used by

| Unit | Component | References |
|---|---|---|
| [gui/deprecated/MainWindow](../../gui/deprecated/MainWindow.md) | gui | 14 |
| [deprecated/controls/Reconstruct](Reconstruct.md) | deprecated | 3 |

## Related

*None.*

## Explore

Run these from the `gplates-code` skill directory:

```bash
python scripts/gpq.py file src/deprecated/controls/AnimationTimer.h
python scripts/gpq.py def GPlatesControls::AnimationTimer --body
python scripts/gpq.py uses AnimationTimer --kind class
python scripts/gpq.py hier AnimationTimer
```
