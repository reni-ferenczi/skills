# ShapefileAttributeMapperDialog

[Book TOC](../../TOC.md) · [qt-widgets](../../components/qt-widgets.md) · cluster Community 308 · tier 3

| Source file | Kind | Lines |
|---|---|---|
| `src/qt-widgets/ShapefileAttributeMapperDialog.h` | C++ | 93 |
| `src/qt-widgets/ShapefileAttributeMapperDialog.cc` | C++ | 106 |
| `src/qt-widgets/ShapefileAttributeMapperDialogUi.ui` | Qt form | 53 |

## Overview

[[[PROSE overview unit=qt-widgets/ShapefileAttributeMapperDialog tier=3]]]
Replace this whole block, markers included, with 1-3 paragraphs: what this unit is, why it exists, and how it fits the surrounding design. Do not restate the tables below.
[[[/PROSE]]]

## Declared types

| Name | Kind | Bases | Template | Subclasses | Description |
|---|---|---|---|---|---|
| [`GPlatesQtWidgets::ShapefileAttributeMapperDialog`](#gplatesqtwidgetsshapefileattributemapperdialog) | class | `QDialog`<br>`Ui_ShapefileAttributeMapper` | — | 0 | — |

## Members

### `GPlatesQtWidgets::ShapefileAttributeMapperDialog`

| Member | Kind | Type | Access | Description |
|---|---|---|---|---|
| `ShapefileAttributeMapperDialog( QWidget *parent_ = NULL)` | constructor | `None` | public | — |
| `~ShapefileAttributeMapperDialog()` | destructor | `None` | public | — |
| `setup( QString &filename, QStringList &field_names, QMap<QString,QString> &model_to_attribute_map)` | method | `void` | public | — |
| `accept()` | method | `void` | public | Use the current state of the combo boxes to build up the shapefile-attribute-to-model-property map. |
| `reset_fields()` | method | `void` | public | Reset the combo boxes to the state they were in when the dialog was created. |
| `handle_buttonbox_clicked( QAbstractButton *button)` | method | `void` | private | — |
| `d_shapefile_attribute_widget` | field | `ShapefileAttributeWidget` | private | — |

## Free functions and macros

| Name | Kind | Type / body | Description |
|---|---|---|---|
| `GPLATES_QTWIDGETS_SHAPEFILEATTRIBUTEMAPPERDIALOG_H` | macro | `None` | — |

## Notes

[[[PROSE notes unit=qt-widgets/ShapefileAttributeMapperDialog tier=3]]]
Replace this whole block, markers included, with invariants, ownership, threading or gotchas that are not visible in the tables. Write *None.* if there is nothing worth saying.
[[[/PROSE]]]

## Used by

| Unit | Component | References |
|---|---|---|
| [qt-widgets/ShapefilePropertyMapper](ShapefilePropertyMapper.md) | qt-widgets | 7 |

## Related

**Qt Designer forms**

| Form class | Base widget | Title | Widgets |
|---|---|---|---|
| `ShapefileAttributeMapper` | `QDialog` | Map File Attributes | 3 |

**Qt signal/slot connections** (3 in this unit)

| Sender | Signal | Receiver | Slot |
|---|---|---|---|
| `main_buttonbox` | `accepted()` | `this` | `accept()` |
| `main_buttonbox` | `rejected()` | `this` | `reject()` |
| `main_buttonbox` | `clicked(QAbstractButton *)` | `this` | `handle_buttonbox_clicked(QAbstractButton *)` |


## Explore

Run these from the `gplates-code` skill directory:

```bash
python scripts/gpq.py file src/qt-widgets/ShapefileAttributeMapperDialog.h
python scripts/gpq.py def GPlatesQtWidgets::ShapefileAttributeMapperDialog --body
python scripts/gpq.py uses ShapefileAttributeMapperDialog --kind class
python scripts/gpq.py hier ShapefileAttributeMapperDialog
```
