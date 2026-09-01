# gui

[Book TOC](../TOC.md)

138 unit page(s), 260 source file(s) documented here, 1 further file(s) listed below.

## Overview

[[[PROSE component unit=component:gui tier=1]]]
Replace this whole block, markers included, with 2-4 paragraphs: what this component is responsible for, the load-bearing units and how it connects to neighbouring components. Do not restate the unit table.
[[[/PROSE]]]

## Units

### `src/gui`

#### Colour

| Unit | Tier | Lines | Fan-in | Description |
|---|---|---|---|---|
| [Colour](../src/gui/Colour.md) | 1 | 1272 | 4081 | (pending) |
| [ColourFilter](../src/gui/ColourFilter.md) | 3 | 60 | 7 | Abstract base class for colour transformation filters |
| [ColourNameSet](../src/gui/ColourNameSet.md) | 2 | 151 | 812 | Base class for static named colour tables such as GMT and HTML colour names |
| [ColourPalette](../src/gui/ColourPalette.md) | 1 | 117 | 643 | (pending) |
| [ColourPaletteAdapter](../src/gui/ColourPaletteAdapter.md) | 2 | 239 | 46 | Templated wrapper adapting a ColourPalette from one value type to another via a converter |
| [ColourPaletteRangeRemapper](../src/gui/ColourPaletteRangeRemapper.md) | 3 | 273 | 1 | Remaps the value ranges of colour palettes to new bounds |
| [ColourPaletteUtils](../src/gui/ColourPaletteUtils.md) | 2 | 345 | 20 | CPT loading and numeric-range extraction helpers built on ColourPalette and the CPT readers |
| [ColourPaletteVisitor](../src/gui/ColourPaletteVisitor.md) | 2 | 120 | 56 | Double-dispatch visitor interface over the fixed set of concrete ColourPalette kinds |
| [ColourProxy](../src/gui/ColourProxy.md) | 2 | 294 | 192 | Pimpl wrapper deferring a ReconstructionGeometry's colour lookup until paint time |
| [ColourRawRaster](../src/gui/ColourRawRaster.md) | 2 | 383 | 8 | Colours a numeric RawRaster into an Rgba8RawRaster using a ColourPalette |
| [ColourScaleGenerator](../src/gui/ColourScaleGenerator.md) | 2 | 911 | 10 | Renders a colour-scale legend pixmap and tick annotations from a RasterColourPalette |
| [ColourScheme](../src/gui/ColourScheme.md) | 2 | 93 | 331 | Abstract policy for assigning a Colour to a ReconstructionGeometry or FeatureHandle |
| [ColourSchemeContainer](../src/gui/ColourSchemeContainer.md) | 2 | 557 | 121 | Registry of loaded ColourScheme instances grouped into categories |
| [ColourSchemeDelegator](../src/gui/ColourSchemeDelegator.md) | 2 | 453 | 34 | Forwards colouring calls to the currently active ColourScheme, globally or per feature collection |
| [ColourSchemeInfo](../src/gui/ColourSchemeInfo.md) | 2 | 83 | 24 | Bundles a ColourScheme pointer with its UI descriptions and built-in flag |
| [ColourSpectrum](../src/gui/ColourSpectrum.md) | 2 | 162 | 22 | Linearly interpolates a Colour between two bounds for a scalar position |

#### Config

| Unit | Tier | Lines | Fan-in | Description |
|---|---|---|---|---|
| [ConfigGuiUtils](../src/gui/ConfigGuiUtils.md) | 2 | 627 | 114 | Adapters wiring Qt preference widgets to a ConfigInterface's key/value store |
| [ConfigModel](../src/gui/ConfigModel.md) | 2 | 537 | 13 | QAbstractTableModel exposing a ConfigInterface's keys/values to a QTableView |
| [ConfigValueDelegate](../src/gui/ConfigValueDelegate.md) | 3 | 249 | 2 | Qt delegate for editing configuration and preference values in tables |

#### Export

