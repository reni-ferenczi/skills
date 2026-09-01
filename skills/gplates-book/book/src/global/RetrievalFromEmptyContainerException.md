# RetrievalFromEmptyContainerException

[Book TOC](../../TOC.md) · [global](../../components/global.md) · cluster Community 1635 · tier 3

| Source file | Kind | Lines |
|---|---|---|
| `src/global/RetrievalFromEmptyContainerException.h` | C++ | 82 |

## Overview

[[[PROSE overview unit=global/RetrievalFromEmptyContainerException tier=3]]]
Replace this whole block, markers included, with 1-3 paragraphs: what this unit is, why it exists, and how it fits the surrounding design. Do not restate the tables below.
[[[/PROSE]]]

## Declared types

| Name | Kind | Bases | Template | Subclasses | Description |
|---|---|---|---|---|---|
| [`GPlatesGlobal::RetrievalFromEmptyContainerException`](#gplatesglobalretrievalfromemptycontainerexception) | class | [`GPlatesGlobal::PreconditionViolationError`](PreconditionViolationError.md) | — | 0 | This is the exception thrown when client code makes an attempt to retrieve an element from an empty container. |

## Members

### `GPlatesGlobal::RetrievalFromEmptyContainerException`

| Member | Kind | Type | Access | Description |
|---|---|---|---|---|
| `RetrievalFromEmptyContainerException( const GPlatesUtils::CallStack::Trace &exception_source)` | constructor | `None` | public | When this exception is thrown, presumably in a member function of the object whose ref-count has been observed to be zero, the parameters to this constructor should be this, GPLATES\_EXCEPTION\_SOURCE, which indicate the object and the ... |
| `~RetrievalFromEmptyContainerException()` | destructor | `None` | public | — |
| `exception_name()` | method | `char` | protected | — |
| `write_message( std::ostream &os)` | method | `void` | protected | — |
| `d_filename` | field | `char` | private | — |
| `d_line_num` | field | `int` | private | — |

## Free functions and macros

| Name | Kind | Type / body | Description |
|---|---|---|---|
| `GPLATES_GLOBAL_RETRIEVALFROMEMPTYCONTAINEREXCEPTION_H` | macro | `None` | — |

## Notes

[[[PROSE notes unit=global/RetrievalFromEmptyContainerException tier=3]]]
Replace this whole block, markers included, with invariants, ownership, threading or gotchas that are not visible in the tables. Write *None.* if there is nothing worth saying.
[[[/PROSE]]]

## Used by

| Unit | Component | References |
|---|---|---|
| [feature-visitors/GeometryFinder](../feature-visitors/GeometryFinder.md) | feature-visitors | 2 |
| [feature-visitors/GeometrySetter](../feature-visitors/GeometrySetter.md) | feature-visitors | 1 |

## Related

*None.*

## Explore

Run these from the `gplates-code` skill directory:

```bash
python scripts/gpq.py file src/global/RetrievalFromEmptyContainerException.h
python scripts/gpq.py def GPlatesGlobal::RetrievalFromEmptyContainerException --body
python scripts/gpq.py uses RetrievalFromEmptyContainerException --kind class
python scripts/gpq.py hier RetrievalFromEmptyContainerException
```
