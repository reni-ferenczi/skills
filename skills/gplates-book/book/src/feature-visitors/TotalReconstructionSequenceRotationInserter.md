# TotalReconstructionSequenceRotationInserter

[Book TOC](../../TOC.md) · [feature-visitors](../../components/feature-visitors.md) · cluster Community 810 · tier 3

| Source file | Kind | Lines |
|---|---|---|
| `src/feature-visitors/TotalReconstructionSequenceRotationInserter.h` | C++ | 147 |
| `src/feature-visitors/TotalReconstructionSequenceRotationInserter.cc` | C++ | 455 |

## Overview

This visitor updates a total reconstruction sequence (rotation file) by inserting or modifying a rotation at a specific reconstruction time. It visits the finite rotation structures in the feature, finds the rotation corresponding to the target time, applies a supplied `Rotation` to compose with it, and updates the result back into the data structure. It handles both exact time matches and interpolated rotations via `GpmlFiniteRotationSlerp` and `GpmlIrregularSampling`. The visitor is non-copyable and maintains references to the file state and rotation proxy needed to persist changes back to the rotation file.

## Declared types

| Name | Kind | Bases | Template | Subclasses | Description |
|---|---|---|---|---|---|
| [`GPlatesFeatureVisitors::TotalReconstructionSequenceRotationInserter`](#gplatesfeaturevisitorstotalreconstructionsequencerotationinserter) | class | [`GPlatesModel::FeatureVisitor`](../model/FeatureVisitor.md) | — | 0 | Insert an updated finite rotation into a total reconstruction sequence for a particular reconstruction time. |

## Members

### `GPlatesFeatureVisitors::TotalReconstructionSequenceRotationInserter`

| Member | Kind | Type | Access | Description |
|---|---|---|---|---|
| `TotalReconstructionSequenceRotationInserter( const double &recon_time, const GPlatesMaths::Rotation &rotation_to_apply, GPlatesAppLogic::FeatureCollectionFileState &file_state)` | constructor | `None` | public | — |
| `~TotalReconstructionSequenceRotationInserter()` | destructor | `None` | public | — |
| `initialise_pre_feature_properties( GPlatesModel::FeatureHandle &feature_handle)` | method | `bool` | protected | — |
| `visit_gpml_finite_rotation( GPlatesPropertyValues::GpmlFiniteRotation &gpml_finite_rotation)` | method | `void` | protected | — |
| `visit_gpml_finite_rotation_slerp( GPlatesPropertyValues::GpmlFiniteRotationSlerp &gpml_finite_rotation_slerp)` | method | `void` | protected | — |
| `visit_gpml_irregular_sampling( GPlatesPropertyValues::GpmlIrregularSampling &gpml_irregular_sampling)` | method | `void` | protected | — |
| `d_file_state` | field | `GPlatesAppLogic::FeatureCollectionFileState` | private | — |
| `d_recon_time` | field | `GPlatesPropertyValues::GeoTimeInstant` | private | — |
| `d_rotation_to_apply` | field | `GPlatesMaths::Rotation` | private | — |
| `d_is_expecting_a_finite_rotation` | field | `bool` | private | — |
| `d_trp_time_matches_exactly` | field | `bool` | private | — |
| `d_finite_rotation` | field | `boost::optional<GPlatesMaths::FiniteRotation>` | private | — |
| `d_grot_proxy` | field | `GPlatesFileIO::PlatesRotationFileProxy` | private | — |
| `d_moving_plate_id` | field | `int` | private | — |
| `d_fixed_plate_id` | field | `int` | private | — |
| `TotalReconstructionSequenceRotationInserter( const TotalReconstructionSequenceRotationInserter &)` | constructor | `None` | private | This constructor should never be defined, because we don't want to allow copy-construction. |
| `operator=` | field | `TotalReconstructionSequenceRotationInserter` | private | This operator should never be defined, because we don't want to allow copy-assignment. |
| `update_finite_rotation( GPlatesPropertyValues::GpmlFiniteRotation &gpml_finite_rotation)` | method | `void` | private | Update the finite rotation in an existing GpmlFiniteRotation time sample (time coincides with existing time sample). |
| `update_pole_metadata( GPlatesPropertyValues::GpmlFiniteRotation &gpml_finite_rotation)` | method | `void` | private | Update the pole metadata in an existing GpmlFiniteRotation time sample (time coincides with existing time sample). |
| `set_pole_metadata( GPlatesPropertyValues::GpmlFiniteRotation &gpml_finite_rotation)` | method | `void` | private | Set/modify the pole metadata in a GpmlFiniteRotation. |

## Free functions and macros

| Name | Kind | Type / body | Description |
|---|---|---|---|
| `GPLATES_FEATUREVISITORS_TOTALRECONSTRUCTIONSEQUENCEROTATIONINSERTER_H` | macro | `None` | — |

## Notes

Non-copyable: the class explicitly deletes copy construction and copy assignment to prevent accidental copies, as it holds references to file state that should not be duplicated.

## Used by

| Unit | Component | References |
|---|---|---|
| [qt-widgets/ApplyReconstructionPoleAdjustmentDialog](../qt-widgets/ApplyReconstructionPoleAdjustmentDialog.md) | qt-widgets | 4 |

## Related

*None.*

## Explore

Run these from the `gplates-code` skill directory:

```bash
python scripts/gpq.py file src/feature-visitors/TotalReconstructionSequenceRotationInserter.h
python scripts/gpq.py def GPlatesFeatureVisitors::TotalReconstructionSequenceRotationInserter --body
python scripts/gpq.py uses TotalReconstructionSequenceRotationInserter --kind class
python scripts/gpq.py hier TotalReconstructionSequenceRotationInserter
```
