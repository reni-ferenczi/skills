# EditFeaturePropertiesWidget

[Book TOC](../../TOC.md) · [qt-widgets](../../components/qt-widgets.md) · cluster Community 654 · tier 3

| Source file | Kind | Lines |
|---|---|---|
| `src/qt-widgets/EditFeaturePropertiesWidget.h` | C++ | 148 |
| `src/qt-widgets/EditFeaturePropertiesWidget.cc` | C++ | 292 |
| `src/qt-widgets/EditFeaturePropertiesWidgetUi.ui` | Qt form | 90 |

## Overview

[[[PROSE overview unit=qt-widgets/EditFeaturePropertiesWidget tier=3]]]
Replace this whole block, markers included, with 1-3 paragraphs: what this unit is, why it exists, and how it fits the surrounding design. Do not restate the tables below.
[[[/PROSE]]]

## Declared types

| Name | Kind | Bases | Template | Subclasses | Description |
|---|---|---|---|---|---|
| [`GPlatesQtWidgets::EditFeaturePropertiesWidget`](#gplatesqtwidgetseditfeaturepropertieswidget) | class | `QWidget`<br>`Ui_EditFeaturePropertiesWidget` | — | 0 | — |

## Members

### `GPlatesQtWidgets::EditFeaturePropertiesWidget`

| Member | Kind | Type | Access | Description |
|---|---|---|---|---|
| `EditFeaturePropertiesWidget( GPlatesPresentation::ViewState &view_state_, QWidget *parent_ = NULL)` | constructor | `None` | public | — |
| `~EditFeaturePropertiesWidget()` | destructor | `None` | public | — |
| `edit_feature( GPlatesModel::FeatureHandle::weak_ref feature_ref)` | method | `void` | public | Updates the dialog to display and edit a new Feature. |
| `clean_up()` | method | `void` | public | Call this to blank edit widgets and get ready for the next feature. |
| `commit_edit_widget_data()` | method | `void` | public | Causes any leftover data in line edits, spinboxes etc. to be committed. |
| `handle_feature_deletion()` | method | `void` | private | Wipes the EditFeaturePropertiesWidget clean without causing any leftover data to be commited (as that feature no longer exists). |
| `handle_model_change()` | method | `void` | private | — |
| `handle_selection_change( const QItemSelection &selected, const QItemSelection &deselected)` | method | `void` | private | — |
| `delete_selected_property()` | method | `void` | private | — |
| `set_up_edit_widgets()` | method | `void` | private | — |
| `d_feature_focus_ptr` | field | `GPlatesGui::FeatureFocus` | private | This is the feature focus which tracks changes to the currently focused feature. |
| `d_property_model_ptr` | field | `GPlatesGui::FeaturePropertyTableModel` | private | — |
| `d_feature_ref` | field | `GPlatesModel::FeatureHandle::weak_ref` | private | — |
| `d_edit_widget_group_box_ptr` | field | `GPlatesQtWidgets::EditWidgetGroupBox` | private | — |
| `d_add_property_dialog_ptr` | field | `GPlatesQtWidgets::AddPropertyDialog` | private | — |
| `d_selected_property_iterator` | field | `boost::optional<GPlatesModel::FeatureHandle::iterator>` | private | Used to remember which property is being edited by the currently-active Edit widget, so that data can be committed when editing is finished. |

## Free functions and macros

| Name | Kind | Type / body | Description |
|---|---|---|---|
| `GPLATES_QTWIDGETS_EDITFEATUREPROPERTIESWIDGET_H` | macro | `None` | — |

## Notes

[[[PROSE notes unit=qt-widgets/EditFeaturePropertiesWidget tier=3]]]
Replace this whole block, markers included, with invariants, ownership, threading or gotchas that are not visible in the tables. Write *None.* if there is nothing worth saying.
[[[/PROSE]]]

## Used by

| Unit | Component | References |
|---|---|---|
| [qt-widgets/FeaturePropertiesDialog](FeaturePropertiesDialog.md) | qt-widgets | 7 |

## Related

**Qt Designer forms**

| Form class | Base widget | Title | Widgets |
|---|---|---|---|
| `EditFeaturePropertiesWidget` | `QWidget` | Edit Feature Properties | 6 |

**Qt signal/slot connections** (6 in this unit)

| Sender | Signal | Receiver | Slot |
|---|---|---|---|
| `property_table->selectionModel()` | `selectionChanged(const QItemSelection &, const QItemSelection &)` | `this` | `handle_selection_change(const QItemSelection &, const QItemSelection &)` |
| `button_add_property` | `clicked()` | `d_add_property_dialog_ptr` | `pop_up()` |
| `button_delete_property` | `clicked()` | `this` | `delete_selected_property()` |
| `d_feature_focus_ptr` | `focused_feature_deleted( GPlatesGui::FeatureFocus &)` | `this` | `handle_feature_deletion()` |
| `d_property_model_ptr` | `feature_modified(GPlatesModel::FeatureHandle::weak_ref)` | `this` | `handle_model_change()` |
| `d_edit_widget_group_box_ptr` | `commit_me()` | `this` | `commit_edit_widget_data()` |


## Explore

Run these from the `gplates-code` skill directory:

```bash
python scripts/gpq.py file src/qt-widgets/EditFeaturePropertiesWidget.h
python scripts/gpq.py def GPlatesQtWidgets::EditFeaturePropertiesWidget --body
python scripts/gpq.py uses EditFeaturePropertiesWidget --kind class
python scripts/gpq.py hier EditFeaturePropertiesWidget
```
