# UninitialisedIteratorException

[Book TOC](../../TOC.md) · [global](../../components/global.md) · cluster Community 17 · tier 3

| Source file | Kind | Lines |
|---|---|---|
| `src/global/UninitialisedIteratorException.h` | C++ | 74 |

## Overview

[[[PROSE overview unit=global/UninitialisedIteratorException tier=3]]]
Replace this whole block, markers included, with 1-3 paragraphs: what this unit is, why it exists, and how it fits the surrounding design. Do not restate the tables below.
[[[/PROSE]]]

## Declared types

| Name | Kind | Bases | Template | Subclasses | Description |
|---|---|---|---|---|---|
| [`GPlatesGlobal::UninitialisedIteratorException`](#gplatesglobaluninitialisediteratorexception) | class | [`Exception`](GPlatesException.md) | — | 0 | Should be thrown when an attempt is made to dereference an uninitialised iterator or access the members of a pointed-to-object through an uninitialised iterator. |

## Members

### `GPlatesGlobal::UninitialisedIteratorException`

| Member | Kind | Type | Access | Description |
|---|---|---|---|---|
| `UninitialisedIteratorException( const GPlatesUtils::CallStack::Trace &exception_source, const char *msg)` | constructor | `None` | public | — |
| `~UninitialisedIteratorException()` | destructor | `None` | public | — |
| `exception_name()` | method | `char` | protected | — |
| `write_message( std::ostream &os)` | method | `void` | protected | — |
| `_msg` | field | `std::string` | private | — |

## Free functions and macros

| Name | Kind | Type / body | Description |
|---|---|---|---|
| `_GPLATES_GLOBAL_UNINITIALISEDITERATOREXCEPTION_H_` | macro | `None` | — |

## Notes

[[[PROSE notes unit=global/UninitialisedIteratorException tier=3]]]
Replace this whole block, markers included, with invariants, ownership, threading or gotchas that are not visible in the tables. Write *None.* if there is nothing worth saying.
[[[/PROSE]]]

## Used by

| Unit | Component | References |
|---|---|---|
| [maths/PolygonOnSphere](../maths/PolygonOnSphere.md) | maths | 4 |
| [file-io/ExportTemplateFilenameSequence](../file-io/ExportTemplateFilenameSequence.md) | file-io | 2 |

## Related

*None.*

## Explore

Run these from the `gplates-code` skill directory:

```bash
python scripts/gpq.py file src/global/UninitialisedIteratorException.h
python scripts/gpq.py def GPlatesGlobal::UninitialisedIteratorException --body
python scripts/gpq.py uses UninitialisedIteratorException --kind class
python scripts/gpq.py hier UninitialisedIteratorException
```
