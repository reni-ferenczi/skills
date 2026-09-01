# SaveFileDialogImpl

[Book TOC](../../TOC.md) · [qt-widgets](../../components/qt-widgets.md) · cluster Community 622 · tier 3

| Source file | Kind | Lines |
|---|---|---|
| `src/qt-widgets/SaveFileDialogImpl.h` | C++ | 198 |
| `src/qt-widgets/SaveFileDialogImpl.cc` | C++ | 280 |

## Overview

This unit contains the internal implementation classes for a save file dialog that abstracts over platform-specific dialog behavior. A virtual base class `SaveFileDialogImpl` defines the interface, with two concrete implementations: `NativeSaveFileDialog` for Windows and macOS using native file choosers, and `QtSaveFileDialog` for Linux using Qt's file dialog.

The split exists because the native GTK file chooser on Linux does not automatically update the filename extension when the user changes the selected filter, leading to files saved with incorrect extensions. The Qt implementation works around this by manually updating the extension in response to filter changes. Both implementations track file extension to filter mappings and manage the currently selected file and filter.

## Declared types

| Name | Kind | Bases | Template | Subclasses | Description |
|---|---|---|---|---|---|
| [`GPlatesQtWidgets::SaveFileDialogInternals::SaveFileDialogImpl`](#gplatesqtwidgetssavefiledialoginternalssavefiledialogimpl) | class | — | — | 2 | — |
| [`GPlatesQtWidgets::SaveFileDialogInternals::NativeSaveFileDialog`](#gplatesqtwidgetssavefiledialoginternalsnativesavefiledialog) | class | [`SaveFileDialogImpl`](SaveFileDialogImpl.md) | — | 0 | Implementation of SaveFileDialog that uses the native dialog. |
| [`GPlatesQtWidgets::SaveFileDialogInternals::QtSaveFileDialog`](#gplatesqtwidgetssavefiledialoginternalsqtsavefiledialog) | class | `QObject`<br>[`SaveFileDialogImpl`](SaveFileDialogImpl.md) | — | 0 | Implementation of SaveFileDialog that uses the Qt dialog. |

## Members

### `GPlatesQtWidgets::SaveFileDialogInternals::SaveFileDialogImpl`

| Member | Kind | Type | Access | Description |
|---|---|---|---|---|
| `filter_list_type` | typedef | `SaveFileDialog::filter_list_type` | public | — |
| `get_file_name( QString *selected_filter)` | method | `boost::optional<QString>` | public | — |
| `set_filters( const filter_list_type &filters)` | method | `void` | public | — |
| `select_file( const QString &file_path)` | method | `void` | public | — |
| `~SaveFileDialogImpl()` | destructor | `None` | public | — |

### `GPlatesQtWidgets::SaveFileDialogInternals::NativeSaveFileDialog`

| Member | Kind | Type | Access | Description |
|---|---|---|---|---|
| `NativeSaveFileDialog( QWidget *parent_, const QString &caption, const filter_list_type &filters, GPlatesGui::DirectoryConfiguration &directory_configuration)` | constructor | `None` | public | — |
| `get_file_name( QString *selected_filter)` | method | `boost::optional<QString>` | public | — |
| `set_filters( const filter_list_type &filters)` | method | `void` | public | — |
| `select_file( const QString &file_path)` | method | `void` | public | — |
| `d_parent_ptr` | field | `QWidget` | private | — |
| `d_caption` | field | `QString` | private | — |
| `d_filters` | field | `QString` | private | — |
| `d_last_file_name` | field | `QString` | private | — |
| `d_filter_map_ext_to_text` | field | `std::map<QString, QString>` | private | Maps file extension to filter text |
| `d_directory_configuration` | field | `GPlatesGui::DirectoryConfiguration` | private | — |

### `GPlatesQtWidgets::SaveFileDialogInternals::QtSaveFileDialog`

| Member | Kind | Type | Access | Description |
|---|---|---|---|---|
| `QtSaveFileDialog( QWidget *parent_, const QString &caption, const filter_list_type &filters, GPlatesGui::DirectoryConfiguration &directory_configuration)` | constructor | `None` | public | — |
| `get_file_name( QString *selected_filter)` | method | `boost::optional<QString>` | public | — |
| `set_filters( const filter_list_type &filters)` | method | `void` | public | — |
| `select_file( const QString &file_path)` | method | `void` | public | — |
| `handle_filter_changed()` | method | `void` | private | — |
| `d_file_dialog_ptr` | field | `boost::scoped_ptr<QFileDialog>` | private | — |
| `d_filter_map_text_to_ext` | field | `std::map<QString, QString>` | private | Maps filter text to file extension |
| `d_filter_map_ext_to_text` | field | `std::map<QString, QString>` | private | Maps file extension to filter text |
| `d_directory_configuration` | field | `GPlatesGui::DirectoryConfiguration` | private | — |

## Free functions and macros

| Name | Kind | Type / body | Description |
|---|---|---|---|
| `get_file_extension( const QString &filename)` | function | `QString` | — |
| `add_exts_to_map( const std::vector<QString> &extensions, const QString &filter_string, std::map<QString, QString> &map)` | function | `void` | — |
| `GPLATES_QTWIDGETS_SAVEFILEDIALOGIMPL_H` | macro | `None` | — |

## Notes

*None.*

## Used by

| Unit | Component | References |
|---|---|---|
| [qt-widgets/SaveFileDialog](SaveFileDialog.md) | qt-widgets | 3 |

## Related

**Qt signal/slot connections** (1 in this unit)

| Sender | Signal | Receiver | Slot |
|---|---|---|---|
| `d_file_dialog_ptr.get()` | `filterSelected(const QString&)` | `this` | `handle_filter_changed()` |


## Explore

Run these from the `gplates-code` skill directory:

```bash
python scripts/gpq.py file src/qt-widgets/SaveFileDialogImpl.h
python scripts/gpq.py def GPlatesQtWidgets::SaveFileDialogInternals::QtSaveFileDialog --body
python scripts/gpq.py uses QtSaveFileDialog --kind class
python scripts/gpq.py hier QtSaveFileDialog
```
