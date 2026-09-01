# NoActiveEditWidgetException

[Book TOC](../../TOC.md) · [qt-widgets](../../components/qt-widgets.md) · cluster Community 92 · tier 3

| Source file | Kind | Lines |
|---|---|---|
| `src/qt-widgets/NoActiveEditWidgetException.h` | C++ | 59 |

## Overview

An exception raised when `EditWidgetGroupBox` cannot satisfy its precondition that at least one edit widget is active. This exception signals that code has attempted an operation that requires an active edit widget when none exists — a precondition violation that should not occur in normal operation.

## Declared types

| Name | Kind | Bases | Template | Subclasses | Description |
|---|---|---|---|---|---|
| [`GPlatesQtWidgets::NoActiveEditWidgetException`](#gplatesqtwidgetsnoactiveeditwidgetexception) | class | [`GPlatesGlobal::PreconditionViolationError`](../global/PreconditionViolationError.md) | — | 0 | Exception thrown by EditWidgetGroupBox when a precondition of at least one edit widget being active is violated. |

## Members

### `GPlatesQtWidgets::NoActiveEditWidgetException`

| Member | Kind | Type | Access | Description |
|---|---|---|---|---|
| `NoActiveEditWidgetException( const GPlatesUtils::CallStack::Trace &exception_source)` | constructor | `None` | public | — |
| `~NoActiveEditWidgetException()` | destructor | `None` | public | — |
| `exception_name()` | method | `char` | public | — |

## Free functions and macros

| Name | Kind | Type / body | Description |
|---|---|---|---|
| `GPLATES_QTWIDGETS_NOACTIVEEDITWIDGETEXCEPTION_H` | macro | `None` | — |

## Notes

*None.*

## Used by

| Unit | Component | References |
|---|---|---|
| [qt-widgets/EditWidgetGroupBox](EditWidgetGroupBox.md) | qt-widgets | 3 |

## Related

*None.*

## Explore

Run these from the `gplates-code` skill directory:

```bash
python scripts/gpq.py file src/qt-widgets/NoActiveEditWidgetException.h
python scripts/gpq.py def GPlatesQtWidgets::NoActiveEditWidgetException --body
python scripts/gpq.py uses NoActiveEditWidgetException --kind class
python scripts/gpq.py hier NoActiveEditWidgetException
```
