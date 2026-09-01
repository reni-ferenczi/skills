# ReconstructScalarCoverageLayerParams

[Book TOC](../../TOC.md) · [app-logic](../../components/app-logic.md) · cluster Community 846 · tier 2

| Source file | Kind | Lines |
|---|---|---|
| `src/app-logic/ReconstructScalarCoverageLayerParams.h` | C++ | 220 |
| `src/app-logic/ReconstructScalarCoverageLayerParams.cc` | C++ | 323 |

## Overview

[[[PROSE overview unit=app-logic/ReconstructScalarCoverageLayerParams tier=2]]]
Replace this whole block, markers included, with 1-3 paragraphs: what this unit is, why it exists, and how it fits the surrounding design. Do not restate the tables below.
[[[/PROSE]]]

## Declared types

| Name | Kind | Bases | Template | Subclasses | Description |
|---|---|---|---|---|---|
| [`GPlatesAppLogic::ReconstructScalarCoverageLayerParams`](#gplatesapplogicreconstructscalarcoveragelayerparams) | class | [`LayerParams`](LayerParams.md) | — | 0 | App-logic parameters for a reconstruct scalar coverage layer. |

## Members

### `GPlatesAppLogic::ReconstructScalarCoverageLayerParams`

| Member | Kind | Type | Access | Description |
|---|---|---|---|---|
| `non_null_ptr_type` | typedef | `GPlatesUtils::non_null_intrusive_ptr<ReconstructScalarCoverageLayerParams>` | public | — |
| `non_null_ptr_to_const_type` | typedef | `GPlatesUtils::non_null_intrusive_ptr<const ReconstructScalarCoverageLayerParams>` | public | — |
| `create( const ReconstructScalarCoverageLayerProxy::non_null_ptr_type &layer_proxy)` | method | `non_null_ptr_type` | public | — |
| `set_reconstruct_scalar_coverage_params( const ReconstructScalarCoverageParams &reconstruct_scalar_coverage_params)` | method | `void` | public | Sets the reconstructing coverage parameters. |
| `set_scalar_type( GPlatesPropertyValues::ValueObjectType scalar_type)` | method | `void` | public | Sets the scalar type, of the scalar coverage, for visualisation/processing. |
| `get_scalar_type` | field | `GPlatesPropertyValues::ValueObjectType` | public | Returns the scalar type currently selected for visualisation/processing. |
| `get_scalar_types( std::vector<GPlatesPropertyValues::ValueObjectType> &scalar_types)` | method | `void` | public | Returns the list of scalar types available in the scalar coverage features. |
| `get_scalar_coverages( std::vector<ScalarCoverageFeatureProperties::Coverage> &scalar_coverages)` | method | `void` | public | Gets all scalar coverages available across the scalar coverage features. |
| `get_scalar_statistics( const GPlatesPropertyValues::ValueObjectType &scalar_type)` | method | `boost::optional<GPlatesPropertyValues::ScalarCoverageStatistics>` | public | Returns the scalar statistics across all scalar coverages of the specified scalar type, or none if no coverages. |
| `update()` | method | `void` | public | Detect any changes in the layer params due to changes in the layer proxy (due to changes in its dependencies). |
| `accept_visitor( ConstLayerParamsVisitor &visitor)` | method | `void` | public | Override of virtual method in LayerParams base. |
| `accept_visitor( LayerParamsVisitor &visitor)` | method | `void` | public | Override of virtual method in LayerParams base. |
| `modified_reconstruct_scalar_coverage_params( GPlatesAppLogic::ReconstructScalarCoverageLayerParams &layer_params)` | method | `void` | public | Emitted when set\_reconstruct\_scalar\_coverage\_params has been called (if a change detected). |
| `scalar_statistics_map_type` | typedef | `std::map< GPlatesPropertyValues::ValueObjectType, // Statistics are only none if there are no scalars... boost::optional<GPlatesPropertyValues::ScalarCoverageStatistics> >` | private | Typedef for scalar types to scalar statistics. |
| `d_reconstruct_scalar_coverage_params` | field | `ReconstructScalarCoverageParams` | private | — |
| `d_layer_proxy` | field | `ReconstructScalarCoverageLayerProxy::non_null_ptr_type` | private | — |
| `d_cached_scalar_statistics` | field | `scalar_statistics_map_type` | private | — |
| `d_layer_proxy_observer_token` | field | `GPlatesUtils::ObserverToken` | private | Detect any changes in the layer proxy (due to changes in its dependencies). |
| `ReconstructScalarCoverageLayerParams( const ReconstructScalarCoverageLayerProxy::non_null_ptr_type &layer_proxy)` | constructor | `None` | private | — |
| `create_scalar_statistics( const GPlatesPropertyValues::ValueObjectType &scalar_type)` | method | `boost::optional<GPlatesPropertyValues::ScalarCoverageStatistics>` | private | Creates the scalar statistics across all scalar coverages of the specified scalar type, or returns none if no coverages. |

## Free functions and macros

| Name | Kind | Type / body | Description |
|---|---|---|---|
| `GPLATES_APP_LOGIC_RECONSTRUCTSCALARCOVERAGELAYERPARAMS_H` | macro | `None` | — |

## Notes

[[[PROSE notes unit=app-logic/ReconstructScalarCoverageLayerParams tier=2]]]
Replace this whole block, markers included, with invariants, ownership, threading or gotchas that are not visible in the tables. Write *None.* if there is nothing worth saying.
[[[/PROSE]]]

## Used by

| Unit | Component | References |
|---|---|---|
| [qt-widgets/ReconstructScalarCoverageLayerOptionsWidget](../qt-widgets/ReconstructScalarCoverageLayerOptionsWidget.md) | qt-widgets | 8 |
| [presentation/TranscribeSession](../presentation/TranscribeSession.md) | presentation | 5 |
| [app-logic/ReconstructScalarCoverageLayerTask](ReconstructScalarCoverageLayerTask.md) | app-logic | 3 |
| [presentation/ReconstructScalarCoverageVisualLayerParams](../presentation/ReconstructScalarCoverageVisualLayerParams.md) | presentation | 3 |

## Related

*None.*

## Explore

Run these from the `gplates-code` skill directory:

```bash
python scripts/gpq.py file src/app-logic/ReconstructScalarCoverageLayerParams.h
python scripts/gpq.py def GPlatesAppLogic::ReconstructScalarCoverageLayerParams --body
python scripts/gpq.py uses ReconstructScalarCoverageLayerParams --kind class
python scripts/gpq.py hier ReconstructScalarCoverageLayerParams
```
