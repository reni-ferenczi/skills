# ComponentManager

[Book TOC](../../TOC.md) · [utils](../../components/utils.md) · cluster Community 1122 · tier 2

| Source file | Kind | Lines |
|---|---|---|
| `src/utils/ComponentManager.h` | C++ | 137 |

## Overview

[[[PROSE overview unit=utils/ComponentManager tier=2]]]
Replace this whole block, markers included, with 1-3 paragraphs: what this unit is, why it exists, and how it fits the surrounding design. Do not restate the tables below.
[[[/PROSE]]]

## Declared types

| Name | Kind | Bases | Template | Subclasses | Description |
|---|---|---|---|---|---|
| [`GPlatesUtils::ComponentManager`](#gplatesutilscomponentmanager) | class | — | — | 0 | — |

## Members

### `GPlatesUtils::ComponentManager`

| Member | Kind | Type | Access | Description |
|---|---|---|---|---|
| `ComponentTypes` | enum | `None` | private | — |
| `Component` | class | `None` | public | — |
| `enable(Component t)` | method | `void` | public | — |
| `disable(Component t)` | method | `void` | public | — |
| `is_enabled(Component t)` | method | `bool` | public | — |
| `ComponentManager()` | constructor | `None` | private | — |
| `ComponentManager(const ComponentManager&)` | constructor | `None` | private | — |
| `operator=` | field | `ComponentManager` | private | — |
| `d_switchs` | field | `std::bitset<COMP_NUM>` | private | — |

## Free functions and macros

| Name | Kind | Type / body | Description |
|---|---|---|---|
| `GPLATES_UTILS_COMPONENT_MANAGER_H` | macro | `None` | — |

## Notes

[[[PROSE notes unit=utils/ComponentManager tier=2]]]
Replace this whole block, markers included, with invariants, ownership, threading or gotchas that are not visible in the tables. Write *None.* if there is nothing worth saying.
[[[/PROSE]]]

## Used by

| Unit | Component | References |
|---|---|---|
| [entry-points/gplates_main](../entry-points/gplates_main.md) | entry-points | 47 |
| [qt-widgets/HellingerThread](../qt-widgets/HellingerThread.md) | qt-widgets | 29 |
| [api/PythonRunner](../api/PythonRunner.md) | api | 20 |
| [api/CoReg](../api/CoReg.md) | api | 17 |
| [qt-widgets/ViewportWindow](../qt-widgets/ViewportWindow.md) | qt-widgets | 16 |
| [gui/DrawStyleAdapters](../gui/DrawStyleAdapters.md) | gui | 13 |
| [file-io/HellingerReader](../file-io/HellingerReader.md) | file-io | 11 |
| [qt-widgets/HellingerSegmentDialog](../qt-widgets/HellingerSegmentDialog.md) | qt-widgets | 11 |
| [api/ConsoleReader](../api/ConsoleReader.md) | api | 7 |
| [api/ConsoleWriter](../api/ConsoleWriter.md) | api | 7 |
| [api/PyApplication](../api/PyApplication.md) | api | 7 |
| [api/PythonUtils](../api/PythonUtils.md) | api | 7 |
| [gui/PythonManager](../gui/PythonManager.md) | gui | 7 |
| [api/PythonExecutionMonitor](../api/PythonExecutionMonitor.md) | api | 6 |
| [api/PythonExecutionThread](../api/PythonExecutionThread.md) | api | 6 |
| [presentation/ReconstructionGeometryRenderer](../presentation/ReconstructionGeometryRenderer.md) | presentation | 6 |
| [presentation/VisualLayerRegistry](../presentation/VisualLayerRegistry.md) | presentation | 6 |
| [qt-widgets/HellingerDialog](../qt-widgets/HellingerDialog.md) | qt-widgets | 6 |
| [qt-widgets/HellingerFitWidget](../qt-widgets/HellingerFitWidget.md) | qt-widgets | 6 |
| [qt-widgets/HellingerPointDialog](../qt-widgets/HellingerPointDialog.md) | qt-widgets | 6 |

*... and 25 more units.*

## Related

*None.*

## Explore

Run these from the `gplates-code` skill directory:

```bash
python scripts/gpq.py file src/utils/ComponentManager.h
python scripts/gpq.py def GPlatesUtils::ComponentManager --body
python scripts/gpq.py uses ComponentManager --kind class
python scripts/gpq.py hier ComponentManager
```
