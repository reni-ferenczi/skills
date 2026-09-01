# GpmlMetadata

[Book TOC](../../TOC.md) · [property-values](../../components/property-values.md) · cluster Community 1054 · tier 3

| Source file | Kind | Lines |
|---|---|---|
| `src/property-values/GpmlMetadata.h` | C++ | 159 |

## Overview

[[[PROSE overview unit=property-values/GpmlMetadata tier=3]]]
Replace this whole block, markers included, with 1-3 paragraphs: what this unit is, why it exists, and how it fits the surrounding design. Do not restate the tables below.
[[[/PROSE]]]

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

[[[PROSE notes unit=property-values/GpmlMetadata tier=3]]]
Replace this whole block, markers included, with invariants, ownership, threading or gotchas that are not visible in the tables. Write *None.* if there is nothing worth saying.
[[[/PROSE]]]

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
