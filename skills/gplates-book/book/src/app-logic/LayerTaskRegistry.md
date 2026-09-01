# LayerTaskRegistry

[Book TOC](../../TOC.md) · [app-logic](../../components/app-logic.md) · cluster Community 202 · tier 2

| Source file | Kind | Lines |
|---|---|---|
| `src/app-logic/LayerTaskRegistry.h` | C++ | 205 |
| `src/app-logic/LayerTaskRegistry.cc` | C++ | 230 |

## Overview

[[[PROSE overview unit=app-logic/LayerTaskRegistry tier=2]]]
Replace this whole block, markers included, with 1-3 paragraphs: what this unit is, why it exists, and how it fits the surrounding design. Do not restate the tables below.
[[[/PROSE]]]

## Declared types

| Name | Kind | Bases | Template | Subclasses | Description |
|---|---|---|---|---|---|
| [`GPlatesAppLogic::LayerTaskRegistry`](#gplatesapplogiclayertaskregistry) | class | — | — | 0 | Manages registration of functions used to create LayerTask types and handles calling those functions to create the LayerTask objects. |

## Members

### `GPlatesAppLogic::LayerTaskRegistry`

| Member | Kind | Type | Access | Description |
|---|---|---|---|---|
| `LayerTaskType` | class | `None` | public | Wrapper around a layer task type. |
| `create_layer_task_function_type` | typedef | `boost::function< boost::shared_ptr<LayerTask> () >` | public | Typedef for a function to create a LayerTask. |
| `should_auto_create_layer_task_for_loaded_file_function_type` | typedef | `boost::function< bool (const GPlatesModel::FeatureCollectionHandle::const_weak_ref &) >` | public | Typedef for a function used to see if a LayerTask should be auto-created to process a feature collection when it is loaded. |
| `register_layer_task_type( const create_layer_task_function_type &create_layer_task_function, const should_auto_create_layer_task_for_loaded_file_function_type & should_auto_create_layer_task_for_loaded_file_function, GPlatesAppLogic::LayerTaskType::Type layer_type)` | method | `LayerTaskType` | public | Register a LayerTask type. |
| `unregister_layer_task_type( const LayerTaskType &)` | method | `void` | public | Unregisters LayerTask type. |
| `get_all_layer_task_types()` | method | `std::vector<LayerTaskType>` | public | Returns a sequence of all registered LayerTask types. |
| `get_layer_task_types_to_auto_create_for_loaded_file( const GPlatesModel::FeatureCollectionHandle::const_weak_ref &feature_collection)` | method | `std::vector<LayerTaskType>` | public | Returns a sequence of LayerTask types that should be created automatically, as opposed to manually created by the user, as a result of feature\_collection having been loaded. |
| `LayerTaskTypeInfo` | class | `None` | private | Contains layer-task-specific functions provided by the client. |
| `layer_task_type_seq_type` | typedef | `std::list< boost::shared_ptr<const LayerTaskTypeInfo> >` | private | Typedef for a sequence of layer task types. |
| `d_layer_task_types` | field | `layer_task_type_seq_type` | private | — |

## Free functions and macros

| Name | Kind | Type / body | Description |
|---|---|---|---|
| `GPLATES_APP_LOGIC_LAYERTASKREGISTRY_H` | macro | `None` | — |
| `register_default_layer_task_types( LayerTaskRegistry &layer_task_registry, ApplicationState &application_state)` | function | `void` | Register the default layer tasks with layer\_task\_registry. |

## Notes

[[[PROSE notes unit=app-logic/LayerTaskRegistry tier=2]]]
Replace this whole block, markers included, with invariants, ownership, threading or gotchas that are not visible in the tables. Write *None.* if there is nothing worth saying.
[[[/PROSE]]]

## Used by

| Unit | Component | References |
|---|---|---|
| [presentation/DeprecatedSessionRestore](../presentation/DeprecatedSessionRestore.md) | presentation | 30 |
| [presentation/TranscribeSession](../presentation/TranscribeSession.md) | presentation | 16 |
| [app-logic/ReconstructGraph](ReconstructGraph.md) | app-logic | 13 |
| [presentation/VisualLayerRegistry](../presentation/VisualLayerRegistry.md) | presentation | 7 |
| [app-logic/ReconstructLayerTask](ReconstructLayerTask.md) | app-logic | 4 |
| [qt-widgets/AssignReconstructionPlateIdsDialog](../qt-widgets/AssignReconstructionPlateIdsDialog.md) | qt-widgets | 4 |
| [qt-widgets/DrawStyleDialog](../qt-widgets/DrawStyleDialog.md) | qt-widgets | 4 |
| [qt-widgets/VisualLayerWidget](../qt-widgets/VisualLayerWidget.md) | qt-widgets | 4 |
| [app-logic/ApplicationState](ApplicationState.md) | app-logic | 3 |
| [qt-widgets/CoRegistrationLayerConfigurationDialog](../qt-widgets/CoRegistrationLayerConfigurationDialog.md) | qt-widgets | 3 |
| [gui/ExportDeformationAnimationStrategy](../gui/ExportDeformationAnimationStrategy.md) | gui | 2 |
| [gui/ExportRasterAnimationStrategy](../gui/ExportRasterAnimationStrategy.md) | gui | 2 |
| [gui/ExportScalarCoverageAnimationStrategy](../gui/ExportScalarCoverageAnimationStrategy.md) | gui | 2 |
| [gui/ExportVelocityAnimationStrategy](../gui/ExportVelocityAnimationStrategy.md) | gui | 2 |
| [presentation/VisualLayers](../presentation/VisualLayers.md) | presentation | 2 |
| [qt-widgets/GenerateDeformingMeshPointsDialog](../qt-widgets/GenerateDeformingMeshPointsDialog.md) | qt-widgets | 2 |
| [gui/ExportCitcomsResolvedTopologyAnimationStrategy](../gui/ExportCitcomsResolvedTopologyAnimationStrategy.md) | gui | 1 |
| [gui/ExportFlowlineAnimationStrategy](../gui/ExportFlowlineAnimationStrategy.md) | gui | 1 |
| [gui/ExportMotionPathAnimationStrategy](../gui/ExportMotionPathAnimationStrategy.md) | gui | 1 |
| [gui/ExportNetRotationAnimationStrategy](../gui/ExportNetRotationAnimationStrategy.md) | gui | 1 |

*... and 4 more units.*

## Related

*None.*

## Explore

Run these from the `gplates-code` skill directory:

```bash
python scripts/gpq.py file src/app-logic/LayerTaskRegistry.h
python scripts/gpq.py def GPlatesAppLogic::LayerTaskRegistry --body
python scripts/gpq.py uses LayerTaskRegistry --kind class
python scripts/gpq.py hier LayerTaskRegistry
```
