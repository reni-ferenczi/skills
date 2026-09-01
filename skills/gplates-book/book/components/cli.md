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
| [CliAssignPlateIdsCommand](../src/cli/CliAssignPlateIdsCommand.md) | 3 | 533 | 13 | (pending) |
| [CliCommand](../src/cli/CliCommand.md) | 2 | 103 | 25 | (pending) |
| [CliCommandDispatcher](../src/cli/CliCommandDispatcher.md) | 3 | 327 | 19 | (pending) |
| [CliCommandRegistry](../src/cli/CliCommandRegistry.md) | 3 | 58 | 2 | (pending) |
| [CliConvertFileFormatCommand](../src/cli/CliConvertFileFormatCommand.md) | 3 | 245 | 1 | (pending) |
| [CliEquivalentTotalRotation](../src/cli/CliEquivalentTotalRotation.md) | 3 | 314 | 1 | (pending) |
| [CliFeatureCollectionFileIO](../src/cli/CliFeatureCollectionFileIO.md) | 2 | 631 | 123 | (pending) |
| [CliInvalidOptionValue](../src/cli/CliInvalidOptionValue.md) | 3 | 87 | 4 | (pending) |
| [CliReconstructCommand](../src/cli/CliReconstructCommand.md) | 3 | 413 | 1 | (pending) |
| [CliRelativeTotalRotation](../src/cli/CliRelativeTotalRotation.md) | 3 | 317 | 1 | (pending) |
| [CliRequiredOptionNotPresent](../src/cli/CliRequiredOptionNotPresent.md) | 3 | 111 | 14 | (pending) |
| [CliStageRotationCommand](../src/cli/CliStageRotationCommand.md) | 3 | 470 | 1 | (pending) |

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
