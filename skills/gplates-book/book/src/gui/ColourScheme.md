# ColourScheme

[Book TOC](../../TOC.md) · [gui](../../components/gui.md) · cluster Community 14 · tier 2

| Source file | Kind | Lines |
|---|---|---|
| `src/gui/ColourScheme.h` | C++ | 93 |

## Overview

`ColourScheme` is the abstract policy interface behind GPlates' colouring system: anything that decides "what colour is this feature drawn in" implements it. It offers two overloads because the same colouring decision can be asked of either a reconstructed `ReconstructionGeometry` (the usual case when rendering the globe or map) or the underlying `FeatureHandle` directly, and either can return `boost::none` to mean "do not draw this at all" rather than any particular colour.

The interface is deliberately thin and reference-counted (via `GPlatesUtils::ReferenceCount`) so that concrete strategies — colouring by plate ID, by age, by a single fixed colour, by a `.cpt` palette, or delegating to another scheme entirely — can be swapped behind a `non_null_ptr_type` at runtime, most visibly through `ColourSchemeDelegator`, without callers caring which strategy is active.

## Declared types

| Name | Kind | Bases | Template | Subclasses | Description |
|---|---|---|---|---|---|
| [`GPlatesGui::ColourScheme`](#gplatesguicolourscheme) | class | [`GPlatesUtils::ReferenceCount<ColourScheme>`](../utils/ReferenceCount.md) | — | 7 | This class assigns colours to ReconstructionGeometry instances. |

## Members

### `GPlatesGui::ColourScheme`

| Member | Kind | Type | Access | Description |
|---|---|---|---|---|
| `non_null_ptr_type` | typedef | `GPlatesUtils::non_null_intrusive_ptr<ColourScheme>` | public | Convenience typedef for GPlatesUtils::non\_null\_intrusive\_ptr\<ColourScheme\>. |
| `non_null_ptr_to_const_type` | typedef | `GPlatesUtils::non_null_intrusive_ptr<const ColourScheme>` | public | Convenience typedef for GPlatesUtils::non\_null\_intrusive\_ptr\<const ColourScheme\>. |
| `~ColourScheme()` | destructor | `None` | public | Destructor |
| `get_colour( const GPlatesAppLogic::ReconstructionGeometry &reconstruction_geometry)` | method | `boost::optional<Colour>` | public | Returns a colour for a particular reconstruction\_geometry, or boost::none if it does not have the necessary parameters or if the reconstruction geometry should not be drawn for some other reason |
| `get_colour( const GPlatesModel::FeatureHandle& feature_ptr)` | method | `boost::optional<Colour>` | public | — |

## Free functions and macros

| Name | Kind | Type / body | Description |
|---|---|---|---|
| `GPLATES_GUI_COLOURSCHEME_H` | macro | `None` | — |

## Notes

- `boost::none` from either `get_colour` overload means "don't draw", not "use a default colour" — callers must treat it as a skip signal, not fall back to black or white.

## Used by

| Unit | Component | References |
|---|---|---|
| [app-logic/deprecated/PaleomagUtils](../app-logic/deprecated/PaleomagUtils.md) | app-logic | 35 |
| [gui/ColourSchemeDelegator](ColourSchemeDelegator.md) | gui | 35 |
| [qt-widgets/ColouringDialog](../qt-widgets/ColouringDialog.md) | qt-widgets | 31 |
| [presentation/ReconstructionGeometryRenderer](../presentation/ReconstructionGeometryRenderer.md) | presentation | 18 |
| [gui/SingleColourScheme](SingleColourScheme.md) | gui | 17 |
| [gui/TopologyTools](TopologyTools.md) | gui | 16 |
| [gui/DrawStyleAdapters](DrawStyleAdapters.md) | gui | 14 |
| [gui/GenericColourScheme](GenericColourScheme.md) | gui | 14 |
| [qt-widgets/CoRegistrationLayerConfigurationDialog](../qt-widgets/CoRegistrationLayerConfigurationDialog.md) | qt-widgets | 14 |
| [qt-widgets/ImportScalarField3DDialog](../qt-widgets/ImportScalarField3DDialog.md) | qt-widgets | 13 |
| [gui/MapCanvasToolAdapter](MapCanvasToolAdapter.md) | gui | 12 |
| [qt-widgets/ModifyReconstructionPoleWidget](../qt-widgets/ModifyReconstructionPoleWidget.md) | qt-widgets | 12 |
| [app-logic/deprecated/PaleomagWorkflow](../app-logic/deprecated/PaleomagWorkflow.md) | app-logic | 10 |
| [gui/ColourProxy](ColourProxy.md) | gui | 9 |
| [qt-widgets/GlobeCanvas](../qt-widgets/GlobeCanvas.md) | qt-widgets | 9 |
| [gui/Map](Map.md) | gui | 8 |
| [canvas-tools/EditTopology](../canvas-tools/EditTopology.md) | canvas-tools | 6 |
| [gui/CommandServer](CommandServer.md) | gui | 6 |
| [gui/Globe](Globe.md) | gui | 6 |
| [gui/ColourSchemeInfo](ColourSchemeInfo.md) | gui | 5 |

*... and 22 more units.*

## Related

*None.*

## Explore

Run these from the `gplates-code` skill directory:

```bash
python scripts/gpq.py file src/gui/ColourScheme.h
python scripts/gpq.py def GPlatesGui::ColourScheme --body
python scripts/gpq.py uses ColourScheme --kind class
python scripts/gpq.py hier ColourScheme
```
