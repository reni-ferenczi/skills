# FeatureHandleToOldId

[Book TOC](../../../TOC.md) · [utils](../../../components/utils.md) · cluster Community 9 · tier 3 · **deprecated**

| Source file | Kind | Lines |
|---|---|---|
| `src/utils/deprecated/FeatureHandleToOldId.h` | C++ | 52 |
| `src/utils/deprecated/FeatureHandleToOldId.cc` | C++ | 90 |

## Overview

`FeatureHandleToOldId` provides deprecated utility functions for extracting legacy Plates format identifiers from features. The functions use a `ValueFinder` visitor to search for the "oldPlatesHeader" property on a feature and return its string value. This unit is kept for backward compatibility with older file formats.

Two overloads are provided: one taking a `FeatureHandle` by const reference, and another taking a `FeatureHandle::weak_ref`.

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

Returns an empty string if the feature does not have an "oldPlatesHeader" property.

## Used by

*Nothing in the tree references this unit.*

## Related

*None.*

## Explore

Run these from the `gplates-code` skill directory:

```bash
python scripts/gpq.py file src/utils/deprecated/FeatureHandleToOldId.h
```
