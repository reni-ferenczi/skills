# LayerInputChannelType

[Book TOC](../../TOC.md) · [app-logic](../../components/app-logic.md) · cluster Community 793 · tier 2

| Source file | Kind | Lines |
|---|---|---|
| `src/app-logic/LayerInputChannelType.h` | C++ | 227 |

## Overview

`LayerInputChannelType` declares, for one named input channel of a layer, what kind of data may be plugged into it: either an input feature collection (a file) or the output of another layer, and whether the channel accepts one item or many (`ChannelDataArity`). When a channel accepts layer output, it is further restricted to one or more `LayerTaskType::Type` values, each optionally paired with an `AutoConnect` mode that says whether `ReconstructGraph` should wire it up automatically to a matching layer in the same file or anywhere in the project.

This is metadata, not behaviour: each concrete `LayerTask` subclass builds a set of these to declare its own input channels (for example the reconstruct layer's separate "rotation tree" and "reconstructable features" channels), and `ReconstructGraph`/`Layer` consult it to validate and auto-wire connections rather than hard-coding per-layer connection rules.

## Declared types

| Name | Kind | Bases | Template | Subclasses | Description |
|---|---|---|---|---|---|
| [`GPlatesAppLogic::LayerInputChannelType`](#gplatesapplogiclayerinputchanneltype) | class | — | — | 0 | Information describing the input data types and arity allowed for a single input channel. |

## Members

### `GPlatesAppLogic::LayerInputChannelType`

| Member | Kind | Type | Access | Description |
|---|---|---|---|---|
| `ChannelDataArity` | enum | `None` | public | Represents the number of data inputs allowed by a specific input channel of a layer. |
| `AutoConnect` | enum | `None` | public | Represents whether, and how, to auto connect to an input layer. |
| `InputLayerType` | struct | `None` | public | Associates a layer input type with its auto-connect capability. |
| `LayerInputChannelType( LayerInputChannelName::Type input_channel_name, ChannelDataArity channel_data_arity)` | constructor | `None` | public | Constructor for an input channel to be connected to an input file. |
| `LayerInputChannelType( LayerInputChannelName::Type input_channel_name, ChannelDataArity channel_data_arity, const std::vector<LayerTaskType::Type> &layer_input_types)` | constructor | `None` | public | Constructor for an input channel to be connected to the output of another layer. |
| `LayerInputChannelType( LayerInputChannelName::Type input_channel_name, ChannelDataArity channel_data_arity, LayerTaskType::Type layer_input_type)` | constructor | `None` | public | Convenience constructor for an input channel to be connected to the output of \*one\* type of layer only. |
| `LayerInputChannelType( LayerInputChannelName::Type input_channel_name, ChannelDataArity channel_data_arity, const std::vector<InputLayerType> &layer_input_types)` | constructor | `None` | public | Constructor for an input channel to be connected to the output of another layer. |
| `LayerInputChannelType( LayerInputChannelName::Type input_channel_name, ChannelDataArity channel_data_arity, const InputLayerType &layer_input_type)` | constructor | `None` | public | Convenience constructor for an input channel to be connected to the output of \*one\* type of layer only. |
| `get_input_channel_name()` | method | `LayerInputChannelName::Type` | public | Returns the name of this input channel. |
| `get_channel_data_arity()` | method | `ChannelDataArity` | public | Returns the input channel data arity. |
| `can_connect_to_input_feature_collections()` | method | `bool` | public | Convenience function that returns true if can connect input feature collections (files) to this input channel. |
| `d_input_channel_name` | field | `LayerInputChannelName::Type` | private | — |
| `d_channel_data_arity` | field | `ChannelDataArity` | private | — |
| `d_input_layer_types` | field | `boost::optional< std::vector<InputLayerType> >` | private | If this is boost::none then it means the layer input is from a feature collection (file) and not from the output of another layer. |

## Free functions and macros

| Name | Kind | Type / body | Description |
|---|---|---|---|
| `GPLATES_APP_LOGIC_LAYERCONNECTIONTYPE_H` | macro | `None` | — |

## Notes

`can_connect_to_input_feature_collections()` is equivalent to `get_input_layer_types()` returning `boost::none`: a channel is either file-fed or layer-fed, never both, and that distinction is encoded purely by whether `d_input_layer_types` is set, not by a separate flag. The two-argument (file-only) and multi-argument (layer-output) constructors are the only ways to obtain each case respectively; the single-`LayerTaskType`/`InputLayerType` constructors are pure convenience wrappers that build the one-element vector.

## Used by

| Unit | Component | References |
|---|---|---|
| [app-logic/ReconstructGraph](ReconstructGraph.md) | app-logic | 15 |
| [qt-widgets/VisualLayerWidget](../qt-widgets/VisualLayerWidget.md) | qt-widgets | 14 |
| [app-logic/ReconstructLayerTask](ReconstructLayerTask.md) | app-logic | 12 |
| [app-logic/VelocityFieldCalculatorLayerTask](VelocityFieldCalculatorLayerTask.md) | app-logic | 6 |
| [app-logic/RasterLayerTask](RasterLayerTask.md) | app-logic | 5 |
| [app-logic/ScalarField3DLayerTask](ScalarField3DLayerTask.md) | app-logic | 4 |
| [app-logic/TopologyGeometryResolverLayerTask](TopologyGeometryResolverLayerTask.md) | app-logic | 4 |
| [app-logic/CoRegistrationLayerTask](CoRegistrationLayerTask.md) | app-logic | 3 |
| [app-logic/Layer](Layer.md) | app-logic | 3 |
| [app-logic/ReconstructScalarCoverageLayerTask](ReconstructScalarCoverageLayerTask.md) | app-logic | 3 |
| [app-logic/TopologyNetworkResolverLayerTask](TopologyNetworkResolverLayerTask.md) | app-logic | 3 |
| [app-logic/LayerTask](LayerTask.md) | app-logic | 2 |
| [app-logic/LayerTaskRegistry](LayerTaskRegistry.md) | app-logic | 2 |
| [app-logic/ReconstructionLayerTask](ReconstructionLayerTask.md) | app-logic | 2 |
| [qt-widgets/ConfigureVelocityLegendOverlayDialog](../qt-widgets/ConfigureVelocityLegendOverlayDialog.md) | qt-widgets | 1 |
| [qt-widgets/TotalReconstructionPolesDialog](../qt-widgets/TotalReconstructionPolesDialog.md) | qt-widgets | 1 |

## Related

*None.*

## Explore

Run these from the `gplates-code` skill directory:

```bash
python scripts/gpq.py file src/app-logic/LayerInputChannelType.h
python scripts/gpq.py def GPlatesAppLogic::LayerInputChannelType --body
python scripts/gpq.py uses LayerInputChannelType --kind class
python scripts/gpq.py hier LayerInputChannelType
```
