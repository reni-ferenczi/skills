# GsmlPropertyHandlers

[Book TOC](../../TOC.md) · [file-io](../../components/file-io.md) · cluster Community 747 · tier 2

| Source file | Kind | Lines |
|---|---|---|
| `src/file-io/GsmlPropertyHandlers.h` | C++ | 117 |
| `src/file-io/GsmlPropertyHandlers.cc` | C++ | 707 |

## Overview

[[[PROSE overview unit=file-io/GsmlPropertyHandlers tier=2]]]
Replace this whole block, markers included, with 1-3 paragraphs: what this unit is, why it exists, and how it fits the surrounding design. Do not restate the tables below.
[[[/PROSE]]]

## Declared types

| Name | Kind | Bases | Template | Subclasses | Description |
|---|---|---|---|---|---|
| [`GPlatesFileIO::GsmlPropertyHandlers`](#gplatesfileiogsmlpropertyhandlers) | class | — | — | 0 | — |

## Members

### `GPlatesFileIO::GsmlPropertyHandlers`

| Member | Kind | Type | Access | Description |
|---|---|---|---|---|
| `GsmlPropertyHandlers( GPlatesModel::FeatureHandle::weak_ref fh)` | constructor | `None` | public | — |
| `handle_geometry_property( QBuffer&)` | method | `void` | public | Parse geometry data and create geometry property in GPlates model |
| `handle_observation_method( QBuffer&)` | method | `void` | public | Parse observation method data. |
| `handle_gml_name( QBuffer&)` | method | `void` | public | Parse gml:name data. |
| `handle_gml_desc( QBuffer&)` | method | `void` | public | Parse gml:description data. |
| `handle_occurrence_property( QBuffer&)` | method | `void` | public | Parse occurrence property. |
| `handle_gml_valid_time( QBuffer&)` | method | `void` | public | Copy the gml:validTime property. |
| `handle_gpml_valid_time_range( QBuffer&)` | method | `void` | public | — |
| `handle_gpml_rock_type(QBuffer&)` | method | `void` | public | — |
| `handle_gpml_rock_max_thick(QBuffer&)` | method | `void` | public | — |
| `handle_gpml_rock_min_thick(QBuffer&)` | method | `void` | public | — |
| `handle_gpml_fossil_diversity(QBuffer&)` | method | `void` | public | — |
| `process_geometries( QBuffer&, const QString&)` | method | `void` | protected | — |
| `d_feature` | field | `GPlatesModel::FeatureHandle::weak_ref` | private | — |
| `d_read_errors` | field | `ReadErrorAccumulation` | private | — |

## Free functions and macros

| Name | Kind | Type / body | Description |
|---|---|---|---|
| `get_element_text( QBuffer& xml_data)` | function | `QString` | — |
| `normalize_geometry_coord( QByteArray& buf)` | function | `void` | Since EPSG:4326 coordinates system put longitude before latitude, which is opposite in gpml. |
| `get_srs_name( QByteArray& array_buf)` | function | `QString` | Get the Spatial Reference System name from xml data. |
| `is_epsg_4326( QString& name)` | function | `bool` | Check the input name and determine if it is EPSG\_4326. |
| `find_srs_dimension( const QByteArray& buf)` | function | `unsigned int` | Find the dimension of Spatial Reference System from xml data buffer. |
| `convert_to_epsg_4326( QByteArray& buf)` | function | `void` | Transform data into EPSG 4326. |
| `create_xml_node( QBuffer& buf)` | function | `GPlatesModel::XmlElementNode::non_null_ptr_type` | Create XmlElementNode from QBuffer |
| `create_xml_node( QByteArray& array)` | function | `GPlatesModel::XmlElementNode::non_null_ptr_type` | Create XmlElementNode from QByteArray |
| `GPLATES_FILEIO_GSMLPROPERTYHANDLERS_H` | macro | `None` | — |

## Notes

[[[PROSE notes unit=file-io/GsmlPropertyHandlers tier=2]]]
Replace this whole block, markers included, with invariants, ownership, threading or gotchas that are not visible in the tables. Write *None.* if there is nothing worth saying.
[[[/PROSE]]]

## Used by

| Unit | Component | References |
|---|---|---|
| [file-io/GsmlPropertyDef](GsmlPropertyDef.md) | file-io | 24 |
| [file-io/GeoscimlProfile](GeoscimlProfile.md) | file-io | 1 |
| [file-io/GsmlFeatureHandlers](GsmlFeatureHandlers.md) | file-io | 1 |
| [file-io/GsmlFeaturesDef](GsmlFeaturesDef.md) | file-io | 1 |

## Related

*None.*

## Explore

Run these from the `gplates-code` skill directory:

```bash
python scripts/gpq.py file src/file-io/GsmlPropertyHandlers.h
python scripts/gpq.py def GPlatesFileIO::GsmlPropertyHandlers --body
python scripts/gpq.py uses GsmlPropertyHandlers --kind class
python scripts/gpq.py hier GsmlPropertyHandlers
```
