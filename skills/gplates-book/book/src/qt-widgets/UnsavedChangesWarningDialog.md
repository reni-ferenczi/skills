# UnsavedChangesWarningDialog

[Book TOC](../../TOC.md) · [qt-widgets](../../components/qt-widgets.md) · cluster Community 1340 · tier 3

| Source file | Kind | Lines |
|---|---|---|
| `src/qt-widgets/UnsavedChangesWarningDialog.h` | C++ | 267 |
| `src/qt-widgets/UnsavedChangesWarningDialogUi.ui` | Qt form | 137 |

## Overview

A warning dialog that intercepts operations which would lose unsaved changes. It is shown when the user attempts to close GPlates, clear the session, load a previous session, or load a project while unsaved changes exist. The dialog displays a list of unsaved feature collection files and offers three choices: save all changes first and proceed, discard changes and proceed, or abort the operation. The text and button labels adapt to the specific action being interrupted (e.g., "Close GPlates" vs. "Load Project"). It is triggered and managed by `UnsavedChangesTracker` in the gui module.

## Declared types

| Name | Kind | Bases | Template | Subclasses | Description |
|---|---|---|---|---|---|
| [`GPlatesQtWidgets::UnsavedChangesWarningDialog`](#gplatesqtwidgetsunsavedchangeswarningdialog) | class | `QDialog`<br>`Ui_UnsavedChangesWarningDialog` | — | 0 | This dialog is the one which pops up if the user attempts to close GPlates while there are yet files unsaved. |

## Members

### `GPlatesQtWidgets::UnsavedChangesWarningDialog`

| Member | Kind | Type | Access | Description |
|---|---|---|---|---|
| `ActionRequested` | enum | `None` | public | — |
| `UnsavedChangesWarningDialog( QWidget *parent_ = NULL)` | constructor | `None` | public | — |
| `~UnsavedChangesWarningDialog()` | destructor | `None` | public | — |
| `set_action_requested( ActionRequested act, QStringList unsaved_feature_collection_filenames, bool has_unsaved_project_changes)` | method | `void` | public | Changes the label text and button labels to be appropriate for the corresponding action requested by the user (that GPlates is interrupting on account of the unsaved changes). |
| `discard_changes()` | method | `void` | private | — |
| `abort_close()` | method | `void` | private | — |
| `tweak_file_list( QStringList unsaved_feature_collection_filenames)` | method | `void` | private | Populate the unsaved feature collection list or hide it if all are saved. |
| `tweak_buttons( ActionRequested act)` | method | `void` | private | Overrides the default labels on the StandardButtons Qt provides, and adds icons. |
| `tweak_label( ActionRequested act, bool has_unsaved_feature_collections, bool has_unsaved_project_changes)` | method | `void` | private | Sets the dialog's main descriptive label (as defined in UI) to something more context-sensitive. |
| `connect_buttons()` | method | `void` | private | Connects all the buttons to a single signal that we can emit to indicate what button was clicked on this dialog. |

## Free functions and macros

| Name | Kind | Type / body | Description |
|---|---|---|---|
| `GPLATES_QTWIDGETS_UNSAVEDCHANGESWARNINGDIALOG_H` | macro | `None` | — |

## Notes

*None.*

## Used by

| Unit | Component | References |
|---|---|---|
| [gui/UnsavedChangesTracker](../gui/UnsavedChangesTracker.md) | gui | 7 |

## Related

**Qt Designer forms**

| Form class | Base widget | Title | Widgets |
|---|---|---|---|
| `UnsavedChangesWarningDialog` | `QDialog` | Unsaved Changes | 6 |

**Qt signal/slot connections** (2 in this unit)

| Sender | Signal | Receiver | Slot |
|---|---|---|---|
| `buttonbox->button(QDialogButtonBox::Discard)` | `clicked()` | `this` | `discard_changes()` |
| `buttonbox->button(QDialogButtonBox::Abort)` | `clicked()` | `this` | `abort_close()` |


## Explore

Run these from the `gplates-code` skill directory:

```bash
python scripts/gpq.py file src/qt-widgets/UnsavedChangesWarningDialog.h
python scripts/gpq.py def GPlatesQtWidgets::UnsavedChangesWarningDialog --body
python scripts/gpq.py uses UnsavedChangesWarningDialog --kind class
python scripts/gpq.py hier UnsavedChangesWarningDialog
```
