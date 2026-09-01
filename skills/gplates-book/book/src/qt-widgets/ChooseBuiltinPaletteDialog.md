# ChooseBuiltinPaletteDialog

[Book TOC](../../TOC.md) · [qt-widgets](../../components/qt-widgets.md) · cluster Community 30 · tier 3

| Source file | Kind | Lines |
|---|---|---|
| `src/qt-widgets/ChooseBuiltinPaletteDialog.h` | C++ | 192 |
| `src/qt-widgets/ChooseBuiltinPaletteDialog.cc` | C++ | 643 |
| `src/qt-widgets/ChooseBuiltinPaletteDialogUi.ui` | Qt form | 687 |

## Overview

[[[PROSE overview unit=qt-widgets/ChooseBuiltinPaletteDialog tier=3]]]
Replace this whole block, markers included, with 1-3 paragraphs: what this unit is, why it exists, and how it fits the surrounding design. Do not restate the tables below.
[[[/PROSE]]]

## Declared types

| Name | Kind | Bases | Template | Subclasses | Description |
|---|---|---|---|---|---|
| [`GPlatesQtWidgets::ChooseBuiltinPaletteDialog`](#gplatesqtwidgetschoosebuiltinpalettedialog) | class | [`GPlatesDialog`](GPlatesDialog.md)<br>`Ui_ChooseBuiltinPaletteDialog` | — | 0 | — |

## Members

### `GPlatesQtWidgets::ChooseBuiltinPaletteDialog`

| Member | Kind | Type | Access | Description |
|---|---|---|---|---|
| `ChooseBuiltinPaletteDialog( const GPlatesGui::BuiltinColourPaletteType::Parameters &builtin_parameters, QWidget *parent_ = NULL)` | constructor | `None` | public | — |
| `builtin_colour_palette_selected( const GPlatesGui::BuiltinColourPaletteType &builtin_colour_palette_type)` | method | `void` | public | NOTE: all signals/slots should use namespace scope for all arguments otherwise differences between signals and slots will cause Qt to not be able to connect them at runtime. |
| `builtin_parameters_changed( const GPlatesGui::BuiltinColourPaletteType::Parameters &builtin_parameters)` | method | `void` | public | — |
| `handle_colorbrewer_sequential_classes_changed( int value)` | method | `void` | private | — |
| `handle_colorbrewer_diverging_classes_changed( int value)` | method | `void` | private | — |
| `handle_colorbrewer_discrete_check_box_changed( int state)` | method | `void` | private | — |
| `handle_invert_check_box_changed( int state)` | method | `void` | private | — |
| `handle_colour_scale_button_clicked( bool checked)` | method | `void` | private | — |
| `add_colour_scale_button( ColourScaleButton *colour_scale_button, QWidget *colour_scale_button_placeholder)` | method | `void` | private | — |
| `get_builtin_colour_palette_type( ColourScaleButton *colour_scale_button)` | method | `GPlatesGui::BuiltinColourPaletteType` | private | — |
| `create_palette_type( GPlatesGui::BuiltinColourPalettes::Age::Type age_type)` | method | `GPlatesGui::BuiltinColourPaletteType` | private | — |
| `create_palette_type( GPlatesGui::BuiltinColourPalettes::Topography::Type topography_type)` | method | `GPlatesGui::BuiltinColourPaletteType` | private | — |
| `create_palette_type( GPlatesGui::BuiltinColourPalettes::SCM::Type scm_type)` | method | `GPlatesGui::BuiltinColourPaletteType` | private | — |
| `create_palette_type( GPlatesGui::BuiltinColourPalettes::ColorBrewer::Sequential::Type sequential_type)` | method | `GPlatesGui::BuiltinColourPaletteType` | private | — |
| `create_palette_type( GPlatesGui::BuiltinColourPalettes::ColorBrewer::Diverging::Type diverging_type)` | method | `GPlatesGui::BuiltinColourPaletteType` | private | — |
| `re_populate_buttons( GPlatesGui::BuiltinColourPaletteType::PaletteType palette_type)` | method | `void` | private | — |
| `d_builtin_parameters` | field | `GPlatesGui::BuiltinColourPaletteType::Parameters` | private | — |
| `d_age_legacy_button` | field | `ColourScaleButton` | private | Age palettes. |
| `d_age_traditional_button` | field | `ColourScaleButton` | private | — |
| `d_age_modern_button` | field | `ColourScaleButton` | private | — |
| `d_topography_etopo1_button` | field | `ColourScaleButton` | private | Topography palettes. |
| `d_topography_geo_button` | field | `ColourScaleButton` | private | — |
| `d_topography_relief_button` | field | `ColourScaleButton` | private | — |
| `d_scm_batlow_button` | field | `ColourScaleButton` | private | SCM palettes. |
| `d_scm_hawaii_button` | field | `ColourScaleButton` | private | — |
| `d_scm_oslo_button` | field | `ColourScaleButton` | private | — |
| `d_scm_lapaz_button` | field | `ColourScaleButton` | private | — |
| `d_scm_lajolla_button` | field | `ColourScaleButton` | private | — |
| `d_scm_buda_button` | field | `ColourScaleButton` | private | — |
| `d_scm_davos_button` | field | `ColourScaleButton` | private | — |
| `d_scm_tokyo_button` | field | `ColourScaleButton` | private | — |
| `d_scm_vik_button` | field | `ColourScaleButton` | private | — |
| `d_scm_roma_button` | field | `ColourScaleButton` | private | — |
| `d_scm_broc_button` | field | `ColourScaleButton` | private | — |
| `d_scm_berlin_button` | field | `ColourScaleButton` | private | — |
| `d_scm_lisbon_button` | field | `ColourScaleButton` | private | — |
| `d_scm_bam_button` | field | `ColourScaleButton` | private | — |
| `d_scm_oleron_button` | field | `ColourScaleButton` | private | — |
| `d_scm_bukavu_button` | field | `ColourScaleButton` | private | — |
| `d_BuGn_button` | field | `ColourScaleButton` | private | ColorBrewer sequential multi-hue palettes. |
| `d_BuPu_button` | field | `ColourScaleButton` | private | — |
| `d_GnBu_button` | field | `ColourScaleButton` | private | — |
| `d_OrRd_button` | field | `ColourScaleButton` | private | — |
| `d_PuBu_button` | field | `ColourScaleButton` | private | — |
| `d_PuBuGn_button` | field | `ColourScaleButton` | private | — |
| `d_PuRd_button` | field | `ColourScaleButton` | private | — |
| `d_RdPu_button` | field | `ColourScaleButton` | private | — |
| `d_YlGn_button` | field | `ColourScaleButton` | private | — |
| `d_YlGnBu_button` | field | `ColourScaleButton` | private | — |
| `d_YlOrBr_button` | field | `ColourScaleButton` | private | — |
| `d_YlOrRd_button` | field | `ColourScaleButton` | private | — |
| `d_Blues_button` | field | `ColourScaleButton` | private | ColorBrewer sequential single hue palettes. |
| `d_Greens_button` | field | `ColourScaleButton` | private | — |
| `d_Greys_button` | field | `ColourScaleButton` | private | — |
| `d_Oranges_button` | field | `ColourScaleButton` | private | — |
| `d_Purples_button` | field | `ColourScaleButton` | private | — |
| `d_Reds_button` | field | `ColourScaleButton` | private | — |
| `d_BrBG_button` | field | `ColourScaleButton` | private | ColorBrewer diverging palettes. |
| `d_PiYG_button` | field | `ColourScaleButton` | private | — |
| `d_PRGn_button` | field | `ColourScaleButton` | private | — |
| `d_PuOr_button` | field | `ColourScaleButton` | private | — |
| `d_RdBu_button` | field | `ColourScaleButton` | private | — |
| `d_RdGy_button` | field | `ColourScaleButton` | private | — |
| `d_RdYlBu_button` | field | `ColourScaleButton` | private | — |
| `d_RdYlGn_button` | field | `ColourScaleButton` | private | — |
| `d_Spectral_button` | field | `ColourScaleButton` | private | — |

## Free functions and macros

| Name | Kind | Type / body | Description |
|---|---|---|---|
| `GPLATES_QT_WIDGETS_CHOOSEBUILTINPALETTEDIALOG_H` | macro | `None` | — |

## Notes

[[[PROSE notes unit=qt-widgets/ChooseBuiltinPaletteDialog tier=3]]]
Replace this whole block, markers included, with invariants, ownership, threading or gotchas that are not visible in the tables. Write *None.* if there is nothing worth saying.
[[[/PROSE]]]

## Used by

| Unit | Component | References |
|---|---|---|
| [qt-widgets/RemappedColourPaletteWidget](RemappedColourPaletteWidget.md) | qt-widgets | 2 |

## Related

**Qt Designer forms**

| Form class | Base widget | Title | Widgets |
|---|---|---|---|
| `ChooseBuiltinPaletteDialog` | `QDialog` | Choose Built-in Palette | 70 |

**Qt signal/slot connections** (6 in this unit)

| Sender | Signal | Receiver | Slot |
|---|---|---|---|
| `invert_checkbox` | `stateChanged(int)` | `this` | `handle_invert_check_box_changed(int)` |
| `colorbrewer_sequential_classes_spinbox` | `valueChanged(int)` | `this` | `handle_colorbrewer_sequential_classes_changed(int)` |
| `colorbrewer_diverging_classes_spinbox` | `valueChanged(int)` | `this` | `handle_colorbrewer_diverging_classes_changed(int)` |
| `colorbrewer_sequential_discrete_checkbox` | `stateChanged(int)` | `this` | `handle_colorbrewer_discrete_check_box_changed(int)` |
| `colorbrewer_diverging_discrete_checkbox` | `stateChanged(int)` | `this` | `handle_colorbrewer_discrete_check_box_changed(int)` |
| `colour_scale_button` | `clicked(bool)` | `this` | `handle_colour_scale_button_clicked(bool)` |


## Explore

Run these from the `gplates-code` skill directory:

```bash
python scripts/gpq.py file src/qt-widgets/ChooseBuiltinPaletteDialog.h
python scripts/gpq.py def GPlatesQtWidgets::ChooseBuiltinPaletteDialog --body
python scripts/gpq.py uses ChooseBuiltinPaletteDialog --kind class
python scripts/gpq.py hier ChooseBuiltinPaletteDialog
```
