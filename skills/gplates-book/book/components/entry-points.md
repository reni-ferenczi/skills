# entry-points

[Book TOC](../TOC.md)

The main() entry points and the Scribe export registration units.

9 unit page(s), 9 source file(s) documented here, 1 further file(s) listed below.

## Overview

This component is where the four build products of the GPlates tree — the `gplates` application, the `gplates-no-gui` demo, the `gplates-unit-test` executable, and the `pygplates` Python extension module — each get their `main()` (or module-init) entry point, their Scribe type-registration unit, and, for the two large binaries, their precompiled header. `src/CMakeLists.txt` is the switchboard behind all of it: it branches on `GPLATES_BUILD_GPLATES` to decide which of these targets to configure, links `gplates`, `gplates-no-gui` and `gplates-unit-test` against a shared static library `gplates-lib` built from the rest of the source tree, and builds `pygplates` as a separate position-independent module that compiles the same sources again rather than linking against `gplates-lib`. When `GPLATES_USE_PRECOMPILED_HEADERS` is set, `gplates-lib` and `pygplates` each get their own `_pch.h` precompiled onto the whole target, since they carry the largest amount of source code.

`gplates_main` is the load-bearing unit of the whole component: it parses command-line arguments to decide between launching the interactive GUI or dispatching to a non-GUI CLI command, and for GUI mode it constructs the Qt `QApplication`, creates the presentation-layer `Application` singleton, optionally initializes embedded Python, loads any project or feature-collection files named on the command line, and runs the Qt event loop. Its `main()` deliberately wraps an `internal_main()` so that the `Application` object is created and destroyed strictly inside that inner call, before `QApplication` itself is torn down, and so uncaught exceptions can be reported without leaving the Qt event thread in an inconsistent state. `gplates_demo_no_gui_main` is a much smaller, self-contained entry point that builds hard-coded GPGIM features directly against the model and reconstruction engine and writes the results out as GPML, without any Qt GUI — it exists to exercise the model, file-io and app-logic layers in isolation. `gplates_unit_test_main` boots just enough of Qt (OpenGL, Python, GPGIM, widgets) to let the Boost.Test-based suite run, then hands control to the registered test-suite hierarchy. The two precompiled headers, `gplates-lib_pch` and `pygplates_pch`, aggregate the external and standard-library headers (Boost, Qt, Python, CGAL, OpenGL, OGR/GDAL) common to their respective targets so those headers are parsed once rather than per translation unit. The four `ScribeExport*` units each define one macro — `SCRIBE_EXPORT_GPLATES`, `SCRIBE_EXPORT_GPLATES_DEMO_NO_GUI`, `SCRIBE_EXPORT_GPLATES_UNIT_TEST`, `SCRIBE_EXPORT_PYGPLATES` — that assembles, per binary, the set of polymorphic classes the `scribe` serialization framework must register at startup so that framework's project save/load format works; the GUI and CLI binary pulls in the `data-mining` export group in addition to the external types, the unit-test binary pulls in the `unit-test` group instead, and the demo and pygplates binaries register only the external types.

Because everything else in the tree ends up linked into one of these four targets, entry-points depends heavily but shallowly on the rest of the codebase: its heaviest ties are to utils, app-logic and model (the layers `gplates_main` and `gplates_demo_no_gui_main` drive directly to build features and run reconstructions), to file-io (for loading the project and feature-collection files named on the command line), and to gui, maths, cli, property-values and scribe for the pieces each entry point wires together at startup. The relationship runs almost entirely one way: only gui (`GPlatesQApplication`) and qt-widgets (`ViewportWindow`) reach back into entry-points, each referencing `gplates_main` to coordinate application startup and shutdown with the code that owns the event loop.

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
