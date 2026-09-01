# Palette

[Book TOC](../../TOC.md) · [gui](../../components/gui.md) · cluster Community 886 · tier 2

| Source file | Kind | Lines |
|---|---|---|
| `src/gui/Palette.h` | C++ | 592 |
| `src/gui/Palette.cc` | C++ | 302 |

## Overview

`Palette` is an older, simpler colour-lookup hierarchy distinct from
`GPlatesGui::ColourPalette` (see `gui/ColourPalette`) — it is keyed by a
`Palette::Key`, a `boost::variant<long, double, QString>` wrapper with
visitor-based conversions (`to_long()`, `to_double()`, `to_qstring()`) and a
comparison operator that falls back to numeric or, failing that, string
comparison when two keys hold different variant alternatives. Three lookup
strategies subclass it: `CategoricalPalette` maps discrete keys to colours
through `d_color_map`, `RegularPalette` interpolates a numeric key through a
sequence of `ColourSpectrum` ranges tried in order, and `SingleColorPalette`
always returns one fixed colour. `Palette` itself carries a
background/foreground/default ("BFN") colour triple returned by
`get_BFN_colour()`, used when a lookup fails to find a match.

`DefaultPlateIdPalette`, `RegionalPlateIdPalette` and `FeatureTypePalette` are
`CategoricalPalette` singletons (Meyers' pattern via a function-local `static`
pointer, never destroyed) with hard-coded colour tables built once in
`build_map()`; `RegionalPlateIdPalette` additionally overrides `get_colour()`
to derive a plate's region from the leading digit of its plate ID
(`get_region_from_plate_id()`) and vary the colour's HSV value by the plate ID
modulo 13, so plates sharing a region get visually distinct shades.
`CptPalette` parses a GMT `.cpt` colour-palette file via
`GPlatesFileIO::CptReader`, routing its categorical entries into an internal
`CategoricalPalette` and its ranged entries into an internal `RegularPalette`,
trying the categorical one first in `get_colour()`. `built_in_palette()` is
the name-keyed registry (`"DefaultPlateId"`, `"Region"`, `"FeatureAgeDefault"`,
`"FeatureAgeMono"`, `"FeatureType"`, `"DeaultPalette"` — note the typo is in
the actual key string) that GUI code looks palettes up by name from.
`GPlatesApi::Palette` is a thin, non-owning wrapper exposing a `Palette*` to
Python bindings, falling back to the default colour or black when the
wrapped pointer is null or the key has no match.

## Declared types

