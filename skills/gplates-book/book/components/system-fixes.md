# system-fixes

[Book TOC](../TOC.md)

3 unit page(s), 3 source file(s) documented here, 1 further file(s) listed below.

## Overview

This component holds vendored, third-party compatibility code that GPlates carries in its own tree rather than depending on system-installed versions: a small Boost header patch and two headers lifted from the Loki library. It has no dependencies of its own on the rest of the codebase and exists purely to be leaned on — a foundation layer of low-level utilities that predates, and sits below, GPlates's own `utils` component.

`cstdint` is a compatibility wrapper around Boost's `cstdint` header that works around a Visual Studio 2010 conflict over the `UINT8_C` macro, undefining and reincluding it around the Boost header. It is pulled in mainly through precompiled headers, which is why its fan-out reaches broadly into `opengl` and `file-io` code that needs fixed-width integer types.

`ScopeGuardImplBase` and its `ScopeGuardImpl0`–`3` and `ObjScopeGuardImpl0`–`2` specializations implement Loki's scope-guard idiom: an RAII object that runs a stored cleanup action on destruction unless dismissed, giving exception-safe rollback without hand-written `try`/`catch` blocks. `RefToValue` supports this and `Loki::SmartPtr` by transporting a reference as a copyable value (the Colvin/Gibbons trick), which is what lets a guard's bound arguments flow through templates that expect value semantics.

`utils` is by far the heaviest consumer of this component, using `ScopeGuard` and `RefToValue` inside its caching and pooling utilities (`KeyValueCache`, `ObjectPool`) to guarantee cleanup runs even when an exception unwinds the stack mid-operation. `opengl`, `file-io`, `gui`, `property-values`, `entry-points`, `scribe`, `maths` and `model` each touch it more lightly, almost entirely through the `cstdint` wrapper reaching them via precompiled headers rather than through the Loki idioms.

## Units

### `src/system-fixes/boost`

| Unit | Tier | Lines | Fan-in | Description |
|---|---|---|---|---|
| [cstdint](../src/system-fixes/boost/cstdint.md) | 3 | 44 | 0 | Compatibility wrapper for Boost cstdint header fixing Visual Studio 2010 UINT8\_C macro conflicts |

### `src/system-fixes/loki`

| Unit | Tier | Lines | Fan-in | Description |
|---|---|---|---|---|
| [RefToValue](../src/system-fixes/loki/RefToValue.md) | 3 | 68 | 8 | Template class transporting references as values for smart pointers and scope guards |
| [ScopeGuard](../src/system-fixes/loki/ScopeGuard.md) | 2 | 382 | 12 | Loki scope-guard idiom: RAII cleanup action run on scope exit unless dismissed |


## Other files

| File | Kind | Lines |
|---|---|---|
| `src/system-fixes/loki/README` | doc | 44 |

## Depends on

*None.*

## Used by

| Component | References |
|---|---|
| [utils](utils.md) | 28 |
| [opengl](opengl.md) | 10 |
| [file-io](file-io.md) | 6 |
| [gui](gui.md) | 4 |
| [property-values](property-values.md) | 3 |
| [entry-points](entry-points.md) | 2 |
| [scribe](scribe.md) | 2 |
| [maths](maths.md) | 1 |
| [model](model.md) | 1 |

## Explore

Run these from the `gplates-code` skill directory:

```bash
python scripts/gpq.py tree src/system-fixes/boost
python scripts/gpq.py sym . --mode sub --path src/system-fixes/boost --defs-only
```
