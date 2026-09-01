# DrawStyleAdapters

[Book TOC](../../TOC.md) · [gui](../../components/gui.md) · cluster Community 354 · tier 2

| Source file | Kind | Lines |
|---|---|---|
| `src/gui/DrawStyleAdapters.h` | C++ | 257 |
| `src/gui/DrawStyleAdapters.cc` | C++ | 298 |

## Overview

[[[PROSE overview unit=gui/DrawStyleAdapters tier=2]]]
Replace this whole block, markers included, with 1-3 paragraphs: what this unit is, why it exists, and how it fits the surrounding design. Do not restate the tables below.
[[[/PROSE]]]

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

[[[PROSE notes unit=gui/DrawStyleAdapters tier=2]]]
Replace this whole block, markers included, with invariants, ownership, threading or gotchas that are not visible in the tables. Write *None.* if there is nothing worth saying.
[[[/PROSE]]]

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
