# utils

[Book TOC](../TOC.md)

68 unit page(s), 93 source file(s) documented here, 1 further file(s) listed below.

## Overview

[[[PROSE component unit=component:utils tier=1]]]
Replace this whole block, markers included, with 2-4 paragraphs: what this component is responsible for, the load-bearing units and how it connects to neighbouring components. Do not restate the unit table.
[[[/PROSE]]]

## Units

### `src/utils`

| Unit | Tier | Lines | Fan-in | Description |
|---|---|---|---|---|
| [AnimationSequenceUtils](../src/utils/AnimationSequenceUtils.md) | 2 | 316 | 69 | Turns a start/end time and increment into a shared animation frame schedule |
| [Base2Utils](../src/utils/Base2Utils.md) | 2 | 234 | 114 | Bit-hack helpers for power-of-two rounding and log2 on 32-bit integers |
| [CallStackTracker](../src/utils/CallStackTracker.md) | 1 | 288 | 1195 | opt-in manual call stack, captured at exception construction because GPlates catches at the top of main |
| [CommandLineParser](../src/utils/CommandLineParser.md) | 2 | 555 | 68 | Shared boost::program\_options wrapper for command-line, response-file and config-file parsing |
| [ComponentManager](../src/utils/ComponentManager.md) | 2 | 137 | 294 | Process-wide singleton bitset gating optional feature areas (Python, data mining, etc.) |
| [ConfigBundle](../src/utils/ConfigBundle.md) | 3 | 541 | 0 | Lightweight portable key-value configuration store with user and default values |
| [ConfigBundleUtils](../src/utils/ConfigBundleUtils.md) | 3 | 180 | 13 | Utility functions for manipulating hierarchical key names in configuration bundles |
| [ConfigInterface](../src/utils/ConfigInterface.md) | 2 | 303 | 27 | Abstract key/value config base shared by UserPreferences and ConfigBundle |
| [CopyConst](../src/utils/CopyConst.md) | 2 | 52 | 387 | Compile-time trait that transfers const-ness from one type onto another |
| [CopyOnWrite](../src/utils/CopyOnWrite.md) | 3 | 506 | 0 | Template wrapper providing copy-on-write semantics for smart pointers |
| [Counter64](../src/utils/Counter64.md) | 2 | 147 | 61 | Increment-only 64-bit counter used as a generation/change token |
| [DeferredCallEvent](../src/utils/DeferredCallEvent.md) | 2 | 405 | 63 | Posts callables from a worker thread to run on the Qt GUI thread |
| [Earth](../src/utils/Earth.md) | 2 | 85 | 30 | WGS-84 equatorial, polar and mean Earth radii in kilometres |
| [Endian](../src/utils/Endian.md) | 3 | 382 | 7 | Fast endianness conversion functions for basic types and sequences |
| [Environment](../src/utils/Environment.md) | 3 | 127 | 3 | Wrapper around std::getenv() returning QStrings with boolean interpretation |
| [FeatureUtils](../src/utils/FeatureUtils.md) | 2 | 410 | 48 | Free functions pulling plate ID, age and time-period values out of a feature |
| [FunctionTypes](../src/utils/FunctionTypes.md) | 2 | 511 | 34 | Hand-rolled Boost.FunctionTypes substitute extracting a callable's result and parameter types |
| [GeometryCreationUtils](../src/utils/GeometryCreationUtils.md) | 2 | 519 | 89 | Validated construction of GeometryOnSphere derivations from raw point sequences |
| [GetPropertyAsPythonObjVisitor](../src/utils/GetPropertyAsPythonObjVisitor.md) | 3 | 628 | 2 | Visitor that converts GPlates property values to Boost.Python objects |
| [HasFunction](../src/utils/HasFunction.md) | 3 | 114 | 1 | Compile-time meta-functions for detecting functions with specific signatures |
| [IdStringSet](../src/utils/IdStringSet.md) | 1 | 810 | 356 | reference-counted feature-ID pool where each string carries back-references to the objects it identifies |
| [IntrusiveSinglyLinkedList](../src/utils/IntrusiveSinglyLinkedList.md) | 2 | 348 | 336 | Zero-allocation singly-linked list where elements embed their own next-pointer |
| [KeyValueCache](../src/utils/KeyValueCache.md) | 2 | 429 | 47 | LRU cache that creates and owns a value object per key on first request |
| [LatLonAreaSampling](../src/utils/LatLonAreaSampling.md) | 2 | 839 | 6 | Downsamples points on the sphere to roughly one representative per lat/lon area bin |
| [Mapper](../src/utils/Mapper.md) | 3 | 122 | 6 | Abstract base class template defining interface for sequence transformation |
| [NetworkUtils](../src/utils/NetworkUtils.md) | 3 | 158 | 6 | Bidirectional conversion between QNetworkProxy objects and URL strings |
| [NullIntrusivePointerHandler](../src/utils/NullIntrusivePointerHandler.md) | 2 | 90 | 116 | Failure policy invoked when a non-nullable intrusive pointer would become null |
| [NullNonNullIntrusivePointerException](../src/utils/NullNonNullIntrusivePointerException.md) | 3 | 70 | 0 | Exception thrown when constructing a non-null intrusive pointer with NULL |
| [ObjectCache](../src/utils/ObjectCache.md) | 2 | 936 | 152 | Bounded, recyclable object pool supporting volatile (stealable) and non-volatile allocation |
| [ObjectPool](../src/utils/ObjectPool.md) | 1 | 534 | 428 | boost::object\_pool wrapper adding O(1) individual release via slot reuse |
| [OverloadResolution](../src/utils/OverloadResolution.md) | 2 | 382 | 87 | Template helpers to take a function pointer to one specific overload of a function |
| [Parse](../src/utils/Parse.md) | 2 | 350 | 36 | Extensible QString-to-value parsing via Parse\<T\> functor specializations |
| [Profile](../src/utils/Profile.md) | 1 | 2019 | 166 | GPlates' own call-graph CPU profiler, compiled in only under GPLATES\_PROFILE\_CODE |
| [QtFormattingUtils](../src/utils/QtFormattingUtils.md) | 3 | 77 | 1 | Formatting utilities for Qt types |
| [QtStreamable](../src/utils/QtStreamable.md) | 2 | 111 | 57 | CRTP mixin deriving QDebug/QTextStream operator\<\< from an existing ostream operator\<\< |
| [Reducer](../src/utils/Reducer.md) | 3 | 73 | 4 | Template base class for reduction operations over value ranges |
| [ReferenceCount](../src/utils/ReferenceCount.md) | 1 | 272 | 231 | the intrusive ownership base behind non\_null\_ptr\_type across the whole tree |
| [SafeBool](../src/utils/SafeBool.md) | 2 | 125 | 10 | Reusable safe-bool-idiom base preventing accidental bool-to-int misuse |
| [Select](../src/utils/Select.md) | 3 | 53 | 9 | Compile-time type selection via template specialization |
| [SetConst](../src/utils/SetConst.md) | 2 | 53 | 73 | Adds or strips top-level const on a type based on a compile-time bool |
| [Singleton](../src/utils/Singleton.md) | 2 | 341 | 75 | Policy-based CRTP singleton base with pluggable creation and lifetime policies |
| [SmartNodeLinkedList](../src/utils/SmartNodeLinkedList.md) | 1 | 405 | 886 | intrusive circular list whose nodes unlink themselves on destruction, chosen for its splice semantics |
| [SmartNodeLinkedList_test](../src/utils/SmartNodeLinkedList_test.md) | 3 | 203 | 0 | Tests for SmartNodeLinkedList template class |
| [StringFormattingUtils](../src/utils/StringFormattingUtils.md) | 2 | 255 | 74 | Fixed-width, fixed-precision number-to-string formatting for column-based export formats |
| [StringSet](../src/utils/StringSet.md) | 1 | 824 | 351 | reference-counted string interning pool giving O(1) identity comparison of repeated names |
| [StringUtils](../src/utils/StringUtils.md) | 3 | 144 | 7 | Utilities for converting between QString and std::wstring |
| [SubjectObserverToken](../src/utils/SubjectObserverToken.md) | 2 | 147 | 202 | Polling subject-observer pattern via a shared invalidation counter |
| [TypeTraits](../src/utils/TypeTraits.md) | 2 | 170 | 34 | Minimal compile-time traits for built-in, integral and floating-point types |
| [UnicodeString](../src/utils/UnicodeString.md) | 1 | 374 | 784 | thin QString wrapper mirroring the slice of ICU's UnicodeString the tree still calls |
| [UnicodeStringUtils](../src/utils/UnicodeStringUtils.md) | 2 | 94 | 289 | Conversions between ICU UnicodeString and Qt/std string types |
| [UniqueId](../src/utils/UniqueId.md) | 3 | 110 | 3 | Generation of globally unique XML-ID-compliant string identifiers |
| [VirtualProxy](../src/utils/VirtualProxy.md) | 3 | 81 | 0 | Defers creation of a pointee object until first dereference via pointer-like interface |
| [XPath](../src/utils/XPath.md) | 3 | 623 | 0 | Tokenizer for breaking XPath expressions into individual tokens |
| [XQueryUtils](../src/utils/XQueryUtils.md) | 2 | 547 | 102 | QXmlQuery-based XQuery evaluation helpers for GeoSciML/GML XML data |
| [XmlNamespaces](../src/utils/XmlNamespaces.md) | 2 | 433 | 57 | Registry of GPlates' XML namespace URIs and their standard aliases |
| [non_null_intrusive_ptr](../src/utils/non_null_intrusive_ptr.md) | 1 | 305 | 1689 | the codebase's ownership primitive: a forked boost::intrusive\_ptr that can never be null |

