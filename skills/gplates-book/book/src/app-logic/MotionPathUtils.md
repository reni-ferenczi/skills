# MotionPathUtils

[Book TOC](../../TOC.md) · [app-logic](../../components/app-logic.md) · cluster Community 481 · tier 2

| Source file | Kind | Lines |
|---|---|---|
| `src/app-logic/MotionPathUtils.h` | C++ | 268 |
| `src/app-logic/MotionPathUtils.cc` | C++ | 229 |

## Overview

`MotionPathUtils` supplies the two feature visitors and helper functions used to reconstruct `gpml:MotionPath` features. `DetectMotionPathFeatures` is a cheap `GPlatesModel::ConstFeatureVisitor` that only inspects `feature_type()` (it never visits properties) to answer whether a feature collection contains any motion path features at all. `MotionPathPropertyFinder` does the real work: it walks one motion-path feature's properties (`gpml:reconstructionPlateId`, a relative plate ID, `gml:validTime`, the seed-point geometry, and the `GpmlArray<TimePeriod>` of sample times) and exposes them as plain accessors, plus `can_process_motion_path()`/`can_process_seed_point()` to check that enough of those properties were actually present before a caller tries to reconstruct anything.

`calculate_motion_track()` turns a present-day seed point and a sequence of `GPlatesMaths::FiniteRotation`s into the polyline of points making up the motion track, applying the rotations from most recent to oldest. `fill_times_vector()` merges a feature's list of time samples with the current reconstruction time into one ascending vector, inserting the reconstruction time only when it falls strictly between the sampled endpoints.

## Declared types

