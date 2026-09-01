# FeatureSummaryWidget

[Book TOC](../../TOC.md) · [qt-widgets](../../components/qt-widgets.md) · cluster Community 236 · tier 3

| Source file | Kind | Lines |
|---|---|---|
| `src/qt-widgets/FeatureSummaryWidget.h` | C++ | 102 |
| `src/qt-widgets/FeatureSummaryWidget.cc` | C++ | 408 |
| `src/qt-widgets/FeatureSummaryWidgetUi.ui` | Qt form | 214 |

## Overview

[[[PROSE overview unit=qt-widgets/FeatureSummaryWidget tier=3]]]
Replace this whole block, markers included, with 1-3 paragraphs: what this unit is, why it exists, and how it fits the surrounding design. Do not restate the tables below.
[[[/PROSE]]]

## Declared types

| Name | Kind | Bases | Template | Subclasses | Description |
|---|---|---|---|---|---|
| [`GPlatesQtWidgets::FeatureSummaryWidget`](#gplatesqtwidgetsfeaturesummarywidget) | class | [`TaskPanelWidget`](TaskPanelWidget.md)<br>`Ui_FeatureSummaryWidget` | — | 0 | — |

## Members

### `GPlatesQtWidgets::FeatureSummaryWidget`

| Member | Kind | Type | Access | Description |
|---|---|---|---|---|
| `FeatureSummaryWidget( GPlatesPresentation::ViewState &view_state_, QWidget *parent_ = NULL)` | constructor | `None` | public | — |
| `handle_activation()` | method | `void` | public | — |
| `get_clear_action_text()` | method | `QString` | public | — |
| `clear_action_enabled()` | method | `bool` | public | — |
| `handle_clear_action_triggered()` | method | `void` | public | — |
| `clear()` | method | `void` | public | — |
| `display_feature( GPlatesGui::FeatureFocus &feature_focus)` | method | `void` | public | — |
| `hide_plate_id_fields_as_appropriate()` | method | `void` | private | — |
| `d_file_state` | field | `GPlatesAppLogic::FeatureCollectionFileState` | private | The loaded feature collection files. |
| `d_feature_focus` | field | `GPlatesGui::FeatureFocus` | private | — |

## Free functions and macros

| Name | Kind | Type / body | Description |
|---|---|---|---|
| `format_time_instant( const GPlatesPropertyValues::GmlTimeInstant &time_instant)` | function | `QString` | Borrowed from FeatureTableModel.cc. |
| `fill_plate_id_field( QLineEdit *field, GPlatesModel::FeatureHandle::weak_ref feature_ref, const GPlatesModel::PropertyName &property_name)` | function | `void` | We now have four of these plate ID fields. |
| `feature_collection_contains_feature( GPlatesModel::FeatureCollectionHandle::const_weak_ref collection_ref, GPlatesModel::FeatureHandle::const_weak_ref feature_ref)` | function | `bool` | The slow way to test membership of a FeatureHandle in a FeatureCollection. |
| `get_file_reference_for_feature( GPlatesAppLogic::FeatureCollectionFileState &state, GPlatesModel::FeatureHandle::const_weak_ref feature_ref)` | function | `boost::optional<GPlatesAppLogic::FeatureCollectionFileState::file_reference>` | The slow way to ascertain what File a particular Feature belongs to. |
| `get_feature_collection_name_for_feature( GPlatesAppLogic::FeatureCollectionFileState &file_state, GPlatesModel::FeatureHandle::const_weak_ref feature_ref)` | function | `QString` | Returns the name of the FeatureCollection that the given FeatureHandle is contained within. |
| `GPLATES_QTWIDGETS_FEATURESUMMARYWIDGET_H` | macro | `None` | — |

## Notes

[[[PROSE notes unit=qt-widgets/FeatureSummaryWidget tier=3]]]
Replace this whole block, markers included, with invariants, ownership, threading or gotchas that are not visible in the tables. Write *None.* if there is nothing worth saying.
[[[/PROSE]]]

## Used by

| Unit | Component | References |
|---|---|---|
| [qt-widgets/TaskPanel](TaskPanel.md) | qt-widgets | 2 |
| [qt-widgets/TopologyToolsWidget](TopologyToolsWidget.md) | qt-widgets | 2 |

## Related

**Qt Designer forms**

| Form class | Base widget | Title | Widgets |
|---|---|---|---|
| `FeatureSummaryWidget` | `QWidget` | Form | 22 |

**Qt signal/slot connections** (2 in this unit)

| Sender | Signal | Receiver | Slot |
|---|---|---|---|
| `&d_feature_focus` | `focus_changed(GPlatesGui::FeatureFocus &)` | `this` | `display_feature(GPlatesGui::FeatureFocus &)` |
| `&d_feature_focus` | `focused_feature_modified(GPlatesGui::FeatureFocus &)` | `this` | `display_feature(GPlatesGui::FeatureFocus &)` |


## Explore

Run these from the `gplates-code` skill directory:

```bash
python scripts/gpq.py file src/qt-widgets/FeatureSummaryWidget.h
python scripts/gpq.py def GPlatesQtWidgets::FeatureSummaryWidget --body
python scripts/gpq.py uses FeatureSummaryWidget --kind class
python scripts/gpq.py hier FeatureSummaryWidget
```
