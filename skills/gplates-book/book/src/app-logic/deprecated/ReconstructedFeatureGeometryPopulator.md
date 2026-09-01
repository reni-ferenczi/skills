# ReconstructedFeatureGeometryPopulator

[Book TOC](../../../TOC.md) · [app-logic](../../../components/app-logic.md) · cluster Community 84 · tier 3 · **deprecated**

| Source file | Kind | Lines |
|---|---|---|
| `src/app-logic/deprecated/ReconstructedFeatureGeometryPopulator.cc` | C++ | 664 |

## Overview

Implementation of the `ReconstructedFeatureGeometryPopulator` visitor, which reconstructs geometries from features at a specified reconstruction time. It applies plate circuit rotations to `GmlPoint`, `GmlLineString`, `GmlPolygon`, `GmlMultiPoint`, and `GmlOrientableCurve` geometries, storing the resulting reconstructed geometries in a `ReconstructionGeometryCollection`. The implementation handles standard reconstructed geometries as well as specialized types: virtual geomagnetic poles (VGP features), flowlines, and motion paths each receive dedicated reconstruction logic via helper detection visitors.

The file also defines the `CanReconstructFeature` helper visitor, which determines whether a feature is reconstructible by checking for the presence of geometry. This pre-filtering step lets the caller identify reconstructible features before instantiating the full populator.

## Declared types

| Name | Kind | Bases | Template | Subclasses | Description |
|---|---|---|---|---|---|
| [`(anonymous)::CanReconstructFeature`](#anonymouscanreconstructfeature) | class | [`GPlatesModel::ConstFeatureVisitor`](../../model/FeatureVisitor.md) | — | 0 | Used to determine if ReconstructedFeatureGeometryPopulator can reconstruct a feature. |

## Members

### `(anonymous)::CanReconstructFeature`

| Member | Kind | Type | Access | Description |
|---|---|---|---|---|
| `CanReconstructFeature()` | constructor | `None` | public | — |
| `can_reconstruct()` | method | `bool` | public | Returns true any features visited by us can be reconstructed. |
| `initialise_pre_feature_properties( const GPlatesModel::FeatureHandle &feature_handle)` | method | `bool` | private | — |
| `finalise_post_feature_properties( const GPlatesModel::FeatureHandle &feature_handle)` | method | `void` | private | — |
| `visit_gml_line_string( const GPlatesPropertyValues::GmlLineString &gml_line_string)` | method | `void` | private | — |
| `visit_gml_multi_point( const GPlatesPropertyValues::GmlMultiPoint &gml_multi_point)` | method | `void` | private | — |
| `visit_gml_orientable_curve( const GPlatesPropertyValues::GmlOrientableCurve &gml_orientable_curve)` | method | `void` | private | — |
| `visit_gml_point( const GPlatesPropertyValues::GmlPoint &gml_point)` | method | `void` | private | — |
| `visit_gml_polygon( const GPlatesPropertyValues::GmlPolygon &gml_polygon)` | method | `void` | private | — |
| `visit_gpml_constant_value( const GPlatesPropertyValues::GpmlConstantValue &gpml_constant_value)` | method | `void` | private | — |
| `visit_gpml_plate_id( const GPlatesPropertyValues::GpmlPlateId &gpml_plate_id)` | method | `void` | private | — |
| `d_can_reconstruct` | field | `bool` | private | — |
| `d_has_geometry` | field | `bool` | private | — |
| `d_has_reconstruction_plate_id` | field | `bool` | private | — |

## Free functions and macros

*None.*

## Notes

The reconstructability check in `CanReconstructFeature` is lenient: it requires only geometry presence, not a reconstruction plate ID. Geometries without an explicit plate ID will be reconstructed using identity rotation. This design accommodates the removal of a default reconstruction layer that once handled unrecognized features.

VGP, flowline, and motion-path features receive special handling: they are detected during initialization via dedicated visitor classes (`DetectPaleomagFeatures`, `DetectFlowlineFeatures`, `DetectMotionPathFeatures`), and the visitor methods skip standard reconstruction for these types in favor of their specialized reconstruction logic.

## Used by

*Nothing in the tree references this unit.*

## Related

*None.*

## Explore

Run these from the `gplates-code` skill directory:

```bash
python scripts/gpq.py file src/app-logic/deprecated/ReconstructedFeatureGeometryPopulator.cc
python scripts/gpq.py def (anonymous)::CanReconstructFeature --body
python scripts/gpq.py uses CanReconstructFeature --kind class
python scripts/gpq.py hier CanReconstructFeature
```
