# EditAffineTransformGeoreferencingWidget

[Book TOC](../../TOC.md) · [qt-widgets](../../components/qt-widgets.md) · cluster Community 321 · tier 2

| Source file | Kind | Lines |
|---|---|---|
| `src/qt-widgets/EditAffineTransformGeoreferencingWidget.h` | C++ | 120 |
| `src/qt-widgets/EditAffineTransformGeoreferencingWidget.cc` | C++ | 406 |
| `src/qt-widgets/EditAffineTransformGeoreferencingWidgetUi.ui` | Qt form | 687 |

## Overview

`EditAffineTransformGeoreferencingWidget` edits a raster's
`GPlatesPropertyValues::Georeferencing` in place, offering two equivalent views on
`main_stackedwidget` toggled by `advanced_checkbox`: a simple lat/lon extents form
(top/bottom latitude, left/right longitude) or the full six-parameter affine
transform, both ultimately reading and writing the same `Georeferencing` object
via `get_lat_lon_extents()`/`set_lat_lon_extents()` and
`get_parameters()`/`set_parameters()`. `grid_line_registration_checkbox` switches
between pixel registration (extents describe pixel *areas*) and grid-line
registration (extents describe pixel *centres*); toggling it converts the
georeferencing's existing values in place via `expand_pixel_to_grid_line_registration()`
or `contract_grid_line_to_pixel_registration()` rather than reinterpreting them,
so the raster's placement on the globe does not jump when the checkbox is
toggled. `Georeferencing::get_lat_lon_extents()` can fail to express the current affine
transform as plain lat/lon extents and returns `boost::none` in that case;
`populate_lat_lon_extents_spinboxes()` then hides the extents form and shows
`cannot_convert_to_extents_label` instead.

## Declared types

