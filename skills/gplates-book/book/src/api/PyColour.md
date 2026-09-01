# PyColour

[Book TOC](../../TOC.md) · [api](../../components/api.md) · cluster Community 740 · tier 2

| Source file | Kind | Lines |
|---|---|---|
| `src/api/PyColour.cc` | C++ | 169 |

## Overview

`PyColour.cc` exposes `GPlatesGui::Colour`, `GPlatesApi::Palette`,
`GPlatesGui::Palette::Key` and `GPlatesGui::DrawStyle` to Python via
`export_colour()` and `export_style()`, called during module setup alongside
the other `export_*` functions in `src/api/`.

The named-colour free functions (`red()`, `blue()`, `white()`, and so on) exist
only as a workaround: `GPlatesGui::Colour`'s own named-colour accessors are
static methods returning `const Colour &`, which Boost.Python cannot export
directly as class members because of how it handles reference return values.
Each wrapper here calls the corresponding `Colour::get_*()` and returns by
value instead, and `export_colour()` binds the wrapper to a Python static
property of the same name (`Colour.red`, `Colour.blue`, ...) rather than a
method, so the workaround is invisible from the Python side.

## Declared types

*None.*

## Members

*None.*

## Free functions and macros

| Name | Kind | Type / body | Description |
|---|---|---|---|
| `red()` | function | `GPlatesGui::Colour` | I have trouble to use the static functions , for example "static const Colour &get\_red();", in GPlatesGui::Colour class for boost python class member function export due to the fact that boost python seems have problem with the return ... |
| `blue()` | function | `GPlatesGui::Colour` | — |
| `white()` | function | `GPlatesGui::Colour` | — |
| `black()` | function | `GPlatesGui::Colour` | — |
| `green()` | function | `GPlatesGui::Colour` | — |
| `grey()` | function | `GPlatesGui::Colour` | — |
| `silver()` | function | `GPlatesGui::Colour` | — |
| `purple()` | function | `GPlatesGui::Colour` | — |
| `yellow()` | function | `GPlatesGui::Colour` | — |
| `navy()` | function | `GPlatesGui::Colour` | — |
| `export_colour()` | function | `void` | — |
| `export_style()` | function | `void` | — |

## Notes

A handful of colours the C++ side supports (maroon, fuchsia, lime, olive, teal,
aqua) are commented out here as `TODO` and are not yet exposed to Python.

## Used by

| Unit | Component | References |
|---|---|---|
| [gui/Colour](../gui/Colour.md) | gui | 7 |
| [qt-widgets/HellingerPickWidget](../qt-widgets/HellingerPickWidget.md) | qt-widgets | 4 |
| [qt-widgets/LatLonCoordinatesTable](../qt-widgets/LatLonCoordinatesTable.md) | qt-widgets | 4 |
| [qt-widgets/KinematicGraphsDialog](../qt-widgets/KinematicGraphsDialog.md) | qt-widgets | 3 |
| [qt-widgets/TopologyNetworkResolverLayerOptionsWidget](../qt-widgets/TopologyNetworkResolverLayerOptionsWidget.md) | qt-widgets | 3 |
| [file-io/CptReader](../file-io/CptReader.md) | file-io | 2 |
| [gui/BuiltinColourPalettes](../gui/BuiltinColourPalettes.md) | gui | 2 |
| [gui/Completionist](../gui/Completionist.md) | gui | 2 |
| [gui/ConfigModel](../gui/ConfigModel.md) | gui | 2 |
| [gui/LogFilterModel](../gui/LogFilterModel.md) | gui | 2 |
| [gui/TopologySectionsTable](../gui/TopologySectionsTable.md) | gui | 2 |
| [qt-widgets/GlobeCanvas](../qt-widgets/GlobeCanvas.md) | qt-widgets | 2 |
| [qt-widgets/PythonConsoleDialog](../qt-widgets/PythonConsoleDialog.md) | qt-widgets | 2 |
| [qt-widgets/SmallCircleWidget](../qt-widgets/SmallCircleWidget.md) | qt-widgets | 2 |
| [gui/ColourScaleGenerator](../gui/ColourScaleGenerator.md) | gui | 1 |
| [gui/FeedbackOpenGLToQPainter](../gui/FeedbackOpenGLToQPainter.md) | gui | 1 |
| [qt-widgets/AgeModelManagerDialog](../qt-widgets/AgeModelManagerDialog.md) | qt-widgets | 1 |
| [qt-widgets/ColouringDialog](../qt-widgets/ColouringDialog.md) | qt-widgets | 1 |
| [qt-widgets/CreateSmallCircleDialog](../qt-widgets/CreateSmallCircleDialog.md) | qt-widgets | 1 |
| [qt-widgets/EditTotalReconstructionSequenceWidget](../qt-widgets/EditTotalReconstructionSequenceWidget.md) | qt-widgets | 1 |

*... and 4 more units.*

## Related

**Python bindings**

| Python name | Kind | Owner | C++ |
|---|---|---|---|
| `Colour` | class | — | `GPlatesGui::Colour` |
| `__init__` | constructor | `Colour` | `init<const float,const float,const float,const float>` |
| `blue` | static_attribute | `Colour` | `&GPlatesApi::blue` |
| `red` | static_attribute | `Colour` | `&GPlatesApi::red` |
| `white` | static_attribute | `Colour` | `&GPlatesApi::white` |
| `black` | static_attribute | `Colour` | `&GPlatesApi::black` |
| `green` | static_attribute | `Colour` | `&GPlatesApi::green` |
| `grey` | static_attribute | `Colour` | `&GPlatesApi::grey` |
| `silver` | static_attribute | `Colour` | `&GPlatesApi::silver` |
| `purple` | static_attribute | `Colour` | `&GPlatesApi::purple` |
| `yellow` | static_attribute | `Colour` | `&GPlatesApi::yellow` |
| `navy` | static_attribute | `Colour` | `&GPlatesApi::navy` |
| `Palette` | class | — | `GPlatesApi::Palette` |
| `get_color` | method | `Palette` | `&GPlatesApi::Palette::get_color` |
| `PaletteKey` | class | — | `GPlatesGui::Palette::Key` |

*... and 6 more bindings.*


## Explore

Run these from the `gplates-code` skill directory:

```bash
python scripts/gpq.py file src/api/PyColour.cc
```
