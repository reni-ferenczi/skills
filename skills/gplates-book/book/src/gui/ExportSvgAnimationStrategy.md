# ExportSvgAnimationStrategy

[Book TOC](../../TOC.md) · [gui](../../components/gui.md) · cluster Community 433 · tier 2

| Source file | Kind | Lines |
|---|---|---|
| `src/gui/ExportSvgAnimationStrategy.h` | C++ | 136 |
| `src/gui/ExportSvgAnimationStrategy.cc` | C++ | 134 |

## Overview

[[[PROSE overview unit=gui/ExportSvgAnimationStrategy tier=2]]]
Replace this whole block, markers included, with 1-3 paragraphs: what this unit is, why it exists, and how it fits the surrounding design. Do not restate the tables below.
[[[/PROSE]]]

## Declared types

| Name | Kind | Bases | Template | Subclasses | Description |
|---|---|---|---|---|---|
| [`GPlatesGui::ExportSvgAnimationStrategy`](#gplatesguiexportsvganimationstrategy) | class | [`GPlatesGui::ExportAnimationStrategy`](ExportAnimationStrategy.md) | — | 0 | Concrete implementation of the ExportAnimationStrategy class for writing SVG snapshots of the globe. |

## Members

### `GPlatesGui::ExportSvgAnimationStrategy`

| Member | Kind | Type | Access | Description |
|---|---|---|---|---|
| `non_null_ptr_type` | typedef | `GPlatesUtils::non_null_intrusive_ptr<ExportSvgAnimationStrategy>` | public | A convenience typedef for GPlatesUtils::non\_null\_intrusive\_ptr\<ExportSvgAnimationStrategy\>. |
| `Configuration` | class | `None` | public | Configuration options.. |
| `const_configuration_ptr` | typedef | `boost::shared_ptr<const Configuration>` | public | Typedef for a shared pointer to const Configuration. |
| `create( ExportAnimationContext &export_animation_context, const const_configuration_ptr &export_configuration)` | method | `non_null_ptr_type` | public | — |
| `~ExportSvgAnimationStrategy()` | destructor | `None` | public | — |
| `do_export_iteration( std::size_t frame_index)` | method | `bool` | public | Does one frame of export. |
| `ExportSvgAnimationStrategy( GPlatesGui::ExportAnimationContext &export_animation_context, const const_configuration_ptr &cfg)` | constructor | `None` | protected | Protected constructor to prevent instantiation on the stack. |
| `d_configuration` | field | `const_configuration_ptr` | private | Export configuration parameters. |

## Free functions and macros

| Name | Kind | Type / body | Description |
|---|---|---|---|
| `GPLATES_GUI_EXPORTSVGANIMATIONSTRATEGY_H` | macro | `None` | — |

## Notes

[[[PROSE notes unit=gui/ExportSvgAnimationStrategy tier=2]]]
Replace this whole block, markers included, with invariants, ownership, threading or gotchas that are not visible in the tables. Write *None.* if there is nothing worth saying.
[[[/PROSE]]]

## Used by

| Unit | Component | References |
|---|---|---|
| [qt-widgets/ExportSvgOptionsWidget](../qt-widgets/ExportSvgOptionsWidget.md) | qt-widgets | 17 |
| [gui/ExportAnimationRegistry](ExportAnimationRegistry.md) | gui | 5 |
| [gui/ExportAnimationContext](ExportAnimationContext.md) | gui | 1 |

## Related

*None.*

## Explore

Run these from the `gplates-code` skill directory:

```bash
python scripts/gpq.py file src/gui/ExportSvgAnimationStrategy.h
python scripts/gpq.py def GPlatesGui::ExportSvgAnimationStrategy --body
python scripts/gpq.py uses ExportSvgAnimationStrategy --kind class
python scripts/gpq.py hier ExportSvgAnimationStrategy
```
