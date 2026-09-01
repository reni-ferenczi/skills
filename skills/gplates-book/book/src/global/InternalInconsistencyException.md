# InternalInconsistencyException

[Book TOC](../../TOC.md) · [global](../../components/global.md) · cluster Community 1429 · tier 3

| Source file | Kind | Lines |
|---|---|---|
| `src/global/InternalInconsistencyException.h` | C++ | 91 |
| `src/global/InternalInconsistencyException.cc` | C++ | 36 |

## Overview

`InternalInconsistencyException` is thrown when code detects an unexpected internal inconsistency that indicates a bug or corruption in the application state. It supports defensive programming: checking invariants the compiler cannot guarantee (e.g., that a lookup succeeds, that state transitions are valid). When detected at runtime, it provides a descriptive message and call stack rather than allowing silent failures or delayed crashes.

## Declared types

| Name | Kind | Bases | Template | Subclasses | Description |
|---|---|---|---|---|---|
| [`GPlatesGlobal::InternalInconsistencyException`](#gplatesglobalinternalinconsistencyexception) | class | [`Exception`](GPlatesException.md) | — | 0 | Should be thrown when an unexpected internal inconsistency is detected. |

## Members

### `GPlatesGlobal::InternalInconsistencyException`

| Member | Kind | Type | Access | Description |
|---|---|---|---|---|
| `InternalInconsistencyException( const GPlatesUtils::CallStack::Trace &exception_source, const std::string &msg)` | constructor | `None` | public | — |
| `~InternalInconsistencyException()` | destructor | `None` | public | — |
| `exception_name()` | method | `char` | protected | — |
| `write_message( std::ostream &os)` | method | `void` | protected | — |
| `m_msg` | field | `std::string` | private | — |

## Free functions and macros

| Name | Kind | Type / body | Description |
|---|---|---|---|
| `GPLATES_GLOBAL_INTERNALINCONSISTENCYEXCEPTION_H` | macro | `None` | — |

## Notes

*None.*

## Used by

| Unit | Component | References |
|---|---|---|
| [deprecated/patterns/PublisherTemplate](../deprecated/patterns/PublisherTemplate.md) | deprecated | 2 |
| [canvas-tools/BuildTopology](../canvas-tools/BuildTopology.md) | canvas-tools | 1 |
| [canvas-tools/EditTopology](../canvas-tools/EditTopology.md) | canvas-tools | 1 |

## Related

*None.*

## Explore

Run these from the `gplates-code` skill directory:

```bash
python scripts/gpq.py file src/global/InternalInconsistencyException.h
python scripts/gpq.py def GPlatesGlobal::InternalInconsistencyException --body
python scripts/gpq.py uses InternalInconsistencyException --kind class
python scripts/gpq.py hier InternalInconsistencyException
```
