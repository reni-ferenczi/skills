# GenericColourScheme

[Book TOC](../../TOC.md) · [gui](../../components/gui.md) · cluster Community 392 · tier 2

| Source file | Kind | Lines |
|---|---|---|
| `src/gui/GenericColourScheme.h` | C++ | 237 |

## Overview

`GenericColourScheme<PropertyExtractorType>` is the generic `ColourScheme` implementation used to build most per-property colouring modes: it delegates extracting a value from a `ReconstructionGeometry` or `FeatureHandle` to a `PropertyExtractorType` functor (which must be callable on either argument and typedef its result as `return_type`), then looks that value up in a `ColourPalette<PropertyExtractorType::return_type>` to produce the final `Colour`. `PROPERTY_NOT_FOUND_COLOUR` (grey) is returned when the extractor comes back empty, so a colour scheme built this way never fails outright — it degrades to a neutral colour instead. The free function `make_colour_scheme` is the usual way to build one, inferring `PropertyExtractorType` from the extractor argument and returning a `ColourScheme::non_null_ptr_type` for storage alongside other schemes.

`PlateIdScheme` and `FeatureAgeScheme` are older, non-template siblings predating the `GenericColourScheme`/`PropertyExtractor` pattern: they colour directly by reconstruction plate ID or by feature age against a `Palette`, with `FeatureAgeScheme` clamping ages outside its `[d_lower, d_upper]` range to the palette's background/foreground/NaN (BFN) colours instead of interpolating.

## Declared types

| Name | Kind | Bases | Template | Subclasses | Description |
|---|---|---|---|---|---|
| [`GPlatesGui::PlateIdScheme`](#gplatesguiplateidscheme) | class | [`ColourScheme`](ColourScheme.md) | — | 0 | — |
| [`GPlatesGui::FeatureAgeScheme`](#gplatesguifeatureagescheme) | class | [`ColourScheme`](ColourScheme.md) | — | 0 | — |
| [`GPlatesGui::GenericColourScheme`](#gplatesguigenericcolourscheme) | class | [`ColourScheme`](ColourScheme.md) | `<class PropertyExtractorType>` | 0 | GenericColourScheme takes a reconstruction geometry, extracts a property and maps that property to a colour using a colour palette. |

## Members

### `GPlatesGui::PlateIdScheme`

| Member | Kind | Type | Access | Description |
|---|---|---|---|---|
| `PlateIdScheme(const Palette* p)` | constructor | `None` | public | — |
| `get_colour( const GPlatesAppLogic::ReconstructionGeometry &reconstruction_geometry)` | method | `boost::optional<Colour>` | public | — |
| `get_colour( const GPlatesModel::FeatureHandle& feature)` | method | `boost::optional<Colour>` | public | — |
| `get_colour(boost::optional<GPlatesModel::integer_plate_id_type> id)` | method | `boost::optional<Colour>` | protected | — |
| `d_palette` | field | `Palette` | protected | — |

### `GPlatesGui::FeatureAgeScheme`

| Member | Kind | Type | Access | Description |
|---|---|---|---|---|
| `d_upper` | field | `double` | private | — |
| `d_lower` | field | `double` | private | — |
| `FeatureAgeScheme( const Palette* (*fun) (const double, const double), const double upper = 450.0, const double lower = 0.0)` | constructor | `None` | public | — |
| `get_colour( const GPlatesAppLogic::ReconstructionGeometry &r)` | method | `boost::optional<Colour>` | public | — |
| `get_colour( const GPlatesModel::FeatureHandle& feature)` | method | `boost::optional<Colour>` | public | — |
| `get_colour(boost::optional<GPlatesMaths::Real> age)` | method | `boost::optional<Colour>` | protected | — |
| `d_palette` | field | `Palette` | protected | — |

### `GPlatesGui::GenericColourScheme`

| Member | Kind | Type | Access | Description |
|---|---|---|---|---|
| `ColourPaletteType` | typedef | `ColourPalette<typename PropertyExtractorType::return_type>` | private | — |
| `GenericColourScheme( typename ColourPaletteType::non_null_ptr_type colour_palette_ptr, const PropertyExtractorType &property_extractor)` | constructor | `None` | public | GenericColourScheme constructor pointer passes to this instance of GenericColourScheme; the memory pointed at by the pointer is deallocated when this instance is destructed. |
| `~GenericColourScheme()` | destructor | `None` | public | Destructor |
| `get_colour_t(const ArguType& argu)` | method | `boost::optional<Colour>` | public | Returns a colour for a particular reconstruction\_geometry, or boost::none if it does not have the necessary parameters or if the reconstruction geometry should not be drawn for some other reason |
| `get_colour( const GPlatesAppLogic::ReconstructionGeometry &reconstruction_geometry)` | method | `boost::optional<Colour>` | public | — |
| `get_colour( const GPlatesModel::FeatureHandle& feature)` | method | `boost::optional<Colour>` | public | — |
| `d_colour_palette_ptr` | field | `typename ColourPaletteType::non_null_ptr_type` | private | — |
| `d_property_extractor` | field | `PropertyExtractorType` | private | — |
| `PROPERTY_NOT_FOUND_COLOUR` | field | `Colour` | private | — |

## Free functions and macros

| Name | Kind | Type / body | Description |
|---|---|---|---|
| `GPLATES_GUI_GENERICCOLOURSCHEME_H` | macro | `None` | — |
| `PROPERTY_NOT_FOUND_COLOUR` | variable | `Colour` | — |
| `make_colour_scheme( ColourPalettePointerType colour_palette_ptr, const PropertyExtractorType &property_extractor)` | function | `ColourScheme::non_null_ptr_type` | — |

## Notes

- `GenericColourScheme` takes ownership of the `ColourPaletteType::non_null_ptr_type` passed to its constructor; the palette is destroyed along with the scheme.
- `PlateIdScheme` and `FeatureAgeScheme` store a raw, non-owning `const Palette *` — the caller is responsible for the palette's lifetime, unlike `GenericColourScheme`'s ownership of its `ColourPalette`.

## Used by

| Unit | Component | References |
|---|---|---|
| [gui/ColourScaleGenerator](ColourScaleGenerator.md) | gui | 8 |
| [gui/ColourSchemeContainer](ColourSchemeContainer.md) | gui | 6 |
| [gui/ColourRawRaster](ColourRawRaster.md) | gui | 3 |
| [file-io/RasterFileCacheFormat](../file-io/RasterFileCacheFormat.md) | file-io | 2 |
| [gui/ColourPaletteRangeRemapper](ColourPaletteRangeRemapper.md) | gui | 2 |
| [gui/DrawStyleManager](DrawStyleManager.md) | gui | 2 |
| [qt-widgets/ColouringDialog](../qt-widgets/ColouringDialog.md) | qt-widgets | 2 |

## Related

*None.*

## Explore

Run these from the `gplates-code` skill directory:

```bash
python scripts/gpq.py file src/gui/GenericColourScheme.h
python scripts/gpq.py def GPlatesGui::GenericColourScheme --body
python scripts/gpq.py uses GenericColourScheme --kind class
python scripts/gpq.py hier GenericColourScheme
```
