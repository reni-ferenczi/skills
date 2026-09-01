# global

[Book TOC](../TOC.md)

31 unit page(s), 36 source file(s) documented here, 4 further file(s) listed below.

## Overview

`global` is the foundation tier of GPlates: it carries no reconstruction logic of its own, only the exception hierarchy, assertion machinery, and a handful of header-level utilities that the rest of the tree is built on. Nothing in the reconstruction pipeline calls into `global` to get work done; instead, when maths code rejects degenerate input, when a file reader hits a corrupt driver, or when internal state that should be impossible turns up, the failure is reported through a type this component defines, so that one top-level handler — `GPlatesGui::GPlatesQApplication::notify`'s `try_catch` — can catch, log and report it the same way no matter which component it came from.

The load-bearing units are almost all pieces of that exception tree. `GPlatesException` is the abstract root: its constructor snapshots the process-wide `CallStack` at the moment of the throw, and deriving from `QtStreamable` lets the same object stream to `qDebug` and a `QMessageBox` without a second formatting path. `GPlatesAssert` is the project's replacement for C `assert` — one written check that traps into the debugger on a `GPLATES_DEBUG` build and throws the chosen exception type on release — and `AssertionFailureException` is the default type it throws, marking "the program's own state is broken" as opposed to `PreconditionViolationError`, the other branch of the tree, which fourteen subclasses across `maths`, `property-values` and `opengl` derive from to reject bad caller-supplied arguments. `AbortException` covers the same "state is broken" ground for `GPlatesGlobal::Abort`, `ExternalResourceFailureException` is the base callers intercept when a file, driver or other outside resource misbehaves, and `LogException` is the catch-all, free-form-message exception that most file readers and export code reach for rather than defining a dedicated type. Two units matter for unrelated reasons: `PointerTraits`, a header-only trick that lets mutually-recursive templates such as `model`'s `BasicHandle`/`BasicRevision` and `app-logic`'s layer proxies name each other's `non_null_ptr_type` without including each other's headers; and `CompilerWarnings`, whose push/pop/enable/disable macros are how the rest of the tree silences specific gcc or MSVC warnings around third-party headers such as Qt's moc output, Boost and GDAL.

`global`'s own dependency runs one way, on `utils`: it borrows `CallStack` (the hand-maintained singleton `GPlatesException` snapshots at every throw), `QtStreamable` (the mixin behind every exception's `operator<<`), and `non_null_intrusive_ptr` (the type `PointerTraits` names without including). Every other component is a consumer rather than a peer, which is why the "Used by" table is so lopsided: `opengl`, `app-logic`, `gui`, `file-io` and `qt-widgets` carry the heaviest reference counts because invalid GL state, missing files, malformed geometry and bad user input are exactly the failures this component exists to name, and `scribe` leans on `GPlatesAssert` almost as hard because its (de)serialisation code treats a corrupt archive as the same kind of internal inconsistency. What crosses every one of those edges is never data, only control — a thrown exception type, an aborted process, or a header-only pointer alias that lets a dependent header skip a heavier include.

## Units

### `src/global`

