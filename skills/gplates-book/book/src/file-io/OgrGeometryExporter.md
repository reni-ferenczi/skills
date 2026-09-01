# OgrGeometryExporter

[Book TOC](../../TOC.md) · [file-io](../../components/file-io.md) · cluster Community 696 · tier 2

| Source file | Kind | Lines |
|---|---|---|
| `src/file-io/OgrGeometryExporter.h` | C++ | 183 |
| `src/file-io/OgrGeometryExporter.cc` | C++ | 190 |

## Overview

[[[PROSE overview unit=file-io/OgrGeometryExporter tier=2]]]
Replace this whole block, markers included, with 1-3 paragraphs: what this unit is, why it exists, and how it fits the surrounding design. Do not restate the tables below.
[[[/PROSE]]]

## Declared types

| Name | Kind | Bases | Template | Subclasses | Description |
|---|---|---|---|---|---|
| [`GPlatesFileIO::OgrGeometryExporter`](#gplatesfileioogrgeometryexporter) | class | [`GPlatesMaths::ConstGeometryOnSphereVisitor`](../maths/ConstGeometryOnSphereVisitor.md)<br>[`GeometryExporter`](GeometryExporter.md)<br>`boost::noncopyable` | — | 0 | — |

## Members

### `GPlatesFileIO::OgrGeometryExporter`

| Member | Kind | Type | Access | Description |
|---|---|---|---|---|
| `OgrGeometryExporter( QString &filename, bool multiple_geometry_types, bool wrap_to_dateline)` | constructor | `None` | public | If all the geometry types to be written are not the same type then multiple\_geometry\_types should be set to true (this will create multiple exported files - one per geometry type encountered). |
| `~OgrGeometryExporter()` | destructor | `None` | public | — |
| `export_geometry( GPlatesMaths::GeometryOnSphere::non_null_ptr_to_const_type geometry_ptr)` | method | `void` | public | — |
| `export_geometry( GPlatesMaths::GeometryOnSphere::non_null_ptr_to_const_type geometry_ptr, GPlatesPropertyValues::GpmlKeyValueDictionary::non_null_ptr_to_const_type key_value_dictionary)` | method | `void` | public | — |
| `export_geometries( ForwardGeometryIter geometries_begin, ForwardGeometryIter geometries_end, boost::optional<GPlatesPropertyValues::GpmlKeyValueDictionary::non_null_ptr_to_const_type> key_value_dictionary)` | method | `void` | public | Export a sequence of geometries. |
| `visit_multi_point_on_sphere( GPlatesMaths::MultiPointOnSphere::non_null_ptr_to_const_type multi_point_on_sphere)` | method | `void` | private | Please keep these geometries ordered alphabetically. |
| `visit_point_on_sphere( GPlatesMaths::PointGeometryOnSphere::non_null_ptr_to_const_type point_on_sphere)` | method | `void` | private | — |
| `visit_polygon_on_sphere( GPlatesMaths::PolygonOnSphere::non_null_ptr_to_const_type polygon_on_sphere)` | method | `void` | private | — |
| `visit_polyline_on_sphere( GPlatesMaths::PolylineOnSphere::non_null_ptr_to_const_type polyline_on_sphere)` | method | `void` | private | — |
| `clear_geometries()` | method | `void` | private | — |
| `write_geometries()` | method | `void` | private | — |
| `d_filename` | field | `QString` | private | — |
| `d_ogr_writer` | field | `OgrWriter` | private | — |
| `d_key_value_dictionary` | field | `boost::optional<GPlatesPropertyValues::GpmlKeyValueDictionary::non_null_ptr_to_const_type>` | private | — |
| `d_point_geometries` | field | `std::vector<GPlatesMaths::PointOnSphere>` | private | Store various geometries encountered in each feature. |
| `d_multi_point_geometries` | field | `std::vector<GPlatesMaths::MultiPointOnSphere::non_null_ptr_to_const_type>` | private | — |
| `d_polyline_geometries` | field | `std::vector<GPlatesMaths::PolylineOnSphere::non_null_ptr_to_const_type>` | private | — |
| `d_polygon_geometries` | field | `std::vector<GPlatesMaths::PolygonOnSphere::non_null_ptr_to_const_type>` | private | — |

## Free functions and macros

| Name | Kind | Type / body | Description |
|---|---|---|---|
| `GPLATES_FILEIO_SHAPEFILEGEOMETRYEXPORTER_H` | macro | `None` | — |

## Notes

[[[PROSE notes unit=file-io/OgrGeometryExporter tier=2]]]
Replace this whole block, markers included, with invariants, ownership, threading or gotchas that are not visible in the tables. Write *None.* if there is nothing worth saying.
[[[/PROSE]]]

## Used by

| Unit | Component | References |
|---|---|---|
| [file-io/OgrFormatResolvedTopologicalGeometryExport](OgrFormatResolvedTopologicalGeometryExport.md) | file-io | 7 |
| [file-io/OgrFormatReconstructedFeatureGeometryExport](OgrFormatReconstructedFeatureGeometryExport.md) | file-io | 3 |
| [qt-widgets/ExportCoordinatesDialog](../qt-widgets/ExportCoordinatesDialog.md) | qt-widgets | 3 |
| [file-io/OgrFormatFlowlineExport](OgrFormatFlowlineExport.md) | file-io | 2 |
| [file-io/OgrFormatMotionPathExport](OgrFormatMotionPathExport.md) | file-io | 2 |

## Related

*None.*

## Explore

Run these from the `gplates-code` skill directory:

```bash
python scripts/gpq.py file src/file-io/OgrGeometryExporter.h
python scripts/gpq.py def GPlatesFileIO::OgrGeometryExporter --body
python scripts/gpq.py uses OgrGeometryExporter --kind class
python scripts/gpq.py hier OgrGeometryExporter
```
