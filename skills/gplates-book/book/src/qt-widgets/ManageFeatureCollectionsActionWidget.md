# ManageFeatureCollectionsActionWidget

[Book TOC](../../TOC.md) · [qt-widgets](../../components/qt-widgets.md) · cluster Community 1277 · tier 2

| Source file | Kind | Lines |
|---|---|---|
| `src/qt-widgets/ManageFeatureCollectionsActionWidget.h` | C++ | 117 |
| `src/qt-widgets/ManageFeatureCollectionsActionWidget.cc` | C++ | 145 |
| `src/qt-widgets/ManageFeatureCollectionsActionWidgetUi.ui` | Qt form | 224 |

## Overview

[[[PROSE overview unit=qt-widgets/ManageFeatureCollectionsActionWidget tier=2]]]
Replace this whole block, markers included, with 1-3 paragraphs: what this unit is, why it exists, and how it fits the surrounding design. Do not restate the tables below.
[[[/PROSE]]]

## Declared types

| Name | Kind | Bases | Template | Subclasses | Description |
|---|---|---|---|---|---|
| [`GPlatesQtWidgets::ManageFeatureCollectionsActionWidget`](#gplatesqtwidgetsmanagefeaturecollectionsactionwidget) | class | `QWidget`<br>`Ui_ManageFeatureCollectionsActionWidget` | — | 0 | — |

## Members

### `GPlatesQtWidgets::ManageFeatureCollectionsActionWidget`

| Member | Kind | Type | Access | Description |
|---|---|---|---|---|
| `ManageFeatureCollectionsActionWidget( ManageFeatureCollectionsDialog &feature_collections_dialog, GPlatesAppLogic::FeatureCollectionFileState::file_reference file_ref, QWidget *parent_ = NULL)` | constructor | `None` | public | Constructor. |
| `update( const GPlatesFileIO::FeatureCollectionFileFormat::Registry &file_format_registry, const GPlatesFileIO::FileInfo &fileinfo, boost::optional<GPlatesFileIO::FeatureCollectionFileFormat::Format> file_format, bool enable_edit_configuration)` | method | `void` | public | Updates with a new filename. file\_format is boost::none if the file's format could not be determined. |
| `get_file_reference()` | method | `GPlatesAppLogic::FeatureCollectionFileState::file_reference` | public | Returns the file referenced by this action widget. |
| `handle_edit_configuration()` | method | `void` | private | — |
| `handle_save()` | method | `void` | private | — |
| `handle_save_as()` | method | `void` | private | — |
| `handle_save_copy()` | method | `void` | private | — |
| `handle_reload()` | method | `void` | private | — |
| `handle_unload()` | method | `void` | private | — |
| `d_feature_collections_dialog` | field | `ManageFeatureCollectionsDialog` | private | — |
| `d_file_reference` | field | `GPlatesAppLogic::FeatureCollectionFileState::file_reference` | private | — |

## Free functions and macros

| Name | Kind | Type / body | Description |
|---|---|---|---|
| `GPLATES_QTWIDGETS_MANAGEFEATURECOLLECTIONSACTIONWIDGET_H` | macro | `None` | — |

## Notes

[[[PROSE notes unit=qt-widgets/ManageFeatureCollectionsActionWidget tier=2]]]
Replace this whole block, markers included, with invariants, ownership, threading or gotchas that are not visible in the tables. Write *None.* if there is nothing worth saying.
[[[/PROSE]]]

## Used by

| Unit | Component | References |
|---|---|---|
| [qt-widgets/ManageFeatureCollectionsDialog](ManageFeatureCollectionsDialog.md) | qt-widgets | 37 |

## Related

**Qt Designer forms**

| Form class | Base widget | Title | Widgets |
|---|---|---|---|
| `ManageFeatureCollectionsActionWidget` | `QWidget` | Feature Collection Actions | 7 |

**Qt signal/slot connections** (6 in this unit)

| Sender | Signal | Receiver | Slot |
|---|---|---|---|
| `button_edit_configuration` | `clicked()` | `this` | `handle_edit_configuration()` |
| `button_save` | `clicked()` | `this` | `handle_save()` |
| `button_save_as` | `clicked()` | `this` | `handle_save_as()` |
| `button_save_copy` | `clicked()` | `this` | `handle_save_copy()` |
| `button_reload` | `clicked()` | `this` | `handle_reload()` |
| `button_unload` | `clicked()` | `this` | `handle_unload()` |


## Explore

Run these from the `gplates-code` skill directory:

```bash
python scripts/gpq.py file src/qt-widgets/ManageFeatureCollectionsActionWidget.h
python scripts/gpq.py def GPlatesQtWidgets::ManageFeatureCollectionsActionWidget --body
python scripts/gpq.py uses ManageFeatureCollectionsActionWidget --kind class
python scripts/gpq.py hier ManageFeatureCollectionsActionWidget
```
