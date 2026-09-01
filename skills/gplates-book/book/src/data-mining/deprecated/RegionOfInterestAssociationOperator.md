# RegionOfInterestAssociationOperator

[Book TOC](../../../TOC.md) · [data-mining](../../../components/data-mining.md) · cluster Community 1524 · tier 3 · **deprecated**

| Source file | Kind | Lines |
|---|---|---|
| `src/data-mining/deprecated/RegionOfInterestAssociationOperator.h` | C++ | 101 |
| `src/data-mining/deprecated/RegionOfInterestAssociationOperator.cc` | C++ | 132 |

## Overview

[[[PROSE overview unit=data-mining/deprecated/RegionOfInterestAssociationOperator tier=3]]]
Replace this whole block, markers included, with 1-3 paragraphs: what this unit is, why it exists, and how it fits the surrounding design. Do not restate the tables below.
[[[/PROSE]]]

## Declared types

| Name | Kind | Bases | Template | Subclasses | Description |
|---|---|---|---|---|---|
| [`GPlatesDataMining::RegionOfInterestAssociationOperator`](#gplatesdataminingregionofinterestassociationoperator) | class | `AssociationOperator` | — | 0 | Comments.... |

## Members

### `GPlatesDataMining::RegionOfInterestAssociationOperator`

| Member | Kind | Type | Access | Description |
|---|---|---|---|---|
| `execute( const GPlatesModel::FeatureHandle::const_weak_ref& seed, /*In*/ const GPlatesModel::FeatureCollectionHandle::const_weak_ref& association_target, /*In*/ const FeatureGeometryMap& seed_map, /*In*/ const FeatureGeometryMap& target_map)` | method | `void` | public | — |
| `associate( GPlatesMaths::GeometryOnSphere::non_null_ptr_to_const_type seed_geo, GPlatesModel::FeatureHandle::non_null_ptr_to_const_type target_feature, const FeatureGeometryMap& target_map)` | method | `void` | protected | — |
| `d_feature_geometry_map` | field | `FeatureGeometryMap` | protected | — |
| `d_cfg` | field | `AssociationOperatorParameters` | protected | — |
| `RegionOfInterestAssociationOperator( AssociationOperatorParameters cfg)` | constructor | `None` | protected | — |
| `RegionOfInterestAssociationOperator()` | constructor | `None` | protected | — |
| `FilterInputSequenceType` | typedef | `std::vector< boost::tuple< GPlatesModel::FeatureHandle::const_weak_ref, std::vector<double>/*distance*/ > >` | protected | — |

## Free functions and macros

| Name | Kind | Type / body | Description |
|---|---|---|---|
| `GPLATESDATAMINING_REGIONOFINTERESTASSOCIATIONOPERATOR_H` | macro | `None` | — |

## Notes

[[[PROSE notes unit=data-mining/deprecated/RegionOfInterestAssociationOperator tier=3]]]
Replace this whole block, markers included, with invariants, ownership, threading or gotchas that are not visible in the tables. Write *None.* if there is nothing worth saying.
[[[/PROSE]]]

## Used by

| Unit | Component | References |
|---|---|---|
| [data-mining/deprecated/AssociationOperatorFactory](AssociationOperatorFactory.md) | data-mining | 3 |

## Related

*None.*

## Explore

Run these from the `gplates-code` skill directory:

```bash
python scripts/gpq.py file src/data-mining/deprecated/RegionOfInterestAssociationOperator.h
python scripts/gpq.py def GPlatesDataMining::RegionOfInterestAssociationOperator --body
python scripts/gpq.py uses RegionOfInterestAssociationOperator --kind class
python scripts/gpq.py hier RegionOfInterestAssociationOperator
```
