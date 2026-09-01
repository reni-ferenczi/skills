# build-and-docs

[Book TOC](../TOC.md)

CMake build system, packaging and repository documentation.

0 unit page(s), 0 source file(s) documented here, 39 further file(s) listed below.

## Overview

This component is the CMake build system that turns the `src/` tree into either
the `gplates` desktop application or the `pygplates` Python extension module,
plus the packaging and repository-level documentation built around that. The
root `CMakeLists.txt` is the entry point: it sets the minimum CMake version,
adds `cmake/modules` to `CMAKE_MODULE_PATH`, pulls in `Version.cmake` for the
project version, then branches on the `GPLATES_BUILD_GPLATES` option to
`project()` either `GPlates` or `PyGPlates` — the two are never built together
from one configure, because CPack's Debian packages cannot carry separate
versions per component. After including `ConfigDefault.cmake` (the project's
cache options) and `CustomBuildConfigs.cmake` (which layers `ProfileGprof` and
`ProfileGplates` on top of the stock Debug/Release/RelWithDebInfo/MinSizeRel
configurations), it descends into `src/`, whose own `CMakeLists.txt` calls
`find_package` for every third-party dependency — OpenGL, GLEW, ZLIB, CGAL,
Python, Boost, Qt5, Qwt, GDAL and PROJ — before looping over a
`source_sub_directories` list that enumerates, one `add_subdirectory` per
entry, every other component in this book (`app-logic`, `model`, `maths`,
`gui`, `qt-widgets`, `opengl`, `file-io`, and so on).

Among the `cmake/modules/` files, a handful carry real weight. `Version.cmake`
owns the GPlates and pyGPlates version numbers independently (pyGPlates
currently trails at 0.39.0 against GPlates 2.5.0) and encodes the pre-release
suffix rules needed to keep Semantic Versioning, Debian versioning and Python's
PEP 440 all ordering pre-releases consistently. `Config_h.cmake` feeds
`src/global/config.h.in`, so options set here — `GPLATES_PUBLIC_RELEASE`,
`GPLATES_PROFILE_CODE`, `GPLATES_INSTALL_STANDALONE` and the detected PROJ
header variant — surface as preprocessor macros read throughout the rest of
the source tree. `Install.cmake` (1449 lines) and `Package.cmake` (593 lines)
are the largest and do the most work: `GPLATES_INSTALL_STANDALONE`, on by
default for Windows and macOS but off for Linux, decides whether `install()`
copies Qt, GDAL, PROJ and the Python standard library into the install tree to
make a relocatable bundle, or leaves dependency resolution to the target
system's package manager; `Package.cmake` then picks CPack generators to match
— NSIS plus a no-admin-required ZIP on Windows, a drag-and-drop `.dmg` on
macOS, a `.deb` on Linux — and both files are guarded by the same
`GPLATES_BUILD_GPLATES` switch so the pyGPlates path installs into a
setuptools-ready staging directory instead. The three custom `Find*.cmake`
modules (`FindPROJ`, `FindQwt`, `FindZLIB`) exist because those libraries lack
adequate upstream CMake support — `FindZLIB` in particular locates the
Windows-contrib `zlibwapi` build that the stock module misses. `Doxygen.cmake`
and `doc/CMakeLists.txt` add a `doc` target that runs Doxygen (via
`doc/doxygen.conf.in`) over a fixed subset of source directories
(`feature-visitors`, `file-io`, `model`, `property-values`, `utils`), and
`TestPythonEmbedding.cmake` compiles and runs a throwaway Boost.Python program
during configuration to catch a mismatched Python/Boost.Python ABI before the
real build starts.

`BUILD.Windows` and `DEPS.Windows` describe the manual half of this system: no
Windows package manager is assumed, so each dependency (Qt, Qwt, GLEW, Python,
Boost, SQLite3, PROJ, NetCDF, GDAL, CGAL, zlib) is built or installed by hand
into locations added to `CMAKE_PREFIX_PATH` and `PATH`, then CMake's
`cmake-gui` generates a Visual Studio solution that a developer builds and
installs (`cmake --install`) exactly as `Install.cmake` and `Package.cmake`
describe for the standalone case. The `AUTHORS`, `CHANGELOG`, `COPYING`,
`CREDITS` and `README.md` files at the repository root, together with the
Linux and macOS counterparts of the BUILD/DEPS notes, round out the
repository-level documentation this component owns.

Because it configures and packages everything else rather than being
reconstruction-pipeline code itself, this component has no measured
dependency edges to or from the other components: the `## Depends on` and
`## Used by` tables are empty by construction. Its real relationship to the
rest of the codebase is structural rather than a call graph — the
`source_sub_directories` list in `src/CMakeLists.txt` is the authoritative
enumeration of which top-level directories exist, and the macros generated
from `Config_h.cmake` into `global/config.h` are consulted by code across many
of those directories at compile time.

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
