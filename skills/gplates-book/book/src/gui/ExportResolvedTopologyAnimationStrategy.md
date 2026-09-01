# ExportResolvedTopologyAnimationStrategy

[Book TOC](../../TOC.md) · [gui](../../components/gui.md) · cluster Community 48 · tier 2

| Source file | Kind | Lines |
|---|---|---|
| `src/gui/ExportResolvedTopologyAnimationStrategy.h` | C++ | 180 |
| `src/gui/ExportResolvedTopologyAnimationStrategy.cc` | C++ | 168 |

## Overview

[[[PROSE overview unit=gui/ExportResolvedTopologyAnimationStrategy tier=2]]]
Replace this whole block, markers included, with 1-3 paragraphs: what this unit is, why it exists, and how it fits the surrounding design. Do not restate the tables below.
[[[/PROSE]]]

## Declared types

| Name | Kind | Bases | Template | Subclasses | Description |
|---|---|---|---|---|---|
| [`GPlatesGui::ExportResolvedTopologyAnimationStrategy`](#gplatesguiexportresolvedtopologyanimationstrategy) | class | [`GPlatesGui::ExportAnimationStrategy`](ExportAnimationStrategy.md) | — | 0 | Concrete implementation of the ExportAnimationStrategy class for exporting resolved topologies in a general manner (as opposed to the CitcomS-specific manner). |

## Members

### `GPlatesGui::ExportResolvedTopologyAnimationStrategy`

| Member | Kind | Type | Access | Description |
|---|---|---|---|---|
| `non_null_ptr_type` | typedef | `GPlatesUtils::non_null_intrusive_ptr<ExportResolvedTopologyAnimationStrategy>` | public | A convenience typedef for GPlatesUtils::non\_null\_intrusive\_ptr\<ExportResolvedTopologyAnimationStrategy\>. |
| `Configuration` | class | `None` | public | Configuration options. |
| `const_configuration_ptr` | typedef | `boost::shared_ptr<const Configuration>` | public | Typedef for a shared pointer to const Configuration. |
| `create( ExportAnimationContext &export_animation_context, const const_configuration_ptr &cfg)` | method | `non_null_ptr_type` | public | — |
| `~ExportResolvedTopologyAnimationStrategy()` | destructor | `None` | public | — |
| `do_export_iteration( std::size_t frame_index)` | method | `bool` | public | Does one frame of export. |
| `ExportResolvedTopologyAnimationStrategy( GPlatesGui::ExportAnimationContext &export_animation_context, const const_configuration_ptr &cfg)` | constructor | `None` | protected | Protected constructor to prevent instantiation on the stack. |
| `d_loaded_files` | field | `GPlatesViewOperations::VisibleReconstructionGeometryExport::files_collection_type` | private | The list of currently loaded files. |
| `d_loaded_reconstruction_files` | field | `GPlatesViewOperations::VisibleReconstructionGeometryExport::files_collection_type` | private | The active and loaded reconstruction file(s) used in the reconstruction. |
| `d_configuration` | field | `const_configuration_ptr` | private | Export configuration parameters. |

## Free functions and macros

| Name | Kind | Type / body | Description |
|---|---|---|---|
| `GPLATES_GUI_EXPORTRESOLVEDTOPOLOGYANIMATIONSTRATEGY_H` | macro | `None` | — |

## Notes

[[[PROSE notes unit=gui/ExportResolvedTopologyAnimationStrategy tier=2]]]
Replace this whole block, markers included, with invariants, ownership, threading or gotchas that are not visible in the tables. Write *None.* if there is nothing worth saying.
[[[/PROSE]]]

## Used by

| Unit | Component | References |
|---|---|---|
| [qt-widgets/ExportResolvedTopologyOptionsWidget](../qt-widgets/ExportResolvedTopologyOptionsWidget.md) | qt-widgets | 46 |
| [gui/ExportAnimationRegistry](ExportAnimationRegistry.md) | gui | 21 |
| [file-io/GMTFormatResolvedTopologicalGeometryExport](../file-io/GMTFormatResolvedTopologicalGeometryExport.md) | file-io | 1 |

## Related

*None.*

## Explore

Run these from the `gplates-code` skill directory:

```bash
python scripts/gpq.py file src/gui/ExportResolvedTopologyAnimationStrategy.h
python scripts/gpq.py def GPlatesGui::ExportResolvedTopologyAnimationStrategy --body
python scripts/gpq.py uses ExportResolvedTopologyAnimationStrategy --kind class
python scripts/gpq.py hier ExportResolvedTopologyAnimationStrategy
```
