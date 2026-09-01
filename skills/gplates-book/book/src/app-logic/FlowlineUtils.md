# FlowlineUtils

[Book TOC](../../TOC.md) · [app-logic](../../components/app-logic.md) · cluster Community 456 · tier 2

| Source file | Kind | Lines |
|---|---|---|
| `src/app-logic/FlowlineUtils.h` | C++ | 352 |
| `src/app-logic/FlowlineUtils.cc` | C++ | 598 |

## Overview

[[[PROSE overview unit=app-logic/FlowlineUtils tier=2]]]
Replace this whole block, markers included, with 1-3 paragraphs: what this unit is, why it exists, and how it fits the surrounding design. Do not restate the tables below.
[[[/PROSE]]]

## Declared types

| Name | Kind | Bases | Template | Subclasses | Description |
|---|---|---|---|---|---|
| [`GPlatesAppLogic::FlowlineUtils::DetectFlowlineFeatures`](#gplatesapplogicflowlineutilsdetectflowlinefeatures) | class | [`GPlatesModel::ConstFeatureVisitor`](../model/FeatureVisitor.md) | — | 0 | Determines if there are any flowline features in the collection. |
| [`GPlatesAppLogic::FlowlineUtils::FlowlinePropertyFinder`](#gplatesapplogicflowlineutilsflowlinepropertyfinder) | class | [`GPlatesModel::ConstFeatureVisitor`](../model/FeatureVisitor.md) | — | 0 | Used to obtain flowline-relevant parameters from a flowline feature. |

## Members

### `GPlatesAppLogic::FlowlineUtils::DetectFlowlineFeatures`

| Member | Kind | Type | Access | Description |
|---|---|---|---|---|
| `DetectFlowlineFeatures()` | constructor | `None` | public | — |
| `has_flowline_features()` | method | `bool` | public | — |
| `initialise_pre_feature_properties( feature_handle_type &feature_handle)` | method | `bool` | public | — |
| `d_found_flowline_features` | field | `bool` | private | — |

### `GPlatesAppLogic::FlowlineUtils::FlowlinePropertyFinder`

| Member | Kind | Type | Access | Description |
|---|---|---|---|---|
| `FlowlinePropertyFinder( const double &reconstruction_time)` | constructor | `None` | public | — |
| `FlowlinePropertyFinder()` | constructor | `None` | public | — |
| `get_reconstruction_plate_id()` | method | `boost::optional<GPlatesModel::integer_plate_id_type>` | public | — |
| `get_left_plate()` | method | `boost::optional<GPlatesModel::integer_plate_id_type>` | public | — |
| `get_right_plate()` | method | `boost::optional<GPlatesModel::integer_plate_id_type>` | public | — |
| `get_feature_info_string()` | method | `QString` | public | — |
| `get_name()` | method | `QString` | public | — |
| `has_geometry()` | method | `bool` | public | — |
| `can_process_flowline()` | method | `bool` | public | Whether or not we should calculate flowlines for the current time. |
| `can_process_seed_point()` | method | `bool` | public | Whether or not we should display the seed point for the current time. |
| `can_correct_seed_point()` | method | `bool` | public | Whether or not we have enough info in the feature to perform a seed-point correction. |
| `initialise_pre_feature_properties( const GPlatesModel::FeatureHandle &feature_handle)` | method | `bool` | private | — |
| `finalise_post_feature_properties( const GPlatesModel::FeatureHandle &feature_handle)` | method | `void` | private | — |
| `visit_gml_multi_point( const GPlatesPropertyValues::GmlMultiPoint &gml_multi_point)` | method | `void` | private | — |
| `visit_gml_point( const GPlatesPropertyValues::GmlPoint &gml_point)` | method | `void` | private | — |
| `visit_gpml_array( const GPlatesPropertyValues::GpmlArray &gpml_array)` | method | `void` | private | — |
| `visit_gpml_constant_value( const GPlatesPropertyValues::GpmlConstantValue &gpml_constant_value)` | method | `void` | private | — |
| `visit_gpml_plate_id( const GPlatesPropertyValues::GpmlPlateId &gpml_plate_id)` | method | `void` | private | — |
| `visit_gml_time_period( const GPlatesPropertyValues::GmlTimePeriod &gml_time_period)` | method | `void` | private | — |
| `visit_xs_string( const GPlatesPropertyValues::XsString &xs_string)` | method | `void` | private | — |
| `d_feature_is_defined_at_recon_time` | field | `bool` | private | — |
| `d_has_geometry` | field | `bool` | private | — |
| `d_reconstruction_time` | field | `boost::optional<GPlatesPropertyValues::GeoTimeInstant>` | private | — |
| `d_reconstruction_plate_id` | field | `boost::optional<GPlatesModel::integer_plate_id_type>` | private | — |
| `d_left_plate` | field | `boost::optional<GPlatesModel::integer_plate_id_type>` | private | — |
| `d_right_plate` | field | `boost::optional<GPlatesModel::integer_plate_id_type>` | private | — |
| `d_time_of_appearance` | field | `boost::optional<GPlatesPropertyValues::GeoTimeInstant>` | private | — |
| `d_time_of_dissappearance` | field | `boost::optional<GPlatesPropertyValues::GeoTimeInstant>` | private | — |
| `d_feature_info` | field | `QString` | private | — |
| `d_name` | field | `QString` | private | — |
| `d_times` | field | `std::vector<double>` | private | The GpmlArray\<TimePeriod\> times converted into a vector of doubles. |

## Free functions and macros

| Name | Kind | Type / body | Description |
|---|---|---|---|
| `GPLATES_APPLOGIC_FLOWLINEUTILS_H` | macro | `None` | — |
| `calculate_flowline( const GPlatesMaths::PointOnSphere &seed_point, const FlowlinePropertyFinder &flowline_parameters, std::vector<GPlatesMaths::PointOnSphere> &flowline, const ReconstructionTreeCreator &reconstruction_tree_creator, const std::vector<GPlatesMaths::FiniteRotation> &rotations)` | function | `void` | — |
| `get_half_angle_rotation( GPlatesMaths::FiniteRotation &rotation)` | function | `void` | Halves the angle of the provided FiniteRotation. |
| `fill_times_vector( std::vector<double> &times, const double &reconstruction_time, const std::vector<double> &time_samples)` | function | `void` | — |
| `get_times_from_time_period_array( std::vector<double> &times, const GPlatesPropertyValues::GpmlArray &array)` | function | `void` | — |
| `reconstruct_seed_point( const GPlatesMaths::PointOnSphere &seed_point, const std::vector<GPlatesMaths::FiniteRotation> &rotations, bool reverse = false)` | function | `GPlatesMaths::PointOnSphere` | — |
| `reconstruct_seed_points( GPlatesMaths::GeometryOnSphere::non_null_ptr_to_const_type seed_points, const std::vector<GPlatesMaths::FiniteRotation> &rotations, bool reverse = false)` | function | `GPlatesMaths::GeometryOnSphere::non_null_ptr_to_const_type` | — |
| `reconstruct_flowline_seed_points( GPlatesMaths::GeometryOnSphere::non_null_ptr_to_const_type seed_points, const double &current_time, const ReconstructionTreeCreator &reconstruction_tree_creator, const GPlatesModel::FeatureHandle::weak_ref &feature_handle, bool reverse = false)` | function | `GPlatesMaths::GeometryOnSphere::non_null_ptr_to_const_type` | — |
| `fill_seed_point_rotations( const double &current_time, const std::vector<double> &flowline_times, const GPlatesModel::integer_plate_id_type &left_plate_id, const GPlatesModel::integer_plate_id_type &right_plate_id, const ReconstructionTreeCreator &reconstruction_tree_creator, std::vector<GPlatesMaths::FiniteRotation> & ...` | function | `void` | Fills seed\_point\_rotations with half-stage rotations from earliest flowline time to current time. |
| `correct_end_point_to_centre( GPlatesMaths::GeometryOnSphere::non_null_ptr_to_const_type geometry_, const GPlatesModel::integer_plate_id_type &plate_1, const GPlatesModel::integer_plate_id_type &plate_2, const std::vector<double> &times, const ReconstructionTreeCreator &reconstruction_tree_creator, const double &reconst ...` | function | `GPlatesMaths::GeometryOnSphere::non_null_ptr_to_const_type` | Given a flowline end point(s) geometry\_ at time reconstruction\_time, calculates the spreading centre for that flowline. |

## Notes

[[[PROSE notes unit=app-logic/FlowlineUtils tier=2]]]
Replace this whole block, markers included, with invariants, ownership, threading or gotchas that are not visible in the tables. Write *None.* if there is nothing worth saying.
[[[/PROSE]]]

## Used by

| Unit | Component | References |
|---|---|---|
| [app-logic/FlowlineGeometryPopulator](FlowlineGeometryPopulator.md) | app-logic | 33 |
| [app-logic/MotionPathUtils](MotionPathUtils.md) | app-logic | 30 |
| [file-io/GMTFormatFlowlineExport](../file-io/GMTFormatFlowlineExport.md) | file-io | 19 |
| [app-logic/ReconstructMethodFlowline](ReconstructMethodFlowline.md) | app-logic | 12 |
| [qt-widgets/FlowlinePropertiesWidget](../qt-widgets/FlowlinePropertiesWidget.md) | qt-widgets | 10 |
| [file-io/OgrFormatFlowlineExport](../file-io/OgrFormatFlowlineExport.md) | file-io | 8 |
| [app-logic/deprecated/ReconstructedFeatureGeometryPopulator](deprecated/ReconstructedFeatureGeometryPopulator.md) | app-logic | 7 |
| [qt-widgets/CreateFeatureDialog](../qt-widgets/CreateFeatureDialog.md) | qt-widgets | 1 |
| [view-operations/FocusedFeatureGeometryManipulator](../view-operations/FocusedFeatureGeometryManipulator.md) | view-operations | 1 |

## Related

*None.*

## Explore

Run these from the `gplates-code` skill directory:

```bash
python scripts/gpq.py file src/app-logic/FlowlineUtils.h
python scripts/gpq.py def GPlatesAppLogic::FlowlineUtils::FlowlinePropertyFinder --body
python scripts/gpq.py uses FlowlinePropertyFinder --kind class
python scripts/gpq.py hier FlowlinePropertyFinder
```
