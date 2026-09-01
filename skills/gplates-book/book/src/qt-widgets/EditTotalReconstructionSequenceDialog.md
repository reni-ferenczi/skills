# EditTotalReconstructionSequenceDialog

[Book TOC](../../TOC.md) · [qt-widgets](../../components/qt-widgets.md) · cluster Community 760 · tier 3

| Source file | Kind | Lines |
|---|---|---|
| `src/qt-widgets/EditTotalReconstructionSequenceDialog.h` | C++ | 130 |
| `src/qt-widgets/EditTotalReconstructionSequenceDialog.cc` | C++ | 202 |
| `src/qt-widgets/EditTotalReconstructionSequenceDialogUi.ui` | Qt form | 63 |

## Overview

A modal dialog for editing a single `TotalReconstructionSequence` feature. The dialog extracts the TRS data (irregular sampling time-rotation sequence, moving plate ID, fixed plate ID) from the feature using `TRSUtils`, initializes an `EditTotalReconstructionSequenceWidget` with this data, and presents it to the user. When the user clicks Apply, it validates the edited data, updates the parent `TotalReconstructionSequencesDialog` with the changes, and applies them to the feature. The Apply button is enabled or disabled based on whether the edited data is valid and whether changes have been made.

## Declared types

| Name | Kind | Bases | Template | Subclasses | Description |
|---|---|---|---|---|---|
| [`(anonymous)::TableUpdateGuard`](#anonymoustableupdateguard) | struct | `boost::noncopyable` | — | 0 | Borrowed from the TopologySectionsTable. |
| [`GPlatesQtWidgets::EditTotalReconstructionSequenceDialog`](#gplatesqtwidgetsedittotalreconstructionsequencedialog) | class | `QDialog`<br>`Ui_EditTotalReconstructionSequenceDialog` | — | 0 | This dialog displays, and allows editing of, the TotalReconstructionSequence trs\_feature. |

## Members

### `(anonymous)::TableUpdateGuard`

| Member | Kind | Type | Access | Description |
|---|---|---|---|---|
| `TableUpdateGuard( bool &guard_flag_ref)` | constructor | `None` | public | — |
| `~TableUpdateGuard()` | destructor | `None` | public | — |
| `d_guard_flag_ptr` | field | `bool` | public | — |

### `GPlatesQtWidgets::EditTotalReconstructionSequenceDialog`

| Member | Kind | Type | Access | Description |
|---|---|---|---|---|
| `EditTotalReconstructionSequenceDialog( GPlatesModel::FeatureHandle::weak_ref &trs_feature, GPlatesQtWidgets::TotalReconstructionSequencesDialog &trs_dialog, QWidget *parent = 0)` | constructor | `None` | public | — |
| `~EditTotalReconstructionSequenceDialog()` | destructor | `None` | public | — |
| `handle_apply()` | method | `void` | private | Handle the apply button being clicked. |
| `handle_cancel()` | method | `void` | private | Handle the cancel button being clicked. |
| `handle_table_validity_changed( bool)` | method | `void` | private | — |
| `handle_plate_ids_changed()` | method | `void` | private | — |
| `make_connections()` | method | `void` | private | — |
| `d_trs_feature` | field | `GPlatesModel::FeatureHandle::weak_ref` | private | The TRS feature which we will edit. |
| `d_trs_dialog` | field | `GPlatesQtWidgets::TotalReconstructionSequencesDialog` | private | The TRS dialog. |
| `d_edit_widget_ptr` | field | `boost::scoped_ptr<EditTotalReconstructionSequenceWidget>` | private | The widget for editing the TRS. |
| `d_irregular_sampling_property_iterator` | field | `boost::optional<GPlatesModel::FeatureHandle::iterator>` | private | The property iterators from d\_trs\_feature that refer to the properties we may want to edit. |
| `d_moving_ref_frame_iterator` | field | `boost::optional<GPlatesModel::FeatureHandle::iterator>` | private | — |
| `d_fixed_ref_frame_iterator` | field | `boost::optional<GPlatesModel::FeatureHandle::iterator>` | private | — |
| `d_irregular_sampling` | field | `boost::optional<GPlatesPropertyValues::GpmlIrregularSampling::non_null_ptr_type>` | private | A clone of the irregular sampling property. |
| `d_moving_plate_id` | field | `boost::optional<GPlatesModel::integer_plate_id_type>` | private | The moving plate id |
| `d_fixed_plate_id` | field | `boost::optional<GPlatesModel::integer_plate_id_type>` | private | The fixed plate id |

## Free functions and macros

| Name | Kind | Type / body | Description |
|---|---|---|---|
| `GPLATES_QTWIDGETS_EDITTOTALRECONSTRUCTIONSEQUENCEDIALOG_H` | macro | `None` | — |

## Notes

The dialog does not modify the feature directly. Instead, it collects edits and notifies the parent `TotalReconstructionSequencesDialog` via the Apply handler, which is responsible for updating the feature. The dialog's Apply button is disabled until valid edits have been made. The enclosed `TableUpdateGuard` is a utility class (borrowed from `TopologySectionsTable`) that suppresses table-change notifications during programmatic updates, allowing slot handlers to distinguish user edits from setup.

## Used by

| Unit | Component | References |
|---|---|---|
| [qt-widgets/TotalReconstructionSequencesDialog](TotalReconstructionSequencesDialog.md) | qt-widgets | 2 |

## Related

**Qt Designer forms**

| Form class | Base widget | Title | Widgets |
|---|---|---|---|
| `EditTotalReconstructionSequenceDialog` | `QDialog` | Edit Total Reconstruction Sequence | 3 |

**Qt signal/slot connections** (4 in this unit)

| Sender | Signal | Receiver | Slot |
|---|---|---|---|
| `buttonbox->button(QDialogButtonBox::Apply)` | `clicked()` | `this` | `handle_apply()` |
| `buttonbox->button(QDialogButtonBox::Cancel)` | `clicked()` | `this` | `handle_cancel()` |
| `d_edit_widget_ptr.get()` | `table_validity_changed(bool)` | `this` | `handle_table_validity_changed(bool)` |
| `d_edit_widget_ptr.get()` | `plate_ids_have_changed()` | `this` | `handle_plate_ids_changed()` |


## Explore

Run these from the `gplates-code` skill directory:

```bash
python scripts/gpq.py file src/qt-widgets/EditTotalReconstructionSequenceDialog.h
python scripts/gpq.py def GPlatesQtWidgets::EditTotalReconstructionSequenceDialog --body
python scripts/gpq.py uses EditTotalReconstructionSequenceDialog --kind class
python scripts/gpq.py hier EditTotalReconstructionSequenceDialog
```
