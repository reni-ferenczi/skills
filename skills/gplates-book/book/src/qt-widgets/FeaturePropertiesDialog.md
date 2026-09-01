# FeaturePropertiesDialog

[Book TOC](../../TOC.md) · [qt-widgets](../../components/qt-widgets.md) · cluster Community 914 · tier 3

| Source file | Kind | Lines |
|---|---|---|
| `src/qt-widgets/FeaturePropertiesDialog.h` | C++ | 144 |
| `src/qt-widgets/FeaturePropertiesDialog.cc` | C++ | 206 |
| `src/qt-widgets/FeaturePropertiesDialogUi.ui` | Qt form | 126 |

## Overview

[[[PROSE overview unit=qt-widgets/FeaturePropertiesDialog tier=3]]]
Replace this whole block, markers included, with 1-3 paragraphs: what this unit is, why it exists, and how it fits the surrounding design. Do not restate the tables below.
[[[/PROSE]]]

## Declared types

| Name | Kind | Bases | Template | Subclasses | Description |
|---|---|---|---|---|---|
| [`GPlatesQtWidgets::FeaturePropertiesDialog`](#gplatesqtwidgetsfeaturepropertiesdialog) | class | [`GPlatesDialog`](GPlatesDialog.md)<br>`Ui_FeaturePropertiesDialog` | — | 0 | — |

## Members

### `GPlatesQtWidgets::FeaturePropertiesDialog`

| Member | Kind | Type | Access | Description |
|---|---|---|---|---|
| `FeaturePropertiesDialog( GPlatesPresentation::ViewState &view_state_, QWidget *parent_ = NULL)` | constructor | `None` | public | — |
| `~FeaturePropertiesDialog()` | destructor | `None` | public | — |
| `display_feature( GPlatesGui::FeatureFocus &feature_focus)` | method | `void` | public | Display the given feature, which may or may not be different to the previous feature viewed. |
| `refresh_display()` | method | `void` | public | Update the current display from whatever feature the dialog was last viewing. |
| `choose_query_widget_and_open()` | method | `void` | public | — |
| `choose_edit_widget_and_open()` | method | `void` | public | — |
| `choose_geometries_widget_and_open()` | method | `void` | public | — |
| `setVisible( bool visible)` | method | `void` | public | We need to reimplement setVisible() because reimplementing closeEvent() is not enough - the default buttonbox "Close" button only appears to hide the dialog. |
| `handle_tab_change( int index)` | method | `void` | private | — |
| `pop_up_change_feature_type_dialog()` | method | `void` | private | — |
| `d_feature_ref` | field | `GPlatesModel::FeatureHandle::weak_ref` | private | The Feature observed by the dialog. |
| `d_focused_rg` | field | `GPlatesAppLogic::ReconstructionGeometry::maybe_null_ptr_to_const_type` | private | The ReconstructedFeatureGeometry associated with the feature that is in focus. |
| `d_query_feature_properties_widget` | field | `QueryFeaturePropertiesWidget` | private | — |
| `d_edit_feature_properties_widget` | field | `EditFeaturePropertiesWidget` | private | — |
| `d_view_feature_geometries_widget` | field | `ViewFeatureGeometriesWidget` | private | — |
| `d_change_feature_type_dialog` | field | `ChangeFeatureTypeDialog` | private | Allows the user to change the feature type of the currently selected feature and also fix up any geometry properties that are no longer valid. |

## Free functions and macros

| Name | Kind | Type / body | Description |
|---|---|---|---|
| `GPLATES_QTWIDGETS_FEATUREPROPERTIESDIALOG_H` | macro | `None` | — |

## Notes

[[[PROSE notes unit=qt-widgets/FeaturePropertiesDialog tier=3]]]
Replace this whole block, markers included, with invariants, ownership, threading or gotchas that are not visible in the tables. Write *None.* if there is nothing worth saying.
[[[/PROSE]]]

## Used by

| Unit | Component | References |
|---|---|---|
| [qt-widgets/ViewportWindow](ViewportWindow.md) | qt-widgets | 3 |
| [canvas-tools/ClickGeometry](../canvas-tools/ClickGeometry.md) | canvas-tools | 2 |
| [gui/Dialogs](../gui/Dialogs.md) | gui | 1 |

## Related

**Qt Designer forms**

| Form class | Base widget | Title | Widgets |
|---|---|---|---|
| `FeaturePropertiesDialog` | `QDialog` | Feature Properties | 7 |

**Qt signal/slot connections** (4 in this unit)

| Sender | Signal | Receiver | Slot |
|---|---|---|---|
| `tabwidget_query_edit` | `currentChanged(int)` | `this` | `handle_tab_change(int)` |
| `&view_state_.get_feature_focus()` | `focus_changed(GPlatesGui::FeatureFocus &)` | `this` | `display_feature(GPlatesGui::FeatureFocus &)` |
| `&view_state_.get_feature_focus()` | `focused_feature_modified(GPlatesGui::FeatureFocus &)` | `this` | `display_feature(GPlatesGui::FeatureFocus &)` |
| `toolbutton_change_feature_type` | `clicked()` | `this` | `pop_up_change_feature_type_dialog()` |


## Explore

Run these from the `gplates-code` skill directory:

```bash
python scripts/gpq.py file src/qt-widgets/FeaturePropertiesDialog.h
python scripts/gpq.py def GPlatesQtWidgets::FeaturePropertiesDialog --body
python scripts/gpq.py uses FeaturePropertiesDialog --kind class
python scripts/gpq.py hier FeaturePropertiesDialog
```
