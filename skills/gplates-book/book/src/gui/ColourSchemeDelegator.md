# ColourSchemeDelegator

[Book TOC](../../TOC.md) · [gui](../../components/gui.md) · cluster Community 630 · tier 2

| Source file | Kind | Lines |
|---|---|---|
| `src/gui/ColourSchemeDelegator.h` | C++ | 183 |
| `src/gui/ColourSchemeDelegator.cc` | C++ | 270 |

## Overview

`ColourSchemeDelegator` is itself a `ColourScheme`, but rather than deciding colours directly it forwards each `get_colour` call to whichever scheme is currently active, looked up by `colour_scheme_handle` (a category/id pair) in a `ColourSchemeContainer`. This indirection is the reason `ColourScheme` clients — the globe and map renderers, `ReconstructionGeometryRenderer`, and so on — hold a single stable reference for the lifetime of the session even as the user switches colouring schemes or edits one in the colouring dialog; only `d_global_colour_scheme` (or an entry in `d_special_colour_schemes`) changes underneath them, via `set_colour_scheme`.

Colouring can be overridden per feature collection: `set_colour_scheme` with a `feature_collection` argument records a special scheme for just that collection in `d_special_colour_schemes`, while `get_colour` resolves a `ReconstructionGeometry` back to its owning `FeatureCollectionHandle` (via `get_feature_collection_from_reconstruction_geometry`) and falls back to `d_global_colour_scheme` when no override is set. The anonymous-namespace `WeakReferenceRemover`, a `WeakReferenceCallback` on the feature collection, keeps that map from accumulating stale entries by erasing its own entry automatically once the feature collection it refers to is deactivated. `ColourSchemeDelegator` also listens for the container's `colour_scheme_edited` signal and re-emits its own `changed()` to tell renderers that previously rendered colours are now stale.

## Declared types

