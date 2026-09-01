# cli

[Book TOC](../TOC.md)

12 unit page(s), 20 source file(s) documented here, 1 further file(s) listed below.

## Overview

`cli` is GPlates' headless, non-interactive front end: a `boost::program_options`-driven executable mode that runs a single named batch operation and exits, instead of launching the Qt GUI's event loop. It exposes a fixed set of reconstruction-pipeline operations as sub-commands — assigning plate IDs to features by cookie-cutting them against a set of polygons, reconstructing feature collections to a paleo time, converting between feature-collection file formats, and computing equivalent, relative or stage rotation poles between plates — so that these operations can be scripted from the command line without any windowing system.

The dispatch machinery is small and uniform: `Command` is the pure interface every sub-command implements (name, description, contributed options, and a `run()` that acts on the parsed `variables_map`); `CommandRegistry` lists the available command classes as a compile-time Boost.MPL vector; and `CommandDispatcher` walks that vector at construction to instantiate one `Command` per registered type, then looks commands up by name and dispatches to whichever one the user typed on argv. `FeatureCollectionFileIO` is the component's most load-bearing unit by a wide margin — every file-touching command builds on it to load feature collections into a `ModelInterface` and save them back out, translating the small set of `--save-file-type` strings into a `FeatureCollectionFileFormat::Format` and deriving output filenames, all without needing the GUI's `FeatureCollectionFileState` or layer machinery. `RequiredOptionNotPresent` and `InvalidOptionValue` are the two exceptions that every command and `FeatureCollectionFileIO` itself throw when a required option is missing or a supplied value cannot be parsed, giving `run()` a single, uniform failure channel that callers can catch and report. The six concrete commands — `AssignPlateIdsCommand`, `ReconstructCommand`, `ConvertFileFormatCommand`, `EquivalentTotalRotationCommand`, `RelativeTotalRotationCommand` and `StageRotationCommand` — are the component's actual payload: each parses its own options, drives the reconstruction engine to produce a result, and either saves feature collections or prints a rotation pole.

Because every command ultimately loads files and runs the reconstruction engine, `cli` leans heavily on the layers beneath the GUI: `file-io` supplies the concrete format readers and writers that `FeatureCollectionFileIO` wraps; `model` supplies `ModelInterface` and `FeatureCollectionHandle`, the containers every loaded feature collection is held in; `app-logic` supplies the reconstruction machinery itself — `ReconstructionTree`, `AssignPlateIds`, `RotationUtils`, `ReconstructParams` — that each command calls to compute plate motions; and `maths` supplies the finite-rotation and Euler-pole types the rotation commands print. `global` contributes only the `Exception` base class the two CLI exceptions derive from. The dependency runs the other way for `entry-points`: `gplates_main` builds a `CommandDispatcher` and, when invoked with a command name, dispatches straight to it instead of starting the GUI — the one point where the headless and windowed builds fork. The smaller edges from `qt-widgets` and `gui` are not the CLI depending on the GUI but the reverse: widgets such as `HellingerDialog` and `MapProjection` reuse `RequiredOptionNotPresent` as a convenient, ready-made exception for their own option-style validation, independent of the command-line pipeline.

## Units

| Unit | Tier | Lines | Fan-in | Description |
|---|---|---|---|---|
| [CliAssignPlateIdsCommand](../src/cli/CliAssignPlateIdsCommand.md) | 3 | 533 | 13 | CLI command that assigns plate IDs to features using partitioning polygons at a reconstruction time |
| [CliCommand](../src/cli/CliCommand.md) | 2 | 103 | 25 | Pure interface every headless CLI sub-command implements, dispatched by CommandDispatcher |
| [CliCommandDispatcher](../src/cli/CliCommandDispatcher.md) | 3 | 327 | 19 | Registry and executor for CLI commands indexed by name |
| [CliCommandRegistry](../src/cli/CliCommandRegistry.md) | 3 | 58 | 2 | Compile-time registry of CLI command classes as a Boost.MPL vector |
| [CliConvertFileFormatCommand](../src/cli/CliConvertFileFormatCommand.md) | 3 | 245 | 1 | CLI command that converts feature collections from one file format to another |
| [CliEquivalentTotalRotation](../src/cli/CliEquivalentTotalRotation.md) | 3 | 314 | 1 | CLI command that calculates the equivalent total rotation pole between two plates |
| [CliFeatureCollectionFileIO](../src/cli/CliFeatureCollectionFileIO.md) | 2 | 631 | 123 | Loads/saves feature collections for CLI commands without needing FeatureCollectionFileState |
| [CliInvalidOptionValue](../src/cli/CliInvalidOptionValue.md) | 3 | 87 | 4 | Exception thrown when a command-line option receives an invalid or out-of-range value |
| [CliReconstructCommand](../src/cli/CliReconstructCommand.md) | 3 | 413 | 1 | CLI command that reconstructs features to a paleo time using plate rotation paths |
| [CliRelativeTotalRotation](../src/cli/CliRelativeTotalRotation.md) | 3 | 317 | 1 | CLI command that calculates the relative rotation between a moving and fixed plate pair |
| [CliRequiredOptionNotPresent](../src/cli/CliRequiredOptionNotPresent.md) | 3 | 111 | 14 | Exception thrown when a required command-line option or configuration parameter is missing |
| [CliStageRotationCommand](../src/cli/CliStageRotationCommand.md) | 3 | 470 | 1 | CLI command to calculate stage rotations between two plates over a time interval |

## Other files

| File | Kind | Lines |
|---|---|---|
| `src/cli/CMakeLists.txt` | build | 37 |

## Depends on

| Component | References |
|---|---|
| [file-io](file-io.md) | 259 |
| [model](model.md) | 164 |
| [app-logic](app-logic.md) | 153 |
| [maths](maths.md) | 84 |
| [global](global.md) | 46 |
| [property-values](property-values.md) | 42 |
| [utils](utils.md) | 6 |
| [qt-widgets](qt-widgets.md) | 4 |
| [presentation](presentation.md) | 1 |

## Used by

| Component | References |
|---|---|
| [entry-points](entry-points.md) | 20 |
| [qt-widgets](qt-widgets.md) | 8 |
| [gui](gui.md) | 4 |

## Explore

Run these from the `gplates-code` skill directory:

```bash
python scripts/gpq.py tree src/cli
python scripts/gpq.py sym . --mode sub --path src/cli --defs-only
```
