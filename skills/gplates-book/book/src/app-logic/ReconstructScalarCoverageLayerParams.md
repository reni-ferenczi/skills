# ReconstructScalarCoverageLayerParams

[Book TOC](../../TOC.md) · [app-logic](../../components/app-logic.md) · cluster Community 846 · tier 2

| Source file | Kind | Lines |
|---|---|---|
| `src/app-logic/ReconstructScalarCoverageLayerParams.h` | C++ | 220 |
| `src/app-logic/ReconstructScalarCoverageLayerParams.cc` | C++ | 323 |

## Overview

`ReconstructScalarCoverageLayerParams` is the `LayerParams` for a reconstruct-scalar-coverage layer: it holds the `ReconstructScalarCoverageParams` evolution settings and the currently selected `ValueObjectType` scalar (out of possibly several scalar types the connected scalar coverage features carry), and delegates actual computation to its `ReconstructScalarCoverageLayerProxy`. `get_scalar_statistics` computes and caches per-scalar-type `ScalarCoverageStatistics` (mean, standard deviation, min/max, including the time history of evolved values) in `d_cached_scalar_statistics`, since visual layers repeatedly query these to map colour palettes.

Because this layer is connected to an upstream Reconstruct layer but is not notified directly of changes there, `d_layer_proxy_observer_token` tracks the layer proxy's subject token so `update()` can detect staleness — for example when scalar coverage features are reloaded from file and the selected scalar type is no longer among the available ones, `update()` (and `set_scalar_type`) fall back to the first available scalar type and clear the statistics cache. `get_scalar_type` and `get_scalar_statistics` both call `update()` internally so callers always see a state consistent with the current layer proxy.

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

`get_scalar_type` and `get_scalar_statistics` are logically `const` but internally `const_cast` themselves to call the mutating `update()` — a deliberate lazy-refresh pattern, not a bug, but it means these "read" accessors can emit the `modified` signal as a side effect. `set_reconstruct_scalar_coverage_params` updates the coverage-evolution parameters but explicitly does *not* push that change into the layer proxy itself.

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
