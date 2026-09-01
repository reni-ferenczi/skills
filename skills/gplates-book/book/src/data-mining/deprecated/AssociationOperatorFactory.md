# AssociationOperatorFactory

[Book TOC](../../../TOC.md) · [data-mining](../../../components/data-mining.md) · cluster Community 959 · tier 3 · **deprecated**

| Source file | Kind | Lines |
|---|---|---|
| `src/data-mining/deprecated/AssociationOperatorFactory.h` | C++ | 60 |

## Overview

A factory for creating `AssociationOperator` instances based on type enum and configuration parameters. The static `create()` method accepts an `AssociationOperatorType` and `AssociationOperatorParameters` and returns a new operator instance. This class is deprecated and was part of an earlier data-mining workflow architecture.

## Declared types

| Name | Kind | Bases | Template | Subclasses | Description |
|---|---|---|---|---|---|
| [`GPlatesDataMining::AssociationOperatorFactory`](#gplatesdataminingassociationoperatorfactory) | class | — | — | 0 | TODO |

## Members

### `GPlatesDataMining::AssociationOperatorFactory`

| Member | Kind | Type | Access | Description |
|---|---|---|---|---|
| `create( AssociationOperatorType type, AssociationOperatorParameters cfg)` | method | `AssociationOperator` | public | — |

## Free functions and macros

| Name | Kind | Type / body | Description |
|---|---|---|---|
| `GPLATESDATAMINING_ASSOCIATIONOPERATORFACTORY_H` | macro | `None` | — |

## Notes

The `create()` method currently creates a `RegionOfInterestAssociationOperator` for all type values, including the default case. The implementation is incomplete and marked as TODO.

## Used by

| Unit | Component | References |
|---|---|---|
| [data-mining/deprecated/RegionOfInterestAssociationOperator](RegionOfInterestAssociationOperator.md) | data-mining | 1 |
| [data-mining/deprecated/SubDataSelector](SubDataSelector.md) | data-mining | 1 |

## Related

*None.*

## Explore

Run these from the `gplates-code` skill directory:

```bash
python scripts/gpq.py file src/data-mining/deprecated/AssociationOperatorFactory.h
python scripts/gpq.py def GPlatesDataMining::AssociationOperatorFactory --body
python scripts/gpq.py uses AssociationOperatorFactory --kind class
python scripts/gpq.py hier AssociationOperatorFactory
```
