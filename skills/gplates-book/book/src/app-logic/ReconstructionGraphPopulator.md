# ReconstructionGraphPopulator

[Book TOC](../../TOC.md) · [app-logic](../../components/app-logic.md) · cluster Community 852 · tier 2

| Source file | Kind | Lines |
|---|---|---|
| `src/app-logic/ReconstructionGraphPopulator.h` | C++ | 137 |
| `src/app-logic/ReconstructionGraphPopulator.cc` | C++ | 280 |

## Overview

[[[PROSE overview unit=app-logic/ReconstructionGraphPopulator tier=2]]]
Replace this whole block, markers included, with 1-3 paragraphs: what this unit is, why it exists, and how it fits the surrounding design. Do not restate the tables below.
[[[/PROSE]]]

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

[[[PROSE notes unit=app-logic/ReconstructionGraphPopulator tier=2]]]
Replace this whole block, markers included, with invariants, ownership, threading or gotchas that are not visible in the tables. Write *None.* if there is nothing worth saying.
[[[/PROSE]]]

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
