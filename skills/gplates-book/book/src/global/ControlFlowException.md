# ControlFlowException

[Book TOC](../../TOC.md) · [global](../../components/global.md) · cluster Community 17 · tier 3

| Source file | Kind | Lines |
|---|---|---|
| `src/global/ControlFlowException.h` | C++ | 75 |

## Overview

`ControlFlowException` is thrown to mark code that should not be reached under normal program flow. It wraps a message describing the unexpected condition and inherits from `Exception` to capture the call stack at the point of throwing, aiding debugging when the exception escapes.

## Declared types

| Name | Kind | Bases | Template | Subclasses | Description |
|---|---|---|---|---|---|
| [`GPlatesGlobal::ControlFlowException`](#gplatesglobalcontrolflowexception) | class | [`Exception`](GPlatesException.md) | — | 0 | Should be thrown when a section of code is reached which should not be logically reachable. |

## Members

### `GPlatesGlobal::ControlFlowException`

| Member | Kind | Type | Access | Description |
|---|---|---|---|---|
| `ControlFlowException( const GPlatesUtils::CallStack::Trace &exception_source, const char *msg)` | constructor | `None` | public | — |
| `~ControlFlowException()` | destructor | `None` | public | — |
| `exception_name()` | method | `char` | protected | — |
| `write_message( std::ostream &os)` | method | `void` | protected | — |
| `_msg` | field | `std::string` | private | — |

## Free functions and macros

| Name | Kind | Type / body | Description |
|---|---|---|---|
| `_GPLATES_GLOBAL_CONTROLFLOWEXCEPTION_H_` | macro | `None` | — |

## Notes

*None.*

## Used by

*Nothing in the tree references this unit.*

## Related

*None.*

## Explore

Run these from the `gplates-code` skill directory:

```bash
python scripts/gpq.py file src/global/ControlFlowException.h
python scripts/gpq.py def GPlatesGlobal::ControlFlowException --body
python scripts/gpq.py uses ControlFlowException --kind class
python scripts/gpq.py hier ControlFlowException
```
