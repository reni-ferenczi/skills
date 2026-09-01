# FeatureCollectionFileState

[Book TOC](../../TOC.md) · [app-logic](../../components/app-logic.md) · cluster Community 767 · tier 1

| Source file | Kind | Lines |
|---|---|---|
| `src/app-logic/FeatureCollectionFileState.h` | C++ | 561 |
| `src/app-logic/FeatureCollectionFileState.cc` | C++ | 545 |

## Overview

The registry of "which files are currently loaded", sitting between
`FeatureCollectionFileIO` (which actually reads and writes them) and everything
that needs to enumerate them — `ReconstructGraph` to wire feature collections into
layers, `ManageFeatureCollectionsDialog` to list them, `UnsavedChangesTracker` to
watch them. `ApplicationState` owns the single instance and forwards its signals.

The design turn that explains the whole class is that it is *not* the authority on
whether a file is loaded — the model is. `add_file_internal` calls
`File::add_feature_collection_to_model`, and `remove_file` removes the feature
collection from the feature store root and then deliberately does nothing else, not
even emit a signal. Loading and unloading are therefore ordinary model edits, and
so they are undoable. A `FeatureCollectionUnloadCallback` attached to each file's
feature collection turns the model's deactivated / reactivated /
about-to-be-destroyed events into this class's state changes and signals. That is
why undoing a file *add* produces `file_state_file_about_to_be_removed` from code
that never called `remove_file`, and why redoing it produces
`file_state_files_added` for a file the user did not load. Everything else here —
the slot array, the free-handle list, the separate index array — exists to make a
file's identity and its position survive that round trip.

Two identifier spaces do that work, and keeping them apart is the point.
`file_handle_type` is a private, stable slot index; a `FileReference` stores one
and nothing else, so a reference stays valid while other files come and go.
`file_index_type` is the public, dense position in load order, always contiguous
from zero over the currently loaded files, recomputed by walking `d_file_indices`
whenever a file deactivates or reactivates. `FileReference::get_file_index()` looks
it up on demand rather than caching it, which is what lets the header promise that
clients can mirror the sequence in their own vector and index it directly.
`FileReference` itself is a two-word value template parameterised on the constness
of the file state, with an implicit non-const to const conversion — the same
pattern the model uses for weak references.

## Declared types

