# ColourScheme

[Book TOC](../../TOC.md) · [gui](../../components/gui.md) · cluster Community 14 · tier 2

| Source file | Kind | Lines |
|---|---|---|
| `src/gui/ColourScheme.h` | C++ | 93 |

## Overview

[[[PROSE overview unit=gui/ColourScheme tier=2]]]
Replace this whole block, markers included, with 1-3 paragraphs: what this unit is, why it exists, and how it fits the surrounding design. Do not restate the tables below.
[[[/PROSE]]]

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

[[[PROSE notes unit=gui/ColourScheme tier=2]]]
Replace this whole block, markers included, with invariants, ownership, threading or gotchas that are not visible in the tables. Write *None.* if there is nothing worth saying.
[[[/PROSE]]]

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
