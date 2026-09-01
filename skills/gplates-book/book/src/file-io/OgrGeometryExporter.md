# OgrGeometryExporter

[Book TOC](../../TOC.md) · [file-io](../../components/file-io.md) · cluster Community 696 · tier 2

| Source file | Kind | Lines |
|---|---|---|
| `src/file-io/OgrGeometryExporter.h` | C++ | 183 |
| `src/file-io/OgrGeometryExporter.cc` | C++ | 190 |

## Overview

`OgrGeometryExporter` adapts the visitor-based `GeometryOnSphere` hierarchy to
`OgrWriter`'s per-geometry-type write calls. Each call to `export_geometry` or
`export_geometries` clears any geometries buffered from the previous call, visits
the incoming geometry (or geometries), sorting each one into its own bucket by
concrete type (`d_point_geometries`, `d_multi_point_geometries`,
`d_polyline_geometries`, `d_polygon_geometries`), then writes each non-empty bucket
out through `d_ogr_writer`. A bucket holding exactly one geometry is written with
the corresponding single-geometry `OgrWriter` call; a bucket holding more than one
is written as a multi-geometry feature, so a feature with several points of the
same type collapses into one multi-point rather than several point features.

`export_geometries` exists specifically for callers that want a whole sequence of
geometries treated as one feature: same-type geometries within the sequence are
merged into a single multi-part feature, but geometries of different types still
end up in separate files, since a single OGR feature (and, for the Shapefile
driver, a single file) can only hold one geometry type. The `multiple_geometry_types`
and `wrap_to_dateline` constructor flags are passed straight through to `OgrWriter`,
which owns the actual output file(s).

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

- Owns its `OgrWriter` (`d_ogr_writer`) via a raw pointer allocated in the
  constructor and deleted in the destructor; the class is `boost::noncopyable`, so
  this ownership is never duplicated.
- A single feature whose geometries mix types (e.g. a point and a polyline) gets
  split across the OGR writer's separate per-type outputs — the comment in
  `write_geometries()` calls this out explicitly as "splitting up a feature across
  different files".
- The OGR Shapefile driver can merge two nested, non-intersecting polygons into one
  polygon with exterior/interior rings, re-orienting the rings itself; the code
  does not rely on this and instead passes `PolygonOnSphere`'s own exterior and
  interior rings straight through to OGR.

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
