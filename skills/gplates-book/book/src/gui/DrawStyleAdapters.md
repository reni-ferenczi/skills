# DrawStyleAdapters

[Book TOC](../../TOC.md) · [gui](../../components/gui.md) · cluster Community 354 · tier 2

| Source file | Kind | Lines |
|---|---|---|
| `src/gui/DrawStyleAdapters.h` | C++ | 257 |
| `src/gui/DrawStyleAdapters.cc` | C++ | 298 |

## Overview

`StyleAdapter` is the abstract base of the "draw style" system: given a `GPlatesModel::FeatureHandle::weak_ref`, `get_style()` returns a `DrawStyle` (currently just a `Colour`) to render that feature with, and each `StyleAdapter` carries a name, a `StyleCategory`, and a `Configuration` of user-adjustable settings. Two concrete adapters implement this. `ColourStyleAdapter` wraps a `boost::shared_ptr<const ColourScheme>` and exists, per its own comment, purely for backward compatibility with the older colouring-scheme mechanism it supersedes. `PythonStyleAdapter` is the general case: it wraps a Python object (`d_py_obj`) implementing a `get_style(feature, draw_style)`/`get_config()`/`set_config()` protocol, letting user-supplied Python draw-style scripts plug into the same interface as built-in C++ styles. `init_configuration()` parses the Python object's `get_config()` dict (keys of the form `"name/subkey"`) into `Configuration`/`ConfigurationItem` objects via `create_cfg_item()`, dispatching on a `"type"` entry (`Color`, `Palette`, else plain string) to the matching `PythonCfgItem` subclass from `PythonConfiguration.h`; `update_cfg()` pushes edited C++-side configuration back into the Python object before each `get_style()` call, but only when `d_cfg_dirty` is set.

`register_alternative_draw_styles()` lets a Python style optionally declare a `get_config_variants()` dict of named preset configurations; for each one it deep-clones the adapter (spawning a fresh Python object via `copy.deepcopy`), applies the variant's settings, and registers the clone with `DrawStyleManager` as a separate style in the same category — this is how a single Python script can appear in the styles list as several ready-made presets.

## Declared types

