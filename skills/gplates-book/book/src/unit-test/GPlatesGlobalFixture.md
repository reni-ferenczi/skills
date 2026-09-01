# GPlatesGlobalFixture

[Book TOC](../../TOC.md) · [unit-test](../../components/unit-test.md) · cluster Community 863 · tier 3

| Source file | Kind | Lines |
|---|---|---|
| `src/unit-test/GPlatesGlobalFixture.h` | C++ | 49 |

## Overview

A global Boost.Test fixture that redirects test logging to a file. The fixture opens a file stream to `GPlates_unit_test.log` during construction and installs it as the Boost.Test logging destination, then restores logging to standard output on destruction. Declared as a global fixture, it runs once at the start and end of the entire test session.

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

*None.*

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