| Name | Kind | Bases | Template | Subclasses | Description |
|---|---|---|---|---|---|
| [`(anonymous)::WeakReferenceRemover`](#anonymousweakreferenceremover) | class | [`GPlatesModel::WeakReferenceCallback<const GPlatesModel::FeatureCollectionHandle>`](../model/WeakReferenceCallback.md) | — | 0 | Removes a weak reference from the special colour schemes map automatically when the feature collection that it points to gets deactivated. |
| [`GPlatesGui::ColourSchemeDelegator`](#gplatesguicolourschemedelegator) | class | `QObject`<br>[`ColourScheme`](ColourScheme.md) | — | 0 | Keeps track of changing target colour schemes - allows switching of the actual colour scheme implementation without having to change reference(s) to it (just refer to ColourTableDelegator instead). |

## Members

### `(anonymous)::WeakReferenceRemover`

| Member | Kind | Type | Access | Description |
|---|---|---|---|---|
| `map_type` | typedef | `GPlatesGui::ColourSchemeDelegator::colour_schemes_map_type` | public | — |
| `iterator_type` | typedef | `map_type::iterator` | public | — |
| `WeakReferenceRemover( map_type &map, iterator_type element)` | constructor | `None` | public | — |
| `publisher_deactivated( const weak_reference_type &reference, const deactivated_event_type &event)` | method | `void` | public | — |
| `d_map` | field | `map_type` | private | — |
| `d_element` | field | `iterator_type` | private | — |

### `GPlatesGui::ColourSchemeDelegator`

| Member | Kind | Type | Access | Description |
|---|---|---|---|---|
| `non_null_ptr_type` | typedef | `GPlatesUtils::non_null_intrusive_ptr<ColourSchemeDelegator>` | public | Convenience typedef for GPlatesUtils::non\_null\_intrusive\_ptr\<ColourSchemeDelegator\>. |
| `non_null_ptr_to_const_type` | typedef | `GPlatesUtils::non_null_intrusive_ptr<const ColourSchemeDelegator>` | public | Convenience typedef for GPlatesUtils::non\_null\_intrusive\_ptr\<const ColourSchemeDelegator\>. |
| `colour_scheme_handle` | typedef | `std::pair<ColourSchemeCategory::Type, ColourSchemeContainer::id_type>` | public | Holds the category and id of a colour scheme together. |
| `colour_schemes_map_type` | typedef | `std::map<GPlatesModel::FeatureCollectionHandle::const_weak_ref, colour_scheme_handle>` | public | The type of the map from feature collection to colour scheme. |
| `ColourSchemeDelegator( const ColourSchemeContainer &colour_scheme_container)` | constructor | `None` | public | Constructor. |
| `set_colour_scheme( ColourSchemeCategory::Type category, ColourSchemeContainer::id_type id, GPlatesModel::FeatureCollectionHandle::const_weak_ref feature_collection = GPlatesModel::FeatureCollectionHandle::const_weak_ref())` | method | `void` | public | Changes the colour scheme for the given feature\_collection to the one with the given id in the given category. |
| `unset_colour_scheme( GPlatesModel::FeatureCollectionHandle::const_weak_ref feature_collection)` | method | `void` | public | Unsets the colour scheme for the given feature\_collection, if that feature collection has a special colour scheme set. |
| `get_colour_scheme( GPlatesModel::FeatureCollectionHandle::const_weak_ref feature_collection = GPlatesModel::FeatureCollectionHandle::const_weak_ref())` | method | `boost::optional<colour_scheme_handle>` | public | Gets the colour scheme for feature\_collection. |
| `get_colour( const GPlatesAppLogic::ReconstructionGeometry &reconstruction_geometry)` | method | `boost::optional<Colour>` | public | Retrieves a colour for a reconstruction\_geometry from the current colour scheme. |
| `get_colour( const GPlatesModel::FeatureHandle& feature)` | method | `boost::optional<Colour>` | public | — |
| `changed()` | method | `void` | public | — |
| `handle_colour_scheme_edited( GPlatesGui::ColourSchemeCategory::Type category, GPlatesGui::ColourSchemeContainer::id_type id)` | method | `void` | private | — |
| `apply_colour_scheme( const colour_scheme_handle &colour_scheme, const GPlatesAppLogic::ReconstructionGeometry &reconstruction_geometry)` | method | `boost::optional<Colour>` | private | Applies the colour\_scheme to the reconstruction\_geometry. |
| `d_colour_scheme_container` | field | `ColourSchemeContainer` | private | Stores all loaded colour schemes, sorted by category. |
| `d_global_colour_scheme` | field | `colour_scheme_handle` | private | The colour scheme to be used by all feature collections for which there is no special colour scheme. |
| `d_special_colour_schemes` | field | `colour_schemes_map_type` | private | A map of feature collection to colour scheme, for those feature collections that have a special colour scheme. |

## Free functions and macros

| Name | Kind | Type / body | Description |
|---|---|---|---|
| `get_feature_collection_from_reconstruction_geometry( const GPlatesAppLogic::ReconstructionGeometry &reconstruction_geometry)` | function | `GPlatesModel::FeatureCollectionHandle` | Returns the feature collection that holds the feature from which the reconstruction\_geometry was created. |
| `GPLATES_GUI_COLOURSCHEMEDELEGATOR_H` | macro | `None` | — |

## Notes

- `d_colour_scheme_container` is stored as a reference, not owned; the `ColourSchemeContainer` passed to the constructor must outlive the `ColourSchemeDelegator`.
- The `FeatureHandle` overload of `get_colour` is an unfinished stub (`//TODO:`) that unconditionally returns `boost::none`; only the `ReconstructionGeometry` overload is implemented.
- Entries in `d_special_colour_schemes` are removed automatically via `WeakReferenceRemover` when their feature collection is deactivated, so callers must not assume an override set with `set_colour_scheme` persists once that collection is unloaded.

## Used by

| Unit | Component | References |
|---|---|---|
| [qt-widgets/ColouringDialog](../qt-widgets/ColouringDialog.md) | qt-widgets | 28 |
| [presentation/ViewState](../presentation/ViewState.md) | presentation | 8 |
| [qt-widgets/ViewportWindow](../qt-widgets/ViewportWindow.md) | qt-widgets | 1 |

## Related

**Qt signal/slot connections** (1 in this unit)

| Sender | Signal | Receiver | Slot |
|---|---|---|---|
| `&d_colour_scheme_container` | `colour_scheme_edited( GPlatesGui::ColourSchemeCategory::Type, GPlatesGui::ColourSchemeContainer::id_type)` | `this` | `handle_colour_scheme_edited( GPlatesGui::ColourSchemeCategory::Type, GPlatesGui::ColourSchemeContainer::id_type)` |


## Explore

Run these from the `gplates-code` skill directory:

```bash
python scripts/gpq.py file src/gui/ColourSchemeDelegator.h
python scripts/gpq.py def GPlatesGui::ColourSchemeDelegator --body
python scripts/gpq.py uses ColourSchemeDelegator --kind class
python scripts/gpq.py hier ColourSchemeDelegator
```
