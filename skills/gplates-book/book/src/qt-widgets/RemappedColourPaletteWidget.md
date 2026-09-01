# RemappedColourPaletteWidget

[Book TOC](../../TOC.md) · [qt-widgets](../../components/qt-widgets.md) · cluster Community 445 · tier 3

| Source file | Kind | Lines |
|---|---|---|
| `src/qt-widgets/RemappedColourPaletteWidget.h` | C++ | 175 |
| `src/qt-widgets/RemappedColourPaletteWidget.cc` | C++ | 371 |
| `src/qt-widgets/RemappedColourPaletteWidgetUi.ui` | Qt form | 359 |

## Overview

This widget manages the selection and configuration of color palettes used to visualize scalar data. It provides controls for choosing between built-in palettes and loading custom CPT (Color Palette Table) files, and displays a visual preview of the selected palette via `ColourScaleWidget`. The widget's main purpose is to map a range of data values to colors for rendering scalar fields and coverages.

A key feature is the ability to remap the palette's value range in two ways: by explicitly setting min and max bounds, or by automatically calculating bounds based on the layer's scalar statistics (min/max or mean plus/minus standard deviation). The widget emits signals when users change palette selections or range settings, allowing parent widgets like `ReconstructScalarCoverageLayerOptionsWidget` to persist these choices to the layer's visual parameters.

## Declared types

