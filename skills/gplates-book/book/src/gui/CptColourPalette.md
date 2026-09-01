# CptColourPalette

[Book TOC](../../TOC.md) · [gui](../../components/gui.md) · cluster Community 168 · tier 2

| Source file | Kind | Lines |
|---|---|---|
| `src/gui/CptColourPalette.h` | C++ | 1110 |
| `src/gui/CptColourPalette.cc` | C++ | 88 |

## Overview

This header implements GMT-style CPT (colour palette table) files as in-memory `ColourPalette<T>` subclasses. `CptColourPalette<EntryType>` is the shared base: it holds an ordered `std::vector<EntryType>` plus optional background, foreground and NaN colours, and `get_colour()` walks the entries linearly, falling back to background/foreground/NaN as appropriate. The template is instantiated two ways to cover the two CPT file variants described in the GMT documentation linked in the header: `RegularCptColourPalette` (`EntryType = ColourSlice`) interpolates a colour gradient between two real-valued bounds per row, while `CategoricalCptColourPalette<T>` (`EntryType = ColourEntry<T>`) maps discrete keys to flat colours, with a `T`-dependent specialisation of `ColourEntry` — a non-integral `T` compares by label, an integral `T` compares by an integer key — chosen via `boost::enable_if`/`disable_if` on `boost::is_integral<T>`.

The `CptColourPaletteInternals` and `CategoricalCptColourPaletteInternals` namespaces hold the compile-time-dispatched helpers (`MakeColourEntry`, `UseForegroundBackgroundColour`, `GetRange`, `AcceptVisitor`) that let the same `CategoricalCptColourPalette<T>` template behave correctly whether `T` is an integer key type (where background/foreground colours and a numeric range make sense) or an arbitrary label type (where they do not, and `accept_visitor()` only forwards to a `ColourPaletteVisitor` for the two integer specialisations, `boost::int32_t` and `boost::uint32_t`, that the visitor interface actually supports). `ColourScaleAnnotation::Type` and its `GPlatesUtils::Parse` specialisation exist to parse the `A`/`L`/`U`/`B` annotation flags GMT uses to mark which end of a colour-scale slice should be labelled when rendered.

## Declared types

