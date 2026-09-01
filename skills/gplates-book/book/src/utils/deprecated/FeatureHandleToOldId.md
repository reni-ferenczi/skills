# FeatureHandleToOldId

[Book TOC](../../../TOC.md) · [utils](../../../components/utils.md) · cluster Community 9 · tier 3 · **deprecated**

| Source file | Kind | Lines |
|---|---|---|
| `src/utils/deprecated/FeatureHandleToOldId.h` | C++ | 52 |
| `src/utils/deprecated/FeatureHandleToOldId.cc` | C++ | 90 |

## Overview

[[[PROSE overview unit=utils/deprecated/FeatureHandleToOldId tier=3]]]
Replace this whole block, markers included, with 1-3 paragraphs: what this unit is, why it exists, and how it fits the surrounding design. Do not restate the tables below.
[[[/PROSE]]]

## Declared types

*None.*

## Members

*None.*

## Free functions and macros

| Name | Kind | Type / body | Description |
|---|---|---|---|
| `GPLATES_UTILS_FEATUREHANDLETOOLDID_H` | macro | `None` | — |
| `get_old_id( const GPlatesModel::FeatureHandle &feature )` | function | `std::string` | From a feature handle, generate an old plates id. |
| `get_old_id( GPlatesModel::FeatureHandle::weak_ref ref)` | function | `std::string` | — |

## Notes

[[[PROSE notes unit=utils/deprecated/FeatureHandleToOldId tier=3]]]
Replace this whole block, markers included, with invariants, ownership, threading or gotchas that are not visible in the tables. Write *None.* if there is nothing worth saying.
[[[/PROSE]]]

## Used by

*Nothing in the tree references this unit.*

## Related

*None.*

## Explore

Run these from the `gplates-code` skill directory:

```bash
python scripts/gpq.py file src/utils/deprecated/FeatureHandleToOldId.h
```
