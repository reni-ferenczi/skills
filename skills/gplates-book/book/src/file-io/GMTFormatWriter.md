# GMTFormatWriter

[Book TOC](../../TOC.md) · [file-io](../../components/file-io.md) · cluster Community 670 · tier 2

| Source file | Kind | Lines |
|---|---|---|
| `src/file-io/GMTFormatWriter.h` | C++ | 195 |
| `src/file-io/GMTFormatWriter.cc` | C++ | 201 |

## Overview

[[[PROSE overview unit=file-io/GMTFormatWriter tier=2]]]
Replace this whole block, markers included, with 1-3 paragraphs: what this unit is, why it exists, and how it fits the surrounding design. Do not restate the tables below.
[[[/PROSE]]]

## Declared types

| Name | Kind | Bases | Template | Subclasses | Description |
|---|---|---|---|---|---|
| [`GPlatesFileIO::GMTFormatWriter`](#gplatesfileiogmtformatwriter) | class | [`GPlatesModel::ConstFeatureVisitor`](../model/FeatureVisitor.md) | — | 0 | — |

## Members

### `GPlatesFileIO::GMTFormatWriter`

| Member | Kind | Type | Access | Description |
|---|---|---|---|---|
| `HeaderFormat` | enum | `None` | public | — |
| `GMTFormatWriter( File::Reference &file_ref, const boost::shared_ptr<const FeatureCollectionFileFormat::GMTConfiguration> &default_gmt_file_configuration)` | constructor | `None` | public | @pre is\_writable(file\_info) is true. |
| `~GMTFormatWriter()` | destructor | `None` | public | — |
| `initialise_pre_feature_properties( const GPlatesModel::FeatureHandle &feature_handle)` | method | `bool` | private | — |
| `finalise_post_feature_properties( const GPlatesModel::FeatureHandle &feature_handle)` | method | `void` | private | — |
| `visit_gml_line_string( const GPlatesPropertyValues::GmlLineString &gml_line_string)` | method | `void` | private | — |
| `visit_gml_multi_point( const GPlatesPropertyValues::GmlMultiPoint &gml_multi_point)` | method | `void` | private | — |
| `visit_gml_orientable_curve( const GPlatesPropertyValues::GmlOrientableCurve &gml_orientable_curve)` | method | `void` | private | — |
| `visit_gml_point( const GPlatesPropertyValues::GmlPoint &gml_point)` | method | `void` | private | — |
| `visit_gml_polygon( const GPlatesPropertyValues::GmlPolygon &gml_polygon)` | method | `void` | private | — |
| `visit_gpml_constant_value( const GPlatesPropertyValues::GpmlConstantValue &gpml_constant_value)` | method | `void` | private | — |
| `FeatureAccumulator` | class | `None` | private | Accumulates feature geometry(s) when visiting a feature. |
| `d_output_file` | field | `boost::scoped_ptr<QFile>` | private | — |
| `d_output_stream` | field | `boost::scoped_ptr<QTextStream>` | private | — |
| `d_feature_header` | field | `boost::scoped_ptr<GMTFormatHeader>` | private | — |
| `d_feature_accumulator` | field | `FeatureAccumulator` | private | — |
| `d_header_printer` | field | `GMTHeaderPrinter` | private | — |

## Free functions and macros

| Name | Kind | Type / body | Description |
|---|---|---|---|
| `GPLATES_FILEIO_GMTFORMATWRITER_H` | macro | `None` | — |

## Notes

[[[PROSE notes unit=file-io/GMTFormatWriter tier=2]]]
Replace this whole block, markers included, with invariants, ownership, threading or gotchas that are not visible in the tables. Write *None.* if there is nothing worth saying.
[[[/PROSE]]]

## Used by

| Unit | Component | References |
|---|---|---|
| [qt-widgets/GMTFileFormatConfigurationDialog](../qt-widgets/GMTFileFormatConfigurationDialog.md) | qt-widgets | 15 |
| [file-io/FeatureCollectionFileFormatConfigurations](FeatureCollectionFileFormatConfigurations.md) | file-io | 11 |
| [file-io/PlatesRotationFileProxy](PlatesRotationFileProxy.md) | file-io | 4 |
| [file-io/FeatureCollectionFileFormatRegistry](FeatureCollectionFileFormatRegistry.md) | file-io | 2 |

## Related

*None.*

## Explore

Run these from the `gplates-code` skill directory:

```bash
python scripts/gpq.py file src/file-io/GMTFormatWriter.h
python scripts/gpq.py def GPlatesFileIO::GMTFormatWriter --body
python scripts/gpq.py uses GMTFormatWriter --kind class
python scripts/gpq.py hier GMTFormatWriter
```
