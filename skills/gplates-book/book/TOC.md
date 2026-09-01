# GPlates Developer's Reference

Generated from the `gplates-code` index of GPlates 2.5.0 (`C:\Dev\gplates_2.5.0_src`), indexed 2026-09-01T18:13:13.

## Overview

GPlates is an interactive plate-tectonic reconstruction application. It loads geological feature data and a set of rotation files and answers one question, over and over: given these features and these rotations, what geometry exists at this reconstruction time and where is it. Around that computation it wraps a globe and a map the user can drag, mouse tools for digitising and editing geometry, roughly a hundred and fifty dialogs, batch exporters, a headless command-line mode and an embedded Python interpreter. The same source tree builds more than one product — the `gplates` desktop application and the standalone `pygplates` Python extension module are configured from the same sources but never in one CMake configure, a branch owned by [build-and-docs](components/build-and-docs.md), while [entry-points](components/entry-points.md) holds each binary's `main()`, its precompiled header, and the `ScribeExport*` unit listing the polymorphic types that binary must register for saved projects to load.

Everything the application knows begins as a feature in [model](components/model.md), the revisioned feature store and the only place data is permitted to change. Its content is three handle levels — a `FeatureStoreRootHandle` of `FeatureCollectionHandle`s, roughly one per loaded file, each of `FeatureHandle`s, each of `TopLevelProperty` objects whose values are trees of `PropertyValue`. The idea the rest of GPlates is built around is that identity is separate from content: a handle keeps one address forever while an edit replaces the revision it points at, which is why a `WeakObserver` back-pointer or a `RevisionAwareIterator` reports itself invalid instead of dangling. The concrete leaves live next door in [property-values](components/property-values.md) — `GmlPoint`, `GpmlFiniteRotation`, `GpmlIrregularSampling`, `GpmlKeyValueDictionary`, `RawRaster` and the rest, plus `GeoTimeInstant`, the two-open-ended time scalar deliberately kept outside the `PropertyValue` hierarchy. Asking a feature a question means walking it with a visitor, which is what [feature-visitors](components/feature-visitors.md) is: a library of small `FeatureVisitor` subclasses, of which `PropertyValueFinder` — the generic, time-aware "give me this property as type T" lookup — is the one most callers actually use.

GPlates does not compile its schema in. The GPGIM document `gpgim.xml`, shipped as a Qt resource by [qt-resources](components/qt-resources.md), declares every feature type, which properties each may carry, what structural types their values may take and whether those values must be wrapped in a time-dependent wrapper; `GPlatesModel::Gpgim` parses it at startup. This is why `ModelUtils::add_property` and `FeatureHandle::add` are not interchangeable — the former consults the GPGIM and adds, strips or converts the `gpml:ConstantValue`, `gpml:PiecewiseAggregation` or `gpml:IrregularSampling` wrapper the definition demands, while the latter accepts anything. Getting data in and out of that store is [file-io](components/file-io.md): GPML (read through a chain of readers whose shape mirrors the GPGIM class hierarchy, with an uninterpreted head link so a load-and-save round trip loses nothing), PLATES4 line and rotation files, shapefiles and other OGR formats, rasters and their block-encoded sidecar caches, and at the far end of the pipeline the two dozen exporters that write reconstruction results back out. Two of its conventions travel everywhere: `ReadErrors`/`ReadErrorAccumulation`, because loading a geological file is expected to be partially successful, and `File`/`File::Reference`, the handle the rest of the application holds instead of a bare feature collection.

The reconstruction engine itself is [app-logic](components/app-logic.md), and it is a dataflow graph rather than a procedure. Rotation files arrive as `gpml:TotalReconstructionSequence` features and become a `ReconstructionGraph`, the time-independent in-memory form of a rotation model; resolving its crossover cycles for one time and one anchored plate yields a rooted acyclic `ReconstructionTree`, and because edge rotations are interpolated and memoised lazily, most consumers hold a copyable `ReconstructionTreeCreator` rather than a tree, so flowlines and motion paths can reach other times. On the feature side, one `ReconstructMethodInterface` per feature knows how that feature moves, `ReconstructContext` caches the expensive feature-to-method mapping and present-day geometries, and everything emitted is a `ReconstructionGeometry` — most often a `ReconstructedFeatureGeometry`, or a `MultiPointVectorField` of velocities, or a resolved topological line, boundary or network — stamped with a `ReconstructHandle` so a client can tell its own batch apart from every other layer's. Above that sits the graph: `ApplicationState` owns the reconstruction time and anchored plate ID and funnels every change into one `reconstruct()`, and `ReconstructGraph` owns the layers, input files and connections that `Layer` and `Layer::InputConnection` are weak handles onto. The single most important thing to internalise is that `reconstruct()` computes nothing — it returns a `Reconstruction` that is only a bag of `LayerProxy` pointers, and the work happens later and lazily, when a renderer, an exporter or a downstream layer pulls on a proxy.

