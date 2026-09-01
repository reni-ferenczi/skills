# cli

[Book TOC](../TOC.md)

12 unit page(s), 20 source file(s) documented here, 1 further file(s) listed below.

## Overview

[[[PROSE component unit=component:cli tier=1]]]
Replace this whole block, markers included, with 2-4 paragraphs: what this component is responsible for, the load-bearing units and how it connects to neighbouring components. Do not restate the unit table.
[[[/PROSE]]]

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
