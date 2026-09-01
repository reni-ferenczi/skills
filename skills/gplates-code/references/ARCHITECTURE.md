# GPlates source tree map

Orientation for the GPlates 2.5.0 source tree. Everything here was derived from the
indexed tree — verify any specific claim with `gpq` before relying on it, and prefer
the code's own Doxygen comments (`gpq def <Class> --body`) over this summary.

## Top level

| Path | What it is |
|---|---|
| `src/` | all C++ sources, ~2.4k files, ~23 MB |
| `cmake/modules/` | build machinery; `Version.cmake` holds the version numbers |
| `scripts/` | standalone Python scripts using the GPlates Python API |
| `sample-data/` | example `.gpml`, `.rot`, shapefile, colour palette and unit-test data |
| `doc/` | Doxygen config and figures |
| `CHANGELOG` | release-by-release feature and bug-fix history — searchable via `gpq grep --category doc` |
| `BUILD.Windows`, `DEPS.Windows` | how the project is actually built |

Entry points: `src/gplates_main.cc` (GUI), `src/gplates_demo_no_gui_main.cc`
(headless), `src/gplates_unit_test_main.cc` (tests). `src/CMakeLists.txt` lists
every source file and is the authoritative module inventory.

## Modules and namespaces

Each `src/<dir>` maps cleanly onto one `GPlates<Something>` namespace.

| Directory | Namespace | Responsibility | Representative classes |
|---|---|---|---|
| `app-logic` | `GPlatesAppLogic` | the reconstruction engine: layers, plate circuits, topologies | `ApplicationState`, `ReconstructGraph`, `ReconstructionTree`, `Reconstruction`, `LayerProxy`, `ReconstructContext`, `TopologyReconstruct` |
| `model` | `GPlatesModel` | the revisioned feature data model | `Model`, `ModelInterface`, `FeatureHandle`, `FeatureCollectionHandle`, `Gpgim`, `GpgimProperty`, `WeakReference` |
| `property-values` | `GPlatesPropertyValues` | concrete GPML/GML property value types | `GmlPoint`, `GmlTimePeriod`, `GpmlAge`, `GpmlFiniteRotation`, `GmlRectifiedGrid`, `Georeferencing` |
| `maths` | `GPlatesMaths` | spherical geometry and rotation maths | `PointOnSphere`, `PolylineOnSphere`, `PolygonOnSphere`, `GreatCircleArc`, `FiniteRotation`, `CubeQuadTreePartition` |
| `file-io` | `GPlatesFileIO` | readers and writers for every supported format | `GpmlReader`, `GpmlOutputVisitor`, `ShapefileXmlReader`, `GDALRasterReader`, `XmlWriter` |
| `feature-visitors` | `GPlatesFeatureVisitors` | visitors that walk features and property values | `GeometryFinder`, `GeometryTypeFinder`, `PropertyValueFinderBase`, `TopologySectionsFinder`, `ToQvariantConverter` |
| `presentation` | `GPlatesPresentation` | view state and visual layers, between app-logic and the GUI | `ViewState`, `VisualLayers`, `VisualLayer`, `ReconstructionGeometryRenderer`, `SessionManagement` |
| `view-operations` | `GPlatesViewOperations` | rendered-geometry model and geometry editing operations | `RenderedGeometryCollection`, `RenderedGeometryLayer`, `GeometryBuilder`, `MoveVertexGeometryOperation` |
| `canvas-tools` | `GPlatesCanvasTools` | the interactive tools on the globe and map | `CanvasTool`, `ClickGeometry`, `MeasureDistance`, `AdjustFittedPoleEstimate` |
| `gui` | `GPlatesGui` | non-widget GUI logic: colouring, painting, animation, topology editing | `AnimationController`, `TopologyTools`, `LayerPainter`, `ColourScheme`, `ColourPalette`, `GlobeCanvasTool` |
| `qt-widgets` | `GPlatesQtWidgets` | the Qt widgets and dialogs — the largest module (632 files) | `ViewportWindow`, plus one `*Dialog` / `*Widget` per `.ui` form |
| `opengl` | `GPlatesOpenGL` | the rendering backend | `GLRenderer`, `GLState`, `GLMultiResolutionRaster`, `GLScalarField3D`, `GLVisualLayers` |
| `qt-resources` | — | non-code resources compiled into the binary: GLSL shaders, GPGIM XML, Python scripts, icons |
| `data-mining` | `GPlatesDataMining` | co-registration and spatio-temporal data mining | `DataSelector`, `CoRegConfigurationTable`, `RegionOfInterestFilter` |
| `scribe` | `GPlatesScribe` | the serialisation framework behind projects and sessions | `Scribe`, `Transcription`, `ObjectTag` |
| `api` | `GPlatesApi` | Boost.Python bindings for the embedded Python console | `Feature`, `FeatureCollection`, `Application`, `Colour` |
| `utils` | `GPlatesUtils` | general-purpose infrastructure | `ObjectCache`, `ObjectPool`, `ReferenceCount`, `StringSet` |
| `global` | `GPlatesGlobal` | the exception hierarchy, assertions and version constants | `Exception`, `PreconditionViolationError`, `AssertionFailureException`, `NotYetImplementedException` |
| `cli` | `GPlatesCli` | command-line sub-commands for the headless build |
| `unit-test` | `GPlatesUnitTest` | Boost.Test suites |
| `deprecated` | — | code kept for reference; usually not what you want |

