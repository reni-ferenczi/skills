# UnexpectedEmptyFeatureCollectionException

[Book TOC](../../TOC.md) · [global](../../components/global.md) · cluster Community 17 · tier 3

| Source file | Kind | Lines |
|---|---|---|
| `src/global/UnexpectedEmptyFeatureCollectionException.h` | C++ | 73 |

## Overview

Exception thrown when code receives a `FeatureCollectionHandle` that is unexpectedly empty. This signals a violated assumption — a function expected its input to contain features but received an empty collection instead. Like `NullParameterException`, this exception carries a custom message to help callers understand which collection was empty or what features were expected.

## Declared types

| Name | Kind | Bases | Template | Subclasses | Description |
|---|---|---|---|---|---|
| [`GPlatesGlobal::UnexpectedEmptyFeatureCollectionException`](#gplatesglobalunexpectedemptyfeaturecollectionexception) | class | [`Exception`](GPlatesException.md) | — | 0 | Should be thrown when a function which expects a non-empty FeatureCollectionHandle is given an empty one. |

## Members

### `GPlatesGlobal::UnexpectedEmptyFeatureCollectionException`

| Member | Kind | Type | Access | Description |
|---|---|---|---|---|
| `UnexpectedEmptyFeatureCollectionException( const GPlatesUtils::CallStack::Trace &exception_source, const char *msg)` | constructor | `None` | public | — |
| `~UnexpectedEmptyFeatureCollectionException()` | destructor | `None` | public | — |
| `exception_name()` | method | `char` | protected | — |
| `write_message( std::ostream &os)` | method | `void` | protected | — |
| `_msg` | field | `std::string` | private | — |

## Free functions and macros

| Name | Kind | Type / body | Description |
|---|---|---|---|
| `GPLATES_GLOBAL_UNEXPECTEDEMPTYFEATURECOLLECTIONEXCEPTION_H` | macro | `None` | — |

## Notes

*None.*

## Used by

| Unit | Component | References |
|---|---|---|
| [gui/FileIOFeedback](../gui/FileIOFeedback.md) | gui | 2 |
| [app-logic/FeatureCollectionFileIO](../app-logic/FeatureCollectionFileIO.md) | app-logic | 1 |
| [qt-widgets/ManageFeatureCollectionsDialog](../qt-widgets/ManageFeatureCollectionsDialog.md) | qt-widgets | 1 |

## Related

*None.*

## Explore

Run these from the `gplates-code` skill directory:

```bash
python scripts/gpq.py file src/global/UnexpectedEmptyFeatureCollectionException.h
python scripts/gpq.py def GPlatesGlobal::UnexpectedEmptyFeatureCollectionException --body
python scripts/gpq.py uses UnexpectedEmptyFeatureCollectionException --kind class
python scripts/gpq.py hier UnexpectedEmptyFeatureCollectionException
```
