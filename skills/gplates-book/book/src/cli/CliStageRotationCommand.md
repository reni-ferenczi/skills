# CliStageRotationCommand

[Book TOC](../../TOC.md) · [cli](../../components/cli.md) · cluster Community 936 · tier 3

| Source file | Kind | Lines |
|---|---|---|
| `src/cli/CliStageRotationCommand.h` | C++ | 119 |
| `src/cli/CliStageRotationCommand.cc` | C++ | 351 |

## Overview

[[[PROSE overview unit=cli/CliStageRotationCommand tier=3]]]
Replace this whole block, markers included, with 1-3 paragraphs: what this unit is, why it exists, and how it fits the surrounding design. Do not restate the tables below.
[[[/PROSE]]]

## Declared types

| Name | Kind | Bases | Template | Subclasses | Description |
|---|---|---|---|---|---|
| [`GPlatesCli::StageRotationCommand`](#gplatesclistagerotationcommand) | class | [`Command`](CliCommand.md) | — | 0 | — |

## Members

### `GPlatesCli::StageRotationCommand`

| Member | Kind | Type | Access | Description |
|---|---|---|---|---|
| `StageRotationCommand()` | constructor | `None` | public | — |
| `get_command_name()` | method | `std::string` | public | Name of this command as seen on the command-line. |
| `get_command_description()` | method | `std::string` | public | A brief description of this command. |
| `add_options( boost::program_options::options_description &generic_options, boost::program_options::options_description &config_options, boost::program_options::options_description &hidden_options, boost::program_options::positional_options_description &positional_options)` | method | `void` | public | Add options to be parsed by the command-line/config-file parser. |
| `run( const boost::program_options::variables_map &vm)` | method | `void` | public | Interprets the parsed command-line and config file options stored in vm and runs this command. |
| `loaded_feature_collection_file_seq_type` | typedef | `std::vector<GPlatesFileIO::File::non_null_ptr_type>` | private | — |
| `d_model` | field | `GPlatesModel::ModelInterface` | private | — |
| `d_extend_total_reconstruction_poles_to_distant_past` | field | `bool` | private | Whether each moving plate rotation sequence is extended back to the distant past such that reconstructed geometries are not snapped back to their present day positions. |
| `d_start_time` | field | `double` | private | — |
| `d_end_time` | field | `double` | private | — |
| `d_anchor_plate_id` | field | `GPlatesModel::integer_plate_id_type` | private | — |
| `d_fixed_plate_id` | field | `GPlatesModel::integer_plate_id_type` | private | — |
| `d_moving_plate_id` | field | `GPlatesModel::integer_plate_id_type` | private | — |
| `d_asymmetry` | field | `double` | private | The asymmetry is in the range \[-1,1\] where the value 0 represents half-stage rotation and the value 1 represents full-stage rotation. |
| `output_stage_rotation( const GPlatesMaths::FiniteRotation &stage_rotation, bool output_indeterminate_for_identity_rotations)` | method | `void` | private | — |

## Free functions and macros

| Name | Kind | Type / body | Description |
|---|---|---|---|
| `LOAD_RECONSTRUCTION_OPTION_NAME` | variable | `char` | Option name for loading reconstruction feature collection file(s). |
| `LOAD_RECONSTRUCTION_OPTION_NAME_WITH_SHORT_OPTION` | variable | `char` | Option name for loading reconstruction feature collection file(s) with short version. |
| `EXTEND_TOTAL_RECONSTRUCTION_POLES_TO_DISTANT_PAST_OPTION_NAME` | variable | `char` | Option name for extending total reconstruction poles back to distant past. |
| `START_TIME_OPTION_NAME_WITH_SHORT_OPTION` | variable | `char` | Option name for start time with short version. |
| `END_TIME_OPTION_NAME_WITH_SHORT_OPTION` | variable | `char` | Option name for end time with short version. |
| `ANCHOR_PLATE_ID_OPTION_NAME_WITH_SHORT_OPTION` | variable | `char` | Option name for anchor plate id with short version. |
| `FIXED_PLATE_ID_OPTION_NAME_WITH_SHORT_OPTION` | variable | `char` | Option name for fixed plate id with short version. |
| `MOVING_PLATE_ID_OPTION_NAME_WITH_SHORT_OPTION` | variable | `char` | Option name for moving plate id with short version. |
| `ASYMMETRY_OPTION_NAME_WITH_SHORT_OPTION` | variable | `char` | Option name for asymmetry with short version. |
| `RELATIVE_TO_ANCHOR_PLATE_OPTION_NAME` | variable | `char` | Option name for enabling stage rotations relative to the anchor plate. |
| `RELATIVE_TO_ANCHOR_PLATE_OPTION_NAME_WITH_SHORT_OPTION` | variable | `char` | Option name enabling stage rotations relative to the anchor plate with short version. |
| `INDETERMINATE_IS_ZERO_ANGLE_NORTH_POLE_OPTION_NAME` | variable | `char` | Option name for replacing 'Indeterminate' rotations with zero-angle north pole. |
| `INDETERMINATE_IS_ZERO_ANGLE_NORTH_POLE_OPTION_NAME_WITH_SHORT_OPTION` | variable | `char` | Option name for replacing 'Indeterminate' rotations with zero-angle north pole with short version. |
| `GPLATES_CLI_CLISTAGEROTATIONCOMMAND_H` | macro | `None` | — |

## Notes

[[[PROSE notes unit=cli/CliStageRotationCommand tier=3]]]
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
python scripts/gpq.py file src/cli/CliStageRotationCommand.h
python scripts/gpq.py def GPlatesCli::StageRotationCommand --body
python scripts/gpq.py uses StageRotationCommand --kind class
python scripts/gpq.py hier StageRotationCommand
```
