# LayerOptionsWidget

[Book TOC](../../TOC.md) · [qt-widgets](../../components/qt-widgets.md) · cluster Community 689 · tier 2

| Source file | Kind | Lines |
|---|---|---|
| `src/qt-widgets/LayerOptionsWidget.h` | C++ | 75 |

## Overview

[[[PROSE overview unit=qt-widgets/LayerOptionsWidget tier=2]]]
Replace this whole block, markers included, with 1-3 paragraphs: what this unit is, why it exists, and how it fits the surrounding design. Do not restate the tables below.
[[[/PROSE]]]

## Declared types

| Name | Kind | Bases | Template | Subclasses | Description |
|---|---|---|---|---|---|
| [`GPlatesQtWidgets::LayerOptionsWidget`](#gplatesqtwidgetslayeroptionswidget) | class | `QWidget` | — | 9 | This is the abstract base class of widgets used to display options particular to different visual layer types. |

## Members

### `GPlatesQtWidgets::LayerOptionsWidget`

| Member | Kind | Type | Access | Description |
|---|---|---|---|---|
| `LayerOptionsWidget( QWidget *parent_)` | constructor | `None` | public | — |
| `~LayerOptionsWidget()` | destructor | `None` | public | — |
| `set_data( const boost::weak_ptr<GPlatesPresentation::VisualLayer> &visual_layer)` | method | `void` | public | Requests that the widget display options for the given visual\_layer. |
| `get_title` | field | `QString` | public | — |

## Free functions and macros

| Name | Kind | Type / body | Description |
|---|---|---|---|
| `GPLATES_QTWIDGETS_LAYEROPTIONSWIDGET_H` | macro | `None` | — |

## Notes

[[[PROSE notes unit=qt-widgets/LayerOptionsWidget tier=2]]]
Replace this whole block, markers included, with invariants, ownership, threading or gotchas that are not visible in the tables. Write *None.* if there is nothing worth saying.
[[[/PROSE]]]

## Used by

| Unit | Component | References |
|---|---|---|
| [qt-widgets/RasterLayerOptionsWidget](RasterLayerOptionsWidget.md) | qt-widgets | 8 |
| [qt-widgets/ReconstructLayerOptionsWidget](ReconstructLayerOptionsWidget.md) | qt-widgets | 8 |
| [qt-widgets/ReconstructScalarCoverageLayerOptionsWidget](ReconstructScalarCoverageLayerOptionsWidget.md) | qt-widgets | 8 |
| [qt-widgets/ReconstructionLayerOptionsWidget](ReconstructionLayerOptionsWidget.md) | qt-widgets | 8 |
| [qt-widgets/ScalarField3DLayerOptionsWidget](ScalarField3DLayerOptionsWidget.md) | qt-widgets | 8 |
| [qt-widgets/TopologyGeometryResolverLayerOptionsWidget](TopologyGeometryResolverLayerOptionsWidget.md) | qt-widgets | 8 |
| [qt-widgets/VelocityFieldCalculatorLayerOptionsWidget](VelocityFieldCalculatorLayerOptionsWidget.md) | qt-widgets | 8 |
| [qt-widgets/TopologyNetworkResolverLayerOptionsWidget](TopologyNetworkResolverLayerOptionsWidget.md) | qt-widgets | 6 |
| [qt-widgets/CoRegistrationOptionsWidget](CoRegistrationOptionsWidget.md) | qt-widgets | 4 |
| [qt-widgets/VisualLayerWidget](VisualLayerWidget.md) | qt-widgets | 1 |

## Related

*None.*

## Explore

Run these from the `gplates-code` skill directory:

```bash
python scripts/gpq.py file src/qt-widgets/LayerOptionsWidget.h
python scripts/gpq.py def GPlatesQtWidgets::LayerOptionsWidget --body
python scripts/gpq.py uses LayerOptionsWidget --kind class
python scripts/gpq.py hier LayerOptionsWidget
```