| Unit | Tier | Lines | Fan-in | Description |
|---|---|---|---|---|
| [AbortException](../src/global/AbortException.md) | 2 | 104 | 47 | Exception subclass for aborts signalling corrupted internal program state |
| [AssertionFailureException](../src/global/AssertionFailureException.md) | 1 | 105 | 2599 | the exception thrown when an internal-state check fails; carries only the throw location |
| [CompilerWarnings](../src/global/CompilerWarnings.md) | 2 | 136 | 56 | Compiler-neutral macros to push/pop/enable/disable specific gcc and MSVC warnings |
| [ControlFlowException](../src/global/ControlFlowException.md) | 3 | 75 | 0 | Exception thrown when unreachable code is executed |
| [ExternalResourceFailureException](../src/global/ExternalResourceFailureException.md) | 2 | 58 | 27 | Base exception for failures of external resources such as files or drivers |
| [GPlatesAssert](../src/global/GPlatesAssert.md) | 1 | 267 | 3310 | the project's assert: aborts into the debugger on debug builds, throws a chosen exception on release |
| [GPlatesException](../src/global/GPlatesException.md) | 1 | 325 | 777 | the root of the GPlates exception hierarchy and the call-stack snapshot taken at each throw |
| [GdalVersion](../src/global/GdalVersion.md) | 2 | 60 | 22 | Re-declares GDAL's version-compute macros so version checks compile on old GDAL |
| [IllegalParametersException](../src/global/IllegalParametersException.md) | 3 | 75 | 2 | Exception thrown for illegal or unreasonable method parameters |
| [InternalInconsistencyException](../src/global/InternalInconsistencyException.md) | 3 | 127 | 1 | Exception thrown when unexpected internal inconsistencies are detected |
| [InternalObjectInconsistencyException](../src/global/InternalObjectInconsistencyException.md) | 3 | 52 | 6 | Base class for exceptions reporting object-level internal inconsistencies |
| [IntrusivePointerZeroRefCountException](../src/global/IntrusivePointerZeroRefCountException.md) | 3 | 83 | 2 | Exception thrown when an intrusive pointer reference count reaches zero unexpectedly |
| [InvalidFeatureCollectionException](../src/global/InvalidFeatureCollectionException.md) | 3 | 73 | 3 | Exception thrown when an invalid FeatureCollectionHandle is encountered |
| [InvalidParametersException](../src/global/InvalidParametersException.md) | 3 | 73 | 1 | Exception thrown for parameters that are individually valid but invalid in combination |
| [License](../src/global/License.md) | 3 | 49 | 2 | Functions providing GPlates copyright information in plain text and HTML |
| [LogException](../src/global/LogException.md) | 2 | 117 | 102 | Catch-all exception carrying a free-form message when no dedicated type exists |
| [NotYetImplementedException](../src/global/NotYetImplementedException.md) | 3 | 62 | 3 | Exception for code that has not yet been implemented |
| [NullParameterException](../src/global/NullParameterException.md) | 3 | 74 | 1 | Exception for NULL pointer parameters when non-null expected |
| [PointerTraits](../src/global/PointerTraits.md) | 1 | 89 | 477 | names a class's non\_null\_ptr\_type without including its header, to break include cycles |
| [PreconditionViolationError](../src/global/PreconditionViolationError.md) | 1 | 63 | 522 | the branch of the exception tree for invalid arguments, as opposed to broken internal state |
| [RetrievalFromEmptyContainerException](../src/global/RetrievalFromEmptyContainerException.md) | 3 | 82 | 1 | Exception when retrieving from an empty container |
| [UnexpectedEmptyFeatureCollectionException](../src/global/UnexpectedEmptyFeatureCollectionException.md) | 3 | 73 | 1 | Exception when receiving an unexpectedly empty FeatureCollectionHandle |
| [UninitialisedIteratorException](../src/global/UninitialisedIteratorException.md) | 3 | 74 | 4 | Exception when dereferencing an uninitialized iterator |
| [UnsupportedFunctionException](../src/global/UnsupportedFunctionException.md) | 3 | 74 | 0 | Exception for deliberately unsupported functions |
| [Version](../src/global/Version.md) | 2 | 135 | 27 | Reports GPlates and pyGPlates version numbers and pre-release suffixes |
| [python](../src/global/python.md) | 2 | 172 | 15 | Mandatory wrapper around including Python.h and boost/python.hpp safely |
| [unicode](../src/global/unicode.md) | 3 | 32 | 0 | Convenience header providing access to Unicode string utilities |

### `src/global/deprecated`

| Unit | Tier | Lines | Fan-in | Description |
|---|---|---|---|---|
| [AlreadyInitialisedSingletonException](../src/global/deprecated/AlreadyInitialisedSingletonException.md) | 3 | 73 | 0 | Deprecated: exception for double-initialization of singletons |
| [InternalRID](../src/global/deprecated/InternalRID.md) | 3 | 108 | 1 | Deprecated: wrapper for rotation ID values |
| [UninitialisedSingletonException](../src/global/deprecated/UninitialisedSingletonException.md) | 3 | 72 | 0 | Deprecated exception for uninitialized singleton access attempts |
| [types](../src/global/deprecated/types.md) | 3 | 83 | 42 | Deprecated type aliases and enumerations for geometry and topology classification |


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
