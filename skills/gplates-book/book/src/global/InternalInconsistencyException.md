# InternalInconsistencyException

[Book TOC](../../TOC.md) · [global](../../components/global.md) · cluster Community 1429 · tier 3

| Source file | Kind | Lines |
|---|---|---|
| `src/global/InternalInconsistencyException.h` | C++ | 91 |
| `src/global/InternalInconsistencyException.cc` | C++ | 36 |

## Overview

[[[PROSE overview unit=global/InternalInconsistencyException tier=3]]]
Replace this whole block, markers included, with 1-3 paragraphs: what this unit is, why it exists, and how it fits the surrounding design. Do not restate the tables below.
[[[/PROSE]]]

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

[[[PROSE notes unit=global/InternalInconsistencyException tier=3]]]
Replace this whole block, markers included, with invariants, ownership, threading or gotchas that are not visible in the tables. Write *None.* if there is nothing worth saying.
[[[/PROSE]]]

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
