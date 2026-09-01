# ShapefilePropertyMapper

[Book TOC](../../TOC.md) · [qt-widgets](../../components/qt-widgets.md) · cluster Community 1034 · tier 3

| Source file | Kind | Lines |
|---|---|---|
| `src/qt-widgets/ShapefilePropertyMapper.h` | C++ | 101 |
| `src/qt-widgets/ShapefilePropertyMapper.cc` | C++ | 88 |

## Overview

[[[PROSE overview unit=qt-widgets/ShapefilePropertyMapper tier=3]]]
Replace this whole block, markers included, with 1-3 paragraphs: what this unit is, why it exists, and how it fits the surrounding design. Do not restate the tables below.
[[[/PROSE]]]

## Declared types

| Name | Kind | Bases | Template | Subclasses | Description |
|---|---|---|---|---|---|
| [`GPlatesQtWidgets::ShapefilePropertyMapper`](#gplatesqtwidgetsshapefilepropertymapper) | class | [`GPlatesFileIO::PropertyMapper`](../file-io/PropertyMapper.md) | — | 0 | — |

## Members

### `GPlatesQtWidgets::ShapefilePropertyMapper`

| Member | Kind | Type | Access | Description |
|---|---|---|---|---|
| `ShapefilePropertyMapper( QWidget *parent_window_ptr)` | constructor | `None` | public | — |
| `~ShapefilePropertyMapper()` | destructor | `None` | public | — |
| `map_properties( QString &filename, QStringList &field_names, QMap<QString,QString> &model_to_attribute_map, bool remapping)` | method | `bool` | public | Fills model\_to\_attribute\_map. |
| `d_parent_window_ptr` | field | `QWidget` | private | The Qt window which will be the parent of the dialogs. |
| `ShapefilePropertyMapper( const ShapefilePropertyMapper &other)` | constructor | `None` | private | Make copy and assignment private. |
| `operator=` | field | `ShapefilePropertyMapper` | private | — |
| `map_initial_properties( QString &filename, QStringList &field_names, QMap<QString,QString> &model_to_attribute_map, QWidget *parent_)` | method | `bool` | private | Obtains the initial shapefile attribute mapping from the \<name\>.shp.gplates.xml file, if it exists. |
| `map_remapped_properties( QString &filename, QStringList &field_names, QMap<QString,QString> &model_to_attribute_map, QWidget *parent_)` | method | `bool` | private | Obtains the shapefile attribute mapping from the \<name\>.shp.gplates.xml, and opens the ShapefileAttributeRemapping dialog to allow the user to change the mapping. |

## Free functions and macros

| Name | Kind | Type / body | Description |
|---|---|---|---|
| `GPLATES_QTWIDGETS_SHAPEFILEPROPERTYMAPPER_H` | macro | `None` | — |

## Notes

[[[PROSE notes unit=qt-widgets/ShapefilePropertyMapper tier=3]]]
Replace this whole block, markers included, with invariants, ownership, threading or gotchas that are not visible in the tables. Write *None.* if there is nothing worth saying.
[[[/PROSE]]]

## Used by

| Unit | Component | References |
|---|---|---|
| [presentation/Application](../presentation/Application.md) | presentation | 3 |
| [qt-widgets/ShapefileAttributeMapperDialog](ShapefileAttributeMapperDialog.md) | qt-widgets | 1 |
| [qt-widgets/ShapefileAttributeRemapperDialog](ShapefileAttributeRemapperDialog.md) | qt-widgets | 1 |
| [qt-widgets/ShapefileAttributeWidget](ShapefileAttributeWidget.md) | qt-widgets | 1 |

## Related

*None.*

## Explore

Run these from the `gplates-code` skill directory:

```bash
python scripts/gpq.py file src/qt-widgets/ShapefilePropertyMapper.h
python scripts/gpq.py def GPlatesQtWidgets::ShapefilePropertyMapper --body
python scripts/gpq.py uses ShapefilePropertyMapper --kind class
python scripts/gpq.py hier ShapefilePropertyMapper
```
