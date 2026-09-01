# GPlates Developer's Reference

Generated from the `gplates-code` index of GPlates 2.5.0 (`C:\Dev\gplates_2.5.0_src`), indexed 2026-09-01T18:13:13.

## Overview

[[[PROSE toc unit=book tier=1]]]
Replace this whole block, markers included, with the project overview: what GPlates is, and the path a change takes through model -> app-logic -> presentation -> view-operations/gui -> opengl. Aim for 4-8 paragraphs.
[[[/PROSE]]]

## How to read this book

- Start here, pick a component, then a unit page; every unit page links back up to its component and to this table of contents.
- Use the indexes below when you already know a name.
- Every unit page ends with `gpq` commands that open the real source, so the book never has to be trusted over the code.
- Tier 1 pages cover the load-bearing engine units, tier 3 the boilerplate; the tier is shown in each page's breadcrumb.

## Components

| Component | Units | Files | Responsibility |
|---|---|---|---|
| [api](components/api.md) | 23 | 36 | (pending) |
| [app-logic](components/app-logic.md) | 145 | 272 | (pending) |
| [build-and-docs](components/build-and-docs.md) | 0 | 39 | CMake build system, packaging and repository documentation. |
| [canvas-tools](components/canvas-tools.md) | 27 | 52 | (pending) |
| [cli](components/cli.md) | 12 | 21 | (pending) |
| [data-mining](components/data-mining.md) | 47 | 69 | (pending) |
| [deprecated](components/deprecated.md) | 12 | 37 | (pending) |
| [entry-points](components/entry-points.md) | 9 | 10 | The main() entry points and the Scribe export registration units. |
| [feature-visitors](components/feature-visitors.md) | 20 | 41 | (pending) |
| [file-io](components/file-io.md) | 137 | 250 | (pending) |
| [global](components/global.md) | 31 | 40 | (pending) |
| [gui](components/gui.md) | 138 | 261 | (pending) |
| [maths](components/maths.md) | 89 | 143 | (pending) |
| [model](components/model.md) | 53 | 82 | (pending) |
| [opengl](components/opengl.md) | 88 | 159 | (pending) |
| [presentation](components/presentation.md) | 26 | 47 | (pending) |
| [property-values](components/property-values.md) | 68 | 126 | (pending) |
| [python-examples](components/python-examples.md) | 1 | 33 | Stand-alone pyGPlates demo and utility scripts. |
| [qt-resources](components/qt-resources.md) | 1 | 191 | (pending) |
| [qt-widgets](components/qt-widgets.md) | 239 | 632 | (pending) |
| [sample-data](components/sample-data.md) | 0 | 186 | Example data files shipped with GPlates. |
| [scribe](components/scribe.md) | 43 | 63 | (pending) |
| [shaders](components/shaders.md) | 10 | 38 | GLSL shader programs compiled into the Qt resource bundle. |
| [system-fixes](components/system-fixes.md) | 3 | 4 | (pending) |
| [unit-test](components/unit-test.md) | 36 | 72 | (pending) |
| [utils](components/utils.md) | 68 | 94 | (pending) |
| [view-operations](components/view-operations.md) | 57 | 83 | (pending) |

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
