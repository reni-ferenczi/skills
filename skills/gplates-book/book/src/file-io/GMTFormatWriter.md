# GMTFormatWriter

[Book TOC](../../TOC.md) · [file-io](../../components/file-io.md) · cluster Community 670 · tier 2

| Source file | Kind | Lines |
|---|---|---|
| `src/file-io/GMTFormatWriter.h` | C++ | 195 |
| `src/file-io/GMTFormatWriter.cc` | C++ | 201 |

## Overview

`GMTFormatWriter` is the `ConstFeatureVisitor` that drives writing a whole feature collection to a GMT xy file: it opens the target `QFile`/`QTextStream` in its constructor (which requires `is_writable(file_info)` to already hold), accumulates every geometry found while visiting a feature's properties in `FeatureAccumulator`, and on `finalise_post_feature_properties()` writes one header-plus-geometry block per accumulated geometry, delegating the geometry itself to a fresh `GMTFormatGeometryExporter` per geometry and the header lines to a `GMTFormatHeader` strategy chosen from the file's `GMTConfiguration` (`PLATES4_STYLE_HEADER`, `VERBOSE_HEADER`, or `PREFER_PLATES4_STYLE_HEADER`). A single `GMTHeaderPrinter` instance is kept for the writer's whole lifetime so header/`>` bookkeeping stays consistent across all features written to the file.

A feature with geometry but no usable header information is still written, with whatever (possibly empty) header lines its `GMTFormatHeader` strategy produced, on the reasoning that the user likely still wants the geometry exported even if header metadata is missing.

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

- The constructor requires `is_writable(file_info)` to already be true; it opens the file itself and throws `ErrorOpeningFileForWritingException` if the open fails.
- If `file_ref` carries no `GMTConfiguration` (or a configuration of the wrong type), the writer falls back to `default_gmt_file_configuration` and writes that configuration back onto `file_ref`, mutating the caller's `File::Reference`.
- The destructor is defined out-of-line specifically so `boost::scoped_ptr<GMTFormatHeader>` is destroyed where `GMTFormatHeader` is a complete type; do not make it `= default` in the header.
- `GmlOrientableCurve` and `GpmlConstantValue` properties are unwrapped by re-dispatching `accept_visitor()` on their inner value rather than being geometries themselves.

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
