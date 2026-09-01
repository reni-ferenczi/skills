# global

[Book TOC](../TOC.md)

31 unit page(s), 36 source file(s) documented here, 4 further file(s) listed below.

## Overview

[[[PROSE component unit=component:global tier=1]]]
Replace this whole block, markers included, with 2-4 paragraphs: what this component is responsible for, the load-bearing units and how it connects to neighbouring components. Do not restate the unit table.
[[[/PROSE]]]

## Units

### `src/global`

| Unit | Tier | Lines | Fan-in | Description |
|---|---|---|---|---|
| [AbortException](../src/global/AbortException.md) | 2 | 104 | 47 | (pending) |
| [AssertionFailureException](../src/global/AssertionFailureException.md) | 1 | 105 | 2599 | (pending) |
| [CompilerWarnings](../src/global/CompilerWarnings.md) | 2 | 136 | 56 | (pending) |
| [ControlFlowException](../src/global/ControlFlowException.md) | 3 | 75 | 0 | (pending) |
| [ExternalResourceFailureException](../src/global/ExternalResourceFailureException.md) | 2 | 58 | 27 | (pending) |
| [GPlatesAssert](../src/global/GPlatesAssert.md) | 1 | 267 | 3310 | (pending) |
| [GPlatesException](../src/global/GPlatesException.md) | 1 | 325 | 777 | (pending) |
| [GdalVersion](../src/global/GdalVersion.md) | 2 | 60 | 22 | (pending) |
| [IllegalParametersException](../src/global/IllegalParametersException.md) | 3 | 75 | 2 | (pending) |
| [InternalInconsistencyException](../src/global/InternalInconsistencyException.md) | 3 | 127 | 1 | (pending) |
| [InternalObjectInconsistencyException](../src/global/InternalObjectInconsistencyException.md) | 3 | 52 | 6 | (pending) |
| [IntrusivePointerZeroRefCountException](../src/global/IntrusivePointerZeroRefCountException.md) | 3 | 83 | 2 | (pending) |
| [InvalidFeatureCollectionException](../src/global/InvalidFeatureCollectionException.md) | 3 | 73 | 3 | (pending) |
| [InvalidParametersException](../src/global/InvalidParametersException.md) | 3 | 73 | 1 | (pending) |
| [License](../src/global/License.md) | 3 | 49 | 2 | (pending) |
| [LogException](../src/global/LogException.md) | 2 | 117 | 102 | (pending) |
| [NotYetImplementedException](../src/global/NotYetImplementedException.md) | 3 | 62 | 3 | (pending) |
| [NullParameterException](../src/global/NullParameterException.md) | 3 | 74 | 1 | (pending) |
| [PointerTraits](../src/global/PointerTraits.md) | 1 | 89 | 477 | (pending) |
| [PreconditionViolationError](../src/global/PreconditionViolationError.md) | 1 | 63 | 522 | (pending) |
| [RetrievalFromEmptyContainerException](../src/global/RetrievalFromEmptyContainerException.md) | 3 | 82 | 1 | (pending) |
| [UnexpectedEmptyFeatureCollectionException](../src/global/UnexpectedEmptyFeatureCollectionException.md) | 3 | 73 | 1 | (pending) |
| [UninitialisedIteratorException](../src/global/UninitialisedIteratorException.md) | 3 | 74 | 4 | (pending) |
| [UnsupportedFunctionException](../src/global/UnsupportedFunctionException.md) | 3 | 74 | 0 | (pending) |
| [Version](../src/global/Version.md) | 2 | 135 | 27 | (pending) |
| [python](../src/global/python.md) | 2 | 172 | 15 | (pending) |
| [unicode](../src/global/unicode.md) | 3 | 32 | 0 | (pending) |

### `src/global/deprecated`

| Unit | Tier | Lines | Fan-in | Description |
|---|---|---|---|---|
| [AlreadyInitialisedSingletonException](../src/global/deprecated/AlreadyInitialisedSingletonException.md) | 3 | 73 | 0 | (pending) |
| [InternalRID](../src/global/deprecated/InternalRID.md) | 3 | 108 | 1 | (pending) |
| [UninitialisedSingletonException](../src/global/deprecated/UninitialisedSingletonException.md) | 3 | 72 | 0 | (pending) |
| [types](../src/global/deprecated/types.md) | 3 | 83 | 42 | (pending) |


## Other files

| File | Kind | Lines |
|---|---|---|
| `src/global/CMakeLists.txt` | build | 47 |
| `src/global/License.cc.in` | build | 39 |
| `src/global/Version.cc.in` | build | 155 |
| `src/global/config.h.in` | build | 50 |

## Depends on

| Component | References |
|---|---|
| [utils](utils.md) | 122 |

## Used by

| Component | References |
|---|---|
| [opengl](opengl.md) | 2351 |
| [app-logic](app-logic.md) | 1160 |
| [gui](gui.md) | 978 |
| [file-io](file-io.md) | 910 |
| [qt-widgets](qt-widgets.md) | 827 |
| [maths](maths.md) | 726 |
| [scribe](scribe.md) | 689 |
| [model](model.md) | 283 |
| [presentation](presentation.md) | 281 |
| [utils](utils.md) | 194 |
| [view-operations](view-operations.md) | 190 |
| [property-values](property-values.md) | 130 |
| [api](api.md) | 74 |
| [data-mining](data-mining.md) | 51 |
| [cli](cli.md) | 46 |
| [deprecated](deprecated.md) | 33 |
| [unit-test](unit-test.md) | 29 |
| [entry-points](entry-points.md) | 16 |
| [feature-visitors](feature-visitors.md) | 13 |
| [canvas-tools](canvas-tools.md) | 6 |

## Explore

Run these from the `gplates-code` skill directory:

```bash
python scripts/gpq.py tree src/global
python scripts/gpq.py sym . --mode sub --path src/global --defs-only
```
