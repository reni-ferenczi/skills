# InvalidPolylineContainsZeroPointsException

[Book TOC](../../TOC.md) · [maths](../../components/maths.md) · cluster Community 750 · tier 3

| Source file | Kind | Lines |
|---|---|---|
| `src/maths/InvalidPolylineContainsZeroPointsException.h` | C++ | 72 |

## Overview

Raised when a polyline is found to contain no points. A valid polyline requires at least two points; this exception indicates an internal consistency error when an empty polyline would be constructed or discovered.

## Declared types

| Name | Kind | Bases | Template | Subclasses | Description |
|---|---|---|---|---|---|
| [`GPlatesMaths::InvalidPolylineContainsZeroPointsException`](#gplatesmathsinvalidpolylinecontainszeropointsexception) | class | [`GPlatesGlobal::InternalObjectInconsistencyException`](../global/InternalObjectInconsistencyException.md) | — | 0 | The exception thrown when a polyline is found to contain zero points. |

## Members

### `GPlatesMaths::InvalidPolylineContainsZeroPointsException`

| Member | Kind | Type | Access | Description |
|---|---|---|---|---|
| `InvalidPolylineContainsZeroPointsException( const GPlatesUtils::CallStack::Trace &exception_source)` | constructor | `None` | public | Instantiate the exception. |
| `exception_name()` | method | `char` | protected | — |
| `d_filename` | field | `char` | private | — |
| `d_line_num` | field | `int` | private | — |

## Free functions and macros

| Name | Kind | Type / body | Description |
|---|---|---|---|
| `GPLATES_MATHS_INVALIDPOLYLINECONTAINSZEROPOINTSEXCEPTION_H` | macro | `None` | — |

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
python scripts/gpq.py file src/maths/InvalidPolylineContainsZeroPointsException.h
python scripts/gpq.py def GPlatesMaths::InvalidPolylineContainsZeroPointsException --body
python scripts/gpq.py uses InvalidPolylineContainsZeroPointsException --kind class
python scripts/gpq.py hier InvalidPolylineContainsZeroPointsException
```
