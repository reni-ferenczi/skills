# EventBlackout

[Book TOC](../../TOC.md) · [gui](../../components/gui.md) · cluster Community 1142 · tier 2

| Source file | Kind | Lines |
|---|---|---|
| `src/gui/EventBlackout.h` | C++ | 104 |
| `src/gui/EventBlackout.cc` | C++ | 172 |

## Overview

[[[PROSE overview unit=gui/EventBlackout tier=2]]]
Replace this whole block, markers included, with 1-3 paragraphs: what this unit is, why it exists, and how it fits the surrounding design. Do not restate the tables below.
[[[/PROSE]]]

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

[[[PROSE notes unit=gui/EventBlackout tier=2]]]
Replace this whole block, markers included, with invariants, ownership, threading or gotchas that are not visible in the tables. Write *None.* if there is nothing worth saying.
[[[/PROSE]]]

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
