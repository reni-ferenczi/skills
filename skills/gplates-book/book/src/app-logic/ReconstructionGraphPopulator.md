# ReconstructionGraphPopulator

[Book TOC](../../TOC.md) · [app-logic](../../components/app-logic.md) · cluster Community 852 · tier 2

| Source file | Kind | Lines |
|---|---|---|
| `src/app-logic/ReconstructionGraphPopulator.h` | C++ | 137 |
| `src/app-logic/ReconstructionGraphPopulator.cc` | C++ | 280 |

## Overview

`ReconstructionGraphPopulator` is the `GPlatesModel::FeatureVisitor` that turns Total Reconstruction Sequence features (as loaded from a rotation file) into calls to `ReconstructionGraphBuilder::insert_total_reconstruction_sequence`. It visits each feature's `gpml:fixedReferenceFrame` and `gpml:movingReferenceFrame` plate-ID properties and its `GpmlIrregularSampling` of `GpmlFiniteRotation` time samples, accumulating them in the private `ReconstructionSequenceAccumulator` until `finalise_post_feature_properties` has all three pieces — a fixed plate ID, a moving plate ID, and at least two enabled pole time samples — and only then inserts the completed sequence into the graph builder; a feature missing any of these, or with fewer than two enabled samples, is silently dropped without reaching the builder.

The anonymous-namespace helper `IsReconstructionFeature` implements the static `can_process` check used by callers to decide, ahead of time, whether a given `FeatureHandle` is worth visiting at all: it runs the same three-property test (a `GpmlFiniteRotation` somewhere inside an irregular sampling, plus both reference-frame plate IDs) as a cheap, read-only probe via `GPlatesModel::ConstFeatureVisitor`, without touching the graph builder.

## Declared types

| Name | Kind | Bases | Template | Subclasses | Description |
|---|---|---|---|---|---|
| [`(anonymous)::IsReconstructionFeature`](#anonymousisreconstructionfeature) | class | [`GPlatesModel::ConstFeatureVisitor`](../model/FeatureVisitor.md) | — | 0 | Used to determine if ReconstructionGraphPopulator can reconstruct a feature. |
| [`GPlatesAppLogic::ReconstructionGraphPopulator`](#gplatesapplogicreconstructiongraphpopulator) | class | [`GPlatesModel::FeatureVisitorThatGuaranteesNotToModify`](../model/FeatureVisitor.md)<br>`boost::noncopyable` | — | 0 | Populate a ReconstructionGraph instance (via a ReconstructionGraphBuilder) with total reconstruction sequences. |

## Members

### `(anonymous)::IsReconstructionFeature`

| Member | Kind | Type | Access | Description |
|---|---|---|---|---|
| `IsReconstructionFeature()` | constructor | `None` | public | — |
| `is_reconstruction_feature()` | method | `bool` | public | Returns true any features visited by us are reconstruction features. |
| `initialise_pre_feature_properties( const GPlatesModel::FeatureHandle &feature_handle)` | method | `bool` | private | — |
| `finalise_post_feature_properties( const GPlatesModel::FeatureHandle &feature_handle)` | method | `void` | private | — |
| `visit_gpml_irregular_sampling( const GPlatesPropertyValues::GpmlIrregularSampling &gpml_irregular_sampling)` | method | `void` | private | — |
| `visit_gpml_finite_rotation( const GPlatesPropertyValues::GpmlFiniteRotation &gpml_finite_rotation)` | method | `void` | private | — |
| `visit_gpml_plate_id( const GPlatesPropertyValues::GpmlPlateId &gpml_plate_id)` | method | `void` | private | — |
| `d_is_reconstruction_feature` | field | `bool` | private | — |
| `d_has_finite_rotation` | field | `bool` | private | — |
| `d_has_fixed_reference_frame` | field | `bool` | private | — |
| `d_has_moving_reference_frame` | field | `bool` | private | — |

### `GPlatesAppLogic::ReconstructionGraphPopulator`

| Member | Kind | Type | Access | Description |
|---|---|---|---|---|
| `can_process( const GPlatesModel::FeatureHandle::const_weak_ref &feature_ref)` | method | `bool` | public | Returns true if feature\_ref can be processed by ReconstructionGraphPopulator. |
| `ReconstructionGraphPopulator( ReconstructionGraphBuilder &graph_builder)` | constructor | `None` | public | When reconstruction features are visited, total reconstruction sequences will get inserted into ReconstructionGraphBuilder. |
| `~ReconstructionGraphPopulator()` | destructor | `None` | public | — |
| `initialise_pre_feature_properties( GPlatesModel::FeatureHandle &feature_handle)` | method | `bool` | protected | — |
| `finalise_post_feature_properties( GPlatesModel::FeatureHandle &feature_handle)` | method | `void` | protected | — |
| `visit_gpml_finite_rotation( GPlatesPropertyValues::GpmlFiniteRotation &gpml_finite_rotation)` | method | `void` | protected | — |
| `visit_gpml_irregular_sampling( GPlatesPropertyValues::GpmlIrregularSampling &gpml_irregular_sampling)` | method | `void` | protected | — |
| `visit_gpml_plate_id( GPlatesPropertyValues::GpmlPlateId &gpml_plate_id)` | method | `void` | protected | — |
| `ReconstructionSequenceAccumulator` | struct | `None` | private | — |
| `d_graph_builder` | field | `ReconstructionGraphBuilder` | private | — |
| `d_accumulator` | field | `ReconstructionSequenceAccumulator` | private | — |

## Free functions and macros

| Name | Kind | Type / body | Description |
|---|---|---|---|
| `GPLATES_APP_LOGIC_RECONSTRUCTIONTREEPOPULATOR_H` | macro | `None` | — |

## Notes

- `visit_gpml_irregular_sampling` assumes every value it contains is a `GpmlFiniteRotation`; it sets `d_is_expecting_a_finite_rotation` before visiting each enabled time sample and relies on `visit_gpml_finite_rotation` only acting when that flag is set, so a differently-typed sample would simply be ignored rather than reported as an error.
- Disabled time samples in a `GpmlIrregularSampling` are skipped, so the two-sample minimum applies to enabled samples only.
- The accumulator is reset both before and after each feature (`initialise_pre_feature_properties` / `finalise_post_feature_properties`), so state never leaks between features visited by the same populator instance.

## Used by

| Unit | Component | References |
|---|---|---|
| [app-logic/ReconstructUtils](ReconstructUtils.md) | app-logic | 3 |
| [app-logic/ReconstructionTreeCreator](ReconstructionTreeCreator.md) | app-logic | 2 |
| [entry-points/gplates_demo_no_gui_main](../entry-points/gplates_demo_no_gui_main.md) | entry-points | 2 |

## Related

*None.*

## Explore

Run these from the `gplates-code` skill directory:

```bash
python scripts/gpq.py file src/app-logic/ReconstructionGraphPopulator.h
python scripts/gpq.py def (anonymous)::IsReconstructionFeature --body
python scripts/gpq.py uses IsReconstructionFeature --kind class
python scripts/gpq.py hier IsReconstructionFeature
```
