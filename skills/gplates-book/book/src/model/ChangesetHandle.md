# ChangesetHandle

[Book TOC](../../TOC.md) · [model](../../components/model.md) · cluster Community 817 · tier 2

| Source file | Kind | Lines |
|---|---|---|
| `src/model/ChangesetHandle.h` | C++ | 142 |
| `src/model/ChangesetHandle.cc` | C++ | 76 |

## Overview

`ChangesetHandle` lets client code group several model transactions into one
logical, user-undoable changeset. A model transaction — adding a feature,
changing a property — is often too fine-grained to present as a single undo
step; without an active `ChangesetHandle`, each `*Handle` mutation generates its
own implicit changeset instead. Client code uses it in RAII style: constructing
one on the stack scopes all transactions between construction and destruction
into that changeset, and the constructor registers the handle with the
`Model` it belongs to (`Model::register_changeset_handle`) while the destructor
unregisters it.

`ChangesetHandle`s nest: only the outermost one in a call chain is operative, so
a helper function that opens its own changeset still gets folded into a
caller's broader one if the caller already opened one. The class carries a
human-readable `description` for the UI and a set of modified handles, but per
its own Doxygen comment it "currently does nothing useful" beyond the
registration bookkeeping — the tracking members exist for future undo/redo
support that has not been built on top of it yet.

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

- `model_ptr` may be `NULL`; when it is, the handle registers with nothing and
  is a no-op for its whole lifetime.
- `ChangesetHandle` derives from `boost::noncopyable`: it is meant to be
  constructed once on the stack at the scope that should own the changeset, not
  copied or passed around by value.
- The class does not itself implement undo/redo — it only records which handles
  were touched — so do not expect constructing one to make changes revertible.

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
