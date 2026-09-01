# CliCommandDispatcher

[Book TOC](../../TOC.md) · [cli](../../components/cli.md) · cluster Community 923 · tier 3

| Source file | Kind | Lines |
|---|---|---|
| `src/cli/CliCommandDispatcher.h` | C++ | 162 |
| `src/cli/CliCommandDispatcher.cc` | C++ | 165 |

## Overview

`CommandDispatcher` is a registry and executor for CLI commands. It holds a map of `Command` subclasses, indexed by name, and instantiates them at construction time by iterating over a compile-time list of registered command types via Boost.MPL meta-programming. The dispatcher provides a uniform interface to look up commands by name, gather their command-line options, and dispatch execution to the chosen command once its options have been parsed.

## Declared types

| Name | Kind | Bases | Template | Subclasses | Description |
|---|---|---|---|---|---|
| [`GPlatesCli::CommandDispatcher`](#gplatesclicommanddispatcher) | class | — | — | 0 | The GPlates command-line allows a single command (with its own command-line options) from a group of possible commands - this class keeps track of those commands and provides an interface for getting a specific command to add its ... |

## Members

### `GPlatesCli::CommandDispatcher`

| Member | Kind | Type | Access | Description |
|---|---|---|---|---|
| `CommandDispatcher()` | constructor | `None` | public | — |
| `command_name_and_description_type` | typedef | `std::pair<std::string, std::string>` | public | Typedef for a command name and description. |
| `get_command_names_and_descriptions()` | method | `std::vector<command_name_and_description_type>` | public | Returns a list of the names of all commands (as they appear on the command-line) and a brief description for each (note: the description does not include the options used by that command - that is taken care of by add\_options\_for\_command ... |
| `is_recognised_command( const std::string &command_name)` | method | `bool` | public | Returns true if command\_name is a recognised command. |
| `add_options_for_command( const std::string &command_name, boost::program_options::options_description &generic_options, boost::program_options::options_description &config_options, boost::program_options::options_description &hidden_options, boost::program_options::positional_options_description &positional_options)` | method | `void` | public | Add options to be parsed by the command-line/config-file parser. |
| `run( const std::string &command_name, const boost::program_options::variables_map &vm)` | method | `void` | public | Interprets the parsed command-line and config file options stored in vm and runs the command specified by command\_name. |
| `command_ptr_type` | typedef | `boost::shared_ptr<Command>` | private | — |
| `command_map_type` | typedef | `std::map<std::string, command_ptr_type >` | private | — |
| `AddCommand` | class | `None` | private | Utility class that adds a command of type CommandType. |
| `d_command_map` | field | `command_map_type` | private | — |
| `get_command( Command *&command, const std::string &command_name)` | method | `bool` | private | Looks up command using command\_name. |

## Free functions and macros

| Name | Kind | Type / body | Description |
|---|---|---|---|
| `operator()( Wrap<CommandType>)` | operator | `void` | — |
| `GPLATES_SRC_CLI_COMMAND_DISPATCHER_H` | macro | `None` | — |

## Notes

*None.*

## Used by

| Unit | Component | References |
|---|---|---|
| [entry-points/gplates_main](../entry-points/gplates_main.md) | entry-points | 20 |

## Related

*None.*

## Explore

Run these from the `gplates-code` skill directory:

```bash
python scripts/gpq.py file src/cli/CliCommandDispatcher.h
python scripts/gpq.py def GPlatesCli::CommandDispatcher --body
python scripts/gpq.py uses CommandDispatcher --kind class
python scripts/gpq.py hier CommandDispatcher
```
