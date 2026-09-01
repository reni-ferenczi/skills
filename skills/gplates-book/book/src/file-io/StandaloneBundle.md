# StandaloneBundle

[Book TOC](../../TOC.md) · [file-io](../../components/file-io.md) · cluster Community 1482 · tier 3

| Source file | Kind | Lines |
|---|---|---|
| `src/file-io/StandaloneBundle.h` | C++ | 104 |
| `src/file-io/StandaloneBundle.cc` | C++ | 278 |

## Overview

Locates bundled resources in standalone distributions of GPlates and pyGPlates, where the binary and all dependencies (GDAL, PROJ, Python standard library) are packaged together. The namespace provides queries for PROJ data (`proj.db`), GDAL data and plugins, and Python standard library location, returning `boost::optional<QString>` to indicate whether resources were bundled.

On initialization, the module configures PROJ and GDAL to look for their data files in the bundle via environment variables and library-specific APIs. GPlates finds its bundle relative to the executable; pyGPlates must specify its import directory explicitly. All queries return `none` if the build was not configured for standalone deployment (`GPLATES_INSTALL_STANDALONE` undefined).

## Declared types

*None.*

## Members

*None.*

## Free functions and macros

| Name | Kind | Type / body | Description |
|---|---|---|---|
| `pygplates_bundle_directory` | variable | `boost::optional<QString>` | This should be initialised with 'initialise()' just after the non-embedded pygplates module was imported by an external (non-embedded Python interpreter). |
| `get_bundle_root_directory()` | function | `boost::optional<QString>` | — |
| `get_bundle_resources_directory()` | function | `boost::optional<QString>` | — |
| `get_bundle_resources_sub_directory( QString dir_relative_to_resources_dir)` | function | `boost::optional<QString>` | — |
| `initialise` | variable | `void` | — |
| `bundle_proj_data_directory` | variable | `boost::optional<QString>` | Let the PROJ and GDAL dependency libraries know where to find Proj resources files (eg, 'proj.db'). |
| `bundle_gdal_data_directory` | variable | `boost::optional<QString>` | Let the GDAL dependency library know where to find its resources files (eg, 'gcs.csv' for GDAL \< 2.5, which was moved into 'proj.db' for GDAL \>= 2.5, but there are other GDAL data files to bundle). |
| `bundle_gdal_plugins_directory` | variable | `boost::optional<QString>` | Let the GDAL dependency library know where to find its plugins (eg, 'gdal\_netCDF.{dll,dylib,so}'). |
| `GPLATES_FILEIO_STANDALONEBUNDLE_H` | macro | `None` | — |
| `initialise` | variable | `void` | Initialise so that queries on the standalone bundle can be made. |
| `get_proj_data_directory()` | function | `boost::optional<QString>` | Return the location of the Proj resource data in the standalone bundle. |
| `get_gdal_data_directory()` | function | `boost::optional<QString>` | Return the location of the GDAL resource data in the standalone bundle. |
| `get_gdal_plugins_directory()` | function | `boost::optional<QString>` | Return the location of the GDAL plugins in the standalone bundle. |
| `get_python_standard_library_directory()` | function | `boost::optional<QString>` | Return the location of the Python standard library in the standalone bundle. |

## Notes

All functions are compile-time conditionally defined: only included if `GPLATES_INSTALL_STANDALONE` is defined. The module is initialized once; for GPlates it uses `QCoreApplication::applicationDirPath()` (which requires Qt to be initialized first), while pyGPlates requires calling `initialise()` with its import directory after being imported. PROJ context paths are set with version-specific APIs to support both old and new PROJ versions. GDAL paths are set via `CPLSetConfigOption()` for data and plugins. On macOS, GPlates uses a different bundle structure (`gplates.app/Contents/`); Windows and Linux use the executable's parent directory.

## Used by

| Unit | Component | References |
|---|---|---|
| [entry-points/gplates_main](../entry-points/gplates_main.md) | entry-points | 3 |
| [gui/PythonManager](../gui/PythonManager.md) | gui | 3 |

## Related

*None.*

## Explore

Run these from the `gplates-code` skill directory:

```bash
python scripts/gpq.py file src/file-io/StandaloneBundle.h
```
