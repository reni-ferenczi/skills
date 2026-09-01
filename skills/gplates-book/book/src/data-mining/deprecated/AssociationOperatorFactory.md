# AssociationOperatorFactory

[Book TOC](../../../TOC.md) · [data-mining](../../../components/data-mining.md) · cluster Community 959 · tier 3 · **deprecated**

| Source file | Kind | Lines |
|---|---|---|
| `src/data-mining/deprecated/AssociationOperatorFactory.h` | C++ | 60 |

## Overview

[[[PROSE overview unit=data-mining/deprecated/AssociationOperatorFactory tier=3]]]
Replace this whole block, markers included, with 1-3 paragraphs: what this unit is, why it exists, and how it fits the surrounding design. Do not restate the tables below.
[[[/PROSE]]]

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

[[[PROSE notes unit=data-mining/deprecated/AssociationOperatorFactory tier=3]]]
Replace this whole block, markers included, with invariants, ownership, threading or gotchas that are not visible in the tables. Write *None.* if there is nothing worth saying.
[[[/PROSE]]]

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
