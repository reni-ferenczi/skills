# GPlatesGlobalFixture

[Book TOC](../../TOC.md) · [unit-test](../../components/unit-test.md) · cluster Community 863 · tier 3

| Source file | Kind | Lines |
|---|---|---|
| `src/unit-test/GPlatesGlobalFixture.h` | C++ | 49 |

## Overview

[[[PROSE overview unit=unit-test/GPlatesGlobalFixture tier=3]]]
Replace this whole block, markers included, with 1-3 paragraphs: what this unit is, why it exists, and how it fits the surrounding design. Do not restate the tables below.
[[[/PROSE]]]

## Declared types

| Name | Kind | Bases | Template | Subclasses | Description |
|---|---|---|---|---|---|
| [`GPlatesGlobalFixture`](#gplatesglobalfixture) | struct | — | — | 0 | — |

## Members

### `GPlatesGlobalFixture`

| Member | Kind | Type | Access | Description |
|---|---|---|---|---|
| `GPlatesGlobalFixture()` | constructor | `None` | public | — |
| `~GPlatesGlobalFixture()` | destructor | `None` | public | — |
| `test_log` | field | `std::ofstream` | public | — |

## Free functions and macros

| Name | Kind | Type / body | Description |
|---|---|---|---|
| `GPLATES_UNIT_TEST_GLOBALFIXTURE_H` | macro | `None` | — |

## Notes

[[[PROSE notes unit=unit-test/GPlatesGlobalFixture tier=3]]]
Replace this whole block, markers included, with invariants, ownership, threading or gotchas that are not visible in the tables. Write *None.* if there is nothing worth saying.
[[[/PROSE]]]

## Used by

| Unit | Component | References |
|---|---|---|
| [entry-points/gplates_unit_test_main](../entry-points/gplates_unit_test_main.md) | entry-points | 2 |

## Related

*None.*

## Explore

Run these from the `gplates-code` skill directory:

```bash
python scripts/gpq.py file src/unit-test/GPlatesGlobalFixture.h
python scripts/gpq.py def GPlatesGlobalFixture --body
python scripts/gpq.py uses GPlatesGlobalFixture --kind struct
python scripts/gpq.py hier GPlatesGlobalFixture
```
