# InvalidPolylineContainsOnlyOnePointException

[Book TOC](../../TOC.md) · [maths](../../components/maths.md) · cluster Community 750 · tier 3

| Source file | Kind | Lines |
|---|---|---|
| `src/maths/InvalidPolylineContainsOnlyOnePointException.h` | C++ | 72 |

## Overview

Raised when a polyline is found to contain only one point. A valid polyline requires at least two points; this exception indicates an internal consistency error in the data structures or geometry operations that would have constructed such a degenerate polyline.

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

*None.*

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
