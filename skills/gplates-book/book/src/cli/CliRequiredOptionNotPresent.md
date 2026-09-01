# CliRequiredOptionNotPresent

[Book TOC](../../TOC.md) · [cli](../../components/cli.md) · cluster Community 17 · tier 3

| Source file | Kind | Lines |
|---|---|---|
| `src/cli/CliRequiredOptionNotPresent.h` | C++ | 111 |

## Overview

An exception class thrown by CLI command handlers when a required option or configuration parameter is missing from the command line or configuration file. It carries the name of the missing option and an optional explanatory message describing why that option is mandatory. This exception is used throughout the CLI module to provide clear error reporting when users omit required parameters.

## Declared types

| Name | Kind | Bases | Template | Subclasses | Description |
|---|---|---|---|---|---|
| [`GPlatesCli::RequiredOptionNotPresent`](#gplatesclirequiredoptionnotpresent) | class | [`GPlatesGlobal::Exception`](../global/GPlatesException.md) | — | 0 | This exception is thrown when an option is required but was not present (not found on command-line or in a config file). |

## Members

### `GPlatesCli::RequiredOptionNotPresent`

| Member | Kind | Type | Access | Description |
|---|---|---|---|---|
| `RequiredOptionNotPresent( const GPlatesUtils::CallStack::Trace &exception_source, const char *option_, boost::optional<std::string> message_ = boost::none)` | constructor | `None` | public | — |
| `~RequiredOptionNotPresent()` | destructor | `None` | public | — |
| `message()` | method | `boost::optional<std::string>` | public | Return the optional message explaining why option is required. |
| `exception_name()` | method | `char` | protected | — |
| `write_message( std::ostream &os)` | method | `void` | protected | — |
| `d_option` | field | `std::string` | private | The option that was required but not present. |
| `d_message` | field | `boost::optional<std::string>` | private | Optional message explaining why option is required. |

## Free functions and macros

| Name | Kind | Type / body | Description |
|---|---|---|---|
| `GPLATES_CLI_CLIREQUIREDOPTIONNOTPRESENT_H` | macro | `None` | — |

## Notes

*None.*

## Used by

| Unit | Component | References |
|---|---|---|
| [qt-widgets/HellingerDialog](../qt-widgets/HellingerDialog.md) | qt-widgets | 8 |
| [gui/MapProjection](../gui/MapProjection.md) | gui | 4 |
| [cli/CliAssignPlateIdsCommand](CliAssignPlateIdsCommand.md) | cli | 2 |
| [cli/CliFeatureCollectionFileIO](CliFeatureCollectionFileIO.md) | cli | 2 |
| [cli/CliCommandDispatcher](CliCommandDispatcher.md) | cli | 1 |
| [cli/CliConvertFileFormatCommand](CliConvertFileFormatCommand.md) | cli | 1 |
| [cli/CliEquivalentTotalRotation](CliEquivalentTotalRotation.md) | cli | 1 |
| [cli/CliReconstructCommand](CliReconstructCommand.md) | cli | 1 |
| [cli/CliRelativeTotalRotation](CliRelativeTotalRotation.md) | cli | 1 |
| [cli/CliStageRotationCommand](CliStageRotationCommand.md) | cli | 1 |

## Related

*None.*

## Explore

Run these from the `gplates-code` skill directory:

```bash
python scripts/gpq.py file src/cli/CliRequiredOptionNotPresent.h
python scripts/gpq.py def GPlatesCli::RequiredOptionNotPresent --body
python scripts/gpq.py uses RequiredOptionNotPresent --kind class
python scripts/gpq.py hier RequiredOptionNotPresent
```
