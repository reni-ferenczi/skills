# GMTFileFormatConfigurationDialog

[Book TOC](../../TOC.md) · [qt-widgets](../../components/qt-widgets.md) · cluster Community 1011 · tier 3

| Source file | Kind | Lines |
|---|---|---|
| `src/qt-widgets/GMTFileFormatConfigurationDialog.h` | C++ | 74 |
| `src/qt-widgets/GMTFileFormatConfigurationDialog.cc` | C++ | 81 |
| `src/qt-widgets/GMTFileFormatConfigurationDialogUi.ui` | Qt form | 87 |

## Overview

A configuration dialog for GMT file export. Users choose the header format style for `.xy` GMT files: PLATES4-style (standard format), verbose (feature properties), or prefer PLATES4 (with fallback). The dialog initializes radio buttons from the current `GMTConfiguration` and updates the configuration when the user clicks Finished.

## Declared types

| Name | Kind | Bases | Template | Subclasses | Description |
|---|---|---|---|---|---|
| [`GPlatesQtWidgets::GMTFileFormatConfigurationDialog`](#gplatesqtwidgetsgmtfileformatconfigurationdialog) | class | `QDialog`<br>`Ui_GMTFileFormatConfigurationDialog` | — | 0 | Dialog for configuring write-only ".xy" GMT file format. |

## Members

### `GPlatesQtWidgets::GMTFileFormatConfigurationDialog`

| Member | Kind | Type | Access | Description |
|---|---|---|---|---|
| `GMTFileFormatConfigurationDialog( const GPlatesFileIO::FeatureCollectionFileFormat::GMTConfiguration::shared_ptr_to_const_type & configuration, QWidget *parent_ = NULL)` | constructor | `None` | public | — |
| `get_configuration()` | method | `GPlatesFileIO::FeatureCollectionFileFormat::GMTConfiguration::shared_ptr_to_const_type` | public | Returns configuration selected by user after dialog closes. |
| `finished()` | method | `void` | public | — |
| `d_configuration` | field | `GPlatesFileIO::FeatureCollectionFileFormat::GMTConfiguration::shared_ptr_type` | private | — |

## Free functions and macros

| Name | Kind | Type / body | Description |
|---|---|---|---|
| `GPLATES_QTWIDGETS_GMTFILEFORMATCONFIGURATIONDIALOG_H` | macro | `None` | — |

## Notes

*None.*

## Used by

| Unit | Component | References |
|---|---|---|
| [qt-widgets/ManageFeatureCollectionsEditConfigurations](ManageFeatureCollectionsEditConfigurations.md) | qt-widgets | 3 |

## Related

**Qt Designer forms**

| Form class | Base widget | Title | Widgets |
|---|---|---|---|
| `GMTFileFormatConfigurationDialog` | `QDialog` | Edit GMT Configuration | 7 |

**Qt signal/slot connections** (1 in this unit)

| Sender | Signal | Receiver | Slot |
|---|---|---|---|
| `push_button_finished` | `clicked()` | `this` | `finished()` |


## Explore

Run these from the `gplates-code` skill directory:

```bash
python scripts/gpq.py file src/qt-widgets/GMTFileFormatConfigurationDialog.h
python scripts/gpq.py def GPlatesQtWidgets::GMTFileFormatConfigurationDialog --body
python scripts/gpq.py uses GMTFileFormatConfigurationDialog --kind class
python scripts/gpq.py hier GMTFileFormatConfigurationDialog
```
