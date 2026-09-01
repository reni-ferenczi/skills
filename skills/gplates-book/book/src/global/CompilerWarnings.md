# CompilerWarnings

[Book TOC](../../TOC.md) · [global](../../components/global.md) · cluster Community 3 · tier 2

| Source file | Kind | Lines |
|---|---|---|
| `src/global/CompilerWarnings.h` | C++ | 136 |

## Overview

[[[PROSE overview unit=global/CompilerWarnings tier=2]]]
Replace this whole block, markers included, with 1-3 paragraphs: what this unit is, why it exists, and how it fits the surrounding design. Do not restate the tables below.
[[[/PROSE]]]

## Declared types

*None.*

## Members

*None.*

## Free functions and macros

| Name | Kind | Type / body | Description |
|---|---|---|---|
| `GPLATES_GLOBAL_COMPILERWARNINGS_H` | macro | `None` | — |
| `PUSH_GCC_WARNINGS` | macro | `_Pragma( STRINGIFY_WARNING(GCC diagnostic push) )` | — |
| `POP_GCC_WARNINGS` | macro | `_Pragma( STRINGIFY_WARNING(GCC diagnostic pop) )` | — |
| `PUSH_MSVC_WARNINGS` | macro | `__pragma( warning( push ) )` | — |
| `POP_MSVC_WARNINGS` | macro | `__pragma( warning( pop ) )` | — |
| `ENABLE_GCC_WARNING` | macro_function | `_Pragma( STRINGIFY_WARNING(GCC diagnostic error warning_string ) )` | — |
| `DISABLE_GCC_WARNING` | macro_function | `_Pragma( STRINGIFY_WARNING(GCC diagnostic ignored warning_string ) )` | — |
| `ENABLE_MSVC_WARNING` | macro_function | `__pragma( warning( error : warning_number ) )` | — |
| `DISABLE_MSVC_WARNING` | macro_function | `__pragma( warning( disable : warning_number ) )` | — |
| `STRINGIFY_WARNING` | macro_function | `#warning` | Used to support gcc's \_Pragma() preprocessor operator which expects a string literal. |

## Notes

[[[PROSE notes unit=global/CompilerWarnings tier=2]]]
Replace this whole block, markers included, with invariants, ownership, threading or gotchas that are not visible in the tables. Write *None.* if there is nothing worth saying.
[[[/PROSE]]]

## Used by

| Unit | Component | References |
|---|---|---|
| [api/PythonRunner](../api/PythonRunner.md) | api | 3 |
| [api/PythonUtils](../api/PythonUtils.md) | api | 3 |
| [app-logic/ResolvedTriangulationDelaunay2](../app-logic/ResolvedTriangulationDelaunay2.md) | app-logic | 3 |
| [data-mining/DataSelector](../data-mining/DataSelector.md) | data-mining | 3 |
| [data-mining/deprecated/RegionOfInterestAssociationOperator](../data-mining/deprecated/RegionOfInterestAssociationOperator.md) | data-mining | 3 |
| [file-io/CitcomsResolvedTopologicalBoundaryExport](../file-io/CitcomsResolvedTopologicalBoundaryExport.md) | file-io | 3 |
| [file-io/ReconstructionGeometryExportImpl](../file-io/ReconstructionGeometryExportImpl.md) | file-io | 3 |
| [global/python](python.md) | global | 3 |
| [gui/DrawStyleManager](../gui/DrawStyleManager.md) | gui | 3 |
| [gui/ExportAnimationType](../gui/ExportAnimationType.md) | gui | 3 |
| [maths/PolygonMesh](../maths/PolygonMesh.md) | maths | 3 |
| [model/TopLevelPropertyInline](../model/TopLevelPropertyInline.md) | model | 3 |
| [opengl/GLMultiResolutionCubeMesh](../opengl/GLMultiResolutionCubeMesh.md) | opengl | 3 |
| [opengl/GLMultiResolutionMapCubeMesh](../opengl/GLMultiResolutionMapCubeMesh.md) | opengl | 3 |
| [opengl/GLStateSets](../opengl/GLStateSets.md) | opengl | 3 |
| [presentation/ReconstructionGeometryRenderer](../presentation/ReconstructionGeometryRenderer.md) | presentation | 3 |
| [property-values/CoordinateTransformation](../property-values/CoordinateTransformation.md) | property-values | 3 |
| [property-values/SpatialReferenceSystem](../property-values/SpatialReferenceSystem.md) | property-values | 3 |
| [qt-widgets/ChangePropertyWidget](../qt-widgets/ChangePropertyWidget.md) | qt-widgets | 3 |
| [qt-widgets/CoRegistrationLayerConfigurationDialog](../qt-widgets/CoRegistrationLayerConfigurationDialog.md) | qt-widgets | 3 |

*... and 31 more units.*

## Related

*None.*

## Explore

Run these from the `gplates-code` skill directory:

```bash
python scripts/gpq.py file src/global/CompilerWarnings.h
```
