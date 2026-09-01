# FlowlinePropertiesWidget

[Book TOC](../../TOC.md) · [qt-widgets](../../components/qt-widgets.md) · cluster Community 1716 · tier 3

| Source file | Kind | Lines |
|---|---|---|
| `src/qt-widgets/FlowlinePropertiesWidget.h` | C++ | 78 |
| `src/qt-widgets/FlowlinePropertiesWidget.cc` | C++ | 118 |
| `src/qt-widgets/FlowlinePropertiesWidgetUi.ui` | Qt form | 93 |

## Overview

A custom properties widget for flowline features, allowing users to define the role of a selected point in creating a flowline. The widget presents three options: the point is the spreading centre, the left endpoint, or the right endpoint of the flowline. If the user selects an endpoint, the widget uses `FlowlineUtils` to compute the equivalent centre point that would yield the desired endpoint after plate reconstruction at the current time.

The geometry correction respects the flowline properties (left and right plate IDs, valid time period) extracted from the feature handle.

## Declared types

| Name | Kind | Bases | Template | Subclasses | Description |
|---|---|---|---|---|---|
| [`GPlatesQtWidgets::FlowlinePropertiesWidget`](#gplatesqtwidgetsflowlinepropertieswidget) | class | [`AbstractCustomPropertiesWidget`](AbstractCustomPropertiesWidget.md)<br>`Ui_FlowlinePropertiesWidget` | — | 0 | — |

## Members

### `GPlatesQtWidgets::FlowlinePropertiesWidget`

| Member | Kind | Type | Access | Description |
|---|---|---|---|---|
| `FlowlinePropertiesWidget( const GPlatesAppLogic::ApplicationState &application_state, QWidget *parent_ = NULL)` | constructor | `None` | public | — |
| `~FlowlinePropertiesWidget()` | destructor | `None` | public | — |
| `do_geometry_tasks( const GPlatesMaths::GeometryOnSphere::non_null_ptr_to_const_type &reconstruction_time_geometry_, const GPlatesModel::FeatureHandle::weak_ref &feature_ref)` | method | `GPlatesMaths::GeometryOnSphere::non_null_ptr_to_const_type` | public | — |
| `d_application_state` | field | `GPlatesAppLogic::ApplicationState` | private | Application state, for getting reconstruction time. |

## Free functions and macros

| Name | Kind | Type / body | Description |
|---|---|---|---|
| `GPLATES_QTWIDGETS_FLOWLINEPROPERTIESWIDGET_H` | macro | `None` | — |

## Notes

*None.*

## Used by

| Unit | Component | References |
|---|---|---|
| [qt-widgets/CreateFeatureDialog](CreateFeatureDialog.md) | qt-widgets | 2 |

## Related

**Qt Designer forms**

| Form class | Base widget | Title | Widgets |
|---|---|---|---|
| `FlowlinePropertiesWidget` | `QWidget` | Form | 6 |


## Explore

Run these from the `gplates-code` skill directory:

```bash
python scripts/gpq.py file src/qt-widgets/FlowlinePropertiesWidget.h
python scripts/gpq.py def GPlatesQtWidgets::FlowlinePropertiesWidget --body
python scripts/gpq.py uses FlowlinePropertiesWidget --kind class
python scripts/gpq.py hier FlowlinePropertiesWidget
```
