# AbortException

[Book TOC](../../TOC.md) · [global](../../components/global.md) · cluster Community 958 · tier 2

| Source file | Kind | Lines |
|---|---|---|
| `src/global/AbortException.h` | C++ | 68 |
| `src/global/AbortException.cc` | C++ | 36 |

## Overview

[[[PROSE overview unit=global/AbortException tier=2]]]
Replace this whole block, markers included, with 1-3 paragraphs: what this unit is, why it exists, and how it fits the surrounding design. Do not restate the tables below.
[[[/PROSE]]]

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

[[[PROSE notes unit=global/AbortException tier=2]]]
Replace this whole block, markers included, with invariants, ownership, threading or gotchas that are not visible in the tables. Write *None.* if there is nothing worth saying.
[[[/PROSE]]]

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
