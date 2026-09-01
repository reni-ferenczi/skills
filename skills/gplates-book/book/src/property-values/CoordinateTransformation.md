# CoordinateTransformation

[Book TOC](../../TOC.md) · [property-values](../../components/property-values.md) · cluster Community 1049 · tier 2

| Source file | Kind | Lines |
|---|---|---|
| `src/property-values/CoordinateTransformation.h` | C++ | 244 |
| `src/property-values/CoordinateTransformation.cc` | C++ | 261 |

## Overview

`CoordinateTransformation` wraps GDAL/OGR's `OGRCoordinateTransformation` to convert
coordinates between two `SpatialReferenceSystem`s, most commonly between a raster's or
shapefile's native projection and WGS84. The two `create()` overloads distinguish the
common cases from the fallible one: the no-argument form always succeeds and produces
an identity transform (source and target both WGS84), while the two-SRS form returns
`boost::none` when GDAL cannot build a transformation between the given systems,
rather than throwing.

Internally, `create()` checks whether the source and target systems are the same
(via `OGRSpatialReference::IsSame`) and substitutes the identity transform in that
case, so `is_identity_transform()` covers both the explicit no-argument construction
and an SRS pair that happens to match. The `Coord` struct bundles an (x, y) pair with
an optional z (height above geoid), and every `transform`/`transform_in_place`
overload — single coordinate, `std::vector<Coord>`, or raw coordinate arrays — funnels
through the same in-place path so identity transforms are a no-op rather than a
special-cased copy.

## Declared types

