# NotYetImplementedException

[Book TOC](../../TOC.md) · [global](../../components/global.md) · cluster Community 8 · tier 3

| Source file | Kind | Lines |
|---|---|---|
| `src/global/NotYetImplementedException.h` | C++ | 62 |

## Overview

[[[PROSE overview unit=global/NotYetImplementedException tier=3]]]
Replace this whole block, markers included, with 1-3 paragraphs: what this unit is, why it exists, and how it fits the surrounding design. Do not restate the tables below.
[[[/PROSE]]]

## Declared types

| Name | Kind | Bases | Template | Subclasses | Description |
|---|---|---|---|---|---|
| [`GPlatesGlobal::NotYetImplementedException`](#gplatesglobalnotyetimplementedexception) | class | [`Exception`](GPlatesException.md) | — | 0 | Should be thrown when a function or call path not YET been implemented is called. |

## Members

### `GPlatesGlobal::NotYetImplementedException`

| Member | Kind | Type | Access | Description |
|---|---|---|---|---|
| `NotYetImplementedException( const GPlatesUtils::CallStack::Trace &exception_source)` | constructor | `None` | public | — |
| `~NotYetImplementedException()` | destructor | `None` | public | — |
| `exception_name()` | method | `char` | protected | — |

## Free functions and macros

| Name | Kind | Type / body | Description |
|---|---|---|---|
| `_GPLATES_GLOBAL_NOTYETIMPLEMENTEDEXCEPTION_H_` | macro | `None` | — |

## Notes

[[[PROSE notes unit=global/NotYetImplementedException tier=3]]]
Replace this whole block, markers included, with invariants, ownership, threading or gotchas that are not visible in the tables. Write *None.* if there is nothing worth saying.
[[[/PROSE]]]

## Used by

| Unit | Component | References |
|---|---|---|
| [api/CoReg](../api/CoReg.md) | api | 2 |
| [app-logic/ReconstructLayerProxy](../app-logic/ReconstructLayerProxy.md) | app-logic | 2 |
| [entry-points/gplates_main](../entry-points/gplates_main.md) | entry-points | 2 |
| [app-logic/ResolvedTopologicalNetwork](../app-logic/ResolvedTopologicalNetwork.md) | app-logic | 1 |
| [deprecated/controls/File](../deprecated/controls/File.md) | deprecated | 1 |
| [file-io/GpmlUpgradeReaderUtils](../file-io/GpmlUpgradeReaderUtils.md) | file-io | 1 |
| [unit-test/CoregTest](../unit-test/CoregTest.md) | unit-test | 1 |
| [utils/CommandLineParser](../utils/CommandLineParser.md) | utils | 1 |

## Related

*None.*

## Explore

Run these from the `gplates-code` skill directory:

```bash
python scripts/gpq.py file src/global/NotYetImplementedException.h
python scripts/gpq.py def GPlatesGlobal::NotYetImplementedException --body
python scripts/gpq.py uses NotYetImplementedException --kind class
python scripts/gpq.py hier NotYetImplementedException
```
