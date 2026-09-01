# PopulateShapeFileAttributesVisitor

[Book TOC](../../TOC.md) · [data-mining](../../components/data-mining.md) · cluster Community 1365 · tier 3

| Source file | Kind | Lines |
|---|---|---|
| `src/data-mining/PopulateShapeFileAttributesVisitor.h` | C++ | 103 |
| `src/data-mining/PopulateShapeFileAttributesVisitor.cc` | C++ | 101 |

## Overview

[[[PROSE overview unit=data-mining/PopulateShapeFileAttributesVisitor tier=3]]]
Replace this whole block, markers included, with 1-3 paragraphs: what this unit is, why it exists, and how it fits the surrounding design. Do not restate the tables below.
[[[/PROSE]]]

## Declared types

| Name | Kind | Bases | Template | Subclasses | Description |
|---|---|---|---|---|---|
| [`GPlatesDataMining::PopulateShapeFileAttributesVisitor`](#gplatesdataminingpopulateshapefileattributesvisitor) | class | [`GPlatesModel::ConstFeatureVisitor`](../model/FeatureVisitor.md) | — | 0 | The ToQvariantConverter feature-visitor is used to locate specific property values within a Feature and convert them to QVariants, if possible. |

## Members

### `GPlatesDataMining::PopulateShapeFileAttributesVisitor`

| Member | Kind | Type | Access | Description |
|---|---|---|---|---|
| `~PopulateShapeFileAttributesVisitor()` | destructor | `None` | public | — |
| `initialise_pre_property_values( const GPlatesModel::TopLevelPropertyInline &top_level_property_inline)` | method | `bool` | protected | — |
| `visit_gpml_key_value_dictionary( const GPlatesPropertyValues::GpmlKeyValueDictionary &dictionary)` | method | `void` | protected | — |
| `visit_xs_boolean( const GPlatesPropertyValues::XsBoolean &xs_boolean)` | method | `void` | protected | — |
| `visit_xs_double( const GPlatesPropertyValues::XsDouble &xs_double)` | method | `void` | protected | — |
| `visit_xs_integer( const GPlatesPropertyValues::XsInteger& xs_integer)` | method | `void` | protected | — |
| `visit_xs_string( const GPlatesPropertyValues::XsString &xs_string)` | method | `void` | protected | — |
| `d_names` | field | `std::vector < QString >` | private | — |

## Free functions and macros

| Name | Kind | Type / body | Description |
|---|---|---|---|
| `GPLATES_FEATUREVISITORS_POPULATESHAPEFILEATTRIBUTESVISITOR_H` | macro | `None` | — |

## Notes

[[[PROSE notes unit=data-mining/PopulateShapeFileAttributesVisitor tier=3]]]
Replace this whole block, markers included, with invariants, ownership, threading or gotchas that are not visible in the tables. Write *None.* if there is nothing worth saying.
[[[/PROSE]]]

## Used by

| Unit | Component | References |
|---|---|---|
| [qt-widgets/CoRegistrationLayerConfigurationDialog](../qt-widgets/CoRegistrationLayerConfigurationDialog.md) | qt-widgets | 5 |

## Related

*None.*

## Explore

Run these from the `gplates-code` skill directory:

```bash
python scripts/gpq.py file src/data-mining/PopulateShapeFileAttributesVisitor.h
python scripts/gpq.py def GPlatesDataMining::PopulateShapeFileAttributesVisitor --body
python scripts/gpq.py uses PopulateShapeFileAttributesVisitor --kind class
python scripts/gpq.py hier PopulateShapeFileAttributesVisitor
```
