# Version

[Book TOC](../../TOC.md) · [global](../../components/global.md) · cluster Community 0 · tier 2

| Source file | Kind | Lines |
|---|---|---|
| `src/global/Version.h` | C++ | 135 |

## Overview

`Version` is a namespace of free functions exposing the build's version numbers to the rest of the application, split into two independent version streams: GPlates itself (`get_GPlates_version*`) and the `pyGPlates` Python bindings (`get_pyGPlates_version*`). Each stream reports major/minor/patch components plus an optional pre-release suffix, since the two components can ship different version numbers even from the same source tree.

The two streams also use different formatting conventions for the pre-release suffix: GPlates follows a Semantic-Versioning-like scheme (e.g. `"2.3.0-dev1"`, `"2.3.0-rc.1"`), while pyGPlates follows PEP 440 (e.g. `"1.0.0.dev1"`, `"1.0.0rc1"`). Callers needing a human-readable version string (about dialogs, log headers, command-line tools) use `get_GPlates_version()`; code needing to compare numerically uses the `_major`/`_minor`/`_patch` accessors.

## Declared types

*None.*

## Members

*None.*

## Free functions and macros

| Name | Kind | Type / body | Description |
|---|---|---|---|
| `GPLATES_GLOBAL_VERSION_H` | macro | `None` | — |
| `get_GPlates_version()` | function | `QString` | The MAJOR.MINOR.PATCH\[-PRERELEASE\] "human-readable" version of GPlates (very similar to Semantic Versioning https://semver.org/spec/v2.0.0.html). |
| `get_GPlates_version_major()` | function | `unsigned int` | The MAJOR version number of GPlates. |
| `get_GPlates_version_minor()` | function | `unsigned int` | The MINOR version number of GPlates. |
| `get_GPlates_version_patch()` | function | `unsigned int` | The PATCH version number of GPlates. |
| `get_GPlates_version_prerelease_suffix()` | function | `boost::optional<QString>` | The optional PRERELEASE "human-readable" version suffix of GPlates (very similar to Semantic Versioning https://semver.org/spec/v2.0.0.html). |
| `get_pyGPlates_version()` | function | `QString` | The MAJOR.MINOR.PATCH\[PRERELEASE\] version of pyGPlates formatted in the PEP440 versioning scheme (https://www.python.org/dev/peps/pep-0440/). |
| `get_pyGPlates_version_major()` | function | `unsigned int` | The MAJOR version number of pyGPlates. |
| `get_pyGPlates_version_minor()` | function | `unsigned int` | The MINOR version number of pyGPlates. |
| `get_pyGPlates_version_patch()` | function | `unsigned int` | The PATCH version number of pyGPlates. |
| `get_pyGPlates_version_prerelease_suffix()` | function | `boost::optional<QString>` | The optional PRERELEASE version suffix of pyGPlates formatted in the PEP440 versioning scheme (https://www.python.org/dev/peps/pep-0440/). |

## Notes

*None.*

## Used by

| Unit | Component | References |
|---|---|---|
| [file-io/LogToFileHandler](../file-io/LogToFileHandler.md) | file-io | 5 |
| [app-logic/LogModel](../app-logic/LogModel.md) | app-logic | 4 |
| [entry-points/gplates_unit_test_main](../entry-points/gplates_unit_test_main.md) | entry-points | 4 |
| [file-io/ShapefileXmlWriter](../file-io/ShapefileXmlWriter.md) | file-io | 4 |
| [app-logic/GPlatesQtMsgHandler](../app-logic/GPlatesQtMsgHandler.md) | app-logic | 3 |
| [app-logic/UserPreferences](../app-logic/UserPreferences.md) | app-logic | 3 |
| [entry-points/gplates_main](../entry-points/gplates_main.md) | entry-points | 3 |
| [gui/GPlatesQApplication](../gui/GPlatesQApplication.md) | gui | 3 |
| [qt-widgets/AboutDialog](../qt-widgets/AboutDialog.md) | qt-widgets | 3 |
| [qt-widgets/PythonConsoleDialog](../qt-widgets/PythonConsoleDialog.md) | qt-widgets | 3 |
| [qt-widgets/ViewportWindow](../qt-widgets/ViewportWindow.md) | qt-widgets | 3 |
| [utils/CommandLineParser](../utils/CommandLineParser.md) | utils | 1 |

## Related

*None.*

## Explore

Run these from the `gplates-code` skill directory:

```bash
python scripts/gpq.py file src/global/Version.h
```
