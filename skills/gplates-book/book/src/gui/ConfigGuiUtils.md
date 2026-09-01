# ConfigGuiUtils

[Book TOC](../../TOC.md) · [gui](../../components/gui.md) · cluster Community 675 · tier 2

| Source file | Kind | Lines |
|---|---|---|
| `src/gui/ConfigGuiUtils.h` | C++ | 267 |
| `src/gui/ConfigGuiUtils.cc` | C++ | 360 |

## Overview

[[[PROSE overview unit=gui/ConfigGuiUtils tier=2]]]
Replace this whole block, markers included, with 1-3 paragraphs: what this unit is, why it exists, and how it fits the surrounding design. Do not restate the tables below.
[[[/PROSE]]]

## Declared types

| Name | Kind | Bases | Template | Subclasses | Description |
|---|---|---|---|---|---|
| [`GPlatesGui::ConfigGuiUtils::MapValueEquals`](#gplatesguiconfigguiutilsmapvalueequals) | class | — | — | 0 | — |
| [`GPlatesGui::ConfigGuiUtils::ConfigWidgetAdapter`](#gplatesguiconfigguiutilsconfigwidgetadapter) | class | `QObject` | — | 0 | — |
| [`GPlatesGui::ConfigGuiUtils::ConfigButtonGroupAdapter`](#gplatesguiconfigguiutilsconfigbuttongroupadapter) | class | `QObject` | — | 0 | The ConfigButtonGroupAdapter class - this is an awkward workaround for storing values from a group of radio buttons in preferences. |

## Members

### `GPlatesGui::ConfigGuiUtils::MapValueEquals`

| Member | Kind | Type | Access | Description |
|---|---|---|---|---|
| `MapValueEquals( QString value)` | constructor | `None` | public | — |
| `operator()( const QString &value)` | operator | `bool` | public | — |
| `d_value` | field | `QString` | private | — |

### `GPlatesGui::ConfigGuiUtils::ConfigWidgetAdapter`

| Member | Kind | Type | Access | Description |
|---|---|---|---|---|
| `ConfigWidgetAdapter( QWidget *widget, GPlatesUtils::ConfigInterface &config, const QString &key)` | constructor | `None` | public | — |
| `~ConfigWidgetAdapter()` | destructor | `None` | public | — |
| `value_changed( const QString &value)` | method | `void` | public | — |
| `value_changed( bool value)` | method | `void` | public | — |
| `value_changed( int value)` | method | `void` | public | — |
| `value_changed( double value)` | method | `void` | public | — |
| `handle_key_value_updated( QString key)` | method | `void` | public | — |
| `handle_widget_value_updated( QString value)` | method | `void` | public | — |
| `handle_widget_value_updated( bool value)` | method | `void` | public | — |
| `handle_widget_value_updated( int value)` | method | `void` | public | — |
| `handle_widget_value_updated( double value)` | method | `void` | public | — |
| `handle_widget_editing_finished()` | method | `void` | public | Because QLineEdit::editingFinished() doesn't also provide the text. |
| `handle_reset_clicked()` | method | `void` | public | — |
| `d_widget_ptr` | field | `QPointer<QWidget>` | private | — |
| `d_config` | field | `GPlatesUtils::ConfigInterface` | private | — |
| `d_key` | field | `QString` | private | — |

### `GPlatesGui::ConfigGuiUtils::ConfigButtonGroupAdapter`

| Member | Kind | Type | Access | Description |
|---|---|---|---|---|
| `button_enum_to_description_map_type` | typedef | `QMap<int,QString>` | public | — |
| `ConfigButtonGroupAdapter( QButtonGroup *button_group, GPlatesUtils::ConfigInterface &config, const QString &key, const button_enum_to_description_map_type &button_to_description_map)` | constructor | `None` | public | — |
| `~ConfigButtonGroupAdapter()` | destructor | `None` | public | — |
| `value_changed( int value)` | method | `void` | public | — |
| `handle_key_value_updated( QString key)` | method | `void` | public | — |
| `handle_checked_button_changed( int index)` | method | `void` | public | — |
| `set_checked_button( int index)` | method | `void` | public | — |
| `handle_reset_clicked()` | method | `void` | public | — |
| `d_button_group_ptr` | field | `QPointer<QButtonGroup>` | private | — |
| `d_config` | field | `GPlatesUtils::ConfigInterface` | private | — |
| `d_key` | field | `QString` | private | — |
| `d_button_to_description_map` | field | `button_enum_to_description_map_type` | private | — |

## Free functions and macros

| Name | Kind | Type / body | Description |
|---|---|---|---|
| `GPLATES_GUI_CONFIGGUIUTILS_H` | macro | `None` | — |
| `link_config_interface_to_table( GPlatesUtils::ConfigInterface &config, bool use_icons, QWidget *parent)` | function | `GPlatesQtWidgets::ConfigTableView` | Given a ConfigBundle (or UserPreferences) and parent widget, create a QTableView that is linked to the ConfigBundle; changes in one will be reflected in the other. |
| `link_widget_to_preference( QLineEdit *widget, GPlatesUtils::ConfigInterface &config, const QString &key, QAbstractButton *reset_button)` | function | `void` | Given an existing widget (of a small number of supported types), set up signal/slot connections so that the value of the widget is synchronised with a UserPreferences key. |
| `link_widget_to_preference( QCheckBox *widget, GPlatesUtils::ConfigInterface &config, const QString &key, QAbstractButton *reset_button)` | function | `void` | — |
| `link_widget_to_preference( QSpinBox *widget, GPlatesUtils::ConfigInterface &config, const QString &key, QAbstractButton *reset_button)` | function | `void` | — |
| `link_widget_to_preference( QDoubleSpinBox *widget, GPlatesUtils::ConfigInterface &config, const QString &key, QAbstractButton *reset_button)` | function | `void` | — |
| `link_button_group_to_preference( QButtonGroup *button_group, GPlatesUtils::ConfigInterface &config, const QString &key, const GPlatesGui::ConfigGuiUtils::ConfigButtonGroupAdapter::button_enum_to_description_map_type &map, QAbstractButton *reset_button)` | function | `void` | — |

## Notes

[[[PROSE notes unit=gui/ConfigGuiUtils tier=2]]]
Replace this whole block, markers included, with invariants, ownership, threading or gotchas that are not visible in the tables. Write *None.* if there is nothing worth saying.
[[[/PROSE]]]

## Used by

| Unit | Component | References |
|---|---|---|
| [qt-widgets/PreferencesPaneFiles](../qt-widgets/PreferencesPaneFiles.md) | qt-widgets | 29 |
| [gui/FileIODirectoryConfigurations](FileIODirectoryConfigurations.md) | gui | 17 |
| [qt-widgets/KinematicGraphsConfigurationWidget](../qt-widgets/KinematicGraphsConfigurationWidget.md) | qt-widgets | 17 |
| [qt-widgets/PreferencesPaneView](../qt-widgets/PreferencesPaneView.md) | qt-widgets | 12 |
| [qt-widgets/PreferencesPaneKinematicGraphs](../qt-widgets/PreferencesPaneKinematicGraphs.md) | qt-widgets | 11 |
| [qt-widgets/PreferencesPaneNetwork](../qt-widgets/PreferencesPaneNetwork.md) | qt-widgets | 10 |
| [qt-widgets/PreferencesPanePython](../qt-widgets/PreferencesPanePython.md) | qt-widgets | 10 |
| [qt-widgets/KinematicGraphsConfigurationDialog](../qt-widgets/KinematicGraphsConfigurationDialog.md) | qt-widgets | 5 |
| [qt-widgets/PreferencesDialog](../qt-widgets/PreferencesDialog.md) | qt-widgets | 5 |
| [qt-widgets/KinematicGraphsDialog](../qt-widgets/KinematicGraphsDialog.md) | qt-widgets | 3 |
| [qt-widgets/OpenFileDialog](../qt-widgets/OpenFileDialog.md) | qt-widgets | 3 |

## Related

**Qt signal/slot connections** (16 in this unit)

| Sender | Signal | Receiver | Slot |
|---|---|---|---|
| `adapter` | `value_changed(const QString &)` | `widget` | `setText(const QString &)` |
| `widget` | `editingFinished()` | `adapter` | `handle_widget_editing_finished()` |
| `reset_button` | `clicked()` | `adapter` | `handle_reset_clicked()` |
| `adapter` | `value_changed(bool)` | `widget` | `setChecked(bool)` |
| `widget` | `clicked(bool)` | `adapter` | `handle_widget_value_updated(bool)` |
| `reset_button` | `clicked()` | `adapter` | `handle_reset_clicked()` |
| `adapter` | `value_changed(int)` | `widget` | `setValue(int)` |
| `widget` | `valueChanged(int)` | `adapter` | `handle_widget_value_updated(int)` |
| `reset_button` | `clicked()` | `adapter` | `handle_reset_clicked()` |
| `adapter` | `value_changed(double)` | `widget` | `setValue(double)` |
| `widget` | `valueChanged(double)` | `adapter` | `handle_widget_value_updated(double)` |
| `reset_button` | `clicked()` | `adapter` | `handle_reset_clicked()` |
| `adapter` | `value_changed(int)` | `adapter` | `set_checked_button(int)` |
| `button_group` | `buttonClicked(int)` | `adapter` | `handle_checked_button_changed(int)` |
| `&config` | `key_value_updated(QString)` | `this` | `handle_key_value_updated(QString)` |

*... and 1 more connections.*


## Explore

Run these from the `gplates-code` skill directory:

```bash
python scripts/gpq.py file src/gui/ConfigGuiUtils.h
python scripts/gpq.py def GPlatesGui::ConfigGuiUtils::ConfigWidgetAdapter --body
python scripts/gpq.py uses ConfigWidgetAdapter --kind class
python scripts/gpq.py hier ConfigWidgetAdapter
```
