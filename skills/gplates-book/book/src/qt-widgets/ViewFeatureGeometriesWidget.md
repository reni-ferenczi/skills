# ViewFeatureGeometriesWidget

[Book TOC](../../TOC.md) · [qt-widgets](../../components/qt-widgets.md) · cluster Community 1115 · tier 3

| Source file | Kind | Lines |
|---|---|---|
| `src/qt-widgets/ViewFeatureGeometriesWidget.h` | C++ | 133 |
| `src/qt-widgets/ViewFeatureGeometriesWidget.cc` | C++ | 122 |
| `src/qt-widgets/ViewFeatureGeometriesWidgetUi.ui` | Qt form | 143 |

## Overview

Displays the geometries of a feature in a tree view, including its reconstructed form at the current reconstruction time. Used within the feature properties dialog to let users inspect the feature's geometry. The widget watches for changes to the focused feature and reconstruction time, and updates its display accordingly. Geometry population is deferred until the widget becomes visible to avoid unnecessary work when it is hidden.

## Declared types

| Name | Kind | Bases | Template | Subclasses | Description |
|---|---|---|---|---|---|
| [`GPlatesQtWidgets::ViewFeatureGeometriesWidget`](#gplatesqtwidgetsviewfeaturegeometrieswidget) | class | `QWidget`<br>`Ui_ViewFeatureGeometriesWidget` | — | 0 | — |

## Members

### `GPlatesQtWidgets::ViewFeatureGeometriesWidget`

| Member | Kind | Type | Access | Description |
|---|---|---|---|---|
| `ViewFeatureGeometriesWidget( GPlatesPresentation::ViewState &view_state_, QWidget *parent_ = NULL)` | constructor | `None` | public | — |
| `~ViewFeatureGeometriesWidget()` | destructor | `None` | public | — |
| `reset()` | method | `void` | public | Clears the geometry display in preparation for a new set of geometries. |
| `refresh_display()` | method | `void` | public | Updates the dialog to redisplay the geometry of the current Feature. |
| `edit_feature( GPlatesModel::FeatureHandle::weak_ref feature_ref, GPlatesAppLogic::ReconstructionGeometry::maybe_null_ptr_to_const_type focused_rg)` | method | `void` | public | Updates the dialog to display the geometry of a new Feature. |
| `showEvent( QShowEvent *event_)` | method | `void` | protected | — |
| `d_application_state_ptr` | field | `GPlatesAppLogic::ApplicationState` | private | This is the reconstruction generator which is used to obtain the reconstruction in order to iterate over RFGs. |
| `d_feature_focus_ptr` | field | `GPlatesGui::FeatureFocus` | private | This is the feature focus which tracks changes to the currently focused feature. |
| `d_feature_ref` | field | `GPlatesModel::FeatureHandle::weak_ref` | private | This is the feature we are displaying. |
| `d_focused_rg` | field | `GPlatesAppLogic::ReconstructionGeometry::maybe_null_ptr_to_const_type` | private | The ReconstructionGeometry associated with the feature that is in focus. |
| `d_populate_geometry_tree_when_visible` | field | `bool` | private | The geometry tree is only populated when this widget is visible. |

## Free functions and macros

| Name | Kind | Type / body | Description |
|---|---|---|---|
| `GPLATES_QTWIDGETS_VIEWFEATUREGEOMETRIESWIDGET_H` | macro | `None` | — |

## Notes

*None.*

## Used by

| Unit | Component | References |
|---|---|---|
| [qt-widgets/FeaturePropertiesDialog](FeaturePropertiesDialog.md) | qt-widgets | 3 |

## Related

**Qt Designer forms**

| Form class | Base widget | Title | Widgets |
|---|---|---|---|
| `ViewFeatureGeometriesWidget` | `QWidget` | Edit Feature Geometries | 7 |

**Qt signal/slot connections** (1 in this unit)

| Sender | Signal | Receiver | Slot |
|---|---|---|---|
| `d_application_state_ptr` | `reconstructed(GPlatesAppLogic::ApplicationState &)` | `this` | `refresh_display()` |


## Explore

Run these from the `gplates-code` skill directory:

```bash
python scripts/gpq.py file src/qt-widgets/ViewFeatureGeometriesWidget.h
python scripts/gpq.py def GPlatesQtWidgets::ViewFeatureGeometriesWidget --body
python scripts/gpq.py uses ViewFeatureGeometriesWidget --kind class
python scripts/gpq.py hier ViewFeatureGeometriesWidget
```
