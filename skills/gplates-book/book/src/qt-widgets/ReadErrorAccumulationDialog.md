# ReadErrorAccumulationDialog

[Book TOC](../../TOC.md) · [qt-widgets](../../components/qt-widgets.md) · cluster Community 102 · tier 2

| Source file | Kind | Lines |
|---|---|---|
| `src/qt-widgets/ReadErrorAccumulationDialog.h` | C++ | 258 |
| `src/qt-widgets/ReadErrorAccumulationDialog.cc` | C++ | 496 |
| `src/qt-widgets/ReadErrorAccumulationDialogUi.ui` | Qt form | 143 |

## Overview

[[[PROSE overview unit=qt-widgets/ReadErrorAccumulationDialog tier=2]]]
Replace this whole block, markers included, with 1-3 paragraphs: what this unit is, why it exists, and how it fits the surrounding design. Do not restate the tables below.
[[[/PROSE]]]

## Declared types

| Name | Kind | Bases | Template | Subclasses | Description |
|---|---|---|---|---|---|
| [`GPlatesQtWidgets::ReadErrorAccumulationDialog`](#gplatesqtwidgetsreaderroraccumulationdialog) | class | [`GPlatesDialog`](GPlatesDialog.md)<br>`Ui_ReadErrorAccumulationDialog` | — | 0 | — |

## Members

### `GPlatesQtWidgets::ReadErrorAccumulationDialog`

| Member | Kind | Type | Access | Description |
|---|---|---|---|---|
| `ReadErrorAccumulationDialog( QWidget *parent_ = NULL)` | constructor | `None` | public | — |
| `clear()` | method | `void` | public | Removes all errors from the tree and resets the top-level items. |
| `update()` | method | `void` | public | Updates the dialog from d\_read\_errors, changing label text and populating the tree. |
| `pop_up_help_dialog()` | method | `void` | public | — |
| `expandAll()` | method | `void` | public | — |
| `collapseAll()` | method | `void` | public | — |
| `clear_errors()` | method | `void` | public | — |
| `handle_buttonbox_clicked( QAbstractButton *button)` | method | `void` | private | — |
| `d_tree_type_failures_to_begin_ptr` | field | `QTreeWidgetItem` | private | Top-level QTreeWidgetItems which will be managed by the QTreeWidget for "By Error" We need to store a pointer to them in order to add children. |
| `d_tree_type_terminating_errors_ptr` | field | `QTreeWidgetItem` | private | — |
| `d_tree_type_recoverable_errors_ptr` | field | `QTreeWidgetItem` | private | — |
| `d_tree_type_warnings_ptr` | field | `QTreeWidgetItem` | private | — |
| `d_tree_line_failures_to_begin_ptr` | field | `QTreeWidgetItem` | private | Top-level QTreeWidgetItems which will be managed by the QTreeWidget for "By Line" We need to store a pointer to them in order to add children. |
| `d_tree_line_terminating_errors_ptr` | field | `QTreeWidgetItem` | private | — |
| `d_tree_line_recoverable_errors_ptr` | field | `QTreeWidgetItem` | private | — |
| `d_tree_line_warnings_ptr` | field | `QTreeWidgetItem` | private | — |
| `d_information_dialog` | field | `InformationDialog` | private | InformationDialog used to inform the user about different error types. |
| `s_information_dialog_text` | field | `QString` | private | — |
| `s_information_dialog_title` | field | `QString` | private | — |
| `d_read_errors` | field | `GPlatesFileIO::ReadErrorAccumulation` | private | The ReadErrorAccumulation used to store all errors for all files currently loaded by GPlates. |
| `populate_top_level_tree_by_type( QTreeWidgetItem *tree_item_ptr, QString tree_item_text, const GPlatesFileIO::ReadErrorAccumulation::read_error_collection_type &errors, const QIcon &occurrence_icon)` | method | `void` | private | Populates one of the Failure to Begin, Terminating Errors, Recoverable Errors or Warnings tree items, unhiding it as necessary and ordering errors by type. |
| `populate_top_level_tree_by_line( QTreeWidgetItem *tree_item_ptr, QString tree_item_text, const GPlatesFileIO::ReadErrorAccumulation::read_error_collection_type &errors, const QIcon &occurrence_icon)` | method | `void` | private | Populates one of the Failure to Begin, Terminating Errors, Recoverable Errors or Warnings tree items, unhiding it as necessary and ordering errors by line. |
| `build_file_tree_by_type( QTreeWidgetItem *parent_item_ptr, const GPlatesFileIO::ReadErrorAccumulation::read_error_collection_type &errors, const QIcon &occurrence_icon)` | method | `void` | private | Builds a tree widget item for the file entry and all errors beneath it, by line number. |
| `build_file_tree_by_line( QTreeWidgetItem *parent_item_ptr, const GPlatesFileIO::ReadErrorAccumulation::read_error_collection_type &errors, const QIcon &occurrence_icon)` | method | `void` | private | Builds a tree widget item for the file entry and all errors beneath it, by error type. |
| `build_occurrence_line_list( QTreeWidgetItem *parent_item_ptr, const GPlatesFileIO::ReadErrorAccumulation::read_error_collection_type &errors, const QIcon &occurrence_icon, bool show_short_description)` | method | `void` | private | Adds a sequence of Line Number nodes to a parent tree widget item, with Description and Result sub-items. |
| `create_occurrence_type_summary_item( const GPlatesFileIO::ReadErrorOccurrence &error, const QIcon &occurrence_icon, size_t quantity)` | method | `QTreeWidgetItem` | private | Creates a Type Summary item for an error occurrence with short description and quantity. |
| `create_occurrence_file_info_item( const GPlatesFileIO::ReadErrorOccurrence &error)` | method | `QTreeWidgetItem` | private | Creates a File Info item for an error occurrence with base file name and type. |
| `create_occurrence_file_path_item( const GPlatesFileIO::ReadErrorOccurrence &error)` | method | `QTreeWidgetItem` | private | Creates a File Path item for an error occurrence with full path (as found on command line). |
| `create_occurrence_line_item( const GPlatesFileIO::ReadErrorOccurrence &error, const QIcon &occurrence_icon, bool show_short_description)` | method | `QTreeWidgetItem` | private | Creates a Line item for an error occurrence of the form "Line %d \[%d; %d\] %s". |
| `create_occurrence_description_item( const GPlatesFileIO::ReadErrorOccurrence &error)` | method | `QTreeWidgetItem` | private | Creates a Description item for an error occurrence with code and full text. |
| `create_occurrence_result_item( const GPlatesFileIO::ReadErrorOccurrence &error)` | method | `QTreeWidgetItem` | private | Creates a Result item for an error occurrence with code and full text. |

## Free functions and macros

| Name | Kind | Type / body | Description |
|---|---|---|---|
| `s_information_dialog_text` | variable | `QString` | — |
| `s_information_dialog_title` | variable | `QString` | — |
| `GPLATES_GUI_READERRORACCUMULATIONDIALOG_H` | macro | `None` | — |

## Notes

[[[PROSE notes unit=qt-widgets/ReadErrorAccumulationDialog tier=2]]]
Replace this whole block, markers included, with invariants, ownership, threading or gotchas that are not visible in the tables. Write *None.* if there is nothing worth saying.
[[[/PROSE]]]

## Used by

| Unit | Component | References |
|---|---|---|
| [gui/Dialogs](../gui/Dialogs.md) | gui | 8 |
| [qt-widgets/MetadataDialog](MetadataDialog.md) | qt-widgets | 3 |
| [qt-widgets/ColouringDialog](ColouringDialog.md) | qt-widgets | 2 |
| [qt-widgets/HellingerPickWidget](HellingerPickWidget.md) | qt-widgets | 2 |
| [qt-widgets/HellingerDialog](HellingerDialog.md) | qt-widgets | 1 |
| [qt-widgets/ViewportWindow](ViewportWindow.md) | qt-widgets | 1 |

## Related

**Qt Designer forms**

| Form class | Base widget | Title | Widgets |
|---|---|---|---|
| `ReadErrorAccumulationDialog` | `QDialog` | Read Errors | 11 |

**Qt signal/slot connections** (4 in this unit)

| Sender | Signal | Receiver | Slot |
|---|---|---|---|
| `button_help` | `clicked()` | `this` | `pop_up_help_dialog()` |
| `button_expand_all` | `clicked()` | `this` | `expandAll()` |
| `button_collapse_all` | `clicked()` | `this` | `collapseAll()` |
| `main_buttonbox` | `clicked(QAbstractButton *)` | `this` | `handle_buttonbox_clicked(QAbstractButton *)` |


## Explore

Run these from the `gplates-code` skill directory:

```bash
python scripts/gpq.py file src/qt-widgets/ReadErrorAccumulationDialog.h
python scripts/gpq.py def GPlatesQtWidgets::ReadErrorAccumulationDialog --body
python scripts/gpq.py uses ReadErrorAccumulationDialog --kind class
python scripts/gpq.py hier ReadErrorAccumulationDialog
```
