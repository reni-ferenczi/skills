# ChangesetHandle

[Book TOC](../../TOC.md) · [model](../../components/model.md) · cluster Community 817 · tier 2

| Source file | Kind | Lines |
|---|---|---|
| `src/model/ChangesetHandle.h` | C++ | 142 |
| `src/model/ChangesetHandle.cc` | C++ | 76 |

## Overview

[[[PROSE overview unit=model/ChangesetHandle tier=2]]]
Replace this whole block, markers included, with 1-3 paragraphs: what this unit is, why it exists, and how it fits the surrounding design. Do not restate the tables below.
[[[/PROSE]]]

## Declared types

| Name | Kind | Bases | Template | Subclasses | Description |
|---|---|---|---|---|---|
| [`GPlatesModel::ChangesetHandle`](#gplatesmodelchangesethandle) | class | `boost::noncopyable` | — | 0 | A model transaction is an atomic operation (such as the addition of one feature into a feature collection, or the changing of one property in a feature). |

## Members

### `GPlatesModel::ChangesetHandle`

| Member | Kind | Type | Access | Description |
|---|---|---|---|---|
| `ChangesetHandle( Model *model_ptr, const std::string &description_ = std::string())` | constructor | `None` | public | Constructs a ChangesetHandle that will construct a changeset belonging to model upon destruction. model may be NULL. |
| `~ChangesetHandle()` | destructor | `None` | public | Destructor. |
| `description` | field | `std::string` | public | Returns the human-readable description of the changeset. |
| `add_handle( const void *handle)` | method | `void` | public | Registers handle as having been modified or added in this changeset. |
| `has_handle( const void *handle)` | method | `bool` | public | Returns true if handle has already been registered in this changeset. |
| `d_model_ptr` | field | `Model` | private | — |
| `d_description` | field | `std::string` | private | — |
| `d_modified_handles` | field | `std::set<const void *>` | private | This is a collection of raw pointers to Handles that have been modified or added in this changeset. |

## Free functions and macros

| Name | Kind | Type / body | Description |
|---|---|---|---|
| `GPLATES_MODEL_CHANGESETHANDLE_H` | macro | `None` | — |

## Notes

[[[PROSE notes unit=model/ChangesetHandle tier=2]]]
Replace this whole block, markers included, with invariants, ownership, threading or gotchas that are not visible in the tables. Write *None.* if there is nothing worth saying.
[[[/PROSE]]]

## Used by

| Unit | Component | References |
|---|---|---|
| [file-io/GpmlReader](../file-io/GpmlReader.md) | file-io | 18 |
| [app-logic/FeatureCollectionFileIO](../app-logic/FeatureCollectionFileIO.md) | app-logic | 13 |
| [model/FeatureHandle](FeatureHandle.md) | model | 11 |
| [model/BasicHandle](BasicHandle.md) | model | 10 |
| [model/Model](Model.md) | model | 5 |
| [file-io/OgrReader](../file-io/OgrReader.md) | file-io | 2 |
| [qt-widgets/EditTotalReconstructionSequenceWidget](../qt-widgets/EditTotalReconstructionSequenceWidget.md) | qt-widgets | 2 |
| [qt-widgets/TotalReconstructionSequencesDialog](../qt-widgets/TotalReconstructionSequencesDialog.md) | qt-widgets | 2 |
| [file-io/PlatesLineFormatReader](../file-io/PlatesLineFormatReader.md) | file-io | 1 |
| [file-io/PlatesRotationFormatReader](../file-io/PlatesRotationFormatReader.md) | file-io | 1 |
| [model/ModelUtils](ModelUtils.md) | model | 1 |
| [qt-widgets/CreateFeatureDialog](../qt-widgets/CreateFeatureDialog.md) | qt-widgets | 1 |
| [qt-widgets/CreateSmallCircleFeatureDialog](../qt-widgets/CreateSmallCircleFeatureDialog.md) | qt-widgets | 1 |
| [qt-widgets/CreateVGPDialog](../qt-widgets/CreateVGPDialog.md) | qt-widgets | 1 |
| [qt-widgets/MetadataDialog](../qt-widgets/MetadataDialog.md) | qt-widgets | 1 |

## Related

*None.*

## Explore

Run these from the `gplates-code` skill directory:

```bash
python scripts/gpq.py file src/model/ChangesetHandle.h
python scripts/gpq.py def GPlatesModel::ChangesetHandle --body
python scripts/gpq.py uses ChangesetHandle --kind class
python scripts/gpq.py hier ChangesetHandle
```
