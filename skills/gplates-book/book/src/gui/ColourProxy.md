# ColourProxy

[Book TOC](../../TOC.md) · [gui](../../components/gui.md) · cluster Community 640 · tier 2

| Source file | Kind | Lines |
|---|---|---|
| `src/gui/ColourProxy.h` | C++ | 177 |
| `src/gui/ColourProxy.cc` | C++ | 117 |

## Overview

[[[PROSE overview unit=gui/ColourProxy tier=2]]]
Replace this whole block, markers included, with 1-3 paragraphs: what this unit is, why it exists, and how it fits the surrounding design. Do not restate the tables below.
[[[/PROSE]]]

## Declared types

| Name | Kind | Bases | Template | Subclasses | Description |
|---|---|---|---|---|---|
| [`GPlatesGui::ColourProxy`](#gplatesguicolourproxy) | class | — | — | 0 | This class allows the colour of a ReconstructionGeometry to be determined at a later time. |
| [`GPlatesGui::ColourProxyImpl`](#gplatesguicolourproxyimpl) | class | — | — | 2 | Pimpl idiom. |
| [`GPlatesGui::DeferredColourProxyImpl`](#gplatesguideferredcolourproxyimpl) | class | [`ColourProxyImpl`](ColourProxy.md) | — | 0 | The version of ColourProxy where we want deferred colour assignment. |
| [`GPlatesGui::FixedColourProxyImpl`](#gplatesguifixedcolourproxyimpl) | class | [`ColourProxyImpl`](ColourProxy.md) | — | 0 | The version of ColourProxy where we don't want deferred colour assignment. |

## Members

### `GPlatesGui::ColourProxy`

| Member | Kind | Type | Access | Description |
|---|---|---|---|---|
| `ColourProxy( GPlatesAppLogic::ReconstructionGeometry::non_null_ptr_to_const_type reconstruction_geometry_ptr, boost::shared_ptr<ColourFilter> colour_filter_ptr = boost::shared_ptr<ColourFilter>())` | constructor | `None` | public | Constructs a ColourProxy with deferred colour assignment. object for which the colour will be determined at a later time. modify the output from the ColourScheme. |
| `ColourProxy( const Colour &colour)` | constructor | `None` | public | Constructs a ColourProxy without deferred colour assignment. |
| `ColourProxy( boost::optional<Colour> colour)` | constructor | `None` | public | Constructs a ColourProxy without deferred colour assignment. |
| `get_colour( ColourScheme::non_null_ptr_type colour_scheme)` | method | `boost::optional<Colour>` | public | Get the colour of the ReconstructionGeometry using a particular ColourScheme. |
| `d_impl_ptr` | field | `boost::shared_ptr<ColourProxyImpl>` | private | — |

### `GPlatesGui::ColourProxyImpl`

| Member | Kind | Type | Access | Description |
|---|---|---|---|---|
| `~ColourProxyImpl()` | destructor | `None` | public | — |
| `get_colour( ColourScheme::non_null_ptr_type colour_scheme)` | method | `boost::optional<Colour>` | public | — |

### `GPlatesGui::DeferredColourProxyImpl`

| Member | Kind | Type | Access | Description |
|---|---|---|---|---|
| `DeferredColourProxyImpl( GPlatesAppLogic::ReconstructionGeometry::non_null_ptr_to_const_type reconstruction_geometry_ptr, boost::shared_ptr<ColourFilter> colour_filter_ptr)` | constructor | `None` | public | — |
| `get_colour( ColourScheme::non_null_ptr_type colour_scheme)` | method | `boost::optional<Colour>` | public | — |
| `d_reconstruction_geometry_ptr` | field | `GPlatesAppLogic::ReconstructionGeometry::non_null_ptr_to_const_type` | private | — |
| `d_colour_filter_ptr` | field | `boost::shared_ptr<ColourFilter>` | private | — |

### `GPlatesGui::FixedColourProxyImpl`

| Member | Kind | Type | Access | Description |
|---|---|---|---|---|
| `FixedColourProxyImpl( boost::optional<Colour> colour)` | constructor | `None` | public | — |
| `get_colour( ColourScheme::non_null_ptr_type colour_scheme)` | method | `boost::optional<Colour>` | public | — |
| `d_colour` | field | `boost::optional<Colour>` | private | — |

## Free functions and macros

| Name | Kind | Type / body | Description |
|---|---|---|---|
| `GPLATES_GUI_COLOURPROXY_H` | macro | `None` | — |

## Notes

[[[PROSE notes unit=gui/ColourProxy tier=2]]]
Replace this whole block, markers included, with invariants, ownership, threading or gotchas that are not visible in the tables. Write *None.* if there is nothing worth saying.
[[[/PROSE]]]

## Used by

| Unit | Component | References |
|---|---|---|
| [presentation/ReconstructionGeometryRenderer](../presentation/ReconstructionGeometryRenderer.md) | presentation | 60 |
| [view-operations/RenderedGeometryFactory](../view-operations/RenderedGeometryFactory.md) | view-operations | 54 |
| [view-operations/RenderedRadialArrow](../view-operations/RenderedRadialArrow.md) | view-operations | 7 |
| [view-operations/RenderedString](../view-operations/RenderedString.md) | view-operations | 7 |
| [gui/GlobeRenderedGeometryLayerPainter](GlobeRenderedGeometryLayerPainter.md) | gui | 6 |
| [app-logic/deprecated/PaleomagWorkflow](../app-logic/deprecated/PaleomagWorkflow.md) | app-logic | 5 |
| [gui/MapRenderedGeometryLayerPainter](MapRenderedGeometryLayerPainter.md) | gui | 5 |
| [app-logic/deprecated/PaleomagUtils](../app-logic/deprecated/PaleomagUtils.md) | app-logic | 4 |
| [view-operations/RenderedArrowedPolyline](../view-operations/RenderedArrowedPolyline.md) | view-operations | 4 |
| [view-operations/RenderedCircleSymbol](../view-operations/RenderedCircleSymbol.md) | view-operations | 4 |
| [view-operations/RenderedColouredMultiPointOnSphere](../view-operations/RenderedColouredMultiPointOnSphere.md) | view-operations | 4 |
| [view-operations/RenderedColouredPolygonOnSphere](../view-operations/RenderedColouredPolygonOnSphere.md) | view-operations | 4 |
| [view-operations/RenderedColouredPolylineOnSphere](../view-operations/RenderedColouredPolylineOnSphere.md) | view-operations | 4 |
| [view-operations/RenderedCrossSymbol](../view-operations/RenderedCrossSymbol.md) | view-operations | 4 |
| [view-operations/RenderedEllipse](../view-operations/RenderedEllipse.md) | view-operations | 4 |
| [view-operations/RenderedMultiPointOnSphere](../view-operations/RenderedMultiPointOnSphere.md) | view-operations | 4 |
| [view-operations/RenderedPointOnSphere](../view-operations/RenderedPointOnSphere.md) | view-operations | 4 |
| [view-operations/RenderedPolygonOnSphere](../view-operations/RenderedPolygonOnSphere.md) | view-operations | 4 |
| [view-operations/RenderedPolylineOnSphere](../view-operations/RenderedPolylineOnSphere.md) | view-operations | 4 |
| [view-operations/RenderedSmallCircle](../view-operations/RenderedSmallCircle.md) | view-operations | 4 |

*... and 8 more units.*

## Related

*None.*

## Explore

Run these from the `gplates-code` skill directory:

```bash
python scripts/gpq.py file src/gui/ColourProxy.h
python scripts/gpq.py def GPlatesGui::ColourProxy --body
python scripts/gpq.py uses ColourProxy --kind class
python scripts/gpq.py hier ColourProxy
```
