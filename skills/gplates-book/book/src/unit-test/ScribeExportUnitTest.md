# ScribeExportUnitTest

[Book TOC](../../TOC.md) · [unit-test](../../components/unit-test.md) · cluster Community 16 · tier 3

| Source file | Kind | Lines |
|---|---|---|
| `src/unit-test/ScribeExportUnitTest.h` | C++ | 54 |

## Overview

Registers test classes with the Scribe serialization framework. This header-only file defines the `SCRIBE_EXPORT_UNIT_TEST` macro, which enrolls several transcription test types—`TranscribePrimitivesTest::Data::NonDefaultConstructable`, `TranscribeInheritanceTest::D`, and `TranscribeCompatibilityTest::Derived`—for object serialization support. These registrations enable the Scribe framework to serialize and deserialize test objects, supporting the transcription tests in `TranscribeTest.h`.

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

String IDs for serialized types are part of the serialization format; changing them breaks backward and forward compatibility with saved objects.

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
