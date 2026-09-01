# Counter64

[Book TOC](../../TOC.md) · [utils](../../components/utils.md) · cluster Community 838 · tier 2

| Source file | Kind | Lines |
|---|---|---|
| `src/utils/Counter64.h` | C++ | 147 |

## Overview

`GPlatesUtils::Counter64` is a monotonically-incrementing 64-bit counter used
as a cheap "has anything changed" or "generation number" token — for example
tracking observer/revision counts on `ReconstructionGeometry` and its
subclasses, or resource generation counters in the `opengl` raster/buffer
classes. It only supports increment, equality and less-than, via Boost's
`operators.hpp` mixins (`boost::incrementable`, `boost::equality_comparable`,
`boost::less_than_comparable`), which derive the remaining operators
(`operator++(int)`, `operator!=`, `operator<=`, etc.) from the three it
implements directly.

Two implementations are compiled depending on `BOOST_NO_INT64_T`: the normal
path stores a single `boost::uint64_t`, while a fallback for compilers
without a native 64-bit integer type composes the counter from two
`boost::uint32_t` halves and detects overflow of the low half manually to
carry into the high half. Both behave identically to callers.

## Declared types

| Name | Kind | Bases | Template | Subclasses | Description |
|---|---|---|---|---|---|
| [`GPlatesUtils::Counter64`](#gplatesutilscounter64) | class | `boost::incrementable<Counter64>`<br>`boost::equality_comparable<Counter64>`<br>`boost::less_than_comparable<Counter64>` | — | 0 | A 64-bit counter that delegates to boost::uint64\_t. |

## Members

### `GPlatesUtils::Counter64`

| Member | Kind | Type | Access | Description |
|---|---|---|---|---|
| `Counter64( boost::uint32_t counter = 0)` | constructor | `None` | public | Constructor to instantiate from a 32-bit integer (defaults to zero). |
| `operator==( const Counter64 &other)` | operator | `bool` | public | — |
| `operator<( const Counter64 &other)` | operator | `bool` | public | — |
| `d_counter` | field | `boost::uint64_t` | private | Use built-in 64-bit integers where available. |

## Free functions and macros

| Name | Kind | Type / body | Description |
|---|---|---|---|
| `GPLATES_UTILS_COUNTER64_H` | macro | `None` | — |

## Notes

- The counter is increment-only by design; there is no `operator--` or
  decrement support in either implementation.
- Overflow is a known non-issue in practice: even incrementing every CPU
  cycle on a 3 GHz machine would take about 195 years to wrap a 64-bit
  counter, so wraparound is not guarded against.
- Not thread-safe: `operator++` reads and writes `d_counter` (or the
  two-word fallback) with no synchronisation.

## Used by

| Unit | Component | References |
|---|---|---|
| [opengl/GLMultiResolutionCubeRasterInterface](../opengl/GLMultiResolutionCubeRasterInterface.md) | opengl | 7 |
| [app-logic/ReconstructedFeatureGeometry](../app-logic/ReconstructedFeatureGeometry.md) | app-logic | 4 |
| [app-logic/ResolvedTopologicalNetwork](../app-logic/ResolvedTopologicalNetwork.md) | app-logic | 4 |
| [opengl/GLMultiResolutionRasterInterface](../opengl/GLMultiResolutionRasterInterface.md) | opengl | 4 |
| [utils/SubjectObserverToken](SubjectObserverToken.md) | utils | 4 |
| [app-logic/ReconstructHandle](../app-logic/ReconstructHandle.md) | app-logic | 3 |
| [app-logic/ReconstructMethodInterface](../app-logic/ReconstructMethodInterface.md) | app-logic | 3 |
| [app-logic/ReconstructedFlowline](../app-logic/ReconstructedFlowline.md) | app-logic | 3 |
| [app-logic/ReconstructionGeometry](../app-logic/ReconstructionGeometry.md) | app-logic | 3 |
| [app-logic/ResolvedTopologicalGeometrySubSegment](../app-logic/ResolvedTopologicalGeometrySubSegment.md) | app-logic | 3 |
| [app-logic/ResolvedTopologicalSection](../app-logic/ResolvedTopologicalSection.md) | app-logic | 3 |
| [app-logic/ResolvedTopologicalSharedSubSegment](../app-logic/ResolvedTopologicalSharedSubSegment.md) | app-logic | 3 |
| [app-logic/ReconstructMethodMotionPath](../app-logic/ReconstructMethodMotionPath.md) | app-logic | 2 |
| [app-logic/ReconstructMethodSmallCircle](../app-logic/ReconstructMethodSmallCircle.md) | app-logic | 2 |
| [app-logic/ReconstructMethodVirtualGeomagneticPole](../app-logic/ReconstructMethodVirtualGeomagneticPole.md) | app-logic | 2 |
| [app-logic/ReconstructedMotionPath](../app-logic/ReconstructedMotionPath.md) | app-logic | 2 |
| [app-logic/ReconstructedSmallCircle](../app-logic/ReconstructedSmallCircle.md) | app-logic | 2 |
| [app-logic/ReconstructedVirtualGeomagneticPole](../app-logic/ReconstructedVirtualGeomagneticPole.md) | app-logic | 2 |
| [app-logic/ResolvedScalarField3D](../app-logic/ResolvedScalarField3D.md) | app-logic | 2 |
| [opengl/GLBuffer](../opengl/GLBuffer.md) | opengl | 2 |

*... and 3 more units.*

## Related

*None.*

## Explore

Run these from the `gplates-code` skill directory:

```bash
python scripts/gpq.py file src/utils/Counter64.h
python scripts/gpq.py def GPlatesUtils::Counter64 --body
python scripts/gpq.py uses Counter64 --kind class
python scripts/gpq.py hier Counter64
```
