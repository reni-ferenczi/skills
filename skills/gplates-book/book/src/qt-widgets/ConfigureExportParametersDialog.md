# ConfigureExportParametersDialog

[Book TOC](../../TOC.md) · [qt-widgets](../../components/qt-widgets.md) · cluster Community 825 · tier 2

| Source file | Kind | Lines |
|---|---|---|
| `src/qt-widgets/ConfigureExportParametersDialog.h` | C++ | 308 |
| `src/qt-widgets/ConfigureExportParametersDialog.cc` | C++ | 518 |
| `src/qt-widgets/ConfigureExportParametersDialogUi.ui` | Qt form | 182 |

## Overview

`ConfigureExportParametersDialog` is the "add an export to the animation
export list" dialog launched from `ExportAnimationDialog`/`EditExportParametersDialog`.
Its three cascading lists — export type, then export format, then a
per-exporter `ExportOptionsWidget` and filename template — are driven by
`GPlatesGui::ExportAnimationRegistry`, which is queried both to discover
supported type/format/export-ID combinations and to construct the export-
specific options widget for whatever was selected. `d_export_animation_context_ptr`
is the `GPlatesGui::ExportAnimationContext`, described in the header comment
as the Context role of the Gang-of-Four Strategy pattern, and holds the
actual accumulated export configuration this dialog is populating.

Since `QListWidgetItem` carries no generic payload slot, the dialog attaches
its own state to list items via three small template mixins —
`ExportTypeWidgetItem`, `ExportFormatWidgetItem` and
`ExportConfigurationWidgetItem` — each wrapping a `WidgetItemType` (typically
`QListWidgetItem`) with one extra field, retrieved back through
`dynamic_cast` by the matching `get_export_type()`/`get_export_format()`/
`get_export_configuration()` static template functions. The private
`ExportFormatListWidget` overrides `sizeHint()`/`minimumSizeHint()` to report
its actual contents size, because — per its header comment — no layout
configuration achieved the same effect, letting the format list stay compact
so the export-options area below gets the remaining space.

## Declared types

