# LayerOptionsWidget

[Book TOC](../../TOC.md) · [qt-widgets](../../components/qt-widgets.md) · cluster Community 689 · tier 2

| Source file | Kind | Lines |
|---|---|---|
| `src/qt-widgets/LayerOptionsWidget.h` | C++ | 75 |

## Overview

`LayerOptionsWidget` is the abstract base for the per-layer-type options panels shown inside `VisualLayerWidget` when a layer is selected in the layers list — one concrete subclass per visual layer type (raster, reconstruct, topology resolvers, velocity field calculator, co-registration, scalar field, and so on). It defines the two-method contract every subclass must implement: `set_data()`, which is called whenever the panel should refresh itself to reflect a given `GPlatesPresentation::VisualLayer` (held only as a `boost::weak_ptr`, since the layer can be destroyed independently of the options widget), and `get_title()`, which supplies the panel's display name. Beyond that it adds nothing over `QWidget`, leaving layout and behaviour entirely to each subclass.

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

`set_data()` is called with a `boost::weak_ptr`, not a strong reference; a subclass must `lock()` it and handle the case where the visual layer has already been destroyed rather than assuming it stays alive for the widget's lifetime.

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
