# Sleeper

[Book TOC](../../TOC.md) · [api](../../components/api.md) · cluster Community 59 · tier 3

| Source file | Kind | Lines |
|---|---|---|
| `src/api/Sleeper.h` | C++ | 55 |
| `src/api/Sleeper.cc` | C++ | 82 |

## Overview

[[[PROSE overview unit=api/Sleeper tier=3]]]
Replace this whole block, markers included, with 1-3 paragraphs: what this unit is, why it exists, and how it fits the surrounding design. Do not restate the tables below.
[[[/PROSE]]]

## Declared types

| Name | Kind | Bases | Template | Subclasses | Description |
|---|---|---|---|---|---|
| [`GPlatesApi::Sleeper`](#gplatesapisleeper) | class | — | — | 0 | On construction, replaces Python's time.sleep with our own functor and on destruction restores the original time.sleep. |

## Members

### `GPlatesApi::Sleeper`

| Member | Kind | Type | Access | Description |
|---|---|---|---|---|
| `Sleeper()` | constructor | `None` | public | — |
| `~Sleeper()` | destructor | `None` | public | — |
| `d_old_object` | field | `boost::python::object` | private | — |

## Free functions and macros

| Name | Kind | Type / body | Description |
|---|---|---|---|
| `GPLATES_API_SLEEPER_H` | macro | `None` | — |

## Notes

[[[PROSE notes unit=api/Sleeper tier=3]]]
Replace this whole block, markers included, with invariants, ownership, threading or gotchas that are not visible in the tables. Write *None.* if there is nothing worth saying.
[[[/PROSE]]]

## Used by

| Unit | Component | References |
|---|---|---|
| [gui/UtilitiesMenu](../gui/UtilitiesMenu.md) | gui | 2 |
| [qt-widgets/PythonConsoleDialog](../qt-widgets/PythonConsoleDialog.md) | qt-widgets | 2 |
| [api/PyApplication](PyApplication.md) | api | 1 |
| [api/PythonExecutionThread](PythonExecutionThread.md) | api | 1 |
| [api/PythonRunner](PythonRunner.md) | api | 1 |
| [entry-points/gplates_main](../entry-points/gplates_main.md) | entry-points | 1 |
| [gui/PythonManager](../gui/PythonManager.md) | gui | 1 |
| [presentation/ViewState](../presentation/ViewState.md) | presentation | 1 |
| [qt-widgets/ViewportWindow](../qt-widgets/ViewportWindow.md) | qt-widgets | 1 |

## Related

*None.*

## Explore

Run these from the `gplates-code` skill directory:

```bash
python scripts/gpq.py file src/api/Sleeper.h
python scripts/gpq.py def GPlatesApi::Sleeper --body
python scripts/gpq.py uses Sleeper --kind class
python scripts/gpq.py hier Sleeper
```
