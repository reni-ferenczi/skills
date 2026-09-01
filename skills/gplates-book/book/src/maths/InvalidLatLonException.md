# InvalidLatLonException

[Book TOC](../../TOC.md) · [maths](../../components/maths.md) · cluster Community 631 · tier 2

| Source file | Kind | Lines |
|---|---|---|
| `src/maths/InvalidLatLonException.h` | C++ | 101 |
| `src/maths/InvalidLatLonException.cc` | C++ | 39 |

## Overview

[[[PROSE overview unit=maths/InvalidLatLonException tier=2]]]
Replace this whole block, markers included, with 1-3 paragraphs: what this unit is, why it exists, and how it fits the surrounding design. Do not restate the tables below.
[[[/PROSE]]]

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

[[[PROSE notes unit=maths/InvalidLatLonException tier=2]]]
Replace this whole block, markers included, with invariants, ownership, threading or gotchas that are not visible in the tables. Write *None.* if there is nothing worth saying.
[[[/PROSE]]]

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
