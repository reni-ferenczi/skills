# LogException

[Book TOC](../../TOC.md) · [global](../../components/global.md) · cluster Community 1531 · tier 2

| Source file | Kind | Lines |
|---|---|---|
| `src/global/LogException.h` | C++ | 117 |

## Overview

[[[PROSE overview unit=global/LogException tier=2]]]
Replace this whole block, markers included, with 1-3 paragraphs: what this unit is, why it exists, and how it fits the surrounding design. Do not restate the tables below.
[[[/PROSE]]]

## Declared types

| Name | Kind | Bases | Template | Subclasses | Description |
|---|---|---|---|---|---|
| [`GPlatesGlobal::LogException`](#gplatesgloballogexception) | class | [`Exception`](GPlatesException.md) | — | 0 | General exception type that accepts an exception message. |

## Members

### `GPlatesGlobal::LogException`

| Member | Kind | Type | Access | Description |
|---|---|---|---|---|
| `LogException( const GPlatesUtils::CallStack::Trace &exception_source, const char *message)` | constructor | `None` | public | — |
| `LogException( const GPlatesUtils::CallStack::Trace &exception_source, const std::string &message)` | constructor | `None` | public | — |
| `LogException( const GPlatesUtils::CallStack::Trace &exception_source, const QString &message)` | constructor | `None` | public | Note that the QString input message gets converted to a std::string so only standard ascii should be used. |
| `~LogException()` | destructor | `None` | public | — |
| `exception_name()` | method | `char` | protected | — |
| `write_message( std::ostream &os)` | method | `void` | protected | — |
| `d_message` | field | `QString` | private | — |

## Free functions and macros

| Name | Kind | Type / body | Description |
|---|---|---|---|
| `GPLATES_GLOBAL_LOGEXCEPTION_H` | macro | `None` | — |

## Notes

[[[PROSE notes unit=global/LogException tier=2]]]
Replace this whole block, markers included, with invariants, ownership, threading or gotchas that are not visible in the tables. Write *None.* if there is nothing worth saying.
[[[/PROSE]]]

## Used by

| Unit | Component | References |
|---|---|---|
| [file-io/CptReader](../file-io/CptReader.md) | file-io | 25 |
| [gui/ExportRasterAnimationStrategy](../gui/ExportRasterAnimationStrategy.md) | gui | 15 |
| [file-io/GdalRasterReader](../file-io/GdalRasterReader.md) | file-io | 11 |
| [file-io/PlatesRotationFileProxy](../file-io/PlatesRotationFileProxy.md) | file-io | 11 |
| [qt-widgets/TotalReconstructionSequencesDialog](../qt-widgets/TotalReconstructionSequencesDialog.md) | qt-widgets | 9 |
| [cli/CliStageRotationCommand](../cli/CliStageRotationCommand.md) | cli | 5 |
| [file-io/MipmappedRasterFormatWriter](../file-io/MipmappedRasterFormatWriter.md) | file-io | 5 |
| [model/GpgimVersion](../model/GpgimVersion.md) | model | 5 |
| [file-io/GsmlFeatureHandlers](../file-io/GsmlFeatureHandlers.md) | file-io | 4 |
| [data-mining/CoRegFilter](../data-mining/CoRegFilter.md) | data-mining | 3 |
| [data-mining/DataMiningUtils](../data-mining/DataMiningUtils.md) | data-mining | 3 |
| [file-io/GsmlPropertyHandlers](../file-io/GsmlPropertyHandlers.md) | file-io | 3 |
| [file-io/MultiPointVectorFieldExport](../file-io/MultiPointVectorFieldExport.md) | file-io | 3 |
| [file-io/ScalarField3DFileFormatReader](../file-io/ScalarField3DFileFormatReader.md) | file-io | 3 |
| [api/PythonExecutionThread](../api/PythonExecutionThread.md) | api | 2 |
| [cli/CliEquivalentTotalRotation](../cli/CliEquivalentTotalRotation.md) | cli | 2 |
| [cli/CliRelativeTotalRotation](../cli/CliRelativeTotalRotation.md) | cli | 2 |
| [data-mining/RegionOfInterestFilter](../data-mining/RegionOfInterestFilter.md) | data-mining | 2 |
| [file-io/RasterFileCacheFormatReader](../file-io/RasterFileCacheFormatReader.md) | file-io | 2 |
| [file-io/RgbaRasterReader](../file-io/RgbaRasterReader.md) | file-io | 2 |

*... and 10 more units.*

## Related

*None.*

## Explore

Run these from the `gplates-code` skill directory:

```bash
python scripts/gpq.py file src/global/LogException.h
python scripts/gpq.py def GPlatesGlobal::LogException --body
python scripts/gpq.py uses LogException --kind class
python scripts/gpq.py hier LogException
```
