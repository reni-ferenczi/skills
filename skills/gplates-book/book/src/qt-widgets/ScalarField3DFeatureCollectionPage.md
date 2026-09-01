# ScalarField3DFeatureCollectionPage

[Book TOC](../../TOC.md) · [qt-widgets](../../components/qt-widgets.md) · cluster Community 1803 · tier 3

| Source file | Kind | Lines |
|---|---|---|
| `src/qt-widgets/ScalarField3DFeatureCollectionPage.h` | C++ | 65 |
| `src/qt-widgets/ScalarField3DFeatureCollectionPage.cc` | C++ | 63 |
| `src/qt-widgets/ScalarField3DFeatureCollectionPageUi.ui` | Qt form | 51 |

## Overview

[[[PROSE overview unit=qt-widgets/ScalarField3DFeatureCollectionPage tier=3]]]
Replace this whole block, markers included, with 1-3 paragraphs: what this unit is, why it exists, and how it fits the surrounding design. Do not restate the tables below.
[[[/PROSE]]]

## Declared types

| Name | Kind | Bases | Template | Subclasses | Description |
|---|---|---|---|---|---|
| [`GPlatesQtWidgets::ScalarField3DFeatureCollectionPage`](#gplatesqtwidgetsscalarfield3dfeaturecollectionpage) | class | `QWizardPage`<br>`Ui_ScalarField3DFeatureCollectionPage` | — | 0 | — |

## Members

### `GPlatesQtWidgets::ScalarField3DFeatureCollectionPage`

| Member | Kind | Type | Access | Description |
|---|---|---|---|---|
| `ScalarField3DFeatureCollectionPage( bool &save_after_finish, QWidget *parent_ = NULL)` | constructor | `None` | public | — |
| `isComplete()` | method | `bool` | public | — |
| `handle_save_checkbox_state_changed( int state)` | method | `void` | private | — |
| `d_save_after_finish` | field | `bool` | private | — |

## Free functions and macros

| Name | Kind | Type / body | Description |
|---|---|---|---|
| `GPLATES_QTWIDGETS_SCALARFIELD3DFEATURECOLLECTIONPAGE_H` | macro | `None` | — |

## Notes

[[[PROSE notes unit=qt-widgets/ScalarField3DFeatureCollectionPage tier=3]]]
Replace this whole block, markers included, with invariants, ownership, threading or gotchas that are not visible in the tables. Write *None.* if there is nothing worth saying.
[[[/PROSE]]]

## Used by

| Unit | Component | References |
|---|---|---|
| [qt-widgets/ImportScalarField3DDialog](ImportScalarField3DDialog.md) | qt-widgets | 2 |

## Related

**Qt Designer forms**

| Form class | Base widget | Title | Widgets |
|---|---|---|---|
| `ScalarField3DFeatureCollectionPage` | `QWizardPage` | WizardPage | 4 |

**Qt signal/slot connections** (1 in this unit)

| Sender | Signal | Receiver | Slot |
|---|---|---|---|
| `save_checkbox` | `stateChanged(int)` | `this` | `handle_save_checkbox_state_changed(int)` |


## Explore

Run these from the `gplates-code` skill directory:

```bash
python scripts/gpq.py file src/qt-widgets/ScalarField3DFeatureCollectionPage.h
python scripts/gpq.py def GPlatesQtWidgets::ScalarField3DFeatureCollectionPage --body
python scripts/gpq.py uses ScalarField3DFeatureCollectionPage --kind class
python scripts/gpq.py hier ScalarField3DFeatureCollectionPage
```
