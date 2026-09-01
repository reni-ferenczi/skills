# ExportOptionsUtils

[Book TOC](../../TOC.md) · [gui](../../components/gui.md) · cluster Community 85 · tier 2

| Source file | Kind | Lines |
|---|---|---|
| `src/gui/ExportOptionsUtils.h` | C++ | 206 |

## Overview

[[[PROSE overview unit=gui/ExportOptionsUtils tier=2]]]
Replace this whole block, markers included, with 1-3 paragraphs: what this unit is, why it exists, and how it fits the surrounding design. Do not restate the tables below.
[[[/PROSE]]]

## Declared types

| Name | Kind | Bases | Template | Subclasses | Description |
|---|---|---|---|---|---|
| [`GPlatesGui::ExportOptionsUtils::ExportFileOptions`](#gplatesguiexportoptionsutilsexportfileoptions) | struct | — | — | 0 | Options useful when exporting to Shapefile - either a single file or multiple files. |
| [`GPlatesGui::ExportOptionsUtils::ExportImageResolutionOptions`](#gplatesguiexportoptionsutilsexportimageresolutionoptions) | struct | — | — | 0 | Common image resolution options useful when exporting either screenshots or to SVG. |
| [`GPlatesGui::ExportOptionsUtils::ExportRotationOptions`](#gplatesguiexportoptionsutilsexportrotationoptions) | struct | — | — | 0 | Common rotations options useful when exporting either total or stage rotations. |
| [`GPlatesGui::ExportOptionsUtils::ExportStageRotationOptions`](#gplatesguiexportoptionsutilsexportstagerotationoptions) | struct | — | — | 0 | Rotations options useful when exporting \*stage\* rotations only. |
| [`GPlatesGui::ExportOptionsUtils::ExportVelocityCalculationOptions`](#gplatesguiexportoptionsutilsexportvelocitycalculationoptions) | struct | — | — | 0 | Velocity calculation options. |
| [`GPlatesGui::ExportOptionsUtils::ExportNetRotationOptions`](#gplatesguiexportoptionsutilsexportnetrotationoptions) | struct | — | — | 0 | Net Rotation options |

## Members

### `GPlatesGui::ExportOptionsUtils::ExportFileOptions`

| Member | Kind | Type | Access | Description |
|---|---|---|---|---|
| `ExportFileOptions( bool export_to_a_single_file_ = true, bool export_to_multiple_files_ = true, bool separate_output_directory_per_file_ = true)` | constructor | `None` | public | — |
| `export_to_a_single_file` | field | `bool` | public | Export all ReconstructionGeometry derived objects to a single export file. |
| `export_to_multiple_files` | field | `bool` | public | Export ReconstructionGeometry derived objects to multiple export files. |
| `separate_output_directory_per_file` | field | `bool` | public | If 'true' then the \*multiple\* export files will follow the pattern... "\<export\_path\>/\<collection\_filename\>/\<export\_template\_filename\>" ...otherwise they will follow the pattern... ... |

### `GPlatesGui::ExportOptionsUtils::ExportImageResolutionOptions`

| Member | Kind | Type | Access | Description |
|---|---|---|---|---|
| `ExportImageResolutionOptions( bool constrain_aspect_ratio_, boost::optional<QSize> image_size_ = boost::none)` | constructor | `None` | public | — |
| `image_size` | field | `boost::optional<QSize>` | public | Image size - boost::none means use the current globe/map viewport dimensions. |
| `constrain_aspect_ratio` | field | `bool` | public | Whether to keep the ratio of width to height constant. |

### `GPlatesGui::ExportOptionsUtils::ExportRotationOptions`

| Member | Kind | Type | Access | Description |
|---|---|---|---|---|
| `IdentityRotationFormatType` | enum | `None` | public | How to write out an identity rotation. |
| `EulerPoleFormatType` | enum | `None` | public | How to write out a Euler pole. |
| `ExportRotationOptions( IdentityRotationFormatType identity_rotation_format_, EulerPoleFormatType euler_pole_format_)` | constructor | `None` | public | — |
| `identity_rotation_format` | field | `IdentityRotationFormatType` | public | — |
| `euler_pole_format` | field | `EulerPoleFormatType` | public | — |

### `GPlatesGui::ExportOptionsUtils::ExportStageRotationOptions`

| Member | Kind | Type | Access | Description |
|---|---|---|---|---|
| `ExportStageRotationOptions( const double &time_interval_)` | constructor | `None` | public | — |
| `time_interval` | field | `double` | public | The stage rotation time interval (in My). |

### `GPlatesGui::ExportOptionsUtils::ExportVelocityCalculationOptions`

| Member | Kind | Type | Access | Description |
|---|---|---|---|---|
| `ExportVelocityCalculationOptions( GPlatesAppLogic::VelocityDeltaTime::Type delta_time_type_, const double &delta_time_, bool is_boundary_smoothing_enabled_, const double &boundary_smoothing_angular_half_extent_degrees_, bool exclude_deforming_regions_)` | constructor | `None` | public | — |
| `delta_time_type` | field | `GPlatesAppLogic::VelocityDeltaTime::Type` | public | — |
| `delta_time` | field | `double` | public | — |
| `is_boundary_smoothing_enabled` | field | `bool` | public | — |
| `boundary_smoothing_angular_half_extent_degrees` | field | `double` | public | — |
| `exclude_deforming_regions` | field | `bool` | public | — |

### `GPlatesGui::ExportOptionsUtils::ExportNetRotationOptions`

| Member | Kind | Type | Access | Description |
|---|---|---|---|---|
| `ExportNetRotationOptions( const double &delta_time_, const GPlatesQtWidgets::VelocityMethodWidget::VelocityMethod &velocity_method_)` | constructor | `None` | public | — |
| `delta_time` | field | `double` | public | — |
| `velocity_method` | field | `GPlatesQtWidgets::VelocityMethodWidget::VelocityMethod` | public | — |

## Free functions and macros

| Name | Kind | Type / body | Description |
|---|---|---|---|
| `GPLATES_GUI_EXPORTOPTIONSUTILS_H` | macro | `None` | — |

## Notes

[[[PROSE notes unit=gui/ExportOptionsUtils tier=2]]]
Replace this whole block, markers included, with invariants, ownership, threading or gotchas that are not visible in the tables. Write *None.* if there is nothing worth saying.
[[[/PROSE]]]

## Used by

| Unit | Component | References |
|---|---|---|
| [gui/ExportVelocityAnimationStrategy](ExportVelocityAnimationStrategy.md) | gui | 34 |
| [qt-widgets/ExportRotationOptionsWidget](../qt-widgets/ExportRotationOptionsWidget.md) | qt-widgets | 33 |
| [gui/ExportAnimationRegistry](ExportAnimationRegistry.md) | gui | 32 |
| [qt-widgets/ExportImageResolutionOptionsWidget](../qt-widgets/ExportImageResolutionOptionsWidget.md) | qt-widgets | 25 |
| [qt-widgets/ExportVelocityCalculationOptionsWidget](../qt-widgets/ExportVelocityCalculationOptionsWidget.md) | qt-widgets | 25 |
| [gui/ExportStageRotationAnimationStrategy](ExportStageRotationAnimationStrategy.md) | gui | 24 |
| [gui/ExportTotalRotationAnimationStrategy](ExportTotalRotationAnimationStrategy.md) | gui | 19 |
| [qt-widgets/ExportFileOptionsWidget](../qt-widgets/ExportFileOptionsWidget.md) | qt-widgets | 16 |
| [gui/ExportDeformationAnimationStrategy](ExportDeformationAnimationStrategy.md) | gui | 15 |
| [gui/ExportScalarCoverageAnimationStrategy](ExportScalarCoverageAnimationStrategy.md) | gui | 15 |
| [qt-widgets/ExportStageRotationOnlyOptionsWidget](../qt-widgets/ExportStageRotationOnlyOptionsWidget.md) | qt-widgets | 10 |
| [gui/ExportFlowlineAnimationStrategy](ExportFlowlineAnimationStrategy.md) | gui | 8 |
| [gui/ExportMotionPathAnimationStrategy](ExportMotionPathAnimationStrategy.md) | gui | 8 |
| [gui/ExportReconstructedGeometryAnimationStrategy](ExportReconstructedGeometryAnimationStrategy.md) | gui | 8 |
| [gui/ExportResolvedTopologyAnimationStrategy](ExportResolvedTopologyAnimationStrategy.md) | gui | 8 |
| [gui/ExportImageAnimationStrategy](ExportImageAnimationStrategy.md) | gui | 7 |
| [gui/ExportNetRotationAnimationStrategy](ExportNetRotationAnimationStrategy.md) | gui | 7 |
| [gui/ExportSvgAnimationStrategy](ExportSvgAnimationStrategy.md) | gui | 7 |
| [qt-widgets/ExportNetRotationOptionsWidget](../qt-widgets/ExportNetRotationOptionsWidget.md) | qt-widgets | 7 |

## Related

*None.*

## Explore

Run these from the `gplates-code` skill directory:

```bash
python scripts/gpq.py file src/gui/ExportOptionsUtils.h
python scripts/gpq.py def GPlatesGui::ExportOptionsUtils::ExportFileOptions --body
python scripts/gpq.py uses ExportFileOptions --kind struct
python scripts/gpq.py hier ExportFileOptions
```
