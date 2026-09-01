# CliCommandRegistry

[Book TOC](../../TOC.md) · [cli](../../components/cli.md) · cluster Community 9 · tier 3

| Source file | Kind | Lines |
|---|---|---|
| `src/cli/CliCommandRegistry.h` | C++ | 58 |

## Overview

[[[PROSE overview unit=cli/CliCommandRegistry tier=3]]]
Replace this whole block, markers included, with 1-3 paragraphs: what this unit is, why it exists, and how it fits the surrounding design. Do not restate the tables below.
[[[/PROSE]]]

## Declared types

| Name | Kind | Bases | Template | Subclasses | Description |
|---|---|---|---|---|---|
| [`GPlatesCli::CommandTypes::command_types`](#gplatesclicommandtypescommand_types) | typedef | — | — | 0 | Add any new command classes you have created here. |

## Members

### `GPlatesCli::CommandTypes::command_types`

*None.*

## Free functions and macros

| Name | Kind | Type / body | Description |
|---|---|---|---|
| `GPLATES_CLI_CLICOMMANDREGISTRY_H` | macro | `None` | — |

## Notes

[[[PROSE notes unit=cli/CliCommandRegistry tier=3]]]
Replace this whole block, markers included, with invariants, ownership, threading or gotchas that are not visible in the tables. Write *None.* if there is nothing worth saying.
[[[/PROSE]]]

## Used by

| Unit | Component | References |
|---|---|---|
| [cli/CliCommandDispatcher](CliCommandDispatcher.md) | cli | 3 |

## Related

*None.*

## Explore

Run these from the `gplates-code` skill directory:

```bash
python scripts/gpq.py file src/cli/CliCommandRegistry.h
python scripts/gpq.py def GPlatesCli::CommandTypes::command_types --body
python scripts/gpq.py uses command_types --kind typedef
```
