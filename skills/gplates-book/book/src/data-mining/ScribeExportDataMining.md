# ScribeExportDataMining

[Book TOC](../../TOC.md) · [data-mining](../../components/data-mining.md) · cluster Community 16 · tier 3

| Source file | Kind | Lines |
|---|---|---|
| `src/data-mining/ScribeExportDataMining.h` | C++ | 56 |

## Overview

[[[PROSE overview unit=data-mining/ScribeExportDataMining tier=3]]]
Replace this whole block, markers included, with 1-3 paragraphs: what this unit is, why it exists, and how it fits the surrounding design. Do not restate the tables below.
[[[/PROSE]]]

## Declared types

*None.*

## Members

*None.*

## Free functions and macros

| Name | Kind | Type / body | Description |
|---|---|---|---|
| `GPLATES_DATA_MINING_SCRIBEEXPORTDATAMINING_H` | macro | `None` | — |
| `SCRIBE_EXPORT_DATA_MINING` | macro | `((GPlatesDataMining::DummyFilter::Config, \ "GPlatesDataMining::DummyFilter::Config")) \ \ ((GPlatesDataMining::RegionOfInterestFilter::Config, \ "GPlatesDataMining::RegionOfIntere ...` | Scribe export registered classes/types in the 'data-mining' source sub-directory. |

## Notes

[[[PROSE notes unit=data-mining/ScribeExportDataMining tier=3]]]
Replace this whole block, markers included, with invariants, ownership, threading or gotchas that are not visible in the tables. Write *None.* if there is nothing worth saying.
[[[/PROSE]]]

## Used by

| Unit | Component | References |
|---|---|---|
| [entry-points/ScribeExportGPlates](../entry-points/ScribeExportGPlates.md) | entry-points | 1 |

## Related

*None.*

## Explore

Run these from the `gplates-code` skill directory:

```bash
python scripts/gpq.py file src/data-mining/ScribeExportDataMining.h
```
