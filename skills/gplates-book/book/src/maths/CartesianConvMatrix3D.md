# CartesianConvMatrix3D

[Book TOC](../../TOC.md) · [maths](../../components/maths.md) · cluster Community 895 · tier 2

| Source file | Kind | Lines |
|---|---|---|
| `src/maths/CartesianConvMatrix3D.h` | C++ | 189 |
| `src/maths/CartesianConvMatrix3D.cc` | C++ | 161 |

## Overview

[[[PROSE overview unit=maths/CartesianConvMatrix3D tier=2]]]
Replace this whole block, markers included, with 1-3 paragraphs: what this unit is, why it exists, and how it fits the surrounding design. Do not restate the tables below.
[[[/PROSE]]]

## Declared types

| Name | Kind | Bases | Template | Subclasses | Description |
|---|---|---|---|---|---|
| [`GPlatesMaths::CartesianConvMatrix3D`](#gplatesmathscartesianconvmatrix3d) | class | — | — | 0 | A 3x3 matrix used to convert the components of a global geocentric Cartesian Vector3D (x, y, z) into the components of a local Cartesian Vector3D (north, east, down) at a given PointOnSphere. |

## Members

### `GPlatesMaths::CartesianConvMatrix3D`

| Member | Kind | Type | Access | Description |
|---|---|---|---|---|
| `CartesianConvMatrix3D( const PointOnSphere &pos)` | constructor | `None` | public | Create a cartesian conversion matrix to operate at the PointOnSphere pos. |
| `d_north` | field | `Vector3D` | private | — |
| `d_east` | field | `Vector3D` | private | — |
| `d_down` | field | `Vector3D` | private | — |

## Free functions and macros

| Name | Kind | Type / body | Description |
|---|---|---|---|
| `_GPLATES_MATHS_CARTESIANCONVMATRIX3D_H_` | macro | `None` | — |
| `convert_from_geocentric_to_north_east_down( const CartesianConvMatrix3D &ccm, const Vector3D &geocentric_vec)` | function | `Vector3D` | Converts a 3D vector in the global geocentric coordinate system to a 3D vector in a local North/East/Down coordinate frame (determined by ccm). |
| `convert_from_north_east_down_to_geocentric( const CartesianConvMatrix3D &ccm, const Vector3D &north_east_down_vec)` | function | `Vector3D` | Converts a 3D vector in a local North/East/Down coordinate frame (determined by ccm) to a 3D vector in the global geocentric coordinate system. |
| `convert_from_geocentric_to_magnitude_azimuth_inclination( const CartesianConvMatrix3D &ccm, const Vector3D &geocentric_vec)` | function | `boost::tuple<real_t/*magnitude*/, real_t/*azimuth*/, real_t/*inclination*/>` | Converts a 3D vector in the global geocentric coordinate system to a tuple of (magnitude, azimuth, inclination) coordinates (in a local North/East/Down coordinate frame determined by ccm). |
| `convert_from_magnitude_azimuth_inclination_to_geocentric( const CartesianConvMatrix3D &ccm, const boost::tuple<real_t/*magnitude*/, real_t/*azimuth*/, real_t/*inclination*/> & magnitude_azimuth_inclination)` | function | `Vector3D` | Converts a tuple of (magnitude, azimuth, inclination) coordinates (in a local North/East/Down coordinate frame determined by ccm) to a 3D vector in the global geocentric coordinate system. |
| `convert_from_north_east_down_to_magnitude_azimuth_inclination( const Vector3D &north_east_down_vec)` | function | `boost::tuple<real_t/*magnitude*/, real_t/*azimuth*/, real_t/*inclination*/>` | Converts a 3D vector in a local North/East/Down coordinate frame to a tuple of (magnitude, azimuth, inclination) coordinates in the same coordinate frame. |
| `convert_from_magnitude_azimuth_inclination_to_north_east_down( const boost::tuple<real_t/*magnitude*/, real_t/*azimuth*/, real_t/*inclination*/> & magnitude_azimuth_inclination)` | function | `Vector3D` | Converts a tuple of (magnitude, azimuth, inclination) coordinates in a local North/East/Down coordinate frame to a 3D vector in the coordinate frame. |
| `operator==( const CartesianConvMatrix3D &ccm1, const CartesianConvMatrix3D &ccm2)` | operator | `bool` | — |
| `operator!=( const CartesianConvMatrix3D &ccm1, const CartesianConvMatrix3D &ccm2)` | operator | `bool` | — |

## Notes

[[[PROSE notes unit=maths/CartesianConvMatrix3D tier=2]]]
Replace this whole block, markers included, with invariants, ownership, threading or gotchas that are not visible in the tables. Write *None.* if there is nothing worth saying.
[[[/PROSE]]]

## Used by

| Unit | Component | References |
|---|---|---|
| [maths/CalculateVelocity](CalculateVelocity.md) | maths | 9 |

## Related

*None.*

## Explore

Run these from the `gplates-code` skill directory:

```bash
python scripts/gpq.py file src/maths/CartesianConvMatrix3D.h
python scripts/gpq.py def GPlatesMaths::CartesianConvMatrix3D --body
python scripts/gpq.py uses CartesianConvMatrix3D --kind class
python scripts/gpq.py hier CartesianConvMatrix3D
```
