# GpgimVersionWarningDialog

[Book TOC](../../TOC.md) · [qt-widgets](../../components/qt-widgets.md) · cluster Community 1449 · tier 3

| Source file | Kind | Lines |
|---|---|---|
| `src/qt-widgets/GpgimVersionWarningDialog.h` | C++ | 128 |
| `src/qt-widgets/GpgimVersionWarningDialog.cc` | C++ | 176 |
| `src/qt-widgets/GpgimVersionWarningDialogUi.ui` | Qt form | 222 |

## Overview

Warning dialog shown when loading or saving GPML files created with a different GPGIM (GPlates Geological Information Model) version than the current application. The dialog alerts the user that overwriting files with a different GPGIM version could render them unreadable by older versions of GPlates, and provides options appropriate to the context: when saving, the user can choose to save, abort the save, or close; when loading, they can acknowledge or suppress future warnings.

The dialog is customizable via `set_action_requested()` to distinguish between load and save workflows, adjusting the button labels and descriptive text via `tweak_buttons()` and `tweak_label()`. It tracks the user's preference to suppress load warnings independently, always showing the dialog for save operations where the risk of data loss is higher.

## Declared types

| Name | Kind | Bases | Template | Subclasses | Description |
|---|---|---|---|---|---|
| [`GPlatesQtWidgets::GpgimVersionWarningDialog`](#gplatesqtwidgetsgpgimversionwarningdialog) | class | `QDialog`<br>`Ui_GpgimVersionWarningDialog` | — | 0 | This dialog is the one which pops up if the user loads files that were created with a different GPGIM version than the current GPlates or if the user attempts to save those files. |

## Members

### `GPlatesQtWidgets::GpgimVersionWarningDialog`

| Member | Kind | Type | Access | Description |
|---|---|---|---|---|
| `ActionRequested` | enum | `None` | public | — |
| `GpgimVersionWarningDialog( bool show_dialog_on_loading_files = true, QWidget *parent_ = NULL)` | constructor | `None` | public | If show\_dialog\_on\_loading\_files is true then this warning dialog will \*not\* be shown when \*loading\* files. |
| `~GpgimVersionWarningDialog()` | destructor | `None` | public | — |
| `set_action_requested( ActionRequested act, QStringList older_version_filenames, QStringList newer_version_filenames)` | method | `void` | public | Changes the list of older and newer version filenames displayed in the dialog. |
| `do_not_show_dialog_on_loading_files()` | method | `bool` | public | Returns true if the user has requested that this warning dialog should \*not\* be shown when \*loading\* files. |
| `save_changes()` | method | `void` | private | — |
| `abort_save()` | method | `void` | private | — |
| `close()` | method | `void` | private | — |
| `tweak_buttons( ActionRequested act)` | method | `void` | private | Overrides the default labels on the StandardButtons Qt provides, and adds icons. |
| `tweak_label( ActionRequested act)` | method | `void` | private | Sets the dialog's main descriptive label (as defined in UI) to something more context-sensitive. |

## Free functions and macros

| Name | Kind | Type / body | Description |
|---|---|---|---|
| `GPLATES_QTWIDGETS_GPGIMVERSIONWARNINGDIALOG_H` | macro | `None` | — |

## Notes

*None.*

## Used by

*Nothing in the tree references this unit.*

## Related

**Qt Designer forms**

| Form class | Base widget | Title | Widgets |
|---|---|---|---|
| `GpgimVersionWarningDialog` | `QDialog` | GPlates Geological Information Model Version | 14 |

**Qt signal/slot connections** (3 in this unit)

| Sender | Signal | Receiver | Slot |
|---|---|---|---|
| `buttonbox->button(QDialogButtonBox::Save)` | `clicked()` | `this` | `save_changes()` |
| `buttonbox->button(QDialogButtonBox::Abort)` | `clicked()` | `this` | `abort_save()` |
| `buttonbox->button(QDialogButtonBox::Close)` | `clicked()` | `this` | `close()` |


## Explore

Run these from the `gplates-code` skill directory:

```bash
python scripts/gpq.py file src/qt-widgets/GpgimVersionWarningDialog.h
python scripts/gpq.py def GPlatesQtWidgets::GpgimVersionWarningDialog --body
python scripts/gpq.py uses GpgimVersionWarningDialog --kind class
python scripts/gpq.py hier GpgimVersionWarningDialog
```
