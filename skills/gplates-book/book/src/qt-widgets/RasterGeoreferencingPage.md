# RasterGeoreferencingPage

[Book TOC](../../TOC.md) · [qt-widgets](../../components/qt-widgets.md) · cluster Community 1503 · tier 3

| Source file | Kind | Lines |
|---|---|---|
| `src/qt-widgets/RasterGeoreferencingPage.h` | C++ | 68 |
| `src/qt-widgets/RasterGeoreferencingPage.cc` | C++ | 74 |
| `src/qt-widgets/RasterGeoreferencingPageUi.ui` | Qt form | 39 |

## Overview

[[[PROSE overview unit=qt-widgets/RasterGeoreferencingPage tier=3]]]
Replace this whole block, markers included, with 1-3 paragraphs: what this unit is, why it exists, and how it fits the surrounding design. Do not restate the tables below.
[[[/PROSE]]]

## Declared types

| Name | Kind | Bases | Template | Subclasses | Description |
|---|---|---|---|---|---|
| [`GPlatesQtWidgets::RasterGeoreferencingPage`](#gplatesqtwidgetsrastergeoreferencingpage) | class | `QWizardPage`<br>`Ui_RasterGeoreferencingPage` | — | 0 | — |

## Members

### `GPlatesQtWidgets::RasterGeoreferencingPage`

| Member | Kind | Type | Access | Description |
|---|---|---|---|---|
| `RasterGeoreferencingPage( GPlatesPropertyValues::Georeferencing::non_null_ptr_type &georeferencing, unsigned int &raster_width, unsigned int &raster_height, QWidget *parent_ = NULL)` | constructor | `None` | public | — |
| `initializePage()` | method | `void` | public | — |
| `d_georeferencing` | field | `GPlatesPropertyValues::Georeferencing::non_null_ptr_type` | private | — |
| `d_georeferencing_widget` | field | `EditAffineTransformGeoreferencingWidget` | private | — |
| `d_raster_width` | field | `unsigned int` | private | — |
| `d_raster_height` | field | `unsigned int` | private | — |
| `d_last_seen_raster_width` | field | `unsigned int` | private | — |
| `d_last_seen_raster_height` | field | `unsigned int` | private | — |

## Free functions and macros

| Name | Kind | Type / body | Description |
|---|---|---|---|
| `GPLATES_QTWIDGETS_RASTERGEOREFERENCINGPAGE_H` | macro | `None` | — |

## Notes

[[[PROSE notes unit=qt-widgets/RasterGeoreferencingPage tier=3]]]
Replace this whole block, markers included, with invariants, ownership, threading or gotchas that are not visible in the tables. Write *None.* if there is nothing worth saying.
[[[/PROSE]]]

## Used by

| Unit | Component | References |
|---|---|---|
| [qt-widgets/ImportRasterDialog](ImportRasterDialog.md) | qt-widgets | 2 |

## Related

**Qt Designer forms**

| Form class | Base widget | Title | Widgets |
|---|---|---|---|
| `RasterGeoreferencingPage` | `QWizardPage` | WizardPage | 2 |


## Explore

Run these from the `gplates-code` skill directory:

```bash
python scripts/gpq.py file src/qt-widgets/RasterGeoreferencingPage.h
python scripts/gpq.py def GPlatesQtWidgets::RasterGeoreferencingPage --body
python scripts/gpq.py uses RasterGeoreferencingPage --kind class
python scripts/gpq.py hier RasterGeoreferencingPage
```
