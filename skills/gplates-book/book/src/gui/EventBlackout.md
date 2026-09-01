# EventBlackout

[Book TOC](../../TOC.md) · [gui](../../components/gui.md) · cluster Community 1142 · tier 2

| Source file | Kind | Lines |
|---|---|---|
| `src/gui/EventBlackout.h` | C++ | 104 |
| `src/gui/EventBlackout.cc` | C++ | 172 |

## Overview

`EventBlackout` installs itself as an application-wide `QObject::eventFilter` (via `start()`/`stop()` on `qApp`) to suppress user interaction while Python code is executing, since the GPlates model is single-threaded and cannot safely tolerate the user modifying it concurrently through the GUI. `eventFilter()` discards every event except: the fixed `PERMITTED_EVENTS` allowlist (layout, paint, resize, timer, and similar events needed to keep widgets visually responsive, plus anything at or above `QEvent::User`), events destined for a widget explicitly exempted via `add_blackout_exemption()` (checked through `is_ancestor()`, so exempting a widget also exempts its children), and the Ctrl+C key combination, which is let through unconditionally so the user can still interrupt a running Python script.

The header's own comment on `is_permitted_while_monitoring()` doubles as the extension point: if a widget stops refreshing correctly during Python execution, the fix is to add the missing `QEvent::Type` to `PERMITTED_EVENTS`, taking care not to permit anything that would let the user click or type through to model-mutating code.

## Declared types

| Name | Kind | Bases | Template | Subclasses | Description |
|---|---|---|---|---|---|
| [`GPlatesGui::EventBlackout`](#gplatesguieventblackout) | class | `QObject` | — | 0 | EventBlackout, when enabled, discards all events other than those necessary for refreshing the user interface. |

## Members

### `GPlatesGui::EventBlackout`

| Member | Kind | Type | Access | Description |
|---|---|---|---|---|
| `EventBlackout()` | constructor | `None` | public | — |
| `start()` | method | `void` | public | Begins the event blackout. |
| `stop()` | method | `void` | public | Ends the event blackout. |
| `add_blackout_exemption( QWidget *widget)` | method | `void` | public | Exempt widget from the event blackout. |
| `remove_blackout_exemption( QWidget *widget)` | method | `void` | public | Removes widget from event blackout exemption. |
| `has_started()` | method | `bool` | public | Returns whether the event blackout is in force. |
| `eventFilter( QObject *obj, QEvent *ev)` | method | `bool` | protected | — |
| `d_has_started` | field | `bool` | private | — |
| `d_exempt_widgets` | field | `std::set<QWidget *>` | private | — |

## Free functions and macros

| Name | Kind | Type / body | Description |
|---|---|---|---|
| `PERMITTED_EVENTS` | variable | `QEvent::Type` | — |
| `NUM_PERMITTED_EVENTS` | variable | `std::size_t` | — |
| `PERMITTED_EVENTS_END` | variable | `QEvent::Type` | — |
| `is_permitted_while_monitoring( QEvent::Type type)` | function | `bool` | Basically, we want to block all user interaction while ensuring that the UI can refresh itself (e.g. when Python prints something out). |
| `is_ancestor( QWidget *widget, QObject *obj)` | function | `bool` | — |
| `is_exempt( QObject *obj, const std::set<QWidget *> &exempt_widgets)` | function | `bool` | — |
| `is_control_c( QEvent *ev)` | function | `bool` | — |
| `GPLATES_GUI_EVENTBLACKOUT_H` | macro | `None` | — |

## Notes

`start()`/`stop()` install and remove the filter on the global `qApp` instance, so a blackout is application-wide, not scoped to one window; forgetting to pair a `start()` with a `stop()` freezes all user interaction in the whole application, not just the widget that triggered it. Exemptions are tracked by raw `QWidget*` in a `std::set` with no ownership or destruction tracking — a widget destroyed while still listed in `d_exempt_widgets` leaves a dangling pointer that `is_ancestor()` will still compare against (though never dereference beyond the identity check) until explicitly removed via `remove_blackout_exemption()`.

## Used by

| Unit | Component | References |
|---|---|---|
| [gui/PythonManager](PythonManager.md) | gui | 11 |
| [api/PythonUtils](../api/PythonUtils.md) | api | 2 |
| [qt-widgets/PythonInitFailedDialog](../qt-widgets/PythonInitFailedDialog.md) | qt-widgets | 2 |
| [qt-widgets/PythonConsoleDialog](../qt-widgets/PythonConsoleDialog.md) | qt-widgets | 1 |

## Related

*None.*

## Explore

Run these from the `gplates-code` skill directory:

```bash
python scripts/gpq.py file src/gui/EventBlackout.h
python scripts/gpq.py def GPlatesGui::EventBlackout --body
python scripts/gpq.py uses EventBlackout --kind class
python scripts/gpq.py hier EventBlackout
```
