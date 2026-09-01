# CliInvalidOptionValue

[Book TOC](../../TOC.md) · [cli](../../components/cli.md) · cluster Community 17 · tier 3

| Source file | Kind | Lines |
|---|---|---|
| `src/cli/CliInvalidOptionValue.h` | C++ | 87 |

## Overview

`InvalidOptionValue` is an exception thrown when a command-line option receives a value that cannot be interpreted or is outside the acceptable range. It inherits from `GPlatesGlobal::Exception` and captures the name of the offending option for diagnostic output. Various CLI commands use this exception to signal parsing errors when validating user-supplied option values.

## Declared types

| Name | Kind | Bases | Template | Subclasses | Description |
|---|---|---|---|---|---|
| [`GPlatesCli::InvalidOptionValue`](#gplatescliinvalidoptionvalue) | class | [`GPlatesGlobal::Exception`](../global/GPlatesException.md) | — | 0 | This exception is thrown when the value of an option is invalid. |

## Members

### `GPlatesCli::InvalidOptionValue`

| Member | Kind | Type | Access | Description |
|---|---|---|---|---|
| `InvalidOptionValue( const GPlatesUtils::CallStack::Trace &exception_source, const char *option_)` | constructor | `None` | public | — |
| `~InvalidOptionValue()` | destructor | `None` | public | — |
| `exception_name()` | method | `char` | protected | — |
| `write_message( std::ostream &os)` | method | `void` | protected | — |
| `d_option` | field | `std::string` | private | The option that was required but not present. |

## Free functions and macros

| Name | Kind | Type / body | Description |
|---|---|---|---|
| `GPLATES_CLI_CLIINVALIDOPTIONVALUE_H` | macro | `None` | — |

## Notes

*None.*

## Used by

| Unit | Component | References |
|---|---|---|
| [cli/CliAssignPlateIdsCommand](CliAssignPlateIdsCommand.md) | cli | 3 |
| [cli/CliFeatureCollectionFileIO](CliFeatureCollectionFileIO.md) | cli | 2 |
| [cli/CliReconstructCommand](CliReconstructCommand.md) | cli | 2 |
| [cli/CliCommandDispatcher](CliCommandDispatcher.md) | cli | 1 |
| [cli/CliEquivalentTotalRotation](CliEquivalentTotalRotation.md) | cli | 1 |
| [cli/CliRelativeTotalRotation](CliRelativeTotalRotation.md) | cli | 1 |
| [cli/CliStageRotationCommand](CliStageRotationCommand.md) | cli | 1 |

## Related

*None.*

## Explore

Run these from the `gplates-code` skill directory:

```bash
python scripts/gpq.py file src/cli/CliInvalidOptionValue.h
python scripts/gpq.py def GPlatesCli::InvalidOptionValue --body
python scripts/gpq.py uses InvalidOptionValue --kind class
python scripts/gpq.py hier InvalidOptionValue
```
