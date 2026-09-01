# CreateSmallCircleFeatureDialog

[Book TOC](../../TOC.md) · [qt-widgets](../../components/qt-widgets.md) · cluster Community 785 · tier 3

| Source file | Kind | Lines |
|---|---|---|
| `src/qt-widgets/CreateSmallCircleFeatureDialog.h` | C++ | 152 |
| `src/qt-widgets/CreateSmallCircleFeatureDialog.cc` | C++ | 315 |
| `src/qt-widgets/CreateSmallCircleFeatureDialogUi.ui` | Qt form | 133 |

## Overview

[[[PROSE overview unit=qt-widgets/CreateSmallCircleFeatureDialog tier=3]]]
Replace this whole block, markers included, with 1-3 paragraphs: what this unit is, why it exists, and how it fits the surrounding design. Do not restate the tables below.
[[[/PROSE]]]

## Declared types

| Name | Kind | Bases | Template | Subclasses | Description |
|---|---|---|---|---|---|
| [`GPlatesQtWidgets::CreateSmallCircleFeatureDialog`](#gplatesqtwidgetscreatesmallcirclefeaturedialog) | class | `QDialog`<br>`Ui_CreateSmallCircleFeatureDialog` | — | 0 | — |

## Members

### `GPlatesQtWidgets::CreateSmallCircleFeatureDialog`

| Member | Kind | Type | Access | Description |
|---|---|---|---|---|
| `small_circle_collection_type` | typedef | `std::vector<GPlatesMaths::SmallCircle>` | private | Convenience typedef for small circle collection. |
| `StackedWidgetPage` | enum | `None` | public | — |
| `CreateSmallCircleFeatureDialog( GPlatesAppLogic::ApplicationState *app_state_ptr, const small_circle_collection_type &small_circles, QWidget *parent_ = NULL)` | constructor | `None` | public | — |
| `reset()` | method | `void` | public | Reset the state of the dialog for a new creation process. |
| `feature_created()` | method | `void` | public | — |
| `setup_connections()` | method | `void` | private | — |
| `setup_properties_page()` | method | `void` | private | — |
| `setup_collection_page()` | method | `void` | private | — |
| `handle_previous()` | method | `void` | private | — |
| `handle_next()` | method | `void` | private | — |
| `handle_create()` | method | `void` | private | — |
| `handle_cancel()` | method | `void` | private | — |
| `d_model_ptr` | field | `GPlatesModel::ModelInterface` | private | The Model interface, used to create new features. |
| `d_file_state` | field | `GPlatesAppLogic::FeatureCollectionFileState` | private | The loaded feature collection files. |
| `d_file_io` | field | `GPlatesAppLogic::FeatureCollectionFileIO` | private | Used to create an empty feature collection file. |
| `d_application_state_ptr` | field | `GPlatesAppLogic::ApplicationState` | private | The application state is used to access the reconstruction tree to perform reverse reconstruction of the temporary geometry (once we know the plate id). |
| `d_choose_feature_collection_widget` | field | `ChooseFeatureCollectionWidget` | private | The widget that allows the user to select an existing feature collection to add the new feature to, or a new feature collection. |
| `d_edit_time_period_widget` | field | `EditTimePeriodWidget` | private | Widget for defining a time period. |
| `d_small_circles` | field | `small_circle_collection_type` | private | A reference to the small circle collection which we will make features out of. |

## Free functions and macros

| Name | Kind | Type / body | Description |
|---|---|---|---|
| `append_name_to_feature( const GPlatesModel::FeatureHandle::weak_ref &feature, const QString &name)` | function | `void` | — |
| `append_description_to_feature( const GPlatesModel::FeatureHandle::weak_ref &feature, const QString &description)` | function | `void` | — |
| `GPLATES_QTWIDGETS_CREATESMALLCIRCLEFEATUREDIALOG_H` | macro | `None` | — |

## Notes

[[[PROSE notes unit=qt-widgets/CreateSmallCircleFeatureDialog tier=3]]]
Replace this whole block, markers included, with invariants, ownership, threading or gotchas that are not visible in the tables. Write *None.* if there is nothing worth saying.
[[[/PROSE]]]

## Used by

| Unit | Component | References |
|---|---|---|
| [qt-widgets/SmallCircleWidget](SmallCircleWidget.md) | qt-widgets | 20 |

## Related

**Qt Designer forms**

| Form class | Base widget | Title | Widgets |
|---|---|---|---|
| `CreateSmallCircleFeatureDialog` | `QDialog` | Dialog | 15 |

**Qt signal/slot connections** (6 in this unit)

| Sender | Signal | Receiver | Slot |
|---|---|---|---|
| `button_previous` | `clicked()` | `this` | `handle_previous()` |
| `button_next` | `clicked()` | `this` | `handle_next()` |
| `button_create` | `clicked()` | `this` | `handle_create()` |
| `button_cancel` | `clicked()` | `this` | `handle_cancel()` |
| `d_choose_feature_collection_widget` | `item_activated()` | `button_create` | `setFocus()` |
| `this` | `feature_created()` | `d_application_state_ptr` | `reconstruct()` |


## Explore

Run these from the `gplates-code` skill directory:

```bash
python scripts/gpq.py file src/qt-widgets/CreateSmallCircleFeatureDialog.h
python scripts/gpq.py def GPlatesQtWidgets::CreateSmallCircleFeatureDialog --body
python scripts/gpq.py uses CreateSmallCircleFeatureDialog --kind class
python scripts/gpq.py hier CreateSmallCircleFeatureDialog
```
