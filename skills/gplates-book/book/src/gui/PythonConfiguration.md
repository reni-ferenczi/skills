# PythonConfiguration

[Book TOC](../../TOC.md) · [gui](../../components/gui.md) · cluster Community 111 · tier 2

| Source file | Kind | Lines |
|---|---|---|
| `src/gui/PythonConfiguration.h` | C++ | 307 |
| `src/gui/PythonConfiguration.cc` | C++ | 130 |

## Overview

`PythonConfiguration` backs the named, typed configuration values that
drawing-style Python scripts expose to the GUI (see `gui/DrawStyleManager`,
`gui/DrawStyleAdapters`): a `Configuration` is a name-to-`ConfigurationItem*`
map with value semantics — copying or assigning it deep-clones every owned
item via `ConfigurationItem::clone()`, and `set()`/the destructor delete the
previous owner's item, so `Configuration` fully owns everything it holds.
`ConfigurationItem` itself is just a `QVariant` value with a virtual `clone()`;
`PythonCfgItem` extends it with a `boost::python::object` mirror
(`d_py_obj`) so the same configured value can be read from a Python drawing
script and edited from a Qt widget in the GUI.

The three concrete kinds mirror the argument types drawing scripts expose:
`PythonCfgColor` parses its `QVariant` as a colour name/hex string into a
`Colour` object; `PythonCfgPalette` treats its string value either as a
readable `.cpt` file path (parsed into a `CptPalette`) or, if not a file, as
the name of a built-in palette looked up via `built_in_palette()` (see
`gui/Palette`); `PythonCfgString` stores an arbitrary trimmed string. Each
`set_value()` rebuilds `d_py_obj` to keep the Python-visible value in sync
with the C++ one.

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

- `Configuration` owns its `ConfigurationItem*` values: `set()` deletes the
  previous item for a name before installing the new one, and the destructor
  deletes every item. Passing a raw pointer into `set()` transfers ownership
  to the `Configuration`.
- Every place that replaces or destroys `d_py_obj` — `PythonCfgItem`'s
  destructor, and `set_value()` on `PythonCfgColor`/`PythonCfgPalette`/
  `PythonCfgString` — first takes a `GPlatesApi::PythonInterpreterLocker`,
  because destroying a `boost::python::object` requires holding the Python
  GIL; skipping this when adding a new `PythonCfgItem` subclass would corrupt
  the interpreter state.
- `PythonCfgPalette::set_value()` distinguishes a CPT file from a built-in
  palette purely by `QFileInfo::isFile()`/`isReadable()`; if a `.cpt` file
  fails to parse, it catches `GPlatesGlobal::LogException`, logs it, and
  leaves `d_palette` null while `d_py_obj` still wraps a `GPlatesApi::Palette`
  around that null pointer (which `GPlatesApi::Palette::get_color()` handles
  by returning black).

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
