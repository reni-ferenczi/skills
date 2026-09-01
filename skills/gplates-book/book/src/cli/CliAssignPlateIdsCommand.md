# CliAssignPlateIdsCommand

[Book TOC](../../TOC.md) · [cli](../../components/cli.md) · cluster Community 1085 · tier 3

| Source file | Kind | Lines |
|---|---|---|
| `src/cli/CliAssignPlateIdsCommand.h` | C++ | 121 |
| `src/cli/CliAssignPlateIdsCommand.cc` | C++ | 412 |

## Overview

[[[PROSE overview unit=cli/CliAssignPlateIdsCommand tier=3]]]
Replace this whole block, markers included, with 1-3 paragraphs: what this unit is, why it exists, and how it fits the surrounding design. Do not restate the tables below.
[[[/PROSE]]]

## Declared types

| Name | Kind | Bases | Template | Subclasses | Description |
|---|---|---|---|---|---|
| [`GPlatesCli::AssignPlateIdsCommand`](#gplatescliassignplateidscommand) | class | [`Command`](CliCommand.md) | — | 0 | — |

## Members

### `GPlatesCli::AssignPlateIdsCommand`

| Member | Kind | Type | Access | Description |
|---|---|---|---|---|
| `AssignPlateIdsCommand()` | constructor | `None` | public | — |
| `get_command_name()` | method | `std::string` | public | Name of this command as seen on the command-line. |
| `get_command_description()` | method | `std::string` | public | A brief description of this command. |
| `add_options( boost::program_options::options_description &generic_options, boost::program_options::options_description &config_options, boost::program_options::options_description &hidden_options, boost::program_options::positional_options_description &positional_options)` | method | `void` | public | Add options to be parsed by the command-line/config-file parser. |
| `run( const boost::program_options::variables_map &vm)` | method | `void` | public | Interprets the parsed command-line and config file options stored in vm and runs this command. |
| `d_model` | field | `GPlatesModel::ModelInterface` | private | — |
| `d_extend_total_reconstruction_poles_to_distant_past` | field | `bool` | private | Whether each moving plate rotation sequence is extended back to the distant past such that reconstructed geometries are not snapped back to their present day positions. |
| `d_recon_time` | field | `double` | private | The reconstruction time at which to do the cookie-cutting or plate id (re)assigning. |
| `d_assign_plate_id` | field | `bool` | private | Assign plate ids (from the partitioning features). |
| `d_assign_time_period` | field | `bool` | private | Assign time period (from the partitioning features). |
| `d_respect_time_period` | field | `bool` | private | Only partition features that exist at the reconstruction time. |
| `d_anchor_plate_id` | field | `GPlatesModel::integer_plate_id_type` | private | — |
| `d_save_file_prefix` | field | `std::string` | private | — |
| `d_save_file_suffix` | field | `std::string` | private | — |

## Free functions and macros

| Name | Kind | Type / body | Description |
|---|---|---|---|
| `PARTITIONING_FILES_OPTION_NAME` | variable | `char` | Option name for partitioning feature collection file(s). |
| `PARTITIONING_FILES_OPTION_NAME_WITH_SHORT_OPTION` | variable | `char` | Option name with short version for partitioning file(s). |
| `ASSIGN_PLATE_ID_FILES_OPTION_NAME` | variable | `char` | Option name for feature collection file(s) having plate ids (re)assigned. |
| `ASSIGN_PLATE_ID_FILES_OPTION_NAME_WITH_SHORT_OPTION` | variable | `char` | Option name with short version for feature collection file(s) having plate ids (re)assigned. |
| `RECONSTRUCTION_FILES_OPTION_NAME` | variable | `char` | Option name for loading reconstruction feature collection file(s). |
| `RECONSTRUCTION_FILES_OPTION_NAME_WITH_SHORT_OPTION` | variable | `char` | Option name for loading reconstruction feature collection file(s) with short version. |
| `EXTEND_TOTAL_RECONSTRUCTION_POLES_TO_DISTANT_PAST_OPTION_NAME` | variable | `char` | Option name for extending total reconstruction poles back to distant past. |
| `ASSIGN_METHOD_OPTION_NAME` | variable | `char` | Option name for assign plate ids method. |
| `ASSIGN_METHOD_OPTION_NAME_WITH_SHORT_OPTION` | variable | `char` | Option name for assign plate ids method with short version. |
| `ASSIGN_PLATE_ID_WITH_SHORT_OPTION` | variable | `char` | Option name for assign plate id with short version. |
| `ASSIGN_TIME_PERIOD_WITH_SHORT_OPTION` | variable | `char` | Option name for assign time period with short version. |
| `RESPECT_TIME_PERIOD_WITH_SHORT_OPTION` | variable | `char` | Option name for respect time period with short version. |
| `SAVE_FILE_TYPE_OPTION_NAME` | variable | `char` | Option name for type of file to save. |
| `SAVE_FILE_TYPE_OPTION_NAME_WITH_SHORT_OPTION` | variable | `char` | Option name for type of file to save with short version. |
| `SAVE_FILE_PREFIX_OPTION_NAME` | variable | `char` | Option name for prefix of saved filenames. |
| `SAVE_FILE_SUFFIX_OPTION_NAME` | variable | `char` | Option name for suffix of saved filenames. |
| `RECONSTRUCTION_TIME_OPTION_NAME_WITH_SHORT_OPTION` | variable | `char` | Option name for reconstruction time with short version. |
| `ANCHOR_PLATE_ID_OPTION_NAME_WITH_SHORT_OPTION` | variable | `char` | Option name for anchor plate id with short version. |
| `ASSIGN_METHOD_ASSIGN_FEATURE_TO_MOST_OVERLAPPING_PLATE` | variable | `unsigned int` | Values specified by user on command-line for method used to assign plate ids. |
| `ASSIGN_METHOD_PARTITION_FEATURE` | variable | `unsigned int` | — |
| `get_assign_plate_ids_method( const boost::program_options::variables_map &vm)` | function | `GPlatesAppLogic::AssignPlateIds::AssignPlateIdMethodType` | Parses command-line option to get the assign plate ids method. |
| `get_save_file_type( const boost::program_options::variables_map &vm)` | function | `std::string` | Parses command-line option to get the save file type. |
| `GPLATES_SRC_CLI_ASSIGN_PLATE_IDS_COMMAND_H` | macro | `None` | — |

## Notes

[[[PROSE notes unit=cli/CliAssignPlateIdsCommand tier=3]]]
Replace this whole block, markers included, with invariants, ownership, threading or gotchas that are not visible in the tables. Write *None.* if there is nothing worth saying.
[[[/PROSE]]]

## Used by

| Unit | Component | References |
|---|---|---|
| [cli/CliCommandDispatcher](CliCommandDispatcher.md) | cli | 12 |
| [cli/CliCommandRegistry](CliCommandRegistry.md) | cli | 2 |

## Related

*None.*

## Explore

Run these from the `gplates-code` skill directory:

```bash
python scripts/gpq.py file src/cli/CliAssignPlateIdsCommand.h
python scripts/gpq.py def GPlatesCli::AssignPlateIdsCommand --body
python scripts/gpq.py uses AssignPlateIdsCommand --kind class
python scripts/gpq.py hier AssignPlateIdsCommand
```
