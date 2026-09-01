# ExportAnimationDialog

[Book TOC](../../TOC.md) · [qt-widgets](../../components/qt-widgets.md) · cluster Community 333 · tier 2

| Source file | Kind | Lines |
|---|---|---|
| `src/qt-widgets/ExportAnimationDialog.h` | C++ | 306 |
| `src/qt-widgets/ExportAnimationDialog.cc` | C++ | 808 |
| `src/qt-widgets/ExportAnimationDialogUi.ui` | Qt form | 930 |

## Overview

`ExportAnimationDialog` is the dialog users configure animation and single-frame exports from. It maintains two independent `QTableWidget`s of queued exports — `tableWidget_range` for animation-sequence exports and `tableWidget_single` for one-off snapshots — switched between via `stackedWidget` and tracked by `d_is_single_frame`; each row's export type, format and configuration are stashed as custom `QTableWidgetItem` subclasses (from `ConfigureExportParametersDialog`) and read back out by the free functions `get_export_id()` and `get_export_configuration()`. Adding or editing a row is a two-step handoff: `react_add_export_clicked()`/`react_edit_export_clicked()` pop up the modal `ConfigureExportParametersDialog` or `EditExportParametersDialog`, which then calls back into `insert_item()` or `edit_item()` once the user finishes choosing a type, format and configuration.

The dialog itself does no exporting; it hands the queued export strategies to `d_export_animation_context_ptr`, a `GPlatesGui::ExportAnimationContext` that plays the Context role of the Strategy pattern and does the actual work, sharing time-range state with the wider application through `d_animation_controller_ptr` (an `AnimationController` also driven by `AnimateDialog` and `AnimateControlWidget`). `set_export_parameters()` computes the `AnimationSequence::SequenceInfo` to export — either the single snapshot time repeated once, or the controller's configured range — and must run before `add_export_animation_strategy()` is called for each queued row, since each strategy initialises its `ExportTemplateFilenameSequence` from that range.

## Declared types

