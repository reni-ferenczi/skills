# PlatesLineFormatGeometryExporter

[Book TOC](../../TOC.md) · [file-io](../../components/file-io.md) · cluster Community 839 · tier 3

| Source file | Kind | Lines |
|---|---|---|
| `src/file-io/PlatesLineFormatGeometryExporter.h` | C++ | 172 |
| `src/file-io/PlatesLineFormatGeometryExporter.cc` | C++ | 278 |

## Overview

[[[PROSE overview unit=file-io/PlatesLineFormatGeometryExporter tier=3]]]
Replace this whole block, markers included, with 1-3 paragraphs: what this unit is, why it exists, and how it fits the surrounding design. Do not restate the tables below.
[[[/PROSE]]]

## Declared types

| Name | Kind | Bases | Template | Subclasses | Description |
|---|---|---|---|---|---|
| [`(anonymous)::PenPositions::PenPosition`](#anonymouspenpositionspenposition) | enum | — | — | 0 | — |
| [`GPlatesFileIO::PlatesLineFormatGeometryExporter`](#gplatesfileioplateslineformatgeometryexporter) | class | [`GPlatesFileIO::GeometryExporter`](GeometryExporter.md)<br>[`GPlatesMaths::ConstGeometryOnSphereVisitor`](../maths/ConstGeometryOnSphereVisitor.md)<br>`boost::noncopyable` | — | 0 | This class is a ConstGeometryOnSphereVisitor which will output PLATES4 compatible pen commands for the geometry it visits. |

## Members

### `(anonymous)::PenPositions::PenPosition`

| Member | Kind | Type | Access | Description |
|---|---|---|---|---|
| `PEN_DRAW_TO_POINT` | enumerator | `None` | — | — |
| `PEN_SKIP_TO_POINT` | enumerator | `None` | — | — |

### `GPlatesFileIO::PlatesLineFormatGeometryExporter`

| Member | Kind | Type | Access | Description |
|---|---|---|---|---|
| `PlatesLineFormatGeometryExporter( QTextStream &output_stream, bool reverse_coordinate_order = false, bool polygon_terminating_point = true)` | constructor | `None` | public | — |
| `~PlatesLineFormatGeometryExporter()` | destructor | `None` | public | — |
| `export_geometry( GPlatesMaths::GeometryOnSphere::non_null_ptr_to_const_type geometry_ptr)` | method | `void` | public | Export a geometry and write the final terminating point. |
| `export_feature_geometries( GeometryForwardIter geometries_begin, GeometryForwardIter geometries_end)` | method | `void` | public | Export one or more geometries of a feature and write the final terminating point after the last geometry. |
| `d_stream_ptr` | field | `QTextStream` | private | The QTextStream we write to. |
| `d_reverse_coordinate_order` | field | `bool` | private | Should we go against the norm and write out coordinates using a (lon,lat) ordering? |
| `d_polygon_terminating_point` | field | `bool` | private | Should we convert gml:Polygons to something the PLATES line format can render, by adding an additional terminating point identical to the first point? |
| `visit_multi_point_on_sphere( GPlatesMaths::MultiPointOnSphere::non_null_ptr_to_const_type multi_point_on_sphere)` | method | `void` | private | Please keep these geometries ordered alphabetically. |
| `visit_point_on_sphere( GPlatesMaths::PointGeometryOnSphere::non_null_ptr_to_const_type point_on_sphere)` | method | `void` | private | — |
| `visit_polygon_on_sphere( GPlatesMaths::PolygonOnSphere::non_null_ptr_to_const_type polygon_on_sphere)` | method | `void` | private | — |
| `visit_polyline_on_sphere( GPlatesMaths::PolylineOnSphere::non_null_ptr_to_const_type polyline_on_sphere)` | method | `void` | private | — |
| `write_polygon_ring( const GPlatesMaths::PolygonOnSphere::ring_vertex_const_iterator &ring_vertex_begin, const GPlatesMaths::PolygonOnSphere::ring_vertex_const_iterator &ring_vertex_end)` | method | `void` | private | — |
| `write_terminating_point()` | method | `void` | private | Writes the terminating point to signal no more geometry(s) for a feature. |

## Free functions and macros

| Name | Kind | Type / body | Description |
|---|---|---|---|
| `print_plates_coordinate_line( QTextStream &stream, const GPlatesMaths::Real &lat, const GPlatesMaths::Real &lon, PenPositions::PenPosition pen, bool reverse_coordinate_order)` | function | `void` | Adapted from PlatesLineFormatWriter to work on a QTextStream. |
| `print_plates_feature_termination_line( QTextStream &stream)` | function | `void` | — |
| `print_plates_coordinate_line( QTextStream &stream, const GPlatesMaths::PointOnSphere &pos, PenPositions::PenPosition pen, bool reverse_coordinate_order)` | function | `void` | — |
| `GPLATES_FILEIO_PLATESLINEFORMATGEOMETRYEXPORTER_H` | macro | `None` | — |

## Notes

[[[PROSE notes unit=file-io/PlatesLineFormatGeometryExporter tier=3]]]
Replace this whole block, markers included, with invariants, ownership, threading or gotchas that are not visible in the tables. Write *None.* if there is nothing worth saying.
[[[/PROSE]]]

## Used by

| Unit | Component | References |
|---|---|---|
| [file-io/PlatesLineFormatWriter](PlatesLineFormatWriter.md) | file-io | 3 |
| [qt-widgets/ExportCoordinatesDialog](../qt-widgets/ExportCoordinatesDialog.md) | qt-widgets | 3 |

## Related

*None.*

## Explore

Run these from the `gplates-code` skill directory:

```bash
python scripts/gpq.py file src/file-io/PlatesLineFormatGeometryExporter.h
python scripts/gpq.py def GPlatesFileIO::PlatesLineFormatGeometryExporter --body
python scripts/gpq.py uses PlatesLineFormatGeometryExporter --kind class
python scripts/gpq.py hier PlatesLineFormatGeometryExporter
```
