# SimpleGlobeOrientation

[Book TOC](../../TOC.md) · [gui](../../components/gui.md) · cluster Community 524 · tier 2

| Source file | Kind | Lines |
|---|---|---|
| `src/gui/SimpleGlobeOrientation.h` | C++ | 250 |
| `src/gui/SimpleGlobeOrientation.cc` | C++ | 247 |

## Overview

[[[PROSE overview unit=gui/SimpleGlobeOrientation tier=2]]]
Replace this whole block, markers included, with 1-3 paragraphs: what this unit is, why it exists, and how it fits the surrounding design. Do not restate the tables below.
[[[/PROSE]]]

## Declared types

| Name | Kind | Bases | Template | Subclasses | Description |
|---|---|---|---|---|---|
| [`GPlatesGui::SimpleGlobeOrientation`](#gplatesguisimpleglobeorientation) | class | `QObject`<br>[`GlobeOrientation`](GlobeOrientation.md)<br>`boost::noncopyable` | — | 0 | This class represents the simplest type of globe orientation: one which is unrelated to any other globe orientation (that is, changes to this globe orientation do not affect any other globe orientation, and vice-versa). |

## Members

### `GPlatesGui::SimpleGlobeOrientation`

| Member | Kind | Type | Access | Description |
|---|---|---|---|---|
| `SimpleGlobeOrientation()` | constructor | `None` | public | — |
| `~SimpleGlobeOrientation()` | destructor | `None` | public | — |
| `set_rotation( const GPlatesMaths::Rotation &rotation /*bool should_emit_external_signal = true */)` | method | `void` | public | Set the accumulated rotation of the globe. |
| `orient_geometry( GPlatesMaths::GeometryOnSphere::non_null_ptr_to_const_type geom)` | method | `GPlatesMaths::GeometryOnSphere::non_null_ptr_to_const_type` | public | Apply the accumulated rotation of the globe to the supplied geometry. |
| `orient_point( const GPlatesMaths::PointOnSphere &pos)` | method | `GPlatesMaths::PointOnSphere` | public | Apply the accumulated rotation of the globe to the supplied point. |
| `reverse_orient_point( const GPlatesMaths::PointOnSphere &pos)` | method | `GPlatesMaths::PointOnSphere` | public | Apply the reverse of the accumulated rotation of the globe to the supplied point. |
| `set_new_handle_at_pos( const GPlatesMaths::PointOnSphere &pos)` | method | `void` | public | Set a new handle at the given position. |
| `move_handle_to_pos( const GPlatesMaths::PointOnSphere &pos)` | method | `void` | public | Move the already-set handle to the given position, changing the orientation of the globe in the process. |
| `move_camera_up( double zoom_factor = 1.0)` | method | `void` | public | For keyboard camera controls to use: nudge the camera 'up' by a few degrees. |
| `move_camera_down( double zoom_factor = 1.0)` | method | `void` | public | For keyboard camera controls to use: nudge the camera 'down' by a few degrees. |
| `move_camera_left( double zoom_factor = 1.0)` | method | `void` | public | For keyboard camera controls to use: nudge the camera 'left' by a few degrees. |
| `move_camera_right( double zoom_factor = 1.0)` | method | `void` | public | For keyboard camera controls to use: nudge the camera 'right' by a few degrees. |
| `rotate_camera_clockwise()` | method | `void` | public | For keyboard camera controls to use: rotate the camera clockwise by a few degrees. |
| `rotate_camera_anticlockwise()` | method | `void` | public | For keyboard camera controls to use: rotate the camera anticlockwise by a few degrees. |
| `rotate_camera( double angle)` | method | `void` | public | Rotates the camera by an arbitrary angle, in degrees. |
| `orient_poles_vertically()` | method | `void` | public | Rotate the camera such that the poles are oriented vertically (with North at the top of the screen). |
| `orientation_changed()` | method | `void` | public | — |
| `s_nudge_camera_amount` | field | `double` | private | How far to nudge or rotate the camera when using the move\_camera\_\* functions, in degrees. |
| `d_handle_pos` | field | `GPlatesMaths::PointOnSphere` | private | The current position of the "handle". |
| `d_accum_rot` | field | `GPlatesMaths::Rotation` | private | The accumulated rotation of the globe. |
| `d_rev_accum_rot` | field | `GPlatesMaths::Rotation` | private | The reverse of the accumulated rotation of the globe. |

## Free functions and macros

| Name | Kind | Type / body | Description |
|---|---|---|---|
| `s_nudge_camera_amount` | variable | `double` | — |
| `project_vector_onto_plane( const GPlatesMaths::Vector3D &normal_to_plane, const GPlatesMaths::Vector3D &v)` | function | `GPlatesMaths::Vector3D` | Projects the vector v onto the plane defined by normal\_to\_plane. |
| `calculate_rotation_angle_for_coplanar_vectors( const GPlatesMaths::Vector3D &normal_to_plane, const GPlatesMaths::Vector3D &v1, const GPlatesMaths::Vector3D &v2)` | function | `GPlatesMaths::real_t` | Calculates the angle (in radians) required to rotate vector v1 to line up with vector v2. |
| `GPLATES_GUI_SIMPLEGLOBEORIENTATION_H` | macro | `None` | — |

## Notes

[[[PROSE notes unit=gui/SimpleGlobeOrientation tier=2]]]
Replace this whole block, markers included, with invariants, ownership, threading or gotchas that are not visible in the tables. Write *None.* if there is nothing worth saying.
[[[/PROSE]]]

## Used by

| Unit | Component | References |
|---|---|---|
| [qt-widgets/ModifyReconstructionPoleWidget](../qt-widgets/ModifyReconstructionPoleWidget.md) | qt-widgets | 11 |
| [gui/Globe](Globe.md) | gui | 8 |
| [qt-widgets/ViewportWindow](../qt-widgets/ViewportWindow.md) | qt-widgets | 6 |
| [qt-widgets/GlobeAndMapWidget](../qt-widgets/GlobeAndMapWidget.md) | qt-widgets | 3 |
| [qt-widgets/GlobeCanvas](../qt-widgets/GlobeCanvas.md) | qt-widgets | 3 |
| [qt-widgets/deprecated/CreateTopologyWidget](../qt-widgets/deprecated/CreateTopologyWidget.md) | qt-widgets | 3 |
| [view-operations/ChangeLightDirectionOperation](../view-operations/ChangeLightDirectionOperation.md) | view-operations | 2 |

## Related

*None.*

## Explore

Run these from the `gplates-code` skill directory:

```bash
python scripts/gpq.py file src/gui/SimpleGlobeOrientation.h
python scripts/gpq.py def GPlatesGui::SimpleGlobeOrientation --body
python scripts/gpq.py uses SimpleGlobeOrientation --kind class
python scripts/gpq.py hier SimpleGlobeOrientation
```
