# InvalidFeatureCollectionException

[Book TOC](../../TOC.md) · [global](../../components/global.md) · cluster Community 17 · tier 3

| Source file | Kind | Lines |
|---|---|---|
| `src/global/InvalidFeatureCollectionException.h` | C++ | 73 |

## Overview

`InvalidFeatureCollectionException` is thrown when code encounters an invalid `FeatureCollectionHandle` where a valid one was expected. It wraps a descriptive message and inherits from `Exception` to capture the call stack at the point of detection.

## Declared types

| Name | Kind | Bases | Template | Subclasses | Description |
|---|---|---|---|---|---|
| [`GPlatesGlobal::InvalidFeatureCollectionException`](#gplatesglobalinvalidfeaturecollectionexception) | class | [`Exception`](GPlatesException.md) | — | 0 | Should be thrown when a function which expects a valid FeatureCollectionHandle is given an invalid one. |

## Members

### `GPlatesGlobal::InvalidFeatureCollectionException`

| Member | Kind | Type | Access | Description |
|---|---|---|---|---|
| `InvalidFeatureCollectionException( const GPlatesUtils::CallStack::Trace &exception_source, const char *msg)` | constructor | `None` | public | — |
| `~InvalidFeatureCollectionException()` | destructor | `None` | public | — |
| `exception_name()` | method | `char` | protected | — |
| `write_message( std::ostream &os)` | method | `void` | protected | — |
| `_msg` | field | `std::string` | private | — |

## Free functions and macros

| Name | Kind | Type / body | Description |
|---|---|---|---|
| `GPLATES_GLOBAL_INVALIDFEATURECOLLECTIONEXCEPTION_H` | macro | `None` | — |

## Notes

*None.*

## Used by

| Unit | Component | References |
|---|---|---|
| [app-logic/FeatureCollectionFileIO](../app-logic/FeatureCollectionFileIO.md) | app-logic | 2 |
| [gui/FileIOFeedback](../gui/FileIOFeedback.md) | gui | 2 |
| [qt-widgets/FeatureSummaryWidget](../qt-widgets/FeatureSummaryWidget.md) | qt-widgets | 2 |
| [model/ModelUtils](../model/ModelUtils.md) | model | 1 |
| [qt-widgets/ManageFeatureCollectionsDialog](../qt-widgets/ManageFeatureCollectionsDialog.md) | qt-widgets | 1 |
| [view-operations/SplitFeatureUndoCommand](../view-operations/SplitFeatureUndoCommand.md) | view-operations | 1 |

## Related

*None.*

## Explore

Run these from the `gplates-code` skill directory:

```bash
python scripts/gpq.py file src/global/InvalidFeatureCollectionException.h
python scripts/gpq.py def GPlatesGlobal::InvalidFeatureCollectionException --body
python scripts/gpq.py uses InvalidFeatureCollectionException --kind class
python scripts/gpq.py hier InvalidFeatureCollectionException
```
