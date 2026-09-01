# DrawStyleManager

[Book TOC](../../TOC.md) · [gui](../../components/gui.md) · cluster Community 258 · tier 2

| Source file | Kind | Lines |
|---|---|---|
| `src/gui/DrawStyleManager.h` | C++ | 296 |
| `src/gui/DrawStyleManager.cc` | C++ | 449 |

## Overview

[[[PROSE overview unit=gui/DrawStyleManager tier=2]]]
Replace this whole block, markers included, with 1-3 paragraphs: what this unit is, why it exists, and how it fits the surrounding design. Do not restate the tables below.
[[[/PROSE]]]

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

[[[PROSE notes unit=gui/DrawStyleManager tier=2]]]
Replace this whole block, markers included, with invariants, ownership, threading or gotchas that are not visible in the tables. Write *None.* if there is nothing worth saying.
[[[/PROSE]]]

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
