# DrawStyleManager

[Book TOC](../../TOC.md) · [gui](../../components/gui.md) · cluster Community 258 · tier 2

| Source file | Kind | Lines |
|---|---|---|
| `src/gui/DrawStyleManager.h` | C++ | 296 |
| `src/gui/DrawStyleManager.cc` | C++ | 449 |

## Overview

`DrawStyleManager` is a singleton (`instance()`) registry of every `StyleAdapter` and `StyleCategory` in the application, and the central place layers look up how a feature should be drawn. On construction it registers the four built-in categories ("PlateId", "SingleColour", "FeatureAge", "FeatureType"); each `StyleAdapter`/`StyleCategory` is given a monotonically increasing `d_id`, offset by `BUILT_IN_OFFSET` (`0x80000000`) when `built_in` is true, which is how `is_built_in_style()` and `remove_style()` distinguish protected built-in styles from user-created ones without a separate flag. `d_reference_map` counts how many layers currently reference each style (`increase_ref()`/`decrease_ref()`), which `can_be_removed()` and `remove_style()` consult so an in-use or built-in style cannot be deleted out from under a layer.

Styles are persisted per-category under the `draw_styles/user-defined` preferences prefix via `save_user_defined_styles()`/`get_saved_styles()`, serialising each style's `Configuration` through a `GPlatesUtils::ConfigBundle`; a category's "template" style — the clean, unconfigured adapter registered with `register_template_style()` — is what `get_saved_styles()` and `get_built_in_styles()` deep-clone to reconstruct each saved or preset variant, since a `StyleAdapter` wrapping a Python object cannot be default-constructed generically. `get_built_in_styles()` hard-codes the built-in preset variants for the C++-defined categories (a fixed palette of colour names for `SingleColour`, named `ColourPalette` presets for `PlateId`/`FeatureAge`/`FeatureType`); Python-defined styles instead supply their own presets through `PythonStyleAdapter::register_alternative_draw_styles()`, as the comment at the end of `get_built_in_styles()` explains.

## Declared types

