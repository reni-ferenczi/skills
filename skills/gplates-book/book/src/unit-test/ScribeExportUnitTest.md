# ScribeExportUnitTest

[Book TOC](../../TOC.md) · [unit-test](../../components/unit-test.md) · cluster Community 16 · tier 3

| Source file | Kind | Lines |
|---|---|---|
| `src/unit-test/ScribeExportUnitTest.h` | C++ | 54 |

## Overview

[[[PROSE overview unit=unit-test/ScribeExportUnitTest tier=3]]]
Replace this whole block, markers included, with 1-3 paragraphs: what this unit is, why it exists, and how it fits the surrounding design. Do not restate the tables below.
[[[/PROSE]]]

## Declared types

*None.*

## Members

*None.*

## Free functions and macros

| Name | Kind | Type / body | Description |
|---|---|---|---|
| `GPLATES_UNIT_TEST_SCRIBEEXPORTUNITTEST_H` | macro | `None` | — |
| `SCRIBE_EXPORT_UNIT_TEST` | macro | `((GPlatesUnitTest::TranscribePrimitivesTest::Data::NonDefaultConstructable, \ "GPlatesUnitTest::TranscribePrimitivesTest::Data::NonDefaultConstructable")) \ \ ((GPlatesUnitTest::Tr ...` | Scribe export registered classes/types in the 'unit-test' source sub-directory. |

## Notes

[[[PROSE notes unit=unit-test/ScribeExportUnitTest tier=3]]]
Replace this whole block, markers included, with invariants, ownership, threading or gotchas that are not visible in the tables. Write *None.* if there is nothing worth saying.
[[[/PROSE]]]

## Used by

| Unit | Component | References |
|---|---|---|
| [entry-points/ScribeExportGPlatesUnitTest](../entry-points/ScribeExportGPlatesUnitTest.md) | entry-points | 1 |

## Related

*None.*

## Explore

Run these from the `gplates-code` skill directory:

```bash
python scripts/gpq.py file src/unit-test/ScribeExportUnitTest.h
```
