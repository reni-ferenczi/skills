# ReconstructGraphImpl

[Book TOC](../../TOC.md) · [app-logic](../../components/app-logic.md) · cluster Community 520 · tier 2

| Source file | Kind | Lines |
|---|---|---|
| `src/app-logic/ReconstructGraphImpl.h` | C++ | 481 |
| `src/app-logic/ReconstructGraphImpl.cc` | C++ | 583 |

## Overview

[[[PROSE overview unit=app-logic/ReconstructGraphImpl tier=2]]]
Replace this whole block, markers included, with 1-3 paragraphs: what this unit is, why it exists, and how it fits the surrounding design. Do not restate the tables below.
[[[/PROSE]]]

## Declared types

| Name | Kind | Bases | Template | Subclasses | Description |
|---|---|---|---|---|---|
| [`GPlatesAppLogic::ReconstructGraphImpl::Data`](#gplatesapplogicreconstructgraphimpldata) | class | `boost::noncopyable` | — | 0 | Data objects in the Reconstruct Graph Implementation are a wrapper around the two kinds of data you find in the graph. |
| [`GPlatesAppLogic::ReconstructGraphImpl::LayerInputConnection`](#gplatesapplogicreconstructgraphimpllayerinputconnection) | class | `boost::noncopyable` | — | 0 | — |
| [`GPlatesAppLogic::ReconstructGraphImpl::LayerInputConnections`](#gplatesapplogicreconstructgraphimpllayerinputconnections) | class | `boost::noncopyable` | — | 0 | — |
| [`GPlatesAppLogic::ReconstructGraphImpl::Layer`](#gplatesapplogicreconstructgraphimpllayer) | class | `boost::noncopyable` | — | 0 | — |

## Members

### `GPlatesAppLogic::ReconstructGraphImpl::Data`

| Member | Kind | Type | Access | Description |
|---|---|---|---|---|
| `connection_seq_type` | typedef | `std::list<LayerInputConnection *>` | public | — |
| `Data( const FeatureCollectionFileState::file_reference &file)` | constructor | `None` | public | Constructor used when connecting a layer to an input feature collection. |
| `Data( const LayerProxy::non_null_ptr_type &layer_proxy)` | constructor | `None` | public | Constructor used when connecting a layer to an output of another layer. |
| `get_input_file()` | method | `boost::optional<FeatureCollectionFileState::file_reference>` | public | Returns the input file. |
| `get_layer_proxy()` | method | `boost::optional<LayerProxy::non_null_ptr_type>` | public | Returns the layer proxy. |
| `get_outputting_layer()` | method | `boost::optional< boost::weak_ptr<Layer> >` | public | Returns the layer outputting us. |
| `set_outputting_layer( const boost::weak_ptr<Layer> &outputting_layer)` | method | `void` | public | Sets the layer that outputs data to 'this'. |
| `add_output_connection( LayerInputConnection *layer_input_connection)` | method | `void` | public | — |
| `remove_output_connection( LayerInputConnection *layer_input_connection)` | method | `void` | public | — |
| `disconnect_output_connections()` | method | `void` | public | Gets all output connections to disconnect themselves from their parent layers, which will destroy them, which will remove them from our output connections list. |
| `data_type` | typedef | `boost::variant< FeatureCollectionFileState::file_reference, LayerProxy::non_null_ptr_type>` | private | Typedef for the data that differs depending on whether this data object is an input feature collection or the output of a layer. |
| `d_data` | field | `data_type` | private | — |
| `d_output_connections` | field | `connection_seq_type` | private | — |
| `d_outputting_layer` | field | `boost::optional< boost::weak_ptr<Layer> >` | private | Only used if this data object is the output of a layer. |

### `GPlatesAppLogic::ReconstructGraphImpl::LayerInputConnection`

| Member | Kind | Type | Access | Description |
|---|---|---|---|---|
| `LayerInputConnection( const boost::shared_ptr<Data> &input_data, const boost::weak_ptr<Layer> &layer_receiving_input, LayerInputChannelName::Type layer_input_channel_name, bool is_input_layer_active = true)` | constructor | `None` | public | PreconditionViolationError if input\_data is NULL. is\_input\_layer\_active is only used if the input is a layer (ie, if the input data is the output of another layer). |
| `~LayerInputConnection()` | destructor | `None` | public | — |
| `get_input_channel_name()` | method | `LayerInputChannelName::Type` | public | — |
| `disconnect_from_parent_layer()` | method | `void` | public | NOTE: this will effectively destroy 'this' since our parent layer has the only owning reference to 'this'. |
| `input_layer_activated( bool active)` | method | `void` | public | Called when the input layer has been activated/deactivated (if the input is a layer). |
| `FeatureCollectionModified` | class | `None` | private | Receives notifications when input file, if connected to one, is modified. |
| `modified_input_feature_collection()` | method | `void` | private | — |
| `d_input_data` | field | `boost::shared_ptr<Data>` | private | — |
| `d_layer_receiving_input` | field | `boost::weak_ptr<Layer>` | private | — |
| `d_layer_input_channel_name` | field | `LayerInputChannelName::Type` | private | — |
| `d_is_input_layer_active` | field | `bool` | private | — |
| `d_callback_input_feature_collection` | field | `GPlatesModel::FeatureCollectionHandle::const_weak_ref` | private | Keep a reference to the input feature collection just for our callback - if the input is not a file then this data member is ignored. |

### `GPlatesAppLogic::ReconstructGraphImpl::LayerInputConnections`

| Member | Kind | Type | Access | Description |
|---|---|---|---|---|
| `connection_seq_type` | typedef | `std::vector< boost::shared_ptr<LayerInputConnection> >` | public | — |
| `input_connection_map_type` | typedef | `std::multimap< LayerInputChannelName::Type, boost::shared_ptr<LayerInputConnection> >` | public | — |
| `add_input_connection( LayerInputChannelName::Type input_channel_name, const boost::shared_ptr<LayerInputConnection> &input_connection)` | method | `void` | public | NOTE: should only be called by class LayerInputConnection. |
| `remove_input_connection( LayerInputChannelName::Type input_channel_name, LayerInputConnection *input_connection)` | method | `void` | public | NOTE: should only be called by class LayerInputConnection. |
| `get_input_connections()` | method | `connection_seq_type` | public | Returns all input connections as a sequence of LayerInputConnection pointers. |
| `get_input_connections( LayerInputChannelName::Type input_channel_name)` | method | `connection_seq_type` | public | Returns all input connections associated with the channel input\_channel\_name as a sequence of LayerInputConnection pointers. |
| `d_connections` | field | `input_connection_map_type` | private | — |

### `GPlatesAppLogic::ReconstructGraphImpl::Layer`

| Member | Kind | Type | Access | Description |
|---|---|---|---|---|
| `Layer( const boost::shared_ptr<LayerTask> &layer_task, ReconstructGraph &reconstruct_graph, bool auto_created = false)` | constructor | `None` | public | PreconditionViolationError if layer\_task is NULL. |
| `~Layer()` | destructor | `None` | public | — |
| `activate( bool active = true)` | method | `void` | public | Activates (or deactivates) this layer. |
| `is_active()` | method | `bool` | public | Returns true if 'this' layer is currently active |
| `get_auto_created()` | method | `bool` | public | Returns true if this layer was auto-created (when a file was loaded). |
| `set_auto_created( bool auto_created = true)` | method | `void` | public | — |
| `set_layer_task( const boost::shared_ptr<LayerTask> &layer_task)` | method | `void` | public | — |
| `get_layer_params()` | method | `LayerParams::non_null_ptr_type` | public | — |
| `d_reconstruct_graph` | field | `ReconstructGraph` | private | — |
| `d_layer_task` | field | `boost::shared_ptr<LayerTask>` | private | — |
| `d_input_data` | field | `LayerInputConnections` | private | — |
| `d_output_data` | field | `boost::shared_ptr<Data>` | private | — |
| `d_active` | field | `bool` | private | — |
| `d_auto_created` | field | `bool` | private | — |

## Free functions and macros

| Name | Kind | Type / body | Description |
|---|---|---|---|
| `GPLATES_APP_LOGIC_RECONSTRUCTGRAPHIMPL_H` | macro | `None` | — |
| `detect_cycle_in_graph( const Layer *originating_layer, const Layer *input_layer)` | function | `bool` | Returns true if a cycle would occur starting at originating\_layer and also ending at originating\_layer if originating\_layer had its input connected to the output of input\_layer. |

## Notes

[[[PROSE notes unit=app-logic/ReconstructGraphImpl tier=2]]]
Replace this whole block, markers included, with invariants, ownership, threading or gotchas that are not visible in the tables. Write *None.* if there is nothing worth saying.
[[[/PROSE]]]

## Used by

| Unit | Component | References |
|---|---|---|
| [app-logic/Layer](Layer.md) | app-logic | 34 |
| [app-logic/ReconstructGraph](ReconstructGraph.md) | app-logic | 11 |

## Related

*None.*

## Explore

Run these from the `gplates-code` skill directory:

```bash
python scripts/gpq.py file src/app-logic/ReconstructGraphImpl.h
python scripts/gpq.py def GPlatesAppLogic::ReconstructGraphImpl::LayerInputConnection --body
python scripts/gpq.py uses LayerInputConnection --kind class
python scripts/gpq.py hier LayerInputConnection
```
