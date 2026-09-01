# ExportAnimationStrategy

[Book TOC](../../TOC.md) · [gui](../../components/gui.md) · cluster Community 251 · tier 1

| Source file | Kind | Lines |
|---|---|---|
| `src/gui/ExportAnimationStrategy.h` | C++ | 201 |
| `src/gui/ExportAnimationStrategy.cc` | C++ | 114 |

## Overview

[[[PROSE overview unit=gui/ExportAnimationStrategy tier=1]]]
Replace this whole block, markers included, with 1-3 paragraphs: what this unit is, why it exists, and how it fits the surrounding design. Do not restate the tables below.
[[[/PROSE]]]

## Declared types

| Name | Kind | Bases | Template | Subclasses | Description |
|---|---|---|---|---|---|
| [`GPlatesGui::ExportAnimationStrategy`](#gplatesguiexportanimationstrategy) | class | [`GPlatesUtils::ReferenceCount<ExportAnimationStrategy>`](../utils/ReferenceCount.md) | — | 15 | Base class for the different Export Animation strategies. |

## Members

### `GPlatesGui::ExportAnimationStrategy`

| Member | Kind | Type | Access | Description |
|---|---|---|---|---|
| `non_null_ptr_type` | typedef | `GPlatesUtils::non_null_intrusive_ptr<ExportAnimationStrategy>` | public | A convenience typedef for GPlatesUtils::non\_null\_intrusive\_ptr\<ExportAnimationStrategy\>. |
| `~ExportAnimationStrategy()` | destructor | `None` | public | — |
| `const_configuration_base_ptr` | typedef | `boost::shared_ptr<const ConfigurationBase>` | public | Typedef for a shared pointer to const ConfigurationBase. |
| `configuration_base_ptr` | typedef | `boost::shared_ptr<ConfigurationBase>` | public | Typedef for a shared pointer to ConfigurationBase. |
| `ConfigurationBase` | class | `None` | public | Configuration parameters for an ExportAnimationStrategy. |
| `create( GPlatesGui::ExportAnimationContext &export_animation_context)` | method | `non_null_ptr_type` | public | Creates an export animation strategy that doesn't do anything. |
| `set_template_filename( const QString &filename)` | method | `void` | public | Sets the internal ExportTemplateFilenameSequence. |
| `do_export_iteration( std::size_t frame_index)` | method | `bool` | public | Does one frame of export. |
| `wrap_up( bool export_successful)` | method | `void` | public | Allows Strategy objects to do any housekeeping that might be necessary after all export iterations are completed. |
| `check_filename_sequence()` | method | `bool` | public | — |
| `ExportAnimationStrategy( GPlatesGui::ExportAnimationContext &export_animation_context)` | constructor | `None` | protected | Protected constructor to prevent instantiation on the stack. |
| `d_export_animation_context_ptr` | field | `GPlatesGui::ExportAnimationContext` | protected | Pointer back to the Context, as an easy way to get at all kinds of state. |
| `d_filename_sequence_opt` | field | `boost::optional<GPlatesFileIO::ExportTemplateFilenameSequence>` | protected | The filename sequence to use when exporting. |
| `d_filename_iterator_opt` | field | `boost::optional<GPlatesFileIO::ExportTemplateFilenameSequence::const_iterator>` | protected | — |

## Free functions and macros

| Name | Kind | Type / body | Description |
|---|---|---|---|
| `GPLATES_GUI_EXPORTANIMATIONSTRATEGY_H` | macro | `None` | — |

## Notes

[[[PROSE notes unit=gui/ExportAnimationStrategy tier=1]]]
Replace this whole block, markers included, with invariants, ownership, threading or gotchas that are not visible in the tables. Write *None.* if there is nothing worth saying.
[[[/PROSE]]]

## Used by

| Unit | Component | References |
|---|---|---|
| [gui/ExportAnimationRegistry](ExportAnimationRegistry.md) | gui | 48 |
| [gui/ExportVelocityAnimationStrategy](ExportVelocityAnimationStrategy.md) | gui | 34 |
| [gui/ExportNetRotationAnimationStrategy](ExportNetRotationAnimationStrategy.md) | gui | 30 |
| [qt-widgets/ConfigureExportParametersDialog](../qt-widgets/ConfigureExportParametersDialog.md) | qt-widgets | 30 |
| [qt-widgets/ExportAnimationDialog](../qt-widgets/ExportAnimationDialog.md) | qt-widgets | 26 |
| [gui/ExportDeformationAnimationStrategy](ExportDeformationAnimationStrategy.md) | gui | 24 |
| [gui/ExportScalarCoverageAnimationStrategy](ExportScalarCoverageAnimationStrategy.md) | gui | 24 |
| [gui/ExportRasterAnimationStrategy](ExportRasterAnimationStrategy.md) | gui | 22 |
| [qt-widgets/EditExportParametersDialog](../qt-widgets/EditExportParametersDialog.md) | qt-widgets | 21 |
| [gui/ExportCitcomsResolvedTopologyAnimationStrategy](ExportCitcomsResolvedTopologyAnimationStrategy.md) | gui | 20 |
| [gui/ExportFlowlineAnimationStrategy](ExportFlowlineAnimationStrategy.md) | gui | 20 |
| [gui/ExportMotionPathAnimationStrategy](ExportMotionPathAnimationStrategy.md) | gui | 20 |
| [gui/ExportReconstructedGeometryAnimationStrategy](ExportReconstructedGeometryAnimationStrategy.md) | gui | 20 |
| [gui/ExportResolvedTopologyAnimationStrategy](ExportResolvedTopologyAnimationStrategy.md) | gui | 20 |
| [gui/ExportImageAnimationStrategy](ExportImageAnimationStrategy.md) | gui | 16 |
| [gui/ExportSvgAnimationStrategy](ExportSvgAnimationStrategy.md) | gui | 16 |
| [gui/ExportCoRegistrationAnimationStrategy](ExportCoRegistrationAnimationStrategy.md) | gui | 13 |
| [gui/ExportStageRotationAnimationStrategy](ExportStageRotationAnimationStrategy.md) | gui | 12 |
| [gui/ExportTotalRotationAnimationStrategy](ExportTotalRotationAnimationStrategy.md) | gui | 12 |
| [gui/ExportAnimationContext](ExportAnimationContext.md) | gui | 11 |

*... and 15 more units.*

## Related

*None.*

## Explore

Run these from the `gplates-code` skill directory:

```bash
python scripts/gpq.py file src/gui/ExportAnimationStrategy.h
python scripts/gpq.py def GPlatesGui::ExportAnimationStrategy --body
python scripts/gpq.py uses ExportAnimationStrategy --kind class
python scripts/gpq.py hier ExportAnimationStrategy
```
