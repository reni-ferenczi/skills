# MetadataDialog

[Book TOC](../../TOC.md) · [qt-widgets](../../components/qt-widgets.md) · cluster Community 69 · tier 3

| Source file | Kind | Lines |
|---|---|---|
| `src/qt-widgets/MetadataDialog.h` | C++ | 638 |
| `src/qt-widgets/MetadataDialog.cc` | C++ | 1657 |
| `src/qt-widgets/AddContributorWidgetUi.ui` | Qt form | 104 |
| `src/qt-widgets/AddCreatorWidgetUi.ui` | Qt form | 94 |
| `src/qt-widgets/AddGTSWidgetUi.ui` | Qt form | 94 |
| `src/qt-widgets/MetadataDialogUi.ui` | Qt form | 243 |

## Overview

[[[PROSE overview unit=qt-widgets/MetadataDialog tier=3]]]
Replace this whole block, markers included, with 1-3 paragraphs: what this unit is, why it exists, and how it fits the surrounding design. Do not restate the tables below.
[[[/PROSE]]]

## Declared types

| Name | Kind | Bases | Template | Subclasses | Description |
|---|---|---|---|---|---|
| [`RejectAllEdit`](#rejectalledit) | class | `QValidator` | — | 0 | — |
| [`GPlatesQtWidgets::DataEdit`](#gplatesqtwidgetsdataedit) | class | `QTextEdit` | — | 0 | — |
| [`GPlatesQtWidgets::MetadataTextEditor`](#gplatesqtwidgetsmetadatatexteditor) | class | `QWidget` | — | 0 | — |
| [`GPlatesQtWidgets::AddContributorWidget`](#gplatesqtwidgetsaddcontributorwidget) | class | `QWidget`<br>`Ui_AddContributorWidget` | — | 0 | — |
| [`GPlatesQtWidgets::AddGTSWidget`](#gplatesqtwidgetsaddgtswidget) | class | `QWidget`<br>`Ui_AddGTSWidget` | — | 0 | — |
| [`GPlatesQtWidgets::AddCreatorWidget`](#gplatesqtwidgetsaddcreatorwidget) | class | `QWidget`<br>`Ui_AddCreatorWidget` | — | 0 | — |
| [`GPlatesQtWidgets::MetadataDialog`](#gplatesqtwidgetsmetadatadialog) | class | `QDialog`<br>`Ui_MetadataDialog` | — | 0 | — |

## Members

### `RejectAllEdit`

| Member | Kind | Type | Access | Description |
|---|---|---|---|---|
| `validate( QString & input, int & pos )` | method | `State` | public | — |

### `GPlatesQtWidgets::DataEdit`

| Member | Kind | Type | Access | Description |
|---|---|---|---|---|
| `DataEdit( QWidget* parent_)` | constructor | `None` | public | — |
| `edit_finished()` | method | `void` | public | — |
| `focusOutEvent( QFocusEvent * event_ )` | method | `void` | protected | — |

### `GPlatesQtWidgets::MetadataTextEditor`

| Member | Kind | Type | Access | Description |
|---|---|---|---|---|
| `MetadataTextEditor( QString &text, MetadataDialog *dlg, bool opt = false, bool readonly = false)` | constructor | `None` | public | — |
| `edit_button_clicked()` | method | `void` | protected | — |
| `del_button_clicked()` | method | `void` | protected | — |
| `editor_text_changed()` | method | `void` | protected | — |
| `handle_edit_finished()` | method | `void` | protected | — |
| `setup_browser()` | method | `void` | protected | — |
| `setup_editor()` | method | `void` | protected | — |
| `setup_ui()` | method | `void` | protected | — |
| `h_layout` | field | `QHBoxLayout` | protected | — |
| `d_editor` | field | `DataEdit` | protected | — |
| `d_browser` | field | `QTextBrowser` | protected | — |
| `d_edit_button` | field | `QPushButton` | protected | — |
| `d_del_button` | field | `QPushButton` | protected | — |
| `d_txt` | field | `QString` | protected | — |
| `d_dlg` | field | `MetadataDialog` | protected | — |
| `d_optional` | field | `bool` | protected | — |
| `d_readonly` | field | `bool` | protected | — |

### `GPlatesQtWidgets::AddContributorWidget`

| Member | Kind | Type | Access | Description |
|---|---|---|---|---|
| `AddContributorWidget(QWidget *parent_=NULL)` | constructor | `None` | public | — |

### `GPlatesQtWidgets::AddGTSWidget`

| Member | Kind | Type | Access | Description |
|---|---|---|---|---|
| `AddGTSWidget(QWidget *parent_=NULL)` | constructor | `None` | public | — |

### `GPlatesQtWidgets::AddCreatorWidget`

| Member | Kind | Type | Access | Description |
|---|---|---|---|---|
| `AddCreatorWidget(QWidget *parent_=NULL)` | constructor | `None` | public | — |

### `GPlatesQtWidgets::MetadataDialog`

| Member | Kind | Type | Access | Description |
|---|---|---|---|---|
| `MetadataDialog( QWidget *parent_ = NULL)` | constructor | `None` | public | — |
| `MetaType` | enum | `None` | public | — |
| `set_data( const GPlatesModel::FeatureCollectionMetadata &d)` | method | `void` | public | — |
| `set_data( GPlatesModel::FeatureHandle::iterator iter)` | method | `void` | public | — |
| `set_data( GPlatesModel::FeatureHandle::iterator iter, QTreeWidgetItem*)` | method | `void` | public | — |
| `set_data( GPlatesModel::FeatureHandle::weak_ref f, QTreeWidgetItem*)` | method | `void` | public | — |
| `clear_data()` | method | `void` | public | — |
| `set_grot_proxy( GPlatesFileIO::PlatesRotationFileProxy *proxy)` | method | `void` | public | — |
| `save()` | method | `void` | public | — |
| `delete_row( MetadataTextEditor*)` | method | `void` | public | — |
| `refresh()` | method | `void` | public | — |
| `refresh_metadata_table()` | method | `void` | public | — |
| `refresh_add_new_entry_combobox()` | method | `void` | public | — |
| `handle_current_item_changed( QTreeWidgetItem *current, QTreeWidgetItem *previous)` | method | `void` | public | — |
| `handle_add_simple_entry_clicked()` | method | `void` | public | — |
| `handle_add_contributor_clicked()` | method | `void` | public | — |
| `handle_add_gts_clicked()` | method | `void` | public | — |
| `handle_add_creator_clicked()` | method | `void` | public | — |
| `handle_remove_button_clicked()` | method | `void` | public | — |
| `set_meta_table_style()` | method | `void` | protected | — |
| `show_creator()` | method | `void` | protected | — |
| `show_dc()` | method | `void` | protected | — |
| `show_rights()` | method | `void` | protected | — |
| `show_header_metadata()` | method | `void` | protected | — |
| `show_date()` | method | `void` | protected | — |
| `show_coverage()` | method | `void` | protected | — |
| `show_mprs()` | method | `void` | protected | — |
| `show_default_pole_data()` | method | `void` | protected | — |
| `show_mprs_only_data()` | method | `void` | protected | show the data which only applies to the rotation sequence. |
| `show_pole()` | method | `void` | protected | — |
| `show_contributors()` | method | `void` | protected | — |
| `show_timescales()` | method | `void` | protected | — |
| `show_bibinfo()` | method | `void` | protected | — |
| `show_data()` | method | `void` | protected | — |
| `show_gts()` | method | `void` | protected | — |
| `show_hell()` | method | `void` | protected | — |
| `show_au()` | method | `void` | protected | — |
| `populate_fc_meta()` | method | `void` | protected | — |
| `polulate_mprs()` | method | `void` | protected | — |
| `populate_pole()` | method | `void` | protected | — |
| `save_fc_meta()` | method | `void` | protected | — |
| `save_mprs_meta()` | method | `void` | protected | — |
| `save_pole_meta()` | method | `void` | protected | — |
| `show_gts( GPlatesModel::GeoTimeScale&, bool readonly = false)` | method | `void` | protected | — |
| `show_contributor( GPlatesModel::DublinCoreMetadata::Contributor &contr, bool readonly = false)` | method | `void` | protected | — |
| `get_pole_metadata( const GPlatesModel::MetadataContainer&, const GPlatesModel::MetadataContainer&)` | method | `GPlatesModel::MetadataContainer` | protected | Merge d\_mprs\_data and d\_pole\_data to get metadata applying to the pole. |
| `get_gpml_finite_rotation( GPlatesModel::PropertyValue::non_null_ptr_to_const_type)` | method | `GPlatesPropertyValues::GpmlFiniteRotation` | protected | — |
| `hide_all_opt_gui_widget()` | method | `void` | protected | — |
| `valid_unique_name( const QString &name, const std::vector<QString> &name_vec)` | method | `QString` | protected | — |
| `default_pole_data_begin()` | method | `GPlatesModel::MetadataContainer::iterator` | protected | — |
| `get_mprs_only_data()` | method | `GPlatesModel::MetadataContainer` | protected | — |
| `get_default_pole_data()` | method | `GPlatesModel::MetadataContainer` | protected | — |
| `is_the_contributor_name( const GPlatesModel::DublinCoreMetadata::Contributor &contr, const QString &name)` | method | `bool` | protected | — |
| `remove_contributor( QString &name)` | method | `void` | protected | — |
| `is_the_gts_name( const GPlatesModel::GeoTimeScale &scale, const QString &name)` | method | `bool` | protected | — |
| `remove_gts( QString &name)` | method | `void` | protected | — |
| `is_the_creator_name( const GPlatesModel::DublinCoreMetadata::Creator &c, const QString &name)` | method | `bool` | protected | — |
| `remove_creator( QString &name)` | method | `void` | protected | — |
| `~MetadataDialog()` | destructor | `None` | protected | — |
| `d_add_GTS_widget` | field | `AddGTSWidget` | protected | — |
| `d_add_contr_widget` | field | `AddContributorWidget` | protected | — |
| `d_add_creator_widget` | field | `AddCreatorWidget` | protected | — |
| `ItemType` | enum | `None` | private | — |
| `d_mprs_data` | field | `GPlatesModel::MetadataContainer` | private | — |
| `d_pole_data` | field | `GPlatesModel::MetadataContainer` | private | — |
| `d_fc_meta` | field | `GPlatesModel::FeatureCollectionMetadata` | private | — |
| `d_func_map` | field | `std::map<int, function>` | private | — |
| `d_type` | field | `MetaType` | private | — |
| `d_feature_iter` | field | `GPlatesModel::FeatureHandle::iterator` | private | — |
| `d_feature_ref` | field | `GPlatesModel::FeatureHandle::weak_ref` | private | — |
| `d_trs_dlg_current_item` | field | `QTreeWidgetItem` | private | — |
| `d_contributor_item` | field | `QTreeWidgetItem` | private | — |
| `d_gts_item` | field | `QTreeWidgetItem` | private | — |
| `d_creator_item` | field | `QTreeWidgetItem` | private | — |
| `d_grot_proxy` | field | `GPlatesFileIO::PlatesRotationFileProxy` | private | — |
| `d_moving_plate_id` | field | `QString` | private | — |

## Free functions and macros

| Name | Kind | Type / body | Description |
|---|---|---|---|
| `dc_rights` | variable | `QTreeWidgetItem` | — |
| `dc_date` | variable | `QTreeWidgetItem` | — |
| `dc_coverage` | variable | `QTreeWidgetItem` | — |
| `gpml_meta` | variable | `QTreeWidgetItem` | — |
| `bibinfo` | variable | `QTreeWidgetItem` | — |
| `convert_mprs_metadata_to_vector( GpmlKeyValueDictionary::non_null_ptr_to_const_type dict)` | function | `std::vector<boost::shared_ptr<Metadata> >` | — |
| `METADATA_DIALOG_H` | macro | `None` | — |

## Notes

[[[PROSE notes unit=qt-widgets/MetadataDialog tier=3]]]
Replace this whole block, markers included, with invariants, ownership, threading or gotchas that are not visible in the tables. Write *None.* if there is nothing worth saying.
[[[/PROSE]]]

## Used by

| Unit | Component | References |
|---|---|---|
| [qt-widgets/TotalReconstructionSequencesDialog](TotalReconstructionSequencesDialog.md) | qt-widgets | 4 |

## Related

**Qt Designer forms**

| Form class | Base widget | Title | Widgets |
|---|---|---|---|
| `AddContributorWidget` | `QWidget` | Form | 13 |
| `AddCreatorWidget` | `QWidget` | Form | 11 |
| `AddGTSWidget` | `QWidget` | Form | 11 |
| `MetadataDialog` | `QDialog` | Metadata Dialog | 10 |

**Qt signal/slot connections** (10 in this unit)

| Sender | Signal | Receiver | Slot |
|---|---|---|---|
| `d_edit_button` | `clicked()` | `this` | `edit_button_clicked()` |
| `d_del_button` | `clicked()` | `this` | `del_button_clicked()` |
| `d_editor` | `textChanged ()` | `this` | `editor_text_changed()` |
| `d_editor` | `edit_finished()` | `this` | `handle_edit_finished()` |
| `meta_tree` | `currentItemChanged(QTreeWidgetItem *, QTreeWidgetItem *)` | `this` | `handle_current_item_changed(QTreeWidgetItem *, QTreeWidgetItem *)` |
| `add_simple_entry_button` | `clicked()` | `this` | `handle_add_simple_entry_clicked()` |
| `remove_button` | `clicked()` | `this` | `handle_remove_button_clicked()` |
| `d_add_GTS_widget->add_button` | `clicked()` | `this` | `handle_add_gts_clicked()` |
| `d_add_contr_widget->add_contr_button` | `clicked()` | `this` | `handle_add_contributor_clicked()` |
| `d_add_creator_widget->add_button` | `clicked()` | `this` | `handle_add_creator_clicked()` |


## Explore

Run these from the `gplates-code` skill directory:

```bash
python scripts/gpq.py file src/qt-widgets/MetadataDialog.h
python scripts/gpq.py def GPlatesQtWidgets::MetadataDialog --body
python scripts/gpq.py uses MetadataDialog --kind class
python scripts/gpq.py hier MetadataDialog
```
