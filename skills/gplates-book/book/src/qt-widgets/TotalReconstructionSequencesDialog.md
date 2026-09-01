# TotalReconstructionSequencesDialog

[Book TOC](../../TOC.md) · [qt-widgets](../../components/qt-widgets.md) · cluster Community 195 · tier 2

| Source file | Kind | Lines |
|---|---|---|
| `src/qt-widgets/TotalReconstructionSequencesDialog.h` | C++ | 354 |
| `src/qt-widgets/TotalReconstructionSequencesDialog.cc` | C++ | 2007 |
| `src/qt-widgets/TotalReconstructionSequencesDialogUi.ui` | Qt form | 483 |

## Overview

`TotalReconstructionSequencesDialog` is the "Total Reconstruction Sequences"
dialog, a `QTreeWidget`-based editor over the loaded `.rot` rotation files: it
lists File → `TotalReconstructionSequence` → `TotalReconstructionPole` as a
three-level tree and lets a user filter by plate ID, edit, create or delete
sequences, and enable/disable individual poles. Edits made through
`CreateTotalReconstructionSequenceDialog` and `EditTotalReconstructionSequenceDialog`
are written back through `GPlatesFileIO::PlatesRotationFileProxy`, which keeps
each rotation file's original text-level formatting and comment metadata so
that unrelated parts of the file are not rewritten when one pole changes.

`TotalReconstructionSequencesSearchIndex` mirrors the tree's structure outside
the `QTreeWidget` so that plate-ID filtering (`apply_filter()`/`reset_filter()`)
can walk File/Sequence/Pole objects and hide or show the corresponding
`QTreeWidgetItem`s without querying Qt's model each time; `PlateIdFilteringPredicate`
is the Interpreter-style predicate the two anonymous subclasses implement, one
that accepts every plate ID and one that accepts a single plate ID typed into
the filter box. Because the search index holds raw `QTreeWidgetItem*` pointers
into a tree that `update()` clears and rebuilds on every file load/unload, the
dialog keeps the two in lockstep manually rather than relying on Qt's
model/view machinery.

## Declared types

