# ShapefileFileFormatConfigurationDialog

[Book TOC](../../TOC.md) · [qt-widgets](../../components/qt-widgets.md) · cluster Community 308 · tier 3

| Source file | Kind | Lines |
|---|---|---|
| `src/qt-widgets/ShapefileFileFormatConfigurationDialog.h` | C++ | 103 |
| `src/qt-widgets/ShapefileFileFormatConfigurationDialog.cc` | C++ | 115 |
| `src/qt-widgets/ShapefileFileFormatConfigurationDialogUi.ui` | Qt form | 56 |

## Overview

A modal dialog that configures OGR/shapefile file format options when loading or editing a file. It combines two embedded widgets: a `DatelineWrapOptionsWidget` for controlling whether geometries should wrap at the dateline, and a `ShapefileAttributeWidget` for mapping shapefile attributes to model properties.

The dialog is initialized with the dateline-wrap setting and attribute mapping data, and provides access to the final dateline-wrap choice via `get_wrap_to_dateline()` after the user accepts the dialog.

## Declared types

| Name | Kind | Bases | Template | Subclasses | Description |
|---|---|---|---|---|---|
| [`GPlatesQtWidgets::ShapefileFileFormatConfigurationDialog`](#gplatesqtwidgetsshapefilefileformatconfigurationdialog) | class | `QDialog`<br>`Ui_ShapefileFileFormatConfiguration` | — | 0 | — |

## Members

### `GPlatesQtWidgets::ShapefileFileFormatConfigurationDialog`

| Member | Kind | Type | Access | Description |
|---|---|---|---|---|
| `ShapefileFileFormatConfigurationDialog( QWidget *parent_ = NULL)` | constructor | `None` | public | — |
| `~ShapefileFileFormatConfigurationDialog()` | destructor | `None` | public | — |
| `setup( bool dateline_wrap, const QString &filename, const QStringList &field_names, QMap<QString,QString> &model_to_attribute_map)` | method | `void` | public | — |
| `get_wrap_to_dateline()` | method | `bool` | public | Get the wrap-to-dateline option. |
| `accept()` | method | `void` | public | Use the current state of the combo boxes to build up the shapefile-attribute-to-model-property map. |
| `reset()` | method | `void` | public | Reset the combo boxes to the state they were in when the dialog was created. |
| `handle_buttonbox_clicked( QAbstractButton *button)` | method | `void` | private | — |
| `d_dateline_wrap` | field | `bool` | private | — |
| `d_dateline_wrap_options_widget` | field | `DatelineWrapOptionsWidget` | private | — |
| `d_shapefile_attribute_widget` | field | `ShapefileAttributeWidget` | private | — |

## Free functions and macros

| Name | Kind | Type / body | Description |
|---|---|---|---|
| `GPLATES_QTWIDGETS_SHAPEFILEFILEFORMATCONFIGURATIONDIALOG_H` | macro | `None` | — |

## Notes

*None.*

## Used by

| Unit | Component | References |
|---|---|---|
| [qt-widgets/ManageFeatureCollectionsEditConfigurations](ManageFeatureCollectionsEditConfigurations.md) | qt-widgets | 2 |

## Related

**Qt Designer forms**

| Form class | Base widget | Title | Widgets |
|---|---|---|---|
| `ShapefileFileFormatConfiguration` | `QDialog` | Edit OGR File Configuration | 4 |

**Qt signal/slot connections** (3 in this unit)

| Sender | Signal | Receiver | Slot |
|---|---|---|---|
| `main_buttonbox` | `accepted()` | `this` | `accept()` |
| `main_buttonbox` | `rejected()` | `this` | `reject()` |
| `main_buttonbox` | `clicked(QAbstractButton *)` | `this` | `handle_buttonbox_clicked(QAbstractButton *)` |


## Explore

Run these from the `gplates-code` skill directory:

```bash
python scripts/gpq.py file src/qt-widgets/ShapefileFileFormatConfigurationDialog.h
python scripts/gpq.py def GPlatesQtWidgets::ShapefileFileFormatConfigurationDialog --body
python scripts/gpq.py uses ShapefileFileFormatConfigurationDialog --kind class
python scripts/gpq.py hier ShapefileFileFormatConfigurationDialog
```