| Name | Kind | Bases | Template | Subclasses | Description |
|---|---|---|---|---|---|
| [`GPlatesGui::StyleCategory`](#gplatesguistylecategory) | class | — | — | 0 | — |
| [`GPlatesGui::DrawStyleManager`](#gplatesguidrawstylemanager) | class | `QObject`<br>`boost::noncopyable` | — | 0 | — |

## Members

### `GPlatesGui::StyleCategory`

| Member | Kind | Type | Access | Description |
|---|---|---|---|---|
| `operator==(const StyleCategory& other)` | operator | `bool` | public | — |
| `StyleCategory( const QString& name_ = QString(), const QString& desc_ = QString())` | constructor | `None` | private | — |
| `d_id` | field | `unsigned` | private | — |
| `d_name` | field | `QString` | private | — |
| `d_desc` | field | `QString` | private | — |

### `GPlatesGui::DrawStyleManager`

| Member | Kind | Type | Access | Description |
|---|---|---|---|---|
| `StyleContainer` | typedef | `std::vector<StyleAdapter*>` | public | — |
| `CatagoryContainer` | typedef | `std::vector<StyleCategory*>` | public | — |
| `instance()` | method | `DrawStyleManager` | public | — |
| `is_alive()` | method | `bool` | public | This function is not so elegant. |
| `register_style( StyleAdapter* sa, bool built_in = false)` | method | `void` | public | — |
| `is_built_in_style(const StyleAdapter& style)` | method | `bool` | public | — |
| `can_be_removed(const StyleAdapter& style)` | method | `bool` | public | — |
| `remove_style(StyleAdapter* style)` | method | `bool` | public | — |
| `get_ref_number(const StyleAdapter& style)` | method | `unsigned` | public | Get the number of how many layers are referencing this style. |
| `increase_ref(const StyleAdapter& style)` | method | `void` | public | — |
| `decrease_ref(const StyleAdapter& style)` | method | `void` | public | — |
| `register_template_style( const StyleCategory* cata, const StyleAdapter* adapter)` | method | `void` | public | Since the style object contains a boost python object, it is necessary to "deep copy" the python object when cloning StyleAdapter. |
| `get_saved_styles( const StyleCategory& cata)` | method | `std::vector<StyleAdapter*>` | public | Get all user defined styles. |
| `get_built_in_styles( const StyleCategory& cata)` | method | `std::vector<StyleAdapter*>` | public | Get all built-in styles. |
| `get_template_style( const StyleCategory& cata)` | method | `StyleAdapter` | public | — |
| `default_style()` | method | `StyleAdapter` | public | — |
| `register_style_catagory( const QString& name, const QString& desc = QString(), bool built_in = false)` | method | `StyleCategory` | public | — |
| `~DrawStyleManager()` | destructor | `None` | public | — |
| `emit_style_changed()` | method | `void` | public | — |
| `get_styles(const StyleCategory& cata)` | method | `StyleContainer` | public | — |
| `get_catagory(const QString& _name)` | method | `StyleCategory` | public | — |
| `save_user_defined_styles()` | method | `void` | public | — |
| `draw_style_changed()` | method | `void` | public | — |
| `clear_container(ContainerType& container)` | method | `void` | protected | — |
| `DrawStyleManager(bool local_user_pref=true)` | constructor | `None` | private | — |
| `DrawStyleManager(const DrawStyleManager&)` | constructor | `None` | private | — |
| `d_styles` | field | `StyleContainer` | private | — |
| `d_catagories` | field | `CatagoryContainer` | private | — |
| `d_next_cata_id` | field | `unsigned` | private | — |
| `d_next_style_id` | field | `unsigned` | private | — |
| `BUILT_IN_OFFSET` | field | `unsigned` | private | — |
| `RefenceMap` | typedef | `std::map<const StyleAdapter*, unsigned>` | private | — |
| `TemplateMap` | typedef | `std::map<const StyleCategory*, const StyleAdapter*>` | private | — |
| `d_reference_map` | field | `RefenceMap` | private | — |
| `d_template_map` | field | `TemplateMap` | private | — |
| `draw_style_prefix` | field | `QString` | private | — |
| `d_user_prefs` | field | `GPlatesAppLogic::UserPreferences` | private | — |
| `d_values_map` | field | `GPlatesAppLogic::UserPreferences::KeyValueMap` | private | — |
| `d_default_style` | field | `GPlatesGui::StyleAdapter` | private | — |
| `d_alive_flag` | field | `bool` | private | — |
| `d_use_local_user_pref` | field | `bool` | private | — |

## Free functions and macros

| Name | Kind | Type / body | Description |
|---|---|---|---|
| `d_alive_flag` | variable | `bool` | — |
| `draw_style_prefix` | variable | `QString` | — |
| `create_built_in_palette_adapter( const QString& cfg_name, const QString& palette_name, const StyleAdapter* template_adapter)` | function | `StyleAdapter` | — |
| `GPLATES_GUI_DRAWSTYLEMANAGER_H` | macro | `None` | — |

## Notes

`instance()` leaks its singleton by design (`new DrawStyleManager()`, never deleted through that path); `is_alive()` exists solely so other code destructing during application teardown can check `DrawStyleManager` hasn't already been destroyed before touching it — a plain null check would not work since the pointer itself is never cleared. The destructor takes the Python GIL (`GPlatesApi::PythonInterpreterLocker`) before deleting any styles, because destroying a `PythonStyleAdapter` destroys a wrapped Python object; `remove_style()` does the same for single-style removal. `DrawStyleManager` owns `d_user_prefs` (a `GPlatesAppLogic::UserPreferences`) only when constructed with `local_user_pref = true`, the default and the path every production caller uses through `instance()`; the alternate constructor argument exists for tests that want to inject a shared `ApplicationState`'s preferences instead, and only that path frees `d_user_prefs` in the destructor. The class is `boost::noncopyable` and both constructors are private, so the only way to obtain one is `instance()`.

## Used by

| Unit | Component | References |
|---|---|---|
| [qt-widgets/DrawStyleDialog](../qt-widgets/DrawStyleDialog.md) | qt-widgets | 26 |
| [presentation/TranscribeSession](../presentation/TranscribeSession.md) | presentation | 22 |
| [api/PyApplication](../api/PyApplication.md) | api | 14 |
| [entry-points/gplates_main](../entry-points/gplates_main.md) | entry-points | 13 |
| [presentation/TopologyNetworkVisualLayerParams](../presentation/TopologyNetworkVisualLayerParams.md) | presentation | 4 |
| [presentation/ReconstructVisualLayerParams](../presentation/ReconstructVisualLayerParams.md) | presentation | 3 |
| [presentation/ReconstructionGeometryRenderer](../presentation/ReconstructionGeometryRenderer.md) | presentation | 3 |
| [presentation/TopologyGeometryVisualLayerParams](../presentation/TopologyGeometryVisualLayerParams.md) | presentation | 3 |
| [gui/DrawStyleAdapters](DrawStyleAdapters.md) | gui | 2 |
| [presentation/VisualLayerRegistry](../presentation/VisualLayerRegistry.md) | presentation | 2 |
| [presentation/VisualLayers](../presentation/VisualLayers.md) | presentation | 2 |
| [api/PyColour](../api/PyColour.md) | api | 1 |
| [gui/GeometryFocusHighlight](GeometryFocusHighlight.md) | gui | 1 |
| [gui/PythonConfiguration](PythonConfiguration.md) | gui | 1 |
| [qt-widgets/TopologyGeometryResolverLayerOptionsWidget](../qt-widgets/TopologyGeometryResolverLayerOptionsWidget.md) | qt-widgets | 1 |
| [qt-widgets/TopologyNetworkResolverLayerOptionsWidget](../qt-widgets/TopologyNetworkResolverLayerOptionsWidget.md) | qt-widgets | 1 |

## Related

*None.*

## Explore

Run these from the `gplates-code` skill directory:

```bash
python scripts/gpq.py file src/gui/DrawStyleManager.h
python scripts/gpq.py def GPlatesGui::DrawStyleManager --body
python scripts/gpq.py uses DrawStyleManager --kind class
python scripts/gpq.py hier DrawStyleManager
```