| Name | Kind | Bases | Template | Subclasses | Description |
|---|---|---|---|---|---|
| [`GPlatesGui::DrawStyle`](#gplatesguidrawstyle) | struct | — | — | 0 | — |
| [`GPlatesGui::StyleAdapter`](#gplatesguistyleadapter) | class | — | — | 2 | — |
| [`GPlatesGui::PythonStyleAdapter`](#gplatesguipythonstyleadapter) | class | [`StyleAdapter`](DrawStyleAdapters.md) | — | 0 | — |
| [`GPlatesGui::ColourStyleAdapter`](#gplatesguicolourstyleadapter) | class | [`StyleAdapter`](DrawStyleAdapters.md) | — | 0 | This class is here for historical reason. |

## Members

### `GPlatesGui::DrawStyle`

| Member | Kind | Type | Access | Description |
|---|---|---|---|---|
| `DrawStyle()` | constructor | `None` | public | — |
| `colour` | field | `Colour` | public | — |

### `GPlatesGui::StyleAdapter`

| Member | Kind | Type | Access | Description |
|---|---|---|---|---|
| `StyleAdapter(const StyleCategory& cata)` | constructor | `None` | public | — |
| `get_style( GPlatesModel::FeatureHandle::weak_ref f)` | method | `DrawStyle` | public | — |
| `set_dirty_flag( bool flag)` | method | `void` | public | — |
| `set_name(const QString& str)` | method | `void` | public | — |
| `deep_clone()` | method | `StyleAdapter` | public | — |
| `~StyleAdapter()` | destructor | `None` | public | — |
| `operator==( const StyleAdapter& other)` | operator | `bool` | public | — |
| `d_catagory` | field | `StyleCategory` | protected | — |
| `d_id` | field | `unsigned` | protected | — |
| `d_name` | field | `QString` | protected | — |
| `d_cfg_dirty` | field | `bool` | protected | — |
| `d_cfg` | field | `Configuration` | protected | — |

### `GPlatesGui::PythonStyleAdapter`

| Member | Kind | Type | Access | Description |
|---|---|---|---|---|
| `PythonStyleAdapter( bp::object& obj, const StyleCategory& cata)` | constructor | `None` | public | — |
| `get_style( GPlatesModel::FeatureHandle::weak_ref f)` | method | `DrawStyle` | public | — |
| `deep_clone()` | method | `StyleAdapter` | public | — |
| `register_alternative_draw_styles( DrawStyleManager& dsm)` | method | `void` | public | Query the Python class for a dict-of-dicts representing a set of alternative configuration values, then instantiate additional StyleAdapters and register them with the DrawStyleManager as variants within the same category as this ... |
| `~PythonStyleAdapter()` | destructor | `None` | public | — |
| `populate_py_dict( boost::python::dict& cfgs)` | method | `void` | protected | This function creates python configuration objects from C++ Configuration object. |
| `init_configuration()` | method | `void` | protected | Read python configuration information from python script and create empty Configuration items. |
| `update_cfg()` | method | `void` | protected | Push the configuration data back to python object. |
| `create_cfg_item( const std::map<QString, QString>& data)` | method | `PythonCfgItem` | protected | Create configuration items according to the config definition map. |
| `d_py_obj` | field | `bp::object` | private | — |

### `GPlatesGui::ColourStyleAdapter`

| Member | Kind | Type | Access | Description |
|---|---|---|---|---|
| `ColourStyleAdapter( boost::shared_ptr<const ColourScheme> scheme, const StyleCategory& cata, const QString s_name = QString())` | constructor | `None` | public | — |
| `get_style( GPlatesModel::FeatureHandle::weak_ref f)` | method | `DrawStyle` | public | — |
| `deep_clone()` | method | `StyleAdapter` | public | — |
| `d_scheme` | field | `boost::shared_ptr<const ColourScheme>` | private | — |

## Free functions and macros

| Name | Kind | Type / body | Description |
|---|---|---|---|
| `GPLATES_GUI_DRAWSTYLEADAPTERS_H` | macro | `None` | — |

## Notes

Every call into `d_py_obj` acquires a `GPlatesApi::PythonInterpreterLocker` (the GIL) first, including in the destructor, which deliberately locks before dropping GPlates' reference to the wrapped Python object so its destruction happens under the GIL. Python exceptions from the wrapped object are always caught as `boost::python::error_already_set` and logged with `qWarning()` rather than propagated — a broken user draw-style script degrades to a default-constructed `DrawStyle` instead of crashing or aborting the render. `d_cfg_dirty` is `mutable` so that `get_style() const` can lazily call `update_cfg()` the first time it is needed after a configuration edit, and `StyleAdapter::operator==` compares only `d_id`, which `DrawStyleManager` (a `friend`) is responsible for assigning uniquely — two independently constructed adapters are never equal until registered.

## Used by

| Unit | Component | References |
|---|---|---|
| [gui/DrawStyleManager](DrawStyleManager.md) | gui | 60 |
| [qt-widgets/DrawStyleDialog](../qt-widgets/DrawStyleDialog.md) | qt-widgets | 49 |
| [presentation/TranscribeSession](../presentation/TranscribeSession.md) | presentation | 20 |
| [api/PyApplication](../api/PyApplication.md) | api | 11 |
| [gui/PythonConfiguration](PythonConfiguration.md) | gui | 6 |
| [presentation/ReconstructionGeometryRenderer](../presentation/ReconstructionGeometryRenderer.md) | presentation | 6 |
| [api/PyColour](../api/PyColour.md) | api | 4 |
| [presentation/VisualLayerRegistry](../presentation/VisualLayerRegistry.md) | presentation | 2 |
| [entry-points/gplates_main](../entry-points/gplates_main.md) | entry-points | 1 |
| [presentation/ReconstructVisualLayerParams](../presentation/ReconstructVisualLayerParams.md) | presentation | 1 |
| [presentation/TopologyGeometryVisualLayerParams](../presentation/TopologyGeometryVisualLayerParams.md) | presentation | 1 |
| [presentation/TopologyNetworkVisualLayerParams](../presentation/TopologyNetworkVisualLayerParams.md) | presentation | 1 |
| [presentation/VisualLayer](../presentation/VisualLayer.md) | presentation | 1 |
| [presentation/VisualLayers](../presentation/VisualLayers.md) | presentation | 1 |

## Related

*None.*

## Explore

Run these from the `gplates-code` skill directory:

```bash
python scripts/gpq.py file src/gui/DrawStyleAdapters.h
python scripts/gpq.py def GPlatesGui::StyleAdapter --body
python scripts/gpq.py uses StyleAdapter --kind class
python scripts/gpq.py hier StyleAdapter
```