### `src/utils/deprecated`

| Unit | Tier | Lines | Fan-in | Description |
|---|---|---|---|---|
| [BinaryReducer](../src/utils/deprecated/BinaryReducer.md) | 3 | 82 | 0 | Deprecated reducer that applies a binary function to accumulate a sequence into a single result |
| [FeatureHandleToOldId](../src/utils/deprecated/FeatureHandleToOldId.md) | 3 | 142 | 0 | Deprecated utility for extracting legacy Plates format identifiers from features |
| [Filter](../src/utils/deprecated/Filter.md) | 3 | 155 | 0 | Abstract interface for filtering operations that transform input ranges to output ranges |
| [FilterMapOutputHandler](../src/utils/deprecated/FilterMapOutputHandler.md) | 3 | 109 | 8 | Abstracts output writing for filter/map operations, dispatching to iterator or container modes |
| [FilterMapReduceWorkFlow](../src/utils/deprecated/FilterMapReduceWorkFlow.md) | 3 | 152 | 1 | Orchestrates a pipeline of filter, map, and reduce operations using template metaprogramming |
| [GenericFilter](../src/utils/deprecated/GenericFilter.md) | 3 | 155 | 0 | Concrete filter implementation that wraps a user-supplied functor for filtering logic |
| [GenericMapper](../src/utils/deprecated/GenericMapper.md) | 3 | 154 | 0 | Concrete template mapper that applies user-provided implementation functors to transform input sequences |
| [GenericMapperImpl](../src/utils/deprecated/GenericMapperImpl.md) | 3 | 64 | 0 | Abstract interface for implementation functors used by GenericMapper |
| [GenericReducer](../src/utils/deprecated/GenericReducer.md) | 3 | 76 | 0 | Concrete template reducer that applies user-provided implementation functors to combine input sequences |
| [GenericReducerImpl](../src/utils/deprecated/GenericReducerImpl.md) | 3 | 55 | 0 | Abstract interface for implementation functors used by GenericReducer |
| [PredicateFilter](../src/utils/deprecated/PredicateFilter.md) | 3 | 176 | 0 | Concrete template filter that selects input elements matching a user-supplied boolean predicate |
| [UnaryMapper](../src/utils/deprecated/UnaryMapper.md) | 3 | 116 | 0 | Concrete template mapper that applies a unary transformation function to each input element |


