# RasterFeatureCollectionPage

[Book TOC](../../TOC.md) · [qt-widgets](../../components/qt-widgets.md) · cluster Community 1800 · tier 3

| Source file | Kind | Lines |
|---|---|---|
| `src/qt-widgets/RasterFeatureCollectionPage.h` | C++ | 65 |
| `src/qt-widgets/RasterFeatureCollectionPage.cc` | C++ | 63 |
| `src/qt-widgets/RasterFeatureCollectionPageUi.ui` | Qt form | 61 |

## Overview

Wizard page for selecting a feature collection to hold the raster during import. It shows a list of existing feature collections and a checkbox to control whether the collection should be saved after import. The checkbox state is synchronized with a boolean reference passed at construction.

## Declared types

| Name | Kind | Bases | Template | Subclasses | Description |
|---|---|---|---|---|---|
| [`GPlatesQtWidgets::RasterFeatureCollectionPage`](#gplatesqtwidgetsrasterfeaturecollectionpage) | class | `QWizardPage`<br>`Ui_RasterFeatureCollectionPage` | — | 0 | — |

## Members

### `GPlatesQtWidgets::RasterFeatureCollectionPage`

| Member | Kind | Type | Access | Description |
|---|---|---|---|---|
| `RasterFeatureCollectionPage( bool &save_after_finish, QWidget *parent_ = NULL)` | constructor | `None` | public | — |
| `isComplete()` | method | `bool` | public | — |
| `handle_save_checkbox_state_changed( int state)` | method | `void` | private | — |
| `d_save_after_finish` | field | `bool` | private | — |

## Free functions and macros

| Name | Kind | Type / body | Description |
|---|---|---|---|
| `GPLATES_QTWIDGETS_RASTERFEATURECOLLECTIONPAGE_H` | macro | `None` | — |

## Notes

The `d_save_after_finish` boolean is held by reference; changes persist to the caller's variable. This page always returns `isComplete() == true`.

## Used by

| Unit | Component | References |
|---|---|---|
| [qt-widgets/ImportRasterDialog](ImportRasterDialog.md) | qt-widgets | 2 |

## Related

**Qt Designer forms**

| Form class | Base widget | Title | Widgets |
|---|---|---|---|
| `RasterFeatureCollectionPage` | `QWizardPage` | WizardPage | 5 |

**Qt signal/slot connections** (1 in this unit)

| Sender | Signal | Receiver | Slot |
|---|---|---|---|
| `save_checkbox` | `stateChanged(int)` | `this` | `handle_save_checkbox_state_changed(int)` |


## Explore

Run these from the `gplates-code` skill directory:

```bash
python scripts/gpq.py file src/qt-widgets/RasterFeatureCollectionPage.h
python scripts/gpq.py def GPlatesQtWidgets::RasterFeatureCollectionPage --body
python scripts/gpq.py uses RasterFeatureCollectionPage --kind class
python scripts/gpq.py hier RasterFeatureCollectionPage
```
