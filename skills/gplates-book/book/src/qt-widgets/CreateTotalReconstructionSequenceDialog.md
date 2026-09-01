# CreateTotalReconstructionSequenceDialog

[Book TOC](../../TOC.md) · [qt-widgets](../../components/qt-widgets.md) · cluster Community 244 · tier 3

| Source file | Kind | Lines |
|---|---|---|
| `src/qt-widgets/CreateTotalReconstructionSequenceDialog.h` | C++ | 163 |
| `src/qt-widgets/CreateTotalReconstructionSequenceDialog.cc` | C++ | 271 |
| `src/qt-widgets/CreateTotalReconstructionSequenceDialogUi.ui` | Qt form | 79 |

## Overview

A multi-page wizard dialog for creating new TotalReconstructionSequence features. Orchestrates a TRS editing page and a feature collection selection page, managing the edited TRS properties and choice of target collection. On creation, returns the new `FeatureHandle` weak reference for the created feature. Also provides `TableUpdateGuard`, an RAII guard for suppressing table updates during batch modifications.

## Declared types

| Name | Kind | Bases | Template | Subclasses | Description |
|---|---|---|---|---|---|
| [`(anonymous)::TableUpdateGuard`](#anonymoustableupdateguard) | struct | `boost::noncopyable` | — | 0 | Borrowed from the TopologySectionsTable. |
| [`GPlatesQtWidgets::CreateTotalReconstructionSequenceDialog`](#gplatesqtwidgetscreatetotalreconstructionsequencedialog) | class | `QDialog`<br>`Ui_CreateTotalReconstructionSequenceDialog` | — | 0 | This dialog displays, and allows editing of, the TotalReconstructionSequence trs\_feature. |

## Members

### `(anonymous)::TableUpdateGuard`

| Member | Kind | Type | Access | Description |
|---|---|---|---|---|
| `TableUpdateGuard( bool &guard_flag_ref)` | constructor | `None` | public | — |
| `~TableUpdateGuard()` | destructor | `None` | public | — |
| `d_guard_flag_ptr` | field | `bool` | public | — |

### `GPlatesQtWidgets::CreateTotalReconstructionSequenceDialog`

| Member | Kind | Type | Access | Description |
|---|---|---|---|---|
| `StackedWidgetPage` | enum | `None` | public | — |
| `CreateTotalReconstructionSequenceDialog( GPlatesQtWidgets::TotalReconstructionSequencesDialog &trs_dialog, GPlatesAppLogic::ApplicationState &app_state, QWidget *parent = 0)` | constructor | `None` | public | — |
| `init()` | method | `void` | public | — |
| `~CreateTotalReconstructionSequenceDialog()` | destructor | `None` | public | — |
| `created_feature()` | method | `boost::optional<GPlatesModel::FeatureHandle::weak_ref>` | public | — |
| `handle_create()` | method | `void` | private | Handle the create button being clicked. |
| `handle_cancel()` | method | `void` | private | Handle the cancel button being clicked. |
| `handle_table_validity_changed( bool)` | method | `void` | private | — |
| `handle_previous()` | method | `void` | private | — |
| `handle_next()` | method | `void` | private | — |
| `make_connections()` | method | `void` | private | — |
| `setup_pages()` | method | `void` | private | — |
| `make_trs_page_current()` | method | `void` | private | — |
| `make_feature_collection_page_current()` | method | `void` | private | — |
| `d_trs_dialog` | field | `GPlatesQtWidgets::TotalReconstructionSequencesDialog` | private | The TRS dialog. |
| `d_edit_widget_ptr` | field | `boost::scoped_ptr<EditTotalReconstructionSequenceWidget>` | private | The widget for editing the TRS. |
| `d_choose_feature_collection_widget_ptr` | field | `GPlatesQtWidgets::ChooseFeatureCollectionWidget` | private | The widget for choosing the feature collection. |
| `d_irregular_sampling` | field | `boost::optional<GPlatesPropertyValues::GpmlIrregularSampling::non_null_ptr_type>` | private | The irregular sampling property. |
| `d_moving_plate_id` | field | `boost::optional<GPlatesModel::integer_plate_id_type>` | private | The moving plate id. |
| `d_fixed_plate_id` | field | `boost::optional<GPlatesModel::integer_plate_id_type>` | private | The fixed plate id. |
| `d_app_state` | field | `GPlatesAppLogic::ApplicationState` | private | The app state, for getting the feature collections. |
| `d_trs_feature` | field | `boost::optional<GPlatesModel::FeatureHandle::weak_ref>` | private | The created TRS feature. |

## Free functions and macros

| Name | Kind | Type / body | Description |
|---|---|---|---|
| `new_feature_collection_string` | variable | `QString` | — |
| `GPLATES_QTWIDGETS_CREATETOTALRECONSTRUCTIONSEQUENCEDIALOG_H` | macro | `None` | — |

## Notes

*None.*

## Used by

| Unit | Component | References |
|---|---|---|
| [qt-widgets/TotalReconstructionSequencesDialog](TotalReconstructionSequencesDialog.md) | qt-widgets | 8 |

## Related

**Qt Designer forms**

| Form class | Base widget | Title | Widgets |
|---|---|---|---|
| `CreateTotalReconstructionSequenceDialog` | `QDialog` | Create Total Reconstruction Sequence | 8 |

**Qt signal/slot connections** (5 in this unit)

| Sender | Signal | Receiver | Slot |
|---|---|---|---|
| `button_create` | `clicked()` | `this` | `handle_create()` |
| `button_cancel` | `clicked()` | `this` | `handle_cancel()` |
| `d_edit_widget_ptr.get()` | `table_validity_changed(bool)` | `this` | `handle_table_validity_changed(bool)` |
| `button_previous` | `clicked()` | `this` | `handle_previous()` |
| `button_next` | `clicked()` | `this` | `handle_next()` |


## Explore

Run these from the `gplates-code` skill directory:

```bash
python scripts/gpq.py file src/qt-widgets/CreateTotalReconstructionSequenceDialog.h
python scripts/gpq.py def GPlatesQtWidgets::CreateTotalReconstructionSequenceDialog --body
python scripts/gpq.py uses CreateTotalReconstructionSequenceDialog --kind class
python scripts/gpq.py hier CreateTotalReconstructionSequenceDialog
```
