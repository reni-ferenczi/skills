# OgrUtils

[Book TOC](../../TOC.md) · [file-io](../../components/file-io.md) · cluster Community 366 · tier 2

| Source file | Kind | Lines |
|---|---|---|
| `src/file-io/OgrUtils.h` | C++ | 325 |
| `src/file-io/OgrUtils.cc` | C++ | 1033 |

## Overview

[[[PROSE overview unit=file-io/OgrUtils tier=2]]]
Replace this whole block, markers included, with 1-3 paragraphs: what this unit is, why it exists, and how it fits the surrounding design. Do not restate the tables below.
[[[/PROSE]]]

## Declared types

| Name | Kind | Bases | Template | Subclasses | Description |
|---|---|---|---|---|---|
| [`GPlatesFileIO::OgrUtils::referenced_files_collection_type`](#gplatesfileioogrutilsreferenced_files_collection_type) | typedef | — | — | 0 | Typedef for a sequence of referenced files. |
| [`GPlatesFileIO::OgrUtils::feature_map_type`](#gplatesfileioogrutilsfeature_map_type) | typedef | — | — | 0 | — |
| [`GPlatesFileIO::OgrUtils::feature_map_const_iterator`](#gplatesfileioogrutilsfeature_map_const_iterator) | typedef | — | — | 0 | — |
| [`GPlatesFileIO::OgrUtils::geometrical_property_sequence_type`](#gplatesfileioogrutilsgeometrical_property_sequence_type) | typedef | — | — | 0 | — |

## Members

### `GPlatesFileIO::OgrUtils::referenced_files_collection_type`

*None.*

### `GPlatesFileIO::OgrUtils::feature_map_type`

*None.*

### `GPlatesFileIO::OgrUtils::feature_map_const_iterator`

*None.*

### `GPlatesFileIO::OgrUtils::geometrical_property_sequence_type`

*None.*

## Free functions and macros

| Name | Kind | Type / body | Description |
|---|---|---|---|
| `get_time_from_time_instant( const GPlatesPropertyValues::GmlTimeInstant &time_instant)` | function | `double` | — |
| `GPLATES_FILEIO_SHAPEFILEUTILS_H` | macro | `None` | — |
| `build_feature_map` | variable | `feature_map_type` | build\_feature\_map Build the map of feature-type two-letter codes to feature-type string. |
| `wkb_type_belongs_to_structural_types( const OGRwkbGeometryType &wkb_type, const GPlatesModel::GpgimProperty::structural_type_seq_type &structural_types)` | function | `bool` | wkb\_type\_belongs\_to\_structural\_types true if |
| `get_structural_type_of_wkb_type( const OGRwkbGeometryType &wkb_type)` | function | `boost::optional<GPlatesPropertyValues::StructuralType>` | get\_structural\_type\_of\_wkb\_type the GpgimStructuralType corresponding to the |
| `get_type_qstring_from_qvariant( const QVariant &variant)` | function | `QString` | ! |
| `feature_type_field_is_gpgim_type( const model_to_attribute_map_type &model_to_attribute_map)` | function | `bool` | Returns true if the attribute field name for feature type in the model\_to\_attribute\_map is "GPGIM\_TYPE", otherwise returns false. |
| `make_ogr_xml_filename( const QFileInfo &file_info)` | function | `QString` | Given a filename in the form \<name\>.\<ext\> , this will produce a filename of the form \<name\>.\<ext\>.gplates.xml |
| `save_attribute_map_as_xml_file( const QString &filename, const QMap<QString,QString> &model_to_attribute_map)` | function | `void` | Writes the data in the QMap\<QString,QString\> to an xml file. |
| `create_default_kvd_from_collection( const GPlatesModel::FeatureCollectionHandle::const_weak_ref &feature_collection, boost::optional<GPlatesPropertyValues::GpmlKeyValueDictionary::non_null_ptr_type> &default_key_value_dictionary)` | function | `void` | — |
| `add_plate_id_to_kvd( const GPlatesModel::FeatureHandle::const_weak_ref &feature, GPlatesPropertyValues::GpmlKeyValueDictionary::non_null_ptr_type kvd)` | function | `void` | — |
| `add_reconstruction_fields_to_kvd( GPlatesPropertyValues::GpmlKeyValueDictionary::non_null_ptr_type kvd, const GPlatesModel::integer_plate_id_type &reconstruction_anchor_plate_id, const double &reconstruction_time)` | function | `void` | — |
| `add_referenced_files_to_kvd( GPlatesPropertyValues::GpmlKeyValueDictionary::non_null_ptr_type kvd, const referenced_files_collection_type &referenced_files)` | function | `void` | — |
| `add_reconstruction_files_to_kvd( GPlatesPropertyValues::GpmlKeyValueDictionary::non_null_ptr_type kvd, const referenced_files_collection_type &reconstruction_files)` | function | `void` | — |
| `add_standard_properties_to_kvd( const GPlatesModel::FeatureHandle::const_weak_ref &feature, GPlatesPropertyValues::GpmlKeyValueDictionary::non_null_ptr_type kvd)` | function | `void` | — |
| `add_feature_type_to_kvd( const GPlatesModel::FeatureHandle::const_weak_ref &feature, GPlatesPropertyValues::GpmlKeyValueDictionary::non_null_ptr_type kvd)` | function | `void` | — |
| `add_begin_and_end_time_to_kvd( const GPlatesModel::FeatureHandle::const_weak_ref &feature, GPlatesPropertyValues::GpmlKeyValueDictionary::non_null_ptr_type kvd)` | function | `void` | — |
| `add_name_to_kvd( const GPlatesModel::FeatureHandle::const_weak_ref &feature, GPlatesPropertyValues::GpmlKeyValueDictionary::non_null_ptr_type kvd)` | function | `void` | — |
| `add_description_to_kvd( const GPlatesModel::FeatureHandle::const_weak_ref &feature, GPlatesPropertyValues::GpmlKeyValueDictionary::non_null_ptr_type kvd)` | function | `void` | — |
| `add_feature_id_to_kvd( const GPlatesModel::FeatureHandle::const_weak_ref &feature, GPlatesPropertyValues::GpmlKeyValueDictionary::non_null_ptr_type kvd)` | function | `void` | — |
| `add_conjugate_plate_id_to_kvd( const GPlatesModel::FeatureHandle::const_weak_ref &feature, GPlatesPropertyValues::GpmlKeyValueDictionary::non_null_ptr_type kvd)` | function | `void` | — |
| `add_left_plate_to_kvd( const GPlatesModel::FeatureHandle::const_weak_ref &feature, GPlatesPropertyValues::GpmlKeyValueDictionary::non_null_ptr_type kvd)` | function | `void` | — |
| `add_right_plate_to_kvd( const GPlatesModel::FeatureHandle::const_weak_ref &feature, GPlatesPropertyValues::GpmlKeyValueDictionary::non_null_ptr_type kvd)` | function | `void` | — |
| `add_reconstruction_method_to_kvd( const GPlatesModel::FeatureHandle::const_weak_ref &feature, GPlatesPropertyValues::GpmlKeyValueDictionary::non_null_ptr_type kvd)` | function | `void` | — |
| `add_spreading_asymmetry_to_kvd( const GPlatesModel::FeatureHandle::const_weak_ref &feature, GPlatesPropertyValues::GpmlKeyValueDictionary::non_null_ptr_type kvd)` | function | `void` | — |
| `add_geometry_import_time_to_kvd( const GPlatesModel::FeatureHandle::const_weak_ref &feature, GPlatesPropertyValues::GpmlKeyValueDictionary::non_null_ptr_type kvd)` | function | `void` | — |
| `get_qvariant_from_kvd_element( const GPlatesPropertyValues::GpmlKeyValueDictionaryElement &element)` | function | `QVariant` | — |
| `add_filename_sequence_to_kvd( const QString &root_attribute_name, const referenced_files_collection_type &files, GPlatesPropertyValues::GpmlKeyValueDictionary::non_null_ptr_type &dictionary)` | function | `void` | — |
| `write_kvd( GPlatesPropertyValues::GpmlKeyValueDictionary::non_null_ptr_type kvd)` | function | `void` | Write kvd to debug output |
| `write_kvd( GPlatesPropertyValues::GpmlKeyValueDictionary::non_null_ptr_to_const_type kvd)` | function | `void` | Write kvd to debug output |

## Notes

[[[PROSE notes unit=file-io/OgrUtils tier=2]]]
Replace this whole block, markers included, with invariants, ownership, threading or gotchas that are not visible in the tables. Write *None.* if there is nothing worth saying.
[[[/PROSE]]]

## Used by

| Unit | Component | References |
|---|---|---|
| [file-io/OgrFormatResolvedTopologicalGeometryExport](OgrFormatResolvedTopologicalGeometryExport.md) | file-io | 25 |
| [file-io/OgrReader](OgrReader.md) | file-io | 21 |
| [file-io/OgrFeatureCollectionWriter](OgrFeatureCollectionWriter.md) | file-io | 17 |
| [file-io/OgrFormatReconstructedFeatureGeometryExport](OgrFormatReconstructedFeatureGeometryExport.md) | file-io | 17 |
| [file-io/OgrWriter](OgrWriter.md) | file-io | 7 |
| [file-io/OgrFormatFlowlineExport](OgrFormatFlowlineExport.md) | file-io | 5 |
| [file-io/OgrFormatMotionPathExport](OgrFormatMotionPathExport.md) | file-io | 5 |
| [qt-widgets/EditShapefileAttributesWidget](../qt-widgets/EditShapefileAttributesWidget.md) | qt-widgets | 5 |

## Related

*None.*

## Explore

Run these from the `gplates-code` skill directory:

```bash
python scripts/gpq.py file src/file-io/OgrUtils.h
python scripts/gpq.py def GPlatesFileIO::OgrUtils::referenced_files_collection_type --body
python scripts/gpq.py uses referenced_files_collection_type --kind typedef
```
