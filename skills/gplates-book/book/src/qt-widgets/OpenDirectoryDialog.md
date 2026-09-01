# OpenDirectoryDialog

[Book TOC](../../TOC.md) · [qt-widgets](../../components/qt-widgets.md) · cluster Community 0 · tier 2

| Source file | Kind | Lines |
|---|---|---|
| `src/qt-widgets/OpenDirectoryDialog.h` | C++ | 71 |
| `src/qt-widgets/OpenDirectoryDialog.cc` | C++ | 59 |

## Overview

[[[PROSE overview unit=qt-widgets/OpenDirectoryDialog tier=2]]]
Replace this whole block, markers included, with 1-3 paragraphs: what this unit is, why it exists, and how it fits the surrounding design. Do not restate the tables below.
[[[/PROSE]]]

## Declared types

| Name | Kind | Bases | Template | Subclasses | Description |
|---|---|---|---|---|---|
| [`GPlatesQtWidgets::OpenDirectoryDialog`](#gplatesqtwidgetsopendirectorydialog) | class | — | — | 0 | — |

## Members

### `GPlatesQtWidgets::OpenDirectoryDialog`

| Member | Kind | Type | Access | Description |
|---|---|---|---|---|
| `OpenDirectoryDialog( QWidget *parent, const QString &caption, GPlatesPresentation::ViewState &view_state)` | constructor | `None` | public | — |
| `get_existing_directory()` | method | `QString` | public | — |
| `select_directory( const QString &directory)` | method | `void` | public | — |
| `d_parent` | field | `QWidget` | private | — |
| `d_caption` | field | `QString` | private | — |
| `d_last_open_directory` | field | `QString` | private | — |

## Free functions and macros

| Name | Kind | Type / body | Description |
|---|---|---|---|
| `GPLATES_QTWIDGETS_OPENDIRECTORYDIALOG_H` | macro | `None` | — |

## Notes

[[[PROSE notes unit=qt-widgets/OpenDirectoryDialog tier=2]]]
Replace this whole block, markers included, with invariants, ownership, threading or gotchas that are not visible in the tables. Write *None.* if there is nothing worth saying.
[[[/PROSE]]]

## Used by

| Unit | Component | References |
|---|---|---|
| [qt-widgets/ExportAnimationDialog](ExportAnimationDialog.md) | qt-widgets | 4 |
| [qt-widgets/GenerateVelocityDomainCitcomsDialog](GenerateVelocityDomainCitcomsDialog.md) | qt-widgets | 4 |
| [qt-widgets/GenerateVelocityDomainLatLonDialog](GenerateVelocityDomainLatLonDialog.md) | qt-widgets | 4 |
| [qt-widgets/GenerateVelocityDomainTerraDialog](GenerateVelocityDomainTerraDialog.md) | qt-widgets | 4 |
| [qt-widgets/HellingerDialog](HellingerDialog.md) | qt-widgets | 4 |
| [qt-widgets/ScalarField3DDepthLayersPage](ScalarField3DDepthLayersPage.md) | qt-widgets | 3 |
| [qt-widgets/TimeDependentRasterPage](TimeDependentRasterPage.md) | qt-widgets | 3 |
| [qt-widgets/CoRegistrationLayerConfigurationDialog](CoRegistrationLayerConfigurationDialog.md) | qt-widgets | 1 |

## Related

*None.*

## Explore

Run these from the `gplates-code` skill directory:

```bash
python scripts/gpq.py file src/qt-widgets/OpenDirectoryDialog.h
python scripts/gpq.py def GPlatesQtWidgets::OpenDirectoryDialog --body
python scripts/gpq.py uses OpenDirectoryDialog --kind class
python scripts/gpq.py hier OpenDirectoryDialog
```
