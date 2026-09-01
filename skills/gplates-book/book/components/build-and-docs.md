# build-and-docs

[Book TOC](../TOC.md)

CMake build system, packaging and repository documentation.

0 unit page(s), 0 source file(s) documented here, 39 further file(s) listed below.

## Overview

[[[PROSE component unit=component:build-and-docs tier=1]]]
Replace this whole block, markers included, with 2-4 paragraphs: what this component is responsible for, the load-bearing units and how it connects to neighbouring components. Do not restate the unit table.
[[[/PROSE]]]

## Units

*None.*

## Other files

| File | Kind | Lines |
|---|---|---|
| `AUTHORS` | doc | 31 |
| `BUILD.Linux` | build | 65 |
| `BUILD.OSX` | build | 88 |
| `BUILD.Windows` | build | 133 |
| `CHANGELOG` | doc | 1626 |
| `CMakeLists.txt` | build | 83 |
| `COPYING` | doc | 360 |
| `CREDITS` | doc | 528 |
| `DEPS.Linux` | build | 156 |
| `DEPS.OSX` | build | 131 |
| `DEPS.Windows` | build | 342 |
| `README.md` | doc | 121 |
| `cmake/add_sources.py` | Python | 129 |
| `cmake/distribution/MacOSXBundleInfo.plist.in` | build | 91 |
| `cmake/distribution/README` | doc | 34 |
| `cmake/distribution/gplates_desktop_icon.icns` | other | 0 |
| `cmake/distribution/gplates_desktop_icon.ico` | other | 0 |
| `cmake/distribution/gplates_desktop_icon.rc` | resource | 1 |
| `cmake/list_external_includes.py` | Python | 276 |
| `cmake/modules/ConfigDefault.cmake` | build | 304 |
| `cmake/modules/Config_h.cmake` | build | 86 |
| `cmake/modules/CustomBuildConfigs.cmake` | build | 128 |
| `cmake/modules/Doxygen.cmake` | build | 74 |
| `cmake/modules/FindDoxygen.cmake` | build | 108 |
| `cmake/modules/FindPROJ.cmake` | build | 200 |
| `cmake/modules/FindQwt.cmake` | build | 82 |
| `cmake/modules/FindZLIB.cmake` | build | 107 |
| `cmake/modules/Install.cmake` | build | 1449 |
| `cmake/modules/Package.cmake` | build | 593 |
| `cmake/modules/PackageGeneratorOverrides.cmake.in` | build | 69 |
| `cmake/modules/TestPythonEmbedding.cmake` | build | 138 |
| `cmake/modules/Utils.cmake` | build | 40 |
| `cmake/modules/Version.cmake` | build | 213 |
| `doc/CMakeLists.txt` | build | 16 |
| `doc/README.fig` | other | 0 |
| `doc/doxygen.conf.in` | build | 1099 |
| `doc/fig_grid.fig` | other | 0 |
| `doc/fig_small_circle.fig` | other | 0 |
| `doc/gplates.1.gz` | other | 0 |

## Depends on

*None.*

## Used by

*None.*

## Explore

Run these from the `gplates-code` skill directory:

```bash
python scripts/gpq.py tree AUTHORS
python scripts/gpq.py sym . --mode sub --path AUTHORS --defs-only
```