| Unit | Tier | Lines | Fan-in | Description |
|---|---|---|---|---|
| [ExportAnimationContext](../src/gui/ExportAnimationContext.md) | 1 | 473 | 401 | (pending) |
| [ExportAnimationRegistry](../src/gui/ExportAnimationRegistry.md) | 2 | 2226 | 32 | Type-erased factory table mapping ExportID to strategy/widget/validator callbacks |
| [ExportAnimationStrategy](../src/gui/ExportAnimationStrategy.md) | 1 | 315 | 484 | (pending) |
| [ExportAnimationType](../src/gui/ExportAnimationType.md) | 1 | 640 | 574 | (pending) |
| [ExportCitcomsResolvedTopologyAnimationStrategy](../src/gui/ExportCitcomsResolvedTopologyAnimationStrategy.md) | 2 | 474 | 113 | ExportAnimationStrategy writing resolved topological boundaries/networks for the CitcomS workflow |
| [ExportCoRegistrationAnimationStrategy](../src/gui/ExportCoRegistrationAnimationStrategy.md) | 3 | 297 | 3 | Strategy for exporting co-registration data during animation playback |
| [ExportDeformationAnimationStrategy](../src/gui/ExportDeformationAnimationStrategy.md) | 2 | 605 | 111 | ExportAnimationStrategy writing per-frame strain and strain-rate output for deformed geometries |
| [ExportFileNameTemplateValidationUtils](../src/gui/ExportFileNameTemplateValidationUtils.md) | 2 | 278 | 96 | Free functions validating export filename templates before an animation export runs |
| [ExportFlowlineAnimationStrategy](../src/gui/ExportFlowlineAnimationStrategy.md) | 2 | 394 | 32 | ExportAnimationStrategy writing flowline geometries per frame in GMT/shapefile/OGR-GMT/GeoJSON |
| [ExportImageAnimationStrategy](../src/gui/ExportImageAnimationStrategy.md) | 2 | 318 | 33 | ExportAnimationStrategy saving a screenshot of the globe/map view to an image file per frame |
| [ExportMotionPathAnimationStrategy](../src/gui/ExportMotionPathAnimationStrategy.md) | 2 | 395 | 32 | ExportAnimationStrategy writing motion path geometries per frame in GMT/shapefile/OGR-GMT/GeoJSON |
| [ExportNetRotationAnimationStrategy](../src/gui/ExportNetRotationAnimationStrategy.md) | 2 | 1179 | 26 | ExportAnimationStrategy computing and writing net rotation of the surface per frame plus a summary |
| [ExportOptionsUtils](../src/gui/ExportOptionsUtils.md) | 2 | 206 | 290 | Plain-data option structs shared by export strategies and their option widgets |
| [ExportRasterAnimationStrategy](../src/gui/ExportRasterAnimationStrategy.md) | 2 | 1665 | 73 | Renders and writes visible colour or numerical rasters to file per frame |
| [ExportReconstructedGeometryAnimationStrategy](../src/gui/ExportReconstructedGeometryAnimationStrategy.md) | 2 | 319 | 34 | Writes reconstructed feature geometries to Shapefile/OGR-GMT/GMT/GeoJSON per frame |
| [ExportResolvedTopologyAnimationStrategy](../src/gui/ExportResolvedTopologyAnimationStrategy.md) | 2 | 348 | 66 | Writes resolved topological lines, polygons and networks per frame |
| [ExportScalarCoverageAnimationStrategy](../src/gui/ExportScalarCoverageAnimationStrategy.md) | 2 | 575 | 79 | Writes reconstructed scalar coverages to GPML or GMT per frame |
| [ExportStageRotationAnimationStrategy](../src/gui/ExportStageRotationAnimationStrategy.md) | 2 | 462 | 56 | Writes finite stage rotations (t+delta\_t to t) per frame |
| [ExportSvgAnimationStrategy](../src/gui/ExportSvgAnimationStrategy.md) | 2 | 270 | 20 | Writes an SVG snapshot of the reconstructed geometry per frame |
| [ExportTotalRotationAnimationStrategy](../src/gui/ExportTotalRotationAnimationStrategy.md) | 2 | 365 | 42 | Writes finite total rotations (to present day) per frame |
| [ExportVelocityAnimationStrategy](../src/gui/ExportVelocityAnimationStrategy.md) | 2 | 761 | 273 | Export strategy writing plate velocity meshes in GPML, GMT, Terra text or CitcomS format |

