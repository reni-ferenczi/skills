# GMTFormatGeometryExporter

[Book TOC](../../TOC.md) · [file-io](../../components/file-io.md) · cluster Community 96 · tier 2

| Source file | Kind | Lines |
|---|---|---|
| `src/file-io/GMTFormatGeometryExporter.h` | C++ | 126 |
| `src/file-io/GMTFormatGeometryExporter.cc` | C++ | 241 |

## Overview

`GMTFormatGeometryExporter` renders a `GeometryOnSphere` as GMT "xy" point records by implementing `ConstGeometryOnSphereVisitor`: each `visit_*` method converts its geometry's vertices to `LatLonPoint`s and writes them as fixed-width coordinate lines via `print_gmt_coordinate_line()`, then closes the feature with a `>` termination line. Callers are expected to go through `export_geometry()` rather than calling `accept_visitor()` directly, since the exporter itself is responsible for writing that trailing terminator.

Polygon rings get special handling in `write_polygon_ring()`: because the GMT xy format has no notion of a closed ring, the exporter repeats the ring's first vertex at the end (controlled by `d_polygon_terminating_point`, on by default) so downstream GMT tools render a closed loop; each interior ring is written and terminated the same way as the exterior ring. `d_reverse_coordinate_order` lets a caller opt out of GMT's normal (lon, lat) ordering and write (lat, lon) instead, matching the PLATES4 line format convention used elsewhere in the file-io component.

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

- The exporter does not own `d_stream_ptr`; the caller must keep the `QTextStream` (and its underlying device) alive for the exporter's lifetime.
- `export_geometry()` must be used instead of calling `accept_visitor()` on the geometry directly, or the required `>` termination line will be missing from the output.
- The trailing `>` written by `print_gmt_feature_termination_line()` carries no newline, since a GMT header line may follow on the same line; a caller writing raw text after export must account for this.

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
