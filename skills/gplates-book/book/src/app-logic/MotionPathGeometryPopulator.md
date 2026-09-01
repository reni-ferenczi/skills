# MotionPathGeometryPopulator

[Book TOC](../../TOC.md) · [app-logic](../../components/app-logic.md) · cluster Community 805 · tier 3

| Source file | Kind | Lines |
|---|---|---|
| `src/app-logic/MotionPathGeometryPopulator.h` | C++ | 127 |
| `src/app-logic/MotionPathGeometryPopulator.cc` | C++ | 351 |

## Overview

A `FeatureVisitor` that reconstructs motion path features by extracting seed points, reconstructing them through time using a `ReconstructionTreeCreator`, and generating motion path geometries that record the path a point travels. The visitor examines motion track properties (e.g. times, plate IDs) to determine the reconstruction trajectory, then creates `ReconstructedFeatureGeometry` objects for output.

## Declared types

| Name | Kind | Bases | Template | Subclasses | Description |
|---|---|---|---|---|---|
| [`GPlatesAppLogic::MotionPathGeometryPopulator`](#gplatesapplogicmotionpathgeometrypopulator) | class | [`GPlatesModel::FeatureVisitor`](../model/FeatureVisitor.md)<br>`boost::noncopyable` | — | 0 | Reconstructs motion path features |

## Members

### `GPlatesAppLogic::MotionPathGeometryPopulator`

| Member | Kind | Type | Access | Description |
|---|---|---|---|---|
| `MotionPathGeometryPopulator( std::vector<ReconstructedFeatureGeometry::non_null_ptr_type> &reconstructed_feature_geometries, const ReconstructionTreeCreator &reconstruction_tree_creator, const double &reconstruction_time)` | constructor | `None` | public | — |
| `~MotionPathGeometryPopulator()` | destructor | `None` | public | — |
| `initialise_pre_feature_properties( GPlatesModel::FeatureHandle &feature_handle)` | method | `bool` | protected | — |
| `visit_gml_multi_point( GPlatesPropertyValues::GmlMultiPoint &gml_multi_point)` | method | `void` | protected | — |
| `visit_gml_point( GPlatesPropertyValues::GmlPoint &gml_point)` | method | `void` | protected | — |
| `visit_gpml_constant_value( GPlatesPropertyValues::GpmlConstantValue &gpml_constant_value)` | method | `void` | protected | — |
| `create_motion_path_geometry( const GPlatesMaths::PointOnSphere &present_day_seed_point, const GPlatesMaths::PointOnSphere &reconstructed_seed_point, const GPlatesMaths::GeometryOnSphere::non_null_ptr_to_const_type &reconstructed_seed_geometry)` | method | `void` | private | — |
| `d_reconstructed_feature_geometries` | field | `std::vector<ReconstructedFeatureGeometry::non_null_ptr_type>` | private | The ReconstructedFeatureGeometry objects generated during reconstruction. |
| `d_reconstruction_tree_creator` | field | `ReconstructionTreeCreator` | private | The function to call (with a time/anchor argument) to get a ReconstructionTree. |
| `d_recon_time` | field | `GPlatesPropertyValues::GeoTimeInstant` | private | — |
| `d_motion_track_property_finder` | field | `boost::scoped_ptr<MotionPathUtils::MotionPathPropertyFinder>` | private | — |
| `d_rotations` | field | `std::vector<GPlatesMaths::FiniteRotation>` | private | — |

## Free functions and macros

| Name | Kind | Type / body | Description |
|---|---|---|---|
| `GPLATES_APP_LOGIC_MOTIONPATHGEOMETRYPOPULATOR_H` | macro | `None` | — |

## Notes

The visitor is non-copyable and stateful — it stores rotations and feature properties across visits. It is typically used once per feature collection pass.

## Used by

| Unit | Component | References |
|---|---|---|
| [app-logic/ReconstructMethodMotionPath](ReconstructMethodMotionPath.md) | app-logic | 3 |

## Related

*None.*

## Explore

Run these from the `gplates-code` skill directory:

```bash
python scripts/gpq.py file src/app-logic/MotionPathGeometryPopulator.h
python scripts/gpq.py def GPlatesAppLogic::MotionPathGeometryPopulator --body
python scripts/gpq.py uses MotionPathGeometryPopulator --kind class
python scripts/gpq.py hier MotionPathGeometryPopulator
```