| Name | Kind | Bases | Template | Subclasses | Description |
|---|---|---|---|---|---|
| [`(anonymous)::ColumnNames`](#anonymouscolumnnames) | class | — | — | 0 | — |
| [`UserItemTypes::UserItemType`](#useritemtypesuseritemtype) | enum | — | — | 0 | A type to describe what sort of data the QTreeWidgetItem represents - file, sequence, or pole. |
| [`(anonymous)::AllowAnyPlateIdFilteringPredicate`](#anonymousallowanyplateidfilteringpredicate) | class | [`GPlatesQtWidgets::PlateIdFilteringPredicate`](TotalReconstructionSequencesDialog.md) | — | 0 | — |
| [`(anonymous)::AllowSinglePlateIdFilteringPredicate`](#anonymousallowsingleplateidfilteringpredicate) | class | [`GPlatesQtWidgets::PlateIdFilteringPredicate`](TotalReconstructionSequencesDialog.md) | — | 0 | — |
| [`GPlatesQtWidgets::TotalReconstructionSequencesSearchIndex`](#gplatesqtwidgetstotalreconstructionsequencessearchindex) | class | — | — | 0 | This class contains a search index for the Total Reconstruction Sequences contained in the TotalReconstructionSequenceDialog. |
| [`GPlatesQtWidgets::PlateIdFilteringPredicate`](#gplatesqtwidgetsplateidfilteringpredicate) | class | — | — | 2 | A predicate to filter by plate ID. |
| [`GPlatesQtWidgets::tree_item_to_feature_map_type`](#gplatesqtwidgetstree_item_to_feature_map_type) | typedef | — | — | 0 | — |
| [`GPlatesQtWidgets::tree_item_to_feature_collection_map_type`](#gplatesqtwidgetstree_item_to_feature_collection_map_type) | typedef | — | — | 0 | — |
| [`GPlatesQtWidgets::TotalReconstructionSequencesDialog`](#gplatesqtwidgetstotalreconstructionsequencesdialog) | class | [`GPlatesDialog`](GPlatesDialog.md)<br>`Ui_TotalReconstructionSequencesDialog` | — | 0 | — |

## Members

### `(anonymous)::ColumnNames`

| Member | Kind | Type | Access | Description |
|---|---|---|---|---|
| `ColumnName` | enum | `None` | public | — |
| `ColumnNames()` | constructor | `None` | public | — |
| `get_index( const QString& id)` | method | `ColumnName` | public | — |
| `get_id( ColumnName idx)` | method | `QString` | public | — |
| `get_ids()` | method | `std::vector<QString>` | public | — |
| `get_name( ColumnName idx)` | method | `QString` | public | — |
| `add( const QString& id, const QString& name, ColumnName index)` | method | `void` | protected | — |
| `ColumnNameMap` | typedef | `std::map<QString, ColumnName>` | protected | — |
| `d_id_index_map` | field | `ColumnNameMap` | protected | — |
| `d_id_vec` | field | `std::vector<QString>` | protected | — |
| `d_name_vec` | field | `std::vector<QString>` | protected | — |

### `UserItemTypes::UserItemType`

| Member | Kind | Type | Access | Description |
|---|---|---|---|---|
| `FILE_ITEM_TYPE` | enumerator | `None` | — | — |
| `SEQUENCE_ITEM_TYPE` | enumerator | `None` | — | — |
| `POLE_ITEM_TYPE` | enumerator | `None` | — | — |

### `(anonymous)::AllowAnyPlateIdFilteringPredicate`

| Member | Kind | Type | Access | Description |
|---|---|---|---|---|
| `AllowAnyPlateIdFilteringPredicate()` | constructor | `None` | public | — |
| `allow_plate_id( GPlatesModel::integer_plate_id_type plate_id)` | method | `bool` | public | — |

### `(anonymous)::AllowSinglePlateIdFilteringPredicate`

| Member | Kind | Type | Access | Description |
|---|---|---|---|---|
| `AllowSinglePlateIdFilteringPredicate( GPlatesModel::integer_plate_id_type plate_id_to_allow)` | constructor | `None` | public | — |
| `allow_plate_id( GPlatesModel::integer_plate_id_type plate_id)` | method | `bool` | public | — |
| `d_plate_id_to_allow` | field | `GPlatesModel::integer_plate_id_type` | private | — |

### `GPlatesQtWidgets::TotalReconstructionSequencesSearchIndex`

| Member | Kind | Type | Access | Description |
|---|---|---|---|---|
| `TotalReconstructionPole` | struct | `None` | public | — |
| `TotalReconstructionSequence` | struct | `None` | public | — |
| `File` | struct | `None` | public | — |
| `file_sequence_type` | typedef | `std::vector<boost::shared_ptr<File> >` | public | — |
| `append_new_file( const QString &filename, QTreeWidgetItem *item)` | method | `File` | public | — |
| `apply_filter( const boost::shared_ptr<PlateIdFilteringPredicate> &predicate)` | method | `void` | public | — |
| `reset_filter()` | method | `void` | public | — |
| `clear()` | method | `void` | public | — |
| `apply_filter_recursively( const boost::shared_ptr<PlateIdFilteringPredicate> &predicate)` | method | `void` | protected | — |
| `show_all_recursively()` | method | `void` | protected | — |
| `d_filtering_predicate_ptr` | field | `boost::shared_ptr<PlateIdFilteringPredicate>` | private | The predicate used to filter by plate ID. |
| `d_files` | field | `file_sequence_type` | private | — |

### `GPlatesQtWidgets::PlateIdFilteringPredicate`

| Member | Kind | Type | Access | Description |
|---|---|---|---|---|
| `~PlateIdFilteringPredicate()` | destructor | `None` | public | — |
| `allow_plate_id( GPlatesModel::integer_plate_id_type plate_id)` | method | `bool` | public | — |

### `GPlatesQtWidgets::tree_item_to_feature_map_type`

*None.*

### `GPlatesQtWidgets::tree_item_to_feature_collection_map_type`

*None.*

### `GPlatesQtWidgets::TotalReconstructionSequencesDialog`

| Member | Kind | Type | Access | Description |
|---|---|---|---|---|
| `TotalReconstructionSequencesDialog( GPlatesAppLogic::FeatureCollectionFileState &file_state, GPlatesPresentation::ViewState &view_state, QWidget *parent_ = NULL)` | constructor | `None` | public | — |
| `~TotalReconstructionSequencesDialog()` | destructor | `None` | public | — |
| `update()` | method | `void` | public | Update the dialog (after a file has been loaded or unloaded, for example). |
| `apply_filter()` | method | `void` | public | Respond to the "Apply Filter" button. |
| `reset_filter()` | method | `void` | public | Respond to the "Reset Filter" button. |
| `handle_current_item_changed( QTreeWidgetItem *current, QTreeWidgetItem *previous)` | method | `void` | public | React when the "current item" of the QTreeWidget has changed. |
| `edit_sequence()` | method | `void` | public | Respond to the "Edit Sequence" button. |
| `create_new_sequence()` | method | `void` | public | Respond to the "New Sequence" button. |
| `delete_sequence()` | method | `void` | public | Respond to the "Delete Sequence" button. |
| `show_metadata()` | method | `void` | public | — |
| `disable_enable_pole()` | method | `void` | public | — |
| `disable_sequence()` | method | `void` | public | — |
| `enable_sequence()` | method | `void` | public | — |
| `update_edited_feature()` | method | `void` | public | Update the tree after a TRS feature has been edited. |
| `handle_feature_collection_file_state_changed()` | method | `void` | public | Listen for changes in the file state so that we can update the tree. |
| `handle_file_reloaded()` | method | `void` | public | — |
| `update_current_sequence( GPlatesModel::TopLevelProperty::non_null_ptr_type moving_plate_id, GPlatesModel::TopLevelProperty::non_null_ptr_type fix_plate_id, GPlatesModel::TopLevelProperty::non_null_ptr_type trs)` | method | `void` | public | This function should only be used to update pole data from EditTotalReconstructionSequenceDialog. |
| `has_metadata( GPlatesModel::FeatureCollectionHandle::weak_ref)` | method | `bool` | public | — |
| `get_current_feature()` | method | `GPlatesModel::FeatureHandle::weak_ref` | public | — |
| `insert_feature_to_proxy( GPlatesModel::FeatureHandle::weak_ref, GPlatesFileIO::File::Reference&)` | method | `void` | public | Insert the feature into rotation file proxy. |
| `is_seq_disabled( GPlatesModel::FeatureHandle::weak_ref)` | method | `bool` | public | — |
| `set_seq_disabled( GPlatesModel::FeatureHandle::weak_ref, bool flag)` | method | `void` | public | — |
| `parse_plate_id_filtering_text()` | method | `boost::shared_ptr<PlateIdFilteringPredicate>` | protected | — |
| `get_current_file_ref` | field | `GPlatesFileIO::File::Reference` | protected | — |
| `get_current_rotation_file_proxy()` | method | `GPlatesFileIO::PlatesRotationFileProxy` | protected | — |
| `get_rotation_file_proxy( GPlatesFileIO::File::Reference&)` | method | `GPlatesFileIO::PlatesRotationFileProxy` | protected | — |
| `remove_feature_from_proxy( GPlatesModel::FeatureHandle::weak_ref, bool keep_mprs_header = false)` | method | `void` | protected | Remove the feature from rotation file proxy. |
| `insert_feature_to_proxy( GPlatesModel::FeatureHandle::weak_ref)` | method | `void` | protected | Insert the feature into rotation file proxy. |
| `insert_feature_to_proxy( GPlatesModel::FeatureHandle::weak_ref, GPlatesFileIO::PlatesRotationFileProxy&)` | method | `void` | protected | — |
| `get_pole_data_from_feature( GPlatesModel::FeatureHandle::weak_ref)` | method | `std::vector<GPlatesFileIO::RotationPoleData>` | protected | — |
| `get_current_fc_metadata()` | method | `GPlatesModel::FeatureCollectionMetadata` | protected | — |
| `get_current_metadata_property()` | method | `GPlatesModel::FeatureHandle::iterator` | protected | — |
| `get_file_ref( GPlatesModel::FeatureCollectionHandle *)` | method | `boost::tuple< bool, GPlatesFileIO::File::Reference*>` | protected | — |
| `d_file_state_ptr` | field | `GPlatesAppLogic::FeatureCollectionFileState` | private | The loaded feature collection files. |
| `d_search_index_ptr` | field | `boost::shared_ptr<TotalReconstructionSequencesSearchIndex>` | private | The search index used to search by plate ID and text-in-comment. |
| `d_tree_item_to_feature_map` | field | `tree_item_to_feature_map_type` | private | A map of tree item to model property, so that we can edit the appropriate part of the model when we select a TRS tree item. |
| `d_current_item` | field | `QTreeWidgetItem` | private | The currently selected item in the tree. |
| `d_current_trs_was_expanded` | field | `bool` | private | Whether or not the current item in the tree was expanded. |
| `d_app_state` | field | `GPlatesAppLogic::ApplicationState` | private | — |
| `make_signal_slot_connections()` | method | `void` | private | Initialise the signal-slot connections in the constructor. |
| `connect_to_file_state_signals()` | method | `void` | private | Connect to signals from a FeatureCollectionFileState object. |
| `d_create_trs_dialog_ptr` | field | `boost::scoped_ptr<CreateTotalReconstructionSequenceDialog>` | private | The create\_trs dialog. |
| `d_edit_trs_dialog_ptr` | field | `boost::scoped_ptr<EditTotalReconstructionSequenceDialog>` | private | The edit\_trs dialog. |
| `d_metadata_dlg` | field | `MetadataDialog` | private | No need to use boost::scoped\_ptr. |

## Free functions and macros

| Name | Kind | Type / body | Description |
|---|---|---|---|
| `column_names` | variable | `ColumnNames` | — |
| `totalReconstructionPole_prop_name()` | function | `GPlatesModel::PropertyName` | — |
| `set_cell_background_to_show_error( QTreeWidgetItem *item, int which_column)` | function | `void` | — |
| `set_colspan_background_to_show_disabled_seq( QTreeWidgetItem *item)` | function | `void` | — |
| `set_row_background_to_show_disabled_pole( QTreeWidgetItem *item)` | function | `void` | — |
| `fill_tree_widget_pole_time_instant( QTreeWidgetItem *item, const GPlatesPropertyValues::GeoTimeInstant &gti, const QLocale &locale_)` | function | `void` | — |
| `fill_tree_widget_pole_finite_rotation( QTreeWidgetItem *item, const GPlatesPropertyValues::GpmlFiniteRotation &finite_rotation, const QLocale &locale_)` | function | `void` | — |
| `fill_tree_widget_pole_sample_value( QTreeWidgetItem *item, const GPlatesModel::PropertyValue::non_null_ptr_to_const_type &time_sample_value, const QLocale &locale_)` | function | `void` | — |
| `fill_tree_widget_items_for_poles( QTreeWidgetItem *parent_item_for_sequence, const GPlatesModel::FeatureHandle::weak_ref &feature_ref, GPlatesQtWidgets::TotalReconstructionSequencesSearchIndex::TotalReconstructionSequence * sequence)` | function | `void` | — |
| `fill_tree_widget_items_for_features( QTreeWidgetItem *parent_item_for_filename, const GPlatesModel::FeatureCollectionHandle::weak_ref &fc, GPlatesQtWidgets::TotalReconstructionSequencesSearchIndex::File *file, GPlatesQtWidgets::tree_item_to_feature_map_type &tree_item_to_feature_map)` | function | `void` | — |
| `reverse_lookup( const GPlatesQtWidgets::tree_item_to_feature_map_type &tree_item_to_feature_map, const GPlatesModel::FeatureHandle::weak_ref &feature_weak_ref)` | function | `GPlatesQtWidgets::tree_item_to_feature_map_type::const_iterator` | A reverse look up in the tree\_item\_to\_feature\_map. |
| `GPLATES_QTWIDGETS_TOTALRECONSTRUCTIONSEQUENCESDIALOG_H` | macro | `None` | — |

## Notes

`TotalReconstructionSequencesSearchIndex`'s `File`/`TotalReconstructionSequence`/
`TotalReconstructionPole` entries hold raw pointers to `QTreeWidgetItem`s owned
by the tree widget; any code that clears or rebuilds `treewidget_seqs` (chiefly
`update()`) must rebuild the search index in the same pass or those pointers
dangle. `d_current_item` and `d_current_trs_was_expanded` exist purely to
restore the tree's selection and expansion state across an `update()` rebuild,
since the rebuild replaces every item. `connect_to_file_state_signals()` is
declared but marked `FIXME: Define this function` in its header comment, so
verify it is actually implemented before relying on it.

## Used by

| Unit | Component | References |
|---|---|---|
| [qt-widgets/EditWidgetGroupBox](EditWidgetGroupBox.md) | qt-widgets | 40 |
| [qt-widgets/ScalarField3DLayerOptionsWidget](ScalarField3DLayerOptionsWidget.md) | qt-widgets | 34 |
| [qt-widgets/MetadataDialog](MetadataDialog.md) | qt-widgets | 13 |
| [qt-widgets/EditAgeWidget](EditAgeWidget.md) | qt-widgets | 7 |
| [qt-widgets/ColouringDialog](ColouringDialog.md) | qt-widgets | 5 |
| [qt-widgets/TopologyToolsWidget](TopologyToolsWidget.md) | qt-widgets | 5 |
| [qt-widgets/ManageFeatureCollectionsDialog](ManageFeatureCollectionsDialog.md) | qt-widgets | 4 |
| [qt-widgets/ReconstructLayerOptionsWidget](ReconstructLayerOptionsWidget.md) | qt-widgets | 4 |
| [qt-widgets/ViewportWindow](ViewportWindow.md) | qt-widgets | 4 |
| [qt-widgets/EditTotalReconstructionSequenceDialog](EditTotalReconstructionSequenceDialog.md) | qt-widgets | 3 |
| [qt-widgets/GpgimVersionWarningDialog](GpgimVersionWarningDialog.md) | qt-widgets | 3 |
| [qt-widgets/HellingerDialog](HellingerDialog.md) | qt-widgets | 3 |
| [qt-widgets/MeasureDistanceWidget](MeasureDistanceWidget.md) | qt-widgets | 3 |
| [qt-widgets/TopologyNetworkResolverLayerOptionsWidget](TopologyNetworkResolverLayerOptionsWidget.md) | qt-widgets | 3 |
| [qt-widgets/VisualLayerWidget](VisualLayerWidget.md) | qt-widgets | 3 |
| [file-io/GeoscimlProfile](../file-io/GeoscimlProfile.md) | file-io | 2 |
| [qt-widgets/ChangeFeatureTypeDialog](ChangeFeatureTypeDialog.md) | qt-widgets | 2 |
| [qt-widgets/CreateTotalReconstructionSequenceDialog](CreateTotalReconstructionSequenceDialog.md) | qt-widgets | 2 |
| [qt-widgets/DrawStyleDialog](DrawStyleDialog.md) | qt-widgets | 2 |
| [qt-widgets/EditAffineTransformGeoreferencingWidget](EditAffineTransformGeoreferencingWidget.md) | qt-widgets | 2 |

*... and 25 more units.*

## Related

**Qt Designer forms**

| Form class | Base widget | Title | Widgets |
|---|---|---|---|
| `TotalReconstructionSequencesDialog` | `QDialog` | Total Reconstruction Sequences | 25 |

**Qt signal/slot connections** (12 in this unit)

| Sender | Signal | Receiver | Slot |
|---|---|---|---|
| `button_Apply_Filter` | `clicked()` | `this` | `apply_filter()` |
| `button_Reset_Filter` | `clicked()` | `this` | `reset_filter()` |
| `button_Edit_Sequence` | `clicked()` | `this` | `edit_sequence()` |
| `button_New_Sequence` | `clicked()` | `this` | `create_new_sequence()` |
| `button_Delete_Sequence` | `clicked()` | `this` | `delete_sequence()` |
| `show_metadata_button` | `clicked()` | `this` | `show_metadata()` |
| `lineedit_Filter_by_Plate_ID` | `returnPressed()` | `this` | `apply_filter()` |
| `treewidget_seqs` | `currentItemChanged(QTreeWidgetItem *, QTreeWidgetItem *)` | `this` | `handle_current_item_changed(QTreeWidgetItem *, QTreeWidgetItem *)` |
| `&(d_app_state.get_feature_collection_file_state())` | `file_state_changed(GPlatesAppLogic::FeatureCollectionFileState &)` | `this` | `handle_feature_collection_file_state_changed()` |
| `&(d_app_state.get_feature_collection_file_state())` | `file_reloaded(GPlatesAppLogic::FeatureCollectionFileState &)` | `this` | `handle_file_reloaded()` |
| `disable_seq_button` | `clicked()` | `this` | `disable_sequence()` |
| `enable_seq_button` | `clicked()` | `this` | `enable_sequence()` |


## Explore

Run these from the `gplates-code` skill directory:

```bash
python scripts/gpq.py file src/qt-widgets/TotalReconstructionSequencesDialog.h
python scripts/gpq.py def GPlatesQtWidgets::TotalReconstructionSequencesDialog --body
python scripts/gpq.py uses TotalReconstructionSequencesDialog --kind class
python scripts/gpq.py hier TotalReconstructionSequencesDialog
```
