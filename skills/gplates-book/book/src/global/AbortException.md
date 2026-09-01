# AbortException

[Book TOC](../../TOC.md) · [global](../../components/global.md) · cluster Community 958 · tier 2

| Source file | Kind | Lines |
|---|---|---|
| `src/global/AbortException.h` | C++ | 68 |
| `src/global/AbortException.cc` | C++ | 36 |

## Overview

`AbortException` is a thin `Exception` subclass reserved for failures that mean the program's internal state is no longer trustworthy, as distinct from ordinary error conditions such as a bad input file or a missing external resource. Throwing it signals "this should never happen" rather than "the user did something wrong".

The class adds nothing beyond an `exception_name()` override and a fixed `write_message()` body ("Abort failure"); the actual diagnostic content comes from the call-stack trace that `Exception`'s constructor captures via `GPLATES_EXCEPTION_SOURCE`.

## Declared types

| Name | Kind | Bases | Template | Subclasses | Description |
|---|---|---|---|---|---|
| [`GPlatesGlobal::AbortException`](#gplatesglobalabortexception) | class | [`Exception`](GPlatesException.md) | — | 0 | Base GPlatesGlobal::Exception class which should be used for aborts; these exceptions indicate something is seriously wrong with the internal state of the program. |

## Members

### `GPlatesGlobal::AbortException`

| Member | Kind | Type | Access | Description |
|---|---|---|---|---|
| `AbortException( const GPlatesUtils::CallStack::Trace &exception_source)` | constructor | `None` | public | — |
| `exception_name()` | method | `char` | protected | — |
| `write_message( std::ostream &os)` | method | `void` | protected | — |

## Free functions and macros

| Name | Kind | Type / body | Description |
|---|---|---|---|
| `GPLATES_GLOBAL_ABORTEXCEPTION_H` | macro | `None` | — |

## Notes

*None.*

## Used by

| Unit | Component | References |
|---|---|---|
| [opengl/GLStateSetKeys](../opengl/GLStateSetKeys.md) | opengl | 33 |
| [app-logic/TopologyReconstruct](../app-logic/TopologyReconstruct.md) | app-logic | 15 |
| [global/GPlatesAssert](GPlatesAssert.md) | global | 2 |

## Related

*None.*

## Explore

Run these from the `gplates-code` skill directory:

```bash
python scripts/gpq.py file src/global/AbortException.h
python scripts/gpq.py def GPlatesGlobal::AbortException --body
python scripts/gpq.py uses AbortException --kind class
python scripts/gpq.py hier AbortException
```
