# PythonInterpreterUnlocker

[Book TOC](../../TOC.md) · [api](../../components/api.md) · cluster Community 974 · tier 2

| Source file | Kind | Lines |
|---|---|---|
| `src/api/PythonInterpreterUnlocker.h` | C++ | 88 |
| `src/api/PythonInterpreterUnlocker.cc` | C++ | 71 |

## Overview

`GPlatesApi::PythonInterpreterUnlocker` is the inverse RAII guard to
`PythonInterpreterLocker`: it wraps `PyEval_SaveThread`/`PyEval_RestoreThread`
to *release* the GIL rather than acquire it. It exists for C++ code that has
been called from Python but is about to do work that does not touch the
interpreter — releasing the GIL there lets other Python threads run
concurrently instead of blocking on this one, improving throughput in code
such as `DeferredApiCallImpl`.

As with `PythonInterpreterLocker`, passing `false` to the constructor defers
the actual `save_thread()` call to the caller, while the destructor still
restores the GIL automatically if it was released and never explicitly
restored.

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

`save_thread()` requires the calling thread to currently hold the GIL.
`restore_thread()` requires the opposite — the calling thread must *not* hold
the GIL — since reacquiring a lock the thread already holds would deadlock.
Calling `restore_thread()` without a prior `save_thread()`, or calling either
out of order, breaks these preconditions; the destructor only calls
`restore_thread()` automatically if `save_thread()` was called and
`restore_thread()` was not.

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