| Name | Kind | Bases | Template | Subclasses | Description |
|---|---|---|---|---|---|
| [`GPlatesQtWidgets::ConfigureExportParametersDialog`](#gplatesqtwidgetsconfigureexportparametersdialog) | class | `QDialog`<br>`Ui_ConfigureExportParametersDialog` | — | 0 | — |

## Members

### `GPlatesQtWidgets::ConfigureExportParametersDialog`

| Member | Kind | Type | Access | Description |
|---|---|---|---|---|
| `ConfigureExportParametersDialog( GPlatesGui::ExportAnimationContext::non_null_ptr_type export_animation_context_ptr, QWidget *parent_ = NULL)` | constructor | `None` | public | — |
| `~ConfigureExportParametersDialog()` | destructor | `None` | public | — |
| `initialise( QTableWidget*)` | method | `void` | public | — |
| `set_single_frame( bool is_single_frame)` | method | `void` | public | — |
| `add_all_remaining_exports()` | method | `void` | public | — |
| `ExportTypeWidgetItem` | class | `None` | public | A widget item to store the state of an ExportAnimationType::Type. |
| `get_export_type( WidgetItemType* widget_item)` | method | `GPlatesGui::ExportAnimationType::Type` | public | — |
| `ExportFormatWidgetItem` | class | `None` | public | A widget item to store the state of an ExportAnimationType::Format. |
| `get_export_format( WidgetItemType* widget_item)` | method | `GPlatesGui::ExportAnimationType::Format` | public | — |
| `ExportConfigurationWidgetItem` | class | `None` | public | A widget item to store the state of an ExportAnimationStrategy::const\_configuration\_base\_ptr. |
| `get_export_configuration( WidgetItemType* widget_item)` | method | `GPlatesGui::ExportAnimationStrategy::const_configuration_base_ptr` | public | — |
| `react_add_item_clicked()` | method | `void` | private | — |
| `react_export_type_selection_changed()` | method | `void` | private | — |
| `react_export_format_selection_changed()` | method | `void` | private | — |
| `focus_on_listwidget_format()` | method | `void` | private | — |
| `ExportFormatListWidget` | class | `None` | private | A QListWidget that resizes to its contents - this ensures that the QScrollArea just below the list of formats can use as much available space as it can for export configuration options. |
| `d_export_animation_context_ptr` | field | `GPlatesGui::ExportAnimationContext::non_null_ptr_type` | private | The ExportAnimationContext is the Context role of the Strategy pattern in Gamma et al p315. |
| `d_is_single_frame` | field | `bool` | private | — |
| `d_export_format_list_widget` | field | `ExportFormatListWidget` | private | — |
| `d_export_file_name_template_widget` | field | `ExportFileNameTemplateWidget` | private | Used to set and retrieve the filename template. |
| `d_current_export_options_widget` | field | `boost::optional<ExportOptionsWidget *>` | private | The current widget, if any, used to select export options. |
| `d_export_options_widget_layout` | field | `QVBoxLayout` | private | The layout for the export options widget. |
| `initialize_export_type_list_widget()` | method | `void` | private | — |
| `clear_export_options_widget()` | method | `void` | private | — |
| `set_export_options_widget( GPlatesGui::ExportAnimationType::ExportID export_id)` | method | `void` | private | — |

## Free functions and macros

| Name | Kind | Type / body | Description |
|---|---|---|---|
| `GPLATES_QTWIDGETS_CONFIGUREEXPORTPARAMETERSDIALOG_H` | macro | `None` | — |

## Notes

Selecting an export type clears and repopulates the format list, which in
turn re-fires `react_export_format_selection_changed()`; that handler can
therefore be invoked with an export ID left over from the previous type and
silently returns if that ID is not in the registry's currently supported
exporters, rather than warning, because — per a comment in the source — this
happens routinely during the cascade rather than indicating an error. The
`Ok` button in `main_buttonbox` is kept disabled until both a type and a
format resolve to a supported, fully-configured export. `get_export_type()`/
`get_export_format()`/`get_export_configuration()` fall back to an
`INVALID_TYPE`/`INVALID_FORMAT`/default value (logging a `qWarning()`)
instead of asserting if handed a widget item that was not actually one of
this dialog's own wrapper types.

## Used by

| Unit | Component | References |
|---|---|---|
| [qt-widgets/ExportAnimationDialog](ExportAnimationDialog.md) | qt-widgets | 29 |
| [qt-widgets/EditExportParametersDialog](EditExportParametersDialog.md) | qt-widgets | 17 |

## Related

**Qt Designer forms**

| Form class | Base widget | Title | Widgets |
|---|---|---|---|
| `ConfigureExportParametersDialog` | `QDialog` | Add Data to Export | 15 |

**Qt signal/slot connections** (7 in this unit)

| Sender | Signal | Receiver | Slot |
|---|---|---|---|
| `export_type_list_widget` | `itemSelectionChanged()` | `this` | `react_export_type_selection_changed()` |
| `export_type_list_widget` | `itemClicked(QListWidgetItem *)` | `this` | `react_export_type_selection_changed()` |
| `d_export_format_list_widget` | `itemSelectionChanged()` | `this` | `react_export_format_selection_changed()` |
| `main_buttonbox` | `accepted()` | `this` | `react_add_item_clicked()` |
| `main_buttonbox` | `rejected()` | `this` | `reject()` |
| `export_type_list_widget` | `itemPressed(QListWidgetItem *)` | `this` | `focus_on_listwidget_format()` |
| `d_export_format_list_widget` | `itemPressed(QListWidgetItem *)` | `d_export_file_name_template_widget` | `focus_on_line_edit_filename()` |


## Explore

Run these from the `gplates-code` skill directory:

```bash
python scripts/gpq.py file src/qt-widgets/ConfigureExportParametersDialog.h
python scripts/gpq.py def GPlatesQtWidgets::ConfigureExportParametersDialog --body
python scripts/gpq.py uses ConfigureExportParametersDialog --kind class
python scripts/gpq.py hier ConfigureExportParametersDialog
```
