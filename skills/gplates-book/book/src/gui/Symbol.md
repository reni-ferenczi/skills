# Symbol

[Book TOC](../../TOC.md) · [gui](../../components/gui.md) · cluster Community 41 · tier 2

| Source file | Kind | Lines |
|---|---|---|
| `src/gui/Symbol.h` | C++ | 108 |
| `src/gui/Symbol.cc` | C++ | 122 |

## Overview

[[[PROSE overview unit=gui/Symbol tier=2]]]
Replace this whole block, markers included, with 1-3 paragraphs: what this unit is, why it exists, and how it fits the surrounding design. Do not restate the tables below.
[[[/PROSE]]]

## Declared types

| Name | Kind | Bases | Template | Subclasses | Description |
|---|---|---|---|---|---|
| [`GPlatesGui::Symbol`](#gplatesguisymbol) | struct | — | — | 0 | — |
| [`GPlatesGui::feature_type_symbol_pair_type`](#gplatesguifeature_type_symbol_pair_type) | typedef | — | — | 0 | — |
| [`GPlatesGui::symbol_map_type`](#gplatesguisymbol_map_type) | typedef | — | — | 0 | — |
| [`GPlatesGui::symbol_text_map_type`](#gplatesguisymbol_text_map_type) | typedef | — | — | 0 | — |

## Members

### `GPlatesGui::Symbol`

| Member | Kind | Type | Access | Description |
|---|---|---|---|---|
| `SymbolType` | enum | `None` | public | — |
| `Symbol( SymbolType symbol_type = TRIANGLE, unsigned int size = 1, // FIXME: Make this floating-point. bool filled = false, boost::optional<double> s_x = boost::none, boost::optional<double> s_y = boost::none, boost::optional<double> a = boost::none)` | constructor | `None` | public | — |
| `d_symbol_type` | field | `SymbolType` | public | — |
| `d_size` | field | `unsigned int` | public | — |
| `d_filled` | field | `bool` | public | — |
| `d_scale_x` | field | `boost::optional<double>` | public | — |
| `d_scale_y` | field | `boost::optional<double>` | public | — |
| `d_angle` | field | `boost::optional<double>` | public | — |
| `transcribe( GPlatesScribe::Scribe &scribe, bool transcribed_construct_data)` | method | `GPlatesScribe::TranscribeResult` | private | — |

### `GPlatesGui::feature_type_symbol_pair_type`

*None.*

### `GPlatesGui::symbol_map_type`

*None.*

### `GPlatesGui::symbol_text_map_type`

*None.*

## Free functions and macros

| Name | Kind | Type / body | Description |
|---|---|---|---|
| `GPLATES_GUI_SYMBOL_H` | macro | `None` | — |
| `get_symbol_type_from_string( const QString &symbol_string)` | function | `boost::optional<Symbol::SymbolType>` | — |
| `transcribe( GPlatesScribe::Scribe &scribe, Symbol::SymbolType &symbol_type, bool transcribed_construct_data)` | function | `GPlatesScribe::TranscribeResult` | Transcribe for sessions/projects. |

## Notes

[[[PROSE notes unit=gui/Symbol tier=2]]]
Replace this whole block, markers included, with invariants, ownership, threading or gotchas that are not visible in the tables. Write *None.* if there is nothing worth saying.
[[[/PROSE]]]

## Used by

| Unit | Component | References |
|---|---|---|
| [qt-widgets/HellingerDialog](../qt-widgets/HellingerDialog.md) | qt-widgets | 58 |
| [view-operations/RenderedGeometryFactory](../view-operations/RenderedGeometryFactory.md) | view-operations | 36 |
| [gui/VisualLayersProxy](VisualLayersProxy.md) | gui | 23 |
| [file-io/SymbolFileReader](../file-io/SymbolFileReader.md) | file-io | 19 |
| [canvas-tools/AdjustFittedPoleEstimate](../canvas-tools/AdjustFittedPoleEstimate.md) | canvas-tools | 17 |
| [presentation/ReconstructionGeometryRenderer](../presentation/ReconstructionGeometryRenderer.md) | presentation | 10 |
| [qt-widgets/HellingerFitWidget](../qt-widgets/HellingerFitWidget.md) | qt-widgets | 9 |
| [presentation/ViewState](../presentation/ViewState.md) | presentation | 7 |
| [qt-widgets/HellingerThread](../qt-widgets/HellingerThread.md) | qt-widgets | 6 |
| [gui/GeometryFocusHighlight](GeometryFocusHighlight.md) | gui | 4 |
| [presentation/TranscribeSession](../presentation/TranscribeSession.md) | presentation | 3 |
| [presentation/VisualLayer](../presentation/VisualLayer.md) | presentation | 3 |
| [gui/FeatureInspectionCanvasToolWorkflow](FeatureInspectionCanvasToolWorkflow.md) | gui | 2 |
| [gui/PoleManipulationCanvasToolWorkflow](PoleManipulationCanvasToolWorkflow.md) | gui | 2 |
| [gui/TopologyCanvasToolWorkflow](TopologyCanvasToolWorkflow.md) | gui | 2 |
| [presentation/VisualLayers](../presentation/VisualLayers.md) | presentation | 2 |
| [qt-widgets/SaveFileDialogImpl](../qt-widgets/SaveFileDialogImpl.md) | qt-widgets | 2 |
| [view-operations/ChangeLightDirectionOperation](../view-operations/ChangeLightDirectionOperation.md) | view-operations | 1 |
| [view-operations/MovePoleOperation](../view-operations/MovePoleOperation.md) | view-operations | 1 |

## Related

*None.*

## Explore

Run these from the `gplates-code` skill directory:

```bash
python scripts/gpq.py file src/gui/Symbol.h
python scripts/gpq.py def GPlatesGui::Symbol --body
python scripts/gpq.py uses Symbol --kind struct
python scripts/gpq.py hier Symbol
```
