# QueryFeaturePropertiesWidget

[Book TOC](../../TOC.md) · [qt-widgets](../../components/qt-widgets.md) · cluster Community 951 · tier 3

| Source file | Kind | Lines |
|---|---|---|
| `src/qt-widgets/QueryFeaturePropertiesWidget.h` | C++ | 146 |
| `src/qt-widgets/QueryFeaturePropertiesWidget.cc` | C++ | 254 |
| `src/qt-widgets/QueryFeaturePropertiesWidgetUi.ui` | Qt form | 262 |

## Overview

Widget that displays the properties of a selected feature in a tree layout. It shows reconstruction parameters (Euler pole, rotation angle, plate IDs, reconstruction time) and a tree of the feature's property-value structure. The widget automatically refreshes when reconstruction geometry changes via a connection to `ApplicationState::reconstructed()`, and uses a lazy-population optimization to avoid populating the tree while the widget is hidden.

## Declared types

| Name | Kind | Bases | Template | Subclasses | Description |
|---|---|---|---|---|---|
| [`GPlatesQtWidgets::QueryFeaturePropertiesWidget`](#gplatesqtwidgetsqueryfeaturepropertieswidget) | class | `QWidget`<br>`Ui_QueryFeaturePropertiesWidget` | — | 0 | — |

## Members

### `GPlatesQtWidgets::QueryFeaturePropertiesWidget`

| Member | Kind | Type | Access | Description |
|---|---|---|---|---|
| `QueryFeaturePropertiesWidget( GPlatesPresentation::ViewState &view_state_, QWidget *parent_ = NULL)` | constructor | `None` | public | — |
| `~QueryFeaturePropertiesWidget()` | destructor | `None` | public | — |
| `set_euler_pole( const QString &point_position)` | method | `void` | public | The parameter is a QString to enable us to pass the string "indeterminate". |
| `set_angle( const double &angle)` | method | `void` | public | — |
| `set_plate_id( unsigned long plate_id)` | method | `void` | public | — |
| `set_root_plate_id( unsigned long plate_id)` | method | `void` | public | — |
| `set_reconstruction_time( const double &recon_time)` | method | `void` | public | — |
| `property_tree` | field | `QTreeWidget` | public | — |
| `refresh_display()` | method | `void` | public | Updates the dialog to redisplay the geometry of the current Feature. |
| `display_feature( GPlatesModel::FeatureHandle::weak_ref feature_ref, GPlatesAppLogic::ReconstructionGeometry::maybe_null_ptr_to_const_type focused_rg)` | method | `void` | public | Updates the query widget to display properties of the given feature. |
| `showEvent( QShowEvent *event_)` | method | `void` | protected | — |
| `d_application_state_ptr` | field | `GPlatesAppLogic::ApplicationState` | private | This is the view state which is used to obtain the reconstruction root. |
| `d_feature_ref` | field | `GPlatesModel::FeatureHandle::weak_ref` | private | This is the feature we are displaying. |
| `d_focused_rg` | field | `GPlatesAppLogic::ReconstructionGeometry::maybe_null_ptr_to_const_type` | private | The ReconstructionGeometry associated with the feature that is in focus. |
| `d_populate_property_tree_when_visible` | field | `bool` | private | The property tree is only populated when this widget is visible. |

## Free functions and macros

| Name | Kind | Type / body | Description |
|---|---|---|---|
| `GPLATES_QTWIDGETS_QUERYFEATUREPROPERTIESWIDGET_H` | macro | `None` | — |

## Notes

The displayed feature ref `d_feature_ref` is a weak reference that must be checked for validity before use. The tree is populated only when the widget is visible, deferred by `d_populate_property_tree_when_visible`; callers should be prepared for the tree to remain unpopulated while the widget is hidden.

## Used by

| Unit | Component | References |
|---|---|---|
| [qt-widgets/FeaturePropertiesDialog](FeaturePropertiesDialog.md) | qt-widgets | 3 |

## Related

**Qt Designer forms**

| Form class | Base widget | Title | Widgets |
|---|---|---|---|
| `QueryFeaturePropertiesWidget` | `QWidget` | Query Feature Properties | 20 |

**Qt signal/slot connections** (1 in this unit)

| Sender | Signal | Receiver | Slot |
|---|---|---|---|
| `d_application_state_ptr` | `reconstructed(GPlatesAppLogic::ApplicationState &)` | `this` | `refresh_display()` |


## Explore

Run these from the `gplates-code` skill directory:

```bash
python scripts/gpq.py file src/qt-widgets/QueryFeaturePropertiesWidget.h
python scripts/gpq.py def GPlatesQtWidgets::QueryFeaturePropertiesWidget --body
python scripts/gpq.py uses QueryFeaturePropertiesWidget --kind class
python scripts/gpq.py hier QueryFeaturePropertiesWidget
```
