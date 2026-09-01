# GMTFormatGeometryExporter

[Book TOC](../../TOC.md) · [file-io](../../components/file-io.md) · cluster Community 96 · tier 2

| Source file | Kind | Lines |
|---|---|---|
| `src/file-io/GMTFormatGeometryExporter.h` | C++ | 126 |
| `src/file-io/GMTFormatGeometryExporter.cc` | C++ | 241 |

## Overview

[[[PROSE overview unit=file-io/GMTFormatGeometryExporter tier=2]]]
Replace this whole block, markers included, with 1-3 paragraphs: what this unit is, why it exists, and how it fits the surrounding design. Do not restate the tables below.
[[[/PROSE]]]

## Declared types

| Name | Kind | Bases | Template | Subclasses | Description |
|---|---|---|---|---|---|
| [`GPlatesFileIO::GMTFormatGeometryExporter`](#gplatesfileiogmtformatgeometryexporter) | class | [`GPlatesMaths::ConstGeometryOnSphereVisitor`](../maths/ConstGeometryOnSphereVisitor.md)<br>[`GeometryExporter`](GeometryExporter.md)<br>`boost::noncopyable` | — | 0 | This class is a ConstGeometryOnSphereVisitor which will output GMT xy points format for the geometry it visits. |

## Members

### `GPlatesFileIO::GMTFormatGeometryExporter`

| Member | Kind | Type | Access | Description |
|---|---|---|---|---|
| `GMTFormatGeometryExporter( QTextStream &output_stream, bool reverse_coordinate_order = false, bool polygon_terminating_point = true)` | constructor | `None` | public | — |
| `~GMTFormatGeometryExporter()` | destructor | `None` | public | — |
| `export_geometry( GPlatesMaths::GeometryOnSphere::non_null_ptr_to_const_type geometry_ptr)` | method | `void` | public | You should call this method on the geometry you wish to write, rather than directly calling -\>accept\_visitor(\*this) on the geometry, since we need to write the final terminating marker. |
| `visit_multi_point_on_sphere( GPlatesMaths::MultiPointOnSphere::non_null_ptr_to_const_type multi_point_on_sphere)` | method | `void` | public | Please keep these geometries ordered alphabetically. |
| `visit_point_on_sphere( GPlatesMaths::PointGeometryOnSphere::non_null_ptr_to_const_type point_on_sphere)` | method | `void` | public | — |
| `visit_polygon_on_sphere( GPlatesMaths::PolygonOnSphere::non_null_ptr_to_const_type polygon_on_sphere)` | method | `void` | public | — |
| `visit_polyline_on_sphere( GPlatesMaths::PolylineOnSphere::non_null_ptr_to_const_type polyline_on_sphere)` | method | `void` | public | — |
| `d_stream_ptr` | field | `QTextStream` | private | The QTextStream we write to. |
| `d_reverse_coordinate_order` | field | `bool` | private | Should we go against the norm and write out coordinates using a (lat,lon) ordering? |
| `d_polygon_terminating_point` | field | `bool` | private | Should we convert gml:Polygons to something the GMT xy format can render, by adding an additional terminating point identical to the first point? |
| `write_polygon_ring( const GPlatesMaths::PolygonOnSphere::ring_vertex_const_iterator &ring_vertex_begin, const GPlatesMaths::PolygonOnSphere::ring_vertex_const_iterator &ring_vertex_end)` | method | `void` | private | — |

## Free functions and macros

| Name | Kind | Type / body | Description |
|---|---|---|---|
| `print_gmt_coordinate_line( QTextStream &stream, const GPlatesMaths::Real &lat, const GPlatesMaths::Real &lon, bool reverse_coordinate_order)` | function | `void` | Adapted from GMTFormatWriter to work on a QTextStream. |
| `print_gmt_feature_termination_line( QTextStream &stream)` | function | `void` | — |
| `print_gmt_coordinate_line( QTextStream &stream, const GPlatesMaths::PointOnSphere &pos, bool reverse_coordinate_order)` | function | `void` | — |
| `GPLATES_FILEIO_GMTFORMATGEOMETRYEXPORTER_H` | macro | `None` | — |

## Notes

[[[PROSE notes unit=file-io/GMTFormatGeometryExporter tier=2]]]
Replace this whole block, markers included, with invariants, ownership, threading or gotchas that are not visible in the tables. Write *None.* if there is nothing worth saying.
[[[/PROSE]]]

## Used by

| Unit | Component | References |
|---|---|---|
| [qt-widgets/ExportCoordinatesDialog](../qt-widgets/ExportCoordinatesDialog.md) | qt-widgets | 13 |
| [file-io/GMTFormatResolvedTopologicalGeometryExport](GMTFormatResolvedTopologicalGeometryExport.md) | file-io | 6 |
| [file-io/CitcomsGMTFormatResolvedTopologicalBoundaryExport](CitcomsGMTFormatResolvedTopologicalBoundaryExport.md) | file-io | 3 |
| [file-io/GMTFormatReconstructedFeatureGeometryExport](GMTFormatReconstructedFeatureGeometryExport.md) | file-io | 3 |
| [file-io/GMTFormatWriter](GMTFormatWriter.md) | file-io | 3 |

## Related

*None.*

## Explore

Run these from the `gplates-code` skill directory:

```bash
python scripts/gpq.py file src/file-io/GMTFormatGeometryExporter.h
python scripts/gpq.py def GPlatesFileIO::GMTFormatGeometryExporter --body
python scripts/gpq.py uses GMTFormatGeometryExporter --kind class
python scripts/gpq.py hier GMTFormatGeometryExporter
```
