# CliRequiredOptionNotPresent

[Book TOC](../../TOC.md) · [cli](../../components/cli.md) · cluster Community 17 · tier 3

| Source file | Kind | Lines |
|---|---|---|
| `src/cli/CliRequiredOptionNotPresent.h` | C++ | 111 |

## Overview

[[[PROSE overview unit=cli/CliRequiredOptionNotPresent tier=3]]]
Replace this whole block, markers included, with 1-3 paragraphs: what this unit is, why it exists, and how it fits the surrounding design. Do not restate the tables below.
[[[/PROSE]]]

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

[[[PROSE notes unit=cli/CliRequiredOptionNotPresent tier=3]]]
Replace this whole block, markers included, with invariants, ownership, threading or gotchas that are not visible in the tables. Write *None.* if there is nothing worth saying.
[[[/PROSE]]]

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