| Name | Kind | Bases | Template | Subclasses | Description |
|---|---|---|---|---|---|
| [`GPlatesGui::Palette`](#gplatesguipalette) | class | — | — | 7 | — |
| [`GPlatesGui::CategoricalPalette`](#gplatesguicategoricalpalette) | class | [`Palette`](Palette.md) | — | 3 | — |
| [`GPlatesGui::RegularPalette`](#gplatesguiregularpalette) | class | [`Palette`](Palette.md) | — | 0 | — |
| [`GPlatesGui::SingleColorPalette`](#gplatesguisinglecolorpalette) | class | [`Palette`](Palette.md) | — | 0 | — |
| [`GPlatesGui::DefaultPlateIdPalette`](#gplatesguidefaultplateidpalette) | class | [`CategoricalPalette`](Palette.md) | — | 0 | — |
| [`GPlatesGui::RegionalPlateIdPalette`](#gplatesguiregionalplateidpalette) | class | [`CategoricalPalette`](Palette.md) | — | 0 | — |
| [`GPlatesGui::FeatureTypePalette`](#gplatesguifeaturetypepalette) | class | [`CategoricalPalette`](Palette.md) | — | 0 | — |
| [`GPlatesGui::CptPalette`](#gplatesguicptpalette) | class | [`Palette`](Palette.md) | — | 0 | — |
| [`GPlatesApi::Palette`](#gplatesapipalette) | class | — | — | 0 | — |

## Members

### `GPlatesGui::Palette`

| Member | Kind | Type | Access | Description |
|---|---|---|---|---|
| `KeyType` | typedef | `boost::variant< long, double , QString>` | private | — |
| `Key` | class | `None` | public | — |
| `~Palette()` | destructor | `None` | public | — |
| `get_colour(const Key& k)` | method | `boost::optional<Colour>` | public | — |
| `set_BFN_colour( const Colour& b, const Colour& f, const Colour& n)` | method | `void` | public | — |
| `get_BFN_colour()` | method | `boost::tuple<Colour, Colour, Colour>` | public | Get background, foreground and NaN(default) color. |
| `Palette()` | constructor | `None` | protected | — |
| `d_background_color` | field | `Colour` | protected | — |
| `d_foreground_color` | field | `Colour` | protected | — |
| `d_default_color` | field | `Colour` | protected | — |

### `GPlatesGui::CategoricalPalette`

| Member | Kind | Type | Access | Description |
|---|---|---|---|---|
| `ColourMapType` | typedef | `std::map<const Palette::Key, Colour>` | public | — |
| `CategoricalPalette()` | constructor | `None` | public | — |
| `CategoricalPalette(const ColourMapType& map)` | constructor | `None` | public | — |
| `insert( const Palette::Key& k, Colour c)` | method | `void` | public | — |
| `get_colour(const Key& k)` | method | `boost::optional<Colour>` | public | — |
| `~CategoricalPalette()` | destructor | `None` | public | — |
| `build_map()` | method | `void` | protected | — |
| `mapping_key(const Key& k)` | method | `Key` | protected | — |
| `d_color_map` | field | `std::map<const Palette::Key, Colour>` | protected | — |

### `GPlatesGui::RegularPalette`

| Member | Kind | Type | Access | Description |
|---|---|---|---|---|
| `RegularPalette(const std::vector<ColourSpectrum>& spectrums)` | constructor | `None` | public | — |
| `RegularPalette()` | constructor | `None` | public | — |
| `append(const ColourSpectrum& sp)` | method | `void` | public | — |
| `get_colour(const Key& k)` | method | `boost::optional<Colour>` | public | — |
| `~RegularPalette()` | destructor | `None` | public | — |
| `d_spectrums` | field | `std::vector<ColourSpectrum>` | protected | — |

### `GPlatesGui::SingleColorPalette`

| Member | Kind | Type | Access | Description |
|---|---|---|---|---|
| `SingleColorPalette(const Colour& c)` | constructor | `None` | public | — |
| `get_colour(const Key& k)` | method | `boost::optional<Colour>` | public | — |
| `~SingleColorPalette()` | destructor | `None` | public | — |
| `d_color` | field | `Colour` | protected | — |

### `GPlatesGui::DefaultPlateIdPalette`

| Member | Kind | Type | Access | Description |
|---|---|---|---|---|
| `instance()` | method | `DefaultPlateIdPalette` | public | — |
| `mapping_key(const Key& k)` | method | `Key` | public | — |
| `~DefaultPlateIdPalette()` | destructor | `None` | public | — |
| `build_map()` | method | `void` | protected | — |
| `DefaultPlateIdPalette()` | constructor | `None` | protected | — |
| `DefaultPlateIdPalette(const DefaultPlateIdPalette&)` | constructor | `None` | protected | — |

### `GPlatesGui::RegionalPlateIdPalette`

| Member | Kind | Type | Access | Description |
|---|---|---|---|---|
| `instance()` | method | `RegionalPlateIdPalette` | public | — |
| `get_colour(const Key& k)` | method | `boost::optional<Colour>` | public | — |
| `build_map()` | method | `void` | protected | — |
| `RegionalPlateIdPalette()` | constructor | `None` | protected | — |
| `RegionalPlateIdPalette(const RegionalPlateIdPalette&)` | constructor | `None` | protected | — |

### `GPlatesGui::FeatureTypePalette`

| Member | Kind | Type | Access | Description |
|---|---|---|---|---|
| `instance()` | method | `FeatureTypePalette` | public | — |
| `~FeatureTypePalette()` | destructor | `None` | public | — |
| `build_map()` | method | `void` | protected | — |
| `FeatureTypePalette()` | constructor | `None` | protected | — |
| `FeatureTypePalette(const FeatureTypePalette&)` | constructor | `None` | protected | — |

### `GPlatesGui::CptPalette`

| Member | Kind | Type | Access | Description |
|---|---|---|---|---|
| `CptPalette(const QString& file)` | constructor | `None` | public | — |
| `get_colour(const Key& k)` | method | `boost::optional<Colour>` | public | — |
| `d_cate_palette` | field | `boost::scoped_ptr<CategoricalPalette>` | private | — |
| `d_regular_palette` | field | `boost::scoped_ptr<RegularPalette>` | private | — |

### `GPlatesApi::Palette`

| Member | Kind | Type | Access | Description |
|---|---|---|---|---|
| `Palette( const GPlatesGui::Palette* p)` | constructor | `None` | public | — |
| `get_color(const GPlatesGui::Palette::Key k)` | method | `GPlatesGui::Colour` | public | — |
| `d_p` | field | `GPlatesGui::Palette` | private | — |

## Free functions and macros

| Name | Kind | Type / body | Description |
|---|---|---|---|
| `make_color(const CptParser::ColourData& data)` | function | `boost::optional<Colour>` | — |
| `GPLATES_GUI_PALETTE_H` | macro | `None` | — |
| `html_colour(const char *name)` | function | `GPlatesGui::Colour` | — |
| `leading_digit( GPlatesModel::integer_plate_id_type plate_id)` | function | `int` | — |
| `get_region_from_plate_id( GPlatesModel::integer_plate_id_type plate_id)` | function | `int` | — |
| `default_age_palette( const double upper = 450, const double lower = 0)` | function | `Palette` | — |
| `mono_age_palette( const double upper = 450, const double lower = 0)` | function | `Palette` | — |
| `default_palette()` | function | `GPlatesGui::Palette` | — |
| `init_built_in_pallette(std::map<QString, const Palette*>& palette_map)` | function | `bool` | — |
| `built_in_palette(const QString& name)` | function | `Palette` | — |

## Notes

- The built-in registry key for the default palette is spelled `"DeaultPalette"`
  in `init_built_in_pallette()` — code or config looking it up must reproduce
  that misspelling.
- `DefaultPlateIdPalette::instance()`, `RegionalPlateIdPalette::instance()` and
  `FeatureTypePalette::instance()` leak their singleton by design (`new` with
  no matching `delete`); they live for the process lifetime.
- `GPlatesApi::Palette::d_p` is a raw, non-owning pointer to a
  `GPlatesGui::Palette` the wrapper does not control the lifetime of — typically
  one of the leaked singletons or `default_age_palette()`/`mono_age_palette()`/
  `default_palette()`, which are themselves function-local `static` instances.
- `RegularPalette::get_colour()` returns the first spectrum that produces a
  colour, so overlapping spectrum ranges are resolved by insertion order via
  `append()`, not by any tie-breaking rule.

## Used by

| Unit | Component | References |
|---|---|---|
| [utils/KeyValueCache](../utils/KeyValueCache.md) | utils | 18 |
| [app-logic/ResolvedTriangulationNetwork](../app-logic/ResolvedTriangulationNetwork.md) | app-logic | 16 |
| [unit-test/CptPaletteTest](../unit-test/CptPaletteTest.md) | unit-test | 14 |
| [gui/PlateIdColourPalettes](PlateIdColourPalettes.md) | gui | 12 |
| [gui/GenericColourScheme](GenericColourScheme.md) | gui | 11 |
| [gui/PythonConfiguration](PythonConfiguration.md) | gui | 8 |
| [gui/ColourSchemeContainer](ColourSchemeContainer.md) | gui | 6 |
| [api/PyColour](../api/PyColour.md) | api | 5 |
| [gui/ColourPalette](ColourPalette.md) | gui | 4 |
| [gui/ColourPaletteRangeRemapper](ColourPaletteRangeRemapper.md) | gui | 4 |
| [app-logic/ResolvedTriangulationDelaunay2](../app-logic/ResolvedTriangulationDelaunay2.md) | app-logic | 3 |
| [presentation/VisualLayerRegistry](../presentation/VisualLayerRegistry.md) | presentation | 3 |
| [presentation/VisualLayers](../presentation/VisualLayers.md) | presentation | 3 |
| [qt-widgets/ColouringDialog](../qt-widgets/ColouringDialog.md) | qt-widgets | 3 |
| [gui/ColourScaleGenerator](ColourScaleGenerator.md) | gui | 2 |
| [app-logic/ResolvedTriangulationUtils](../app-logic/ResolvedTriangulationUtils.md) | app-logic | 1 |
| [gui/DrawStyleAdapters](DrawStyleAdapters.md) | gui | 1 |
| [gui/DrawStyleManager](DrawStyleManager.md) | gui | 1 |
| [presentation/ReconstructionGeometryRenderer](../presentation/ReconstructionGeometryRenderer.md) | presentation | 1 |
| [presentation/TranscribeSession](../presentation/TranscribeSession.md) | presentation | 1 |

## Related

*None.*

## Explore

Run these from the `gplates-code` skill directory:

```bash
python scripts/gpq.py file src/gui/Palette.h
python scripts/gpq.py def GPlatesGui::Palette --body
python scripts/gpq.py uses Palette --kind class
python scripts/gpq.py hier Palette
```
