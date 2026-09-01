# TrailingLatLonCoordinateException

[Book TOC](../../TOC.md) · [maths](../../components/maths.md) · cluster Community 541 · tier 3

| Source file | Kind | Lines |
|---|---|---|
| `src/maths/TrailingLatLonCoordinateException.h` | C++ | 90 |
| `src/maths/TrailingLatLonCoordinateException.cc` | C++ | 38 |

## Overview

[[[PROSE overview unit=maths/TrailingLatLonCoordinateException tier=3]]]
Replace this whole block, markers included, with 1-3 paragraphs: what this unit is, why it exists, and how it fits the surrounding design. Do not restate the tables below.
[[[/PROSE]]]

## Declared types

| Name | Kind | Bases | Template | Subclasses | Description |
|---|---|---|---|---|---|
| [`GPlatesMaths::TrailingLatLonCoordinateException`](#gplatesmathstrailinglatloncoordinateexception) | class | [`GPlatesGlobal::ExternalResourceFailureException`](../global/ExternalResourceFailureException.md) | — | 0 | This is the exception thrown when a sequence of doubles, whose elements are to be paired into (lat, lon) coordinate-pairs, encounters a trailing coordinate. |

## Members

### `GPlatesMaths::TrailingLatLonCoordinateException`

| Member | Kind | Type | Access | Description |
|---|---|---|---|---|
| `size_type` | typedef | `unsigned long` | public | — |
| `TrailingLatLonCoordinateException( const GPlatesUtils::CallStack::Trace &exception_source, const double &trailing_coord_, size_type sequence_len_)` | constructor | `None` | public | — |
| `sequence_len()` | method | `size_type` | public | — |
| `exception_name()` | method | `char` | protected | — |
| `write_message( std::ostream &os)` | method | `void` | protected | — |
| `d_trailing_coord` | field | `double` | private | — |
| `d_sequence_len` | field | `size_type` | private | — |

## Free functions and macros

| Name | Kind | Type / body | Description |
|---|---|---|---|
| `GPLATES_MATHS_TRAILINGLATLONCOORDINATEEXCEPTION_H` | macro | `None` | — |

## Notes

[[[PROSE notes unit=maths/TrailingLatLonCoordinateException tier=3]]]
Replace this whole block, markers included, with invariants, ownership, threading or gotchas that are not visible in the tables. Write *None.* if there is nothing worth saying.
[[[/PROSE]]]

## Used by

| Unit | Component | References |
|---|---|---|
| [maths/PointOnSphere](PointOnSphere.md) | maths | 2 |

## Related

*None.*

## Explore

Run these from the `gplates-code` skill directory:

```bash
python scripts/gpq.py file src/maths/TrailingLatLonCoordinateException.h
python scripts/gpq.py def GPlatesMaths::TrailingLatLonCoordinateException --body
python scripts/gpq.py uses TrailingLatLonCoordinateException --kind class
python scripts/gpq.py hier TrailingLatLonCoordinateException
```
