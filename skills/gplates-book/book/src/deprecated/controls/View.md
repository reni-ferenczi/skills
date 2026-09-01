# View

[Book TOC](../../../TOC.md) · [deprecated](../../../components/deprecated.md) · cluster Community 1827 · tier 3 · **deprecated**

| Source file | Kind | Lines |
|---|---|---|
| `src/deprecated/controls/View.h` | C++ | 48 |
| `src/deprecated/controls/View.cc` | C++ | 34 |

## Overview

A stub namespace containing a single function `DocumentMetadata()` that returns the title and metadata for the loaded data set. Currently implemented as a placeholder that returns an empty string.

## Declared types

*None.*

## Members

*None.*

## Free functions and macros

| Name | Kind | Type / body | Description |
|---|---|---|---|
| `_GPLATES_CONTROLS_VIEW_H_` | macro | `None` | — |
| `DocumentMetadata()` | function | `std::string` | Return the title and meta information for the loaded data set. |

## Notes

The implementation is a stub that always returns an empty string. The header documentation indicates it should emit an error when no data set is loaded, but this is not implemented.

## Used by

*Nothing in the tree references this unit.*

## Related

*None.*

## Explore

Run these from the `gplates-code` skill directory:

```bash
python scripts/gpq.py file src/deprecated/controls/View.h
```
