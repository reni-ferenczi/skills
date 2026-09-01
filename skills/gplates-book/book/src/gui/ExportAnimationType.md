# ExportAnimationType

[Book TOC](../../TOC.md) · [gui](../../components/gui.md) · cluster Community 1143 · tier 1

| Source file | Kind | Lines |
|---|---|---|
| `src/gui/ExportAnimationType.h` | C++ | 196 |
| `src/gui/ExportAnimationType.cc` | C++ | 444 |

## Overview

[[[PROSE overview unit=gui/ExportAnimationType tier=1]]]
Replace this whole block, markers included, with 1-3 paragraphs: what this unit is, why it exists, and how it fits the surrounding design. Do not restate the tables below.
[[[/PROSE]]]

## Declared types

| Name | Kind | Bases | Template | Subclasses | Description |
|---|---|---|---|---|---|
| [`GPlatesGui::ExportAnimationType::Type`](#gplatesguiexportanimationtypetype) | enum | — | — | 0 | The list of export types. |
| [`GPlatesGui::ExportAnimationType::Format`](#gplatesguiexportanimationtypeformat) | enum | — | — | 0 | The list of exporter formats. |
| [`GPlatesGui::ExportAnimationType::ExportID`](#gplatesguiexportanimationtypeexportid) | typedef | — | — | 0 | An identifier, that can be generated via get\_export\_id, to identify an exporter that is a combination of Type and Format. |

## Members

### `GPlatesGui::ExportAnimationType::Type`

| Member | Kind | Type | Access | Description |
|---|---|---|---|---|
| `RECONSTRUCTED_GEOMETRIES` | enumerator | `None` | — | — |
| `PROJECTED_GEOMETRIES` | enumerator | `None` | — | — |
| `IMAGE` | enumerator | `None` | — | — |
| `COLOUR_RASTER` | enumerator | `None` | — | — |
| `NUMERICAL_RASTER` | enumerator | `None` | — | — |
| `SCALAR_COVERAGES` | enumerator | `None` | — | — |
| `DEFORMATION` | enumerator | `None` | — | — |
| `VELOCITIES` | enumerator | `None` | — | — |
| `RESOLVED_TOPOLOGIES` | enumerator | `None` | — | — |
| `RESOLVED_TOPOLOGIES_CITCOMS` | enumerator | `None` | — | — |
| `RELATIVE_TOTAL_ROTATION` | enumerator | `None` | — | — |
| `EQUIVALENT_TOTAL_ROTATION` | enumerator | `None` | — | — |
| `RELATIVE_STAGE_ROTATION` | enumerator | `None` | — | — |
| `EQUIVALENT_STAGE_ROTATION` | enumerator | `None` | — | — |
| `FLOWLINES` | enumerator | `None` | — | — |
| `MOTION_PATHS` | enumerator | `None` | — | — |
| `CO_REGISTRATION` | enumerator | `None` | — | — |
| `NET_ROTATIONS` | enumerator | `None` | — | — |
| `NUM_TYPES` | enumerator | `None` | — | — |
| `INVALID_TYPE` | enumerator | `None` | — | — |

### `GPlatesGui::ExportAnimationType::Format`

| Member | Kind | Type | Access | Description |
|---|---|---|---|---|
| `GMT` | enumerator | `None` | — | — |
| `SHAPEFILE` | enumerator | `None` | — | — |
| `OGRGMT` | enumerator | `None` | — | — |
| `GEOJSON` | enumerator | `None` | — | — |
| `SVG` | enumerator | `None` | — | — |
| `GPML` | enumerator | `None` | — | — |
| `CSV_COMMA` | enumerator | `None` | — | — |
| `CSV_SEMICOLON` | enumerator | `None` | — | — |
| `CSV_TAB` | enumerator | `None` | — | — |
| `BMP` | enumerator | `None` | — | Colour raster/image formats. |
| `JPG` | enumerator | `None` | — | — |
| `JPEG` | enumerator | `None` | — | — |
| `PNG` | enumerator | `None` | — | — |
| `PPM` | enumerator | `None` | — | — |
| `TIFF` | enumerator | `None` | — | — |
| `XBM` | enumerator | `None` | — | — |
| `XPM` | enumerator | `None` | — | — |
| `NETCDF_NC` | enumerator | `None` | — | Numerical raster formats. |
| `NETCDF_GRD` | enumerator | `None` | — | — |
| `GEOTIFF` | enumerator | `None` | — | — |
| `ERDAS_IMAGINE` | enumerator | `None` | — | — |
| `ERMAPPER` | enumerator | `None` | — | — |
| `CITCOMS_GLOBAL` | enumerator | `None` | — | — |
| `TERRA_TEXT` | enumerator | `None` | — | — |
| `NUM_FORMATS` | enumerator | `None` | — | — |
| `INVALID_FORMAT` | enumerator | `None` | — | — |

### `GPlatesGui::ExportAnimationType::ExportID`

*None.*

## Free functions and macros

| Name | Kind | Type / body | Description |
|---|---|---|---|
| `initialise_export_type_name_map()` | function | `std::map<Type, QString>` | — |
| `initialise_export_type_description_map()` | function | `std::map<Type, QString>` | — |
| `initialise_export_format_description_map()` | function | `std::map<Format, QString>` | — |
| `initialise_export_format_filename_extension_map()` | function | `std::map<Format, QString>` | — |
| `DISABLE_GCC_WARNING` | variable | `PUSH_GCC_WARNINGS` | For the BOOST\_STATIC\_ASSERT below with GCC 4.2. |
| `GPLATES_GUI_EXPORTANIMATIONTYPE_H` | macro | `None` | — |
| `get_export_type_name` | variable | `QString` | Returns the name of the specified export type. |
| `get_export_type_description` | variable | `QString` | Returns the description of the specified export type. |
| `get_export_format_description` | variable | `QString` | Returns the description of the specified export format. |
| `get_export_format_filename_extension` | variable | `QString` | Returns the filename extension of the specified export format. |
| `get_export_id( Type type, Format format)` | function | `ExportID` | Returns the export animation type corresponding to the specified export name and format. |
| `get_export_type( ExportID export_id)` | function | `Type` | Returns the export type corresponding to the specified export ID. |
| `get_export_format( ExportID export_id)` | function | `Format` | Returns the export format corresponding to the specified export ID. |
| `get_export_types( const std::vector<ExportID> &export_ids)` | function | `std::vector<Type>` | Returns a unique list of export types in export\_ids. |
| `get_export_formats( const std::vector<ExportID> &export_ids, Type export_type)` | function | `std::vector<Format>` | Returns those export formats in export\_ids that have the specified export type. |

## Notes

[[[PROSE notes unit=gui/ExportAnimationType tier=1]]]
Replace this whole block, markers included, with invariants, ownership, threading or gotchas that are not visible in the tables. Write *None.* if there is nothing worth saying.
[[[/PROSE]]]

## Used by

| Unit | Component | References |
|---|---|---|
| [gui/ExportAnimationRegistry](ExportAnimationRegistry.md) | gui | 436 |
| [qt-widgets/ConfigureExportParametersDialog](../qt-widgets/ConfigureExportParametersDialog.md) | qt-widgets | 89 |
| [qt-widgets/EditExportParametersDialog](../qt-widgets/EditExportParametersDialog.md) | qt-widgets | 10 |
| [qt-widgets/ExportFileNameTemplateWidget](../qt-widgets/ExportFileNameTemplateWidget.md) | qt-widgets | 10 |
| [qt-widgets/ExportAnimationDialog](../qt-widgets/ExportAnimationDialog.md) | qt-widgets | 9 |
| [qt-widgets/ExportVelocityOptionsWidget](../qt-widgets/ExportVelocityOptionsWidget.md) | qt-widgets | 9 |
| [gui/ExportAnimationContext](ExportAnimationContext.md) | gui | 7 |
| [gui/ExportNetRotationAnimationStrategy](ExportNetRotationAnimationStrategy.md) | gui | 6 |
| [gui/ExportVelocityAnimationStrategy](ExportVelocityAnimationStrategy.md) | gui | 3 |
| [gui/ExportDeformationAnimationStrategy](ExportDeformationAnimationStrategy.md) | gui | 1 |
| [gui/ExportImageAnimationStrategy](ExportImageAnimationStrategy.md) | gui | 1 |
| [gui/ExportScalarCoverageAnimationStrategy](ExportScalarCoverageAnimationStrategy.md) | gui | 1 |

## Related

*None.*

## Explore

Run these from the `gplates-code` skill directory:

```bash
python scripts/gpq.py file src/gui/ExportAnimationType.h
python scripts/gpq.py def GPlatesGui::ExportAnimationType::Format --body
python scripts/gpq.py uses Format --kind enum
```
