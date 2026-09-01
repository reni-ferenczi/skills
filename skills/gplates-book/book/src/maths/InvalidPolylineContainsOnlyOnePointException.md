# InvalidPolylineContainsOnlyOnePointException

[Book TOC](../../TOC.md) · [maths](../../components/maths.md) · cluster Community 750 · tier 3

| Source file | Kind | Lines |
|---|---|---|
| `src/maths/InvalidPolylineContainsOnlyOnePointException.h` | C++ | 72 |

## Overview

[[[PROSE overview unit=maths/InvalidPolylineContainsOnlyOnePointException tier=3]]]
Replace this whole block, markers included, with 1-3 paragraphs: what this unit is, why it exists, and how it fits the surrounding design. Do not restate the tables below.
[[[/PROSE]]]

## Declared types

| Name | Kind | Bases | Template | Subclasses | Description |
|---|---|---|---|---|---|
| [`GPlatesMaths::InvalidPolylineContainsOnlyOnePointException`](#gplatesmathsinvalidpolylinecontainsonlyonepointexception) | class | [`GPlatesGlobal::InternalObjectInconsistencyException`](../global/InternalObjectInconsistencyException.md) | — | 0 | The exception thrown when a polyline is found to contain zero points. |

## Members

### `GPlatesMaths::InvalidPolylineContainsOnlyOnePointException`

| Member | Kind | Type | Access | Description |
|---|---|---|---|---|
| `InvalidPolylineContainsOnlyOnePointException( const GPlatesUtils::CallStack::Trace &exception_source)` | constructor | `None` | public | Instantiate the exception. |
| `exception_name()` | method | `char` | protected | — |
| `d_filename` | field | `char` | private | — |
| `d_line_num` | field | `int` | private | — |

## Free functions and macros

| Name | Kind | Type / body | Description |
|---|---|---|---|
| `GPLATES_MATHS_INVALIDPOLYLINECONTAINSONLYONEPOINTEXCEPTION_H` | macro | `None` | — |

## Notes

[[[PROSE notes unit=maths/InvalidPolylineContainsOnlyOnePointException tier=3]]]
Replace this whole block, markers included, with invariants, ownership, threading or gotchas that are not visible in the tables. Write *None.* if there is nothing worth saying.
[[[/PROSE]]]

## Used by

| Unit | Component | References |
|---|---|---|
| [file-io/PlatesLineFormatWriter](../file-io/PlatesLineFormatWriter.md) | file-io | 1 |

## Related

*None.*

## Explore

Run these from the `gplates-code` skill directory:

```bash
python scripts/gpq.py file src/maths/InvalidPolylineContainsOnlyOnePointException.h
python scripts/gpq.py def GPlatesMaths::InvalidPolylineContainsOnlyOnePointException --body
python scripts/gpq.py uses InvalidPolylineContainsOnlyOnePointException --kind class
python scripts/gpq.py hier InvalidPolylineContainsOnlyOnePointException
```
