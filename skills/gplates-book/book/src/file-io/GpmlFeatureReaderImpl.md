# GpmlFeatureReaderImpl

[Book TOC](../../TOC.md) · [file-io](../../components/file-io.md) · cluster Community 671 · tier 1

| Source file | Kind | Lines |
|---|---|---|
| `src/file-io/GpmlFeatureReaderImpl.h` | C++ | 390 |
| `src/file-io/GpmlFeatureReaderImpl.cc` | C++ | 432 |

## Overview

[[[PROSE overview unit=file-io/GpmlFeatureReaderImpl tier=1]]]
Replace this whole block, markers included, with 1-3 paragraphs: what this unit is, why it exists, and how it fits the surrounding design. Do not restate the tables below.
[[[/PROSE]]]

## Declared types

| Name | Kind | Bases | Template | Subclasses | Description |
|---|---|---|---|---|---|
| [`GPlatesFileIO::GpmlFeatureReaderImpl`](#gplatesfileiogpmlfeaturereaderimpl) | class | [`GPlatesUtils::ReferenceCount<GpmlFeatureReaderImpl>`](../utils/ReferenceCount.md) | — | 9 | Abstract base class for an implementation that reads a feature from a GPML file. |
| [`GPlatesFileIO::GpmlFeatureCreator`](#gplatesfileiogpmlfeaturecreator) | class | [`GpmlFeatureReaderImpl`](GpmlFeatureReaderImpl.md) | — | 0 | The feature reader at the end of the chain of parent readers. |
| [`GPlatesFileIO::GpmlFeatureReader`](#gplatesfileiogpmlfeaturereader) | class | [`GpmlFeatureReaderImpl`](GpmlFeatureReaderImpl.md) | — | 0 | Default concrete class for reading a feature from a GPML file. |
| [`GPlatesFileIO::GpmlAnyPropertyFeatureReader`](#gplatesfileiogpmlanypropertyfeaturereader) | class | [`GpmlFeatureReaderImpl`](GpmlFeatureReaderImpl.md) | — | 0 | A feature reader that reads all unprocessed properties using any of the properties defined in the GPGIM. |
| [`GPlatesFileIO::GpmlUninterpretedFeatureReader`](#gplatesfileiogpmluninterpretedfeaturereader) | class | [`GpmlFeatureReaderImpl`](GpmlFeatureReaderImpl.md) | — | 0 | A feature reader that reads all unprocessed properties as 'UninterpretedPropertyValue' property values. |

## Members

### `GPlatesFileIO::GpmlFeatureReaderImpl`

| Member | Kind | Type | Access | Description |
|---|---|---|---|---|
| `non_null_ptr_type` | typedef | `GPlatesUtils::non_null_intrusive_ptr<GpmlFeatureReaderImpl>` | public | A convenience typedef for a shared pointer to a non-const GpmlFeatureReaderImpl. |
| `non_null_ptr_to_const_type` | typedef | `GPlatesUtils::non_null_intrusive_ptr<const GpmlFeatureReaderImpl>` | public | A convenience typedef for a shared pointer to a const GpmlFeatureReaderImpl. |
| `xml_node_seq_type` | typedef | `std::list<GPlatesModel::XmlNode::non_null_ptr_type>` | public | Typedef for a sequence of XmlNode objects. |
| `~GpmlFeatureReaderImpl()` | destructor | `None` | public | — |
| `read_feature( const GPlatesModel::XmlElementNode::non_null_ptr_type &feature_xml_element, xml_node_seq_type &unprocessed_feature_property_xml_nodes, GpmlReaderUtils::ReaderParams &reader_params)` | method | `GPlatesModel::FeatureHandle::non_null_ptr_type` | public | Creates and reads a feature from the specified sequence of XML nodes representing properties of the feature that have not yet been processed (by other feature reader impls). |

### `GPlatesFileIO::GpmlFeatureCreator`

| Member | Kind | Type | Access | Description |
|---|---|---|---|---|
| `non_null_ptr_type` | typedef | `GPlatesUtils::non_null_intrusive_ptr<GpmlFeatureCreator>` | public | A convenience typedef for a shared pointer to a non-const GpmlFeatureCreator. |
| `non_null_ptr_to_const_type` | typedef | `GPlatesUtils::non_null_intrusive_ptr<const GpmlFeatureCreator>` | public | A convenience typedef for a shared pointer to a const GpmlFeatureCreator. |
| `create( const GPlatesModel::GpgimVersion &gpml_version)` | method | `non_null_ptr_type` | public | Creates a GpmlFeatureCreator. |
| `read_feature( const GPlatesModel::XmlElementNode::non_null_ptr_type &feature_xml_element, xml_node_seq_type &unprocessed_feature_property_xml_nodes, GpmlReaderUtils::ReaderParams &reader_params)` | method | `GPlatesModel::FeatureHandle::non_null_ptr_type` | public | Creates a feature and reads the feature-id and revision-id from the specified property nodes. |
| `d_gpml_version` | field | `GPlatesModel::GpgimVersion` | private | The version of the GPGIM used to create the GPML file being read. |
| `GpmlFeatureCreator( const GPlatesModel::GpgimVersion &gpml_version)` | constructor | `None` | private | — |

### `GPlatesFileIO::GpmlFeatureReader`

| Member | Kind | Type | Access | Description |
|---|---|---|---|---|
| `non_null_ptr_type` | typedef | `GPlatesUtils::non_null_intrusive_ptr<GpmlFeatureReader>` | public | A convenience typedef for a shared pointer to a non-const GpmlFeatureReader. |
| `non_null_ptr_to_const_type` | typedef | `GPlatesUtils::non_null_intrusive_ptr<const GpmlFeatureReader>` | public | A convenience typedef for a shared pointer to a const GpmlFeatureReader. |
| `create( const GPlatesModel::GpgimFeatureClass::non_null_ptr_to_const_type &gpgim_feature_class, const GpmlFeatureReaderImpl::non_null_ptr_to_const_type &parent_feature_reader, const GpmlPropertyStructuralTypeReader::non_null_ptr_to_const_type &structural_type_reader, const GPlatesModel::GpgimVersion &gpml_version)` | method | `non_null_ptr_type` | public | Creates a GpmlFeatureReader. |
| `read_feature( const GPlatesModel::XmlElementNode::non_null_ptr_type &feature_xml_element, xml_node_seq_type &unprocessed_feature_property_xml_nodes, GpmlReaderUtils::ReaderParams &reader_params)` | method | `GPlatesModel::FeatureHandle::non_null_ptr_type` | public | Reads properties associated with our feature class and delegates remaining properties to the reader associated with the parent feature class. |
| `property_reader_seq_type` | typedef | `std::vector<GpmlPropertyReader::non_null_ptr_to_const_type>` | private | Typedef for a sequence of property readers. |
| `d_property_readers` | field | `property_reader_seq_type` | private | Property readers for only the properties in the GPGIM feature class associated with this reader. |
| `d_parent_feature_reader` | field | `GpmlFeatureReaderImpl::non_null_ptr_to_const_type` | private | The feature reader associated with the parent GPGIM feature class. |
| `GpmlFeatureReader( const GPlatesModel::GpgimFeatureClass::non_null_ptr_to_const_type &gpgim_feature_class, const GpmlFeatureReaderImpl::non_null_ptr_to_const_type &parent_feature_reader, const GpmlPropertyStructuralTypeReader::non_null_ptr_to_const_type &property_structural_type_reader, const GPlatesModel::GpgimVersion ...` | constructor | `None` | private | — |

### `GPlatesFileIO::GpmlAnyPropertyFeatureReader`

| Member | Kind | Type | Access | Description |
|---|---|---|---|---|
| `non_null_ptr_type` | typedef | `GPlatesUtils::non_null_intrusive_ptr<GpmlAnyPropertyFeatureReader>` | public | A convenience typedef for a shared pointer to a non-const GpmlAnyPropertyFeatureReader. |
| `non_null_ptr_to_const_type` | typedef | `GPlatesUtils::non_null_intrusive_ptr<const GpmlAnyPropertyFeatureReader>` | public | A convenience typedef for a shared pointer to a const GpmlAnyPropertyFeatureReader. |
| `property_reader_seq_type` | typedef | `std::vector<GpmlPropertyReader::non_null_ptr_to_const_type>` | public | Typedef for a sequence of property readers. |
| `create( const GpmlFeatureReaderImpl::non_null_ptr_to_const_type &feature_reader, const property_reader_seq_type &all_property_readers)` | method | `non_null_ptr_type` | public | Creates a GpmlAnyPropertyFeatureReader that handles any feature properties not processed by feature\_reader. |
| `read_feature( const GPlatesModel::XmlElementNode::non_null_ptr_type &feature_xml_element, xml_node_seq_type &unprocessed_feature_property_xml_nodes, GpmlReaderUtils::ReaderParams &reader_params)` | method | `GPlatesModel::FeatureHandle::non_null_ptr_type` | public | Reads all unprocessed properties using any property defined in the GPGIM. |
| `d_all_property_readers` | field | `property_reader_seq_type` | private | Property readers for all properties defined in the GPGIM. |
| `d_feature_reader` | field | `GpmlFeatureReaderImpl::non_null_ptr_to_const_type` | private | Delegate reading of feature properties to this feature reader. |
| `GpmlAnyPropertyFeatureReader( const GpmlFeatureReaderImpl::non_null_ptr_to_const_type &feature_reader, const property_reader_seq_type &all_property_readers)` | constructor | `None` | private | — |

### `GPlatesFileIO::GpmlUninterpretedFeatureReader`

| Member | Kind | Type | Access | Description |
|---|---|---|---|---|
| `non_null_ptr_type` | typedef | `GPlatesUtils::non_null_intrusive_ptr<GpmlUninterpretedFeatureReader>` | public | A convenience typedef for a shared pointer to a non-const GpmlUninterpretedFeatureReader. |
| `non_null_ptr_to_const_type` | typedef | `GPlatesUtils::non_null_intrusive_ptr<const GpmlUninterpretedFeatureReader>` | public | A convenience typedef for a shared pointer to a const GpmlUninterpretedFeatureReader. |
| `create( const GpmlFeatureReaderImpl::non_null_ptr_to_const_type &feature_reader)` | method | `non_null_ptr_type` | public | Creates a GpmlUninterpretedFeatureReader that handles any feature properties not processed by feature\_reader. |
| `read_feature( const GPlatesModel::XmlElementNode::non_null_ptr_type &feature_xml_element, xml_node_seq_type &unprocessed_feature_property_xml_nodes, GpmlReaderUtils::ReaderParams &reader_params)` | method | `GPlatesModel::FeatureHandle::non_null_ptr_type` | public | Reads all unprocessed properties as 'UninterpretedPropertyValue's. |
| `UninterpretedPropertyValueCreator` | struct | `None` | private | Wraps each visited property in an 'UninterpretedPropertyValue' property value and adds to feature. |
| `d_feature_reader` | field | `GpmlFeatureReaderImpl::non_null_ptr_to_const_type` | private | Delegate reading of feature properties to this feature reader. |
| `GpmlUninterpretedFeatureReader( const GpmlFeatureReaderImpl::non_null_ptr_to_const_type &feature_reader)` | constructor | `None` | private | — |

## Free functions and macros

| Name | Kind | Type / body | Description |
|---|---|---|---|
| `GPLATES_FILE_IO_GPMLFEATUREREADERIMPL_H` | macro | `None` | — |

## Notes

[[[PROSE notes unit=file-io/GpmlFeatureReaderImpl tier=1]]]
Replace this whole block, markers included, with invariants, ownership, threading or gotchas that are not visible in the tables. Write *None.* if there is nothing worth saying.
[[[/PROSE]]]

## Used by

| Unit | Component | References |
|---|---|---|
| [file-io/GpmlUpgradeReaderUtils](GpmlUpgradeReaderUtils.md) | file-io | 154 |
| [file-io/GpmlFeatureReaderFactory](GpmlFeatureReaderFactory.md) | file-io | 151 |
| [file-io/GpmlFeatureReaderInterface](GpmlFeatureReaderInterface.md) | file-io | 18 |
| [file-io/GpmlReader](GpmlReader.md) | file-io | 11 |

## Related

*None.*

## Explore

Run these from the `gplates-code` skill directory:

```bash
python scripts/gpq.py file src/file-io/GpmlFeatureReaderImpl.h
python scripts/gpq.py def GPlatesFileIO::GpmlFeatureReader --body
python scripts/gpq.py uses GpmlFeatureReader --kind class
python scripts/gpq.py hier GpmlFeatureReader
```
