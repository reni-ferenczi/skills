# NotYetImplementedException

[Book TOC](../../TOC.md) · [global](../../components/global.md) · cluster Community 8 · tier 3

| Source file | Kind | Lines |
|---|---|---|
| `src/global/NotYetImplementedException.h` | C++ | 62 |

## Overview

Exception thrown when code that has not yet been implemented is invoked. This is a placeholder exception for incomplete features — when a function or code path is stubbed out but not yet fully written, throwing this signals that the feature needs work before it can be used. It inherits from `Exception`, the base class for all GPlates exceptions, and captures the call stack trace at the point of throwing for debugging.

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

*None.*

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
