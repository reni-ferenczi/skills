# EditExportParametersDialog

[Book TOC](../../TOC.md) · [qt-widgets](../../components/qt-widgets.md) · cluster Community 880 · tier 3

| Source file | Kind | Lines |
|---|---|---|
| `src/qt-widgets/EditExportParametersDialog.h` | C++ | 140 |
| `src/qt-widgets/EditExportParametersDialog.cc` | C++ | 253 |
| `src/qt-widgets/EditExportParametersDialogUi.ui` | Qt form | 90 |

## Overview

A dialog for editing export parameters in the animation export workflow. The dialog is initialized via `initialise()` with the export row being edited and the export configuration, then lets the user modify the export filename template and any export format-specific options. It uses `ExportFileNameTemplateWidget` to manage filename template configuration and dynamically creates an `ExportOptionsWidget` appropriate to the export type (which may be omitted for formats with no options). The dialog is a client of `ExportAnimationContext`, which holds all the export configuration data in the Strategy pattern. When the user accepts, it calls `react_edit_item_accepted()` to sync changes back to the context.

## Declared types

| Name | Kind | Bases | Template | Subclasses | Description |
|---|---|---|---|---|---|
| [`GPlatesQtWidgets::EditExportParametersDialog`](#gplatesqtwidgetseditexportparametersdialog) | class | `QDialog`<br>`Ui_EditExportParametersDialog` | — | 0 | — |

## Members

### `GPlatesQtWidgets::EditExportParametersDialog`

| Member | Kind | Type | Access | Description |
|---|---|---|---|---|
| `EditExportParametersDialog( GPlatesGui::ExportAnimationContext::non_null_ptr_type export_animation_context_ptr, QWidget *parent_ = NULL)` | constructor | `None` | public | — |
| `~EditExportParametersDialog()` | destructor | `None` | public | — |
| `initialise( int export_row_in_animation_dialog, GPlatesGui::ExportAnimationType::ExportID export_id, const GPlatesGui::ExportAnimationStrategy::const_configuration_base_ptr &export_configuration)` | method | `void` | public | Initialise the export configuration that the user is going to edit with this dialog. |
| `set_single_frame( bool is_single_frame)` | method | `void` | public | — |
| `react_edit_item_accepted()` | method | `void` | private | — |
| `d_export_animation_context_ptr` | field | `GPlatesGui::ExportAnimationContext::non_null_ptr_type` | private | The ExportAnimationContext is the Context role of the Strategy pattern in Gamma et al p315. |
| `d_is_single_frame` | field | `bool` | private | — |
| `d_export_file_name_template_widget` | field | `ExportFileNameTemplateWidget` | private | Used to set and retrieve the filename template. |
| `d_export_row_in_animation_dialog` | field | `boost::optional<int>` | private | The export table row, in ExportAnimationDialog, of the export configuration being edited. |
| `d_export_id` | field | `boost::optional<GPlatesGui::ExportAnimationType::ExportID>` | private | The export ID of the export configuration being edited. |
| `d_export_options_widget` | field | `boost::optional<ExportOptionsWidget *>` | private | The widget, if any, used to select export options for the export configuration being edited. |
| `d_export_options_widget_layout` | field | `QVBoxLayout` | private | The layout for the export options widget. |
| `clear_export_options_widget()` | method | `void` | private | — |
| `set_export_options_widget( const GPlatesGui::ExportAnimationStrategy::const_configuration_base_ptr &export_configuration)` | method | `void` | private | — |

## Free functions and macros

| Name | Kind | Type / body | Description |
|---|---|---|---|
| `GPLATES_QTWIDGETS_EDITEXPORTPARAMETERSDIALOG_H` | macro | `None` | — |

## Notes

The dialog must be initialized via `initialise()` before being shown; the export row and ID are stored in optional fields and checked for validity when accepting. The export options widget is also optional (some export types have no format-specific options). The dialog delegates export configuration management to `ExportAnimationContext` and does not own the configuration data. The `set_single_frame()` method controls whether the dialog is for a single-frame or animated export.

## Used by

| Unit | Component | References |
|---|---|---|
| [qt-widgets/ExportAnimationDialog](ExportAnimationDialog.md) | qt-widgets | 3 |

## Related

**Qt Designer forms**

| Form class | Base widget | Title | Widgets |
|---|---|---|---|
| `EditExportParametersDialog` | `QDialog` | Edit Export | 7 |

**Qt signal/slot connections** (2 in this unit)

| Sender | Signal | Receiver | Slot |
|---|---|---|---|
| `main_buttonbox` | `accepted()` | `this` | `react_edit_item_accepted()` |
| `main_buttonbox` | `rejected()` | `this` | `reject()` |


## Explore

Run these from the `gplates-code` skill directory:

```bash
python scripts/gpq.py file src/qt-widgets/EditExportParametersDialog.h
python scripts/gpq.py def GPlatesQtWidgets::EditExportParametersDialog --body
python scripts/gpq.py uses EditExportParametersDialog --kind class
python scripts/gpq.py hier EditExportParametersDialog
```
