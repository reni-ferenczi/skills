# InvalidLatLonException

[Book TOC](../../TOC.md) · [maths](../../components/maths.md) · cluster Community 631 · tier 2

| Source file | Kind | Lines |
|---|---|---|
| `src/maths/InvalidLatLonException.h` | C++ | 101 |
| `src/maths/InvalidLatLonException.cc` | C++ | 39 |

## Overview

`InvalidLatLonException` is thrown when a `LatLonPoint` is constructed from a latitude or longitude value outside the valid range. It carries the single offending value and a `LatOrLon` tag saying which coordinate was bad, and `write_message` formats them into the exception's diagnostic text; if both coordinates are invalid, only one is reported.

It is a thin `GPlatesGlobal::PreconditionViolationError` specialisation, following the same shape as the other precondition exceptions in the codebase: a private data member per invalid input, plus `exception_name` and `write_message` overrides that plug into the base class's reporting machinery.

## Declared types

| Name | Kind | Bases | Template | Subclasses | Description |
|---|---|---|---|---|---|
| [`GPlatesMaths::InvalidLatLonException`](#gplatesmathsinvalidlatlonexception) | class | [`GPlatesGlobal::PreconditionViolationError`](../global/PreconditionViolationError.md) | — | 0 | This is the exception thrown when an attempt is made to instantiate a LatLonPoint using either an invalid latitude or an invalid longitude (or both, though this exception can only report one problem). |

## Members

### `GPlatesMaths::InvalidLatLonException`

| Member | Kind | Type | Access | Description |
|---|---|---|---|---|
| `LatOrLon` | enum | `None` | public | — |
| `InvalidLatLonException( const GPlatesUtils::CallStack::Trace &exception_source, const double &invalid_value_, LatOrLon lat_or_lon_)` | constructor | `None` | public | invalid longitude. |
| `~InvalidLatLonException()` | destructor | `None` | public | — |
| `lat_or_lon()` | method | `LatOrLon` | public | — |
| `exception_name()` | method | `char` | protected | — |
| `write_message( std::ostream &os)` | method | `void` | protected | — |
| `d_invalid_value` | field | `double` | private | — |
| `d_lat_or_lon` | field | `LatOrLon` | private | — |

## Free functions and macros

| Name | Kind | Type / body | Description |
|---|---|---|---|
| `GPLATES_MATHS_INVALIDLATLONEXCEPTION_H` | macro | `None` | — |

## Notes

*None.*

## Used by

| Unit | Component | References |
|---|---|---|
| [maths/LatLonPoint](LatLonPoint.md) | maths | 7 |
| [api/PyViewportWindow](../api/PyViewportWindow.md) | api | 2 |
| [gui/Dialogs](../gui/Dialogs.md) | gui | 2 |
| [qt-widgets/EditGeometryWidget](../qt-widgets/EditGeometryWidget.md) | qt-widgets | 2 |
| [gui/TopologyTools](../gui/TopologyTools.md) | gui | 1 |
| [qt-widgets/DigitisationWidget](../qt-widgets/DigitisationWidget.md) | qt-widgets | 1 |
| [qt-widgets/LatLonCoordinatesTable](../qt-widgets/LatLonCoordinatesTable.md) | qt-widgets | 1 |
| [qt-widgets/MapView](../qt-widgets/MapView.md) | qt-widgets | 1 |

## Related

*None.*

## Explore

Run these from the `gplates-code` skill directory:

```bash
python scripts/gpq.py file src/maths/InvalidLatLonException.h
python scripts/gpq.py def GPlatesMaths::InvalidLatLonException --body
python scripts/gpq.py uses InvalidLatLonException --kind class
python scripts/gpq.py hier InvalidLatLonException
```
