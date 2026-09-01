# ShapefileAttributeWidget

[Book TOC](../../TOC.md) · [qt-widgets](../../components/qt-widgets.md) · cluster Community 1337 · tier 2

| Source file | Kind | Lines |
|---|---|---|
| `src/qt-widgets/ShapefileAttributeWidget.h` | C++ | 90 |
| `src/qt-widgets/ShapefileAttributeWidget.cc` | C++ | 389 |
| `src/qt-widgets/ShapefileAttributeWidgetUi.ui` | Qt form | 307 |

## Overview

`ShapefileAttributeWidget` presents one combo box per GPlates model property (plate ID, feature type, begin/end age, name, description, feature ID, conjugate plate, reconstruction method, left/right plate, spreading asymmetry, geometry import time) and lets the user pick which shapefile attribute column, if any, supplies that property. `setup()` populates every combo box with a leading `<none>` entry followed by the shapefile's `d_field_names`, then pre-selects a default for each: it prefers an existing entry in the incoming `model_to_attribute_map` (via `fill_fields_from_qmap()`), falling back to the hard-coded `ShapefileAttributes::default_attribute_field_names` (via `fill_fields_from_default_list()`) when the map is empty or a mapped attribute is missing from the file's field list. The `remapping` constructor flag disables the feature-type and feature-ID combo boxes, since those two properties cannot be changed once a feature collection has already been imported.

`accept_fields()` reads the combo boxes back into `d_model_to_attribute_map` (a reference the widget does not own), skipping any still set to `<none>`; `reset_fields()` restores the selections captured in `d_combo_reset_map` at the end of `setup()`, undoing whatever the user changed without re-deriving the defaults.

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

- `d_field_names` and `d_model_to_attribute_map` are stored as references to caller-owned objects, not copies; the widget must not outlive them, and `accept_fields()` mutates the caller's map in place.
- The feature-type default lookup has a hard-coded fallback: if the configured default field (normally `GPGIM_TYPE`) is not present in the shapefile, the code also tries a literal `"TYPE"` column before giving up. A comment in `setup()` flags this as a stopgap pending a proper list of fallback default names per property.

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
