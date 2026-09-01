# ScalarField3DLayerParams

[Book TOC](../../TOC.md) · [app-logic](../../components/app-logic.md) · cluster Community 521 · tier 2

| Source file | Kind | Lines |
|---|---|---|
| `src/app-logic/ScalarField3DLayerParams.h` | C++ | 226 |
| `src/app-logic/ScalarField3DLayerParams.cc` | C++ | 120 |

## Overview

The `LayerParams` for a 3D scalar field layer: it holds the feature reference for the scalar field and caches metadata read out of the field's on-disk file — depth-layer radius range and per-field statistics (min/max/mean/standard deviation of both the scalar values and their gradient magnitudes). These are the numbers the scalar-field rendering options widget uses to set up sensible default colour-mapping ranges without having to reopen the file itself.

`set_scalar_field_feature` does the actual work: it runs `ExtractScalarField3DFeatureProperties` on the feature to find the field's filename, opens it with `GPlatesFileIO::ScalarField3DFileFormat::Reader`, and copies the precomputed statistics out of the file header into this object's fields, emitting the `modified` signal (inherited from `LayerParams`) whichever way the call ends. Everything is cleared to `boost::none` up front, so a failed lookup — no feature, no filename, a missing file, or an unsupported/corrupt file format (caught and logged with `qWarning`) — leaves all the optionals unset rather than stale from a previous field.

## Declared types

| Name | Kind | Bases | Template | Subclasses | Description |
|---|---|---|---|---|---|
| [`GPlatesAppLogic::ScalarField3DLayerParams`](#gplatesapplogicscalarfield3dlayerparams) | class | [`LayerParams`](LayerParams.md) | — | 0 | App-logic parameters for a 3D scalar field layer. |

## Members

### `GPlatesAppLogic::ScalarField3DLayerParams`

| Member | Kind | Type | Access | Description |
|---|---|---|---|---|
| `non_null_ptr_type` | typedef | `GPlatesUtils::non_null_intrusive_ptr<ScalarField3DLayerParams>` | public | — |
| `non_null_ptr_to_const_type` | typedef | `GPlatesUtils::non_null_intrusive_ptr<const ScalarField3DLayerParams>` | public | — |
| `create()` | method | `non_null_ptr_type` | public | — |
| `set_scalar_field_feature( boost::optional<GPlatesModel::FeatureHandle::weak_ref> feature_ref)` | method | `void` | public | Sets (or unsets) the 3D scalar field feature. |
| `get_minimum_depth_layer_radius()` | method | `boost::optional<double>` | public | Returns the minimum depth layer radius of scalar field or none if no field. |
| `get_maximum_depth_layer_radius()` | method | `boost::optional<double>` | public | Returns the maximum depth layer radius of scalar field or none if no field. |
| `get_scalar_min()` | method | `boost::optional<double>` | public | Returns the minimum scalar value across the entire scalar field or none if no field. |
| `get_scalar_max()` | method | `boost::optional<double>` | public | Returns the maximum scalar value across the entire scalar field or none if no field. |
| `get_scalar_mean()` | method | `boost::optional<double>` | public | Returns the mean scalar value across the entire scalar field or none if no field. |
| `get_scalar_standard_deviation()` | method | `boost::optional<double>` | public | Returns the standard deviation of scalar values across the entire scalar field or none if no field. |
| `get_gradient_magnitude_min()` | method | `boost::optional<double>` | public | Returns the minimum gradient magnitude across the entire scalar field or none if no field. |
| `get_gradient_magnitude_max()` | method | `boost::optional<double>` | public | Returns the maximum gradient magnitude across the entire scalar field or none if no field. |
| `get_gradient_magnitude_mean()` | method | `boost::optional<double>` | public | Returns the mean gradient magnitude across the entire scalar field or none if no field. |
| `get_gradient_magnitude_standard_deviation()` | method | `boost::optional<double>` | public | Returns the standard deviation of gradient magnitudes across the entire scalar field or none if no field. |
| `accept_visitor( ConstLayerParamsVisitor &visitor)` | method | `void` | public | Override of virtual method in LayerParams base. |
| `accept_visitor( LayerParamsVisitor &visitor)` | method | `void` | public | Override of virtual method in LayerParams base. |
| `d_scalar_field_feature` | field | `boost::optional<GPlatesModel::FeatureHandle::weak_ref>` | private | The scalar field feature. |
| `d_minimum_depth_layer_radius` | field | `boost::optional<double>` | private | — |
| `d_maximum_depth_layer_radius` | field | `boost::optional<double>` | private | — |
| `d_scalar_min` | field | `boost::optional<double>` | private | — |
| `d_scalar_max` | field | `boost::optional<double>` | private | — |
| `d_scalar_mean` | field | `boost::optional<double>` | private | — |
| `d_scalar_standard_deviation` | field | `boost::optional<double>` | private | — |
| `d_gradient_magnitude_min` | field | `boost::optional<double>` | private | — |
| `d_gradient_magnitude_max` | field | `boost::optional<double>` | private | — |
| `d_gradient_magnitude_mean` | field | `boost::optional<double>` | private | — |
| `d_gradient_magnitude_standard_deviation` | field | `boost::optional<double>` | private | — |
| `ScalarField3DLayerParams()` | constructor | `None` | private | — |

## Free functions and macros

| Name | Kind | Type / body | Description |
|---|---|---|---|
| `GPLATES_APP_LOGIC_SCALARFIELD3DLAYERPARAMS_H` | macro | `None` | — |

## Notes

All the statistic getters are documented as reflecting the field at present day; the header notes they will need to become time-dependent if/when time-varying scalar fields are supported, so treat the current values as a present-day snapshot, not a per-reconstruction-time quantity. `set_scalar_field_feature` swallows `UnsupportedVersion` and `FileFormatNotSupportedException` (logging via `qWarning` and leaving the optionals empty) rather than propagating them, so callers cannot distinguish "no field" from "field present but unreadable" except by checking the application's log.

## Used by

| Unit | Component | References |
|---|---|---|
| [qt-widgets/ScalarField3DLayerOptionsWidget](../qt-widgets/ScalarField3DLayerOptionsWidget.md) | qt-widgets | 21 |
| [presentation/ScalarField3DVisualLayerParams](../presentation/ScalarField3DVisualLayerParams.md) | presentation | 19 |
| [app-logic/ScalarField3DLayerProxy](ScalarField3DLayerProxy.md) | app-logic | 4 |
| [app-logic/ScalarField3DLayerTask](ScalarField3DLayerTask.md) | app-logic | 4 |
| [presentation/TranscribeSession](../presentation/TranscribeSession.md) | presentation | 1 |

## Related

*None.*

## Explore

Run these from the `gplates-code` skill directory:

```bash
python scripts/gpq.py file src/app-logic/ScalarField3DLayerParams.h
python scripts/gpq.py def GPlatesAppLogic::ScalarField3DLayerParams --body
python scripts/gpq.py uses ScalarField3DLayerParams --kind class
python scripts/gpq.py hier ScalarField3DLayerParams
```
