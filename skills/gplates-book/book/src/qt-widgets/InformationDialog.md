# InformationDialog

[Book TOC](../../TOC.md) · [qt-widgets](../../components/qt-widgets.md) · cluster Community 1718 · tier 2

| Source file | Kind | Lines |
|---|---|---|
| `src/qt-widgets/InformationDialog.h` | C++ | 57 |
| `src/qt-widgets/InformationDialog.cc` | C++ | 56 |
| `src/qt-widgets/InformationDialogUi.ui` | Qt form | 125 |

## Overview

`InformationDialog` is a minimal, reusable pop-up for showing a block of read-only text under a caller-supplied title — an "about this feature" or help note rather than a full-featured message box. It is built from the `InformationDialogUi.ui` form and simply forwards `set_text()`/`set_title()` calls to the generated `text_information` label and the window title, which is why its constructor also takes `text_` and `title_` directly. The window hints passed to `QDialog` (`CustomizeWindowHint | WindowTitleHint | WindowSystemMenuHint`) strip the dialog down to just a title bar and system menu, deliberately hiding the minimize/maximize/help buttons that a plain `QDialog` would otherwise get.

Its long "Used by" list across the qt-widgets component reflects that it is the standard, low-ceremony way many other dialogs and layer-options widgets show a short explanatory note to the user.

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

*None.*

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