#### Feature

| Unit | Tier | Lines | Fan-in | Description |
|---|---|---|---|---|
| [FeatureFocus](../src/gui/FeatureFocus.md) | 1 | 730 | 508 | (pending) |
| [FeatureInspectionCanvasToolWorkflow](../src/gui/FeatureInspectionCanvasToolWorkflow.md) | 3 | 760 | 1 | Manages a suite of canvas tools for inspecting and editing a focused feature's geometry |
| [FeaturePropertyTableModel](../src/gui/FeaturePropertyTableModel.md) | 2 | 728 | 92 | Qt table model showing a feature's top-level properties as name/value rows |
| [FeatureTableModel](../src/gui/FeatureTableModel.md) | 2 | 1296 | 50 | Qt table model behind the search-results/clicked-feature lists of reconstruction geometries |
| [FeatureTypeColourPalette](../src/gui/FeatureTypeColourPalette.md) | 3 | 274 | 0 | Maps feature types to colors using a hash-based palette with hardcoded overrides |

#### Globe

| Unit | Tier | Lines | Fan-in | Description |
|---|---|---|---|---|
| [Globe](../src/gui/Globe.md) | 2 | 856 | 231 | Draws the 3D globe: stars, sphere, grid and rendered geometries, and tracks its orientation |
| [GlobeCanvasTool](../src/gui/GlobeCanvasTool.md) | 1 | 766 | 468 | (pending) |
| [GlobeCanvasToolAdapter](../src/gui/GlobeCanvasToolAdapter.md) | 3 | 555 | 6 | Adapts GlobeCanvas mouse signals to the GlobeCanvasTool interface |
| [GlobeOrientation](../src/gui/GlobeOrientation.md) | 2 | 109 | 14 | Abstract handle-based interface for rotating and querying the globe's orientation |
| [GlobeRenderedGeometryCollectionPainter](../src/gui/GlobeRenderedGeometryCollectionPainter.md) | 2 | 551 | 8 | Visits a RenderedGeometryCollection and paints its layers onto the globe |
| [GlobeRenderedGeometryLayerPainter](../src/gui/GlobeRenderedGeometryLayerPainter.md) | 2 | 3494 | 13 | Visits and tessellates every RenderedGeometry kind into globe-surface or sub-surface primitives |
| [GlobeVisibilityTester](../src/gui/GlobeVisibilityTester.md) | 2 | 113 | 480 | Tests whether a point on the sphere lies on the globe's near or far side |

#### Map

| Unit | Tier | Lines | Fan-in | Description |
|---|---|---|---|---|
| [Map](../src/gui/Map.md) | 2 | 357 | 25 | Holds map view state and projection, and paints the map background, grid and rendered geometries |
| [MapBackground](../src/gui/MapBackground.md) | 2 | 448 | 14 | Draws the coloured map background as a cached mesh reprojected under the current MapProjection |
| [MapCanvasTool](../src/gui/MapCanvasTool.md) | 2 | 562 | 91 | Abstract State-pattern base for interactive tools on the map view, mirroring GlobeCanvasTool |
| [MapCanvasToolAdapter](../src/gui/MapCanvasToolAdapter.md) | 1 | 519 | 335 | (pending) |
| [MapGrid](../src/gui/MapGrid.md) | 3 | 498 | 1 | Renders latitude/longitude grid lines in the map view |
| [MapProjection](../src/gui/MapProjection.md) | 1 | 1260 | 227 | (pending) |
| [MapRenderedGeometryCollectionPainter](../src/gui/MapRenderedGeometryCollectionPainter.md) | 2 | 347 | 14 | Draws a RenderedGeometryCollection onto the map view, visiting layers in the configured order |
| [MapRenderedGeometryLayerPainter](../src/gui/MapRenderedGeometryLayerPainter.md) | 3 | 3540 | 1 | Visitor that renders geometries in a single map layer |
| [MapTransform](../src/gui/MapTransform.md) | 2 | 305 | 63 | Holds the map view's centre, rotation and forwarded zoom, emitting transform\_changed on any change |

