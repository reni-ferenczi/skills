# GsmlPropertyHandlers

[Book TOC](../../TOC.md) · [file-io](../../components/file-io.md) · cluster Community 747 · tier 2

| Source file | Kind | Lines |
|---|---|---|
| `src/file-io/GsmlPropertyHandlers.h` | C++ | 117 |
| `src/file-io/GsmlPropertyHandlers.cc` | C++ | 707 |

## Overview

`GsmlPropertyHandlers` is the callback target for the `PropertyInfo` table in
`file-io/GsmlPropertyDef`: each `handle_*` method is invoked with the
`QBuffer` of XML matched by that property's query, parses it, and appends the
resulting property value to the `GPlatesModel::FeatureHandle` the handler was
constructed with. `handle_geometry_property` is the most involved case: it
re-runs three XPath queries (`gml:Point`, `gml:LineString`, `gml:Polygon`)
through `process_geometries`, which rewrites the matched fragment's XML
nesting to match what GPML's `GpmlPropertyStructuralTypeReaderUtils` expects
(for example replacing `gml:outerBoundaryIs`/`innerBoundaryIs` with
`gml:exterior`/`gml:interior`, and wrapping a `Polygon` in `gpml:ConstantValue`)
before handing it to the structural-type reader.

The free functions at the top of the `.cc` handle the coordinate-system side
of that conversion: `get_srs_name` and `is_epsg_4326` inspect the `srsName`
attribute, `find_srs_dimension` checks for a 2D or 3D `posList`, and
`convert_to_epsg_4326` is meant to reproject non-4326 coordinates before
`normalize_geometry_coord` swaps GML's longitude-first `posList` ordering to
GPML's latitude-first convention. `create_xml_node` builds the
`GPlatesModel::XmlElementNode` tree that the structural-type readers consume,
from either a `QBuffer` or a `QByteArray`.

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

The actual reprojection step inside `convert_to_epsg_4326` — building an
`OGRSpatialReference` and running it through
`GPlatesPropertyValues::CoordinateTransformation` — is compiled out behind
`#if 0`. In the current build, non-EPSG:4326 input coordinates are passed
through unconverted except for the longitude/latitude axis swap done by
`normalize_geometry_coord`; only data already in EPSG:4326 is handled
correctly end to end. `d_read_errors` is a raw, non-owning pointer obtained
from `ArbitraryXmlReader::instance()` in the constructor, so a
`GsmlPropertyHandlers` must not outlive the reader that owns the accumulator.

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