| Name | Kind | Bases | Template | Subclasses | Description |
|---|---|---|---|---|---|
| [`GPlatesGui::ColourScaleAnnotation::Type`](#gplatesguicolourscaleannotationtype) | enum | — | — | 0 | — |
| [`GPlatesUtils::Parse<GPlatesGui::ColourScaleAnnotation::Type>`](#gplatesutilsparsegplatesguicolourscaleannotationtype) | struct | — | `<>` | 0 | Specialisation of Parse for ColourScaleAnnotation::Type. |
| [`GPlatesGui::ColourModel::Type`](#gplatesguicolourmodeltype) | enum | — | — | 0 | — |
| [`GPlatesGui::ColourSlice`](#gplatesguicolourslice) | class | — | — | 0 | A colour slice specifies a gradient of colour between two real values. |
| [`GPlatesGui::ColourEntry<T, typename boost::disable_if<boost::is_integral<T> >::type>`](#gplatesguicolourentryt-typename-boostdisable_ifboostis_integralt-type) | class | — | `<typename T>` | 0 | In the version of ColourEntry for non-ints, the label is used as the value that is mapped to the colour. |
| [`GPlatesGui::ColourEntry<IntType, typename boost::enable_if<boost::is_integral<IntType> >::type>`](#gplatesguicolourentryinttype-typename-boostenable_ifboostis_integralinttype-type) | class | — | `<typename IntType>` | 0 | In the specialisation of ColourEntry for int, the integer key is used as the value that is mapped to the colour, and the label is used as a text label for rendering purposes. |
| [`GPlatesGui::CptColourPaletteInternals::MakeColourEntry<T, typename boost::disable_if<boost::is_integral<T> >::type>`](#gplatesguicptcolourpaletteinternalsmakecolourentryt-typename-boostdisable_ifboostis_integralt-type) | class | — | `<typename T>` | 0 | — |
| [`GPlatesGui::CptColourPaletteInternals::MakeColourEntry<IntType, typename boost::enable_if<boost::is_integral<IntType> >::type>`](#gplatesguicptcolourpaletteinternalsmakecolourentryinttype-typename-boostenable_ifboostis_integralinttype-type) | class | — | `<typename IntType>` | 0 | — |
| [`GPlatesGui::CptColourPalette`](#gplatesguicptcolourpalette) | class | [`ColourPalette<typename EntryType::value_type>`](ColourPalette.md) | `<class EntryType>` | 2 | CptColourPalette stores the in-memory representation of a CPT file, whether regular or categorical. |
| [`GPlatesGui::RegularCptColourPalette`](#gplatesguiregularcptcolourpalette) | class | [`CptColourPalette<ColourSlice>`](CptColourPalette.md) | — | 0 | A colour palette that stores entries from a regular CPT file. |
| [`GPlatesGui::CategoricalCptColourPaletteInternals::UseForegroundBackgroundColour<T, typename boost::enable_if<boost::is_integral<T> >::type>`](#gplatesguicategoricalcptcolourpaletteinternalsuseforegroundbackgroundcolourt-typename-boostenable_ifboostis_integralt-type) | struct | — | `<typename T>` | 0 | — |
| [`GPlatesGui::CategoricalCptColourPaletteInternals::UseForegroundBackgroundColour<T, typename boost::disable_if<boost::is_integral<T> >::type>`](#gplatesguicategoricalcptcolourpaletteinternalsuseforegroundbackgroundcolourt-typename-boostdisable_ifboostis_integralt-type) | struct | — | `<typename T>` | 0 | — |
| [`GPlatesGui::CategoricalCptColourPaletteInternals::GetRange<T, typename boost::enable_if<boost::is_integral<T> >::type>`](#gplatesguicategoricalcptcolourpaletteinternalsgetranget-typename-boostenable_ifboostis_integralt-type) | struct | — | `<typename T>` | 0 | — |
| [`GPlatesGui::CategoricalCptColourPaletteInternals::GetRange<T, typename boost::disable_if<boost::is_integral<T> >::type>`](#gplatesguicategoricalcptcolourpaletteinternalsgetranget-typename-boostdisable_ifboostis_integralt-type) | struct | — | `<typename T>` | 0 | — |
| [`GPlatesGui::CategoricalCptColourPaletteInternals::AcceptVisitor`](#gplatesguicategoricalcptcolourpaletteinternalsacceptvisitor) | struct | — | `<typename T>` | 0 | This exists because this class is visitable only for certain template parameters T. |
| [`GPlatesGui::CategoricalCptColourPaletteInternals::AcceptVisitor<boost::int32_t>`](#gplatesguicategoricalcptcolourpaletteinternalsacceptvisitorboostint32_t) | struct | — | `<>` | 0 | — |
| [`GPlatesGui::CategoricalCptColourPaletteInternals::AcceptVisitor<boost::uint32_t>`](#gplatesguicategoricalcptcolourpaletteinternalsacceptvisitorboostuint32_t) | struct | — | `<>` | 0 | — |
| [`GPlatesGui::CategoricalCptColourPalette`](#gplatesguicategoricalcptcolourpalette) | class | [`CptColourPalette<ColourEntry<T> >`](CptColourPalette.md) | `<typename T>` | 0 | A colour palette that stores entries from a categorical CPT file. |

## Members

### `GPlatesGui::ColourScaleAnnotation::Type`

| Member | Kind | Type | Access | Description |
|---|---|---|---|---|
| `NONE` | enumerator | `None` | — | — |
| `LOWER` | enumerator | `None` | — | — |
| `UPPER` | enumerator | `None` | — | — |
| `BOTH` | enumerator | `None` | — | — |

### `GPlatesUtils::Parse<GPlatesGui::ColourScaleAnnotation::Type>`

| Member | Kind | Type | Access | Description |
|---|---|---|---|---|
| `operator()( const QString &s)` | operator | `GPlatesGui::ColourScaleAnnotation::Type` | public | — |

### `GPlatesGui::ColourModel::Type`

| Member | Kind | Type | Access | Description |
|---|---|---|---|---|
| `RGB` | enumerator | `None` | — | — |
| `HSV` | enumerator | `None` | — | — |
| `CMYK` | enumerator | `None` | — | — |

### `GPlatesGui::ColourSlice`

| Member | Kind | Type | Access | Description |
|---|---|---|---|---|
| `value_type` | typedef | `GPlatesMaths::Real` | public | — |
| `ColourSlice( value_type lower_value_, boost::optional<Colour> lower_colour_, value_type upper_value_, boost::optional<Colour> upper_colour_, ColourScaleAnnotation::Type annotation_ = ColourScaleAnnotation::NONE, boost::optional<QString> label_ = boost::none)` | constructor | `None` | public | — |
| `can_handle( value_type value)` | method | `bool` | public | — |
| `get_colour( value_type value)` | method | `boost::optional<Colour>` | public | — |
| `lower_value()` | method | `value_type` | public | — |
| `set_lower_value( value_type lower_value_)` | method | `void` | public | — |
| `upper_value()` | method | `value_type` | public | — |
| `set_upper_value( value_type upper_value_)` | method | `void` | public | — |
| `set_lower_colour( const boost::optional<Colour> &lower_colour_)` | method | `void` | public | — |
| `set_upper_colour( const boost::optional<Colour> &upper_colour_)` | method | `void` | public | — |
| `annotation()` | method | `ColourScaleAnnotation::Type` | public | — |
| `set_annotation( ColourScaleAnnotation::Type annotation_)` | method | `void` | public | — |
| `set_label( const boost::optional<QString> &label_)` | method | `void` | public | — |
| `d_lower_value` | field | `value_type` | private | — |
| `d_upper_value` | field | `value_type` | private | — |
| `d_inverse_value_range` | field | `value_type` | private | — |
| `d_lower_colour` | field | `boost::optional<Colour>` | private | — |
| `d_upper_colour` | field | `boost::optional<Colour>` | private | — |
| `d_annotation` | field | `ColourScaleAnnotation::Type` | private | — |
| `d_label` | field | `boost::optional<QString>` | private | — |
| `set_inverse_value_range()` | method | `void` | private | — |

### `GPlatesGui::ColourEntry<T, typename boost::disable_if<boost::is_integral<T> >::type>`

| Member | Kind | Type | Access | Description |
|---|---|---|---|---|
| `value_type` | typedef | `T` | public | — |
| `(anonymous enum)` | enum | `None` | public | — |
| `ColourEntry( int key_, Colour colour_, const T &label_)` | method | `None` | public | — |
| `can_handle( const T &value)` | method | `bool` | public | — |
| `key()` | method | `int` | public | — |
| `set_key( int key_)` | method | `void` | public | — |
| `set_colour( const Colour &colour_)` | method | `void` | public | — |
| `set_label( const T &label_)` | method | `void` | public | — |
| `d_key` | field | `int` | private | — |
| `d_colour` | field | `Colour` | private | — |
| `d_label` | field | `T` | private | — |

### `GPlatesGui::ColourEntry<IntType, typename boost::enable_if<boost::is_integral<IntType> >::type>`

| Member | Kind | Type | Access | Description |
|---|---|---|---|---|
| `value_type` | typedef | `IntType` | public | — |
| `(anonymous enum)` | enum | `None` | public | — |
| `ColourEntry( IntType key_, Colour colour_, const boost::optional<QString> &label_)` | method | `None` | public | — |
| `can_handle( IntType value)` | method | `bool` | public | — |
| `key()` | method | `IntType` | public | — |
| `set_key( IntType key_)` | method | `void` | public | — |
| `set_colour( const Colour &colour_)` | method | `void` | public | — |
| `set_label( const boost::optional<QString> &label_)` | method | `void` | public | — |
| `d_key` | field | `IntType` | private | — |
| `d_colour` | field | `Colour` | private | — |
| `d_label` | field | `boost::optional<QString>` | private | — |

### `GPlatesGui::CptColourPaletteInternals::MakeColourEntry<T, typename boost::disable_if<boost::is_integral<T> >::type>`

| Member | Kind | Type | Access | Description |
|---|---|---|---|---|
| `key_type` | typedef | `int` | public | — |
| `make_colour_entry( int key, const Colour &colour, const boost::optional<QString> &label)` | method | `ColourEntry<T>` | public | — |

### `GPlatesGui::CptColourPaletteInternals::MakeColourEntry<IntType, typename boost::enable_if<boost::is_integral<IntType> >::type>`

| Member | Kind | Type | Access | Description |
|---|---|---|---|---|
| `key_type` | typedef | `IntType` | public | — |
| `make_colour_entry( IntType key, const Colour &colour, const boost::optional<QString> &label)` | method | `ColourEntry<IntType>` | public | — |

### `GPlatesGui::CptColourPalette`

| Member | Kind | Type | Access | Description |
|---|---|---|---|---|
| `value_type` | typedef | `typename ColourPalette<typename EntryType::value_type>::value_type` | public | — |
| `add_entry( const EntryType &entry)` | method | `void` | public | Adds an entry to the colour palette. |
| `set_background_colour( const Colour &colour)` | method | `void` | public | Sets the background colour, used for values that go before the first entry. |
| `get_background_colour()` | method | `boost::optional<Colour>` | public | Returns the background colour. |
| `set_foreground_colour( const Colour &colour)` | method | `void` | public | Sets the foreground colour, used for values that go after the last entry. |
| `get_foreground_colour()` | method | `boost::optional<Colour>` | public | Returns the foreground colour. |
| `set_nan_colour( const Colour &colour)` | method | `void` | public | Sets the NaN colour, used for values that are: - NaN - not present, and - values not covered by entries in the CPT file or the background/ foreground colours. |
| `get_nan_colour()` | method | `boost::optional<Colour>` | public | Returns the NaN colour. |
| `set_colour_model( ColourModel::Type colour_model)` | method | `void` | public | For regular CPT files, this sets whether space-separated colour components are interpreted as RGB, HSV or CMTK (for both colour slices and FBN lines). |
| `get_colour_model()` | method | `ColourModel::Type` | public | set\_colour\_model(). |
| `get_colour( value_type value)` | method | `boost::optional<Colour>` | public | Retrieves a Colour based on the value given. |
| `size()` | method | `size_t` | public | — |
| `CptColourPalette()` | constructor | `None` | protected | — |
| `use_background_colour( value_type value)` | method | `bool` | protected | — |
| `use_foreground_colour( value_type value)` | method | `bool` | protected | — |
| `d_entries` | field | `std::vector<EntryType>` | protected | — |
| `d_background_colour` | field | `boost::optional<Colour>` | private | — |
| `d_foreground_colour` | field | `boost::optional<Colour>` | private | — |
| `d_nan_colour` | field | `boost::optional<Colour>` | private | — |
| `d_colour_model` | field | `ColourModel::Type` | private | Colour model as specified in CPT file. |

### `GPlatesGui::RegularCptColourPalette`

| Member | Kind | Type | Access | Description |
|---|---|---|---|---|
| `this_type` | typedef | `RegularCptColourPalette` | public | — |
| `non_null_ptr_type` | typedef | `GPlatesUtils::non_null_intrusive_ptr<this_type>` | public | — |
| `non_null_ptr_to_const_type` | typedef | `GPlatesUtils::non_null_intrusive_ptr<const this_type>` | public | — |
| `maybe_null_ptr_type` | typedef | `boost::intrusive_ptr<this_type>` | public | — |
| `maybe_null_ptr_to_const_type` | typedef | `boost::intrusive_ptr<const this_type>` | public | — |
| `create()` | method | `non_null_ptr_type` | public | — |
| `accept_visitor( ConstColourPaletteVisitor &visitor)` | method | `void` | public | — |
| `accept_visitor( ColourPaletteVisitor &visitor)` | method | `void` | public | — |
| `get_range()` | method | `boost::optional< std::pair<GPlatesMaths::Real, GPlatesMaths::Real> >` | public | Returns none if there are no colour slices (size returns zero). |
| `use_background_colour( value_type value)` | method | `bool` | protected | — |
| `use_foreground_colour( value_type value)` | method | `bool` | protected | — |
| `RegularCptColourPalette()` | constructor | `None` | private | — |

### `GPlatesGui::CategoricalCptColourPaletteInternals::UseForegroundBackgroundColour<T, typename boost::enable_if<boost::is_integral<T> >::type>`

| Member | Kind | Type | Access | Description |
|---|---|---|---|---|
| `use_background_colour( const std::vector<ColourEntry<T> > &entries, ValueType value)` | method | `bool` | public | — |
| `use_foreground_colour( const std::vector<ColourEntry<T> > &entries, ValueType value)` | method | `bool` | public | — |

### `GPlatesGui::CategoricalCptColourPaletteInternals::UseForegroundBackgroundColour<T, typename boost::disable_if<boost::is_integral<T> >::type>`

| Member | Kind | Type | Access | Description |
|---|---|---|---|---|
| `use_background_colour( const std::vector<ColourEntry<T> > &entries, ValueType value)` | method | `bool` | public | — |
| `use_foreground_colour( const std::vector<ColourEntry<T> > &entries, ValueType value)` | method | `bool` | public | — |

### `GPlatesGui::CategoricalCptColourPaletteInternals::GetRange<T, typename boost::enable_if<boost::is_integral<T> >::type>`

| Member | Kind | Type | Access | Description |
|---|---|---|---|---|
| `get_range( const std::vector<EntryType> &entries)` | method | `boost::optional< std::pair<T, T> >` | public | — |

### `GPlatesGui::CategoricalCptColourPaletteInternals::GetRange<T, typename boost::disable_if<boost::is_integral<T> >::type>`

| Member | Kind | Type | Access | Description |
|---|---|---|---|---|
| `get_range( const std::vector<EntryType> &entries)` | method | `boost::optional< std::pair<T, T> >` | public | — |

### `GPlatesGui::CategoricalCptColourPaletteInternals::AcceptVisitor`

| Member | Kind | Type | Access | Description |
|---|---|---|---|---|
| `do_accept_visitor( ConstColourPaletteVisitor &visitor, const CategoricalCptColourPalette<T> &colour_palette)` | method | `void` | public | — |
| `do_accept_visitor( ColourPaletteVisitor &visitor, CategoricalCptColourPalette<T> &colour_palette)` | method | `void` | public | — |

### `GPlatesGui::CategoricalCptColourPaletteInternals::AcceptVisitor<boost::int32_t>`

| Member | Kind | Type | Access | Description |
|---|---|---|---|---|
| `do_accept_visitor( ConstColourPaletteVisitor &visitor, const CategoricalCptColourPalette<boost::int32_t> &colour_palette)` | method | `void` | public | — |
| `do_accept_visitor( ColourPaletteVisitor &visitor, CategoricalCptColourPalette<boost::int32_t> &colour_palette)` | method | `void` | public | — |

### `GPlatesGui::CategoricalCptColourPaletteInternals::AcceptVisitor<boost::uint32_t>`

| Member | Kind | Type | Access | Description |
|---|---|---|---|---|
| `do_accept_visitor( ConstColourPaletteVisitor &visitor, const CategoricalCptColourPalette<boost::uint32_t> &colour_palette)` | method | `void` | public | — |
| `do_accept_visitor( ColourPaletteVisitor &visitor, CategoricalCptColourPalette<boost::uint32_t> &colour_palette)` | method | `void` | public | — |

### `GPlatesGui::CategoricalCptColourPalette`

| Member | Kind | Type | Access | Description |
|---|---|---|---|---|
| `base_type` | typedef | `CptColourPalette<ColourEntry<T> >` | private | — |
| `this_type` | typedef | `CategoricalCptColourPalette<T>` | public | — |
| `non_null_ptr_type` | typedef | `GPlatesUtils::non_null_intrusive_ptr<this_type>` | public | — |
| `non_null_ptr_to_const_type` | typedef | `GPlatesUtils::non_null_intrusive_ptr<const this_type>` | public | — |
| `maybe_null_ptr_type` | typedef | `boost::intrusive_ptr<this_type>` | public | — |
| `maybe_null_ptr_to_const_type` | typedef | `boost::intrusive_ptr<const this_type>` | public | — |
| `value_type` | typedef | `typename base_type::value_type` | public | — |
| `create()` | method | `non_null_ptr_type` | public | — |
| `accept_visitor( ConstColourPaletteVisitor &visitor)` | method | `void` | public | — |
| `accept_visitor( ColourPaletteVisitor &visitor)` | method | `void` | public | — |
| `get_range()` | method | `boost::optional< std::pair<T, T> >` | public | Returns the range covered by this colour palette. |
| `CategoricalCptColourPalette()` | constructor | `None` | protected | — |
| `use_background_colour( value_type value)` | method | `bool` | protected | — |
| `use_foreground_colour( value_type value)` | method | `bool` | protected | — |

## Free functions and macros

| Name | Kind | Type / body | Description |
|---|---|---|---|
| `operator<( ColourSlice::value_type value, const ColourSlice &colour_slice)` | operator | `bool` | — |
| `operator>( ColourSlice::value_type value, const ColourSlice &colour_slice)` | operator | `bool` | — |
| `GPLATES_GUI_CPTCOLOURPALETTE_H` | macro | `None` | — |
| `operator<( typename boost::enable_if<boost::is_integral<IntType>, IntType>::type value, const ColourEntry<IntType> &colour_entry)` | operator | `bool` | — |
| `operator>( typename boost::enable_if<boost::is_integral<IntType>, IntType>::type value, const ColourEntry<IntType> &colour_entry)` | operator | `bool` | — |
| `make_colour_entry( typename CptColourPaletteInternals::MakeColourEntry<T>::key_type key, const Colour &colour, const boost::optional<QString> &label)` | function | `ColourEntry<T>` | — |

## Notes

`add_entry()` requires entries to be appended in increasing order for regular CPT files and for categorical files with an integer value type — `use_background_colour()`/`use_foreground_colour()` and `get_colour()`'s linear scan both assume sorted, non-overlapping entries and give wrong answers silently if that invariant is violated. `ColourSlice::can_handle()` and the foreground/background comparisons deliberately avoid epsilon comparisons on floating-point values, trading strict correctness at slice boundaries for speed when classifying millions of raster pixels. For categorical palettes whose value type is not integral, background, foreground and range queries are unconditionally disabled (`GetRange` returns `boost::none`, `UseForegroundBackgroundColour` always returns `false`) because label values have no defined order. `CptColourPalette` is reference-counted through `GPlatesUtils::non_null_intrusive_ptr` (via `RegularCptColourPalette`/`CategoricalCptColourPalette`'s `create()` factories and private constructors) rather than being constructed directly.

## Used by

| Unit | Component | References |
|---|---|---|
| [gui/BuiltinColourPalettes](BuiltinColourPalettes.md) | gui | 69 |
| [file-io/CptReader](../file-io/CptReader.md) | file-io | 25 |
| [gui/ColourPaletteRangeRemapper](ColourPaletteRangeRemapper.md) | gui | 19 |
| [presentation/ViewState](../presentation/ViewState.md) | presentation | 5 |
| [qt-widgets/ColourScaleWidget](../qt-widgets/ColourScaleWidget.md) | qt-widgets | 2 |
| [gui/ColourPaletteUtils](ColourPaletteUtils.md) | gui | 1 |
| [gui/ColourScaleGenerator](ColourScaleGenerator.md) | gui | 1 |
| [presentation/TranscribeSession](../presentation/TranscribeSession.md) | presentation | 1 |
| [qt-widgets/ColouringDialog](../qt-widgets/ColouringDialog.md) | qt-widgets | 1 |
| [qt-widgets/RasterLayerOptionsWidget](../qt-widgets/RasterLayerOptionsWidget.md) | qt-widgets | 1 |
| [qt-widgets/ReconstructScalarCoverageLayerOptionsWidget](../qt-widgets/ReconstructScalarCoverageLayerOptionsWidget.md) | qt-widgets | 1 |

## Related

*None.*

## Explore

Run these from the `gplates-code` skill directory:

```bash
python scripts/gpq.py file src/gui/CptColourPalette.h
python scripts/gpq.py def GPlatesGui::CptColourPalette --body
python scripts/gpq.py uses CptColourPalette --kind class
python scripts/gpq.py hier CptColourPalette
```
