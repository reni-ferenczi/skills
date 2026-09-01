# entry-points

[Book TOC](../TOC.md)

The main() entry points and the Scribe export registration units.

9 unit page(s), 9 source file(s) documented here, 1 further file(s) listed below.

## Overview

[[[PROSE component unit=component:entry-points tier=1]]]
Replace this whole block, markers included, with 2-4 paragraphs: what this component is responsible for, the load-bearing units and how it connects to neighbouring components. Do not restate the unit table.
[[[/PROSE]]]

## Units

| Unit | Tier | Lines | Fan-in | Description |
|---|---|---|---|---|
| [ScribeExportGPlates](../src/entry-points/ScribeExportGPlates.md) | 3 | 47 | 0 | Registers polymorphic classes and types for Scribe serialization in the main GPlates application |
| [ScribeExportGPlatesDemoNoGui](../src/entry-points/ScribeExportGPlatesDemoNoGui.md) | 3 | 44 | 0 | Registers polymorphic classes and types for Scribe serialization in the headless demo application |
| [ScribeExportGPlatesUnitTest](../src/entry-points/ScribeExportGPlatesUnitTest.md) | 3 | 47 | 0 | Registers polymorphic classes and types for Scribe serialization in the unit test executable |
| [ScribeExportPyGPlates](../src/entry-points/ScribeExportPyGPlates.md) | 3 | 44 | 0 | Registers polymorphic classes and types for Scribe serialization in the pyGPlates dynamic library |
| [gplates-lib_pch](../src/entry-points/gplates-lib_pch.md) | 3 | 405 | 0 | Precompiled header combining frequently used external and standard library headers |
| [gplates_demo_no_gui_main](../src/entry-points/gplates_demo_no_gui_main.md) | 3 | 606 | 0 | Entry point for headless demo application demonstrating feature model and reconstruction engine |
| [gplates_main](../src/entry-points/gplates_main.md) | 3 | 994 | 3 | Entry point for GPlates handling both GUI and command-line operation modes |
| [gplates_unit_test_main](../src/entry-points/gplates_unit_test_main.md) | 3 | 181 | 0 | Entry point for unit test executable using Boost.Test framework |
| [pygplates_pch](../src/entry-points/pygplates_pch.md) | 3 | 405 | 0 | precompiled header bundling dependencies for the pyGPlates Python module build |

## Other files

| File | Kind | Lines |
|---|---|---|
| `src/CMakeLists.txt` | build | 917 |

## Depends on

| Component | References |
|---|---|
| [utils](utils.md) | 178 |
| [app-logic](app-logic.md) | 152 |
| [model](model.md) | 148 |
| [file-io](file-io.md) | 118 |
| [gui](gui.md) | 49 |
| [maths](maths.md) | 39 |
| [cli](cli.md) | 20 |
| [property-values](property-values.md) | 17 |
| [global](global.md) | 16 |
| [qt-widgets](qt-widgets.md) | 14 |
| [scribe](scribe.md) | 12 |
| [unit-test](unit-test.md) | 10 |
| [api](api.md) | 4 |
| [system-fixes](system-fixes.md) | 2 |
| [presentation](presentation.md) | 2 |
| [data-mining](data-mining.md) | 1 |

## Used by

| Component | References |
|---|---|
| [gui](gui.md) | 2 |
| [qt-widgets](qt-widgets.md) | 1 |

## Explore

Run these from the `gplates-code` skill directory:

```bash
python scripts/gpq.py tree src
python scripts/gpq.py sym . --mode sub --path src --defs-only
```
