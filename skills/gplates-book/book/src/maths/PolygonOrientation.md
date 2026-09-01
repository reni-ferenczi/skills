# PolygonOrientation

[Book TOC](../../TOC.md) · [maths](../../components/maths.md) · cluster Community 644 · tier 2

| Source file | Kind | Lines |
|---|---|---|
| `src/maths/PolygonOrientation.h` | C++ | 90 |
| `src/maths/PolygonOrientation.cc` | C++ | 274 |

## Overview

[[[PROSE overview unit=maths/PolygonOrientation tier=2]]]
Replace this whole block, markers included, with 1-3 paragraphs: what this unit is, why it exists, and how it fits the surrounding design. Do not restate the tables below.
[[[/PROSE]]]

## Declared types

| Name | Kind | Bases | Template | Subclasses | Description |
|---|---|---|---|---|---|
| [`GPlatesMaths::PolygonOrientation::Orientation`](#gplatesmathspolygonorientationorientation) | enum | — | — | 0 | Orientation of a polygon. |

## Members

### `GPlatesMaths::PolygonOrientation::Orientation`

| Member | Kind | Type | Access | Description |
|---|---|---|---|---|
| `CLOCKWISE` | enumerator | `None` | — | — |
| `COUNTERCLOCKWISE` | enumerator | `None` | — | — |

## Free functions and macros

| Name | Kind | Type / body | Description |
|---|---|---|---|
| `MAXIMUM_PROJECTION_ANGLE_DEGREES` | variable | `double` | If any 3D point (in polygon) is further than this angle from the polygon centroid then the gnomonic projection fails. |
| `calculate_polygon_ring_projected_signed_area( const PolygonOnSphere::ring_vertex_const_iterator &ring_vertex_begin, const PolygonOnSphere::ring_vertex_const_iterator &ring_vertex_end, const GnomonicProjection &gnomonic_projection)` | function | `boost::optional<real_t>` | Iterate through the vertices of the polygon ring and project onto the plane and calculate the signed area of the projected ring. |
| `GPLATES_MATHS_POLYGONORIENTATION_H` | macro | `None` | — |
| `calculate_polygon_orientation( const PolygonOnSphere &polygon)` | function | `Orientation` | Calculates the orientation of the vertices of polygon when viewed from above the globe (looking down on the globe's surface). |
| `calculate_polygon_exterior_ring_orientation( const PolygonOnSphere &polygon)` | function | `Orientation` | Calculates the orientation of the exterior ring of the specified polygon when viewed from above the globe (looking down on the globe's surface). |
| `calculate_polygon_interior_ring_orientation( const PolygonOnSphere &polygon, unsigned int interior_ring_index)` | function | `Orientation` | Calculates the orientation of the interior ring at the specified interior ring index of the specified polygon when viewed from above the globe (looking down on the globe's surface). |

## Notes

[[[PROSE notes unit=maths/PolygonOrientation tier=2]]]
Replace this whole block, markers included, with invariants, ownership, threading or gotchas that are not visible in the tables. Write *None.* if there is nothing worth saying.
[[[/PROSE]]]

## Used by

| Unit | Component | References |
|---|---|---|
| [qt-widgets/ExportResolvedTopologyOptionsWidget](../qt-widgets/ExportResolvedTopologyOptionsWidget.md) | qt-widgets | 22 |
| [app-logic/GeometryUtils](../app-logic/GeometryUtils.md) | app-logic | 17 |
| [maths/PolygonOnSphere](PolygonOnSphere.md) | maths | 13 |
| [maths/PolygonPartitioner](PolygonPartitioner.md) | maths | 11 |
| [file-io/ResolvedTopologicalGeometryExport](../file-io/ResolvedTopologicalGeometryExport.md) | file-io | 8 |
| [gui/ExportResolvedTopologyAnimationStrategy](../gui/ExportResolvedTopologyAnimationStrategy.md) | gui | 7 |
| [file-io/GMTFormatResolvedTopologicalGeometryExport](../file-io/GMTFormatResolvedTopologicalGeometryExport.md) | file-io | 6 |
| [view-operations/VisibleReconstructionGeometryExport](../view-operations/VisibleReconstructionGeometryExport.md) | view-operations | 6 |
| [file-io/OgrFormatResolvedTopologicalGeometryExport](../file-io/OgrFormatResolvedTopologicalGeometryExport.md) | file-io | 5 |
| [gui/ConfigModel](../gui/ConfigModel.md) | gui | 2 |
| [gui/ExportAnimationRegistry](../gui/ExportAnimationRegistry.md) | gui | 2 |
| [gui/FeaturePropertyTableModel](../gui/FeaturePropertyTableModel.md) | gui | 2 |
| [gui/FeatureTableModel](../gui/FeatureTableModel.md) | gui | 2 |
| [qt-widgets/deprecated/CreateFeatureIdListModel](../qt-widgets/deprecated/CreateFeatureIdListModel.md) | qt-widgets | 2 |
| [qt-widgets/CoRegistrationResultTableDialog](../qt-widgets/CoRegistrationResultTableDialog.md) | qt-widgets | 1 |

## Related

*None.*

## Explore

Run these from the `gplates-code` skill directory:

```bash
python scripts/gpq.py file src/maths/PolygonOrientation.h
python scripts/gpq.py def GPlatesMaths::PolygonOrientation::Orientation --body
python scripts/gpq.py uses Orientation --kind enum
```
