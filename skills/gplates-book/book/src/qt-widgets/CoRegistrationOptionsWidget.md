# CoRegistrationOptionsWidget

[Book TOC](../../TOC.md) · [qt-widgets](../../components/qt-widgets.md) · cluster Community 911 · tier 3

| Source file | Kind | Lines |
|---|---|---|
| `src/qt-widgets/CoRegistrationOptionsWidget.h` | C++ | 226 |
| `src/qt-widgets/CoRegistrationOptionsWidgetUi.ui` | Qt form | 51 |

## Overview

Displays configuration and results options for co-registration layers in the visual layers panel. It inherits from `LayerOptionsWidget` and hosts two buttons: one to open a `CoRegistrationLayerConfigurationDialog` for adjusting co-registration parameters, and another to view results in a `CoRegistrationResultTableDialog`. The result viewer button is disabled unless the layer has input seed data to process.

## Declared types

| Name | Kind | Bases | Template | Subclasses | Description |
|---|---|---|---|---|---|
| [`GPlatesQtWidgets::CoRegistrationOptionsWidget`](#gplatesqtwidgetscoregistrationoptionswidget) | class | [`LayerOptionsWidget`](LayerOptionsWidget.md)<br>`Ui_CoRegistrationOptionsWidget` | — | 0 | CoRegistrationOptionsWidget is used to show additional options for co-registration layers in the visual layers widget. |

## Members

### `GPlatesQtWidgets::CoRegistrationOptionsWidget`

| Member | Kind | Type | Access | Description |
|---|---|---|---|---|
| `create( GPlatesAppLogic::ApplicationState &application_state, GPlatesPresentation::ViewState &view_state, ViewportWindow *viewport_window, QWidget *parent_)` | method | `LayerOptionsWidget` | public | — |
| `set_data( const boost::weak_ptr<GPlatesPresentation::VisualLayer> &visual_layer)` | method | `void` | public | — |
| `handle_co_registration_configuration_button_clicked()` | method | `void` | private | — |
| `handle_view_result_button_clicked()` | method | `void` | private | — |
| `CoRegistrationOptionsWidget( GPlatesAppLogic::ApplicationState &application_state, GPlatesPresentation::ViewState &view_state, ViewportWindow *viewport_window, QWidget *parent_)` | constructor | `None` | private | — |
| `d_application_state` | field | `GPlatesAppLogic::ApplicationState` | private | — |
| `d_view_state` | field | `GPlatesPresentation::ViewState` | private | — |
| `d_viewport_window` | field | `ViewportWindow` | private | — |
| `d_current_visual_layer` | field | `boost::weak_ptr<GPlatesPresentation::VisualLayer>` | private | The visual layer for which we are currently displaying options. |
| `d_coreg_layer_config_dialog` | field | `boost::shared_ptr<CoRegistrationLayerConfigurationDialog>` | private | — |
| `d_result_dialog` | field | `boost::shared_ptr<CoRegistrationResultTableDialog>` | private | — |

## Free functions and macros

| Name | Kind | Type / body | Description |
|---|---|---|---|
| `GPLATES_QTWIDGETS_COREGISTRATIONOPTIONSWIDGET_H` | macro | `None` | — |

## Notes

*None.*

## Used by

| Unit | Component | References |
|---|---|---|
| [presentation/VisualLayerRegistry](../presentation/VisualLayerRegistry.md) | presentation | 2 |

## Related

**Qt Designer forms**

| Form class | Base widget | Title | Widgets |
|---|---|---|---|
| `CoRegistrationOptionsWidget` | `QWidget` | Layers | 3 |

**Qt signal/slot connections** (2 in this unit)

| Sender | Signal | Receiver | Slot |
|---|---|---|---|
| `co_registration_configuration_button` | `clicked()` | `this` | `handle_co_registration_configuration_button_clicked()` |
| `view_result_button` | `clicked()` | `this` | `handle_view_result_button_clicked()` |


## Explore

Run these from the `gplates-code` skill directory:

```bash
python scripts/gpq.py file src/qt-widgets/CoRegistrationOptionsWidget.h
python scripts/gpq.py def GPlatesQtWidgets::CoRegistrationOptionsWidget --body
python scripts/gpq.py uses CoRegistrationOptionsWidget --kind class
python scripts/gpq.py hier CoRegistrationOptionsWidget
```