| Name | Kind | Bases | Template | Subclasses | Description |
|---|---|---|---|---|---|
| [`GPlatesAppLogic::MotionPathUtils::DetectMotionPathFeatures`](#gplatesapplogicmotionpathutilsdetectmotionpathfeatures) | class | [`GPlatesModel::ConstFeatureVisitor`](../model/FeatureVisitor.md) | — | 0 | Determines if there are any motion track features in the collection. |
| [`GPlatesAppLogic::MotionPathUtils::MotionPathPropertyFinder`](#gplatesapplogicmotionpathutilsmotionpathpropertyfinder) | class | [`GPlatesModel::ConstFeatureVisitor`](../model/FeatureVisitor.md) | — | 0 | Used to obtain motion-track-relevant parameters from a motion track feature. |

## Members

### `GPlatesAppLogic::MotionPathUtils::DetectMotionPathFeatures`

| Member | Kind | Type | Access | Description |
|---|---|---|---|---|
| `DetectMotionPathFeatures()` | constructor | `None` | public | — |
| `has_motion_track_features()` | method | `bool` | public | — |
| `visit_feature_handle( const GPlatesModel::FeatureHandle &feature_handle)` | method | `void` | public | — |
| `d_found_motion_track_features` | field | `bool` | private | — |

### `GPlatesAppLogic::MotionPathUtils::MotionPathPropertyFinder`

| Member | Kind | Type | Access | Description |
|---|---|---|---|---|
| `MotionPathPropertyFinder( const double &reconstruction_time)` | constructor | `None` | public | — |
| `MotionPathPropertyFinder()` | constructor | `None` | public | — |
| `get_reconstruction_plate_id()` | method | `boost::optional<GPlatesModel::integer_plate_id_type>` | public | — |
| `get_relative_plate_id()` | method | `boost::optional<GPlatesModel::integer_plate_id_type>` | public | — |
| `get_feature_info_string()` | method | `QString` | public | — |
| `get_name()` | method | `QString` | public | — |
| `has_geometry()` | method | `bool` | public | — |
| `can_process_motion_path()` | method | `bool` | public | — |
| `can_process_seed_point()` | method | `bool` | public | — |
| `initialise_pre_feature_properties( const GPlatesModel::FeatureHandle &feature_handle)` | method | `bool` | private | — |
| `finalise_post_feature_properties( const GPlatesModel::FeatureHandle &feature_handle)` | method | `void` | private | — |
| `visit_gml_multi_point( const GPlatesPropertyValues::GmlMultiPoint &gml_multi_point)` | method | `void` | private | — |
| `visit_gml_time_period( const GPlatesPropertyValues::GmlTimePeriod &gml_time_period)` | method | `void` | private | — |
| `visit_gml_point( const GPlatesPropertyValues::GmlPoint &gml_point)` | method | `void` | private | — |
| `visit_gpml_array( const GPlatesPropertyValues::GpmlArray &gpml_array)` | method | `void` | private | — |
| `visit_gpml_constant_value( const GPlatesPropertyValues::GpmlConstantValue &gpml_constant_value)` | method | `void` | private | — |
| `visit_gpml_plate_id( const GPlatesPropertyValues::GpmlPlateId &gpml_plate_id)` | method | `void` | private | — |
| `d_feature_is_defined_at_recon_time` | field | `bool` | private | — |
| `d_has_geometry` | field | `bool` | private | — |
| `d_reconstruction_time` | field | `boost::optional<GPlatesPropertyValues::GeoTimeInstant>` | private | — |
| `d_reconstruction_plate_id` | field | `boost::optional<GPlatesModel::integer_plate_id_type>` | private | — |
| `d_relative_plate_id` | field | `boost::optional<GPlatesModel::integer_plate_id_type>` | private | — |
| `d_time_of_appearance` | field | `boost::optional<GPlatesPropertyValues::GeoTimeInstant>` | private | — |
| `d_time_of_dissappearance` | field | `boost::optional<GPlatesPropertyValues::GeoTimeInstant>` | private | — |
| `d_feature_info` | field | `QString` | private | — |
| `d_name` | field | `QString` | private | — |
| `d_times` | field | `std::vector<double>` | private | The GpmlArray\<TimePeriod\> times converted into a vector of doubles. |

## Free functions and macros

| Name | Kind | Type / body | Description |
|---|---|---|---|
| `GPLATES_APPLOGIC_MOTIONPATHUTILS_H` | macro | `None` | — |
| `calculate_motion_track( const GPlatesMaths::PointOnSphere &present_day_seed_point, const MotionPathPropertyFinder &motion_track_parameters, std::vector<GPlatesMaths::PointOnSphere> &motion_track, const std::vector<GPlatesMaths::FiniteRotation> &rotations)` | function | `void` | — |
| `fill_times_vector( std::vector<double> &times, const double &reconstruction_time, const std::vector<double> &time_samples)` | function | `void` | — |

## Notes

`MotionPathPropertyFinder::get_time_of_disappearance()` returns `d_time_of_appearance`, not `d_time_of_dissappearance` — it is implemented as a copy of `get_time_of_appearance()`, so callers currently cannot read the actual disappearance time through this accessor.

`can_process_motion_path()` no longer requires the reconstruction time to fall within the feature's time-of-appearance/disappearance range, by design, so that a motion path can still be displayed or exported (e.g. at present day) even when its sample times don't cover that instant.

## Used by

| Unit | Component | References |
|---|---|---|
| [file-io/GMTFormatMotionPathExport](../file-io/GMTFormatMotionPathExport.md) | file-io | 21 |
| [app-logic/MotionPathGeometryPopulator](MotionPathGeometryPopulator.md) | app-logic | 18 |
| [file-io/OgrFormatMotionPathExport](../file-io/OgrFormatMotionPathExport.md) | file-io | 8 |
| [app-logic/deprecated/ReconstructedFeatureGeometryPopulator](deprecated/ReconstructedFeatureGeometryPopulator.md) | app-logic | 6 |
| [app-logic/ReconstructMethodMotionPath](ReconstructMethodMotionPath.md) | app-logic | 3 |
| [qt-widgets/KinematicGraphsDialog](../qt-widgets/KinematicGraphsDialog.md) | qt-widgets | 3 |

## Related

*None.*

## Explore

Run these from the `gplates-code` skill directory:

```bash
python scripts/gpq.py file src/app-logic/MotionPathUtils.h
python scripts/gpq.py def GPlatesAppLogic::MotionPathUtils::MotionPathPropertyFinder --body
python scripts/gpq.py uses MotionPathPropertyFinder --kind class
python scripts/gpq.py hier MotionPathPropertyFinder
```
