# OpenDirectoryDialog

[Book TOC](../../TOC.md) · [qt-widgets](../../components/qt-widgets.md) · cluster Community 0 · tier 2

| Source file | Kind | Lines |
|---|---|---|
| `src/qt-widgets/OpenDirectoryDialog.h` | C++ | 71 |
| `src/qt-widgets/OpenDirectoryDialog.cc` | C++ | 59 |

## Overview

A thin wrapper around `QFileDialog::getExistingDirectory` that remembers the last directory the user picked. `d_last_open_directory` is bound by reference in the constructor to `GPlatesPresentation::ViewState::get_last_open_directory()`, so every dialog instance reads and writes the same view-state field rather than keeping its own state: opening the dialog seeds it with wherever the user last browsed to (in any directory dialog sharing that `ViewState`), and a successful pick writes the new path straight back through the reference.

It exists so the many "browse for a folder" actions scattered across the export and import dialogs (see Used by) do not each have to thread a "last directory" value through themselves — they just construct this with the shared `ViewState` and call `get_existing_directory()`.

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

`d_last_open_directory` is a `QString &`, not a `QString`: it aliases the `ViewState` instance passed to the constructor, so that `ViewState` must outlive the dialog. There is no default constructor and no way to construct one without a live `ViewState`.

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
