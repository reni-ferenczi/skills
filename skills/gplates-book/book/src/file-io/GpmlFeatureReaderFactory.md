# GpmlFeatureReaderFactory

[Book TOC](../../TOC.md) · [file-io](../../components/file-io.md) · cluster Community 280 · tier 3

| Source file | Kind | Lines |
|---|---|---|
| `src/file-io/GpmlFeatureReaderFactory.h` | C++ | 238 |
| `src/file-io/GpmlFeatureReaderFactory.cc` | C++ | 724 |

## Overview

[[[PROSE overview unit=file-io/GpmlFeatureReaderFactory tier=3]]]
Replace this whole block, markers included, with 1-3 paragraphs: what this unit is, why it exists, and how it fits the surrounding design. Do not restate the tables below.
[[[/PROSE]]]

## Declared types

| Name | Kind | Bases | Template | Subclasses | Description |
|---|---|---|---|---|---|
| [`GPlatesFileIO::GpmlFeatureReaderFactory`](#gplatesfileiogpmlfeaturereaderfactory) | class | `boost::noncopyable` | — | 0 | Handles generation of GPML feature reader structures that match the GPGIM version in a GPML file. |

## Members

### `GPlatesFileIO::GpmlFeatureReaderFactory`

| Member | Kind | Type | Access | Description |
|---|---|---|---|---|
| `GpmlFeatureReaderFactory( const GpmlPropertyStructuralTypeReader::non_null_ptr_to_const_type &property_structural_type_reader, const GPlatesModel::GpgimVersion &gpml_version)` | constructor | `None` | public | Constructs a GpmlFeatureReaderFactory from a GPGIM. gpml\_version is the GPGIM version stored in the GPML file. |
| `get_feature_reader( const GPlatesModel::FeatureType &feature_type)` | method | `GpmlFeatureReaderInterface` | public | Returns the feature reader associated with the specified feature type, and creates a new feature reader if one was not previously created. |
| `feature_reader_map_impl_type` | typedef | `std::map<GPlatesModel::FeatureType, GpmlFeatureReaderImpl::non_null_ptr_type>` | private | Typedef for a map of feature types to feature reader impls. |
| `property_reader_seq_type` | typedef | `std::vector<GpmlPropertyReader::non_null_ptr_to_const_type>` | private | Typedef for a sequence of property readers. |
| `d_property_structural_type_reader` | field | `GpmlPropertyStructuralTypeReader::non_null_ptr_to_const_type` | private | Used to read structural types from a GPML file. |
| `d_gpml_version` | field | `GPlatesModel::GpgimVersion` | private | The version of the GPGIM used to create the GPML file being read. |
| `d_unprocessed_property_readers` | field | `property_reader_seq_type` | private | Used to read feature properties not allowed for a feature type, or when a feature type is not recognised (by the GPGIM). |
| `d_feature_reader_impl_map` | field | `feature_reader_map_impl_type` | private | Map of feature types to feature reader impls. |
| `get_feature_reader_impl( const GPlatesModel::FeatureType &feature_type)` | method | `boost::optional<GpmlFeatureReaderImpl::non_null_ptr_type>` | private | Gets the feature reader implementation for the specified feature type. |
| `create_feature_reader_impl( const GPlatesModel::FeatureType &feature_type)` | method | `boost::optional<GpmlFeatureReaderImpl::non_null_ptr_type>` | private | Creates a feature reader implementation for the specified feature type. |
| `create_feature_reader_impl( const GPlatesModel::GpgimFeatureClass::non_null_ptr_to_const_type &gpgim_feature_class)` | method | `boost::optional<GpmlFeatureReaderImpl::non_null_ptr_type>` | private | Creates a feature reader implementation for the specified feature class. |
| `get_parent_feature_reader_impl( const GPlatesModel::GpgimFeatureClass::non_null_ptr_to_const_type &gpgim_feature_class)` | method | `boost::optional<GpmlFeatureReaderImpl::non_null_ptr_type>` | private | Gets the parent feature reader implementation for the specified gpgim feature class. |
| `create_upgrade_feature_reader_impl( const GPlatesModel::FeatureType &feature_type)` | method | `boost::optional<GpmlFeatureReaderImpl::non_null_ptr_type>` | private | Creates a feature reader implementation for the specified feature type that can upgrade the feature (being read) from an older version GPGIM. |
| `create_upgrade_1_6_318_feature_reader_impl( const GPlatesModel::FeatureType &feature_type)` | method | `boost::optional<GpmlFeatureReaderImpl::non_null_ptr_type>` | private | Creates a feature reader that handles changes made in the GPGIM version (in the method's name). |
| `create_upgrade_1_6_319_feature_reader_impl( const GPlatesModel::FeatureType &feature_type)` | method | `boost::optional<GpmlFeatureReaderImpl::non_null_ptr_type>` | private | Creates a feature reader that handles changes made in the GPGIM version (in the method's name). |
| `create_upgrade_1_6_320_feature_reader_impl( const GPlatesModel::FeatureType &feature_type)` | method | `boost::optional<GpmlFeatureReaderImpl::non_null_ptr_type>` | private | Creates a feature reader that handles changes made in the GPGIM version (in the method's name). |
| `create_upgrade_1_6_338_feature_reader_impl( const GPlatesModel::FeatureType &feature_type)` | method | `boost::optional<GpmlFeatureReaderImpl::non_null_ptr_type>` | private | Creates a feature reader that handles changes made in the GPGIM version (in the method's name). |
| `create_upgrade_1_6_339_feature_reader_impl( const GPlatesModel::FeatureType &feature_type)` | method | `boost::optional<GpmlFeatureReaderImpl::non_null_ptr_type>` | private | Creates a feature reader that handles changes made in the GPGIM version (in the method's name). |
| `create_property_rename_feature_reader_impl( const GPlatesModel::FeatureType &feature_type, const GPlatesModel::PropertyName &from_property_name, const GPlatesModel::PropertyName &to_property_name)` | method | `boost::optional<GpmlFeatureReaderImpl::non_null_ptr_type>` | private | Creates a feature reader that renames a single property. |
| `create_property_rename_feature_reader_impl( const GPlatesModel::FeatureType &feature_type, const std::vector<GpmlUpgradeReaderUtils::PropertyRename> &property_rename_pairs)` | method | `boost::optional<GpmlFeatureReaderImpl::non_null_ptr_type>` | private | Creates a feature reader that renames multiple properties. |
| `create_property_remove_feature_reader_impl( const GPlatesModel::FeatureType &feature_type, const GPlatesModel::GpgimProperty::non_null_ptr_to_const_type &property)` | method | `boost::optional<GpmlFeatureReaderImpl::non_null_ptr_type>` | private | Creates a feature reader that removes a single property. |
| `create_property_remove_feature_reader_impl( const GPlatesModel::FeatureType &feature_type, const std::vector<GPlatesModel::GpgimProperty::non_null_ptr_to_const_type> &properties)` | method | `boost::optional<GpmlFeatureReaderImpl::non_null_ptr_type>` | private | Creates a feature reader that removes multiple properties. |

## Free functions and macros

| Name | Kind | Type / body | Description |
|---|---|---|---|
| `GPLATES_FILE_IO_GPMLFEATUREREADERFACTORY_H` | macro | `None` | — |

## Notes

[[[PROSE notes unit=file-io/GpmlFeatureReaderFactory tier=3]]]
Replace this whole block, markers included, with invariants, ownership, threading or gotchas that are not visible in the tables. Write *None.* if there is nothing worth saying.
[[[/PROSE]]]

## Used by

| Unit | Component | References |
|---|---|---|
| [file-io/GpmlReader](GpmlReader.md) | file-io | 5 |

## Related

*None.*

## Explore

Run these from the `gplates-code` skill directory:

```bash
python scripts/gpq.py file src/file-io/GpmlFeatureReaderFactory.h
python scripts/gpq.py def GPlatesFileIO::GpmlFeatureReaderFactory --body
python scripts/gpq.py uses GpmlFeatureReaderFactory --kind class
python scripts/gpq.py hier GpmlFeatureReaderFactory
```
