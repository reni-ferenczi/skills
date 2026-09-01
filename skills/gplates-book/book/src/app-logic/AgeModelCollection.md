# AgeModelCollection

[Book TOC](../../TOC.md) · [app-logic](../../components/app-logic.md) · cluster Community 350 · tier 2

| Source file | Kind | Lines |
|---|---|---|
| `src/app-logic/AgeModelCollection.h` | C++ | 196 |
| `src/app-logic/AgeModelCollection.cc` | C++ | 137 |

## Overview

`AgeModelCollection` holds the set of named age models (e.g. `CandeKent95`) imported
from an age model file: each `AgeModel` pairs an identifier with a `age_model_map_type`
mapping magnetic chron names such as `"2An.1ny"` to an age in Ma. The collection tracks
one model as "active" by index, exposes it through `get_active_age_model()`, and emits
`active_age_model_changed()` when the selection changes, so GUI code such as
`qt-widgets/AgeModelManagerDialog` can react to a user switching models.

Alongside the per-model chron ages, the collection separately keeps a file-wide,
chronologically ordered list of chron names (`d_ordered_chrons`) and free-text
per-chron metadata (`d_chron_comments`/`chron_comment_map_type`), both populated by
the file reader (`file-io/AgeModelReader`) as it parses each chron line in order,
since QString's default sort order does not match chronological chron order.

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

The `add_chron_to_model(const QString &model_id, ...)` overload is an empty stub — it
does nothing regardless of arguments. Only the index-based overload,
`add_chron_to_model(int index, ...)`, actually inserts into a model's `d_model` map;
callers that look up a model by identifier will silently lose data if they call the
wrong overload. `get_active_age_model()` and `set_active_age_model()` bounds-check
`d_active_model_index` against `d_age_models`, but `add_chron_to_model(int, ...)` and
`get_model_id(int)` only reject an index strictly greater than the size, so an index
equal to `size()` still reaches `at()` and throws `std::out_of_range`.

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
