# ShapefileFileFormatConfigurationDialog

[Book TOC](../../TOC.md) · [qt-widgets](../../components/qt-widgets.md) · cluster Community 308 · tier 3

| Source file | Kind | Lines |
|---|---|---|
| `src/qt-widgets/ShapefileFileFormatConfigurationDialog.h` | C++ | 103 |
| `src/qt-widgets/ShapefileFileFormatConfigurationDialog.cc` | C++ | 115 |
| `src/qt-widgets/ShapefileFileFormatConfigurationDialogUi.ui` | Qt form | 56 |

## Overview

[[[PROSE overview unit=qt-widgets/ShapefileFileFormatConfigurationDialog tier=3]]]
Replace this whole block, markers included, with 1-3 paragraphs: what this unit is, why it exists, and how it fits the surrounding design. Do not restate the tables below.
[[[/PROSE]]]

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

[[[PROSE notes unit=qt-widgets/ShapefileFileFormatConfigurationDialog tier=3]]]
Replace this whole block, markers included, with invariants, ownership, threading or gotchas that are not visible in the tables. Write *None.* if there is nothing worth saying.
[[[/PROSE]]]

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
