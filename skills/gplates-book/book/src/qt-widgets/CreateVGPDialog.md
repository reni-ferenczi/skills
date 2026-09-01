# CreateVGPDialog

[Book TOC](../../TOC.md) · [qt-widgets](../../components/qt-widgets.md) · cluster Community 686 · tier 3

| Source file | Kind | Lines |
|---|---|---|
| `src/qt-widgets/CreateVGPDialog.h` | C++ | 154 |
| `src/qt-widgets/CreateVGPDialog.cc` | C++ | 403 |
| `src/qt-widgets/CreateVGPDialogUi.ui` | Qt form | 410 |

## Overview

[[[PROSE overview unit=qt-widgets/CreateVGPDialog tier=3]]]
Replace this whole block, markers included, with 1-3 paragraphs: what this unit is, why it exists, and how it fits the surrounding design. Do not restate the tables below.
[[[/PROSE]]]

## Declared types

| Name | Kind | Bases | Template | Subclasses | Description |
|---|---|---|---|---|---|
| [`GPlatesQtWidgets::CreateVGPDialog`](#gplatesqtwidgetscreatevgpdialog) | class | [`GPlatesDialog`](GPlatesDialog.md)<br>`Ui_CreateVGPDialog` | — | 0 | — |

## Members

### `GPlatesQtWidgets::CreateVGPDialog`

| Member | Kind | Type | Access | Description |
|---|---|---|---|---|
| `StackedWidgetPage` | enum | `None` | public | — |
| `CreateVGPDialog( GPlatesPresentation::ViewState &view_state_, QWidget *parent_ = NULL)` | constructor | `None` | public | — |
| `reset()` | method | `void` | public | Reset the state of the dialog for a new creation process. |
| `feature_created()` | method | `void` | public | — |
| `feature_collection_created( GPlatesModel::FeatureCollectionHandle::weak_ref feature_collection, GPlatesAppLogic::FeatureCollectionFileState::file_reference &file_iter)` | method | `void` | public | FIXME: Not sure if this signal is required any more. |
| `setup_connections()` | method | `void` | private | — |
| `setup_properties_page()` | method | `void` | private | — |
| `setup_collection_page()` | method | `void` | private | — |
| `handle_previous()` | method | `void` | private | — |
| `handle_next()` | method | `void` | private | — |
| `handle_create()` | method | `void` | private | — |
| `handle_cancel()` | method | `void` | private | — |
| `handle_site_checked(int state)` | method | `void` | private | — |
| `d_model_ptr` | field | `GPlatesModel::ModelInterface` | private | The Model interface, used to create new features. |
| `d_file_state` | field | `GPlatesAppLogic::FeatureCollectionFileState` | private | The loaded feature collection files. |
| `d_file_io` | field | `GPlatesAppLogic::FeatureCollectionFileIO` | private | Used to create an empty feature collection file. |
| `d_application_state_ptr` | field | `GPlatesAppLogic::ApplicationState` | private | The application state is used to access the reconstruction tree to perform reverse reconstruction of the temporary geometry (once we know the plate id). |
| `d_choose_feature_collection_widget` | field | `ChooseFeatureCollectionWidget` | private | The widget that allows the user to select an existing feature collection to add the new feature to, or a new feature collection. |

## Free functions and macros

| Name | Kind | Type / body | Description |
|---|---|---|---|
| `append_name_to_feature( const GPlatesModel::FeatureHandle::weak_ref &feature, const QString &description)` | function | `void` | FIXME: The following append.... functions are a duplicate of those in GmapReader's anonymous namespace These should be put somewhere accessible by both the GmapReader and CreateVGPFeature. |
| `append_site_geometry_to_feature( const GPlatesModel::FeatureHandle::weak_ref &feature, const float &latitude, const float &longitude)` | function | `void` | — |
| `append_inclination_to_feature( const GPlatesModel::FeatureHandle::weak_ref &feature, const float &inclination)` | function | `void` | — |
| `append_declination_to_feature( const GPlatesModel::FeatureHandle::weak_ref &feature, const float &declination)` | function | `void` | — |
| `append_a95_to_feature( const GPlatesModel::FeatureHandle::weak_ref &feature, const float &a95)` | function | `void` | — |
| `append_age_to_feature( const GPlatesModel::FeatureHandle::weak_ref &feature, const float &age)` | function | `void` | — |
| `append_vgp_position_to_feature( const GPlatesModel::FeatureHandle::weak_ref &feature, const float &vgp_latitude, const float &vgp_longitude)` | function | `void` | — |
| `append_plate_id_to_feature( const GPlatesModel::FeatureHandle::weak_ref &feature, const GPlatesModel::integer_plate_id_type &plate_id)` | function | `void` | — |
| `append_dm_to_feature( const GPlatesModel::FeatureHandle::weak_ref &feature, const float &dm)` | function | `void` | — |
| `append_dp_to_feature( const GPlatesModel::FeatureHandle::weak_ref &feature, const float &dp)` | function | `void` | — |
| `GPLATES_QTWIDGETS_CREATEVGPDIALOG_H` | macro | `None` | — |

## Notes

[[[PROSE notes unit=qt-widgets/CreateVGPDialog tier=3]]]
Replace this whole block, markers included, with invariants, ownership, threading or gotchas that are not visible in the tables. Write *None.* if there is nothing worth saying.
[[[/PROSE]]]

## Used by

| Unit | Component | References |
|---|---|---|
| [gui/Dialogs](../gui/Dialogs.md) | gui | 1 |

## Related

**Qt Designer forms**

| Form class | Base widget | Title | Widgets |
|---|---|---|---|
| `CreateVGPDialog` | `QDialog` | Create Virtual Geomagnetic Pole | 28 |

**Qt signal/slot connections** (7 in this unit)

| Sender | Signal | Receiver | Slot |
|---|---|---|---|
| `button_previous` | `clicked()` | `this` | `handle_previous()` |
| `button_next` | `clicked()` | `this` | `handle_next()` |
| `button_create` | `clicked()` | `this` | `handle_create()` |
| `button_cancel` | `clicked()` | `this` | `handle_cancel()` |
| `checkbox_site` | `stateChanged(int)` | `this` | `handle_site_checked(int)` |
| `d_choose_feature_collection_widget` | `item_activated()` | `button_create` | `setFocus()` |
| `this` | `feature_created()` | `d_application_state_ptr` | `reconstruct()` |


## Explore

Run these from the `gplates-code` skill directory:

```bash
python scripts/gpq.py file src/qt-widgets/CreateVGPDialog.h
python scripts/gpq.py def GPlatesQtWidgets::CreateVGPDialog --body
python scripts/gpq.py uses CreateVGPDialog --kind class
python scripts/gpq.py hier CreateVGPDialog
```
