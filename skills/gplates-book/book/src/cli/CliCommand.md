# CliCommand

[Book TOC](../../TOC.md) · [cli](../../components/cli.md) · cluster Community 1685 · tier 2

| Source file | Kind | Lines |
|---|---|---|
| `src/cli/CliCommand.h` | C++ | 103 |

## Overview

`Command` is the pure abstract interface every headless CLI sub-command implements, so the surrounding infrastructure can treat "reconstruct", "convert file format", "equivalent total rotation" and the rest uniformly rather than special-casing each one. `GPlatesCli::CommandDispatcher` instantiates one `Command` per registered type (listed in `CliCommandTypes`), keyed by `get_command_name()`, then dispatches to whichever name the user typed on the command line.

The four virtual methods mirror the lifecycle a `boost::program_options`-driven CLI needs: `get_command_name()` and `get_command_description()` support listing available commands to the user, `add_options()` lets each command contribute its own generic, config-file, hidden and positional options into the shared parser, and `run()` executes the command against the resulting `variables_map` once parsing succeeds.

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

`run()` is documented to throw an exception on failure rather than return a status code; callers such as `CommandDispatcher` are expected to catch and report it. `get_command_description()` deliberately omits the options themselves, since `boost::program_options::options_description` cannot be rendered as a description string — option help comes from `add_options()` populating the parser directly.

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
