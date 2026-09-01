# types

[Book TOC](../../TOC.md) · [model](../../components/model.md) · cluster Community 138 · tier 1

| Source file | Kind | Lines |
|---|---|---|
| `src/model/types.h` | C++ | 53 |

## Overview

A three-declaration header that exists to be included from anywhere. Its own comments
give the reason twice: `container_size_type` and `INVALID_INDEX` are defined here
rather than taken from the `size_type` of whichever container is actually involved
"to avoid circular header includes and to simplify code in general". The model's
containers, their iterators and the handles that index into them all need to name the
same index type, but they cannot include each other, so they all include this instead.
`integer_plate_id_type` is here for the same reason on a much wider scale — it is the
spelling of a plate ID everywhere in GPlates, from `PlatesRotationFormatReader`
parsing a `.rot` line, through `ReconstructionTree` and `ReconstructionTreeCreator`
building the plate circuit, out to `SpecifyAnchoredPlateIdDialog` in the GUI. The fan-in
is the point of the file; there is no behaviour in it to understand.

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

- `INVALID_INDEX` is initialised from `-1` and `container_size_type` is `size_t`, so
  its value is `SIZE_MAX`, not a negative number. It is only ever compared, never
  arithmetic — `BasicHandle` and `RevisionAwareIterator` initialise their index
  members with it and `TopLevelPropertyRef` tests against it. An index that is
  incremented past the end silently becomes a plausible-looking large index, not
  `INVALID_INDEX`.
- Being a namespace-scope `static const` in a header, `INVALID_INDEX` has internal
  linkage: every translation unit gets its own copy. Comparing values is fine;
  taking its address, binding it to a reference across a translation-unit boundary, or
  expecting one definition is not.
- `integer_plate_id_type` is `unsigned long`, whose width is platform-dependent
  (32-bit under MSVC, 64-bit under LP64). It is fine as an in-memory type, but do not
  assume a fixed byte width when writing binary formats, and pick printf-style format
  specifiers accordingly.
- The header has no `#include` directives at all, yet uses `size_t`. It compiles only
  because every current include site has already pulled in a header that declares it.
  Adding a first, direct include of this file from a translation unit that has not may
  fail to build.

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
