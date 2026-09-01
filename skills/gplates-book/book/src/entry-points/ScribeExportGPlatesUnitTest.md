# ScribeExportGPlatesUnitTest

[Book TOC](../../TOC.md) · [entry-points](../../components/entry-points.md) · cluster Community 16 · tier 3

| Source file | Kind | Lines |
|---|---|---|
| `src/ScribeExportGPlatesUnitTest.cc` | C++ | 47 |

## Overview

Defines the set of polymorphic classes and types that the Scribe serialization framework will register as available for transcription in the unit test executable. The macro combines types from the unit-test module with external types, enabling the test suite to serialize and deserialize test objects and project files.

## Declared types

*None.*

## Members

*None.*

## Free functions and macros

| Name | Kind | Type / body | Description |
|---|---|---|---|
| `SCRIBE_EXPORT_GPLATES_UNIT_TEST` | macro | `SCRIBE_EXPORT_UNIT_TEST \ SCRIBE_EXPORT_EXTERNAL` | Group all classes/types to be scribe export registered for the 'gplates-unit-test' program. |

## Notes

*None.*

## Used by

*Nothing in the tree references this unit.*

## Related

*None.*

## Explore

Run these from the `gplates-code` skill directory:

```bash
python scripts/gpq.py file src/ScribeExportGPlatesUnitTest.cc
```
