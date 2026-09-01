# InternalRID

[Book TOC](../../../TOC.md) · [global](../../../components/global.md) · cluster Community 1691 · tier 3 · **deprecated**

| Source file | Kind | Lines |
|---|---|---|
| `src/global/deprecated/InternalRID.h` | C++ | 108 |

## Overview

**Deprecated.** A lightweight wrapper around an unsigned integer that represents a rotation ID (RID) of a rotating object. This was introduced to isolate internal kinematic calculations from the complex state of plate IDs and rotation IDs in GPlates and GPML. The Earth's internal RID is always 0. The class deliberately lacks a default constructor (you must provide an initial value) and provides comparison operators primarily to enable use as keys in STL containers.

## Declared types

| Name | Kind | Bases | Template | Subclasses | Description |
|---|---|---|---|---|---|
| [`GPlatesGlobal::InternalRID`](#gplatesglobalinternalrid) | class | — | — | 0 | Instances of this class will be used internally to represent the rotation ids of rotating objects. |

## Members

### `GPlatesGlobal::InternalRID`

| Member | Kind | Type | Access | Description |
|---|---|---|---|---|
| `InternalRID(unsigned int i)` | constructor | `None` | public | — |
| `ival()` | method | `unsigned int` | public | no default constructor |
| `_ival` | field | `unsigned int` | private | — |

## Free functions and macros

| Name | Kind | Type / body | Description |
|---|---|---|---|
| `_GPLATES_GLOBAL_INTERNALRID_H_` | macro | `None` | — |
| `operator==(const InternalRID &i1, const InternalRID &i2)` | operator | `bool` | — |
| `operator!=(const InternalRID &i1, const InternalRID &i2)` | operator | `bool` | — |
| `operator<(const InternalRID &i1, const InternalRID &i2)` | operator | `bool` | Although this operation doesn't strictly make sense for an InternalRID, it is provided to enable InternalRIDs to be used as keys in STL maps. |
| `operator>(const InternalRID &i1, const InternalRID &i2)` | operator | `bool` | Although this operation doesn't strictly make sense for an InternalRID, it is provided to enable client code to work out the "highest" InternalRID in a collection. |

## Notes

The comparison operators `<` and `>` are provided solely to enable `InternalRID` to be used as a key in STL associative containers; they do not represent a meaningful ordering and their use in other contexts is misleading.

## Used by

| Unit | Component | References |
|---|---|---|
| [global/deprecated/types](types.md) | global | 2 |

## Related

*None.*

## Explore

Run these from the `gplates-code` skill directory:

```bash
python scripts/gpq.py file src/global/deprecated/InternalRID.h
python scripts/gpq.py def GPlatesGlobal::InternalRID --body
python scripts/gpq.py uses InternalRID --kind class
python scripts/gpq.py hier InternalRID
```