Get the current numbers any time with `gpq info`, and drill in with
`gpq tree src/<module>`.

## The concepts you need before reading code

**Feature / property model.** A `FeatureHandle` is a persistent handle to a
conceptual feature; its content lives in a succession of revisions, so the handle
survives edits. A feature carries an immutable feature type and feature ID plus a
list of top-level properties whose values are `property-values` types. Which
properties a given feature type may hold is not hard-coded — it is described by
the **GPGIM**.

**GPGIM.** The GPlates Geological Information Model, `src/qt-resources/gpgim/gpgim.xml`,
defines 109 feature classes (with inheritance) and 115 property definitions (with
value types and multiplicity). `GPlatesModel::Gpgim` loads it at startup and the
rest of the application validates against it. Query it with `gpq gpgim`.

**Reconstruction.** Rotation files define a plate circuit; a `ReconstructionTree`
is that hierarchy resolved at one instant in time, and a `Reconstruction` is the
accumulated output of all layers at that time.

**Layers and layer proxies.** `ReconstructGraph` manages layers, their connections
to feature collections and to each other. Each layer exposes a `LayerProxy`
subclass that computes output lazily, on request (a pull model) — see the comment
on `GPlatesAppLogic::LayerProxy`. `gpq hier LayerProxy` lists the subclasses; each
one is the entry point for a kind of layer (reconstruct, raster, topology, scalar
field, co-registration).

**Rendering path.** App-logic results are turned into `RenderedGeometry` objects
held in a `RenderedGeometryCollection` (`view-operations`), which the painters in
`gui` and `opengl` draw onto the globe or the map.

**State objects.** `ApplicationState` (app-logic) owns model-and-file state;
`ViewState` (presentation) owns everything about how it is displayed. Most GUI
classes are handed one or both. They are the hubs — `gpq includes
src/app-logic/ApplicationState.h --by` shows how widely.

## Qt specifics

- Dialogs come in pairs: a Designer form `src/qt-widgets/FooDialogUi.ui` (the
  layout) and `FooDialog.h/.cc` (the behaviour, inheriting the generated
  `Ui::FooDialog`). Start from the form when you know what the user saw on screen:
  `gpq ui "<label text>"`.
- Wiring is old-style `connect(sender, SIGNAL(...), receiver, SLOT(...))`, which the
  index captures — `gpq signals <name>`.
- `ViewportWindow` (`src/qt-widgets/ViewportWindow.h`) is the main window and the
  place most menu actions are connected.

## Rendering resources

`src/qt-resources/opengl/` holds the GLSL shaders, one directory per rendering
subsystem (`scalar_field_3d`, `multi_resolution_raster`, `layer_painter`,
`normal_map_source`, …). They are compiled into the binary via the `.qrc` files and
loaded by name from the matching `GL*` class in `src/opengl`. Search them with
`gpq grep <name> --category shader`.

## Python

Two different things share the name:

- **The embedded API** (`src/api/`, `GPlatesApi`) — Boost.Python bindings exposed to
  the Python console inside the GPlates application. `gpq pyapi` lists the whole
  surface. Example scripts ship in `src/qt-resources/python/scripts/`.
- **pyGPlates** — the standalone library, built from the `pygplates` branch of the
  GPlates repository. It is *not* in the GPlates 2.5.0 source archive, so the index
  cannot answer questions about it.

`scripts/*.py` at the top of the tree (`reconstruct.py`, `hellinger.py`,
`feature_collection_demo.py`) are worked examples of the API.

## Sample data

`sample-data/` is indexed as text (category `data`), so it doubles as a corpus of
real file-format examples: `gpml/` for the native XML format, `plates4-rotation-files/`
for `.rot`, `shapefiles/`, `cpt/` for colour palettes, `unit-test-data/` for the
Boost.Test fixtures. `gpq grep "<element>" --category data` shows how a construct
appears in a real file.
