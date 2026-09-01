# ScalarField3DGeoreferencingPage

[Book TOC](../../TOC.md) · [qt-widgets](../../components/qt-widgets.md) · cluster Community 1453 · tier 3

| Source file | Kind | Lines |
|---|---|---|
| `src/qt-widgets/ScalarField3DGeoreferencingPage.h` | C++ | 71 |
| `src/qt-widgets/ScalarField3DGeoreferencingPage.cc` | C++ | 79 |
| `src/qt-widgets/ScalarField3DGeoreferencingPageUi.ui` | Qt form | 39 |

## Overview

A wizard page in the scalar field 3D import dialog where users specify the geographic extent of the imported raster data via an `EditAffineTransformGeoreferencingWidget`. The page accepts latitude–longitude bounds or an affine transformation to define how raster pixels map to geographic coordinates. When the page is shown, it updates the widget if the raster dimensions have changed since initialization.

## Declared types

| Name | Kind | Bases | Template | Subclasses | Description |
|---|---|---|---|---|---|
| [`GPlatesQtWidgets::ScalarField3DGeoreferencingPage`](#gplatesqtwidgetsscalarfield3dgeoreferencingpage) | class | `QWizardPage`<br>`Ui_ScalarField3DGeoreferencingPage` | — | 0 | — |

## Members

### `GPlatesQtWidgets::ScalarField3DGeoreferencingPage`

| Member | Kind | Type | Access | Description |
|---|---|---|---|---|
| `ScalarField3DGeoreferencingPage( GPlatesPropertyValues::Georeferencing::non_null_ptr_type &georeferencing, unsigned int &raster_width, unsigned int &raster_height, ScalarField3DDepthLayersSequence &depth_layers_sequence, QWidget *parent_ = NULL)` | constructor | `None` | public | — |
| `initializePage()` | method | `void` | public | — |
| `d_georeferencing` | field | `GPlatesPropertyValues::Georeferencing::non_null_ptr_type` | private | — |
| `d_georeferencing_widget` | field | `EditAffineTransformGeoreferencingWidget` | private | — |
| `d_raster_width` | field | `unsigned int` | private | — |
| `d_raster_height` | field | `unsigned int` | private | — |
| `d_depth_layers_sequence` | field | `ScalarField3DDepthLayersSequence` | private | — |
| `d_last_seen_raster_width` | field | `unsigned int` | private | — |
| `d_last_seen_raster_height` | field | `unsigned int` | private | — |

## Free functions and macros

| Name | Kind | Type / body | Description |
|---|---|---|---|
| `GPLATES_QTWIDGETS_SCALARFIELD3DGEOREFERENCINGPAGE_H` | macro | `None` | — |

## Notes

*None.*

## Used by

| Unit | Component | References |
|---|---|---|
| [qt-widgets/ImportScalarField3DDialog](ImportScalarField3DDialog.md) | qt-widgets | 2 |

## Related

**Qt Designer forms**

| Form class | Base widget | Title | Widgets |
|---|---|---|---|
| `ScalarField3DGeoreferencingPage` | `QWizardPage` | WizardPage | 2 |


## Explore

Run these from the `gplates-code` skill directory:

```bash
python scripts/gpq.py file src/qt-widgets/ScalarField3DGeoreferencingPage.h
python scripts/gpq.py def GPlatesQtWidgets::ScalarField3DGeoreferencingPage --body
python scripts/gpq.py uses ScalarField3DGeoreferencingPage --kind class
python scripts/gpq.py hier ScalarField3DGeoreferencingPage
```
