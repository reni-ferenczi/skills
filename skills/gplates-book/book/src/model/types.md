# types

[Book TOC](../../TOC.md) · [model](../../components/model.md) · cluster Community 138 · tier 1

| Source file | Kind | Lines |
|---|---|---|
| `src/model/types.h` | C++ | 53 |

## Overview

[[[PROSE overview unit=model/types tier=1]]]
Replace this whole block, markers included, with 1-3 paragraphs: what this unit is, why it exists, and how it fits the surrounding design. Do not restate the tables below.
[[[/PROSE]]]

## Declared types

| Name | Kind | Bases | Template | Subclasses | Description |
|---|---|---|---|---|---|
| [`GPlatesModel::integer_plate_id_type`](#gplatesmodelinteger_plate_id_type) | typedef | — | — | 0 | This is the type which is used to represent integer plate IDs. |
| [`GPlatesModel::container_size_type`](#gplatesmodelcontainer_size_type) | typedef | — | — | 0 | This is the type which is used to describe the sizes of containers of properties, features, and feature collections, and also for the indices into these containers. |

## Members

### `GPlatesModel::integer_plate_id_type`

*None.*

### `GPlatesModel::container_size_type`

*None.*

## Free functions and macros

| Name | Kind | Type / body | Description |
|---|---|---|---|
| `GPLATES_MODEL_TYPES_H` | macro | `None` | — |
| `INVALID_INDEX` | variable | `container_size_type` | This is the value used to indicate an invalid index. |

## Notes

[[[PROSE notes unit=model/types tier=1]]]
Replace this whole block, markers included, with invariants, ownership, threading or gotchas that are not visible in the tables. Write *None.* if there is nothing worth saying.
[[[/PROSE]]]

## Used by

| Unit | Component | References |
|---|---|---|
| [app-logic/ReconstructionTreeCreator](../app-logic/ReconstructionTreeCreator.md) | app-logic | 36 |
| [app-logic/ReconstructionTree](../app-logic/ReconstructionTree.md) | app-logic | 35 |
| [app-logic/TopologyReconstruct](../app-logic/TopologyReconstruct.md) | app-logic | 23 |
| [model/BasicRevision](BasicRevision.md) | model | 21 |
| [model/BasicHandle](BasicHandle.md) | model | 18 |
| [qt-widgets/TotalReconstructionSequencesDialog](../qt-widgets/TotalReconstructionSequencesDialog.md) | qt-widgets | 18 |
| [file-io/CitcomsResolvedTopologicalBoundaryExport](../file-io/CitcomsResolvedTopologicalBoundaryExport.md) | file-io | 17 |
| [app-logic/RotationUtils](../app-logic/RotationUtils.md) | app-logic | 15 |
| [app-logic/FlowlineUtils](../app-logic/FlowlineUtils.md) | app-logic | 14 |
| [app-logic/PartitionFeatureUtils](../app-logic/PartitionFeatureUtils.md) | app-logic | 13 |
| [app-logic/ReconstructUtils](../app-logic/ReconstructUtils.md) | app-logic | 13 |
| [app-logic/ReconstructionLayerProxy](../app-logic/ReconstructionLayerProxy.md) | app-logic | 13 |
| [gui/ExportStageRotationAnimationStrategy](../gui/ExportStageRotationAnimationStrategy.md) | gui | 12 |
| [app-logic/ReconstructedFeatureGeometry](../app-logic/ReconstructedFeatureGeometry.md) | app-logic | 11 |
| [app-logic/ReconstructionGraph](../app-logic/ReconstructionGraph.md) | app-logic | 11 |
| [file-io/PlatesRotationFormatReader](../file-io/PlatesRotationFormatReader.md) | file-io | 11 |
| [property-values/GpmlOldPlatesHeader](../property-values/GpmlOldPlatesHeader.md) | property-values | 11 |
| [qt-widgets/MovePoleWidget](../qt-widgets/MovePoleWidget.md) | qt-widgets | 11 |
| [qt-widgets/SpecifyAnchoredPlateIdDialog](../qt-widgets/SpecifyAnchoredPlateIdDialog.md) | qt-widgets | 11 |
| [app-logic/PlateVelocityUtils](../app-logic/PlateVelocityUtils.md) | app-logic | 10 |

*... and 149 more units.*

## Related

*None.*

## Explore

Run these from the `gplates-code` skill directory:

```bash
python scripts/gpq.py file src/model/types.h
python scripts/gpq.py def GPlatesModel::integer_plate_id_type --body
python scripts/gpq.py uses integer_plate_id_type --kind typedef
```