| Name | Kind | Bases | Template | Subclasses | Description |
|---|---|---|---|---|---|
| [`GPlatesQtWidgets::ExportAnimationDialog`](#gplatesqtwidgetsexportanimationdialog) | class | [`GPlatesDialog`](GPlatesDialog.md)<br>`Ui_ExportAnimationDialog` | — | 0 | — |

## Members

### `GPlatesQtWidgets::ExportAnimationDialog`

| Member | Kind | Type | Access | Description |
|---|---|---|---|---|
| `ExportAnimationDialog( GPlatesPresentation::ViewState &view_state_, GPlatesQtWidgets::ViewportWindow &viewport_window_, QWidget *parent_ = NULL)` | constructor | `None` | public | — |
| `~ExportAnimationDialog()` | destructor | `None` | public | — |
| `view_time` | field | `double` | public | — |
| `insert_item( GPlatesGui::ExportAnimationType::Type export_type, GPlatesGui::ExportAnimationType::Format export_format, const GPlatesGui::ExportAnimationStrategy::const_configuration_base_ptr &export_configuration)` | method | `void` | public | Adds a new export of the specified type, format and configuration. |
| `edit_item( int export_row, const GPlatesGui::ExportAnimationStrategy::const_configuration_base_ptr &export_configuration)` | method | `void` | public | Changes the export configuration for the selected export row. |
| `reset()` | method | `void` | public | Reset controls to their "Eagerly awaiting user input" state. |
| `update_progress_bar( std::size_t length, std::size_t frame)` | method | `void` | public | — |
| `update_single_frame_progress_bar( std::size_t val, std::size_t range)` | method | `void` | public | — |
| `update_status_message( QString message, bool is_error_msg = false)` | method | `void` | public | — |
| `set_start_time_value_to_view_time()` | method | `void` | public | — |
| `set_end_time_value_to_view_time()` | method | `void` | public | — |
| `setVisible( bool visible)` | method | `void` | public | We need to reimplement setVisible() because reimplementing closeEvent() is not enough - the default buttonbox "Close" button only appears to hide the dialog. |
| `current_time_changed( double new_value)` | method | `void` | public | — |
| `react_start_time_spinbox_changed( double new_val)` | method | `void` | private | — |
| `react_end_time_spinbox_changed( double new_val)` | method | `void` | private | — |
| `react_time_increment_spinbox_changed( double new_val)` | method | `void` | private | — |
| `handle_start_time_changed( double new_val)` | method | `void` | private | — |
| `handle_end_time_changed( double new_val)` | method | `void` | private | — |
| `handle_time_increment_changed( double new_val)` | method | `void` | private | — |
| `set_path()` | method | `void` | private | — |
| `select_single_snapshot( bool checked)` | method | `void` | private | — |
| `select_range_snapshot( bool checked)` | method | `void` | private | — |
| `set_snapshot_time_to_view_time()` | method | `void` | private | — |
| `handle_options_changed()` | method | `void` | private | (Re)sets checkboxes according to animation controller state. |
| `react_export_button_clicked()` | method | `void` | private | — |
| `react_abort_button_clicked()` | method | `void` | private | — |
| `react_add_export_clicked()` | method | `void` | private | — |
| `react_choose_target_directory_clicked()` | method | `void` | private | — |
| `react_remove_export_clicked()` | method | `void` | private | — |
| `react_edit_export_clicked()` | method | `void` | private | — |
| `handle_export_selection_changed()` | method | `void` | private | — |
| `d_export_animation_context_ptr` | field | `GPlatesGui::ExportAnimationContext::non_null_ptr_type` | private | The ExportAnimationContext is the Context role of the Strategy pattern in Gamma et al p315. |
| `d_animation_controller_ptr` | field | `GPlatesGui::AnimationController` | private | This is the animation controller, which holds the state of any animation set up in the application. |
| `d_configure_parameters_dialog_ptr` | field | `GPlatesQtWidgets::ConfigureExportParametersDialog` | private | We have a miniature sub-dialog, which is modal, for configuring parameters. |
| `d_edit_parameters_dialog_ptr` | field | `GPlatesQtWidgets::EditExportParametersDialog` | private | We have a miniature sub-dialog, which is modal, for edit parameters for the selected export. |
| `d_open_directory_dialog` | field | `OpenDirectoryDialog` | private | — |
| `d_is_single_frame` | field | `bool` | private | flag used to indicate which stack widget is currently using |
| `d_single_path` | field | `QString` | private | the output path for single snapshot |
| `d_range_path` | field | `QString` | private | the output path for a range of snapshots |
| `set_export_abort_button_state( bool we_are_exporting)` | method | `void` | private | Updates button label & icon. |
| `recalculate_progress_bar()` | method | `void` | private | Recalculates the range of the progress bar to be displayed BEFORE we export. |
| `update_target_directory( const QString &new_target)` | method | `bool` | private | — |
| `set_export_parameters()` | method | `void` | private | — |

## Free functions and macros

| Name | Kind | Type / body | Description |
|---|---|---|---|
| `get_export_id( QTableWidget *table_widget, int row)` | function | `GPlatesGui::ExportAnimationType::ExportID` | Returns the export ID associated with the specified row in the table widget. |
| `get_export_configuration( QTableWidget *table_widget, int row)` | function | `GPlatesGui::ExportAnimationStrategy::const_configuration_base_ptr` | Returns the export configuration associated with the specified row in the table widget. |
| `GPLATES_QTWIDGETS_EXPORTANIMATIONDIALOG_H` | macro | `None` | — |

## Notes

`d_configure_parameters_dialog_ptr` and `d_edit_parameters_dialog_ptr` are raw pointers but are Qt-parented to this dialog, so their lifetime is managed by Qt rather than by explicit deletion here. `setVisible()` is overridden because the buttonbox "Close" button only hides the dialog rather than closing it; hiding it while `d_export_animation_context_ptr->is_running()` is treated as an implicit cancel and triggers `react_abort_button_clicked()` before the base-class hide, so closing the dialog mid-export always aborts the export rather than leaving it running headless. `react_export_button_clicked()` refuses to proceed if the active table has zero rows or the target directory fails `update_target_directory()`, and it always restores the export/abort button state afterwards even though nothing currently catches an exception thrown mid-export.

## Used by

| Unit | Component | References |
|---|---|---|
| [gui/ExportAnimationContext](../gui/ExportAnimationContext.md) | gui | 6 |
| [qt-widgets/ConfigureExportParametersDialog](ConfigureExportParametersDialog.md) | qt-widgets | 6 |
| [qt-widgets/EditExportParametersDialog](EditExportParametersDialog.md) | qt-widgets | 5 |
| [gui/Dialogs](../gui/Dialogs.md) | gui | 2 |

## Related

**Qt Designer forms**

| Form class | Base widget | Title | Widgets |
|---|---|---|---|
| `ExportAnimationDialog` | `QDialog` | Export | 54 |

**Qt signal/slot connections** (29 in this unit)

| Sender | Signal | Receiver | Slot |
|---|---|---|---|
| `button_Use_View_Time_start_time` | `clicked()` | `this` | `set_start_time_value_to_view_time()` |
| `button_Use_View_Time_end_time` | `clicked()` | `this` | `set_end_time_value_to_view_time()` |
| `button_Use_View_Time_snapshot_time` | `clicked()` | `this` | `set_snapshot_time_to_view_time()` |
| `widget_start_time` | `valueChanged(double)` | `this` | `react_start_time_spinbox_changed(double)` |
| `widget_end_time` | `valueChanged(double)` | `this` | `react_end_time_spinbox_changed(double)` |
| `widget_time_increment` | `valueChanged(double)` | `this` | `react_time_increment_spinbox_changed(double)` |
| `button_Reverse_the_Animation` | `clicked()` | `d_animation_controller_ptr` | `swap_start_and_end_times()` |
| `checkbox_finish_exactly_on_end_time` | `clicked(bool)` | `d_animation_controller_ptr` | `set_should_finish_exactly_on_end_time(bool)` |
| `button_export` | `clicked()` | `this` | `react_export_button_clicked()` |
| `button_export_single_frame` | `clicked()` | `this` | `react_export_button_clicked()` |
| `button_abort` | `clicked()` | `this` | `react_abort_button_clicked()` |
| `button_add` | `clicked()` | `this` | `react_add_export_clicked()` |
| `button_single_add` | `clicked()` | `this` | `react_add_export_clicked()` |
| `button_single_remove` | `clicked()` | `this` | `react_remove_export_clicked()` |
| `button_remove` | `clicked()` | `this` | `react_remove_export_clicked()` |

*... and 14 more connections.*


## Explore

Run these from the `gplates-code` skill directory:

```bash
python scripts/gpq.py file src/qt-widgets/ExportAnimationDialog.h
python scripts/gpq.py def GPlatesQtWidgets::ExportAnimationDialog --body
python scripts/gpq.py uses ExportAnimationDialog --kind class
python scripts/gpq.py hier ExportAnimationDialog
```
