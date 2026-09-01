# InvalidParametersException

[Book TOC](../../TOC.md) · [global](../../components/global.md) · cluster Community 17 · tier 3

| Source file | Kind | Lines |
|---|---|---|
| `src/global/InvalidParametersException.h` | C++ | 73 |

## Overview

`InvalidParametersException` is thrown when a function or method is called with parameters that are individually valid but invalid in combination. It wraps a descriptive message and inherits from `Exception` to capture the call stack for debugging.

## Declared types

| Name | Kind | Bases | Template | Subclasses | Description |
|---|---|---|---|---|---|
| [`GPlatesGlobal::InvalidParametersException`](#gplatesglobalinvalidparametersexception) | class | [`Exception`](GPlatesException.md) | — | 0 | Should be thrown when a method is called with parameters which are invalid in combination (but none are specifically invalid on their own). |

## Members

### `GPlatesGlobal::InvalidParametersException`

| Member | Kind | Type | Access | Description |
|---|---|---|---|---|
| `InvalidParametersException( const GPlatesUtils::CallStack::Trace &exception_source, const char *msg)` | constructor | `None` | public | — |
| `~InvalidParametersException()` | destructor | `None` | public | — |
| `exception_name()` | method | `char` | protected | — |
| `write_message( std::ostream &os)` | method | `void` | protected | — |
| `_msg` | field | `std::string` | private | — |

## Free functions and macros

| Name | Kind | Type / body | Description |
|---|---|---|---|
| `_GPLATES_GLOBAL_INVALIDPARAMETERSEXCEPTION_H_` | macro | `None` | — |

## Notes

*None.*

## Used by

| Unit | Component | References |
|---|---|---|
| [qt-widgets/FeatureSummaryWidget](../qt-widgets/FeatureSummaryWidget.md) | qt-widgets | 2 |
| [maths/PolygonOnSphere](../maths/PolygonOnSphere.md) | maths | 1 |
| [maths/PolylineOnSphere](../maths/PolylineOnSphere.md) | maths | 1 |
| [model/ModelUtils](../model/ModelUtils.md) | model | 1 |
| [view-operations/SplitFeatureUndoCommand](../view-operations/SplitFeatureUndoCommand.md) | view-operations | 1 |

## Related

*None.*

## Explore

Run these from the `gplates-code` skill directory:

```bash
python scripts/gpq.py file src/global/InvalidParametersException.h
python scripts/gpq.py def GPlatesGlobal::InvalidParametersException --body
python scripts/gpq.py uses InvalidParametersException --kind class
python scripts/gpq.py hier InvalidParametersException
```
