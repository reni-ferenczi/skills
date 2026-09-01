# ConfigureVelocityLegendOverlayDialog

[Book TOC](../../TOC.md) · [qt-widgets](../../components/qt-widgets.md) · cluster Community 587 · tier 3

| Source file | Kind | Lines |
|---|---|---|
| `src/qt-widgets/ConfigureVelocityLegendOverlayDialog.h` | C++ | 174 |
| `src/qt-widgets/ConfigureVelocityLegendOverlayDialog.cc` | C++ | 276 |
| `src/qt-widgets/ConfigureVelocityLegendOverlayDialogUi.ui` | Qt form | 390 |

## Overview

Provides a dialog and helper widget for configuring the appearance of velocity legend overlays on the map. `ConfigureVelocityLegendOverlayDialog` wraps a Qt Designer form to present controls for arrow colour, scale text colour, background colour, font selection, and scale range. `ColourButton` is a custom colour button that opens a `QColorDialog` preserving alpha values, used elsewhere in the codebase that need to set colours with transparency.

## Declared types

| Name | Kind | Bases | Template | Subclasses | Description |
|---|---|---|---|---|---|
| [`GPlatesQtWidgets::ColourButton`](#gplatesqtwidgetscolourbutton) | class | `QToolButton` | — | 0 | The ColourButton class The ChooseColourButton class (used elsewhere in GPlates) uses the static function getColour which resets the Alpha value each time it's called.This version of a colour button instantiates a QColorDialog which allows ... |
| [`GPlatesQtWidgets::ConfigureVelocityLegendOverlayDialog`](#gplatesqtwidgetsconfigurevelocitylegendoverlaydialog) | class | [`GPlatesDialog`](GPlatesDialog.md)<br>`Ui_ConfigureVelocityLegendOverlayDialog` | — | 0 | — |

## Members

### `GPlatesQtWidgets::ColourButton`

| Member | Kind | Type | Access | Description |
|---|---|---|---|---|
| `ColourButton( QWidget *parent_ = NULL)` | constructor | `None` | public | — |
| `set_colour( const GPlatesGui::Colour &colour)` | method | `void` | public | Set the colour. |
| `colour_changed( GPlatesQtWidgets::ColourButton &)` | method | `void` | public | Emitted if user changes colour via GUI or if set\_colour is explicitly called. |
| `handle_clicked()` | method | `void` | private | — |
| `d_colour` | field | `GPlatesGui::Colour` | private | — |

### `GPlatesQtWidgets::ConfigureVelocityLegendOverlayDialog`

| Member | Kind | Type | Access | Description |
|---|---|---|---|---|
| `ConfigureVelocityLegendOverlayDialog( GPlatesPresentation::ViewState &view_state, QWidget *parent_ = NULL)` | constructor | `None` | public | — |
| `exec( GPlatesGui::VelocityLegendOverlaySettings &settings)` | method | `int` | public | Shows the dialog modal to allow the user to modify the text overlay settings passed in as a mutable reference, settings. |
| `handle_radio_buttons_checked()` | method | `void` | private | — |
| `populate( const GPlatesGui::VelocityLegendOverlaySettings &settings)` | method | `void` | private | populate - fill the dialog's widgets from the values in |
| `save( GPlatesGui::VelocityLegendOverlaySettings &settings)` | method | `void` | private | save - fill |
| `d_scale_text_colour_button` | field | `GPlatesQtWidgets::ColourButton` | private | — |
| `d_arrow_colour_button` | field | `GPlatesQtWidgets::ColourButton` | private | — |
| `d_background_colour_button` | field | `GPlatesQtWidgets::ColourButton` | private | — |
| `d_scale_text_font_button` | field | `ChooseFontButton` | private | — |
| `d_visual_layers_combo_box` | field | `VisualLayersComboBox` | private | — |
| `d_fixed_scale_help_dialog` | field | `InformationDialog` | private | — |
| `s_fixed_scale_text` | field | `QString` | private | — |
| `d_max_arrow_length_help_dialog` | field | `InformationDialog` | private | — |
| `s_max_arrow_length_text` | field | `QString` | private | — |

## Free functions and macros

| Name | Kind | Type / body | Description |
|---|---|---|---|
| `s_fixed_scale_text` | variable | `QString` | — |
| `s_max_arrow_length_text` | variable | `QString` | — |
| `GPLATES_QTWIDGETS_CONFIGUREVELOCITYLEGENDOVERLAYDIALOG_H` | macro | `None` | — |

## Notes

*None.*

## Used by

| Unit | Component | References |
|---|---|---|
| [gui/Dialogs](../gui/Dialogs.md) | gui | 1 |

## Related

**Qt Designer forms**

| Form class | Base widget | Title | Widgets |
|---|---|---|---|
| `ConfigureVelocityLegendOverlayDialog` | `QDialog` | Configure Velocity Legend Overlay | 28 |

**Qt signal/slot connections** (8 in this unit)

| Sender | Signal | Receiver | Slot |
|---|---|---|---|
| `main_buttonbox` | `accepted()` | `this` | `accept()` |
| `main_buttonbox` | `rejected()` | `this` | `reject()` |
| `radio_button_arrow_length` | `clicked()` | `this` | `handle_radio_buttons_checked()` |
| `radio_button_scale` | `clicked()` | `this` | `handle_radio_buttons_checked()` |
| `button_help_fixed_scale` | `clicked()` | `d_fixed_scale_help_dialog` | `show()` |
| `button_help_maximum_length` | `clicked()` | `d_max_arrow_length_help_dialog` | `show()` |
| `d_visual_layers_combo_box` | `selected_visual_layer_changed( boost::weak_ptr<GPlatesPresentation::VisualLayer>)` | `this` | `handle_visual_layer_changed()` |
| `this` | `clicked()` | `this` | `handle_clicked()` |


## Explore

Run these from the `gplates-code` skill directory:

```bash
python scripts/gpq.py file src/qt-widgets/ConfigureVelocityLegendOverlayDialog.h
python scripts/gpq.py def GPlatesQtWidgets::ConfigureVelocityLegendOverlayDialog --body
python scripts/gpq.py uses ConfigureVelocityLegendOverlayDialog --kind class
python scripts/gpq.py hier ConfigureVelocityLegendOverlayDialog
```
