# CliCommandRegistry

[Book TOC](../../TOC.md) · [cli](../../components/cli.md) · cluster Community 9 · tier 3

| Source file | Kind | Lines |
|---|---|---|
| `src/cli/CliCommandRegistry.h` | C++ | 58 |

## Overview

`CommandTypes::command_types` is a compile-time registry of available CLI command classes expressed as a Boost.MPL vector. It names each `Command` subclass that the CLI supports, and `CommandDispatcher` iterates over this vector at construction time to instantiate and register each command in its internal map. Adding a new command requires both creating the command class and adding it to this vector.

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

*None.*

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
