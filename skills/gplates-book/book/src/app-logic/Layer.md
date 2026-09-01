# Layer

[Book TOC](../../TOC.md) · [app-logic](../../components/app-logic.md) · cluster Community 181 · tier 1

| Source file | Kind | Lines |
|---|---|---|
| `src/app-logic/Layer.h` | C++ | 618 |
| `src/app-logic/Layer.cc` | C++ | 555 |

## Overview

`Layer` is the public face of a node in the reconstruct graph. The node itself is
`ReconstructGraphImpl::Layer`, owned by `ReconstructGraph` in a
`std::list<boost::shared_ptr<...>>`; everything outside `app-logic` — the layer
options widgets, `VisualLayers`, the session save/restore code — holds this
handle instead, which is nothing but a `boost::weak_ptr` to that implementation
node plus the operations that are safe to expose. The two nested wrappers follow
the same pattern: `InputFile` wraps a `ReconstructGraphImpl::Data` created from a
loaded file, and `InputConnection` wraps a
`ReconstructGraphImpl::LayerInputConnection`, the edge joining one data object to
one input channel of one layer. Because all three are weak, copying them freely
and storing them in GUI objects is safe; the graph decides lifetime, and a stale
handle reports `is_valid() == false` rather than dangling.

The three things a layer is made of are reached through here but implemented
elsewhere. Its behaviour is a `LayerTask` (`get_type`,
`get_input_channel_types`, `get_main_input_feature_collection_channel` all just
forward to it, and `set_layer_task` swaps it wholesale); its user-visible
settings are a `LayerParams`; and its output is a `LayerProxy`, the lazily
evaluated pull-model result described on that page. `get_layer_output()` is the
normal way into the second half of the pipeline, and the templated overload
combines the fetch with a `LayerProxyUtils::get_layer_proxy_derived_type` cast so
callers that know they are talking to, say, a `ReconstructionLayerProxy` can skip
the visitor.

The connect/disconnect methods are also the graph's mutation API: there is no
separate edge-building interface. Each of them performs the structural change on
the implementation objects and then asks the owning `ReconstructGraph` to emit
the matching Qt signal, so the GUI stays in step without `Layer` knowing anything
about it. `LayerInputChannelName::Type` identifies the channel in every one of
these calls, and a channel is a multimap key, not a slot — several inputs may
share one channel, which is why the disconnect helpers search the channel's
connections for a match instead of indexing.

## Declared types

