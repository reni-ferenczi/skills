# ConfigModel

[Book TOC](../../TOC.md) · [gui](../../components/gui.md) · cluster Community 780 · tier 2

| Source file | Kind | Lines |
|---|---|---|
| `src/gui/ConfigModel.h` | C++ | 238 |
| `src/gui/ConfigModel.cc` | C++ | 299 |

## Overview

[[[PROSE overview unit=gui/ConfigModel tier=2]]]
Replace this whole block, markers included, with 1-3 paragraphs: what this unit is, why it exists, and how it fits the surrounding design. Do not restate the tables below.
[[[/PROSE]]]

## Declared types

| Name | Kind | Bases | Template | Subclasses | Description |
|---|---|---|---|---|---|
| [`GPlatesGui::ConfigModel`](#gplatesguiconfigmodel) | class | `QAbstractTableModel`<br>`boost::noncopyable` | — | 0 | A Qt Model class to adapt the interface of UserPreferences/ConfigBundle to a Qt TableView. |

## Members

### `GPlatesGui::ConfigModel`

| Member | Kind | Type | Access | Description |
|---|---|---|---|---|
| `CustomItemDataRole` | enum | `None` | public | Custom Qt::ItemDataRole to allow ConfigValueDelegate to reset a value to the default. |
| `ConfigModel( GPlatesUtils::ConfigInterface &_config, bool use_icons, QObject *_parent)` | constructor | `None` | public | Constructor for ConfigModel. |
| `~ConfigModel()` | destructor | `None` | public | — |
| `data( const QModelIndex &idx, int role = Qt::DisplayRole)` | method | `QVariant` | public | Qt Model/View accessor for data of a key or value (depending on index column). |
| `headerData( int section, Qt::Orientation orientation, int role)` | method | `QVariant` | public | Qt Model/View accessor for header contents and style. |
| `setData( const QModelIndex &idx, const QVariant &value, int role = Qt::EditRole)` | method | `bool` | public | Qt Model/View accessor to set data of a key's value. |
| `flags( const QModelIndex &idx)` | method | `Qt::ItemFlags` | public | Qt Model/View accessor for item flags of a key or value (depending on index column). |
| `rowCount( const QModelIndex &parent_idx)` | method | `int` | public | Qt Model/View accessor to see how many configuration keyvalues we have. |
| `columnCount( const QModelIndex &parent_idx)` | method | `int` | public | Qt Model/View accessor to see how many columns the table should have. |
| `SchemaEntry` | struct | `None` | public | In order to effectively map the hashmap-like ConfigInterface onto a table, complete with smart widget delegates and user-friendly key names, we need a few extra bits of metadata to be stored for each key name. |
| `SchemaType` | typedef | `QList<SchemaEntry>` | public | — |
| `react_key_value_updated( QString key)` | method | `void` | private | When our underlying ConfigInterface gets changed, we need to emite a 'dataChanged()' signal that Qt Views can use to repaint table cells as needed. |
| `get_name_data_for_role( const SchemaEntry &entry, int role)` | method | `QVariant` | private | Return suitable QVariant-packed data for the 'name' column of a particular SchemaEntry. |
| `get_value_data_for_role( const SchemaEntry &entry, int role)` | method | `QVariant` | private | Return suitable QVariant-packed data for the 'value' column of a particular SchemaEntry. |
| `ModelColumn` | enum | `None` | private | Configuration tables are only ever going to have two columns; the name and the value. |
| `d_config_ptr` | field | `QPointer<GPlatesUtils::ConfigInterface>` | private | The ConfigBundle or UserPreferences backend. |
| `d_schema` | field | `SchemaType` | private | The schema is a list of SchemaEntry structs that defines two important things for the ConfigModel:- 1. |
| `d_use_icons_indicating_defaults` | field | `bool` | private | The default setup for UserPreferences uses tick icons to show whether a default value has been overridden by the user. |
| `d_default_foreground` | field | `QVariant` | private | Default colours, packed into QBrushes, packed into QVariants, to be returned from data() accesses for table foreground/background requests. |
| `d_default_background` | field | `QVariant` | private | — |
| `d_user_overriding_default_icon` | field | `QVariant` | private | Possible icons indicating a user-set value, with and without a default backing it, and a blank icon for no user-set value. |
| `d_user_no_default_icon` | field | `QVariant` | private | — |
| `d_default_value_icon` | field | `QVariant` | private | — |

## Free functions and macros

| Name | Kind | Type / body | Description |
|---|---|---|---|
| `initialise_basic_schema( GPlatesGui::ConfigModel::SchemaType &schema, GPlatesUtils::ConfigInterface &config)` | function | `void` | Initialises the SchemaEntry list with a single basic entry per key found in the ConfigBundle/UserPreferences, so that we can use it as an 'index'. |
| `GPLATES_GUI_CONFIGMODEL_H` | macro | `None` | — |

## Notes

[[[PROSE notes unit=gui/ConfigModel tier=2]]]
Replace this whole block, markers included, with invariants, ownership, threading or gotchas that are not visible in the tables. Write *None.* if there is nothing worth saying.
[[[/PROSE]]]

## Used by

| Unit | Component | References |
|---|---|---|
| [gui/ConfigValueDelegate](ConfigValueDelegate.md) | gui | 12 |
| [gui/ConfigGuiUtils](ConfigGuiUtils.md) | gui | 3 |

## Related

**Qt signal/slot connections** (1 in this unit)

| Sender | Signal | Receiver | Slot |
|---|---|---|---|
| `d_config_ptr` | `key_value_updated(QString)` | `this` | `react_key_value_updated(QString)` |


## Explore

Run these from the `gplates-code` skill directory:

```bash
python scripts/gpq.py file src/gui/ConfigModel.h
python scripts/gpq.py def GPlatesGui::ConfigModel --body
python scripts/gpq.py uses ConfigModel --kind class
python scripts/gpq.py hier ConfigModel
```
