# ShapefileAttributeViewerDialog

[Book TOC](../../TOC.md) · [qt-widgets](../../components/qt-widgets.md) · cluster Community 561 · tier 3

| Source file | Kind | Lines |
|---|---|---|
| `src/qt-widgets/ShapefileAttributeViewerDialog.h` | C++ | 101 |
| `src/qt-widgets/ShapefileAttributeViewerDialog.cc` | C++ | 311 |
| `src/qt-widgets/ShapefileAttributeViewerDialogUi.ui` | Qt form | 136 |

## Overview

A modeless dialog that displays the raw shapefile attributes of features in the current feature collection as a table. The dialog extracts the `shapefileAttributes` property (a `GpmlKeyValueDictionary` containing key-value pairs from the original shapefile) from each feature and populates table columns from the keys and rows from the values.

The dialog holds a `vector` of `File::Reference` pointers to track files with shapefile attributes and allows the user to switch between feature collections via a combo box. When the file state changes (e.g., a file is loaded or reloaded), the dialog updates to reflect the new set of available feature collections and their attributes.

## Declared types

| Name | Kind | Bases | Template | Subclasses | Description |
|---|---|---|---|---|---|
| [`GPlatesQtWidgets::ShapefileAttributeViewerDialog`](#gplatesqtwidgetsshapefileattributeviewerdialog) | class | [`GPlatesDialog`](GPlatesDialog.md)<br>`Ui_ShapefileAttributeViewerDialog` | — | 0 | — |

## Members

### `GPlatesQtWidgets::ShapefileAttributeViewerDialog`

| Member | Kind | Type | Access | Description |
|---|---|---|---|---|
| `ShapefileAttributeViewerDialog( GPlatesAppLogic::FeatureCollectionFileState &file_state, QWidget *parent_= NULL)` | constructor | `None` | public | — |
| `~ShapefileAttributeViewerDialog()` | destructor | `None` | public | — |
| `update( GPlatesAppLogic::FeatureCollectionFileState &file_state)` | method | `void` | public | Update the dialog to reflect the current Application State. |
| `update_table()` | method | `void` | private | — |
| `connect_feature_collection_file_state_signals( GPlatesAppLogic::FeatureCollectionFileState &file_state)` | method | `void` | private | — |
| `handle_feature_collection_changed( int index)` | method | `void` | private | Handle the feature-collection combo-box changing, which will require us to update the table contents. |
| `d_file_vector` | field | `std::vector<GPlatesFileIO::File::Reference *>` | private | Files corresponding to shapefile feature collections. |

## Free functions and macros

| Name | Kind | Type / body | Description |
|---|---|---|---|
| `feature_collection_contains_shapefile_attributes( const GPlatesModel::FeatureCollectionHandle::const_weak_ref &feature_collection)` | function | `bool` | — |
| `file_contains_shapefile_attributes( const GPlatesFileIO::File::Reference &file)` | function | `bool` | — |
| `is_file_shapefile( const GPlatesFileIO::FileInfo &file_info)` | function | `bool` | — |
| `fill_header_from_feature( const GPlatesModel::FeatureHandle::weak_ref &feature, QTableWidget *table_widget)` | function | `void` | — |
| `fill_row_from_feature( const GPlatesModel::FeatureHandle::weak_ref &feature, QTableWidget* table_widget, int row)` | function | `void` | — |
| `fill_table_from_feature_collection( const GPlatesModel::FeatureCollectionHandle::weak_ref &feature_collection, QTableWidget *table_widget)` | function | `void` | — |
| `GPLATES_QTWIDGETS_SHAPEFILEATTRIBUTEVIEWERDIALOG_H` | macro | `None` | — |

## Notes

The `d_file_vector` maintains its own copies of file references to track which files contain shapefile attributes. Features are normally expected to have at most one `shapefileAttributes` property, though the code defends against multiple dictionaries and logs a comment if found.

## Used by

| Unit | Component | References |
|---|---|---|
| [gui/Dialogs](../gui/Dialogs.md) | gui | 1 |
| [presentation/Application](../presentation/Application.md) | presentation | 1 |

## Related

**Qt Designer forms**

| Form class | Base widget | Title | Widgets |
|---|---|---|---|
| `ShapefileAttributeViewerDialog` | `QDialog` | Attribute Table | 6 |

**Qt signal/slot connections** (2 in this unit)

| Sender | Signal | Receiver | Slot |
|---|---|---|---|
| `combo_feature_collections` | `currentIndexChanged(int)` | `this` | `handle_feature_collection_changed(int)` |
| `&file_state` | `file_state_changed( GPlatesAppLogic::FeatureCollectionFileState &)` | `this` | `update( GPlatesAppLogic::FeatureCollectionFileState &)` |


## Explore

Run these from the `gplates-code` skill directory:

```bash
python scripts/gpq.py file src/qt-widgets/ShapefileAttributeViewerDialog.h
python scripts/gpq.py def GPlatesQtWidgets::ShapefileAttributeViewerDialog --body
python scripts/gpq.py uses ShapefileAttributeViewerDialog --kind class
python scripts/gpq.py hier ShapefileAttributeViewerDialog
```
