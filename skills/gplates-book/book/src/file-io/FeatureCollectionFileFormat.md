# FeatureCollectionFileFormat

[Book TOC](../../TOC.md) · [file-io](../../components/file-io.md) · cluster Community 9 · tier 2

| Source file | Kind | Lines |
|---|---|---|
| `src/file-io/FeatureCollectionFileFormat.h` | C++ | 59 |

## Overview

[[[PROSE overview unit=file-io/FeatureCollectionFileFormat tier=2]]]
Replace this whole block, markers included, with 1-3 paragraphs: what this unit is, why it exists, and how it fits the surrounding design. Do not restate the tables below.
[[[/PROSE]]]

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

[[[PROSE notes unit=file-io/FeatureCollectionFileFormat tier=2]]]
Replace this whole block, markers included, with invariants, ownership, threading or gotchas that are not visible in the tables. Write *None.* if there is nothing worth saying.
[[[/PROSE]]]

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