Turning that pull-model output into pixels takes three components in sequence. [presentation](components/presentation.md) is the middle tier of the three-tier state stack (`ApplicationState`, then `ViewState`, then `ViewportWindow`, built in that order by `Application`): its `VisualLayers` mirrors `ReconstructGraph` one-to-one, each `VisualLayer` holds the display-only decisions app-logic has no business making in a `VisualLayerParams`, and `LayerOutputRenderer` plus `ReconstructionGeometryRenderer` convert whatever a proxy currently holds into `RenderedGeometry`. Those handles land in [view-operations](components/view-operations.md), whose `RenderedGeometryCollection` is the only channel connecting any producer of drawable output to the canvas — and which also owns `GeometryBuilder`, the mutable point sequence that digitising tools accumulate before an immutable `GeometryOnSphere` can exist, together with the undo machinery around it. [gui](components/gui.md) then walks that collection: it decides colour (with `ColourScheme` extracting a key from a geometry and `ColourPalette`, which never sees a geometry, mapping the key to a `Colour`), tessellates each `RenderedGeometry` into primitives, and batches them through `LayerPainter`, which draws nothing until `end_painting()` sorts everything into depth buckets. Underneath, [opengl](components/opengl.md) is the backend: `GLRenderer` is the single funnel through which all drawing passes, recording into a shadowed `GLState` so state reaches the driver only as a difference at a draw call, and the bulk of the component is the cube-quad-tree machinery that turns global rasters and 3-D scalar fields into cached tile hierarchies. The GLSL those classes compile at run time lives in [shaders](components/shaders.md), invisible to the dependency graph because it is loaded by resource path rather than `#include`.

Around that spine sit the parts a newcomer meets first and understands last. [qt-widgets](components/qt-widgets.md) is the whole desktop UI — `ViewportWindow`, `GlobeCanvas` and `MapView` behind `GlobeAndMapWidget`, the task and layers panels, and the dialogs — and despite its size computes almost nothing about plate motion; it names a value and hands it to the layer that does the work. [canvas-tools](components/canvas-tools.md) is the mouse layer beside it: one class per gesture, written against a view-agnostic `CanvasTool` base with globe and map adapters, driving state that `gui` and `view-operations` own. [scribe](components/scribe.md) is GPlates' own serialisation library, built rather than adopted, in which a client writes one `transcribe()` that serves both saving and loading; it is intrusive by design, which is why components that sit architecturally below it — `model`, `maths`, `property-values` — nonetheless include its headers, and why [presentation](components/presentation.md) can put a whole layer graph into a `.gproj` project. [api](components/api.md) hosts the CPython interpreter and the Boost.Python bindings, and is mostly threading plumbing: GIL guards, a dedicated `PythonExecutionThread`, and `run_in_main_thread` marshalling back onto the Qt GUI thread. [cli](components/cli.md) is the headless fork — `gplates_main` dispatches to a `CommandDispatcher` instead of starting the event loop — and [data-mining](components/data-mining.md) is the co-registration filter/map/reduce pipeline that samples target-layer attributes onto seed features.

Three components underlie all of the above and belong to none of it. [maths](components/maths.md) is the geometric kernel: `Real` with its epsilon comparison, `UnitVector3D` and `PointOnSphere`, the immutable reference-counted `GeometryOnSphere` hierarchy, `FiniteRotation` and `UnitQuaternion3D`, and the `AngularExtent`/`CubeQuadTreePartition` machinery that keeps spatial queries cheap. [utils](components/utils.md) supplies ownership and lifetime — `non_null_intrusive_ptr` and the `ReferenceCount` mixin nearly every long-lived object derives from — plus the `StringSet` interning pools behind every feature type and property name, the object pools and caches the OpenGL layer recycles through, and `SubjectObserverToken`, the polling invalidation counter the whole lazy pull model is built on. [global](components/global.md) owns only the exception hierarchy and `GPlatesAssert`, so that one top-level handler can report a failure identically no matter which component threw it; [system-fixes](components/system-fixes.md) is vendored Boost and Loki compatibility code beneath even that. The remaining components carry no pipeline code: [unit-test](components/unit-test.md) is the Boost.Test harness, [sample-data](components/sample-data.md) the fixtures it and the tutorials read by relative path, [python-examples](components/python-examples.md) standalone `pygplates` scripts, and [deprecated](components/deprecated.md) the pre-Qt wxWidgets control layer kept for reference only.

If you are new, read in the order the data flows rather than the order the directories sort. Start with [model](components/model.md) and [property-values](components/property-values.md), because every other component is ultimately talking about the objects they define; then [app-logic](components/app-logic.md), and within it `ApplicationState`, `ReconstructGraph` and `LayerProxy`, since the lazy pull model explains behaviour you will otherwise find inexplicable everywhere downstream; then [presentation](components/presentation.md) and [view-operations](components/view-operations.md), which are short and tell you how a computed result becomes something drawable. [maths](components/maths.md) and [utils](components/utils.md) are worth skimming before any of that, since their types appear in every signature you will read. Leave [opengl](components/opengl.md), [qt-widgets](components/qt-widgets.md) and [file-io](components/file-io.md) until you have a specific reason to open them — each is large, largely self-contained, and best entered from the one class you actually need.

