# PythonInterpreterUnlocker

[Book TOC](../../TOC.md) · [api](../../components/api.md) · cluster Community 974 · tier 2

| Source file | Kind | Lines |
|---|---|---|
| `src/api/PythonInterpreterUnlocker.h` | C++ | 88 |
| `src/api/PythonInterpreterUnlocker.cc` | C++ | 71 |

## Overview

[[[PROSE overview unit=api/PythonInterpreterUnlocker tier=2]]]
Replace this whole block, markers included, with 1-3 paragraphs: what this unit is, why it exists, and how it fits the surrounding design. Do not restate the tables below.
[[[/PROSE]]]

## Declared types

| Name | Kind | Bases | Template | Subclasses | Description |
|---|---|---|---|---|---|
| [`GPlatesApi::PythonInterpreterUnlocker`](#gplatesapipythoninterpreterunlocker) | class | — | — | 0 | A wrapper around Python's PyEval\_SaveThread (which releases the Global Interpreter Lock (GIL)) and PyEval\_RestoreThread (which acquires the GIL). |

## Members

### `GPlatesApi::PythonInterpreterUnlocker`

| Member | Kind | Type | Access | Description |
|---|---|---|---|---|
| `PythonInterpreterUnlocker( bool save_thread_ = true)` | constructor | `None` | public | Constructs a PythonInterpreterUnlocker. |
| `~PythonInterpreterUnlocker()` | destructor | `None` | public | Reacquires the GIL if we have released it, i.e. save\_thread has been called but restore\_thread has not been called. |
| `save_thread()` | method | `void` | public | Releases the GIL. |
| `restore_thread()` | method | `void` | public | Reacquires the GIL. |
| `d_thread_state` | field | `PyThreadState` | private | — |

## Free functions and macros

| Name | Kind | Type / body | Description |
|---|---|---|---|
| `GPLATES_API_PYTHONINTERPRETERUNLOCKER_H` | macro | `None` | — |

## Notes

[[[PROSE notes unit=api/PythonInterpreterUnlocker tier=2]]]
Replace this whole block, markers included, with invariants, ownership, threading or gotchas that are not visible in the tables. Write *None.* if there is nothing worth saying.
[[[/PROSE]]]

## Used by

| Unit | Component | References |
|---|---|---|
| [api/DeferredApiCallImpl](DeferredApiCallImpl.md) | api | 12 |
| [api/ConsoleReader](ConsoleReader.md) | api | 3 |
| [api/ConsoleWriter](ConsoleWriter.md) | api | 2 |
| [api/PythonUtils](PythonUtils.md) | api | 1 |

## Related

*None.*

## Explore

Run these from the `gplates-code` skill directory:

```bash
python scripts/gpq.py file src/api/PythonInterpreterUnlocker.h
python scripts/gpq.py def GPlatesApi::PythonInterpreterUnlocker --body
python scripts/gpq.py uses PythonInterpreterUnlocker --kind class
python scripts/gpq.py hier PythonInterpreterUnlocker
```
