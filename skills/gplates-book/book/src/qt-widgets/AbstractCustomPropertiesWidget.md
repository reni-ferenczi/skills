# AbstractCustomPropertiesWidget

[Book TOC](../../TOC.md) · [qt-widgets](../../components/qt-widgets.md) · cluster Community 1711 · tier 3

| Source file | Kind | Lines |
|---|---|---|
| `src/qt-widgets/AbstractCustomPropertiesWidget.h` | C++ | 71 |

## Overview

[[[PROSE overview unit=qt-widgets/AbstractCustomPropertiesWidget tier=3]]]
Replace this whole block, markers included, with 1-3 paragraphs: what this unit is, why it exists, and how it fits the surrounding design. Do not restate the tables below.
[[[/PROSE]]]

## Declared types

| Name | Kind | Bases | Template | Subclasses | Description |
|---|---|---|---|---|---|
| [`GPlatesQtWidgets::AbstractCustomPropertiesWidget`](#gplatesqtwidgetsabstractcustompropertieswidget) | class | `QWidget` | — | 1 | An abstract base class for special handling of feature properties. |

## Members

### `GPlatesQtWidgets::AbstractCustomPropertiesWidget`

| Member | Kind | Type | Access | Description |
|---|---|---|---|---|
| `AbstractCustomPropertiesWidget( QWidget *parent_ = NULL)` | constructor | `None` | public | — |
| `~AbstractCustomPropertiesWidget()` | destructor | `None` | public | — |
| `do_geometry_tasks( const GPlatesMaths::GeometryOnSphere::non_null_ptr_to_const_type &reconstruction_time_geometry_, const GPlatesModel::FeatureHandle::weak_ref &feature_handle)` | method | `GPlatesMaths::GeometryOnSphere::non_null_ptr_to_const_type` | public | — |

## Free functions and macros

| Name | Kind | Type / body | Description |
|---|---|---|---|
| `GPLATES_QTWIDGETS_ABSTRACTCUSTOMPROPERTIESWIDGET_H` | macro | `None` | — |

## Notes

[[[PROSE notes unit=qt-widgets/AbstractCustomPropertiesWidget tier=3]]]
Replace this whole block, markers included, with invariants, ownership, threading or gotchas that are not visible in the tables. Write *None.* if there is nothing worth saying.
[[[/PROSE]]]

## Used by

| Unit | Component | References |
|---|---|---|
| [qt-widgets/FlowlinePropertiesWidget](FlowlinePropertiesWidget.md) | qt-widgets | 5 |
| [qt-widgets/CreateFeatureDialog](CreateFeatureDialog.md) | qt-widgets | 3 |

## Related

*None.*

## Explore

Run these from the `gplates-code` skill directory:

```bash
python scripts/gpq.py file src/qt-widgets/AbstractCustomPropertiesWidget.h
python scripts/gpq.py def GPlatesQtWidgets::AbstractCustomPropertiesWidget --body
python scripts/gpq.py uses AbstractCustomPropertiesWidget --kind class
python scripts/gpq.py hier AbstractCustomPropertiesWidget
```