| Name | Kind | Bases | Template | Subclasses | Description |
|---|---|---|---|---|---|
| [`GPlatesPropertyValues::CoordinateTransformation`](#gplatespropertyvaluescoordinatetransformation) | class | [`GPlatesUtils::ReferenceCount<CoordinateTransformation>`](../utils/ReferenceCount.md) | — | 0 | Transforms coordinates from one spatial reference system to another. |

## Members

### `GPlatesPropertyValues::CoordinateTransformation`

| Member | Kind | Type | Access | Description |
|---|---|---|---|---|
| `non_null_ptr_type` | typedef | `GPlatesUtils::non_null_intrusive_ptr<CoordinateTransformation>` | public | — |
| `non_null_ptr_to_const_type` | typedef | `GPlatesUtils::non_null_intrusive_ptr<const CoordinateTransformation>` | public | — |
| `Coord` | struct | `None` | public | A coordinate of (x,y) and optional z (where z is the height above geoid). |
| `create()` | method | `non_null_ptr_type` | public | Creates a coordinate transformation that does nothing (identity transform). |
| `create( const SpatialReferenceSystem::non_null_ptr_to_const_type &source_spatial_reference_system, const SpatialReferenceSystem::non_null_ptr_to_const_type &target_spatial_reference_system = SpatialReferenceSystem::get_WGS84())` | method | `boost::optional<non_null_ptr_type>` | public | Creates a coordinate transformation from source\_spatial\_reference\_system to target\_spatial\_reference\_system. target\_spatial\_reference\_system defaults to the standard "WGS84" coordinate system. |
| `~CoordinateTransformation()` | destructor | `None` | public | — |
| `get_source_spatial_reference_system()` | method | `SpatialReferenceSystem::non_null_ptr_to_const_type` | public | Returns the source spatial reference system. |
| `get_target_spatial_reference_system()` | method | `SpatialReferenceSystem::non_null_ptr_to_const_type` | public | Returns the target spatial reference system. |
| `is_identity_transform()` | method | `bool` | public | Returns true if both the source and target spatial reference systems are the same. |
| `transform( const Coord &coord)` | method | `boost::optional<Coord>` | public | Transform an (x,y\[,z\]) coordinate from the source to the target spatial reference system. |
| `transform_in_place( Coord &coord)` | method | `bool` | public | Same as transform but converts coordinates in place. |
| `transform_in_place( double *x, double *y, double *z = NULL)` | method | `bool` | public | Same as transform but converts coordinates in place. |
| `transform( const std::vector<Coord> &transform_input, std::vector<Coord> &transform_output)` | method | `bool` | public | Transform a sequence of (x,y\[,z\]) coordinates from source to target spatial reference system. |
| `transform_in_place( std::vector<Coord> &coords)` | method | `bool` | public | Same as transform but converts coordinates in place. |
| `transform_in_place( unsigned int count, double *x, double *y, double *z = NULL)` | method | `bool` | public | Same as transform but converts coordinates in place. x and y (and optionally z) are expected to be arrays containing count elements each to be transformed in place. |
| `d_source_srs` | field | `SpatialReferenceSystem::non_null_ptr_to_const_type` | private | — |
| `d_target_srs` | field | `SpatialReferenceSystem::non_null_ptr_to_const_type` | private | — |
| `d_ogr_coordinate_transformation` | field | `boost::scoped_ptr<OGRCoordinateTransformation>` | private | No coordinate transformation (NULL) means identity transform. |
| `CoordinateTransformation()` | constructor | `None` | private | — |
| `CoordinateTransformation( const SpatialReferenceSystem::non_null_ptr_to_const_type &source_srs, const SpatialReferenceSystem::non_null_ptr_to_const_type &target_srs, std::unique_ptr<OGRCoordinateTransformation> ogr_coordinate_transformation)` | constructor | `None` | private | — |

## Free functions and macros

| Name | Kind | Type / body | Description |
|---|---|---|---|
| `GPLATES_PROPERTY_VALUES_COORDINATETRANSFORMATION_H` | macro | `None` | — |
| `DISABLE_MSVC_WARNING` | variable | `PUSH_MSVC_WARNINGS` | — |

## Notes

- `create(source, target)` copies both spatial reference systems internally, so the
  caller is free to modify or destroy the SRS objects it passed in afterwards.
- A failed transform (`OGRCoordinateTransformation::Transform` returning false) leaves
  the output coordinate(s) unmodified for the single-`Coord` overloads, but for the
  batch `transform(vector, vector)` overload the output vector is left unmodified only
  as a whole — a partial failure does not commit a partial result.
- `d_ogr_coordinate_transformation` being null is the identity-transform marker, not
  an error state; `boost::scoped_ptr` requires `OGRCoordinateTransformation` to be a
  complete type at the point of the class's constructors/destructor, which is why
  those are defined out-of-line in the `.cc` even though they do nothing else.

## Used by

| Unit | Component | References |
|---|---|---|
| [file-io/OgrWriter](../file-io/OgrWriter.md) | file-io | 16 |
| [opengl/GLMultiResolutionRaster](../opengl/GLMultiResolutionRaster.md) | opengl | 14 |
| [file-io/GsmlPropertyHandlers](../file-io/GsmlPropertyHandlers.md) | file-io | 12 |
| [app-logic/RasterLayerProxy](../app-logic/RasterLayerProxy.md) | app-logic | 8 |
| [qt-widgets/ImportScalarField3DDialog](../qt-widgets/ImportScalarField3DDialog.md) | qt-widgets | 8 |
| [file-io/OgrReader](../file-io/OgrReader.md) | file-io | 6 |
| [opengl/GLScalarField3DGenerator](../opengl/GLScalarField3DGenerator.md) | opengl | 6 |
| [qt-widgets/ScalarField3DGeoreferencingPage](../qt-widgets/ScalarField3DGeoreferencingPage.md) | qt-widgets | 1 |

## Related

*None.*

## Explore

Run these from the `gplates-code` skill directory:

```bash
python scripts/gpq.py file src/property-values/CoordinateTransformation.h
python scripts/gpq.py def GPlatesPropertyValues::CoordinateTransformation --body
python scripts/gpq.py uses CoordinateTransformation --kind class
python scripts/gpq.py hier CoordinateTransformation
```
