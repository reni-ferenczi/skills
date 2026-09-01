# ChooseFeatureCollectionDialog

[Book TOC](../../TOC.md) · [qt-widgets](../../components/qt-widgets.md) · cluster Community 0 · tier 3

| Source file | Kind | Lines |
|---|---|---|
| `src/qt-widgets/ChooseFeatureCollectionDialog.h` | C++ | 106 |
| `src/qt-widgets/ChooseFeatureCollectionDialog.cc` | C++ | 152 |
| `src/qt-widgets/ChooseFeatureCollectionDialogUi.ui` | Qt form | 43 |

## Overview

Dialog wrapper around `ChooseFeatureCollectionWidget` for selecting a feature collection file. The dialog offers three overloaded `get_file_reference()` methods: one taking an initial file reference to pre-select, one taking an initial feature collection, and one with no initial selection. Each runs the dialog and returns either the user's selected file reference plus a flag indicating whether it was newly created, or `boost::none` if the user cancelled or an exception occurred.

## Declared types

| Name | Kind | Bases | Template | Subclasses | Description |
|---|---|---|---|---|---|
| [`GPlatesQtWidgets::ChooseFeatureCollectionDialog`](#gplatesqtwidgetschoosefeaturecollectiondialog) | class | [`GPlatesDialog`](GPlatesDialog.md)<br>`Ui_ChooseFeatureCollectionDialog` | — | 0 | — |

## Members

### `GPlatesQtWidgets::ChooseFeatureCollectionDialog`

| Member | Kind | Type | Access | Description |
|---|---|---|---|---|
| `ChooseFeatureCollectionDialog( const GPlatesAppLogic::ReconstructMethodRegistry &reconstruct_method_registry, GPlatesAppLogic::FeatureCollectionFileState &file_state, GPlatesAppLogic::FeatureCollectionFileIO &file_io, QWidget *parent_ = NULL)` | constructor | `None` | public | — |
| `get_file_reference( const GPlatesAppLogic::FeatureCollectionFileState::file_reference &initial)` | method | `boost::optional<std::pair<GPlatesAppLogic::FeatureCollectionFileState::file_reference, bool> >` | public | Returns an iterator to the file selected by the user, and a boolean value indicating whether the iterator points to a file that was newly created. |
| `get_file_reference( const GPlatesModel::FeatureCollectionHandle::weak_ref &initial)` | method | `boost::optional<std::pair<GPlatesAppLogic::FeatureCollectionFileState::file_reference, bool> >` | public | Returns an iterator to the file selected by the user, and a boolean value indicating whether the iterator points to a file that was newly created. |
| `get_file_reference()` | method | `boost::optional<std::pair<GPlatesAppLogic::FeatureCollectionFileState::file_reference, bool> >` | public | Overloaded version of get\_file\_reference which does not require an initial feature collection or file\_reference. |
| `d_choose_widget` | field | `ChooseFeatureCollectionWidget` | private | — |

## Free functions and macros

| Name | Kind | Type / body | Description |
|---|---|---|---|
| `GPLATES_QTWIDGETS_CHOOSEFEATURECOLLECTIONDIALOG_H` | macro | `None` | — |

## Notes

*None.*

## Used by

| Unit | Component | References |
|---|---|---|
| [qt-widgets/ViewportWindow](ViewportWindow.md) | qt-widgets | 2 |
| [gui/Dialogs](../gui/Dialogs.md) | gui | 1 |

## Related

**Qt Designer forms**

| Form class | Base widget | Title | Widgets |
|---|---|---|---|
| `ChooseFeatureCollectionDialog` | `QDialog` | Choose Feature Collection | 3 |

**Qt signal/slot connections** (3 in this unit)

| Sender | Signal | Receiver | Slot |
|---|---|---|---|
| `d_choose_widget` | `item_activated()` | `this` | `accept()` |
| `main_buttonbox` | `accepted()` | `this` | `accept()` |
| `main_buttonbox` | `rejected()` | `this` | `reject()` |


## Explore

Run these from the `gplates-code` skill directory:

```bash
python scripts/gpq.py file src/qt-widgets/ChooseFeatureCollectionDialog.h
python scripts/gpq.py def GPlatesQtWidgets::ChooseFeatureCollectionDialog --body
python scripts/gpq.py uses ChooseFeatureCollectionDialog --kind class
python scripts/gpq.py hier ChooseFeatureCollectionDialog
```
