# AgeModelCollection

[Book TOC](../../TOC.md) · [app-logic](../../components/app-logic.md) · cluster Community 350 · tier 2

| Source file | Kind | Lines |
|---|---|---|
| `src/app-logic/AgeModelCollection.h` | C++ | 196 |
| `src/app-logic/AgeModelCollection.cc` | C++ | 137 |

## Overview

[[[PROSE overview unit=app-logic/AgeModelCollection tier=2]]]
Replace this whole block, markers included, with 1-3 paragraphs: what this unit is, why it exists, and how it fits the surrounding design. Do not restate the tables below.
[[[/PROSE]]]

## Declared types

| Name | Kind | Bases | Template | Subclasses | Description |
|---|---|---|---|---|---|
| [`GPlatesAppLogic::age_model_map_type`](#gplatesapplogicage_model_map_type) | typedef | — | — | 0 | — |
| [`GPlatesAppLogic::age_model_pair_type`](#gplatesapplogicage_model_pair_type) | typedef | — | — | 0 | typedef std::vector\<std::pair\<QString,double\> \> age\_model\_map\_type; |
| [`GPlatesAppLogic::ordered_chron_container_type`](#gplatesapplogicordered_chron_container_type) | typedef | — | — | 0 | — |
| [`GPlatesAppLogic::chron_comment_map_type`](#gplatesapplogicchron_comment_map_type) | typedef | — | — | 0 | — |
| [`GPlatesAppLogic::AgeModel`](#gplatesapplogicagemodel) | struct | — | — | 0 | — |
| [`GPlatesAppLogic::age_model_container_type`](#gplatesapplogicage_model_container_type) | typedef | — | — | 0 | — |
| [`GPlatesAppLogic::AgeModelCollection`](#gplatesapplogicagemodelcollection) | class | `QObject`<br>`boost::noncopyable` | — | 0 | — |

## Members

### `GPlatesAppLogic::age_model_map_type`

*None.*

### `GPlatesAppLogic::age_model_pair_type`

*None.*

### `GPlatesAppLogic::ordered_chron_container_type`

*None.*

### `GPlatesAppLogic::chron_comment_map_type`

*None.*

### `GPlatesAppLogic::AgeModel`

| Member | Kind | Type | Access | Description |
|---|---|---|---|---|
| `AgeModel()` | constructor | `None` | public | — |
| `AgeModel( const QString &model_id)` | constructor | `None` | public | — |
| `d_identifier` | field | `QString` | public | d\_identifier - A brief name for the model, for example CandeKent95 |
| `d_model` | field | `age_model_map_type` | public | d\_model - a map of chron (e.g. "2An.1ny") to time (Ma) |

### `GPlatesAppLogic::age_model_container_type`

*None.*

### `GPlatesAppLogic::AgeModelCollection`

| Member | Kind | Type | Access | Description |
|---|---|---|---|---|
| `AgeModelCollection( QObject *parent_ = NULL)` | constructor | `None` | public | — |
| `get_active_age_model()` | method | `boost::optional<const AgeModel &>` | public | — |
| `set_active_age_model( unsigned int index)` | method | `void` | public | — |
| `add_age_model( const AgeModel &age_model)` | method | `void` | public | — |
| `add_chron_to_model( const QString &model_id, const QString &chron, double age)` | method | `void` | public | — |
| `add_chron_to_model( int index, const QString &chron, double age)` | method | `void` | public | — |
| `add_chron_metadata( const QString &chron, const QString &chron_metadata)` | method | `void` | public | — |
| `set_filename( const QString &filename)` | method | `void` | public | — |
| `set_age_models( const age_model_container_type &models)` | method | `void` | public | — |
| `number_of_age_models()` | method | `int` | public | — |
| `clear()` | method | `void` | public | — |
| `get_model_id( int index)` | method | `QString` | public | — |
| `add_next_ordered_chron( const QString &chron)` | method | `void` | public | — |
| `get_ordered_chrons` | field | `ordered_chron_container_type` | public | — |
| `get_chron_comment_map` | field | `chron_comment_map_type` | public | — |
| `active_age_model_changed()` | method | `void` | public | — |
| `d_age_models` | field | `age_model_container_type` | private | — |
| `d_chron_comments` | field | `chron_comment_map_type` | private | d\_chron\_comment - additional information relating to the chron - comments, references etc Ultimately we might have several fields here; for now I'm bundling everything into one QString. |
| `d_active_model_index` | field | `boost::optional<unsigned int>` | private | — |
| `d_filename` | field | `QString` | private | Name of file from which the age models were imported. |
| `d_ordered_chrons` | field | `std::vector<QString>` | private | An ordered vector of chrons, from youngest to oldest. |

## Free functions and macros

| Name | Kind | Type / body | Description |
|---|---|---|---|
| `GPLATES_APP_LOGIC_AGEMODELCOLLECTION_H` | macro | `None` | — |

## Notes

[[[PROSE notes unit=app-logic/AgeModelCollection tier=2]]]
Replace this whole block, markers included, with invariants, ownership, threading or gotchas that are not visible in the tables. Write *None.* if there is nothing worth saying.
[[[/PROSE]]]

## Used by

| Unit | Component | References |
|---|---|---|
| [app-logic/ApplicationState](ApplicationState.md) | app-logic | 52 |
| [qt-widgets/AgeModelManagerDialog](../qt-widgets/AgeModelManagerDialog.md) | qt-widgets | 40 |
| [file-io/AgeModelReader](../file-io/AgeModelReader.md) | file-io | 20 |
| [qt-widgets/HellingerDialog](../qt-widgets/HellingerDialog.md) | qt-widgets | 15 |

## Related

*None.*

## Explore

Run these from the `gplates-code` skill directory:

```bash
python scripts/gpq.py file src/app-logic/AgeModelCollection.h
python scripts/gpq.py def GPlatesAppLogic::AgeModelCollection --body
python scripts/gpq.py uses AgeModelCollection --kind class
python scripts/gpq.py hier AgeModelCollection
```
