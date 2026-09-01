# CliConvertFileFormatCommand

[Book TOC](../../TOC.md) · [cli](../../components/cli.md) · cluster Community 1364 · tier 3

| Source file | Kind | Lines |
|---|---|---|
| `src/cli/CliConvertFileFormatCommand.h` | C++ | 89 |
| `src/cli/CliConvertFileFormatCommand.cc` | C++ | 156 |

## Overview

`ConvertFileFormatCommand` is a CLI command that converts loaded feature collections from one file format to another. It reads feature collections into a `ModelInterface`, then saves them in the specified output format (GPML, compressed GPML, Shapefile, GMT, or Plates4 line format). The command allows users to provide prefix and suffix decorations to the output filenames during conversion.

## Declared types

| Name | Kind | Bases | Template | Subclasses | Description |
|---|---|---|---|---|---|
| [`GPlatesCli::ConvertFileFormatCommand`](#gplatescliconvertfileformatcommand) | class | [`Command`](CliCommand.md) | — | 0 | — |

## Members

### `GPlatesCli::ConvertFileFormatCommand`

| Member | Kind | Type | Access | Description |
|---|---|---|---|---|
| `ConvertFileFormatCommand()` | constructor | `None` | public | — |
| `get_command_name()` | method | `std::string` | public | Name of this command as seen on the command-line. |
| `get_command_description()` | method | `std::string` | public | A brief description of this command. |
| `add_options( boost::program_options::options_description &generic_options, boost::program_options::options_description &config_options, boost::program_options::options_description &hidden_options, boost::program_options::positional_options_description &positional_options)` | method | `void` | public | Add options to be parsed by the command-line/config-file parser. |
| `run( const boost::program_options::variables_map &vm)` | method | `void` | public | Interprets the parsed command-line and config file options stored in vm and runs this command. |
| `d_model` | field | `GPlatesModel::ModelInterface` | private | — |
| `d_save_file_type` | field | `std::string` | private | — |
| `d_save_file_prefix` | field | `std::string` | private | — |
| `d_save_file_suffix` | field | `std::string` | private | — |

## Free functions and macros

| Name | Kind | Type / body | Description |
|---|---|---|---|
| `LOAD_FEATURE_COLLECTION_OPTION_NAME` | variable | `char` | Option name for loading feature collection file(s). |
| `LOAD_FEATURE_COLLECTION_OPTION_NAME_WITH_SHORT_OPTION` | variable | `char` | Option name for loading feature collection file(s) with short version. |
| `SAVE_FILE_TYPE_OPTION_NAME_WITH_SHORT_OPTION` | variable | `char` | Option name for type of file to save with short version. |
| `SAVE_FILE_PREFIX_OPTION_NAME_WITH_SHORT_OPTION` | variable | `char` | Option name for prefix of saved filenames with short option. |
| `SAVE_FILE_SUFFIX_OPTION_NAME_WITH_SHORT_OPTION` | variable | `char` | Option name for suffix of saved filenames with short option. |
| `GPLATES_CLI_CLICONVERTFILEFORMATCOMMAND_H` | macro | `None` | — |

## Notes

*None.*

## Used by

| Unit | Component | References |
|---|---|---|
| [cli/CliCommandRegistry](CliCommandRegistry.md) | cli | 2 |

## Related

*None.*

## Explore

Run these from the `gplates-code` skill directory:

```bash
python scripts/gpq.py file src/cli/CliConvertFileFormatCommand.h
python scripts/gpq.py def GPlatesCli::ConvertFileFormatCommand --body
python scripts/gpq.py uses ConvertFileFormatCommand --kind class
python scripts/gpq.py hier ConvertFileFormatCommand
```