## Other files

| File | Kind | Lines |
|---|---|---|
| `src/utils/CMakeLists.txt` | build | 93 |

## Depends on

| Component | References |
|---|---|
| [maths](maths.md) | 271 |
| [global](global.md) | 194 |
| [model](model.md) | 194 |
| [property-values](property-values.md) | 116 |
| [api](api.md) | 82 |
| [gui](gui.md) | 47 |
| [scribe](scribe.md) | 37 |
| [system-fixes](system-fixes.md) | 28 |
| [file-io](file-io.md) | 28 |
| [data-mining](data-mining.md) | 8 |
| [qt-widgets](qt-widgets.md) | 7 |
| [feature-visitors](feature-visitors.md) | 6 |
| [opengl](opengl.md) | 2 |
| [unit-test](unit-test.md) | 2 |

## Used by

| Component | References |
|---|---|
| [opengl](opengl.md) | 1679 |
| [file-io](file-io.md) | 1408 |
| [app-logic](app-logic.md) | 1374 |
| [scribe](scribe.md) | 770 |
| [model](model.md) | 715 |
| [gui](gui.md) | 617 |
| [qt-widgets](qt-widgets.md) | 578 |
| [maths](maths.md) | 523 |
| [property-values](property-values.md) | 383 |
| [api](api.md) | 333 |
| [presentation](presentation.md) | 238 |
| [unit-test](unit-test.md) | 181 |
| [entry-points](entry-points.md) | 178 |
| [view-operations](view-operations.md) | 131 |
| [global](global.md) | 122 |
| [feature-visitors](feature-visitors.md) | 74 |
| [data-mining](data-mining.md) | 34 |
| [canvas-tools](canvas-tools.md) | 21 |
| [cli](cli.md) | 6 |

## Explore

Run these from the `gplates-code` skill directory:

```bash
python scripts/gpq.py tree src/utils
python scripts/gpq.py sym . --mode sub --path src/utils --defs-only
```
