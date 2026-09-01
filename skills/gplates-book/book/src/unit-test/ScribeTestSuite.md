# ScribeTestSuite

[Book TOC](../../TOC.md) · [unit-test](../../components/unit-test.md) · cluster Community 1727 · tier 3

| Source file | Kind | Lines |
|---|---|---|
| `src/unit-test/ScribeTestSuite.h` | C++ | 55 |
| `src/unit-test/ScribeTestSuite.cc` | C++ | 43 |

## Overview

Test suite for the `GPlatesScribe` serialization framework. The Scribe module is the serialization layer that handles persistence of GPlates projects and sessions, and this suite exercises the transcription mechanism that Scribe uses to convert objects to and from serialized form.

## Declared types

| Name | Kind | Bases | Template | Subclasses | Description |
|---|---|---|---|---|---|
| [`GPlatesUnitTest::ScribeTestSuite`](#gplatesunittestscribetestsuite) | class | [`GPlatesUnitTest::GPlatesTestSuite`](GPlatesTestSuite.md) | — | 0 | — |

## Members

### `GPlatesUnitTest::ScribeTestSuite`

| Member | Kind | Type | Access | Description |
|---|---|---|---|---|
| `ScribeTestSuite( unsigned depth)` | constructor | `None` | public | — |
| `construct_maps()` | method | `void` | protected | — |

## Free functions and macros

| Name | Kind | Type / body | Description |
|---|---|---|---|
| `GPLATES_UNIT_TEST_SCRIBETESTSUITE_H` | macro | `None` | — |

## Notes

*None.*

## Used by

| Unit | Component | References |
|---|---|---|
| [unit-test/MainTestSuite](MainTestSuite.md) | unit-test | 1 |

## Related

*None.*

## Explore

Run these from the `gplates-code` skill directory:

```bash
python scripts/gpq.py file src/unit-test/ScribeTestSuite.h
python scripts/gpq.py def GPlatesUnitTest::ScribeTestSuite --body
python scripts/gpq.py uses ScribeTestSuite --kind class
python scripts/gpq.py hier ScribeTestSuite
```
