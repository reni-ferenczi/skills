# ComponentManager

[Book TOC](../../TOC.md) · [utils](../../components/utils.md) · cluster Community 1122 · tier 2

| Source file | Kind | Lines |
|---|---|---|
| `src/utils/ComponentManager.h` | C++ | 137 |

## Overview

`GPlatesUtils::ComponentManager` is a process-wide singleton (`instance()`, a
Meyers singleton) that tracks which optional feature areas of GPlates —
`DATA_MINING`, `PYTHON`, `SYMBOLOGY`, `HELLINGER_THREE_PLATE` — are currently
enabled, backed by a fixed-size `std::bitset`. It gives widely scattered code
(the API bindings, dialogs, presentation layer) a single yes/no gate to check
before offering or running a feature, instead of threading a build flag or
preference value through every call site.

The nested `Component` class is the only way to name one of the enum values
from outside the manager: it exposes named factory functions
(`Component::python()`, `Component::symbology()`, …) that convert implicitly
to the bitset index, so callers never see or depend on the raw
`ComponentTypes` enum, which stays private.

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

- `Component::python()` is enabled by default in the constructor; every other
  component starts disabled and must be turned on explicitly with `enable()`.
- The class is non-copyable (copy constructor and `operator=` are private and
  unimplemented) and reachable only through `instance()` — there is no way to
  construct a second, independent `ComponentManager`.
- `std::bitset` access is not synchronised; concurrent `enable()`/`disable()`/
  `is_enabled()` calls from different threads are not safe against each
  other.

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
