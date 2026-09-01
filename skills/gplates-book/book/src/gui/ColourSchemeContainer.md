# ColourSchemeContainer

[Book TOC](../../TOC.md) · [gui](../../components/gui.md) · cluster Community 406 · tier 2

| Source file | Kind | Lines |
|---|---|---|
| `src/gui/ColourSchemeContainer.h` | C++ | 280 |
| `src/gui/ColourSchemeContainer.cc` | C++ | 277 |

## Overview

`ColourSchemeContainer` is the registry of every `ColourScheme` the application knows about, keyed by an `id_type` and grouped into one of the `ColourSchemeCategory::Type` buckets (`PLATE_ID`, `SINGLE_COLOUR`, `FEATURE_AGE`, `FEATURE_TYPE`). Its constructor populates the container with GPlates' built-in schemes via `create_built_in_colour_schemes`, and callers such as the colouring dialog add, remove or edit further entries (`add`, `remove`, `add_single_colour_scheme`, `edit_single_colour_scheme`) as the user creates custom schemes at runtime. `ColourSchemeCategory::Iterator` and its free `begin()`/`end()` let code range over the category enum itself, separately from `ColourSchemeContainer::iterator`, which ranges over the `ColourSchemeInfo` entries within one category.

As the header states directly, this container only tracks what colour schemes exist; it has no notion of which one is currently selected in the GUI. That responsibility, and the `colour_scheme_edited` signal's consumption, belongs to `ColourSchemeDelegator`, which this class is deliberately decoupled from.

## Declared types

| Name | Kind | Bases | Template | Subclasses | Description |
|---|---|---|---|---|---|
| [`GPlatesGui::ColourSchemeCategory::Type`](#gplatesguicolourschemecategorytype) | enum | — | — | 0 | The different categories that colour schemes can fall into. |
| [`GPlatesGui::ColourSchemeCategory::Iterator`](#gplatesguicolourschemecategoryiterator) | class | — | — | 0 | — |
| [`GPlatesGui::ColourSchemeContainer`](#gplatesguicolourschemecontainer) | class | `QObject` | — | 0 | ColourSchemeContainer is a container that stores all loaded colour schemes. |

## Members

### `GPlatesGui::ColourSchemeCategory::Type`

| Member | Kind | Type | Access | Description |
|---|---|---|---|---|
| `PLATE_ID` | enumerator | `None` | — | — |
| `SINGLE_COLOUR` | enumerator | `None` | — | — |
| `FEATURE_AGE` | enumerator | `None` | — | — |
| `FEATURE_TYPE` | enumerator | `None` | — | — |
| `NUM_CATEGORIES` | enumerator | `None` | — | — |

### `GPlatesGui::ColourSchemeCategory::Iterator`

| Member | Kind | Type | Access | Description |
|---|---|---|---|---|
| `iterator_category` | alias | `std::input_iterator_tag` | public | Iterator typedefs. |
| `value_type` | alias | `Type` | public | — |
| `difference_type` | alias | `std::ptrdiff_t` | public | — |
| `pointer` | alias | `Type *` | public | — |
| `reference` | alias | `Type &` | public | — |
| `Iterator( Type curr)` | constructor | `None` | public | — |
| `operator->()` | operator | `Type` | public | — |
| `operator++(int)` | operator | `Iterator` | public | — |
| `operator==( const Iterator &other)` | operator | `bool` | public | — |
| `d_curr` | field | `Type` | private | — |

### `GPlatesGui::ColourSchemeContainer`

| Member | Kind | Type | Access | Description |
|---|---|---|---|---|
| `id_type` | typedef | `size_t` | public | The type of an ID that uniquely identifies a colour scheme loaded into this ColourSchemeContainer. |
| `container_type` | typedef | `std::map<id_type, ColourSchemeInfo>` | public | The type of the underlying container that holds all of the colour schemes in a particular category. |
| `iterator` | typedef | `container_type::const_iterator` | public | The type of an iterator over the container of ColourSchemeInfo objects for a particular category. |
| `ColourSchemeContainer( GPlatesAppLogic::ApplicationState &application_state)` | constructor | `None` | public | Constructor. |
| `begin( ColourSchemeCategory::Type category)` | method | `iterator` | public | Returns a 'begin' iterator over the colour schemes in category. |
| `end( ColourSchemeCategory::Type category)` | method | `iterator` | public | Returns an 'end' iterator over the colour schemes in category. |
| `add( ColourSchemeCategory::Type category, const ColourSchemeInfo &colour_scheme)` | method | `id_type` | public | Adds colour\_scheme to category. |
| `remove( ColourSchemeCategory::Type category, id_type id)` | method | `void` | public | Removes the colour scheme with the given id in category. |
| `get` | field | `ColourSchemeInfo` | public | Returns the colour scheme with the given id in category. |
| `add_single_colour_scheme( const Colour &colour, const QString &colour_name, bool is_built_in = true)` | method | `id_type` | public | Adds a colour scheme to the category Single Colour. |
| `edit_single_colour_scheme( id_type id, const Colour &colour, const QString &colour_name)` | method | `void` | public | Changes the Single Colour scheme with given id to colour. |
| `colour_scheme_edited( GPlatesGui::ColourSchemeCategory::Type, GPlatesGui::ColourSchemeContainer::id_type)` | method | `void` | public | — |
| `create_built_in_colour_schemes( GPlatesAppLogic::ApplicationState &application_state)` | method | `void` | private | Creates the built-in colour schemes and places them into the categories. |
| `create_single_colour_scheme( const Colour &colour, const QString &colour_name, bool is_built_in)` | method | `ColourSchemeInfo` | private | — |
| `d_next_id` | field | `id_type` | private | Remembers the next id to be given out to a ColourSchemeInfo when inserted. |
| `d_colour_schemes` | field | `container_type` | private | Stores the loaded colour schemes, sorted into categories. |

## Free functions and macros

| Name | Kind | Type / body | Description |
|---|---|---|---|
| `GPLATES_GUI_COLOURSCHEMECONTAINER_H` | macro | `None` | — |
| `begin()` | function | `Iterator` | Returns a 'begin' iterator over the colour scheme category enums. |
| `end()` | function | `Iterator` | Returns an 'end' iterator over the colour scheme category enums. |
| `get_description( Type category)` | function | `QString` | Returns a human-readable description for the given category. |

## Notes

- `get` has undefined behaviour if passed an `id` that was never returned by `add`/`add_single_colour_scheme` for that `category`, or that has since been `remove`d — there is no bounds or existence check.
- Ids are assigned from a single monotonically increasing `d_next_id` shared across all categories, so ids are unique container-wide, not just within a category.

## Used by

| Unit | Component | References |
|---|---|---|
| [qt-widgets/ColouringDialog](../qt-widgets/ColouringDialog.md) | qt-widgets | 78 |
| [gui/ColourSchemeDelegator](ColourSchemeDelegator.md) | gui | 40 |
| [presentation/ViewState](../presentation/ViewState.md) | presentation | 5 |
| [qt-widgets/ViewportWindow](../qt-widgets/ViewportWindow.md) | qt-widgets | 1 |

## Related

*None.*

## Explore

Run these from the `gplates-code` skill directory:

```bash
python scripts/gpq.py file src/gui/ColourSchemeContainer.h
python scripts/gpq.py def GPlatesGui::ColourSchemeContainer --body
python scripts/gpq.py uses ColourSchemeContainer --kind class
python scripts/gpq.py hier ColourSchemeContainer
```
