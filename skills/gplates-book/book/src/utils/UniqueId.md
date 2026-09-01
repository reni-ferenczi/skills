# UniqueId

[Book TOC](../../TOC.md) · [utils](../../components/utils.md) · cluster Community 116 · tier 3

| Source file | Kind | Lines |
|---|---|---|
| `src/utils/UniqueId.h` | C++ | 59 |
| `src/utils/UniqueId.cc` | C++ | 51 |

## Overview

`generate_unique_id()` creates globally unique string identifiers by wrapping Qt's `QUuid::createUuid()` and formatting the result as a string that conforms to XML ID rules (matching the pattern `[A-Za-z_][-A-Za-z_0-9.]*`). The generated identifiers follow a `GPlates-<hex>` format suitable for use as feature IDs in GPML files.

## Declared types

*None.*

## Members

*None.*

## Free functions and macros

| Name | Kind | Type / body | Description |
|---|---|---|---|
| `GPLATES_UTILS_UNIQUEID_H` | macro | `None` | — |
| `generate_unique_id()` | function | `GPlatesUtils::UnicodeString` | Generate a unique string identifier. |

## Notes

*None.*

## Used by

| Unit | Component | References |
|---|---|---|
| [model/IdTypeGenerator](../model/IdTypeGenerator.md) | model | 2 |
| [model/RevisionId](../model/RevisionId.md) | model | 2 |
| [model/FeatureId](../model/FeatureId.md) | model | 1 |

## Related

*None.*

## Explore

Run these from the `gplates-code` skill directory:

```bash
python scripts/gpq.py file src/utils/UniqueId.h
```
