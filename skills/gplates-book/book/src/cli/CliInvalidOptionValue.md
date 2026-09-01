# CliInvalidOptionValue

[Book TOC](../../TOC.md) · [cli](../../components/cli.md) · cluster Community 17 · tier 3

| Source file | Kind | Lines |
|---|---|---|
| `src/cli/CliInvalidOptionValue.h` | C++ | 87 |

## Overview

[[[PROSE overview unit=cli/CliInvalidOptionValue tier=3]]]
Replace this whole block, markers included, with 1-3 paragraphs: what this unit is, why it exists, and how it fits the surrounding design. Do not restate the tables below.
[[[/PROSE]]]

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

[[[PROSE notes unit=cli/CliInvalidOptionValue tier=3]]]
Replace this whole block, markers included, with invariants, ownership, threading or gotchas that are not visible in the tables. Write *None.* if there is nothing worth saying.
[[[/PROSE]]]

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