#### Python

| Unit | Tier | Lines | Fan-in | Description |
|---|---|---|---|---|
| [PythonConfiguration](../src/gui/PythonConfiguration.md) | 2 | 437 | 219 | Named, typed configuration values shared between drawing-style Python scripts and Qt widgets |
| [PythonConsoleHistory](../src/gui/PythonConsoleHistory.md) | 3 | 219 | 5 | Manages command history for the Python console with bash-like navigation. |
| [PythonManager](../src/gui/PythonManager.md) | 1 | 1080 | 288 | (pending) |

#### Topology

| Unit | Tier | Lines | Fan-in | Description |
|---|---|---|---|---|
| [TopologyCanvasToolWorkflow](../src/gui/TopologyCanvasToolWorkflow.md) | 3 | 638 | 1 | Workflow for building and editing topological features with dynamic tool enable state. |
| [TopologySectionsContainer](../src/gui/TopologySectionsContainer.md) | 2 | 891 | 298 | GUI-agnostic ordered data model for the Topology Sections table with a movable insertion point |
| [TopologySectionsTable](../src/gui/TopologySectionsTable.md) | 3 | 1365 | 1 | Manages a QTableWidget for displaying topology sections during plate polygon construction |
| [TopologySectionsTableColumns](../src/gui/TopologySectionsTableColumns.md) | 2 | 917 | 51 | Column definitions (accessor/mutator/widget factory) for the Topology Sections table |
| [TopologyTools](../src/gui/TopologyTools.md) | 2 | 4707 | 19 | Controller behind the build/edit-topology canvas tools, assembling sections into a geometry |

#### Other

