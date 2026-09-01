# FlowlineGeometryPopulator

[Book TOC](../../TOC.md) · [app-logic](../../components/app-logic.md) · cluster Community 704 · tier 2

| Source file | Kind | Lines |
|---|---|---|
| `src/app-logic/FlowlineGeometryPopulator.h` | C++ | 161 |
| `src/app-logic/FlowlineGeometryPopulator.cc` | C++ | 488 |

## Overview

[[[PROSE overview unit=app-logic/FlowlineGeometryPopulator tier=2]]]
Replace this whole block, markers included, with 1-3 paragraphs: what this unit is, why it exists, and how it fits the surrounding design. Do not restate the tables below.
[[[/PROSE]]]

## Declared types

| Name | Kind | Bases | Template | Subclasses | Description |
|---|---|---|---|---|---|
| [`GPlatesAppLogic::FlowlineGeometryPopulator`](#gplatesapplogicflowlinegeometrypopulator) | class | [`GPlatesModel::FeatureVisitor`](../model/FeatureVisitor.md)<br>`boost::noncopyable` | — | 0 | Reconstructs flowline features. |

## Members

### `GPlatesAppLogic::FlowlineGeometryPopulator`

| Member | Kind | Type | Access | Description |
|---|---|---|---|---|
| `FlowlineGeometryPopulator( std::vector<ReconstructedFeatureGeometry::non_null_ptr_type> &reconstructed_feature_geometries, const ReconstructionTreeCreator &reconstruction_tree_creator, const double &reconstruction_time)` | constructor | `None` | public | — |
| `~FlowlineGeometryPopulator()` | destructor | `None` | public | — |
| `initialise_pre_feature_properties( GPlatesModel::FeatureHandle &feature_handle)` | method | `bool` | protected | — |
| `visit_gml_multi_point( GPlatesPropertyValues::GmlMultiPoint &gml_multi_point)` | method | `void` | protected | — |
| `visit_gml_point( GPlatesPropertyValues::GmlPoint &gml_point)` | method | `void` | protected | — |
| `visit_gpml_constant_value( GPlatesPropertyValues::GpmlConstantValue &gpml_constant_value)` | method | `void` | protected | — |
| `reconstruct_seed_geometry_with_recon_plate_id( const GPlatesMaths::GeometryOnSphere::non_null_ptr_to_const_type &present_day_seed_geometry)` | method | `void` | private | Create a reconstructed feature geometry from present\_day\_seed\_geometry, using the reconstruction plate id, and add it to the reconstruction geometry collection. |
| `create_flowline_geometry( const GPlatesMaths::PointOnSphere &present_day_seed_point, const GPlatesMaths::PointOnSphere &reconstructed_seed_point, const GPlatesMaths::GeometryOnSphere::non_null_ptr_to_const_type &reconstructed_seed_geometry)` | method | `void` | private | Create a reconstructed flowline (incorporating both left- and right-hand parts) from the point given by present\_day\_seed\_point, and add this to the reconstruction geometry collection. reconstructed\_seed\_point is required so that we can ... |
| `d_reconstructed_feature_geometries` | field | `std::vector<ReconstructedFeatureGeometry::non_null_ptr_type>` | private | The ReconstructedFeatureGeometry objects generated during reconstruction. |
| `d_reconstruction_tree_creator` | field | `ReconstructionTreeCreator` | private | The function to call (with a reconstruction time argument) to get a ReconstructionTree. |
| `d_recon_time` | field | `GPlatesPropertyValues::GeoTimeInstant` | private | — |
| `d_flowline_property_finder` | field | `boost::scoped_ptr<FlowlineUtils::FlowlinePropertyFinder>` | private | — |
| `d_left_rotations` | field | `std::vector<GPlatesMaths::FiniteRotation>` | private | The (half) stage-pole rotations required for building up the flowlines. |
| `d_right_rotations` | field | `std::vector<GPlatesMaths::FiniteRotation>` | private | — |
| `d_left_seed_point_rotations` | field | `std::vector<GPlatesMaths::FiniteRotation>` | private | Rotations for moving the seed point prior to building the rest of the flowline. |
| `d_right_seed_point_rotations` | field | `std::vector<GPlatesMaths::FiniteRotation>` | private | — |

## Free functions and macros

| Name | Kind | Type / body | Description |
|---|---|---|---|
| `fill_times_vector( std::vector<double> &times, const double &reconstruction_time, const std::vector<double> &time_samples)` | function | `void` | — |
| `GPLATES_APP_LOGIC_FLOWLINEGEOMETRYPOPULATOR_H` | macro | `None` | — |

## Notes

[[[PROSE notes unit=app-logic/FlowlineGeometryPopulator tier=2]]]
Replace this whole block, markers included, with invariants, ownership, threading or gotchas that are not visible in the tables. Write *None.* if there is nothing worth saying.
[[[/PROSE]]]

## Used by

| Unit | Component | References |
|---|---|---|
| [app-logic/ReconstructMethodFlowline](ReconstructMethodFlowline.md) | app-logic | 6 |

## Related

*None.*

## Explore

Run these from the `gplates-code` skill directory:

```bash
python scripts/gpq.py file src/app-logic/FlowlineGeometryPopulator.h
python scripts/gpq.py def GPlatesAppLogic::FlowlineGeometryPopulator --body
python scripts/gpq.py uses FlowlineGeometryPopulator --kind class
python scripts/gpq.py hier FlowlineGeometryPopulator
```
