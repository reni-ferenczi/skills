# NetCDFWriter

[Book TOC](../../../TOC.md) · [file-io](../../../components/file-io.md) · cluster Community 1368 · tier 3 · **deprecated**

| Source file | Kind | Lines |
|---|---|---|
| `src/file-io/deprecated/NetCDFWriter.h` | C++ | 54 |
| `src/file-io/deprecated/NetCDFWriter.cc` | C++ | 172 |

## Overview

[[[PROSE overview unit=file-io/deprecated/NetCDFWriter tier=3]]]
Replace this whole block, markers included, with 1-3 paragraphs: what this unit is, why it exists, and how it fits the surrounding design. Do not restate the tables below.
[[[/PROSE]]]

## Declared types

| Name | Kind | Bases | Template | Subclasses | Description |
|---|---|---|---|---|---|
| [`GPlatesFileIO::NetCDFWriter`](#gplatesfileionetcdfwriter) | class | — | — | 0 | NetCDFWriter is responsible for outputting a GridData object, in the netCDF data format. |

## Members

### `GPlatesFileIO::NetCDFWriter`

| Member | Kind | Type | Access | Description |
|---|---|---|---|---|
| `Write(const std::string &filename, GPlatesGeo::GridData *grid, wxProgressDialog *dlg = 0)` | method | `bool` | public | Output a GridData object. |

## Free functions and macros

| Name | Kind | Type / body | Description |
|---|---|---|---|
| `llp(const GPlatesMaths::PointOnSphere &pos)` | function | `GPlatesMaths::LatLonPoint` | — |
| `_GPLATES_FILEIO_NETCDFWRITER_H_` | macro | `None` | — |

## Notes

[[[PROSE notes unit=file-io/deprecated/NetCDFWriter tier=3]]]
Replace this whole block, markers included, with invariants, ownership, threading or gotchas that are not visible in the tables. Write *None.* if there is nothing worth saying.
[[[/PROSE]]]

## Used by

| Unit | Component | References |
|---|---|---|
| [qt-widgets/TotalReconstructionPolesDialog](../../qt-widgets/TotalReconstructionPolesDialog.md) | qt-widgets | 4 |
| [app-logic/PlateVelocityUtils](../../app-logic/PlateVelocityUtils.md) | app-logic | 2 |
| [cli/CliEquivalentTotalRotation](../../cli/CliEquivalentTotalRotation.md) | cli | 2 |
| [cli/CliRelativeTotalRotation](../../cli/CliRelativeTotalRotation.md) | cli | 2 |
| [gui/ExportStageRotationAnimationStrategy](../../gui/ExportStageRotationAnimationStrategy.md) | gui | 2 |
| [gui/ExportTotalRotationAnimationStrategy](../../gui/ExportTotalRotationAnimationStrategy.md) | gui | 2 |
| [qt-widgets/ApplyReconstructionPoleAdjustmentDialog](../../qt-widgets/ApplyReconstructionPoleAdjustmentDialog.md) | qt-widgets | 2 |
| [qt-widgets/EditTotalReconstructionSequenceWidget](../../qt-widgets/EditTotalReconstructionSequenceWidget.md) | qt-widgets | 2 |
| [qt-widgets/TotalReconstructionSequencesDialog](../../qt-widgets/TotalReconstructionSequencesDialog.md) | qt-widgets | 2 |
| [qt-widgets/HellingerDialog](../../qt-widgets/HellingerDialog.md) | qt-widgets | 1 |
| [unit-test/FeatureHandleTest](../../unit-test/FeatureHandleTest.md) | unit-test | 1 |

## Related

*None.*

## Explore

Run these from the `gplates-code` skill directory:

```bash
python scripts/gpq.py file src/file-io/deprecated/NetCDFWriter.h
python scripts/gpq.py def GPlatesFileIO::NetCDFWriter --body
python scripts/gpq.py uses NetCDFWriter --kind class
python scripts/gpq.py hier NetCDFWriter
```
