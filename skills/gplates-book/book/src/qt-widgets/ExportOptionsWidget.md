# ExportOptionsWidget

[Book TOC](../../TOC.md) · [qt-widgets](../../components/qt-widgets.md) · cluster Community 235 · tier 2

| Source file | Kind | Lines |
|---|---|---|
| `src/qt-widgets/ExportOptionsWidget.h` | C++ | 68 |

## Overview

`ExportOptionsWidget` is the abstract base for the per-export-type option panels shown inside `ConfigureExportParametersDialog` and `EditExportParametersDialog` — one concrete subclass per `ExportAnimationType` (raster, SVG, velocity, rotation, and so on). Its single pure virtual, `create_export_animation_strategy_configuration()`, is the contract every subclass must fulfil: read back whatever controls it added, and package them together with the caller-supplied filename template into an `ExportAnimationStrategy::const_configuration_base_ptr` that the export machinery in `ExportAnimationContext` can act on uniformly regardless of which export type is selected.

## Declared types

| Name | Kind | Bases | Template | Subclasses | Description |
|---|---|---|---|---|---|
| [`GPlatesQtWidgets::ExportOptionsWidget`](#gplatesqtwidgetsexportoptionswidget) | class | `QWidget` | — | 14 | This is the abstract base class of widgets used to display export options particular to different export animation types. |

## Members

### `GPlatesQtWidgets::ExportOptionsWidget`

| Member | Kind | Type | Access | Description |
|---|---|---|---|---|
| `ExportOptionsWidget( QWidget *parent_)` | constructor | `None` | public | — |
| `~ExportOptionsWidget()` | destructor | `None` | public | — |
| `create_export_animation_strategy_configuration( const QString &filename_template)` | method | `GPlatesGui::ExportAnimationStrategy::const_configuration_base_ptr` | public | Collects the options specified by the user and returns them as an export animation strategy configuration. |

## Free functions and macros

| Name | Kind | Type / body | Description |
|---|---|---|---|
| `GPLATES_QT_WIDGETS_EXPORTOPTIONSWIDGET_H` | macro | `None` | — |

## Notes

*None.*

## Used by

| Unit | Component | References |
|---|---|---|
| [qt-widgets/ExportRasterOptionsWidget](ExportRasterOptionsWidget.md) | qt-widgets | 16 |
| [qt-widgets/ExportCitcomsResolvedTopologyOptionsWidget](ExportCitcomsResolvedTopologyOptionsWidget.md) | qt-widgets | 4 |
| [qt-widgets/ExportDeformationOptionsWidget](ExportDeformationOptionsWidget.md) | qt-widgets | 4 |
| [qt-widgets/ExportFlowlineOptionsWidget](ExportFlowlineOptionsWidget.md) | qt-widgets | 4 |
| [qt-widgets/ExportImageOptionsWidget](ExportImageOptionsWidget.md) | qt-widgets | 4 |
| [qt-widgets/ExportMotionPathOptionsWidget](ExportMotionPathOptionsWidget.md) | qt-widgets | 4 |
| [qt-widgets/ExportNetRotationOptionsWidget](ExportNetRotationOptionsWidget.md) | qt-widgets | 4 |
| [qt-widgets/ExportReconstructedGeometryOptionsWidget](ExportReconstructedGeometryOptionsWidget.md) | qt-widgets | 4 |
| [qt-widgets/ExportResolvedTopologyOptionsWidget](ExportResolvedTopologyOptionsWidget.md) | qt-widgets | 4 |
| [qt-widgets/ExportScalarCoverageOptionsWidget](ExportScalarCoverageOptionsWidget.md) | qt-widgets | 4 |
| [qt-widgets/ExportStageRotationOptionsWidget](ExportStageRotationOptionsWidget.md) | qt-widgets | 4 |
| [qt-widgets/ExportSvgOptionsWidget](ExportSvgOptionsWidget.md) | qt-widgets | 4 |
| [qt-widgets/ExportTotalRotationOptionsWidget](ExportTotalRotationOptionsWidget.md) | qt-widgets | 4 |
| [qt-widgets/ExportVelocityOptionsWidget](ExportVelocityOptionsWidget.md) | qt-widgets | 4 |
| [qt-widgets/ConfigureExportParametersDialog](ConfigureExportParametersDialog.md) | qt-widgets | 2 |
| [qt-widgets/EditExportParametersDialog](EditExportParametersDialog.md) | qt-widgets | 2 |
| [qt-widgets/ExportFileOptionsWidget](ExportFileOptionsWidget.md) | qt-widgets | 1 |
| [qt-widgets/ExportImageResolutionOptionsWidget](ExportImageResolutionOptionsWidget.md) | qt-widgets | 1 |
| [qt-widgets/ExportRotationOptionsWidget](ExportRotationOptionsWidget.md) | qt-widgets | 1 |
| [qt-widgets/ExportStageRotationOnlyOptionsWidget](ExportStageRotationOnlyOptionsWidget.md) | qt-widgets | 1 |

*... and 1 more units.*

## Related

*None.*

## Explore

Run these from the `gplates-code` skill directory:

```bash
python scripts/gpq.py file src/qt-widgets/ExportOptionsWidget.h
python scripts/gpq.py def GPlatesQtWidgets::ExportOptionsWidget --body
python scripts/gpq.py uses ExportOptionsWidget --kind class
python scripts/gpq.py hier ExportOptionsWidget
```
