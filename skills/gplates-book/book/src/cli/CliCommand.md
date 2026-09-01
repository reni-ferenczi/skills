# CliCommand

[Book TOC](../../TOC.md) · [cli](../../components/cli.md) · cluster Community 1685 · tier 2

| Source file | Kind | Lines |
|---|---|---|
| `src/cli/CliCommand.h` | C++ | 103 |

## Overview

[[[PROSE overview unit=cli/CliCommand tier=2]]]
Replace this whole block, markers included, with 1-3 paragraphs: what this unit is, why it exists, and how it fits the surrounding design. Do not restate the tables below.
[[[/PROSE]]]

## Declared types

| Name | Kind | Bases | Template | Subclasses | Description |
|---|---|---|---|---|---|
| [`GPlatesCli::Command`](#gplatesclicommand) | class | — | — | 6 | An interface for retrieving a command's name (on the command-line), adding a command's options to the command-line and executing the command once its command-line options have been parsed. |

## Members

### `GPlatesCli::Command`

| Member | Kind | Type | Access | Description |
|---|---|---|---|---|
| `~Command()` | destructor | `None` | public | — |
| `get_command_name()` | method | `std::string` | public | Name of this command as seen on the command-line. |
| `get_command_description()` | method | `std::string` | public | A brief description of this command. |
| `add_options( boost::program_options::options_description &generic_options, boost::program_options::options_description &config_options, boost::program_options::options_description &hidden_options, boost::program_options::positional_options_description &positional_options)` | method | `void` | public | Add options to be parsed by the command-line/config-file parser. in config files. in config files but will not be shown to the user. don't look like "--name value" or "-n value" - instead they look like "value". |
| `run( const boost::program_options::variables_map &vm)` | method | `void` | public | Interprets the parsed command-line and config file options stored in vm and runs this command. |

## Free functions and macros

| Name | Kind | Type / body | Description |
|---|---|---|---|
| `GPLATES_SRC_CLI_COMMAND_H` | macro | `None` | — |

## Notes

[[[PROSE notes unit=cli/CliCommand tier=2]]]
Replace this whole block, markers included, with invariants, ownership, threading or gotchas that are not visible in the tables. Write *None.* if there is nothing worth saying.
[[[/PROSE]]]

## Used by

| Unit | Component | References |
|---|---|---|
| [cli/CliReconstructCommand](CliReconstructCommand.md) | cli | 8 |
| [cli/CliStageRotationCommand](CliStageRotationCommand.md) | cli | 6 |
| [cli/CliConvertFileFormatCommand](CliConvertFileFormatCommand.md) | cli | 5 |
| [cli/CliEquivalentTotalRotation](CliEquivalentTotalRotation.md) | cli | 5 |
| [cli/CliRelativeTotalRotation](CliRelativeTotalRotation.md) | cli | 5 |
| [cli/CliAssignPlateIdsCommand](CliAssignPlateIdsCommand.md) | cli | 2 |

## Related

*None.*

## Explore

Run these from the `gplates-code` skill directory:

```bash
python scripts/gpq.py file src/cli/CliCommand.h
python scripts/gpq.py def GPlatesCli::Command --body
python scripts/gpq.py uses Command --kind class
python scripts/gpq.py hier Command
```