| Unit | Tier | Lines | Fan-in | Description |
|---|---|---|---|---|
| [AddClickedGeometriesToFeatureTable](../src/gui/AddClickedGeometriesToFeatureTable.md) | 2 | 358 | 111 | Turns a globe/map click into rows in the clicked feature table via proximity hit-testing |
| [AgeColourPalettes](../src/gui/AgeColourPalettes.md) | 1 | 379 | 431 | (pending) |
| [AnimationController](../src/gui/AnimationController.md) | 1 | 1227 | 430 | (pending) |
| [BuiltinColourPaletteType](../src/gui/BuiltinColourPaletteType.md) | 2 | 681 | 379 | Tagged union identifying a built-in age/topography/SCM/ColorBrewer palette and its parameters |
| [BuiltinColourPalettes](../src/gui/BuiltinColourPalettes.md) | 1 | 2331 | 424 | (pending) |
| [CanvasToolWorkflow](../src/gui/CanvasToolWorkflow.md) | 2 | 503 | 85 | Abstract base implementing the activate/deactivate state machine for a tab of canvas tools |
| [CanvasToolWorkflows](../src/gui/CanvasToolWorkflows.md) | 1 | 610 | 2722 | (pending) |
| [ChooseCanvasToolUndoCommand](../src/gui/ChooseCanvasToolUndoCommand.md) | 3 | 133 | 7 | Captures and restores the currently active canvas tool for undo/redo |
| [CommandServer](../src/gui/CommandServer.md) | 2 | 1038 | 41 | QTcpServer exposing an XML remote-control protocol for a running GPlates instance |
| [Completionist](../src/gui/Completionist.md) | 3 | 328 | 7 | Singleton that manages autocompletion for Qt line edits |
| [CptColourPalette](../src/gui/CptColourPalette.md) | 2 | 1198 | 117 | In-memory representation of GMT regular and categorical CPT colour palette files |
| [CsvExport](../src/gui/CsvExport.md) | 2 | 387 | 112 | Static helper for writing table widgets or row data to CSV files |
| [CustomCompleter](../src/gui/CustomCompleter.md) | 3 | 165 | 3 | QCompleter subclass customizing popup display and path handling for two-column models |
| [Dialogs](../src/gui/Dialogs.md) | 1 | 1523 | 212 | (pending) |
| [DigitisationCanvasToolWorkflow](../src/gui/DigitisationCanvasToolWorkflow.md) | 3 | 626 | 1 | Canvas tool workflow managing interactive geometry digitization on globe and map |
| [DockState](../src/gui/DockState.md) | 2 | 567 | 19 | Tracks and manipulates which dock widgets occupy which edges of the main window |
| [DrawStyleAdapters](../src/gui/DrawStyleAdapters.md) | 2 | 555 | 159 | StyleAdapter implementations bridging feature colouring to C++ and Python draw styles |
| [DrawStyleManager](../src/gui/DrawStyleManager.md) | 2 | 745 | 84 | Singleton registry, persistence and built-in presets for draw styles and categories |
| [EventBlackout](../src/gui/EventBlackout.md) | 2 | 276 | 14 | Application-wide input filter used to block GUI interaction during Python execution |
| [ExternalSyncController](../src/gui/ExternalSyncController.md) | 2 | 1164 | 78 | Synchronises time, camera and files with an external process over a stdio text protocol |
| [FeedbackOpenGLToQPainter](../src/gui/FeedbackOpenGLToQPainter.md) | 2 | 1162 | 295 | Captures OpenGL rendering into a QPainter for vector output devices |
| [FileIODirectoryConfigurations](../src/gui/FileIODirectoryConfigurations.md) | 2 | 242 | 52 | Picks the directory a file dialog should open in, from user preferences |
| [FileIOFeedback](../src/gui/FileIOFeedback.md) | 2 | 2222 | 105 | Wraps app-logic file load/save with dialogs, filters and error feedback |
| [FullScreenMode](../src/gui/FullScreenMode.md) | 3 | 408 | 10 | Manages toggling the main window to full-screen presentation mode |
| [GMTColourNames](../src/gui/GMTColourNames.md) | 3 | 746 | 3 | A singleton color palette containing GMT color names and their RGB values |
| [GPlatesQApplication](../src/gui/GPlatesQApplication.md) | 3 | 359 | 4 | Extends QApplication with exception handling for the Qt event loop |
| [GenericColourScheme](../src/gui/GenericColourScheme.md) | 2 | 237 | 22 | Template ColourScheme mapping an extracted property to a colour via a palette |
| [GeometryFocusHighlight](../src/gui/GeometryFocusHighlight.md) | 3 | 251 | 6 | Utility namespace for rendering focused feature geometries with visual highlighting |
| [GraticuleSettings](../src/gui/GraticuleSettings.md) | 2 | 234 | 30 | User-configurable spacing, colour and line width for the lat/lon graticule |
| [GuiDebug](../src/gui/GuiDebug.md) | 3 | 466 | 2 | Creates a debug menu with introspected debug slots for testing and runtime inspection |
| [GuiException](../src/gui/GuiException.md) | 3 | 49 | 6 | Marker exception class for GUI-related errors |
| [HTMLColourNames](../src/gui/HTMLColourNames.md) | 2 | 223 | 27 | Singleton table mapping standard HTML/CSS colour keywords to RGB values |
| [HellingerCanvasToolWorkflow](../src/gui/HellingerCanvasToolWorkflow.md) | 3 | 300 | 1 | Canvas tool workflow for pole fits by the Hellinger method |
| [ImportMenu](../src/gui/ImportMenu.md) | 3 | 237 | 8 | Manages the Import submenu in the File menu |
| [LayerPainter](../src/gui/LayerPainter.md) | 1 | 2243 | 325 | (pending) |
| [LogFilterModel](../src/gui/LogFilterModel.md) | 3 | 283 | 3 | Qt proxy model for filtering and coloring log entries |
| [Mipmapper](../src/gui/Mipmapper.md) | 2 | 1479 | 86 | Builds successive halved-resolution mipmap levels of a raster for cached-raster rendering |
| [OpaqueSphere](../src/gui/OpaqueSphere.md) | 3 | 504 | 1 | Renders the background sphere of the 3D globe view |
| [Palette](../src/gui/Palette.md) | 2 | 894 | 112 | Older colour-lookup hierarchy (categorical, ranged, single-colour, CPT-file) keyed by a variant Key |
| [PlateIdColourPalettes](../src/gui/PlateIdColourPalettes.md) | 3 | 270 | 5 | Color palette implementations for mapping plate IDs to colors |
| [PoleManipulationCanvasToolWorkflow](../src/gui/PoleManipulationCanvasToolWorkflow.md) | 3 | 483 | 1 | Workflow for manipulating rotation poles on globe and map views with three interactive tools. |
| [ProjectionException](../src/gui/ProjectionException.md) | 3 | 77 | 9 | Exception class for map projection errors. |
| [RasterColourPalette](../src/gui/RasterColourPalette.md) | 1 | 372 | 224 | (pending) |
| [RenderSettings](../src/gui/RenderSettings.md) | 2 | 163 | 105 | Per-geometry-kind visibility flags letting layer painters know what to draw without a Globe reference |
| [SceneLightingParameters](../src/gui/SceneLightingParameters.md) | 2 | 367 | 87 | Value object holding scene lighting config: enabled state, ambient level, globe/map light directions |
| [SessionMenu](../src/gui/SessionMenu.md) | 2 | 304 | 19 | Builds and maintains the recent-sessions submenu from SessionManagement's session list |
| [SimpleGlobeOrientation](../src/gui/SimpleGlobeOrientation.md) | 2 | 497 | 30 | Self-contained globe orientation driven by drag-handle re-orientation and keyboard camera nudges |
| [SingleColourScheme](../src/gui/SingleColourScheme.md) | 3 | 145 | 4 | Simple colour scheme that assigns a fixed colour to all reconstruction geometries. |
| [SmallCircleCanvasToolWorkflow](../src/gui/SmallCircleCanvasToolWorkflow.md) | 3 | 288 | 1 | Workflow for creating small circles (circles at fixed distance from a pole) on globe and map. |
| [SphericalGrid](../src/gui/SphericalGrid.md) | 2 | 523 | 12 | Renders and caches the compiled draw state for the globe's lat/lon graticule and circumference |
| [Stars](../src/gui/Stars.md) | 3 | 410 | 1 | Renders a random starfield background for the 3D globe view. |
| [Symbol](../src/gui/Symbol.md) | 2 | 230 | 188 | Value struct describing a feature's replacement symbol shape, size, fill, scale and rotation |
| [TextOverlay](../src/gui/TextOverlay.md) | 3 | 204 | 3 | Paints configurable text overlays on the globe and map with reconstruction time substitution. |
| [TextOverlaySettings](../src/gui/TextOverlaySettings.md) | 2 | 292 | 38 | Settings bag for the on-screen text overlay: template text, font, colour, anchor and offset |
| [TreeWidgetBuilder](../src/gui/TreeWidgetBuilder.md) | 2 | 1447 | 269 | Assembles a QTreeWidget hierarchy via item handles before attaching it to the real widget |
| [TrinketArea](../src/gui/TrinketArea.md) | 3 | 269 | 2 | Manages status bar icons indicating unsaved changes and file read errors |
| [UnsavedChangesTracker](../src/gui/UnsavedChangesTracker.md) | 2 | 691 | 30 | Watches loaded feature collections for unsaved changes and warns before closing/clearing/loading |
| [UtilitiesMenu](../src/gui/UtilitiesMenu.md) | 3 | 200 | 4 | Allows Python scripts to register and execute via the Utilities menu |
| [VelocityLegendOverlay](../src/gui/VelocityLegendOverlay.md) | 3 | 570 | 3 | Paints a scale arrow legend for velocity data on the globe or map |
| [VelocityLegendOverlaySettings](../src/gui/VelocityLegendOverlaySettings.md) | 2 | 428 | 57 | Value object holding the appearance and placement settings for the velocity-scale legend overlay |
| [ViewCanvasToolWorkflow](../src/gui/ViewCanvasToolWorkflow.md) | 3 | 343 | 1 | Workflow for view-manipulation canvas tools (drag, zoom, lighting) |
| [ViewportProjection](../src/gui/ViewportProjection.md) | 3 | 117 | 12 | Central hub for map projection state and change notifications |
| [ViewportZoom](../src/gui/ViewportZoom.md) | 2 | 290 | 66 | Shared model of the globe/map viewport's zoom, exposed as both a percent and a level |
| [VisualLayersListModel](../src/gui/VisualLayersListModel.md) | 2 | 440 | 29 | QAbstractListModel adapter over VisualLayersProxy for the visual layers list view, reorder via drag-drop |
| [VisualLayersProxy](../src/gui/VisualLayersProxy.md) | 2 | 488 | 37 | Wraps VisualLayers to present its back-to-front layer order as front-to-back for the UI |