## How to read this book

- Start here, pick a component, then a unit page; every unit page links back up to its component and to this table of contents.
- Use the indexes below when you already know a name.
- Every unit page ends with `gpq` commands that open the real source, so the book never has to be trusted over the code.
- Tier 1 pages cover the load-bearing engine units, tier 3 the boilerplate; the tier is shown in each page's breadcrumb.

## Components

| Component | Units | Files | Responsibility |
|---|---|---|---|
| [api](components/api.md) | 23 | 36 | Embedded-Python bridge: GIL/thread dispatch and Boost.Python bindings for model and GUI |
| [app-logic](components/app-logic.md) | 145 | 272 | the reconstruction engine: the layer graph, rotation trees and the geometry they produce |
| [build-and-docs](components/build-and-docs.md) | 0 | 39 | CMake build, packaging and repository documentation for GPlates/pyGPlates |
| [canvas-tools](components/canvas-tools.md) | 27 | 52 | mouse-driven globe/map tools for picking, digitising, editing, measuring and pole fitting |
| [cli](components/cli.md) | 12 | 21 | Headless CLI for batch plate reconstruction, format conversion and rotation-pole queries |
| [data-mining](components/data-mining.md) | 47 | 69 | Co-registration pipeline sampling target-layer attributes onto seed features |
| [deprecated](components/deprecated.md) | 12 | 37 | legacy pre-Qt wxWidgets controls, kept for reference only |
| [entry-points](components/entry-points.md) | 9 | 10 | Main() functions, Scribe export registration and precompiled headers for each binary |
| [feature-visitors](components/feature-visitors.md) | 20 | 41 | feature-property visitors: find, classify, convert and write property values |
| [file-io](components/file-io.md) | 137 | 250 | readers, writers and exporters for every GPlates file format, plus the raster disk caches |
| [global](components/global.md) | 31 | 40 | exception hierarchy, assertions, and header utilities underpinning the whole codebase |
| [gui](components/gui.md) | 138 | 261 | colouring, globe and map painting, canvas tool state, animation export and Python hosting |
| [maths](components/maths.md) | 89 | 143 | Spherical geometry, rotation and spatial-indexing kernel every other component computes with |
| [model](components/model.md) | 53 | 82 | revisioned feature store, its weak-reference notification machinery and the GPGIM schema |
| [opengl](components/opengl.md) | 88 | 159 | the rendering backend: GL state funnel, resource wrappers and the cube-map raster pipeline |
| [presentation](components/presentation.md) | 26 | 47 | display-state tier turning app-logic layer output into rendered geometry and saved sessions |
| [property-values](components/property-values.md) | 68 | 126 | concrete PropertyValue classes for scalars, geometry, rotations, topology and rasters |
| [python-examples](components/python-examples.md) | 1 | 33 | Standalone pygplates demo scripts and deprecated Orange co-registration widgets |
| [qt-resources](components/qt-resources.md) | 1 | 191 | GPGIM schema, icons, colour palettes and default preferences compiled as Qt resources |
| [qt-widgets](components/qt-widgets.md) | 239 | 632 | the whole Qt desktop UI: main window, globe/map canvases, task and layers panels, dialogs |
| [sample-data](components/sample-data.md) | 0 | 186 | example GPML/rotation/CPT fixtures, some consumed as unit-test golden data |
| [scribe](components/scribe.md) | 43 | 63 | hand-rolled serialisation framework for projects, sessions and undo state |
| [shaders](components/shaders.md) | 10 | 38 | GLSL sources compiled by GL\* classes into the rendering pipeline's shader programs |
| [system-fixes](components/system-fixes.md) | 3 | 4 | Vendored Boost and Loki compatibility headers underpinning utils and other components |
| [unit-test](components/unit-test.md) | 36 | 72 | hand-rolled Boost.Test harness with its own suite-filtering framework |
| [utils](components/utils.md) | 68 | 94 | ownership, interning, pooling and diagnostic primitives underlying the whole codebase |
| [view-operations](components/view-operations.md) | 57 | 83 | Rendered-geometry scene graph and the mutable model behind geometry editing |

## Indexes

| Index | Contents |
|---|---|
| [Components](indexes/Components.md) | every component, with its unit count |
| [Classes](indexes/Classes.md) | classes and unions |
| [Structs](indexes/Structs.md) | structs |
| [Enums](indexes/Enums.md) | enumerations |
| [Typedefs](indexes/Typedefs.md) | typedefs and type aliases |
| [Functions](indexes/Functions.md) | free functions at namespace scope |
| [Macros](indexes/Macros.md) | preprocessor macros, include guards last |

## Index facts

| Fact | Count |
|---|---|
| source files | 3081 |
| C++ files | 2368 |
| indexed lines | 843998 |
| entities | 121523 |
| identifier occurrences | 560598 |
| of them resolved | 514736 |
| resolved #include edges | 20515 |
| Qt Designer forms | 185 |
| signal/slot connections | 1656 |
| GPGIM feature types | 109 |
| GPGIM property types | 115 |

Unit pages: 1383. Component pages: 27.
