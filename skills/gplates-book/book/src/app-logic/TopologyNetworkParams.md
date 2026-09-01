# TopologyNetworkParams

[Book TOC](../../TOC.md) · [app-logic](../../components/app-logic.md) · cluster Community 64 · tier 2

| Source file | Kind | Lines |
|---|---|---|
| `src/app-logic/TopologyNetworkParams.h` | C++ | 229 |
| `src/app-logic/TopologyNetworkParams.cc` | C++ | 293 |

## Overview

`TopologyNetworkParams` is the plain value object holding the deformation settings for one topological network layer: how to smooth computed strain rates (`StrainRateSmoothing`), whether and how to clamp them (`StrainRateClamping`), and the stretching-profile parameters used when a network represents a rift (`RiftParams`, applicable only when the network feature carries rift left/right plate IDs). `TopologyNetworkLayerParams` stores one instance per layer and hands it to the resolving code in `TopologyNetworkResolverLayerProxy` and `ResolvedTriangulationNetwork`, while `qt-widgets::TopologyNetworkResolverLayerOptionsWidget` is what lets a user edit it. Full value comparability (`operator==`, `operator<`) lets `TopologyNetworkLayerParams::set_topology_network_params()` detect a genuine change and skip re-resolving otherwise.

## Declared types

| Name | Kind | Bases | Template | Subclasses | Description |
|---|---|---|---|---|---|
| [`GPlatesAppLogic::TopologyNetworkParams`](#gplatesapplogictopologynetworkparams) | class | `boost::less_than_comparable<TopologyNetworkParams>`<br>`boost::equality_comparable<TopologyNetworkParams>` | — | 0 | TopologyNetworkParams is used to store additional parameters for resolving topological networks and associated attributes in TopologyNetworkLayerTask layers. |

## Members

### `GPlatesAppLogic::TopologyNetworkParams`

| Member | Kind | Type | Access | Description |
|---|---|---|---|---|
| `StrainRateSmoothing` | enum | `None` | public | — |
| `StrainRateClamping` | struct | `None` | public | Strain rate clamping parameters. |
| `RiftParams` | struct | `None` | public | Rift parameters for networks that are rifts. |
| `TopologyNetworkParams()` | constructor | `None` | public | — |
| `get_strain_rate_smoothing()` | method | `StrainRateSmoothing` | public | — |
| `set_strain_rate_smoothing( StrainRateSmoothing strain_rate_smoothing)` | method | `void` | public | — |
| `set_strain_rate_clamping( const StrainRateClamping &strain_rate_clamping)` | method | `void` | public | — |
| `set_rift_params( const RiftParams &rift_params)` | method | `void` | public | — |
| `operator==( const TopologyNetworkParams &rhs)` | operator | `bool` | public | Equality comparison operator. |
| `operator<( const TopologyNetworkParams &rhs)` | operator | `bool` | public | Less than comparison operator. |
| `COMPARE_STRAIN_RATE_SCALE` | field | `double` | private | Strain rates (units 1/second) are typically much smaller than GPlatesMaths::EPSILON and so we need to scale them before using the comparison functionality of GPlatesMaths::Real. |
| `d_strain_rate_smoothing` | field | `StrainRateSmoothing` | private | Whether, and how, to smooth the deformation strain rates. |
| `d_strain_rate_clamping` | field | `StrainRateClamping` | private | Whether, and how much, to clamp the deformation strain rates. |
| `d_rift_params` | field | `RiftParams` | private | Rift parameters for networks that are rifts. |
| `transcribe( GPlatesScribe::Scribe &scribe, bool transcribed_construct_data)` | method | `GPlatesScribe::TranscribeResult` | private | — |

## Free functions and macros

| Name | Kind | Type / body | Description |
|---|---|---|---|
| `COMPARE_STRAIN_RATE_SCALE` | variable | `double` | Strain rates get to around 1e-17 so we should scale that to 1.0 before doing epsilon comparisons. |
| `operator==( const TopologyNetworkParams &rhs)` | operator | `bool` | — |
| `operator<( const TopologyNetworkParams &rhs)` | operator | `bool` | — |
| `operator==( const TopologyNetworkParams::StrainRateClamping &rhs)` | operator | `bool` | — |
| `operator<( const TopologyNetworkParams::StrainRateClamping &rhs)` | operator | `bool` | — |
| `operator==( const TopologyNetworkParams::RiftParams &rhs)` | operator | `bool` | — |
| `operator<( const TopologyNetworkParams::RiftParams &rhs)` | operator | `bool` | — |
| `GPLATES_APP_LOGIC_TOPOLOGYNETWORKPARAMS_H` | macro | `None` | — |
| `transcribe( GPlatesScribe::Scribe &scribe, TopologyNetworkParams::StrainRateSmoothing &strain_rate_smoothing, bool transcribed_construct_data)` | function | `GPlatesScribe::TranscribeResult` | Transcribe for sessions/projects. |

## Notes

Strain rate fields are compared after scaling by `COMPARE_STRAIN_RATE_SCALE` (1e17) before being wrapped in `GPlatesMaths::real_t`, because raw strain rates (around 1e-17 1/s) are far smaller than `GPlatesMaths::EPSILON` and would otherwise all compare equal.

## Used by

| Unit | Component | References |
|---|---|---|
| [qt-widgets/TopologyNetworkResolverLayerOptionsWidget](../qt-widgets/TopologyNetworkResolverLayerOptionsWidget.md) | qt-widgets | 59 |
| [app-logic/TopologyNetworkResolverLayerProxy](TopologyNetworkResolverLayerProxy.md) | app-logic | 25 |
| [app-logic/ResolvedTriangulationNetwork](ResolvedTriangulationNetwork.md) | app-logic | 19 |
| [app-logic/TopologyUtils](TopologyUtils.md) | app-logic | 7 |
| [presentation/ReconstructionGeometryRenderer](../presentation/ReconstructionGeometryRenderer.md) | presentation | 6 |
| [app-logic/TopologyNetworkResolver](TopologyNetworkResolver.md) | app-logic | 5 |
| [app-logic/TopologyNetworkLayerParams](TopologyNetworkLayerParams.md) | app-logic | 4 |
| [app-logic/ResolvedTriangulationDelaunay2](ResolvedTriangulationDelaunay2.md) | app-logic | 2 |
| [presentation/TranscribeSession](../presentation/TranscribeSession.md) | presentation | 1 |

## Related

*None.*

## Explore

Run these from the `gplates-code` skill directory:

```bash
python scripts/gpq.py file src/app-logic/TopologyNetworkParams.h
python scripts/gpq.py def GPlatesAppLogic::TopologyNetworkParams --body
python scripts/gpq.py uses TopologyNetworkParams --kind class
python scripts/gpq.py hier TopologyNetworkParams
```
