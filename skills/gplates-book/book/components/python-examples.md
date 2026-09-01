# python-examples

[Book TOC](../TOC.md)

Stand-alone pyGPlates demo and utility scripts.

1 unit page(s), 7 source file(s) documented here, 26 further file(s) listed below.

## Overview

[[[PROSE component unit=component:python-examples tier=1]]]
Replace this whole block, markers included, with 2-4 paragraphs: what this component is responsible for, the load-bearing units and how it connects to neighbouring components. Do not restate the unit table.
[[[/PROSE]]]

## Units

| Unit | Tier | Lines | Fan-in | Description |
|---|---|---|---|---|
| [python-examples](../src/scripts/python-examples.md) | 3 | 3876 | 0 | example scripts demonstrating the pygplates API for reconstruction, interpolation, camera control, co-registration and plate motion analysis |

## Other files

| File | Kind | Lines |
|---|---|---|
| `scripts/deprecated/orange-widget/CombineDomains.py` | Python | 47 |
| `scripts/deprecated/orange-widget/LoadCoregFileSelectTime.py` | Python | 213 |
| `scripts/deprecated/orange-widget/OWAttributeAtTime.py` | Python | 143 |
| `scripts/deprecated/orange-widget/OWBirthAttribute.py` | Python | 154 |
| `scripts/deprecated/orange-widget/OWBirthTime.py` | Python | 113 |
| `scripts/deprecated/orange-widget/OWMergeRowAligned.py` | Python | 80 |
| `scripts/deprecated/orange-widget/OWOrdinalSignature.py` | Python | 229 |
| `scripts/deprecated/orange-widget/OWReadDataSingleTime.py` | Python | 160 |
| `scripts/deprecated/orange-widget/OWStringToNum.py` | Python | 106 |
| `scripts/deprecated/orange-widget/OWTimeSeries.py` | Python | 207 |
| `scripts/deprecated/orange-widget/__init__.py` | Python | 22 |
| `scripts/deprecated/orange-widget/attr_at_time.ui` | Qt form | 124 |
| `scripts/deprecated/orange-widget/birth_attr.ui` | Qt form | 101 |
| `scripts/deprecated/orange-widget/birth_time.ui` | Qt form | 68 |
| `scripts/deprecated/orange-widget/example.py` | Python | 78 |
| `scripts/deprecated/orange-widget/gplates.py` | Python | 398 |
| `scripts/deprecated/orange-widget/icons/combine_data.png` | other | 0 |
| `scripts/deprecated/orange-widget/icons/compute_attrib_at_time.png` | other | 0 |
| `scripts/deprecated/orange-widget/icons/compute_birth_attribute.png` | other | 0 |
| `scripts/deprecated/orange-widget/icons/compute_birth_time.png` | other | 0 |
| `scripts/deprecated/orange-widget/icons/load_data_select_time.png` | other | 0 |
| `scripts/deprecated/orange-widget/icons/merge_timedepdata.png` | other | 0 |
| `scripts/deprecated/orange-widget/icons/ordinal_signature.png` | other | 0 |
| `scripts/deprecated/orange-widget/icons/string_to_num.png` | other | 0 |
| `scripts/deprecated/orange-widget/time_series.ui` | Qt form | 261 |
| `scripts/deprecated/orange_demo.py` | Python | 66 |

## Depends on

*None.*

## Used by

*None.*

## Explore

Run these from the `gplates-code` skill directory:

```bash
python scripts/gpq.py tree scripts
python scripts/gpq.py sym . --mode sub --path scripts --defs-only
```
