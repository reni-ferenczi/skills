# Metadata

[Book TOC](../../TOC.md) · [model](../../components/model.md) · cluster Community 135 · tier 1

| Source file | Kind | Lines |
|---|---|---|
| `src/model/Metadata.h` | C++ | 708 |
| `src/model/Metadata.cc` | C++ | 462 |

## Overview

[[[PROSE overview unit=model/Metadata tier=1]]]
Replace this whole block, markers included, with 1-3 paragraphs: what this unit is, why it exists, and how it fits the surrounding design. Do not restate the tables below.
[[[/PROSE]]]

## Declared types

| Name | Kind | Bases | Template | Subclasses | Description |
|---|---|---|---|---|---|
| [`GPlatesModel::DublinCoreMetadata`](#gplatesmodeldublincoremetadata) | struct | — | — | 0 | — |
| [`GPlatesModel::GeoTimeScale`](#gplatesmodelgeotimescale) | struct | — | — | 0 | — |
| [`GPlatesModel::BibInfoType`](#gplatesmodelbibinfotype) | struct | — | — | 0 | — |
| [`GPlatesModel::HeaderMetadataType`](#gplatesmodelheadermetadatatype) | struct | — | — | 0 | — |
| [`GPlatesModel::HellData`](#gplatesmodelhelldata) | class | — | — | 0 | — |
| [`GPlatesModel::FeatureCollectionMetadata`](#gplatesmodelfeaturecollectionmetadata) | class | — | — | 0 | — |
| [`GPlatesModel::Metadata`](#gplatesmodelmetadata) | class | `boost::equality_comparable<Metadata>` | — | 0 | — |
| [`GPlatesModel::MetadataContainer`](#gplatesmodelmetadatacontainer) | typedef | — | — | 0 | — |

## Members

### `GPlatesModel::DublinCoreMetadata`

| Member | Kind | Type | Access | Description |
|---|---|---|---|---|
| `Creator` | struct | `None` | public | — |
| `Contributor` | struct | `None` | public | — |
| `Rights` | struct | `None` | public | — |
| `Coverage` | struct | `None` | public | — |
| `Date` | struct | `None` | public | — |
| `dc_namespace` | field | `QString` | public | — |
| `title` | field | `QString` | public | — |
| `bibliographicCitation` | field | `QString` | public | — |
| `description` | field | `QString` | public | — |
| `contributors` | field | `std::vector<Contributor>` | public | — |
| `creators` | field | `std::vector<Creator>` | public | — |
| `rights` | field | `Rights` | public | — |
| `coverage` | field | `Coverage` | public | — |
| `date` | field | `Date` | public | — |

### `GPlatesModel::GeoTimeScale`

| Member | Kind | Type | Access | Description |
|---|---|---|---|---|
| `to_string()` | method | `QString` | public | — |
| `id` | field | `QString` | public | — |
| `pub_id` | field | `QString` | public | — |
| `ref` | field | `QString` | public | — |
| `bib_ref` | field | `QString` | public | — |
| `original_text` | field | `QString` | public | — |

### `GPlatesModel::BibInfoType`

| Member | Kind | Type | Access | Description |
|---|---|---|---|---|
| `bibfile` | field | `QString` | public | — |
| `doibase` | field | `QString` | public | — |

### `GPlatesModel::HeaderMetadataType`

| Member | Kind | Type | Access | Description |
|---|---|---|---|---|
| `GPLATESROTATIONFILE_version` | field | `QString` | public | — |
| `GPLATESROTATIONFILE_documentation` | field | `QString` | public | — |
| `GPML_namespace` | field | `QString` | public | — |
| `REVISIONHIST` | field | `std::vector<boost::shared_ptr<QString> >` | public | — |

### `GPlatesModel::HellData`

| Member | Kind | Type | Access | Description |
|---|---|---|---|---|
| `HellData( const QString &)` | constructor | `None` | public | — |
| `HellData( const QString &r, const QString &Ns, const QString &dF, const QString &kappahat, const QString &cov)` | constructor | `None` | public | — |
| `r` | field | `double` | private | — |
| `kappahat` | field | `double` | private | — |
| `Ns_n` | field | `int` | private | — |
| `Ns_s` | field | `int` | private | — |
| `dF` | field | `int` | private | — |
| `cov` | field | `std::vector<double>` | private | — |

### `GPlatesModel::FeatureCollectionMetadata`

| Member | Kind | Type | Access | Description |
|---|---|---|---|---|
| `FeatureCollectionMetadata()` | constructor | `None` | public | — |
| `FeatureCollectionMetadata( const GPlatesModel::XmlElementNode::non_null_ptr_type)` | constructor | `None` | public | — |
| `is_fc_metadata( const QString& name)` | method | `bool` | public | — |
| `set_metadata( const QString& name, const QString& value)` | method | `bool` | public | — |
| `get_metadata_as_map()` | method | `std::multimap<QString, QString>` | public | — |
| `to_xml()` | method | `QString` | public | — |
| `serialize( GPlatesFileIO::XmlWriter& writer)` | method | `void` | public | — |
| `serialize( QString& buffer)` | method | `void` | public | — |
| `init()` | method | `void` | protected | — |
| `process_complex_xml_element( QXmlStreamReader&)` | method | `void` | protected | — |
| `process_gpml_meta( QXmlStreamReader&)` | method | `void` | protected | — |
| `process_dc_creator( QXmlStreamReader&)` | method | `void` | protected | — |
| `process_dc_rights( QXmlStreamReader&)` | method | `void` | protected | — |
| `process_dc_date( QXmlStreamReader&)` | method | `void` | protected | — |
| `process_dc_coverage( QXmlStreamReader& reader)` | method | `void` | protected | — |
| `process_dc_namespace( QXmlStreamReader& reader)` | method | `void` | protected | — |
| `process_dc_title( QXmlStreamReader& reader)` | method | `void` | protected | — |
| `process_dc_bibliographicCitation( QXmlStreamReader& reader)` | method | `void` | protected | — |
| `process_dc_description( QXmlStreamReader& reader)` | method | `void` | protected | — |
| `process_dc_contributor( QXmlStreamReader& reader)` | method | `void` | protected | — |
| `set_version( const QString& str)` | method | `void` | protected | — |
| `set_documentation( const QString& str)` | method | `void` | protected | — |
| `set_dc_namespace( const QString& str)` | method | `void` | protected | — |
| `set_dc_title( const QString& str)` | method | `void` | protected | — |
| `set_dc_creator( const QString& str)` | method | `void` | protected | — |
| `set_dc_rights_license( const QString& str)` | method | `void` | protected | — |
| `set_dc_rights_url( const QString& str)` | method | `void` | protected | — |
| `set_dc_date_created( const QString& str)` | method | `void` | protected | — |
| `set_dc_date_modified( const QString& str)` | method | `void` | protected | — |
| `set_dc_coverage_temporal( const QString& str)` | method | `void` | protected | — |
| `set_dc_bibliographicCitation( const QString& str)` | method | `void` | protected | — |
| `set_dc_description( const QString& str)` | method | `void` | protected | — |
| `set_dc_revision_history( const QString& str)` | method | `void` | protected | — |
| `set_dc_bibinfo_bibfile( const QString& str)` | method | `void` | protected | — |
| `set_dc_bibinfo_doibase( const QString& str)` | method | `void` | protected | — |
| `set_gpml_namespace( const QString& str)` | method | `void` | protected | — |
| `set_geotimescale( const QString& str)` | method | `void` | protected | — |
| `set_dc_contributor( const QString& str)` | method | `void` | protected | — |
| `qualified_name( const QXmlStreamReader& reader)` | method | `QString` | protected | — |
| `DC` | field | `DublinCoreMetadata` | protected | — |
| `BIBINFO` | field | `BibInfoType` | protected | — |
| `HeaderMetadata` | field | `HeaderMetadataType` | protected | — |
| `GEOTIMESCALE` | field | `std::vector<GeoTimeScale>` | protected | — |
| `FuncMap` | typedef | `std::map<QString,func_ptr>` | protected | — |
| `d_meta_func` | field | `FuncMap` | protected | — |
| `XMLFuncMap` | typedef | `std::map<QString,xml_process_func_ptr>` | protected | — |
| `d_xml_func_map` | field | `XMLFuncMap` | protected | — |
| `d_recurring_data` | field | `std::set<QString>` | protected | — |
| `DC_NAMESPACE` | field | `QString` | protected | — |
| `GPML_NAMESPACE` | field | `QString` | protected | — |
| `set_data( const QString& name, QXmlStreamReader& reader, func_ptr func)` | method | `void` | protected | — |

### `GPlatesModel::Metadata`

| Member | Kind | Type | Access | Description |
|---|---|---|---|---|
| `shared_ptr_type` | typedef | `boost::shared_ptr<GPlatesModel::Metadata>` | public | — |
| `shared_ptr_to_const_type` | typedef | `boost::shared_ptr<const GPlatesModel::Metadata>` | public | — |
| `Metadata( const QString &name, const QString &content)` | constructor | `None` | public | — |
| `Metadata( const Metadata &other)` | constructor | `None` | public | — |
| `clone()` | method | `shared_ptr_type` | public | — |
| `get_name()` | method | `QString` | public | — |
| `operator==( const Metadata &other)` | operator | `bool` | public | Equality comparison operator. |
| `DISABLED_SEQUENCE_FLAG` | field | `QString` | public | — |
| `DELETE_MARK` | field | `QString` | public | — |
| `d_name` | field | `QString` | protected | — |
| `d_content` | field | `QString` | protected | — |

### `GPlatesModel::MetadataContainer`

*None.*

## Free functions and macros

| Name | Kind | Type / body | Description |
|---|---|---|---|
| `DC_NAMESPACE` | variable | `QString` | — |
| `GPML_NAMESPACE` | variable | `QString` | — |
| `DISABLED_SEQUENCE_FLAG` | variable | `QString` | — |
| `DELETE_MARK` | variable | `QString` | — |
| `create_attr_str( const QString& name, const QString& val)` | function | `QString` | — |
| `GPLATES_MODEL_DCMETADATA_H` | macro | `None` | — |
| `replace_field_string( const QString &str, const std::vector<QString> &fields)` | function | `QString` | This function replace fields in a string with new values. |
| `create_metadata_from_gpml( XmlElementNode::non_null_ptr_type total_reconstruction_pole_element)` | function | `MetadataContainer` | Read rotation pole metadata from a 'gpml:TotalReconstructionPole' structural element. |
| `find_first_of( const QString &name, MetadataContainer &container)` | function | `MetadataContainer::iterator` | — |
| `find_all( const QString &name, MetadataContainer &container)` | function | `MetadataContainer` | — |
| `is_same_meta( Metadata::shared_ptr_type first, Metadata::shared_ptr_type second)` | function | `bool` | — |

## Notes

[[[PROSE notes unit=model/Metadata tier=1]]]
Replace this whole block, markers included, with invariants, ownership, threading or gotchas that are not visible in the tables. Write *None.* if there is nothing worth saying.
[[[/PROSE]]]

## Used by

| Unit | Component | References |
|---|---|---|
| [qt-widgets/MetadataDialog](../qt-widgets/MetadataDialog.md) | qt-widgets | 218 |
| [file-io/PlatesRotationFileProxy](../file-io/PlatesRotationFileProxy.md) | file-io | 41 |
| [property-values/GpmlIrregularSampling](../property-values/GpmlIrregularSampling.md) | property-values | 26 |
| [file-io/PlatesRotationFormatWriter](../file-io/PlatesRotationFormatWriter.md) | file-io | 20 |
| [property-values/GpmlFiniteRotation](../property-values/GpmlFiniteRotation.md) | property-values | 14 |
| [qt-widgets/TotalReconstructionSequencesDialog](../qt-widgets/TotalReconstructionSequencesDialog.md) | qt-widgets | 11 |
| [file-io/deprecated/GpmlOnePointFiveOutputVisitor](../file-io/deprecated/GpmlOnePointFiveOutputVisitor.md) | file-io | 8 |
| [property-values/GpmlMetadata](../property-values/GpmlMetadata.md) | property-values | 8 |
| [app-logic/PartitionFeatureUtils](../app-logic/PartitionFeatureUtils.md) | app-logic | 6 |
| [file-io/GpmlOutputVisitor](../file-io/GpmlOutputVisitor.md) | file-io | 6 |
| [file-io/GsmlPropertyHandlers](../file-io/GsmlPropertyHandlers.md) | file-io | 5 |
| [file-io/GpmlPropertyStructuralTypeReaderUtils](../file-io/GpmlPropertyStructuralTypeReaderUtils.md) | file-io | 4 |
| [app-logic/deprecated/ReconstructedFeatureGeometryPopulator](../app-logic/deprecated/ReconstructedFeatureGeometryPopulator.md) | app-logic | 2 |
| [app-logic/ReconstructScalarCoverageLayerProxy](../app-logic/ReconstructScalarCoverageLayerProxy.md) | app-logic | 1 |
| [file-io/GMTFormatReconstructedScalarCoverageExport](../file-io/GMTFormatReconstructedScalarCoverageExport.md) | file-io | 1 |
| [file-io/GpmlStructuralTypeReaderUtils](../file-io/GpmlStructuralTypeReaderUtils.md) | file-io | 1 |
| [file-io/PlatesLineFormatReader](../file-io/PlatesLineFormatReader.md) | file-io | 1 |
| [gui/ExportFileNameTemplateValidationUtils](../gui/ExportFileNameTemplateValidationUtils.md) | gui | 1 |
| [qt-widgets/EditTotalReconstructionSequenceWidget](../qt-widgets/EditTotalReconstructionSequenceWidget.md) | qt-widgets | 1 |
| [utils/QtFormattingUtils](../utils/QtFormattingUtils.md) | utils | 1 |

## Related

*None.*

## Explore

Run these from the `gplates-code` skill directory:

```bash
python scripts/gpq.py file src/model/Metadata.h
python scripts/gpq.py def GPlatesModel::FeatureCollectionMetadata --body
python scripts/gpq.py uses FeatureCollectionMetadata --kind class
python scripts/gpq.py hier FeatureCollectionMetadata
```
