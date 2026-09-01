# MeasureDistanceWidget

[Book TOC](../../TOC.md) · [qt-widgets](../../components/qt-widgets.md) · cluster Community 335 · tier 3

| Source file | Kind | Lines |
|---|---|---|
| `src/qt-widgets/MeasureDistanceWidget.h` | C++ | 184 |
| `src/qt-widgets/MeasureDistanceWidget.cc` | C++ | 411 |
| `src/qt-widgets/MeasureDistanceWidgetUi.ui` | Qt form | 409 |

## Overview

A task panel widget displaying measurements from the distance measuring canvas tool. `MeasureDistanceWidget` presents two sections: Quick Measure (for ad-hoc distance measurements between two points) and Feature Measure (for distances and areas computed when a feature is selected). It renders latitude/longitude coordinates, distances, and optional area values with 4 decimal places of precision. The widget responds to measurement state changes via signals from `MeasureDistanceState`, updating the display and highlighting measurement fields when new data arrives. Users can clear all measurements via an action button.

## Declared types

| Name | Kind | Bases | Template | Subclasses | Description |
|---|---|---|---|---|---|
| [`GPlatesQtWidgets::MeasureDistanceWidget`](#gplatesqtwidgetsmeasuredistancewidget) | class | [`TaskPanelWidget`](TaskPanelWidget.md)<br>`Ui_MeasureDistanceWidget` | — | 0 | TaskPanel widget that displays information for distance measuring canvas tool |

## Members

### `GPlatesQtWidgets::MeasureDistanceWidget`

| Member | Kind | Type | Access | Description |
|---|---|---|---|---|
| `MeasureDistanceWidget( GPlatesCanvasTools::MeasureDistanceState &measure_distance_state, QWidget *parent_ = NULL)` | constructor | `None` | public | Contructor |
| `handle_activation()` | method | `void` | public | — |
| `get_clear_action_text()` | method | `QString` | public | — |
| `clear_action_enabled()` | method | `bool` | public | — |
| `handle_clear_action_triggered()` | method | `void` | public | — |
| `update_quick_measure( boost::optional<GPlatesMaths::PointOnSphere> start, boost::optional<GPlatesMaths::PointOnSphere> end, boost::optional<double> distance)` | method | `void` | private | Update the Quick Measure part of the widget |
| `update_feature_measure( double total_distance, boost::optional<double> area, boost::optional<GPlatesMaths::PointOnSphere> segment_start, boost::optional<GPlatesMaths::PointOnSphere> segment_end, boost::optional<double> segment_distance)` | method | `void` | private | Update the Feature Measure part of the widget (when there is a feature to show) |
| `update_feature_measure()` | method | `void` | private | Update the Feature Measure part of the widget (when there is NO feature to show) |
| `lineedit_radius_text_edited( const QString &text)` | method | `void` | private | Handles textEdited signal for lineedit\_radius (we only want to pick up changes by the user, not changes made programmatically) |
| `change_quick_measure_highlight( bool is_highlighted)` | method | `void` | private | Toggles background highlight of Quick Measure distance field |
| `change_feature_measure_highlight( bool is_highlighted)` | method | `void` | private | Toggles background highlight of Feature Measure segment distance field |
| `d_measure_distance_state_ptr` | field | `GPlatesCanvasTools::MeasureDistanceState` | private | A pointer to the state of the measuring distance tool |
| `d_lineedit_original_palette` | field | `QPalette` | private | Stores the original palette of the QLineEdit controls so that we can change their background colour back again |
| `make_signal_slot_connections()` | method | `void` | private | Sets up Qt signal/slots |
| `change_background_colour( QLineEdit *lineedit, const QColor &colour)` | method | `void` | private | Changes the background colour of a QLineEdit to a particular colour |
| `restore_background_colour( QLineEdit *lineedit)` | method | `void` | private | Restores the background colour of a QLineEdit |
| `PRECISION` | field | `unsigned int` | private | The number of decimal places used in the part above history table |

## Free functions and macros

| Name | Kind | Type / body | Description |
|---|---|---|---|
| `set_lineedit_text( QLineEdit &control, double value, int precision)` | function | `void` | Sets the text of a QLineEdit to a particular floating point @value rounded to @precision decimal places |
| `display_point_on_sphere( QLineEdit &lat_control, QLineEdit &lon_control, const GPlatesMaths::PointOnSphere &point_on_sphere, int precision)` | function | `void` | Displays point\_on\_sphere in Lat-Lon format in two QLineEdit controls, lat\_control and lon\_control |
| `clear_and_disable( QLineEdit *control)` | function | `void` | Clears the text and disables a QLineEdit control |
| `PRECISION` | variable | `unsigned int` | — |
| `GPLATES_QTWIDGETS_MEASUREDISTANCEWIDGET_H` | macro | `None` | — |

## Notes

The `textEdited` signal (not `textChanged`) is connected for the radius input to capture only user-initiated changes, excluding programmatic updates. Background color changes to `QLineEdit` controls are temporary highlights; the original palette is saved and restored when highlighting is toggled off.

## Used by

| Unit | Component | References |
|---|---|---|
| [qt-widgets/TaskPanel](TaskPanel.md) | qt-widgets | 2 |

## Related

**Qt Designer forms**

| Form class | Base widget | Title | Widgets |
|---|---|---|---|
| `MeasureDistanceWidget` | `QWidget` | Form | 33 |

**Qt signal/slot connections** (6 in this unit)

| Sender | Signal | Receiver | Slot |
|---|---|---|---|
| `lineedit_radius` | `textEdited(const QString &)` | `this` | `lineedit_radius_text_edited(const QString &)` |
| `d_measure_distance_state_ptr` | `quick_measure_updated( boost::optional<GPlatesMaths::PointOnSphere>, boost::optional<GPlatesMaths::PointOnSphere>, boost::optional<double>)` | `this` | `update_quick_measure( boost::optional<GPlatesMaths::PointOnSphere>, boost::optional<GPlatesMaths::PointOnSphere>, boost::optional<double>)` |
| `d_measure_distance_state_ptr` | `feature_measure_updated( double, boost::optional<double>, boost::optional<GPlatesMaths::PointOnSphere>, boost::optional<GPlatesMaths::PointOnSphere>, boost::optional<double>)` | `this` | `update_feature_measure( double, boost::optional<double>, boost::optional<GPlatesMaths::PointOnSphere>, boost::optional<GPlatesMaths::PointOnSphere>, boost::optional<double>)` |
| `d_measure_distance_state_ptr` | `feature_measure_updated()` | `this` | `update_feature_measure()` |
| `d_measure_distance_state_ptr` | `quick_measure_highlight_changed(bool)` | `this` | `change_quick_measure_highlight(bool)` |
| `d_measure_distance_state_ptr` | `feature_measure_highlight_changed(bool)` | `this` | `change_feature_measure_highlight(bool)` |


## Explore

Run these from the `gplates-code` skill directory:

```bash
python scripts/gpq.py file src/qt-widgets/MeasureDistanceWidget.h
python scripts/gpq.py def GPlatesQtWidgets::MeasureDistanceWidget --body
python scripts/gpq.py uses MeasureDistanceWidget --kind class
python scripts/gpq.py hier MeasureDistanceWidget
```
