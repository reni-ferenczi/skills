# gplates_main

[Book TOC](../../TOC.md) · [entry-points](../../components/entry-points.md) · cluster Community 542 · tier 3

| Source file | Kind | Lines |
|---|---|---|
| `src/gplates_main.cc` | C++ | 994 |

## Overview

[[[PROSE overview unit=entry-points/gplates_main tier=3]]]
Replace this whole block, markers included, with 1-3 paragraphs: what this unit is, why it exists, and how it fits the surrounding design. Do not restate the tables below.
[[[/PROSE]]]

## Declared types

| Name | Kind | Bases | Template | Subclasses | Description |
|---|---|---|---|---|---|
| [`(anonymous)::GuiCommandLineOptions`](#anonymousguicommandlineoptions) | class | — | — | 0 | The results of parsing the GUI command-line options. |
| [`(anonymous)::FirstCommandLineArgumentType`](#anonymousfirstcommandlineargumenttype) | enum | — | — | 0 | Classifies the type of the first command-line argument. |

## Members

### `(anonymous)::GuiCommandLineOptions`

| Member | Kind | Type | Access | Description |
|---|---|---|---|---|
| `GuiCommandLineOptions()` | constructor | `None` | public | — |
| `project_filename` | field | `boost::optional<QString>` | public | — |
| `feature_collection_filenames` | field | `QStringList` | public | — |
| `debug_gui` | field | `bool` | public | — |
| `enable_python` | field | `bool` | public | — |
| `enable_external_syncing` | field | `bool` | public | — |
| `enable_data_mining` | field | `bool` | public | — |
| `enable_symbol_table` | field | `bool` | public | — |
| `enable_hellinger_three_plate` | field | `bool` | public | — |

### `(anonymous)::FirstCommandLineArgumentType`

| Member | Kind | Type | Access | Description |
|---|---|---|---|---|
| `FIRST_ARG_IS_COMMAND` | enumerator | `None` | — | — |
| `FIRST_ARG_IS_UNRECOGNISED_COMMAND` | enumerator | `None` | — | — |
| `FIRST_ARG_IS_OPTION` | enumerator | `None` | — | — |
| `FIRST_ARG_IS_FILENAME` | enumerator | `None` | — | — |
| `FIRST_ARG_IS_NONEXISTENT` | enumerator | `None` | — | — |

## Free functions and macros

| Name | Kind | Type / body | Description |
|---|---|---|---|
| `HELP_COMMAND_OPTION_NAME` | variable | `char` | Option name to print usage of a specific GPlates command (non-GUI). |
| `COMMAND_OPTION_NAME` | variable | `char` | The option name used to extract the first positional command-line argument which is the GPlates command that the user wishes to execute (for non-GUI GPlates). |
| `POSITIONAL_FILENAMES_OPTION_NAME` | variable | `char` | Option name associated with positional arguments (project files or feature collection files). |
| `PROJECT_FILENAME_OPTION_NAME` | variable | `char` | Option name for loading a project file. |
| `PROJECT_FILENAME_OPTION_NAME_WITH_SHORT_OPTION` | variable | `char` | Option name for loading a project file with short version. |
| `FEATURE_COLLECTION_FILENAMES_OPTION_NAME` | variable | `char` | Option name for loading feature collection file(s). |
| `FEATURE_COLLECTION_FILENAMES_OPTION_NAME_WITH_SHORT_OPTION` | variable | `char` | Option name for loading feature collection file(s) with short version. |
| `DEBUG_GUI_OPTION_NAME` | variable | `char` | Enable the debug GUI menu. |
| `DATA_MINING_OPTION_NAME` | variable | `char` | Enable data-mining feature by secret command line option. |
| `SYMBOL_TABLE_OPTION_NAME` | variable | `char` | Enable symbol-table feature by secret command line option. |
| `NO_PYTHON_OPTION_NAME` | variable | `char` | Enable python by secret command line option. |
| `ENABLE_EXTERNAL_SYNCING_OPTION_NAME` | variable | `char` | Enable communication with external programs |
| `ENABLE_HELLINGER_THREE_PLATE_OPTION_NAME` | variable | `char` | Enable hellinger fitting tool |
| `print_usage( std::ostream &os, const GPlatesUtils::CommandLineParser::InputOptions &input_options)` | function | `void` | Prints program usage to os. |
| `add_help_command_option( GPlatesUtils::CommandLineParser::InputOptions &input_options)` | function | `void` | Adds the help command option (non-GUI). |
| `print_command_usage( std::ostream &os, const GPlatesUtils::CommandLineParser::InputOptions &input_options, const std::string &command)` | function | `void` | Prints usage for to os. |
| `parse_gui_command_line_options( int argc, char *argv[])` | function | `GuiCommandLineOptions` | — |
| `parse_and_run_command( const std::string &command, GPlatesCli::CommandDispatcher &command_dispatcher, int argc, char* argv[])` | function | `void` | Parses command-line assuming first argument is a recognised command and executes command. |
| `get_command( std::string &command, GPlatesCli::CommandDispatcher &command_dispatcher, int argc, char* argv[])` | function | `FirstCommandLineArgumentType` | Parses the command-line to determine the command specified by the user but doesn't parse any options specific to that command since we don't yet know the command. |
| `process_command_line_options( int argc, char *argv[])` | function | `boost::optional<GuiCommandLineOptions>` | Parses command-line options and either: 1) processes a non-GUI command (with its own options), or 2) parses GUI command-line options. |
| `initialise_python( GPlatesPresentation::Application *app, char* argv[])` | function | `void` | — |
| `clean_up()` | function | `void` | — |
| `internal_main(int argc, char* argv[])` | function | `int` | — |
| `main(int argc, char* argv[])` | function | `int` | — |

## Notes

[[[PROSE notes unit=entry-points/gplates_main tier=3]]]
Replace this whole block, markers included, with invariants, ownership, threading or gotchas that are not visible in the tables. Write *None.* if there is nothing worth saying.
[[[/PROSE]]]

## Used by

| Unit | Component | References |
|---|---|---|
| [gui/GPlatesQApplication](../gui/GPlatesQApplication.md) | gui | 2 |
| [qt-widgets/ViewportWindow](../qt-widgets/ViewportWindow.md) | qt-widgets | 1 |

## Related

*None.*

## Explore

Run these from the `gplates-code` skill directory:

```bash
python scripts/gpq.py file src/gplates_main.cc
python scripts/gpq.py def (anonymous)::GuiCommandLineOptions --body
python scripts/gpq.py uses GuiCommandLineOptions --kind class
python scripts/gpq.py hier GuiCommandLineOptions
```
