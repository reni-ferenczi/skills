# InvalidPropertyValueException

[Book TOC](../../TOC.md) · [qt-widgets](../../components/qt-widgets.md) · cluster Community 1798 · tier 3

| Source file | Kind | Lines |
|---|---|---|
| `src/qt-widgets/InvalidPropertyValueException.h` | C++ | 78 |

## Overview

[[[PROSE overview unit=qt-widgets/InvalidPropertyValueException tier=3]]]
Replace this whole block, markers included, with 1-3 paragraphs: what this unit is, why it exists, and how it fits the surrounding design. Do not restate the tables below.
[[[/PROSE]]]

## Declared types

| Name | Kind | Bases | Template | Subclasses | Description |
|---|---|---|---|---|---|
| [`GPlatesQtWidgets::InvalidPropertyValueException`](#gplatesqtwidgetsinvalidpropertyvalueexception) | class | [`GPlatesGlobal::PreconditionViolationError`](../global/PreconditionViolationError.md) | — | 0 | Exception thrown by an Edit Widget when create\_property\_value\_from\_widget() is called when the fields of the widget do not contain data that can be used to construct a valid PropertyValue. |

## Members

### `GPlatesQtWidgets::InvalidPropertyValueException`

| Member | Kind | Type | Access | Description |
|---|---|---|---|---|
| `InvalidPropertyValueException( const GPlatesUtils::CallStack::Trace &exception_source, const QString &reason_)` | constructor | `None` | public | reason\_ is a translated, human-readable description of the specific details of the failure. |
| `~InvalidPropertyValueException()` | destructor | `None` | public | — |
| `exception_name()` | method | `char` | public | — |
| `d_reason` | field | `QString` | private | — |

## Free functions and macros

| Name | Kind | Type / body | Description |
|---|---|---|---|
| `GPLATES_QTWIDGETS_INVALIDPROPERTYVALUEEXCEPTION_H` | macro | `None` | — |

## Notes

[[[PROSE notes unit=qt-widgets/InvalidPropertyValueException tier=3]]]
Replace this whole block, markers included, with invariants, ownership, threading or gotchas that are not visible in the tables. Write *None.* if there is nothing worth saying.
[[[/PROSE]]]

## Used by

| Unit | Component | References |
|---|---|---|
| [qt-widgets/CreateFeatureDialog](CreateFeatureDialog.md) | qt-widgets | 5 |
| [qt-widgets/EditGeometryWidget](EditGeometryWidget.md) | qt-widgets | 3 |
| [qt-widgets/AddPropertyDialog](AddPropertyDialog.md) | qt-widgets | 2 |
| [qt-widgets/CreateFeatureAddOrEditPropertyDialog](CreateFeatureAddOrEditPropertyDialog.md) | qt-widgets | 2 |
| [qt-widgets/CreateSmallCircleFeatureDialog](CreateSmallCircleFeatureDialog.md) | qt-widgets | 2 |
| [qt-widgets/EditTimeSequenceWidget](EditTimeSequenceWidget.md) | qt-widgets | 2 |
| [qt-widgets/EditStringListWidget](EditStringListWidget.md) | qt-widgets | 1 |

## Related

*None.*

## Explore

Run these from the `gplates-code` skill directory:

```bash
python scripts/gpq.py file src/qt-widgets/InvalidPropertyValueException.h
python scripts/gpq.py def GPlatesQtWidgets::InvalidPropertyValueException --body
python scripts/gpq.py uses InvalidPropertyValueException --kind class
python scripts/gpq.py hier InvalidPropertyValueException
```
