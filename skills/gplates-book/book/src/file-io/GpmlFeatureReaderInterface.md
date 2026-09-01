# GpmlFeatureReaderInterface

[Book TOC](../../TOC.md) · [file-io](../../components/file-io.md) · cluster Community 280 · tier 3

| Source file | Kind | Lines |
|---|---|---|
| `src/file-io/GpmlFeatureReaderInterface.h` | C++ | 70 |
| `src/file-io/GpmlFeatureReaderInterface.cc` | C++ | 64 |

## Overview

A wrapper interface for reading individual features from GPML XML. `GpmlFeatureReaderInterface` holds a `GpmlFeatureReaderImpl` and delegates the actual parsing to it. When `read_feature` is called, it collects all child XML nodes from the feature element, passes them to the implementation for processing, and asserts that every property node has been consumed (unprocessed nodes indicate a malformed or unrecognized feature structure).

## Declared types

| Name | Kind | Bases | Template | Subclasses | Description |
|---|---|---|---|---|---|
| [`GPlatesFileIO::GpmlFeatureReaderInterface`](#gplatesfileiogpmlfeaturereaderinterface) | class | — | — | 0 | Interface class for reading a feature from a GPML file using a GpmlFeatureReaderImpl implementation. |

## Members

### `GPlatesFileIO::GpmlFeatureReaderInterface`

| Member | Kind | Type | Access | Description |
|---|---|---|---|---|
| `GpmlFeatureReaderInterface( const GpmlFeatureReaderImpl::non_null_ptr_type &impl)` | constructor | `None` | public | Construct from a feature reader implementation. |
| `read_feature( const GPlatesModel::XmlElementNode::non_null_ptr_type &feature_xml_element, GpmlReaderUtils::ReaderParams &reader_params)` | method | `GPlatesModel::FeatureHandle::non_null_ptr_type` | public | Creates and reads a feature from the specified feature XML element node. |
| `d_impl` | field | `GpmlFeatureReaderImpl::non_null_ptr_type` | private | — |

## Free functions and macros

| Name | Kind | Type / body | Description |
|---|---|---|---|
| `GPLATES_FILE_IO_GPMLFEATUREREADERINTERFACE_H` | macro | `None` | — |

## Notes

*None.*

## Used by

| Unit | Component | References |
|---|---|---|
| [file-io/GpmlFeatureReaderFactory](GpmlFeatureReaderFactory.md) | file-io | 4 |
| [file-io/GpmlReader](GpmlReader.md) | file-io | 1 |

## Related

*None.*

## Explore

Run these from the `gplates-code` skill directory:

```bash
python scripts/gpq.py file src/file-io/GpmlFeatureReaderInterface.h
python scripts/gpq.py def GPlatesFileIO::GpmlFeatureReaderInterface --body
python scripts/gpq.py uses GpmlFeatureReaderInterface --kind class
python scripts/gpq.py hier GpmlFeatureReaderInterface
```
