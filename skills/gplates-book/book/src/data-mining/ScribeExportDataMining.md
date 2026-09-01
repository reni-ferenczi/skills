# ScribeExportDataMining

[Book TOC](../../TOC.md) · [data-mining](../../components/data-mining.md) · cluster Community 16 · tier 3

| Source file | Kind | Lines |
|---|---|---|
| `src/data-mining/ScribeExportDataMining.h` | C++ | 56 |

## Overview

Registers Scribe serialization mappings for the data-mining filter configuration classes: `DummyFilter::Config`, `RegionOfInterestFilter::Config`, and `SeedSelfFilter::Config`. Each mapping associates a runtime class with a stable string identifier used during serialization and deserialization. This header is included by the entry-points serialization registration layer to make these types available to the broader GPlates persistence system.

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

The string identifiers used here must never change, as they are persisted in saved files. Modifying or removing an identifier breaks backward compatibility with existing GPlates projects. When adding new filter types to the data-mining module, add their registrations to this macro.

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
