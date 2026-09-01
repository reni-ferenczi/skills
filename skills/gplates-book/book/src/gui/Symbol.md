# Symbol

[Book TOC](../../TOC.md) · [gui](../../components/gui.md) · cluster Community 41 · tier 2

| Source file | Kind | Lines |
|---|---|---|
| `src/gui/Symbol.h` | C++ | 108 |
| `src/gui/Symbol.cc` | C++ | 122 |

## Overview

`GPlatesGui::Symbol` is a small value struct describing how to draw a feature as a symbol instead of its native geometry — a `SymbolType` (triangle, square, circle, cross or strain marker), a size, whether it is filled, and optional per-axis scale and rotation angle. `symbol_map_type` associates a `GPlatesModel::FeatureType` with the `Symbol` used to render features of that type, which is how `presentation/ReconstructionGeometryRenderer` and `view-operations/RenderedGeometryFactory` decide to draw symbols instead of the feature's actual geometry; `get_symbol_type_from_string()` and `symbol_text_map_type` support parsing the symbol type from text, used when reading symbol configuration such as `file-io/SymbolFileReader`'s files.

`Symbol` participates in the Scribe serialisation used for sessions and projects: both the struct itself and its `SymbolType` enum have `transcribe()` overloads. The enum is transcribed by string id (via `GPlatesScribe::transcribe_enum_protocol`) rather than by numeric value, so its serialised form is stable even if the enum's declaration order changes.

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

`Symbol::transcribe()` treats every field as optional on read: if a field fails to transcribe, it falls back to that field's default-constructed value rather than failing the whole transcription, so older or newer saved sessions stay forward/backward compatible as fields are added. The enum's string ids used in serialisation (`"TRIANGLE"`, `"SQUARE"`, etc.) must never change once shipped, even if the C++ enumerator names do, or saved sessions/projects referencing them will fail to load. Adding a new `SymbolType` value also requires adding it to `transcribe()`'s `enum_values` table.

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
