# PlatesLineFormatHeaderVisitor

[Book TOC](../../TOC.md) · [file-io](../../components/file-io.md) · cluster Community 459 · tier 2

| Source file | Kind | Lines |
|---|---|---|
| `src/file-io/PlatesLineFormatHeaderVisitor.h` | C++ | 178 |
| `src/file-io/PlatesLineFormatHeaderVisitor.cc` | C++ | 361 |

## Overview

[[[PROSE overview unit=file-io/PlatesLineFormatHeaderVisitor tier=2]]]
Replace this whole block, markers included, with 1-3 paragraphs: what this unit is, why it exists, and how it fits the surrounding design. Do not restate the tables below.
[[[/PROSE]]]

## Declared types

| Name | Kind | Bases | Template | Subclasses | Description |
|---|---|---|---|---|---|
| [`GPlatesFileIO::OldPlatesHeader`](#gplatesfileiooldplatesheader) | struct | — | — | 0 | — |
| [`GPlatesFileIO::PlatesLineFormatHeaderVisitor`](#gplatesfileioplateslineformatheadervisitor) | class | [`GPlatesModel::ConstFeatureVisitor`](../model/FeatureVisitor.md) | — | 0 | Collects PLATES4 header information. |

## Members

### `GPlatesFileIO::OldPlatesHeader`

| Member | Kind | Type | Access | Description |
|---|---|---|---|---|
| `region_number` | field | `unsigned` | public | — |
| `reference_number` | field | `unsigned` | public | — |
| `string_number` | field | `unsigned` | public | — |
| `geographic_description` | field | `GPlatesUtils::UnicodeString` | public | — |
| `plate_id_number` | field | `GPlatesModel::integer_plate_id_type` | public | — |
| `age_of_appearance` | field | `double` | public | — |
| `age_of_disappearance` | field | `double` | public | — |
| `data_type_code` | field | `GPlatesUtils::UnicodeString` | public | — |
| `data_type_code_number` | field | `unsigned` | public | — |
| `data_type_code_number_additional` | field | `GPlatesUtils::UnicodeString` | public | — |
| `conjugate_plate_id_number` | field | `GPlatesModel::integer_plate_id_type` | public | — |
| `colour_code` | field | `unsigned` | public | — |
| `number_of_points` | field | `unsigned` | public | — |
| `OldPlatesHeader( unsigned int region_number_, unsigned int reference_number_, unsigned int string_number_, const GPlatesUtils::UnicodeString &geographic_description_, GPlatesModel::integer_plate_id_type plate_id_number_, double age_of_appearance_, double age_of_disappearance_, const GPlatesUtils::UnicodeString &data_ty ...` | constructor | `None` | public | — |
| `OldPlatesHeader()` | constructor | `None` | public | Default constructor for an OldPlatesHeader. |
| `create_gpml_old_plates_header()` | method | `GPlatesPropertyValues::GpmlOldPlatesHeader::non_null_ptr_type` | public | Creates a GpmlOldPlatesHeader property value from 'this'. |

### `GPlatesFileIO::PlatesLineFormatHeaderVisitor`

| Member | Kind | Type | Access | Description |
|---|---|---|---|---|
| `PlatesLineFormatHeaderVisitor()` | constructor | `None` | public | — |
| `get_old_plates_header( const GPlatesModel::FeatureHandle::const_weak_ref &feature, OldPlatesHeader& old_plates_header, bool append_feature_id_to_geographic_description = true)` | method | `void` | public | Visits feature\_handle and collects old plates header information. |
| `visit_gml_time_instant( const GPlatesPropertyValues::GmlTimeInstant &gml_time_instant)` | method | `void` | private | — |
| `visit_gml_time_period( const GPlatesPropertyValues::GmlTimePeriod &gml_time_period)` | method | `void` | private | — |
| `visit_gpml_constant_value( const GPlatesPropertyValues::GpmlConstantValue &gpml_constant_value)` | method | `void` | private | — |
| `visit_gpml_old_plates_header( const GPlatesPropertyValues::GpmlOldPlatesHeader &gpml_old_plates_header)` | method | `void` | private | — |
| `visit_gpml_plate_id( const GPlatesPropertyValues::GpmlPlateId &gpml_plate_id)` | method | `void` | private | — |
| `visit_xs_string( const GPlatesPropertyValues::XsString &xs_string)` | method | `void` | private | — |
| `PlatesHeaderAccumulator` | struct | `None` | private | — |
| `d_accum` | field | `PlatesHeaderAccumulator` | private | — |

## Free functions and macros

| Name | Kind | Type / body | Description |
|---|---|---|---|
| `convert_geotimeinstant_to_double( const GPlatesPropertyValues::GeoTimeInstant &geo_time)` | function | `double` | Convert a GeoTimeInstant instance to a double, for output in the PLATES4 line-format. |
| `generate_geog_description()` | function | `GPlatesUtils::UnicodeString` | Generate a geographic description when we have nothing to put there. |
| `append_feature_id_to_geog_description( const GPlatesModel::FeatureId &feature_id, GPlatesUtils::UnicodeString &geog_description)` | function | `void` | Add \<identity\>feature\_id\</identity\> to end of geographic description. |
| `GPLATES_FILEIO_PLATESLINEFORMATHEADERVISITOR_H` | macro | `None` | — |

## Notes

[[[PROSE notes unit=file-io/PlatesLineFormatHeaderVisitor tier=2]]]
Replace this whole block, markers included, with invariants, ownership, threading or gotchas that are not visible in the tables. Write *None.* if there is nothing worth saying.
[[[/PROSE]]]

## Used by

| Unit | Component | References |
|---|---|---|
| [file-io/GMTFormatHeader](GMTFormatHeader.md) | file-io | 29 |
| [file-io/PlatesLineFormatWriter](PlatesLineFormatWriter.md) | file-io | 22 |
| [file-io/CitcomsGMTFormatResolvedTopologicalBoundaryExport](CitcomsGMTFormatResolvedTopologicalBoundaryExport.md) | file-io | 6 |
| [file-io/PlatesLineFormatReader](PlatesLineFormatReader.md) | file-io | 3 |
| [feature-visitors/QueryFeaturePropertiesWidgetPopulator](../feature-visitors/QueryFeaturePropertiesWidgetPopulator.md) | feature-visitors | 2 |
| [feature-visitors/ToQvariantConverter](../feature-visitors/ToQvariantConverter.md) | feature-visitors | 2 |
| [file-io/CitcomsResolvedTopologicalBoundaryExportImpl](CitcomsResolvedTopologicalBoundaryExportImpl.md) | file-io | 2 |
| [file-io/GpmlOutputVisitor](GpmlOutputVisitor.md) | file-io | 2 |
| [file-io/deprecated/GpmlOnePointFiveOutputVisitor](deprecated/GpmlOnePointFiveOutputVisitor.md) | file-io | 2 |
| [qt-widgets/EditOldPlatesHeaderWidget](../qt-widgets/EditOldPlatesHeaderWidget.md) | qt-widgets | 2 |
| [file-io/GMTFormatWriter](GMTFormatWriter.md) | file-io | 1 |
| [file-io/OgrFeatureCollectionWriter](OgrFeatureCollectionWriter.md) | file-io | 1 |

## Related

*None.*

## Explore

Run these from the `gplates-code` skill directory:

```bash
python scripts/gpq.py file src/file-io/PlatesLineFormatHeaderVisitor.h
python scripts/gpq.py def GPlatesFileIO::PlatesLineFormatHeaderVisitor --body
python scripts/gpq.py uses PlatesLineFormatHeaderVisitor --kind class
python scripts/gpq.py hier PlatesLineFormatHeaderVisitor
```
