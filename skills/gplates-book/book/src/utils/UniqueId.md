# UniqueId

[Book TOC](../../TOC.md) · [utils](../../components/utils.md) · cluster Community 116 · tier 3

| Source file | Kind | Lines |
|---|---|---|
| `src/utils/UniqueId.h` | C++ | 59 |
| `src/utils/UniqueId.cc` | C++ | 51 |

## Overview

[[[PROSE overview unit=utils/UniqueId tier=3]]]
Replace this whole block, markers included, with 1-3 paragraphs: what this unit is, why it exists, and how it fits the surrounding design. Do not restate the tables below.
[[[/PROSE]]]

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

[[[PROSE notes unit=utils/UniqueId tier=3]]]
Replace this whole block, markers included, with invariants, ownership, threading or gotchas that are not visible in the tables. Write *None.* if there is nothing worth saying.
[[[/PROSE]]]

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