| Name | Kind | Bases | Template | Subclasses | Description |
|---|---|---|---|---|---|
| [`GPlatesQtWidgets::EditAffineTransformGeoreferencingWidget`](#gplatesqtwidgetseditaffinetransformgeoreferencingwidget) | class | `QWidget`<br>`Ui_EditAffineTransformGeoreferencingWidget` | — | 0 | — |

## Members

### `GPlatesQtWidgets::EditAffineTransformGeoreferencingWidget`

| Member | Kind | Type | Access | Description |
|---|---|---|---|---|
| `EditAffineTransformGeoreferencingWidget( GPlatesPropertyValues::Georeferencing::non_null_ptr_type &georeferencing, QWidget *parent_ = NULL)` | constructor | `None` | public | — |
| `reset( unsigned int raster_width, unsigned int raster_height)` | method | `void` | public | Resets the raster to global extents. |
| `georeferencing_changed()` | method | `void` | public | — |
| `handle_grid_line_registration_checkbox_state_changed( int state)` | method | `void` | private | — |
| `handle_advanced_checkbox_state_changed( int state)` | method | `void` | private | — |
| `handle_use_global_extents_button_clicked()` | method | `void` | private | — |
| `update_extents_if_necessary()` | method | `void` | private | — |
| `update_affine_transform_if_necessary()` | method | `void` | private | — |
| `lat_lon_extents_type` | typedef | `GPlatesPropertyValues::Georeferencing::lat_lon_extents_type` | private | — |
| `affine_transform_type` | typedef | `GPlatesPropertyValues::Georeferencing::parameters_type` | private | — |
| `make_signal_slot_connections()` | method | `void` | private | — |
| `populate_lat_lon_extents_spinboxes( const boost::optional<lat_lon_extents_type> &extents)` | method | `void` | private | — |
| `populate_affine_transform_spinboxes( const affine_transform_type &parameters)` | method | `void` | private | — |
| `refresh_spinboxes()` | method | `void` | private | — |
| `d_extents_spinboxes` | field | `QDoubleSpinBox` | private | — |
| `d_affine_transform_spinboxes` | field | `QDoubleSpinBox` | private | — |
| `d_last_known_extents_values` | field | `double` | private | — |
| `d_last_known_affine_transform_values` | field | `double` | private | — |
| `d_georeferencing` | field | `GPlatesPropertyValues::Georeferencing::non_null_ptr_type` | private | — |
| `d_raster_width` | field | `unsigned int` | private | — |
| `d_raster_height` | field | `unsigned int` | private | — |
| `d_help_grid_line_registration_dialog` | field | `GPlatesQtWidgets::InformationDialog` | private | — |

## Free functions and macros

| Name | Kind | Type / body | Description |
|---|---|---|---|
| `HELP_GRID_LINE_REGISTRATION_DIALOG_TITLE` | variable | `QString` | — |
| `HELP_GRID_LINE_REGISTRATION_DIALOG_TEXT` | variable | `QString` | — |
| `any_changed( QDoubleSpinBox **spinboxes, double *last_known_values, unsigned int length)` | function | `bool` | — |
| `GPLATES_QTWIDGETS_EDITAFFINETRANSFORMGEOREFERENCINGWIDGET_H` | macro | `None` | — |

## Notes

`d_georeferencing` is a reference to a `non_null_ptr_type` owned by the caller, not
a copy, so every edit here mutates the caller's `Georeferencing` object directly
and `georeferencing_changed()` is emitted to tell it (and other observers) to
react. `update_extents_if_necessary()` and `update_affine_transform_if_necessary()`
compare against `d_last_known_*_values` (via the file-local `any_changed()`) before
writing anything back, because `editingFinished()` fires even when a spinbox's
value did not actually change; after writing, they re-read the value from
`Georeferencing` rather than trusting the spinbox, since what was set may not be
exactly what is returned. `reset()` must be called with the raster's actual
dimensions before the widget can do anything meaningful, since `d_raster_width`/
`d_raster_height` default to 0 at construction.

## Used by

| Unit | Component | References |
|---|---|---|
| [qt-widgets/RasterGeoreferencingPage](RasterGeoreferencingPage.md) | qt-widgets | 10 |
| [qt-widgets/ScalarField3DGeoreferencingPage](ScalarField3DGeoreferencingPage.md) | qt-widgets | 10 |
| [qt-widgets/RasterPropertiesDialog](RasterPropertiesDialog.md) | qt-widgets | 2 |

## Related

**Qt Designer forms**

| Form class | Base widget | Title | Widgets |
|---|---|---|---|
| `EditAffineTransformGeoreferencingWidget` | `QWidget` | Form | 42 |

**Qt signal/slot connections** (6 in this unit)

| Sender | Signal | Receiver | Slot |
|---|---|---|---|
| `push_button_help_grid_line_registration` | `clicked()` | `d_help_grid_line_registration_dialog` | `show()` |
| `grid_line_registration_checkbox` | `stateChanged(int)` | `this` | `handle_grid_line_registration_checkbox_state_changed(int)` |
| `advanced_checkbox` | `stateChanged(int)` | `this` | `handle_advanced_checkbox_state_changed(int)` |
| `use_global_extents_button` | `clicked()` | `this` | `handle_use_global_extents_button_clicked()` |
| `d_extents_spinboxes[i]` | `editingFinished()` | `this` | `update_extents_if_necessary()` |
| `d_affine_transform_spinboxes[i]` | `editingFinished()` | `this` | `update_affine_transform_if_necessary()` |


## Explore

Run these from the `gplates-code` skill directory:

```bash
python scripts/gpq.py file src/qt-widgets/EditAffineTransformGeoreferencingWidget.h
python scripts/gpq.py def GPlatesQtWidgets::EditAffineTransformGeoreferencingWidget --body
python scripts/gpq.py uses EditAffineTransformGeoreferencingWidget --kind class
python scripts/gpq.py hier EditAffineTransformGeoreferencingWidget
```
