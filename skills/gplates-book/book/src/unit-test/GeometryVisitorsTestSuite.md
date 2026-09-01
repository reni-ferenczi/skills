# GeometryVisitorsTestSuite

[Book TOC](../../TOC.md) · [unit-test](../../components/unit-test.md) · cluster Community 76 · tier 3

| Source file | Kind | Lines |
|---|---|---|
| `src/unit-test/GeometryVisitorsTestSuite.h` | C++ | 46 |
| `src/unit-test/GeometryVisitorsTestSuite.cc` | C++ | 46 |

## Overview

A container for test cases exercising geometry visitor patterns. The suite inherits from `GPlatesTestSuite` and manages the collection of individual tests via `construct_maps()`. Tests registered here exercise the visitor implementations in the `feature-visitors` module that walk features and extract geometry information.

## Declared types

| Name | Kind | Bases | Template | Subclasses | Description |
|---|---|---|---|---|---|
| [`GPlatesUnitTest::GeometryVisitorsTestSuite`](#gplatesunittestgeometryvisitorstestsuite) | class | [`GPlatesUnitTest::GPlatesTestSuite`](GPlatesTestSuite.md) | — | 0 | — |

## Members

### `GPlatesUnitTest::GeometryVisitorsTestSuite`

| Member | Kind | Type | Access | Description |
|---|---|---|---|---|
| `GeometryVisitorsTestSuite(unsigned depth)` | constructor | `None` | public | — |
| `construct_maps()` | method | `void` | protected | — |

## Free functions and macros

| Name | Kind | Type / body | Description |
|---|---|---|---|
| `GPLATES_UNIT_TEST_GEOMETRY_VISITORS_APP_LOGIC_TEST_SUITE_H` | macro | `None` | — |

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
python scripts/gpq.py file src/unit-test/GeometryVisitorsTestSuite.h
python scripts/gpq.py def GPlatesUnitTest::GeometryVisitorsTestSuite --body
python scripts/gpq.py uses GeometryVisitorsTestSuite --kind class
python scripts/gpq.py hier GeometryVisitorsTestSuite
```
