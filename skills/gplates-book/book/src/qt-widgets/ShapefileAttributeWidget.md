# ShapefileAttributeWidget

[Book TOC](../../TOC.md) · [qt-widgets](../../components/qt-widgets.md) · cluster Community 1337 · tier 2

| Source file | Kind | Lines |
|---|---|---|
| `src/qt-widgets/ShapefileAttributeWidget.h` | C++ | 90 |
| `src/qt-widgets/ShapefileAttributeWidget.cc` | C++ | 389 |
| `src/qt-widgets/ShapefileAttributeWidgetUi.ui` | Qt form | 307 |

## Overview

[[[PROSE overview unit=qt-widgets/ShapefileAttributeWidget tier=2]]]
Replace this whole block, markers included, with 1-3 paragraphs: what this unit is, why it exists, and how it fits the surrounding design. Do not restate the tables below.
[[[/PROSE]]]

## Declared types

| Name | Kind | Bases | Template | Subclasses | Description |
|---|---|---|---|---|---|
| [`GPlatesQtWidgets::ShapefileAttributeWidget`](#gplatesqtwidgetsshapefileattributewidget) | class | `QWidget`<br>`Ui_ShapefileAttributeWidget` | — | 0 | — |

## Members

### `GPlatesQtWidgets::ShapefileAttributeWidget`

| Member | Kind | Type | Access | Description |
|---|---|---|---|---|
| `ShapefileAttributeWidget( QWidget *parent_, const QString &filename, const QStringList &field_names, QMap<QString,QString> &model_to_attribute_map, bool remapping = false)` | constructor | `None` | public | — |
| `setup()` | method | `void` | public | Set up the combo boxes with fields from the shapefile. |
| `reset_fields()` | method | `void` | public | Reset the combo boxes to the state they were in when the dialog was created. |
| `accept_fields()` | method | `void` | public | Use the current state of the combo boxes to build up the shapefile-attribute-to-model-property map. |
| `d_filename` | field | `QString` | private | — |
| `d_field_names` | field | `QStringList` | private | The attribute field names obtained from the ShapefileReader. |
| `d_model_to_attribute_map` | field | `QMap<QString,QString>` | private | A map of the model property to the shapefile attribute. |
| `d_default_fields` | field | `QStringList` | private | The default names for the model fields. |
| `d_combo_reset_map` | field | `std::vector<int>` | private | The combo box settings. |

## Free functions and macros

| Name | Kind | Type / body | Description |
|---|---|---|---|
| `display_qmap( QMap< QString,QString > map)` | function | `void` | — |
| `display_field_names( QStringList names)` | function | `void` | — |
| `fill_fields_from_default_list( QStringList &default_fields)` | function | `void` | Fills the QStringList default\_fields with field names from the list of default\_attribute\_names defined in "PropertyMapper.h" |
| `fill_fields_from_qmap( QStringList &default_fields, const QMap<QString,QString> &model_to_attribute_map, const QStringList &field_names)` | function | `void` | Fills the QStringList default\_fields with the field names from the QMap\<QString,QString\> model\_to\_attribute\_map. |
| `GPLATES_QTWIDGETS_SHAPEFILEATTRIBUTEWIDGET_H` | macro | `None` | — |

## Notes

[[[PROSE notes unit=qt-widgets/ShapefileAttributeWidget tier=2]]]
Replace this whole block, markers included, with invariants, ownership, threading or gotchas that are not visible in the tables. Write *None.* if there is nothing worth saying.
[[[/PROSE]]]

## Used by

| Unit | Component | References |
|---|---|---|
| [qt-widgets/ShapefileFileFormatConfigurationDialog](ShapefileFileFormatConfigurationDialog.md) | qt-widgets | 6 |
| [qt-widgets/ShapefileAttributeMapperDialog](ShapefileAttributeMapperDialog.md) | qt-widgets | 5 |
| [qt-widgets/ShapefileAttributeRemapperDialog](ShapefileAttributeRemapperDialog.md) | qt-widgets | 5 |
| [qt-widgets/ManageFeatureCollectionsEditConfigurations](ManageFeatureCollectionsEditConfigurations.md) | qt-widgets | 1 |

## Related

**Qt Designer forms**

| Form class | Base widget | Title | Widgets |
|---|---|---|---|
| `ShapefileAttributeWidget` | `QWidget` | Form | 33 |


## Explore

Run these from the `gplates-code` skill directory:

```bash
python scripts/gpq.py file src/qt-widgets/ShapefileAttributeWidget.h
python scripts/gpq.py def GPlatesQtWidgets::ShapefileAttributeWidget --body
python scripts/gpq.py uses ShapefileAttributeWidget --kind class
python scripts/gpq.py hier ShapefileAttributeWidget
```
