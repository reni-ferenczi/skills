# CliReconstructCommand

[Book TOC](../../TOC.md) · [cli](../../components/cli.md) · cluster Community 1138 · tier 3

| Source file | Kind | Lines |
|---|---|---|
| `src/cli/CliReconstructCommand.h` | C++ | 123 |
| `src/cli/CliReconstructCommand.cc` | C++ | 290 |

## Overview

[[[PROSE overview unit=cli/CliReconstructCommand tier=3]]]
Replace this whole block, markers included, with 1-3 paragraphs: what this unit is, why it exists, and how it fits the surrounding design. Do not restate the tables below.
[[[/PROSE]]]

## Declared types

| Name | Kind | Bases | Template | Subclasses | Description |
|---|---|---|---|---|---|
| [`GPlatesCli::ReconstructCommand`](#gplatesclireconstructcommand) | class | [`Command`](CliCommand.md) | — | 0 | — |

## Members

### `GPlatesCli::ReconstructCommand`

| Member | Kind | Type | Access | Description |
|---|---|---|---|---|
| `ReconstructCommand()` | constructor | `None` | public | — |
| `get_command_name()` | method | `std::string` | public | Name of this command as seen on the command-line. |
| `get_command_description()` | method | `std::string` | public | A brief description of this command. |
| `add_options( boost::program_options::options_description &generic_options, boost::program_options::options_description &config_options, boost::program_options::options_description &hidden_options, boost::program_options::positional_options_description &positional_options)` | method | `void` | public | Add options to be parsed by the command-line/config-file parser. |
| `run( const boost::program_options::variables_map &vm)` | method | `void` | public | Interprets the parsed command-line and config file options stored in vm and runs this command. |
| `loaded_feature_collection_file_seq_type` | typedef | `std::vector<GPlatesFileIO::File::Reference::non_null_ptr_type>` | private | — |
| `d_model` | field | `GPlatesModel::ModelInterface` | private | — |
| `d_recon_time` | field | `double` | private | — |
| `d_anchor_plate_id` | field | `GPlatesModel::integer_plate_id_type` | private | — |
| `d_export_filename` | field | `std::string` | private | — |
| `d_export_single_output_file` | field | `bool` | private | Export all reconstruction geometries to a single file. |
| `d_export_separate_output_directory_per_input_file` | field | `bool` | private | If 'true' then the \*multiple\* export files will follow the pattern... "\<export\_path\>/\<collection\_filename\>/\<export\_template\_filename\>" ...otherwise they will follow the pattern... ... |
| `d_wrap_to_dateline` | field | `bool` | private | Wraps reconstructed geometries to the dateline. |

## Free functions and macros

| Name | Kind | Type / body | Description |
|---|---|---|---|
| `LOAD_RECONSTRUCTABLE_OPTION_NAME` | variable | `char` | Option name for loading reconstructable feature collection file(s). |
| `LOAD_RECONSTRUCTABLE_OPTION_NAME_WITH_SHORT_OPTION` | variable | `char` | Option name for loading reconstructable feature collection file(s) with short version. |
| `LOAD_RECONSTRUCTION_OPTION_NAME` | variable | `char` | Option name for loading reconstruction feature collection file(s). |
| `LOAD_RECONSTRUCTION_OPTION_NAME_WITH_SHORT_OPTION` | variable | `char` | Option name for loading reconstruction feature collection file(s) with short version. |
| `EXPORT_FILENAME_OPTION_NAME_WITH_SHORT_OPTION` | variable | `char` | Option name for filename to export with short version. |
| `EXPORT_FILE_TYPE_OPTION_NAME` | variable | `char` | Option name for type of file to export. |
| `EXPORT_FILE_TYPE_OPTION_NAME_WITH_SHORT_OPTION` | variable | `char` | Option name for type of file to export with short version. |
| `RECONSTRUCTION_TIME_OPTION_NAME_WITH_SHORT_OPTION` | variable | `char` | Option name for reconstruction time with short version. |
| `ANCHOR_PLATE_ID_OPTION_NAME_WITH_SHORT_OPTION` | variable | `char` | Option name for anchor plate id with short version. |
| `SINGLE_OUTPUT_FILE_OPTION_NAME_WITH_SHORT_OPTION` | variable | `char` | Option name for outputting to a single file with short version. |
| `SEPARATE_OUTPUT_DIRECTORY_OPTION_NAME_WITH_SHORT_OPTION` | variable | `char` | Option name for outputting each file to a separate directory with short version. |
| `WRAP_TO_DATELINE_OPTION_NAME_WITH_SHORT_OPTION` | variable | `char` | Option name for wrapping-to-dateline with short version. |
| `get_export_file_type( const boost::program_options::variables_map &vm)` | function | `std::string` | Parses command-line option to get the export file type. |
| `GPLATES_SRC_CLI_RECONSTRUCT_COMMAND_H` | macro | `None` | — |

## Notes

[[[PROSE notes unit=cli/CliReconstructCommand tier=3]]]
Replace this whole block, markers included, with invariants, ownership, threading or gotchas that are not visible in the tables. Write *None.* if there is nothing worth saying.
[[[/PROSE]]]

## Used by

| Unit | Component | References |
|---|---|---|
| [cli/CliCommandRegistry](CliCommandRegistry.md) | cli | 2 |

## Related

*None.*

## Explore

Run these from the `gplates-code` skill directory:

```bash
python scripts/gpq.py file src/cli/CliReconstructCommand.h
python scripts/gpq.py def GPlatesCli::ReconstructCommand --body
python scripts/gpq.py uses ReconstructCommand --kind class
python scripts/gpq.py hier ReconstructCommand
```
