# PlatesLineFormatWriter

[Book TOC](../../TOC.md) · [file-io](../../components/file-io.md) · cluster Community 639 · tier 3

| Source file | Kind | Lines |
|---|---|---|
| `src/file-io/PlatesLineFormatWriter.h` | C++ | 167 |
| `src/file-io/PlatesLineFormatWriter.cc` | C++ | 318 |

## Overview

[[[PROSE overview unit=file-io/PlatesLineFormatWriter tier=3]]]
Replace this whole block, markers included, with 1-3 paragraphs: what this unit is, why it exists, and how it fits the surrounding design. Do not restate the tables below.
[[[/PROSE]]]

## Declared types

| Name | Kind | Bases | Template | Subclasses | Description |
|---|---|---|---|---|---|
| [`(anonymous)::NumberOfGeometryPoints`](#anonymousnumberofgeometrypoints) | class | [`GPlatesMaths::ConstGeometryOnSphereVisitor`](../maths/ConstGeometryOnSphereVisitor.md) | — | 0 | Visitor determines number of points in a derived GeometryOnSphere object. |
| [`GPlatesFileIO::PlatesLineFormatWriter`](#gplatesfileioplateslineformatwriter) | class | [`GPlatesModel::ConstFeatureVisitor`](../model/FeatureVisitor.md) | — | 0 | — |

## Members

### `(anonymous)::NumberOfGeometryPoints`

| Member | Kind | Type | Access | Description |
|---|---|---|---|---|
| `NumberOfGeometryPoints()` | constructor | `None` | public | — |
| `get_number_of_points( const GPlatesMaths::GeometryOnSphere *geometry)` | method | `unsigned int` | public | — |
| `d_number_of_points` | field | `int` | private | — |
| `visit_multi_point_on_sphere( GPlatesMaths::MultiPointOnSphere::non_null_ptr_to_const_type multi_point_on_sphere)` | method | `void` | private | — |
| `visit_point_on_sphere( GPlatesMaths::PointGeometryOnSphere::non_null_ptr_to_const_type /*point_on_sphere*/)` | method | `void` | private | — |
| `visit_polygon_on_sphere( GPlatesMaths::PolygonOnSphere::non_null_ptr_to_const_type polygon_on_sphere)` | method | `void` | private | — |
| `visit_polyline_on_sphere( GPlatesMaths::PolylineOnSphere::non_null_ptr_to_const_type polyline_on_sphere)` | method | `void` | private | — |

### `GPlatesFileIO::PlatesLineFormatWriter`

| Member | Kind | Type | Access | Description |
|---|---|---|---|---|
| `PlatesLineFormatWriter( const FileInfo &file_info)` | constructor | `None` | public | @pre is\_writable(file\_info) is true. |
| `~PlatesLineFormatWriter()` | destructor | `None` | public | — |
| `initialise_pre_feature_properties( const GPlatesModel::FeatureHandle &feature_handle)` | method | `bool` | private | — |
| `finalise_post_feature_properties( const GPlatesModel::FeatureHandle &feature_handle)` | method | `void` | private | — |
| `visit_gml_line_string( const GPlatesPropertyValues::GmlLineString &gml_line_string)` | method | `void` | private | — |
| `visit_gml_multi_point( const GPlatesPropertyValues::GmlMultiPoint &gml_multi_point)` | method | `void` | private | — |
| `visit_gml_orientable_curve( const GPlatesPropertyValues::GmlOrientableCurve &gml_orientable_curve)` | method | `void` | private | — |
| `visit_gml_point( const GPlatesPropertyValues::GmlPoint &gml_point)` | method | `void` | private | — |
| `visit_gml_polygon( const GPlatesPropertyValues::GmlPolygon &gml_polygon)` | method | `void` | private | — |
| `visit_gpml_constant_value( const GPlatesPropertyValues::GpmlConstantValue &gpml_constant_value)` | method | `void` | private | — |
| `print_header_lines( const OldPlatesHeader &old_plates_header)` | method | `void` | private | — |
| `FeatureAccumulator` | class | `None` | private | Accumulates feature geometry(s) when visiting a feature. |
| `d_feature_geometries` | field | `std::vector<GPlatesMaths::GeometryOnSphere::non_null_ptr_to_const_type>` | private | Stores geometries encountered while traversing a feature. |
| `d_output_file` | field | `boost::scoped_ptr<QFile>` | private | — |
| `d_output_stream` | field | `boost::scoped_ptr<QTextStream>` | private | — |
| `d_feature_accumulator` | field | `FeatureAccumulator` | private | — |
| `d_feature_header` | field | `PlatesLineFormatHeaderVisitor` | private | — |

## Free functions and macros

| Name | Kind | Type / body | Description |
|---|---|---|---|
| `get_number_of_points_in_geometry( GPlatesMaths::GeometryOnSphere::non_null_ptr_to_const_type geometry)` | function | `unsigned int` | Returns number of points in geometry. |
| `GPLATES_FILEIO_PLATESLINEFORMATWRITER_H` | macro | `None` | — |

## Notes

[[[PROSE notes unit=file-io/PlatesLineFormatWriter tier=3]]]
Replace this whole block, markers included, with invariants, ownership, threading or gotchas that are not visible in the tables. Write *None.* if there is nothing worth saying.
[[[/PROSE]]]

## Used by

| Unit | Component | References |
|---|---|---|
| [file-io/FeatureCollectionFileFormatRegistry](FeatureCollectionFileFormatRegistry.md) | file-io | 2 |
| [entry-points/gplates_demo_no_gui_main](../entry-points/gplates_demo_no_gui_main.md) | entry-points | 1 |

## Related

*None.*

## Explore

Run these from the `gplates-code` skill directory:

```bash
python scripts/gpq.py file src/file-io/PlatesLineFormatWriter.h
python scripts/gpq.py def GPlatesFileIO::PlatesLineFormatWriter --body
python scripts/gpq.py uses PlatesLineFormatWriter --kind class
python scripts/gpq.py hier PlatesLineFormatWriter
```
