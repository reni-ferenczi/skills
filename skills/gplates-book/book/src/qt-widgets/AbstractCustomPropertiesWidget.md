# AbstractCustomPropertiesWidget

[Book TOC](../../TOC.md) · [qt-widgets](../../components/qt-widgets.md) · cluster Community 1711 · tier 3

| Source file | Kind | Lines |
|---|---|---|
| `src/qt-widgets/AbstractCustomPropertiesWidget.h` | C++ | 71 |

## Overview

Abstract base class for feature-specific property widget behaviour. Subclasses override `do_geometry_tasks()` to apply geometry-based transformations to features at a given reconstruction time, with the base implementation returning the input geometry unchanged. Allows feature property editing to handle domain-specific geometry customization without embedding logic in the main dialog code.

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

*None.*

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
