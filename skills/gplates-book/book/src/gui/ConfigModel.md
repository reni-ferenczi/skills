# ConfigModel

[Book TOC](../../TOC.md) · [gui](../../components/gui.md) · cluster Community 780 · tier 2

| Source file | Kind | Lines |
|---|---|---|
| `src/gui/ConfigModel.h` | C++ | 238 |
| `src/gui/ConfigModel.cc` | C++ | 299 |

## Overview

`ConfigModel` is the `QAbstractTableModel` that lets a `QTableView` display and edit an arbitrary `GPlatesUtils::ConfigInterface` (a `ConfigBundle` or `UserPreferences` instance) as a two-column name/value table. It builds its row list once, at construction, by calling the free function `initialise_basic_schema()`, which enumerates `config.subkeys()` into a flat `SchemaType` list of `SchemaEntry { key, label }` pairs — currently just the key name repeated as its own label, though the header notes this indexing step could later be replaced by a user-supplied or Python-generated schema. Because `ConfigInterface` itself has no concept of row order or display metadata, this schema is what gives the table a stable row-to-key mapping.

When `use_icons` is enabled, the name column's `Qt::DecorationRole` shows one of three icons per row — `d_user_overriding_default_icon`, `d_user_no_default_icon` or `d_default_value_icon` — chosen from `d_config_ptr->has_been_set()` and `default_exists()`, so a `QTableView` can indicate at a glance whether a preference is at its default, user-overridden with a default behind it, or user-set with no default. `setData()` also honours a private role, `ROLE_RESET_VALUE_TO_DEFAULT`, that `ConfigValueDelegate` uses to route a "reset to default" click straight to `d_config_ptr->clear_value()` rather than through the normal `Qt::EditRole` path.

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

`d_config_ptr` is a `QPointer`, not an owning reference, so the model tolerates its backing `ConfigInterface` being destroyed but does not extend its lifetime; the constructor connects `key_value_updated` into `react_key_value_updated()` so external changes to the backend still repaint the affected row via `dataChanged()`. The schema built by `initialise_basic_schema()` is captured once at construction — keys added to the `ConfigInterface` afterwards will not appear as new rows since nothing rebuilds `d_schema`. The class is `boost::noncopyable`, and only the value column is editable (`flags()` and `setData()` both refuse edits on `COLUMN_NAME`).

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
