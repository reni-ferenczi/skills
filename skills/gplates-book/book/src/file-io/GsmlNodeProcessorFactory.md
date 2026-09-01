# GsmlNodeProcessorFactory

[Book TOC](../../TOC.md) · [file-io](../../components/file-io.md) · cluster Community 663 · tier 3

| Source file | Kind | Lines |
|---|---|---|
| `src/file-io/GsmlNodeProcessorFactory.h` | C++ | 77 |
| `src/file-io/GsmlNodeProcessorFactory.cc` | C++ | 129 |

## Overview

Orchestrates extraction of GSML properties from feature XML. Constructed with a `FeatureHandle`, it holds a `GsmlPropertyHandlers` instance. When `process_with_property_processors()` is called with a feature type and XML data, it looks up the property schema in `GsmlFeaturesDef::AllFeatureTypes`, creating a `GsmlNodeProcessor` for each property with its XQuery and a bound handler callback. It handles both exact type matches (e.g., `MappedFeature`) and prefix-based matches for dynamic types (e.g., `RockUnit_*`). Each processor is executed sequentially against the XML, extracting and populating properties in the target feature.

## Declared types

| Name | Kind | Bases | Template | Subclasses | Description |
|---|---|---|---|---|---|
| [`GPlatesFileIO::GsmlNodeProcessorFactory`](#gplatesfileiogsmlnodeprocessorfactory) | class | — | — | 0 | — |

## Members

### `GPlatesFileIO::GsmlNodeProcessorFactory`

| Member | Kind | Type | Access | Description |
|---|---|---|---|---|
| `GsmlNodeProcessorFactory( GPlatesModel::FeatureHandle::weak_ref feature)` | constructor | `None` | public | — |
| `process_with_property_processors( const QString& feature_type, QByteArray& data)` | method | `void` | public | — |
| `process_with_property_processors( const QString& feature_type, QBuffer& buf)` | method | `void` | public | — |
| `GsmlNodeProcessorFactory()` | constructor | `None` | protected | — |
| `GsmlNodeProcessorFactory( const GsmlNodeProcessorFactory&)` | constructor | `None` | protected | — |
| `create_property_processors( const QString& feature_type)` | method | `std::vector<boost::shared_ptr<GsmlNodeProcessor> >` | protected | — |
| `d_property_handler` | field | `boost::shared_ptr<GsmlPropertyHandlers>` | private | — |

## Free functions and macros

| Name | Kind | Type / body | Description |
|---|---|---|---|
| `GPLATES_FILEIO_XMLNODEPROCESSORFACTORY_H` | macro | `None` | — |

## Notes

*None.*

## Used by

| Unit | Component | References |
|---|---|---|
| [file-io/GsmlFeatureHandlers](GsmlFeatureHandlers.md) | file-io | 9 |
| [file-io/GeoscimlProfile](GeoscimlProfile.md) | file-io | 1 |
| [file-io/GsmlPropertyHandlers](GsmlPropertyHandlers.md) | file-io | 1 |

## Related

*None.*

## Explore

Run these from the `gplates-code` skill directory:

```bash
python scripts/gpq.py file src/file-io/GsmlNodeProcessorFactory.h
python scripts/gpq.py def GPlatesFileIO::GsmlNodeProcessorFactory --body
python scripts/gpq.py uses GsmlNodeProcessorFactory --kind class
python scripts/gpq.py hier GsmlNodeProcessorFactory
```
