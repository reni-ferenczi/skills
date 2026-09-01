# PythonConfiguration

[Book TOC](../../TOC.md) · [gui](../../components/gui.md) · cluster Community 111 · tier 2

| Source file | Kind | Lines |
|---|---|---|
| `src/gui/PythonConfiguration.h` | C++ | 307 |
| `src/gui/PythonConfiguration.cc` | C++ | 130 |

## Overview

[[[PROSE overview unit=gui/PythonConfiguration tier=2]]]
Replace this whole block, markers included, with 1-3 paragraphs: what this unit is, why it exists, and how it fits the surrounding design. Do not restate the tables below.
[[[/PROSE]]]

## Declared types

| Name | Kind | Bases | Template | Subclasses | Description |
|---|---|---|---|---|---|
| [`GPlatesGui::ConfigurationItem`](#gplatesguiconfigurationitem) | class | — | — | 4 | — |
| [`GPlatesGui::Configuration`](#gplatesguiconfiguration) | class | — | — | 0 | — |
| [`GPlatesGui::PythonCfgItem`](#gplatesguipythoncfgitem) | class | [`ConfigurationItem`](PythonConfiguration.md) | — | 3 | — |
| [`GPlatesGui::PythonCfgColor`](#gplatesguipythoncfgcolor) | class | [`PythonCfgItem`](PythonConfiguration.md) | — | 0 | — |
| [`GPlatesGui::PythonCfgPalette`](#gplatesguipythoncfgpalette) | class | [`PythonCfgItem`](PythonConfiguration.md) | — | 0 | — |
| [`GPlatesGui::PythonCfgString`](#gplatesguipythoncfgstring) | class | [`PythonCfgItem`](PythonConfiguration.md) | — | 0 | — |

## Members

### `GPlatesGui::ConfigurationItem`

| Member | Kind | Type | Access | Description |
|---|---|---|---|---|
| `ConfigurationItem( const QVariant& v)` | constructor | `None` | public | — |
| `ConfigurationItem()` | constructor | `None` | public | — |
| `set_value( const QVariant& v)` | method | `void` | public | — |
| `clone()` | method | `ConfigurationItem` | public | — |
| `~ConfigurationItem()` | destructor | `None` | public | — |
| `d_value` | field | `QVariant` | protected | — |

### `GPlatesGui::Configuration`

| Member | Kind | Type | Access | Description |
|---|---|---|---|---|
| `Configuration()` | constructor | `None` | public | — |
| `get( const QString& name)` | method | `ConfigurationItem` | public | — |
| `set( const QString& name, ConfigurationItem* new_item)` | method | `void` | public | — |
| `all_cfg_item_names()` | method | `std::vector<QString>` | public | — |
| `Configuration( const Configuration& rhs)` | constructor | `None` | public | — |
| `~Configuration()` | destructor | `None` | public | — |
| `CfgItemMap` | typedef | `std::map<QString, ConfigurationItem*>` | protected | — |
| `d_items` | field | `CfgItemMap` | protected | — |

### `GPlatesGui::PythonCfgItem`

| Member | Kind | Type | Access | Description |
|---|---|---|---|---|
| `PythonCfgItem()` | constructor | `None` | public | — |
| `py_object()` | method | `boost::python::object` | public | — |
| `get_value()` | method | `QString` | public | — |
| `clone()` | method | `PythonCfgItem` | public | — |
| `~PythonCfgItem()` | destructor | `None` | public | — |
| `d_py_obj` | field | `boost::python::object` | protected | — |

### `GPlatesGui::PythonCfgColor`

| Member | Kind | Type | Access | Description |
|---|---|---|---|---|
| `PythonCfgColor( const QString& cfg_name, const QString& color_name)` | constructor | `None` | public | — |
| `PythonCfgColor( const QString& cfg_name, const Colour& color)` | constructor | `None` | public | — |
| `set_value( const QVariant& value)` | method | `void` | public | — |
| `clone()` | method | `PythonCfgColor` | public | — |

### `GPlatesGui::PythonCfgPalette`

| Member | Kind | Type | Access | Description |
|---|---|---|---|---|
| `PythonCfgPalette( const QString& cfg_name, const QString& palette_name)` | constructor | `None` | public | — |
| `PythonCfgPalette( const QString& cfg_name, const Palette* palette)` | constructor | `None` | public | — |
| `~PythonCfgPalette()` | destructor | `None` | public | — |
| `set_value( const QVariant& value)` | method | `void` | public | — |
| `clone()` | method | `PythonCfgPalette` | public | — |
| `is_built_in_palette()` | method | `bool` | public | Returns true if palette corresponds to one of the builtin types, otherwise should be a CPT filename. |
| `d_palette` | field | `boost::shared_ptr<Palette>` | private | — |

### `GPlatesGui::PythonCfgString`

| Member | Kind | Type | Access | Description |
|---|---|---|---|---|
| `PythonCfgString( const QString& cfg_name, const QString& str_value)` | constructor | `None` | public | — |
| `~PythonCfgString()` | destructor | `None` | public | — |
| `set_value( const QVariant& new_value)` | method | `void` | public | — |
| `clone()` | method | `PythonCfgString` | public | — |

## Free functions and macros

| Name | Kind | Type / body | Description |
|---|---|---|---|
| `GPLATES_GUI_PYTHON_CONFIGURATION_H` | macro | `None` | — |

## Notes

[[[PROSE notes unit=gui/PythonConfiguration tier=2]]]
Replace this whole block, markers included, with invariants, ownership, threading or gotchas that are not visible in the tables. Write *None.* if there is nothing worth saying.
[[[/PROSE]]]

## Used by

| Unit | Component | References |
|---|---|---|
| [presentation/ReconstructionGeometryRenderer](../presentation/ReconstructionGeometryRenderer.md) | presentation | 56 |
| [presentation/TranscribeSession](../presentation/TranscribeSession.md) | presentation | 38 |
| [qt-widgets/TopologyNetworkResolverLayerOptionsWidget](../qt-widgets/TopologyNetworkResolverLayerOptionsWidget.md) | qt-widgets | 32 |
| [qt-widgets/PythonArgumentWidget](../qt-widgets/PythonArgumentWidget.md) | qt-widgets | 21 |
| [gui/DrawStyleAdapters](DrawStyleAdapters.md) | gui | 18 |
| [qt-widgets/ModifyReconstructionPoleWidget](../qt-widgets/ModifyReconstructionPoleWidget.md) | qt-widgets | 15 |
| [gui/DrawStyleManager](DrawStyleManager.md) | gui | 13 |
| [qt-widgets/DrawStyleDialog](../qt-widgets/DrawStyleDialog.md) | qt-widgets | 11 |
| [qt-widgets/ReconstructLayerOptionsWidget](../qt-widgets/ReconstructLayerOptionsWidget.md) | qt-widgets | 8 |
| [qt-widgets/TopologyGeometryResolverLayerOptionsWidget](../qt-widgets/TopologyGeometryResolverLayerOptionsWidget.md) | qt-widgets | 4 |
| [gui/GeometryFocusHighlight](GeometryFocusHighlight.md) | gui | 3 |
| [presentation/VisualLayer](../presentation/VisualLayer.md) | presentation | 3 |
| [presentation/ReconstructVisualLayerParams](../presentation/ReconstructVisualLayerParams.md) | presentation | 2 |

## Related

*None.*

## Explore

Run these from the `gplates-code` skill directory:

```bash
python scripts/gpq.py file src/gui/PythonConfiguration.h
python scripts/gpq.py def GPlatesGui::Configuration --body
python scripts/gpq.py uses Configuration --kind class
python scripts/gpq.py hier Configuration
```
