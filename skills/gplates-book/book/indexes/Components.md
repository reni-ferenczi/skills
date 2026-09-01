# Components

[Book TOC](../TOC.md)

27 components covering every file in the source tree. The tier column counts units at tier 1 / 2 / 3.

| Component | Units | Files | Tiers | Responsibility |
|---|---|---|---|---|
| [api](../components/api.md) | 23 | 36 | 1/8/14 | Embedded-Python bridge: GIL/thread dispatch and Boost.Python bindings for model and GUI |
| [app-logic](../components/app-logic.md) | 145 | 272 | 34/86/25 | the reconstruction engine: the layer graph, rotation trees and the geometry they produce |
| [build-and-docs](../components/build-and-docs.md) | 0 | 39 | 0/0/0 | CMake build, packaging and repository documentation for GPlates/pyGPlates |
| [canvas-tools](../components/canvas-tools.md) | 27 | 52 | 1/10/16 | mouse-driven globe/map tools for picking, digitising, editing, measuring and pole fitting |
| [cli](../components/cli.md) | 12 | 21 | 0/2/10 | Headless CLI for batch plate reconstruction, format conversion and rotation-pole queries |
| [data-mining](../components/data-mining.md) | 47 | 69 | 1/9/37 | Co-registration pipeline sampling target-layer attributes onto seed features |
| [deprecated](../components/deprecated.md) | 12 | 37 | 0/0/12 | legacy pre-Qt wxWidgets controls, kept for reference only |
| [entry-points](../components/entry-points.md) | 9 | 10 | 0/0/9 | Main() functions, Scribe export registration and precompiled headers for each binary |
| [feature-visitors](../components/feature-visitors.md) | 20 | 41 | 1/10/9 | feature-property visitors: find, classify, convert and write property values |
| [file-io](../components/file-io.md) | 137 | 250 | 11/60/66 | readers, writers and exporters for every GPlates file format, plus the raster disk caches |
| [global](../components/global.md) | 31 | 40 | 5/7/19 | exception hierarchy, assertions, and header utilities underpinning the whole codebase |
| [gui](../components/gui.md) | 138 | 261 | 17/79/42 | colouring, globe and map painting, canvas tool state, animation export and Python hosting |
| [maths](../components/maths.md) | 89 | 143 | 25/30/34 | Spherical geometry, rotation and spatial-indexing kernel every other component computes with |
| [model](../components/model.md) | 53 | 82 | 19/27/7 | revisioned feature store, its weak-reference notification machinery and the GPGIM schema |
| [opengl](../components/opengl.md) | 88 | 159 | 19/64/5 | the rendering backend: GL state funnel, resource wrappers and the cube-map raster pipeline |
| [presentation](../components/presentation.md) | 26 | 47 | 2/21/3 | display-state tier turning app-logic layer output into rendered geometry and saved sessions |
| [property-values](../components/property-values.md) | 68 | 126 | 5/45/18 | concrete PropertyValue classes for scalars, geometry, rotations, topology and rasters |
| [python-examples](../components/python-examples.md) | 1 | 33 | 0/0/1 | Standalone pygplates demo scripts and deprecated Orange co-registration widgets |
| [qt-resources](../components/qt-resources.md) | 1 | 191 | 0/1/0 | GPGIM schema, icons, colour palettes and default preferences compiled as Qt resources |
| [qt-widgets](../components/qt-widgets.md) | 239 | 632 | 4/60/175 | the whole Qt desktop UI: main window, globe/map canvases, task and layers panels, dialogs |
| [sample-data](../components/sample-data.md) | 0 | 186 | 0/0/0 | example GPML/rotation/CPT fixtures, some consumed as unit-test golden data |
| [scribe](../components/scribe.md) | 43 | 63 | 5/28/10 | hand-rolled serialisation framework for projects, sessions and undo state |
| [shaders](../components/shaders.md) | 10 | 38 | 0/10/0 | GLSL sources compiled by GL\* classes into the rendering pipeline's shader programs |
| [system-fixes](../components/system-fixes.md) | 3 | 4 | 0/1/2 | Vendored Boost and Loki compatibility headers underpinning utils and other components |
| [unit-test](../components/unit-test.md) | 36 | 72 | 0/4/32 | hand-rolled Boost.Test harness with its own suite-filtering framework |
| [utils](../components/utils.md) | 68 | 94 | 9/29/30 | ownership, interning, pooling and diagnostic primitives underlying the whole codebase |
| [view-operations](../components/view-operations.md) | 57 | 83 | 5/21/31 | Rendered-geometry scene graph and the mutable model behind geometry editing |
