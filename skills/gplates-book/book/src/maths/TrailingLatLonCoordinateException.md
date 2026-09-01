# TrailingLatLonCoordinateException

[Book TOC](../../TOC.md) · [maths](../../components/maths.md) · cluster Community 541 · tier 3

| Source file | Kind | Lines |
|---|---|---|
| `src/maths/TrailingLatLonCoordinateException.h` | C++ | 90 |
| `src/maths/TrailingLatLonCoordinateException.cc` | C++ | 38 |

## Overview

An exception thrown when parsing a sequence of latitude/longitude coordinates encounters an unpaired trailing coordinate. Since coordinates must be processed in (latitude, longitude) pairs, an odd-length sequence is an error. The exception stores the trailing coordinate value and the length of the sequence, allowing error reporting and diagnosis. It inherits from `ExternalResourceFailureException`, categorizing it as a resource parsing error.

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

*None.*

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