### `src/gui/deprecated`

| Unit | Tier | Lines | Fan-in | Description |
|---|---|---|---|---|
| [FeatureWeakRefSequence](../src/gui/deprecated/FeatureWeakRefSequence.md) | 3 | 163 | 0 | Container of weak references to features, shared via intrusive pointer (deprecated) |
| [GLCanvas](../src/gui/deprecated/GLCanvas.md) | 3 | 959 | 10 | wxWidgets-based OpenGL canvas for 3D globe rendering (deprecated) |
| [GPlatesApp](../src/gui/deprecated/GPlatesApp.md) | 3 | 203 | 2 | wxApp subclass managing application initialization and the main window lifecycle |
| [MainWindow](../src/gui/deprecated/MainWindow.md) | 3 | 967 | 10 | Top-level frame window managing menus, toolbars, status bar, and the GL canvas for the GUI |


## Other files

| File | Kind | Lines |
|---|---|---|
| `src/gui/CMakeLists.txt` | build | 268 |

## Depends on

| Component | References |
|---|---|
| [app-logic](app-logic.md) | 2834 |
| [maths](maths.md) | 2136 |
| [opengl](opengl.md) | 1575 |
| [model](model.md) | 1265 |
| [global](global.md) | 978 |
| [file-io](file-io.md) | 828 |
| [qt-widgets](qt-widgets.md) | 779 |
| [view-operations](view-operations.md) | 622 |
| [utils](utils.md) | 617 |
| [property-values](property-values.md) | 586 |
| [presentation](presentation.md) | 566 |
| [canvas-tools](canvas-tools.md) | 544 |
| [scribe](scribe.md) | 395 |
| [api](api.md) | 155 |
| [feature-visitors](feature-visitors.md) | 138 |
| [deprecated](deprecated.md) | 64 |
| [data-mining](data-mining.md) | 20 |
| [unit-test](unit-test.md) | 12 |
| [system-fixes](system-fixes.md) | 4 |
| [cli](cli.md) | 4 |
| [entry-points](entry-points.md) | 2 |

## Used by

| Component | References |
|---|---|
| [qt-widgets](qt-widgets.md) | 7008 |
| [presentation](presentation.md) | 1315 |
| [opengl](opengl.md) | 969 |
| [canvas-tools](canvas-tools.md) | 799 |
| [view-operations](view-operations.md) | 721 |
| [file-io](file-io.md) | 483 |
| [feature-visitors](feature-visitors.md) | 239 |
| [unit-test](unit-test.md) | 175 |
| [api](api.md) | 157 |
| [app-logic](app-logic.md) | 150 |
| [property-values](property-values.md) | 105 |
| [entry-points](entry-points.md) | 49 |
| [utils](utils.md) | 47 |
| [maths](maths.md) | 34 |
| [data-mining](data-mining.md) | 19 |
| [deprecated](deprecated.md) | 18 |
| [model](model.md) | 13 |

## Explore

Run these from the `gplates-code` skill directory:

```bash
python scripts/gpq.py tree src/gui
python scripts/gpq.py sym . --mode sub --path src/gui --defs-only
```
