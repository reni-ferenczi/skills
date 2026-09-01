# ExportAnimationType

[Book TOC](../../TOC.md) · [gui](../../components/gui.md) · cluster Community 1143 · tier 1

| Source file | Kind | Lines |
|---|---|---|
| `src/gui/ExportAnimationType.h` | C++ | 196 |
| `src/gui/ExportAnimationType.cc` | C++ | 444 |

## Overview

This is the vocabulary the whole export subsystem is keyed on — a namespace of free
functions rather than a class. It answers three separate questions. What kinds of
export exist and in what file formats (`Type` and `Format`). How to name one exporter
with a single scalar (`ExportID`, a `Type` and a `Format` packed into a `uint32_t`).
And what to call any of these on screen (the four string accessors).

The packing is the reason this unit is load-bearing.
`ExportAnimationRegistry` keys its exporter table by `ExportID`, and
`ExportAnimationContext` keys its multimap of live strategies by the same value, so a
single integer identifies "resolved topologies, as OGR GMT" throughout the feature —
easy to store in a `QTableWidget` item's user data, cheap to compare, and no
composite key type needed. `get_export_id()` shifts the type into the high 16 bits
and ors the format into the low 16; `get_export_type()` and `get_export_format()`
unpack it and assert the result is in range.

Not every `Type`/`Format` pair is meaningful, and this header does not say which are —
the registry does, by registering only the combinations that have an exporter. That
is what `get_export_types()` and `get_export_formats()` are for: given the vector of
IDs that `ExportAnimationRegistry::get_registered_exporters()` returns,
`ConfigureExportParametersDialog` derives the list of types to offer, and then, for
whichever type the user picks, the formats available for it. The dialog therefore never
enumerates the raw enums. The string accessors feed the same dialog: the type and
format descriptions are HTML fragments, so the dialog can show a formatted explanation
of a selection. `get_export_format_filename_extension()` is used differently: the
registry appends it to each exporter's default filename template as it registers, and
`ExportFileNameTemplateWidget` uses it to split a template into an editable basename
and a fixed, non-editable extension label.

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

Both enums carry an explicit contract, stated in the header: the enumerators must be
sequential from zero, `NUM_TYPES` / `NUM_FORMATS` must be the count, and
`INVALID_TYPE` / `INVALID_FORMAT` must come *after* the count so they never collide
with a real value. A `BOOST_STATIC_ASSERT` in `get_export_id()` additionally pins both
counts below 65536, since each occupies half of the packed ID. Inserting a new
enumerator anywhere other than immediately before the count changes the numeric value
of everything after it, and therefore changes every `ExportID`.

`get_export_type()` and `get_export_format()` are asserting, not tolerant. Each
extracts its 16-bit field and asserts it is below the corresponding count, throwing
`PreconditionViolationError` otherwise. So an `ExportID` built from `INVALID_TYPE` or
`INVALID_FORMAT` is not a representable sentinel — it detonates on unpacking. Callers
that can hold "nothing selected" must keep the `Type` and `Format` separately and
check for the invalid values before packing, which is what
`ConfigureExportParametersDialog` does.

The four string accessors are the sharpest trap here. Each builds a function-local
static `std::map` on first call and then looks up with `operator[]` — which inserts a
default-constructed empty `QString` for a key that has no entry, rather than failing.
So an enumerator added to `Type` or `Format` without a matching line in the
corresponding `initialise_*_map()` produces a silently blank label or description in
the export dialogs, with no warning and no assertion. An empty extension cannot be
used to detect the omission either, because `CITCOMS_GLOBAL` and `TERRA_TEXT`
legitimately have none. Adding one enumerator means editing the enum plus up to four
map initialisers.

Two consequences of that `operator[]` follow. These functions look like pure getters
but mutate a shared static map, so they are not safe to call concurrently — in
practice everything here runs on the GUI thread. And because the maps are built inside
a function-local static, the `QObject::tr()` calls run once, at first use, and the
translated strings are cached for the life of the process; a language change after the
first export dialog has been opened will not be reflected. The returned
`const QString &` itself is stable — `std::map` does not invalidate references on
insertion.

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