| Name | Kind | Bases | Template | Subclasses | Description |
|---|---|---|---|---|---|
| [`GPlatesAppLogic::FeatureCollectionFileState`](#gplatesapplogicfeaturecollectionfilestate) | class | `QObject`<br>`boost::noncopyable` | — | 0 | Holds information associated with the currently loaded and active feature collection files. |

## Members

### `GPlatesAppLogic::FeatureCollectionFileState`

| Member | Kind | Type | Access | Description |
|---|---|---|---|---|
| `file_handle_type` | typedef | `std::size_t` | private | Typedef for a file handle. |
| `file_index_type` | typedef | `std::size_t` | public | Typedef for an index defining the order of currently loaded files. |
| `FileReference` | class | `None` | public | A reference to a file loaded into FeatureCollectionFileState. 'FileStateQualifiedType' can be either 'FeatureCollectionFileState' or 'const FeatureCollectionFileState'. |
| `const_file_reference` | typedef | `FileReference<const FeatureCollectionFileState>` | public | Typedef for a 'const' reference to a loaded file. |
| `file_reference` | typedef | `FileReference<FeatureCollectionFileState>` | public | Typedef for a 'non-const' reference to a loaded file. |
| `FeatureCollectionFileState( GPlatesModel::ModelInterface &model)` | constructor | `None` | public | Constructor. |
| `~FeatureCollectionFileState()` | destructor | `None` | public | Destructor. |
| `get_loaded_files()` | method | `std::vector<const_file_reference>` | public | Returns a sequence of 'const' file references to all currently loaded files. |
| `add_files( const std::vector<GPlatesFileIO::File::non_null_ptr_type> &files)` | method | `std::vector<file_reference>` | public | Adds multiple feature collection files and activates them. |
| `add_file( const GPlatesFileIO::File::non_null_ptr_type &file)` | method | `file_reference` | public | Adds a file and activates it. |
| `remove_file( file_reference file_ref)` | method | `void` | public | Remove file from the collection of currently loaded files. |
| `emit_file_reloaded()` | method | `void` | public | — |
| `file_state_files_added( GPlatesAppLogic::FeatureCollectionFileState &file_state, const std::vector<GPlatesAppLogic::FeatureCollectionFileState::file_reference> &new_files)` | method | `void` | public | The following signals only occur at the end (and in some cases also the beginning) of a public method of this class. |
| `file_state_file_about_to_be_removed( GPlatesAppLogic::FeatureCollectionFileState &file_state, GPlatesAppLogic::FeatureCollectionFileState::file_reference file)` | method | `void` | public | NOTE: Do not dereference the internal feature collection of file as it might be invalid (if this signal was generated when "undo"ing a file add). |
| `file_state_file_info_changed( GPlatesAppLogic::FeatureCollectionFileState &file_state, GPlatesAppLogic::FeatureCollectionFileState::file_reference file)` | method | `void` | public | — |
| `file_state_changed( GPlatesAppLogic::FeatureCollectionFileState &file_state)` | method | `void` | public | This signal is emitted \*after\* any file state has changed. |
| `file_reloaded( GPlatesAppLogic::FeatureCollectionFileState &file_state)` | method | `void` | public | — |
| `FileSlotExtra` | class | `None` | private | Contains a loaded file's shared reference and less frequently accessed information or information that is more expensive to copy. |
| `FileSlot` | class | `None` | private | A slot to store information about a file in a sequence of loaded files. |
| `file_slot_seq_type` | typedef | `std::vector<FileSlot>` | private | Typedef for a sequence of FileSlot objects. |
| `file_handles_seq_type` | typedef | `std::vector<file_handle_type>` | private | Typedef for a sequence of file handles. |
| `file_indices_seq_type` | typedef | `std::vector<file_index_type>` | private | Typedef for a sequence of indices indicating the order in which files were added. |
| `d_model` | field | `GPlatesModel::ModelInterface` | private | Used to add the feature collections of new files to the model. |
| `d_num_currently_loaded_files` | field | `std::size_t` | private | The number of loaded files (includes files that were deactivated in the \*model\* and subsequently reactivated). |
| `d_file_slots` | field | `file_slot_seq_type` | private | The sequence of all currently loaded files (includes those that have been conceptually deleted in the model - ie, deactivated in the model). |
| `d_free_file_handles` | field | `file_handles_seq_type` | private | A sequence of file handles that have been released and can be reused. |
| `d_file_indices` | field | `file_indices_seq_type` | private | The sequence of file indices. |
| `add_file_internal( const GPlatesFileIO::File::non_null_ptr_type &file)` | method | `file_handle_type` | private | — |
| `get_file` | field | `GPlatesFileIO::File::Reference` | private | — |
| `get_file_index( file_handle_type file_handle)` | method | `file_index_type` | private | — |
| `set_file_info( file_handle_type file_handle, const GPlatesFileIO::FileInfo &new_file_info, boost::optional<GPlatesFileIO::FeatureCollectionFileFormat::Configuration::shared_ptr_to_const_type> new_file_configuration)` | method | `void` | private | — |
| `deactivated_feature_collection( file_handle_type file_handle)` | method | `void` | private | — |
| `reactivated_feature_collection( file_handle_type file_handle)` | method | `void` | private | — |
| `destroying_feature_collection( file_handle_type file_handle)` | method | `void` | private | — |
| `FeatureCollectionUnloadCallback` | class | `None` | private | Keeps track of feature collections as they are deactivated and reactivated in the \*model\*. |

## Free functions and macros

| Name | Kind | Type / body | Description |
|---|---|---|---|
| `feature_collection_contains_feature( const GPlatesModel::FeatureCollectionHandle::weak_ref &feature_collection_ref, const GPlatesModel::FeatureHandle::weak_ref &feature_ref)` | function | `bool` | — |
| `GPLATES_APP_LOGIC_FEATURECOLLECTIONFILESTATE_H` | macro | `None` | — |
| `get_file_reference_containing_feature( GPlatesAppLogic::FeatureCollectionFileState &file_state_ref, GPlatesModel::FeatureHandle::weak_ref feature_ref)` | function | `boost::optional<GPlatesAppLogic::FeatureCollectionFileState::file_reference>` | — |

## Notes

**`remove_file` is not synchronous.** It removes the collection from the store root
and returns; the state change and every signal happen inside the model callback,
which a `GPlatesModel::NotificationGuard` further up the call stack can defer
arbitrarily. Do not assume `get_loaded_files()` has shrunk when `remove_file`
returns.

**Do not dereference the feature collection in
`file_state_file_about_to_be_removed`.** The header says so explicitly: the signal
also fires when a file add is undone, and in that case the collection is already
gone. If you need a post-removal hook, listen to `file_state_changed`, which
carries no file reference precisely because a valid one cannot be given.

**File handles are recycled, so a stale `FileReference` is dangerous.** Slots stay
occupied while a file is merely deactivated (undo can bring it back), but
`destroying_feature_collection` pushes the handle onto `d_free_file_handles` and
the next `add_file` reuses it. A `FileReference` kept across a genuine unload can
therefore silently start referring to a *different* file rather than failing.
Between deactivation and destruction the behaviour differs by accessor:
`get_file` and `set_file_info` assert `d_is_active_in_model` and throw
`AssertionFailureException`, while `get_file_index` does not check and returns the
stale index.

**Destruction can arrive without deactivation.** `destroying_feature_collection`
handles the case where `d_is_active_in_model` is still true by calling
`deactivated_feature_collection` itself, because a notification guard blocks
deactivation events but not impending-destruction events. The disabled assertion
left in an `#if 0` block records the assumption that used to hold. Any new code
reacting to these callbacks has to tolerate the same ordering.

**The destructor unloads everything, with signals.** It walks the slots and calls
`remove_file` on each still-active file, so listeners can be reached while the
object is being torn down. This is exactly why `ApplicationState`'s destructor
calls `QObject::disconnect` on it first.

**Never let the callback-carrying weak reference escape.**
`FileSlotExtra::d_callback_feature_collection` is a second weak ref to the same
collection, held privately, because a `WeakReference` copy also copies its
callback — handing it out would make the unload callback fire once per copy. The
public `File::get_feature_collection()` deliberately returns a different, unattached
weak ref.

**Costs are linear in loaded files, per operation.** Deactivate and reactivate
each walk the tail of `d_file_indices`; destroy erases from that vector and then
scans every slot; `get_loaded_files()` allocates a fresh vector and iterates all
slots including dead ones. The comments accept this for hundreds of files. Note
that `get_file_reference_containing_feature` calls `get_loaded_files()` and then
scans it, so resolving a feature to its file is O(N) with an allocation — do not
put it in a loop over features.

**Single-threaded.** A `QObject` driven by model callbacks and direct connections
on the GUI thread; none of the bookkeeping is synchronised.

**`emit_file_reloaded` is a pass-through, not a detector.** This class never
notices a reload itself; `FeatureCollectionFileIO` calls it after re-reading a
file, and `TotalReconstructionSequencesDialog` is the only listener in the tree.

## Used by

| Unit | Component | References |
|---|---|---|
| [gui/FileIOFeedback](../gui/FileIOFeedback.md) | gui | 96 |
| [qt-widgets/ManageFeatureCollectionsDialog](../qt-widgets/ManageFeatureCollectionsDialog.md) | qt-widgets | 79 |
| [qt-widgets/ManageFeatureCollectionsEditConfigurations](../qt-widgets/ManageFeatureCollectionsEditConfigurations.md) | qt-widgets | 59 |
| [app-logic/ReconstructGraphImpl](ReconstructGraphImpl.md) | app-logic | 54 |
| [app-logic/Layer](Layer.md) | app-logic | 48 |
| [app-logic/FeatureCollectionFileIO](FeatureCollectionFileIO.md) | app-logic | 37 |
| [qt-widgets/ChooseFeatureCollectionWidget](../qt-widgets/ChooseFeatureCollectionWidget.md) | qt-widgets | 37 |
| [app-logic/ReconstructGraph](ReconstructGraph.md) | app-logic | 34 |
| [qt-widgets/ScalarField3DLayerOptionsWidget](../qt-widgets/ScalarField3DLayerOptionsWidget.md) | qt-widgets | 31 |
| [app-logic/ApplicationState](ApplicationState.md) | app-logic | 29 |
| [gui/UnsavedChangesTracker](../gui/UnsavedChangesTracker.md) | gui | 28 |
| [qt-widgets/ColouringDialog](../qt-widgets/ColouringDialog.md) | qt-widgets | 27 |
| [qt-widgets/ChooseFeatureCollectionDialog](../qt-widgets/ChooseFeatureCollectionDialog.md) | qt-widgets | 26 |
| [qt-widgets/ShapefileAttributeViewerDialog](../qt-widgets/ShapefileAttributeViewerDialog.md) | qt-widgets | 21 |
| [qt-widgets/FeatureSummaryWidget](../qt-widgets/FeatureSummaryWidget.md) | qt-widgets | 20 |
| [qt-widgets/ManageFeatureCollectionsActionWidget](../qt-widgets/ManageFeatureCollectionsActionWidget.md) | qt-widgets | 20 |
| [qt-widgets/TotalReconstructionSequencesDialog](../qt-widgets/TotalReconstructionSequencesDialog.md) | qt-widgets | 18 |
| [qt-widgets/RasterLayerOptionsWidget](../qt-widgets/RasterLayerOptionsWidget.md) | qt-widgets | 17 |
| [app-logic/deprecated/PaleomagWorkflow](deprecated/PaleomagWorkflow.md) | app-logic | 16 |
| [app-logic/deprecated/PlateVelocityWorkflow](deprecated/PlateVelocityWorkflow.md) | app-logic | 16 |

*... and 46 more units.*

## Related

*None.*

## Explore

Run these from the `gplates-code` skill directory:

```bash
python scripts/gpq.py file src/app-logic/FeatureCollectionFileState.h
python scripts/gpq.py def GPlatesAppLogic::FeatureCollectionFileState --body
python scripts/gpq.py uses FeatureCollectionFileState --kind class
python scripts/gpq.py hier FeatureCollectionFileState
```