| Name | Kind | Bases | Template | Subclasses | Description |
|---|---|---|---|---|---|
| [`GPlatesAppLogic::Layer`](#gplatesapplogiclayer) | class | `boost::equivalent<Layer>`<br>`boost::equality_comparable<Layer>` | — | 0 | Wrapper around a layer of ReconstructGraph that can be used to query the layer. |

## Members

### `GPlatesAppLogic::Layer`

| Member | Kind | Type | Access | Description |
|---|---|---|---|---|
| `InputFile` | class | `None` | public | Wrapper around an input file to a layer. |
| `InputConnection` | class | `None` | public | Wrapper around an input connection of a layer. |
| `CycleDetectedInReconstructGraph` | class | `None` | public | Exception thrown when a cycle is detected in the reconstruct graph. |
| `Layer( const boost::weak_ptr<ReconstructGraphImpl::Layer> &layer_impl = boost::weak_ptr<ReconstructGraphImpl::Layer>())` | constructor | `None` | public | Constructor. |
| `is_valid()` | method | `bool` | public | Returns true if this layer is still valid and has not been destroyed. |
| `is_active()` | method | `bool` | public | Returns true if this layer is currently active. |
| `activate( bool active = true)` | method | `void` | public | Activates (or deactivates) this layer. |
| `get_type()` | method | `LayerTaskType::Type` | public | Returns the type of this layer. |
| `get_input_channel_types()` | method | `std::vector<LayerInputChannelType>` | public | Returns a description of each input channel of this layer. |
| `get_main_input_feature_collection_channel()` | method | `LayerInputChannelName::Type` | public | Returns the main input feature collection channel used by this layer. |
| `set_layer_task( const boost::shared_ptr<LayerTask> &layer_task)` | method | `void` | public | Changes the layer task for this layer. |
| `connect_input_to_file( const InputFile &input_file, LayerInputChannelName::Type input_data_channel)` | method | `InputConnection` | public | Connects a feature collection, from a loaded file, as input on the input\_data\_channel input channel. |
| `connect_input_to_layer_output( const Layer &layer_outputting_data, LayerInputChannelName::Type input_data_channel)` | method | `InputConnection` | public | Connects the output of the layer\_outputting\_data layer as input to the this layer on the input\_data\_channel input channel. |
| `disconnect_input_from_file( const InputFile &input_file, LayerInputChannelName::Type input_data_channel)` | method | `void` | public | Disconnects a feature collection, from a loaded file input\_file, as input on the input\_data\_channel input channel. |
| `disconnect_input_from_layer_output( const Layer &layer_outputting_data, LayerInputChannelName::Type input_data_channel)` | method | `void` | public | Disconnects the output of the layer\_outputting\_data as input on the input\_data\_channel input channel. |
| `disconnect_channel_inputs( LayerInputChannelName::Type input_data_channel)` | method | `void` | public | Disconnects all input data sources on input channel input\_data\_channel from this layer. |
| `get_channel_inputs( LayerInputChannelName::Type input_data_channel)` | method | `std::vector<InputConnection>` | public | Returns the input connections on input channel input\_data\_channel. |
| `get_all_inputs()` | method | `std::vector<InputConnection>` | public | Returns all input connections. |
| `get_layer_params()` | method | `LayerParams::non_null_ptr_type` | public | Returns a non-const reference to the additional parameters and configuration options of this layer. |
| `get_layer_output()` | method | `boost::optional<typename LayerProxyDerivedType::non_null_ptr_type>` | public | Similar to the other overload of get\_layer\_output except attempts to cast to the specified derived LayerProxy type. |
| `get_layer_proxy_handle()` | method | `LayerProxyHandle::non_null_ptr_type` | public | Returns a handle to the layer proxy at the output of this layer. |
| `operator<( const Layer &rhs)` | operator | `bool` | public | 'operator==()' provided by boost::equivalent. |
| `d_impl` | field | `boost::weak_ptr<ReconstructGraphImpl::Layer>` | private | — |
| `get_auto_created()` | method | `bool` | public | FIXME: These method are public but should be private. |
| `set_auto_created( bool auto_created = true)` | method | `void` | public | — |

## Free functions and macros

| Name | Kind | Type / body | Description |
|---|---|---|---|
| `GPLATES_APP_LOGIC_LAYER_H` | macro | `None` | — |

## Notes

- **Validity is a precondition, not a return code.** Nearly every method opens
  with `GPlatesGlobal::Assert<PreconditionViolationError>(is_valid(), ...)` and
  then constructs a `boost::shared_ptr` from the weak one. Check `is_valid()`
  before calling anything on a handle you have been holding across graph edits or
  file unloads. `get_layer_output()` layers a second condition on top: it returns
  `boost::none` for a valid but *inactive* layer, deliberately, so that a
  disabled layer cannot be made to compute by a caller that got hold of its
  proxy. `get_layer_proxy_handle()` bypasses that check and always returns the
  proxy.
- **`CycleDetectedInReconstructGraph` is currently dead.** `connect_input_to_layer_output`
  still calls `ReconstructGraphImpl::detect_cycle_in_graph`, but that function's
  body is inside `#if 0` and it unconditionally returns false — the comment
  explains why (a raster consuming an age grid that in turn uses the raster as a
  normal map is a graph cycle but not a dependency cycle). Keep catching the
  exception, but do not rely on the graph being acyclic.
- **Signal ordering in `InputConnection::disconnect()` is deliberate.**
  `layer_about_to_remove_input_connection` is emitted first; then the last owning
  `shared_ptr` is dropped inside its own scope so that
  `~LayerInputConnection` — which notifies the connected layers — completes
  while app-logic state is still private; only then is
  `layer_removed_input_connection` emitted. Do not flatten that scope. Note also
  that `this` is invalid on return, and that no signal at all is emitted when a
  connection dies because its parent layer was removed.
- **Ownership of connections is one-directional.** A returned `InputConnection`
  is a weak reference and does not need to be kept alive; the parent layer holds
  the only owning reference. Conversely, `Data` holds raw
  `LayerInputConnection *` back-pointers in its output list, so a connection must
  outlive nothing and unregister itself on destruction.
- `get_auto_created` / `set_auto_created` are marked in the header as wanting to
  be private; they are public only so session save/restore can reach them. Do not
  treat them as general API.

## Used by

| Unit | Component | References |
|---|---|---|
| [app-logic/ReconstructGraph](ReconstructGraph.md) | app-logic | 139 |
| [qt-widgets/ScalarField3DLayerOptionsWidget](../qt-widgets/ScalarField3DLayerOptionsWidget.md) | qt-widgets | 81 |
| [presentation/TranscribeSession](../presentation/TranscribeSession.md) | presentation | 78 |
| [qt-widgets/CoRegistrationLayerConfigurationDialog](../qt-widgets/CoRegistrationLayerConfigurationDialog.md) | qt-widgets | 69 |
| [qt-widgets/VisualLayerWidget](../qt-widgets/VisualLayerWidget.md) | qt-widgets | 58 |
| [presentation/DeprecatedSessionRestore](../presentation/DeprecatedSessionRestore.md) | presentation | 53 |
| [qt-widgets/MergeReconstructionLayersDialog](../qt-widgets/MergeReconstructionLayersDialog.md) | qt-widgets | 42 |
| [presentation/VisualLayers](../presentation/VisualLayers.md) | presentation | 38 |
| [qt-widgets/TopologyNetworkResolverLayerOptionsWidget](../qt-widgets/TopologyNetworkResolverLayerOptionsWidget.md) | qt-widgets | 36 |
| [qt-widgets/VelocityFieldCalculatorLayerOptionsWidget](../qt-widgets/VelocityFieldCalculatorLayerOptionsWidget.md) | qt-widgets | 24 |
| [presentation/VisualLayer](../presentation/VisualLayer.md) | presentation | 23 |
| [gui/TopologyTools](../gui/TopologyTools.md) | gui | 19 |
| [app-logic/LayerProxyUtils](LayerProxyUtils.md) | app-logic | 18 |
| [qt-widgets/RasterLayerOptionsWidget](../qt-widgets/RasterLayerOptionsWidget.md) | qt-widgets | 15 |
| [qt-widgets/ReconstructScalarCoverageLayerOptionsWidget](../qt-widgets/ReconstructScalarCoverageLayerOptionsWidget.md) | qt-widgets | 13 |
| [gui/ExportCitcomsResolvedTopologyAnimationStrategy](../gui/ExportCitcomsResolvedTopologyAnimationStrategy.md) | gui | 12 |
| [gui/ExportReconstructedGeometryAnimationStrategy](../gui/ExportReconstructedGeometryAnimationStrategy.md) | gui | 12 |
| [gui/ExportFlowlineAnimationStrategy](../gui/ExportFlowlineAnimationStrategy.md) | gui | 11 |
| [gui/ExportMotionPathAnimationStrategy](../gui/ExportMotionPathAnimationStrategy.md) | gui | 11 |
| [gui/ExportNetRotationAnimationStrategy](../gui/ExportNetRotationAnimationStrategy.md) | gui | 11 |

*... and 83 more units.*

## Related

*None.*

## Explore

Run these from the `gplates-code` skill directory:

```bash
python scripts/gpq.py file src/app-logic/Layer.h
python scripts/gpq.py def GPlatesAppLogic::Layer --body
python scripts/gpq.py uses Layer --kind class
python scripts/gpq.py hier Layer
```
