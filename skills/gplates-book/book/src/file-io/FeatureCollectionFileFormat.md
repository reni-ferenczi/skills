# FeatureCollectionFileFormat

[Book TOC](../../TOC.md) · [file-io](../../components/file-io.md) · cluster Community 9 · tier 2

| Source file | Kind | Lines |
|---|---|---|
| `src/file-io/FeatureCollectionFileFormat.h` | C++ | 59 |

## Overview

This header contributes a single closed enumeration, `Format`, naming every
file format the application can read or write a feature collection as: the
native `GPML`/`GPMLZ` formats plus PLATES4 line and rotation files, GPlates
rotation files, shapefiles, OGR GMT, GeoJSON, GeoPackage, KML, a write-only
plain-XY GMT variant, VGP ("GMAP") and GSML. It is a leaf header with no
behaviour, used throughout `file-io` and beyond as the tag that identifies
which reader/writer implementation, file extension and
`FeatureCollectionFileFormatConfiguration` subtype apply to a given file.

## Declared types

| Name | Kind | Bases | Template | Subclasses | Description |
|---|---|---|---|---|---|
| [`GPlatesFileIO::FeatureCollectionFileFormat::Format`](#gplatesfileiofeaturecollectionfileformatformat) | enum | — | — | 0 | Formats of files that can contain feature collections. |

## Members

### `GPlatesFileIO::FeatureCollectionFileFormat::Format`

| Member | Kind | Type | Access | Description |
|---|---|---|---|---|
| `GPML` | enumerator | `None` | — | — |
| `GPMLZ` | enumerator | `None` | — | — |
| `PLATES4_LINE` | enumerator | `None` | — | — |
| `GPLATES_ROTATION` | enumerator | `None` | — | — |
| `PLATES4_ROTATION` | enumerator | `None` | — | — |
| `SHAPEFILE` | enumerator | `None` | — | — |
| `OGRGMT` | enumerator | `None` | — | — |
| `GEOJSON` | enumerator | `None` | — | — |
| `GEOPACKAGE` | enumerator | `None` | — | — |
| `KML` | enumerator | `None` | — | — |
| `WRITE_ONLY_XY_GMT` | enumerator | `None` | — | — |
| `GMAP` | enumerator | `None` | — | — |
| `GSML` | enumerator | `None` | — | — |
| `NUM_FORMATS` | enumerator | `None` | — | NOTE: This must be last and must be the actual number of formats (ie, no gaps in enum values). |

## Free functions and macros

| Name | Kind | Type / body | Description |
|---|---|---|---|
| `GPLATES_FILEIO_FEATURECOLLECTIONFILEFORMAT_H` | macro | `None` | — |

## Notes

`NUM_FORMATS` must stay last and the enumerators before it must not skip a
value, since it is used elsewhere as the count of formats (e.g. to size an
array indexed by `Format`); inserting a new format requires adding it before
`NUM_FORMATS`, not after.

## Used by

| Unit | Component | References |
|---|---|---|
| [cli/CliFeatureCollectionFileIO](../cli/CliFeatureCollectionFileIO.md) | cli | 90 |
| [file-io/FeatureCollectionFileFormatRegistry](FeatureCollectionFileFormatRegistry.md) | file-io | 64 |
| [file-io/OgrFeatureCollectionWriter](OgrFeatureCollectionWriter.md) | file-io | 31 |
| [file-io/ResolvedTopologicalGeometryExport](ResolvedTopologicalGeometryExport.md) | file-io | 26 |
| [file-io/ReconstructedFeatureGeometryExport](ReconstructedFeatureGeometryExport.md) | file-io | 25 |
| [file-io/ReconstructedFlowlineExport](ReconstructedFlowlineExport.md) | file-io | 25 |
| [file-io/ReconstructedMotionPathExport](ReconstructedMotionPathExport.md) | file-io | 25 |
| [view-operations/VisibleReconstructionGeometryExport](../view-operations/VisibleReconstructionGeometryExport.md) | view-operations | 20 |
| [qt-widgets/GMTFileFormatConfigurationDialog](../qt-widgets/GMTFileFormatConfigurationDialog.md) | qt-widgets | 18 |
| [qt-widgets/ManageFeatureCollectionsDialog](../qt-widgets/ManageFeatureCollectionsDialog.md) | qt-widgets | 11 |
| [gui/FileIOFeedback](../gui/FileIOFeedback.md) | gui | 10 |
| [file-io/OgrReader](OgrReader.md) | file-io | 9 |
| [file-io/PlatesRotationFileProxy](PlatesRotationFileProxy.md) | file-io | 8 |
| [cli/CliReconstructCommand](../cli/CliReconstructCommand.md) | cli | 7 |
| [file-io/File](File.md) | file-io | 7 |
| [unit-test/GenerateVelocityDomainCitcomsTest](../unit-test/GenerateVelocityDomainCitcomsTest.md) | unit-test | 7 |
| [api/PyFunctions](../api/PyFunctions.md) | api | 6 |
| [gui/ExportAnimationRegistry](../gui/ExportAnimationRegistry.md) | gui | 6 |
| [file-io/GMTFormatWriter](GMTFormatWriter.md) | file-io | 5 |
| [qt-widgets/ManageFeatureCollectionsEditConfigurations](../qt-widgets/ManageFeatureCollectionsEditConfigurations.md) | qt-widgets | 5 |

*... and 24 more units.*

## Related

*None.*

## Explore

Run these from the `gplates-code` skill directory:

```bash
python scripts/gpq.py file src/file-io/FeatureCollectionFileFormat.h
python scripts/gpq.py def GPlatesFileIO::FeatureCollectionFileFormat::Format --body
python scripts/gpq.py uses Format --kind enum
```
