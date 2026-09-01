# system-fixes

[Book TOC](../TOC.md)

3 unit page(s), 3 source file(s) documented here, 1 further file(s) listed below.

## Overview

[[[PROSE component unit=component:system-fixes tier=1]]]
Replace this whole block, markers included, with 2-4 paragraphs: what this component is responsible for, the load-bearing units and how it connects to neighbouring components. Do not restate the unit table.
[[[/PROSE]]]

## Units

### `src/system-fixes/boost`

| Unit | Tier | Lines | Fan-in | Description |
|---|---|---|---|---|
| [cstdint](../src/system-fixes/boost/cstdint.md) | 3 | 44 | 0 | Compatibility wrapper for Boost cstdint header fixing Visual Studio 2010 UINT8\_C macro conflicts |

### `src/system-fixes/loki`

| Unit | Tier | Lines | Fan-in | Description |
|---|---|---|---|---|
| [RefToValue](../src/system-fixes/loki/RefToValue.md) | 3 | 68 | 8 | Template class transporting references as values for smart pointers and scope guards |
| [ScopeGuard](../src/system-fixes/loki/ScopeGuard.md) | 2 | 382 | 12 | (pending) |


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
