# UninitialisedEditWidgetException

[Book TOC](../../TOC.md) · [qt-widgets](../../components/qt-widgets.md) · cluster Community 8 · tier 3

| Source file | Kind | Lines |
|---|---|---|
| `src/qt-widgets/UninitialisedEditWidgetException.h` | C++ | 60 |

## Overview

[[[PROSE overview unit=qt-widgets/UninitialisedEditWidgetException tier=3]]]
Replace this whole block, markers included, with 1-3 paragraphs: what this unit is, why it exists, and how it fits the surrounding design. Do not restate the tables below.
[[[/PROSE]]]

## Declared types

| Name | Kind | Bases | Template | Subclasses | Description |
|---|---|---|---|---|---|
| [`GPlatesQtWidgets::UninitialisedEditWidgetException`](#gplatesqtwidgetsuninitialisededitwidgetexception) | class | [`GPlatesGlobal::PreconditionViolationError`](../global/PreconditionViolationError.md) | — | 0 | Exception thrown by an Edit Widget when update\_property\_value\_from\_widget() is called without a property value to update being previously set via update\_widget\_from\_xxxx(). |

## Members

### `GPlatesQtWidgets::UninitialisedEditWidgetException`

| Member | Kind | Type | Access | Description |
|---|---|---|---|---|
| `UninitialisedEditWidgetException( const GPlatesUtils::CallStack::Trace &exception_source)` | constructor | `None` | public | — |
| `~UninitialisedEditWidgetException()` | destructor | `None` | public | — |
| `exception_name()` | method | `char` | public | — |

## Free functions and macros

| Name | Kind | Type / body | Description |
|---|---|---|---|
| `GPLATES_QTWIDGETS_UNINITIALISEDEDITWIDGETEXCEPTION_H` | macro | `None` | — |

## Notes

[[[PROSE notes unit=qt-widgets/UninitialisedEditWidgetException tier=3]]]
Replace this whole block, markers included, with invariants, ownership, threading or gotchas that are not visible in the tables. Write *None.* if there is nothing worth saying.
[[[/PROSE]]]

## Used by

| Unit | Component | References |
|---|---|---|
| [qt-widgets/EditPlateIdWidget](EditPlateIdWidget.md) | qt-widgets | 5 |
| [qt-widgets/EditAgeWidget](EditAgeWidget.md) | qt-widgets | 2 |
| [qt-widgets/EditAngleWidget](EditAngleWidget.md) | qt-widgets | 2 |
| [qt-widgets/EditBooleanWidget](EditBooleanWidget.md) | qt-widgets | 2 |
| [qt-widgets/EditDoubleWidget](EditDoubleWidget.md) | qt-widgets | 2 |
| [qt-widgets/EditEnumerationWidget](EditEnumerationWidget.md) | qt-widgets | 2 |
| [qt-widgets/EditGeometryWidget](EditGeometryWidget.md) | qt-widgets | 2 |
| [qt-widgets/EditIntegerWidget](EditIntegerWidget.md) | qt-widgets | 2 |
| [qt-widgets/EditOldPlatesHeaderWidget](EditOldPlatesHeaderWidget.md) | qt-widgets | 2 |
| [qt-widgets/EditPolarityChronIdWidget](EditPolarityChronIdWidget.md) | qt-widgets | 2 |
| [qt-widgets/EditShapefileAttributesWidget](EditShapefileAttributesWidget.md) | qt-widgets | 2 |
| [qt-widgets/EditStringListWidget](EditStringListWidget.md) | qt-widgets | 2 |
| [qt-widgets/EditStringWidget](EditStringWidget.md) | qt-widgets | 2 |
| [qt-widgets/EditTimeInstantWidget](EditTimeInstantWidget.md) | qt-widgets | 2 |
| [qt-widgets/EditTimePeriodWidget](EditTimePeriodWidget.md) | qt-widgets | 2 |
| [qt-widgets/EditTimeSequenceWidget](EditTimeSequenceWidget.md) | qt-widgets | 2 |

## Related

*None.*

## Explore

Run these from the `gplates-code` skill directory:

```bash
python scripts/gpq.py file src/qt-widgets/UninitialisedEditWidgetException.h
python scripts/gpq.py def GPlatesQtWidgets::UninitialisedEditWidgetException --body
python scripts/gpq.py uses UninitialisedEditWidgetException --kind class
python scripts/gpq.py hier UninitialisedEditWidgetException
```
