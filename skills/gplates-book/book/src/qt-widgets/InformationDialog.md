# InformationDialog

[Book TOC](../../TOC.md) · [qt-widgets](../../components/qt-widgets.md) · cluster Community 1718 · tier 2

| Source file | Kind | Lines |
|---|---|---|
| `src/qt-widgets/InformationDialog.h` | C++ | 57 |
| `src/qt-widgets/InformationDialog.cc` | C++ | 56 |
| `src/qt-widgets/InformationDialogUi.ui` | Qt form | 125 |

## Overview

[[[PROSE overview unit=qt-widgets/InformationDialog tier=2]]]
Replace this whole block, markers included, with 1-3 paragraphs: what this unit is, why it exists, and how it fits the surrounding design. Do not restate the tables below.
[[[/PROSE]]]

## Declared types

| Name | Kind | Bases | Template | Subclasses | Description |
|---|---|---|---|---|---|
| [`GPlatesQtWidgets::InformationDialog`](#gplatesqtwidgetsinformationdialog) | class | `QDialog`<br>`Ui_InformationDialog` | — | 0 | — |

## Members

### `GPlatesQtWidgets::InformationDialog`

| Member | Kind | Type | Access | Description |
|---|---|---|---|---|
| `InformationDialog( const QString &text_, const QString &title_, QWidget *parent_ = NULL)` | constructor | `None` | public | — |
| `set_text( const QString &text_)` | method | `void` | public | — |
| `set_title( const QString &title_)` | method | `void` | public | — |

## Free functions and macros

| Name | Kind | Type / body | Description |
|---|---|---|---|
| `GPLATES_QTWIDGETS_INFORMATIONDIALOG_H` | macro | `None` | — |

## Notes

[[[PROSE notes unit=qt-widgets/InformationDialog tier=2]]]
Replace this whole block, markers included, with invariants, ownership, threading or gotchas that are not visible in the tables. Write *None.* if there is nothing worth saying.
[[[/PROSE]]]

## Used by

| Unit | Component | References |
|---|---|---|
| [qt-widgets/SetTopologyReconstructionParametersDialog](SetTopologyReconstructionParametersDialog.md) | qt-widgets | 21 |
| [qt-widgets/TopologyNetworkResolverLayerOptionsWidget](TopologyNetworkResolverLayerOptionsWidget.md) | qt-widgets | 15 |
| [qt-widgets/AssignReconstructionPlateIdsDialog](AssignReconstructionPlateIdsDialog.md) | qt-widgets | 13 |
| [qt-widgets/VelocityFieldCalculatorLayerOptionsWidget](VelocityFieldCalculatorLayerOptionsWidget.md) | qt-widgets | 11 |
| [qt-widgets/RasterPropertiesDialog](RasterPropertiesDialog.md) | qt-widgets | 8 |
| [qt-widgets/GenerateDeformingMeshPointsDialog](GenerateDeformingMeshPointsDialog.md) | qt-widgets | 7 |
| [qt-widgets/GenerateVelocityDomainCitcomsDialog](GenerateVelocityDomainCitcomsDialog.md) | qt-widgets | 5 |
| [qt-widgets/GenerateVelocityDomainLatLonDialog](GenerateVelocityDomainLatLonDialog.md) | qt-widgets | 5 |
| [qt-widgets/GenerateVelocityDomainTerraDialog](GenerateVelocityDomainTerraDialog.md) | qt-widgets | 5 |
| [qt-widgets/EditAffineTransformGeoreferencingWidget](EditAffineTransformGeoreferencingWidget.md) | qt-widgets | 3 |
| [qt-widgets/EditTimePeriodWidget](EditTimePeriodWidget.md) | qt-widgets | 3 |
| [qt-widgets/ExportRasterOptionsWidget](ExportRasterOptionsWidget.md) | qt-widgets | 3 |
| [qt-widgets/ReconstructLayerOptionsWidget](ReconstructLayerOptionsWidget.md) | qt-widgets | 3 |
| [qt-widgets/ReconstructionLayerOptionsWidget](ReconstructionLayerOptionsWidget.md) | qt-widgets | 3 |
| [qt-widgets/ReadErrorAccumulationDialog](ReadErrorAccumulationDialog.md) | qt-widgets | 2 |
| [qt-widgets/ConfigureVelocityLegendOverlayDialog](ConfigureVelocityLegendOverlayDialog.md) | qt-widgets | 1 |
| [qt-widgets/CreateFeatureDialog](CreateFeatureDialog.md) | qt-widgets | 1 |
| [qt-widgets/DatelineWrapOptionsWidget](DatelineWrapOptionsWidget.md) | qt-widgets | 1 |
| [qt-widgets/ExportCoordinatesDialog](ExportCoordinatesDialog.md) | qt-widgets | 1 |
| [qt-widgets/ExportResolvedTopologyOptionsWidget](ExportResolvedTopologyOptionsWidget.md) | qt-widgets | 1 |

## Related

**Qt Designer forms**

| Form class | Base widget | Title | Widgets |
|---|---|---|---|
| `InformationDialog` | `QDialog` | Information | 3 |


## Explore

Run these from the `gplates-code` skill directory:

```bash
python scripts/gpq.py file src/qt-widgets/InformationDialog.h
python scripts/gpq.py def GPlatesQtWidgets::InformationDialog --body
python scripts/gpq.py uses InformationDialog --kind class
python scripts/gpq.py hier InformationDialog
```
