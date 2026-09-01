# SmallCircleGeometryPopulator

[Book TOC](../../TOC.md) · [app-logic](../../components/app-logic.md) · cluster Community 638 · tier 3

| Source file | Kind | Lines |
|---|---|---|
| `src/app-logic/SmallCircleGeometryPopulator.h` | C++ | 133 |
| `src/app-logic/SmallCircleGeometryPopulator.cc` | C++ | 168 |

## Overview

`SmallCircleGeometryPopulator` is a feature visitor that extracts properties from a `SmallCircle` feature and creates reconstructed small circle geometries. It walks the feature hierarchy to find the centre point, angular radius, plate ID, and valid time; checks that the feature is defined at the reconstruction time; rotates the centre to its reconstructed position; and creates a `ReconstructedSmallCircle` object with the reconstructed centre and radius in radians. Used by `ReconstructMethodSmallCircle` to populate the reconstruction output.

## Declared types

| Name | Kind | Bases | Template | Subclasses | Description |
|---|---|---|---|---|---|
| [`GPlatesAppLogic::SmallCircleGeometryPopulator`](#gplatesapplogicsmallcirclegeometrypopulator) | class | [`GPlatesModel::FeatureVisitor`](../model/FeatureVisitor.md)<br>`boost::noncopyable` | — | 0 | Creates small circle geometries |

## Members

### `GPlatesAppLogic::SmallCircleGeometryPopulator`

| Member | Kind | Type | Access | Description |
|---|---|---|---|---|
| `SmallCircleGeometryPopulator( std::vector<ReconstructedFeatureGeometry::non_null_ptr_type> &reconstructed_feature_geometries, const ReconstructionTreeCreator &reconstruction_tree_creator, const double &reconstruction_time)` | constructor | `None` | public | — |
| `~SmallCircleGeometryPopulator()` | destructor | `None` | public | — |
| `initialise_pre_feature_properties( GPlatesModel::FeatureHandle &feature_handle)` | method | `bool` | protected | — |
| `finalise_post_feature_properties( GPlatesModel::FeatureHandle &feature_handle)` | method | `void` | protected | — |
| `visit_gml_point( GPlatesPropertyValues::GmlPoint &gml_point)` | method | `void` | protected | — |
| `visit_gml_time_period( GPlatesPropertyValues::GmlTimePeriod &gml_time_period)` | method | `void` | protected | — |
| `visit_gpml_constant_value( GPlatesPropertyValues::GpmlConstantValue &gpml_constant_value)` | method | `void` | protected | — |
| `visit_gpml_plate_id( GPlatesPropertyValues::GpmlPlateId &gpml_plate_id)` | method | `void` | protected | — |
| `visit_gpml_measure( GPlatesPropertyValues::GpmlMeasure &gpml_measure)` | method | `void` | protected | — |
| `d_reconstructed_feature_geometries` | field | `std::vector<ReconstructedFeatureGeometry::non_null_ptr_type>` | private | The ReconstructedFeatureGeometry objects generated during reconstruction. |
| `d_reconstruction_tree_creator` | field | `ReconstructionTreeCreator` | private | Used to get a ReconstructionTree. |
| `d_reconstruction_time` | field | `GPlatesPropertyValues::GeoTimeInstant` | private | — |
| `d_centre` | field | `boost::optional<GPlatesMaths::PointOnSphere>` | private | — |
| `d_radius_in_degrees` | field | `boost::optional<double>` | private | — |
| `d_geometry_iterator` | field | `boost::optional<GPlatesModel::FeatureHandle::iterator>` | private | We need to provide an iterator-to-geometry-property to the various ReconstructedGeometry creation functions. |
| `d_reconstruction_plate_id` | field | `boost::optional<GPlatesModel::integer_plate_id_type>` | private | — |
| `d_feature_is_defined_at_recon_time` | field | `bool` | private | — |

## Free functions and macros

| Name | Kind | Type / body | Description |
|---|---|---|---|
| `GPLATES_APP_LOGIC_SMALLCIRCLEGEOMETRYPOPULATOR_H` | macro | `None` | — |

## Notes

*None.*

## Used by

| Unit | Component | References |
|---|---|---|
| [app-logic/ReconstructMethodSmallCircle](ReconstructMethodSmallCircle.md) | app-logic | 2 |
| [app-logic/ReconstructUtils](ReconstructUtils.md) | app-logic | 1 |

## Related

*None.*

## Explore

Run these from the `gplates-code` skill directory:

```bash
python scripts/gpq.py file src/app-logic/SmallCircleGeometryPopulator.h
python scripts/gpq.py def GPlatesAppLogic::SmallCircleGeometryPopulator --body
python scripts/gpq.py uses SmallCircleGeometryPopulator --kind class
python scripts/gpq.py hier SmallCircleGeometryPopulator
```
