# PropertyValueNotSupportedException

[Book TOC](../../TOC.md) · [qt-widgets](../../components/qt-widgets.md) · cluster Community 17 · tier 3

| Source file | Kind | Lines |
|---|---|---|
| `src/qt-widgets/PropertyValueNotSupportedException.h` | C++ | 66 |

## Overview

An exception thrown by edit widgets when asked to configure themselves for a property value type they do not support. For example, `EditEnumerationWidget` throws this when asked to edit an `xs:double` property. The exception inherits from `GPlatesGlobal::IllegalParametersException` and carries a fixed error message.

## Declared types

| Name | Kind | Bases | Template | Subclasses | Description |
|---|---|---|---|---|---|
| [`GPlatesQtWidgets::PropertyValueNotSupportedException`](#gplatesqtwidgetspropertyvaluenotsupportedexception) | class | [`GPlatesGlobal::IllegalParametersException`](../global/IllegalParametersException.md) | — | 0 | Exception thrown by Edit Widgets when asked to configure themselves for a property value type which they do not support. |

## Members

### `GPlatesQtWidgets::PropertyValueNotSupportedException`

| Member | Kind | Type | Access | Description |
|---|---|---|---|---|
| `PropertyValueNotSupportedException( const GPlatesUtils::CallStack::Trace &exception_source)` | constructor | `None` | public | FIXME: I thought we weren't using strings in exceptions? |
| `exception_name()` | method | `char` | protected | — |

## Free functions and macros

| Name | Kind | Type / body | Description |
|---|---|---|---|
| `GPLATES_QTWIDGETS_PROPERTYVALUENOTSUPPORTEDEXCEPTION_H` | macro | `None` | — |

## Notes

*None.*

## Used by

| Unit | Component | References |
|---|---|---|
| [qt-widgets/AbstractEditWidget](AbstractEditWidget.md) | qt-widgets | 1 |

## Related

*None.*

## Explore

Run these from the `gplates-code` skill directory:

```bash
python scripts/gpq.py file src/qt-widgets/PropertyValueNotSupportedException.h
python scripts/gpq.py def GPlatesQtWidgets::PropertyValueNotSupportedException --body
python scripts/gpq.py uses PropertyValueNotSupportedException --kind class
python scripts/gpq.py hier PropertyValueNotSupportedException
```
