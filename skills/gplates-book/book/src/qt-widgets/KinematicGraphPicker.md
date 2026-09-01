# KinematicGraphPicker

[Book TOC](../../TOC.md) · [qt-widgets](../../components/qt-widgets.md) · cluster Community 1414 · tier 3

| Source file | Kind | Lines |
|---|---|---|
| `src/qt-widgets/KinematicGraphPicker.h` | C++ | 81 |
| `src/qt-widgets/KinematicGraphPicker.cc` | C++ | 210 |

## Overview

A `QwtPlotPicker` subclass for extracting and displaying information from kinematic graphs. The primary responsibility is the `trackerTextF()` method, which generates a formatted text string displayed when the user hovers over the graph. It performs linear interpolation between adjacent data points to estimate values between grid points, and appends the appropriate unit suffix based on the graph type (degrees, cm/year, or degrees/Ma depending on whether the graph shows latitude, velocity, or rotation rate).

The `SmallestTimeCoordinateYoungerThan` functor and `get_interpolated_y_value()` helper function support binary search and linear interpolation between the bracketing data points.

## Declared types

| Name | Kind | Bases | Template | Subclasses | Description |
|---|---|---|---|---|---|
| [`(anonymous)::SmallestTimeCoordinateYoungerThan`](#anonymoussmallesttimecoordinateyoungerthan) | class | — | — | 0 | — |
| [`GPlatesQtWidgets::KinematicGraphPicker`](#gplatesqtwidgetskinematicgraphpicker) | class | `QwtPlotPicker` | — | 0 | The KinematicGraphPicker class - used to extract and display information from the kinematic graph. |

## Members

### `(anonymous)::SmallestTimeCoordinateYoungerThan`

| Member | Kind | Type | Access | Description |
|---|---|---|---|---|
| `SmallestTimeCoordinateYoungerThan( double value)` | constructor | `None` | public | — |
| `operator()( const QPointF &point)` | operator | `bool` | public | — |
| `d_x` | field | `double` | private | — |

### `GPlatesQtWidgets::KinematicGraphPicker`

| Member | Kind | Type | Access | Description |
|---|---|---|---|---|
| `KinematicGraphPicker( const QwtPointSeriesData *point_series_data, const QwtPlotCurve *plot_curve, QwtPlot::Axis axis1, QwtPlot::Axis axis2, QwtPicker::RubberBand rubber_band, QwtPicker::DisplayMode display_mode, QwtPlotCanvas *canvas)` | constructor | `None` | public | — |
| `trackerTextF(const QPointF &)` | method | `QwtText` | public | — |
| `set_graph_type( const KinematicGraphsDialog::KinematicGraphType &type)` | method | `void` | public | — |
| `d_data_ptr` | field | `QwtPointSeriesData` | private | — |
| `d_plot_curve_ptr` | field | `QwtPlotCurve` | private | — |
| `d_type` | field | `KinematicGraphsDialog::KinematicGraphType` | private | — |

## Free functions and macros

| Name | Kind | Type / body | Description |
|---|---|---|---|
| `get_interpolated_y_value( const QPointF &point, const QwtPointSeriesData *data)` | function | `boost::optional<double>` | get\_interpolated\_y\_value - returns y value based on linear interpolation between the x-values to the left and right of the x value contained in point. interpolated y value. |
| `KINEMATICGRAPHPICKER_H` | macro | `None` | — |

## Notes

*None.*

## Used by

| Unit | Component | References |
|---|---|---|
| [qt-widgets/KinematicGraphsDialog](KinematicGraphsDialog.md) | qt-widgets | 5 |

## Related

*None.*

## Explore

Run these from the `gplates-code` skill directory:

```bash
python scripts/gpq.py file src/qt-widgets/KinematicGraphPicker.h
python scripts/gpq.py def GPlatesQtWidgets::KinematicGraphPicker --body
python scripts/gpq.py uses KinematicGraphPicker --kind class
python scripts/gpq.py hier KinematicGraphPicker
```
