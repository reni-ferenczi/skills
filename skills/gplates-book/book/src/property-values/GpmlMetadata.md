# GpmlMetadata

[Book TOC](../../TOC.md) · [property-values](../../components/property-values.md) · cluster Community 1054 · tier 3

| Source file | Kind | Lines |
|---|---|---|
| `src/property-values/GpmlMetadata.h` | C++ | 159 |

## Overview

`GpmlMetadata` wraps a `FeatureCollectionMetadata` object to represent metadata about a feature collection as a property value. The class is mutable—metadata can be replaced via `set_data()`, which updates the instance ID. It provides convenience methods to access the metadata in different forms: as a multimap for programmatic access, as XML for serialization, or via `serialize()` for direct XML writing. The visitor pattern enables feature traversal to encounter metadata properties.

## Declared types

| Name | Kind | Bases | Template | Subclasses | Description |
|---|---|---|---|---|---|
| [`GPlatesPropertyValues::GpmlMetadata`](#gplatespropertyvaluesgpmlmetadata) | class | [`GPlatesModel::PropertyValue`](../model/PropertyValue.md) | — | 0 | — |

## Members

### `GPlatesPropertyValues::GpmlMetadata`

| Member | Kind | Type | Access | Description |
|---|---|---|---|---|
| `non_null_ptr_type` | typedef | `GPlatesUtils::non_null_intrusive_ptr<GpmlMetadata>` | public | A convenience typedef for GPlatesUtils::non\_null\_intrusive\_ptr\<GpmlMetadata\>. |
| `non_null_ptr_to_const_type` | typedef | `GPlatesUtils::non_null_intrusive_ptr<const GpmlMetadata>` | public | A convenience typedef for GPlatesUtils::non\_null\_intrusive\_ptr\<const GpmlMetadata\>. |
| `create( const GPlatesModel::FeatureCollectionMetadata &metadata)` | method | `non_null_ptr_type` | public | — |
| `deep_clone()` | method | `non_null_ptr_type` | public | — |
| `DEFINE_FUNCTION_DEEP_CLONE_AS_PROP_VAL()` | method | `None` | public | — |
| `set_data( const GPlatesModel::FeatureCollectionMetadata &metadata)` | method | `void` | public | — |
| `get_feature_collection_metadata_as_map()` | method | `std::multimap<QString, QString>` | public | — |
| `get_feature_collection_metadata_as_xml()` | method | `QString` | public | — |
| `serialize( GPlatesFileIO::XmlWriter& writer)` | method | `void` | public | — |
| `get_structural_type()` | method | `GPlatesPropertyValues::StructuralType` | public | — |
| `accept_visitor( GPlatesModel::FeatureVisitor &visitor)` | method | `void` | public | — |
| `accept_visitor( GPlatesModel::ConstFeatureVisitor &visitor)` | method | `void` | public | — |
| `d_metadata` | field | `GPlatesModel::FeatureCollectionMetadata` | protected | — |
| `GpmlMetadata( const GPlatesModel::FeatureCollectionMetadata &metadata)` | constructor | `None` | protected | — |

## Free functions and macros

| Name | Kind | Type / body | Description |
|---|---|---|---|
| `GPLATES_PROPERTYVALUES_GPMLMETADATA_H` | macro | `None` | — |

## Notes

*None.*

## Used by

| Unit | Component | References |
|---|---|---|
| [file-io/GpmlPropertyStructuralTypeReaderUtils](../file-io/GpmlPropertyStructuralTypeReaderUtils.md) | file-io | 3 |
| [file-io/PlatesRotationFileProxy](../file-io/PlatesRotationFileProxy.md) | file-io | 2 |
| [file-io/GpmlOutputVisitor](../file-io/GpmlOutputVisitor.md) | file-io | 1 |
| [qt-widgets/MetadataDialog](../qt-widgets/MetadataDialog.md) | qt-widgets | 1 |
| [qt-widgets/TotalReconstructionSequencesDialog](../qt-widgets/TotalReconstructionSequencesDialog.md) | qt-widgets | 1 |

## Related

*None.*

## Explore

Run these from the `gplates-code` skill directory:

```bash
python scripts/gpq.py file src/property-values/GpmlMetadata.h
python scripts/gpq.py def GPlatesPropertyValues::GpmlMetadata --body
python scripts/gpq.py uses GpmlMetadata --kind class
python scripts/gpq.py hier GpmlMetadata
```
