# CommandLineParser

[Book TOC](../../TOC.md) · [utils](../../components/utils.md) · cluster Community 954 · tier 2

| Source file | Kind | Lines |
|---|---|---|
| `src/utils/CommandLineParser.h` | C++ | 119 |
| `src/utils/CommandLineParser.cc` | C++ | 436 |

## Overview

[[[PROSE overview unit=utils/CommandLineParser tier=2]]]
Replace this whole block, markers included, with 1-3 paragraphs: what this unit is, why it exists, and how it fits the surrounding design. Do not restate the tables below.
[[[/PROSE]]]

## Declared types

| Name | Kind | Bases | Template | Subclasses | Description |
|---|---|---|---|---|---|
| [`GPlatesUtils::CommandLineParser::InputOptions`](#gplatesutilscommandlineparserinputoptions) | struct | — | — | 0 | This is where all options to be parsed on the command-line are stored. |

## Members

### `GPlatesUtils::CommandLineParser::InputOptions`

| Member | Kind | Type | Access | Description |
|---|---|---|---|---|
| `InputOptions()` | constructor | `None` | public | — |
| `add_simple_options()` | method | `void` | public | Adds the basic options such as help describing how to use response/configuration files and the version of GPlates. |
| `generic_options` | field | `boost::program_options::options_description` | public | Options that will be allowed only on command line. |
| `config_options` | field | `boost::program_options::options_description` | public | Options that will be allowed both on command line and in config file. |
| `hidden_options` | field | `boost::program_options::options_description` | public | Hidden options that will be allowed both on command line and in config files but will not be shown to the user. |
| `positional_options` | field | `boost::program_options::positional_options_description` | public | Positional options. |

## Free functions and macros

| Name | Kind | Type / body | Description |
|---|---|---|---|
| `HELP_OPTION_NAME` | variable | `char` | The option name used to print the program usage on the command-line. |
| `HELP_OPTION_NAME_WITH_SHORT_OPTION` | variable | `char` | Same as HELP\_OPTION\_NAME but with additional short option char. |
| `VERSION_OPTION_NAME` | variable | `char` | The option name used to print the program version on the command-line. |
| `VERSION_OPTION_NAME_WITH_SHORT_OPTION` | variable | `char` | Same as VERSION\_OPTION\_NAME but with additional short option char. |
| `RESPONSE_FILE_OPTION_NAME` | variable | `char` | A response file to contain command-line options for those systems that have a small limit on the size of the command-line arguments. |
| `CONFIG_FILE_OPTION_NAME` | variable | `char` | Configuration file containing options that the user wants to store in a file instead of having to type them on the command-line every time they run GPlates. |
| `at_option_parser( const std::string &option_name)` | function | `std::pair<std::string, std::string>` | Function for parsing options that the regular parser doesn't recognise. |
| `parse_command_line( boost::program_options::variables_map &vm, int argc, char* argv[], const boost::program_options::options_description &cmdline_options, const boost::program_options::positional_options_description &positional_options, int command_line_style)` | function | `void` | Parse the command-line arguments defined by argc and argv. |
| `parse_config_file( const std::string &config_filename, const boost::program_options::options_description &config_file_options, boost::program_options::variables_map &vm)` | function | `void` | Parses a file containing configuration options. |
| `parse_config_files( boost::program_options::variables_map &vm, const boost::program_options::options_description &config_file_options)` | function | `void` | Parses any files containing configuration options. |
| `read_response_file( const boost::program_options::variables_map &vm)` | function | `std::vector<std::string>` | Reads response file named by RESPONSE\_FILE\_OPTION\_NAME option and tokenizes it into a vector of strings which is returned by this function. |
| `parse_response_file( boost::program_options::variables_map &vm, const boost::program_options::options_description &cmdline_options, const boost::program_options::positional_options_description &positional_options, int command_line_style)` | function | `void` | Parses a response file containing command-line options. |
| `GPLATES_UTILS_COMMAND_LINE_PARSER_H` | macro | `None` | — |
| `get_cmdline_options( const GPlatesUtils::CommandLineParser::InputOptions &input_options)` | function | `boost::program_options::options_description` | — |
| `get_config_file_options( const GPlatesUtils::CommandLineParser::InputOptions &input_options)` | function | `boost::program_options::options_description` | — |
| `get_visible_options( const GPlatesUtils::CommandLineParser::InputOptions &input_options)` | function | `boost::program_options::options_description` | — |
| `parse_command_line_options( boost::program_options::variables_map &vm, int argc, char* argv[], const InputOptions &input_options, int command_line_style = boost::program_options::command_line_style::default_style)` | function | `void` | Parse the command-line options and also parse any response file and config files that are specified and store parsed results in vm. command\_line\_style contains options for how boost::program\_options processes the command-line. |
| `is_help_requested( const boost::program_options::variables_map &vm)` | function | `bool` | Returns true if help was requested in the parsed command-line arguments. |
| `is_version_requested( const boost::program_options::variables_map &vm)` | function | `bool` | Returns true if the GPlates version was requested in the parsed command-line arguments. |

## Notes

[[[PROSE notes unit=utils/CommandLineParser tier=2]]]
Replace this whole block, markers included, with invariants, ownership, threading or gotchas that are not visible in the tables. Write *None.* if there is nothing worth saying.
[[[/PROSE]]]

## Used by

| Unit | Component | References |
|---|---|---|
| [entry-points/gplates_main](../entry-points/gplates_main.md) | entry-points | 48 |
| [entry-points/gplates_unit_test_main](../entry-points/gplates_unit_test_main.md) | entry-points | 22 |

## Related

*None.*

## Explore

Run these from the `gplates-code` skill directory:

```bash
python scripts/gpq.py file src/utils/CommandLineParser.h
python scripts/gpq.py def GPlatesUtils::CommandLineParser::InputOptions --body
python scripts/gpq.py uses InputOptions --kind struct
python scripts/gpq.py hier InputOptions
```
