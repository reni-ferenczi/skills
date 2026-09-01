# BuiltinColourPaletteType

[Book TOC](../../TOC.md) · [gui](../../components/gui.md) · cluster Community 584 · tier 2

| Source file | Kind | Lines |
|---|---|---|
| `src/gui/BuiltinColourPaletteType.h` | C++ | 288 |
| `src/gui/BuiltinColourPaletteType.cc` | C++ | 393 |

## Overview

[[[PROSE overview unit=gui/BuiltinColourPaletteType tier=2]]]
Replace this whole block, markers included, with 1-3 paragraphs: what this unit is, why it exists, and how it fits the surrounding design. Do not restate the tables below.
[[[/PROSE]]]

## Declared types

| Name | Kind | Bases | Template | Subclasses | Description |
|---|---|---|---|---|---|
| [`GPlatesGui::BuiltinColourPaletteType`](#gplatesguibuiltincolourpalettetype) | class | — | — | 0 | Used to define the type of a built-in colour palette. |

## Members

### `GPlatesGui::BuiltinColourPaletteType`

| Member | Kind | Type | Access | Description |
|---|---|---|---|---|
| `PaletteType` | enum | `None` | public | Some pre-defined internal palette types are provided for convenience. |
| `Parameters` | struct | `None` | public | Parameters that may be related to the palette type. |
| `BuiltinColourPaletteType( BuiltinColourPalettes::Age::Type age_type, const Parameters &parameters)` | constructor | `None` | public | Construct an age type. |
| `BuiltinColourPaletteType( BuiltinColourPalettes::Topography::Type topography_type, const Parameters &parameters)` | constructor | `None` | public | Construct a topography type. |
| `BuiltinColourPaletteType( BuiltinColourPalettes::SCM::Type scm_type, const Parameters &parameters)` | constructor | `None` | public | Construct a SCM type. |
| `BuiltinColourPaletteType( BuiltinColourPalettes::ColorBrewer::Sequential::Type colorbrewer_sequential_type, const Parameters &parameters)` | constructor | `None` | public | Construct a ColorBrewer sequential palette type. |
| `BuiltinColourPaletteType( BuiltinColourPalettes::ColorBrewer::Diverging::Type colorbrewer_diverging_type, const Parameters &parameters)` | constructor | `None` | public | Construct a ColorBrewer diverging palette type. |
| `create_palette()` | method | `RasterColourPalette::non_null_ptr_type` | public | Creates a colour palette. |
| `get_palette_name()` | method | `QString` | public | Returns the name of the colour palette. |
| `get_palette_type()` | method | `PaletteType` | public | Return the palette type. |
| `get_age_type()` | method | `BuiltinColourPalettes::Age::Type` | public | Return the age palette type (if get\_palette\_type returns AGE\_PALETTE). |
| `get_topography_type()` | method | `BuiltinColourPalettes::Topography::Type` | public | Return the topography palette type (if get\_palette\_type returns TOPOGRAPHY\_PALETTE). |
| `get_scm_type()` | method | `BuiltinColourPalettes::SCM::Type` | public | Return the SCM palette type (if get\_palette\_type returns SCM\_PALETTE). |
| `get_colorbrewer_sequential_type()` | method | `BuiltinColourPalettes::ColorBrewer::Sequential::Type` | public | Return the ColorBrewer sequential palette type (if get\_palette\_type returns COLORBREWER\_SEQUENTIAL\_PALETTE). |
| `get_colorbrewer_diverging_type()` | method | `BuiltinColourPalettes::ColorBrewer::Diverging::Type` | public | Return the ColorBrewer diverging palette type (if get\_palette\_type returns COLORBREWER\_DIVERGING\_PALETTE). |
| `d_palette_type` | field | `PaletteType` | private | — |
| `d_parameters` | field | `Parameters` | private | — |
| `d_age_type` | field | `BuiltinColourPalettes::Age::Type` | private | This is only used if d\_palette\_type is AGE\_PALETTE. |
| `d_topography_type` | field | `BuiltinColourPalettes::Topography::Type` | private | This is only used if d\_palette\_type is TOPOGRAPHY\_PALETTE. |
| `d_scm_type` | field | `BuiltinColourPalettes::SCM::Type` | private | This is only used if d\_palette\_type is SCM\_PALETTE. |
| `d_colorbrewer_sequential_type` | field | `BuiltinColourPalettes::ColorBrewer::Sequential::Type` | private | These are only used if d\_palette\_type is COLORBREWER\_SEQUENTIAL\_PALETTE or COLORBREWER\_DIVERGING\_PALETTE. |
| `d_colorbrewer_diverging_type` | field | `BuiltinColourPalettes::ColorBrewer::Diverging::Type` | private | — |
| `DEFAULT_PALETTE_TYPE` | field | `PaletteType` | private | — |
| `DEFAULT_AGE_TYPE` | field | `BuiltinColourPalettes::Age::Type` | private | — |
| `DEFAULT_TOPOGRAPHY_TYPE` | field | `BuiltinColourPalettes::Topography::Type` | private | — |
| `DEFAULT_SCM_TYPE` | field | `BuiltinColourPalettes::SCM::Type` | private | — |
| `DEFAULT_COLORBREWER_SEQUENTIAL_TYPE` | field | `BuiltinColourPalettes::ColorBrewer::Sequential::Type` | private | — |
| `DEFAULT_COLORBREWER_DIVERGING_TYPE` | field | `BuiltinColourPalettes::ColorBrewer::Diverging::Type` | private | — |
| `BuiltinColourPaletteType()` | constructor | `None` | private | Default constructor makes transcribing easier. |
| `transcribe( GPlatesScribe::Scribe &scribe, bool transcribed_construct_data)` | method | `GPlatesScribe::TranscribeResult` | private | — |

## Free functions and macros

| Name | Kind | Type / body | Description |
|---|---|---|---|
| `DEFAULT_PALETTE_TYPE` | variable | `GPlatesGui::BuiltinColourPaletteType::PaletteType` | — |
| `DEFAULT_AGE_TYPE` | variable | `GPlatesGui::BuiltinColourPalettes::Age::Type` | GPlates 2.3 made the existing age palette legacy and added two new palettes (traditional and modern). |
| `DEFAULT_TOPOGRAPHY_TYPE` | variable | `GPlatesGui::BuiltinColourPalettes::Topography::Type` | GPlates 2.4 added three new topography palettes (etopo1, oleron and bukavu). |
| `DEFAULT_SCM_TYPE` | variable | `GPlatesGui::BuiltinColourPalettes::SCM::Type` | GPlates 2.4 added new SCM palettes. |
| `DEFAULT_COLORBREWER_SEQUENTIAL_TYPE` | variable | `GPlatesGui::BuiltinColourPalettes::ColorBrewer::Sequential::Type` | — |
| `DEFAULT_COLORBREWER_DIVERGING_TYPE` | variable | `GPlatesGui::BuiltinColourPalettes::ColorBrewer::Diverging::Type` | — |
| `GPLATES_GUI_BUILTINCOLOURPALETTETYPE_H` | macro | `None` | — |
| `transcribe( GPlatesScribe::Scribe &scribe, BuiltinColourPaletteType::PaletteType &palette_type, bool transcribed_construct_data)` | function | `GPlatesScribe::TranscribeResult` | Transcribe for sessions/projects. |

## Notes

[[[PROSE notes unit=gui/BuiltinColourPaletteType tier=2]]]
Replace this whole block, markers included, with invariants, ownership, threading or gotchas that are not visible in the tables. Write *None.* if there is nothing worth saying.
[[[/PROSE]]]

## Used by

| Unit | Component | References |
|---|---|---|
| [qt-widgets/ChooseBuiltinPaletteDialog](../qt-widgets/ChooseBuiltinPaletteDialog.md) | qt-widgets | 227 |
| [qt-widgets/ScalarField3DLayerOptionsWidget](../qt-widgets/ScalarField3DLayerOptionsWidget.md) | qt-widgets | 38 |
| [presentation/RemappedColourPaletteParameters](../presentation/RemappedColourPaletteParameters.md) | presentation | 28 |
| [qt-widgets/VisualLayerWidget](../qt-widgets/VisualLayerWidget.md) | qt-widgets | 26 |
| [qt-widgets/RemappedColourPaletteWidget](../qt-widgets/RemappedColourPaletteWidget.md) | qt-widgets | 22 |
| [qt-widgets/RasterLayerOptionsWidget](../qt-widgets/RasterLayerOptionsWidget.md) | qt-widgets | 20 |
| [qt-widgets/ReconstructScalarCoverageLayerOptionsWidget](../qt-widgets/ReconstructScalarCoverageLayerOptionsWidget.md) | qt-widgets | 20 |
| [presentation/TranscribeSession](../presentation/TranscribeSession.md) | presentation | 6 |
| [presentation/RasterVisualLayerParams](../presentation/RasterVisualLayerParams.md) | presentation | 1 |
| [qt-widgets/MapView](../qt-widgets/MapView.md) | qt-widgets | 1 |

## Related

*None.*

## Explore

Run these from the `gplates-code` skill directory:

```bash
python scripts/gpq.py file src/gui/BuiltinColourPaletteType.h
python scripts/gpq.py def GPlatesGui::BuiltinColourPaletteType --body
python scripts/gpq.py uses BuiltinColourPaletteType --kind class
python scripts/gpq.py hier BuiltinColourPaletteType
```