| Name | Kind | Bases | Template | Subclasses | Description |
|---|---|---|---|---|---|
| [`GPlatesQtWidgets::RemappedColourPaletteWidget`](#gplatesqtwidgetsremappedcolourpalettewidget) | class | `QWidget`<br>`Ui_RemappedColourPaletteWidget` | — | 0 | A widget containing a colour palette and options to remap the palette range according to min/max or mean/standard-deviation. |

## Members

### `GPlatesQtWidgets::RemappedColourPaletteWidget`

| Member | Kind | Type | Access | Description |
|---|---|---|---|---|
| `RemappedColourPaletteWidget( GPlatesPresentation::ViewState &view_state, ViewportWindow *viewport_window, QWidget *parent_)` | constructor | `None` | public | — |
| `set_parameters( const GPlatesPresentation::RemappedColourPaletteParameters &parameters)` | method | `void` | public | Set parameters to configure the state of the widget. |
| `select_palette_filename_button_clicked()` | method | `void` | public | NOTE: all signals/slots should use namespace scope for all arguments otherwise differences between signals and slots will cause Qt to not be able to connect them at runtime. |
| `use_default_palette_button_clicked()` | method | `void` | public | — |
| `builtin_colour_palette_selected( const GPlatesGui::BuiltinColourPaletteType &builtin_colour_palette_type)` | method | `void` | public | — |
| `builtin_parameters_changed( const GPlatesGui::BuiltinColourPaletteType::Parameters &builtin_parameters)` | method | `void` | public | — |
| `range_check_box_changed( int)` | method | `void` | public | — |
| `min_line_editing_finished( double)` | method | `void` | public | — |
| `max_line_editing_finished( double)` | method | `void` | public | — |
| `range_restore_min_max_button_clicked()` | method | `void` | public | — |
| `range_restore_mean_deviation_button_clicked()` | method | `void` | public | — |
| `range_restore_mean_deviation_spinbox_changed( double value)` | method | `void` | public | — |
| `handle_select_palette_filename_button_clicked()` | method | `void` | private | — |
| `handle_use_default_palette_button_clicked()` | method | `void` | private | — |
| `open_choose_builtin_palette_dialog()` | method | `void` | private | — |
| `handle_builtin_colour_palette_selected( const GPlatesGui::BuiltinColourPaletteType &builtin_colour_palette_type)` | method | `void` | private | — |
| `handle_builtin_parameters_changed( const GPlatesGui::BuiltinColourPaletteType::Parameters &builtin_parameters)` | method | `void` | private | — |
| `handle_range_check_box_changed( int)` | method | `void` | private | — |
| `handle_min_line_editing_finished()` | method | `void` | private | — |
| `handle_max_line_editing_finished()` | method | `void` | private | — |
| `handle_range_restore_min_max_button_clicked()` | method | `void` | private | — |
| `handle_range_restore_mean_deviation_button_clicked()` | method | `void` | private | — |
| `handle_range_restore_mean_deviation_spinbox_changed( double value)` | method | `void` | private | — |
| `d_viewport_window` | field | `ViewportWindow` | private | — |
| `d_palette_name_lineedit` | field | `FriendlyLineEdit` | private | — |
| `d_choose_builtin_palette_dialog` | field | `ChooseBuiltinPaletteDialog` | private | — |
| `d_colour_scale_widget` | field | `ColourScaleWidget` | private | — |
| `d_builtin_colour_palette_parameters` | field | `GPlatesGui::BuiltinColourPaletteType::Parameters` | private | The built-in colour palette parameters for use in the built-in palette dialog. |

## Free functions and macros

| Name | Kind | Type / body | Description |
|---|---|---|---|
| `GPLATES_QT_WIDGETS_REMAPPEDCOLOURPALETTEWIDGET_H` | macro | `None` | — |

## Notes

*None.*

## Used by

| Unit | Component | References |
|---|---|---|
| [qt-widgets/ScalarField3DLayerOptionsWidget](ScalarField3DLayerOptionsWidget.md) | qt-widgets | 8 |
| [qt-widgets/ReconstructScalarCoverageLayerOptionsWidget](ReconstructScalarCoverageLayerOptionsWidget.md) | qt-widgets | 2 |
| [qt-widgets/RasterLayerOptionsWidget](RasterLayerOptionsWidget.md) | qt-widgets | 1 |

## Related

**Qt Designer forms**

| Form class | Base widget | Title | Widgets |
|---|---|---|---|
| `RemappedColourPaletteWidget` | `QWidget` | Form | 24 |

**Qt signal/slot connections** (15 in this unit)

| Sender | Signal | Receiver | Slot |
|---|---|---|---|
| `choose_builtin_palette_link` | `link_activated()` | `this` | `open_choose_builtin_palette_dialog()` |
| `select_palette_filename_button` | `clicked()` | `this` | `handle_select_palette_filename_button_clicked()` |
| `use_default_palette_button` | `clicked()` | `this` | `handle_use_default_palette_button_clicked()` |
| `range_check_box` | `stateChanged(int)` | `this` | `handle_range_check_box_changed(int)` |
| `min_line_edit` | `editingFinished()` | `this` | `handle_min_line_editing_finished()` |
| `max_line_edit` | `editingFinished()` | `this` | `handle_max_line_editing_finished()` |
| `range_restore_min_max_button` | `clicked()` | `this` | `handle_range_restore_min_max_button_clicked()` |
| `range_restore_mean_deviation_button` | `clicked()` | `this` | `handle_range_restore_mean_deviation_button_clicked()` |
| `range_restore_mean_deviation_spin_box` | `valueChanged(double)` | `this` | `handle_range_restore_mean_deviation_spinbox_changed(double)` |
| `range_check_box` | `stateChanged(int)` | `this` | `handle_range_check_box_changed(int)` |
| `min_line_edit` | `editingFinished()` | `this` | `handle_min_line_editing_finished()` |
| `max_line_edit` | `editingFinished()` | `this` | `handle_max_line_editing_finished()` |
| `range_restore_mean_deviation_spin_box` | `valueChanged(double)` | `this` | `handle_range_restore_mean_deviation_spinbox_changed(double)` |
| `d_choose_builtin_palette_dialog` | `builtin_colour_palette_selected(const GPlatesGui::BuiltinColourPaletteType &)` | `this` | `handle_builtin_colour_palette_selected(const GPlatesGui::BuiltinColourPaletteType &)` |
| `d_choose_builtin_palette_dialog` | `builtin_parameters_changed(const GPlatesGui::BuiltinColourPaletteType::Parameters &)` | `this` | `handle_builtin_parameters_changed(const GPlatesGui::BuiltinColourPaletteType::Parameters &)` |


## Explore

Run these from the `gplates-code` skill directory:

```bash
python scripts/gpq.py file src/qt-widgets/RemappedColourPaletteWidget.h
python scripts/gpq.py def GPlatesQtWidgets::RemappedColourPaletteWidget --body
python scripts/gpq.py uses RemappedColourPaletteWidget --kind class
python scripts/gpq.py hier RemappedColourPaletteWidget
```
