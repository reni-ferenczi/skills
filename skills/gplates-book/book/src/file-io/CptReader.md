# CptReader

[Book TOC](../../TOC.md) · [file-io](../../components/file-io.md) · cluster Community 324 · tier 1

| Source file | Kind | Lines |
|---|---|---|
| `src/file-io/CptReader.h` | C++ | 1722 |
| `src/file-io/CptReader.cc` | C++ | 901 |

## Overview

This unit reads GMT colour palette table (`.cpt`) files, the format GPlates accepts for user-supplied colouring of rasters, scalar fields, plate IDs and draw styles. It holds **two independent readers** that share nothing but the file format. The older one is the template family `CptReader<CptFileFormat>`, which populates a `GPlatesGui::RegularCptColourPalette` or `GPlatesGui::CategoricalCptColourPalette<T>` and reports problems through a `ReadErrorAccumulation`; it is what `GPlatesGui::ColourPaletteUtils::read_cpt_raster_colour_palette` and `ColouringDialog` use. The second is `CptParser`, marked in the `.cc` as the "new implementation of cpt reader": it does no colour construction at all, just decomposes the file into `ColourData` / `CategoricalEntry` / `RegularEntry` structs, and its only caller is `GPlatesGui::CptPalette` in `src/gui/Palette.cc`. Neither has replaced the other; if you are fixing a CPT parsing bug, first work out which of the two paths the user's file went through.

The template reader is built on two orthogonal traits axes, which is why `CptReaderInternals` is so large for a line-oriented format. A **file-format trait** (`RegularCptFileFormat`, `CategoricalCptFileFormat<T>`) supplies the palette type and the z-value type, so the read loop, `ParserState` and the error reporting are written once for both file varieties. A **colour specification** (`RGBColourSpecification`, `HSVTripletColourSpecification`, `GMTNameColourSpecification`, …) is a policy struct declaring a `components_type` `boost::tuple` plus a static `convert`; `parse_components` walks that tuple recursively, parsing each token into the tuple's element type through `GPlatesUtils::Parse<T>`. Adding a new colour syntax therefore means adding one struct and one entry to a dispatch chain, not touching the line loop.

Because CPT lines are not self-describing, the reader identifies them by **trial**: `TryProcessTokensImpl` runs an ordered short-circuiting `||` chain of candidate grammars, each of which returns `false` when the line is not of its shape. Order is load-bearing — the `COLOR_MODEL`-dependent space-separated forms are tried before the model-independent `R/G/B`, `H-S-V` and `C/M/Y/K` triplets, then GMT colour names, plain grey, the invisible `-` slice and finally the pattern fill that is deliberately rejected. `BadTokenException`, `BadComponentsException` and `PatternFillEncounteredException` exist only to unwind out of the deep recursive parse; every candidate swallows them in a `catch (...)` and reports failure by return value. `IntegerCptReader` applies the same trial-and-error idea one level up, to the file: it reads as regular first, and treats that as a real regular file only if at least one `ColourSlice` was produced (BFN lines alone parse under both grammars), otherwise re-reads as categorical. `ColourPaletteUtils::read_cpt_raster_colour_palette` reimplements that same decision independently, so a change to the heuristic needs to be made in both places.

## Declared types

| Name | Kind | Bases | Template | Subclasses | Description |
|---|---|---|---|---|---|
| [`GPlatesFileIO::CptReaderInternals::RegularCptFileFormat`](#gplatesfileiocptreaderinternalsregularcptfileformat) | struct | — | — | 0 | For use as template parameter to CptReader. |
| [`GPlatesFileIO::CptReaderInternals::CategoricalCptFileFormat`](#gplatesfileiocptreaderinternalscategoricalcptfileformat) | struct | — | `<typename T>` | 0 | For use as template parameter to CptReader. |
| [`GPlatesFileIO::CptReaderInternals::BadTokenException`](#gplatesfileiocptreaderinternalsbadtokenexception) | struct | — | — | 0 | — |
| [`GPlatesFileIO::CptReaderInternals::BadComponentsException`](#gplatesfileiocptreaderinternalsbadcomponentsexception) | struct | — | — | 0 | — |
| [`GPlatesFileIO::CptReaderInternals::PatternFillEncounteredException`](#gplatesfileiocptreaderinternalspatternfillencounteredexception) | struct | — | — | 0 | — |
| [`GPlatesFileIO::CptReaderInternals::LowestValue<double>`](#gplatesfileiocptreaderinternalslowestvaluedouble) | struct | — | `<>` | 0 | — |
| [`GPlatesFileIO::CptReaderInternals::LowestValue<int>`](#gplatesfileiocptreaderinternalslowestvalueint) | struct | — | `<>` | 0 | — |
| [`GPlatesFileIO::CptReaderInternals::BaseRGBColourSpecification`](#gplatesfileiocptreaderinternalsbasergbcolourspecification) | struct | — | `<int Base>` | 0 | — |
| [`GPlatesFileIO::CptReaderInternals::HexRGBColourSpecification`](#gplatesfileiocptreaderinternalshexrgbcolourspecification) | typedef | — | — | 0 | — |
| [`GPlatesFileIO::CptReaderInternals::RGBColourSpecification`](#gplatesfileiocptreaderinternalsrgbcolourspecification) | struct | — | — | 0 | — |
| [`GPlatesFileIO::CptReaderInternals::RGBTripletColourSpecification`](#gplatesfileiocptreaderinternalsrgbtripletcolourspecification) | struct | — | — | 0 | Parsed as "R/G/B" instead of "R G B". |
| [`GPlatesFileIO::CptReaderInternals::HSVColourSpecification`](#gplatesfileiocptreaderinternalshsvcolourspecification) | struct | — | — | 0 | — |
| [`GPlatesFileIO::CptReaderInternals::HSVTripletColourSpecification`](#gplatesfileiocptreaderinternalshsvtripletcolourspecification) | struct | — | — | 0 | Parsed as "H-S-V" instead of "H S V". |
| [`GPlatesFileIO::CptReaderInternals::CMYKColourSpecification`](#gplatesfileiocptreaderinternalscmykcolourspecification) | struct | — | — | 0 | — |
| [`GPlatesFileIO::CptReaderInternals::CMYKTripletColourSpecification`](#gplatesfileiocptreaderinternalscmyktripletcolourspecification) | struct | — | — | 0 | Parsed as "C/M/Y/K" instead of "C M Y K". |
| [`GPlatesFileIO::CptReaderInternals::GreyColourSpecification`](#gplatesfileiocptreaderinternalsgreycolourspecification) | struct | — | — | 0 | — |
| [`GPlatesFileIO::CptReaderInternals::GMTNameColourSpecification`](#gplatesfileiocptreaderinternalsgmtnamecolourspecification) | struct | — | — | 0 | — |
| [`GPlatesFileIO::CptReaderInternals::PatternFillColourSpecification`](#gplatesfileiocptreaderinternalspatternfillcolourspecification) | struct | — | — | 0 | — |
| [`GPlatesFileIO::CptReaderInternals::InvisibleColourSpecification`](#gplatesfileiocptreaderinternalsinvisiblecolourspecification) | struct | — | — | 0 | — |
| [`GPlatesFileIO::CptReaderInternals::RegularCptSliceColourSpecification`](#gplatesfileiocptreaderinternalsregularcptslicecolourspecification) | struct | — | — | 0 | Any colour without space-separated components that can be used in a regular CPT colour slice. |
| [`GPlatesFileIO::CptReaderInternals::ParserState`](#gplatesfileiocptreaderinternalsparserstate) | struct | `boost::noncopyable` | `<class CptFileFormat>` | 0 | Stores the state of the CPT parser as it proceeds through the file. |
| [`GPlatesFileIO::CptReaderInternals::TryProcessTokensImpl<RegularCptFileFormat>`](#gplatesfileiocptreaderinternalstryprocesstokensimplregularcptfileformat) | struct | — | `<>` | 0 | — |
| [`GPlatesFileIO::CptReaderInternals::TryProcessTokensImpl<CategoricalCptFileFormat<T> >`](#gplatesfileiocptreaderinternalstryprocesstokensimplcategoricalcptfileformatt-) | struct | — | `<typename T>` | 0 | — |
| [`GPlatesFileIO::CptReaderInternals::TryProcessLineImpl`](#gplatesfileiocptreaderinternalstryprocesslineimpl) | struct | — | `<class CptFileFormat>` | 0 | — |
| [`GPlatesFileIO::CptReader`](#gplatesfileiocptreader) | class | — | `<class CptFileFormat>` | 0 | This reads in GMT colour palette table (CPT) files. |
| [`GPlatesFileIO::RegularCptReader`](#gplatesfileioregularcptreader) | typedef | — | — | 0 | A file reader that reads a regular CPT file and produces a colour palette. |
| [`GPlatesFileIO::CategoricalCptReader`](#gplatesfileiocategoricalcptreader) | struct | — | `<typename T>` | 0 | Can't wait for C++0x... |
| [`GPlatesFileIO::IntegerCptReader`](#gplatesfileiointegercptreader) | class | — | `<typename IntType = int>` | 0 | IntegerCptReader parses a file that is either a regular or categorical CPT file, but it is not known which of the two formats it is actually in. |
| [`GPlatesFileIO::CptParser`](#gplatesfileiocptparser) | class | — | — | 0 | — |

## Members

### `GPlatesFileIO::CptReaderInternals::RegularCptFileFormat`

| Member | Kind | Type | Access | Description |
|---|---|---|---|---|
| `colour_palette_type` | typedef | `GPlatesGui::RegularCptColourPalette` | public | — |
| `value_type` | typedef | `double` | public | — |

### `GPlatesFileIO::CptReaderInternals::CategoricalCptFileFormat`

| Member | Kind | Type | Access | Description |
|---|---|---|---|---|
| `colour_palette_type` | typedef | `GPlatesGui::CategoricalCptColourPalette<T>` | public | — |
| `value_type` | typedef | `int` | public | — |

### `GPlatesFileIO::CptReaderInternals::BadTokenException`

*None.*

### `GPlatesFileIO::CptReaderInternals::BadComponentsException`

*None.*

### `GPlatesFileIO::CptReaderInternals::PatternFillEncounteredException`

*None.*

### `GPlatesFileIO::CptReaderInternals::LowestValue<double>`

| Member | Kind | Type | Access | Description |
|---|---|---|---|---|
| `value()` | method | `double` | public | — |

### `GPlatesFileIO::CptReaderInternals::LowestValue<int>`

| Member | Kind | Type | Access | Description |
|---|---|---|---|---|
| `value()` | method | `int` | public | — |

### `GPlatesFileIO::CptReaderInternals::BaseRGBColourSpecification`

| Member | Kind | Type | Access | Description |
|---|---|---|---|---|
| `components_type` | typedef | `boost::tuple<Int<Base>, Int<Base>, Int<Base> >` | public | — |
| `convert( const components_type &components)` | method | `boost::optional<GPlatesGui::Colour>` | public | — |

### `GPlatesFileIO::CptReaderInternals::HexRGBColourSpecification`

*None.*

### `GPlatesFileIO::CptReaderInternals::RGBColourSpecification`

| Member | Kind | Type | Access | Description |
|---|---|---|---|---|
| `components_type` | typedef | `boost::tuple<double, double, double>` | public | — |
| `convert( const components_type& components)` | method | `boost::optional<GPlatesGui::Colour>` | public | — |

### `GPlatesFileIO::CptReaderInternals::RGBTripletColourSpecification`

| Member | Kind | Type | Access | Description |
|---|---|---|---|---|
| `components_type` | typedef | `boost::tuple<const QString &>` | public | — |
| `convert( const components_type& components)` | method | `boost::optional<GPlatesGui::Colour>` | public | — |

### `GPlatesFileIO::CptReaderInternals::HSVColourSpecification`

| Member | Kind | Type | Access | Description |
|---|---|---|---|---|
| `components_type` | typedef | `boost::tuple<double, double, double>` | public | — |
| `convert( const components_type& components)` | method | `boost::optional<GPlatesGui::Colour>` | public | — |

### `GPlatesFileIO::CptReaderInternals::HSVTripletColourSpecification`

| Member | Kind | Type | Access | Description |
|---|---|---|---|---|
| `components_type` | typedef | `boost::tuple<const QString &>` | public | — |
| `convert( const components_type& components)` | method | `boost::optional<GPlatesGui::Colour>` | public | — |

### `GPlatesFileIO::CptReaderInternals::CMYKColourSpecification`

| Member | Kind | Type | Access | Description |
|---|---|---|---|---|
| `components_type` | typedef | `boost::tuple<double, double, double, double>` | public | — |
| `convert( const components_type &components)` | method | `boost::optional<GPlatesGui::Colour>` | public | — |

### `GPlatesFileIO::CptReaderInternals::CMYKTripletColourSpecification`

| Member | Kind | Type | Access | Description |
|---|---|---|---|---|
| `components_type` | typedef | `boost::tuple<const QString &>` | public | — |
| `convert( const components_type& components)` | method | `boost::optional<GPlatesGui::Colour>` | public | — |

### `GPlatesFileIO::CptReaderInternals::GreyColourSpecification`

| Member | Kind | Type | Access | Description |
|---|---|---|---|---|
| `components_type` | typedef | `boost::tuple<double>` | public | — |
| `convert( const components_type &components)` | method | `boost::optional<GPlatesGui::Colour>` | public | — |

### `GPlatesFileIO::CptReaderInternals::GMTNameColourSpecification`

| Member | Kind | Type | Access | Description |
|---|---|---|---|---|
| `components_type` | typedef | `boost::tuple<const QString &>` | public | — |
| `convert( const components_type &components)` | method | `boost::optional<GPlatesGui::Colour>` | public | — |

### `GPlatesFileIO::CptReaderInternals::PatternFillColourSpecification`

| Member | Kind | Type | Access | Description |
|---|---|---|---|---|
| `components_type` | typedef | `boost::tuple<const QString &>` | public | — |
| `convert( const components_type &components)` | method | `boost::optional<GPlatesGui::Colour>` | public | — |

### `GPlatesFileIO::CptReaderInternals::InvisibleColourSpecification`

| Member | Kind | Type | Access | Description |
|---|---|---|---|---|
| `components_type` | typedef | `boost::tuple<const QString &>` | public | — |
| `convert( const components_type &components)` | method | `boost::optional<GPlatesGui::Colour>` | public | — |

### `GPlatesFileIO::CptReaderInternals::RegularCptSliceColourSpecification`

| Member | Kind | Type | Access | Description |
|---|---|---|---|---|
| `components_type` | typedef | `boost::tuple<const QString &>` | public | — |
| `convert( const components_type &components)` | method | `boost::optional<GPlatesGui::Colour>` | public | — |

### `GPlatesFileIO::CptReaderInternals::ParserState`

| Member | Kind | Type | Access | Description |
|---|---|---|---|---|
| `colour_palette_type` | typedef | `typename CptFileFormat::colour_palette_type` | public | — |
| `value_type` | typedef | `typename CptFileFormat::value_type` | public | — |
| `ParserState( colour_palette_type &palette_, ReadErrorAccumulation &errors_, boost::shared_ptr<DataSource> data_source_)` | constructor | `None` | public | — |
| `palette` | field | `colour_palette_type` | public | The data structure that holds all lines successfully read in. |
| `errors` | field | `ReadErrorAccumulation` | public | For the reporting of read errors. |
| `data_source` | field | `boost::shared_ptr<DataSource>` | public | Where our lines are coming from; used for error reporting. |
| `colour_model` | field | `GPlatesGui::ColourModel::Type` | public | Colour model as specified in CPT file. |
| `any_successful_lines` | field | `bool` | public | True if any non-comment lines have been successfully parsed. |
| `error_reported_for_current_line` | field | `bool` | public | True if an error has already been reported for the current line; used to prevent cascading errors being reported. |
| `current_line_number` | field | `unsigned long` | public | The line number that we're currently parsing. |
| `previous_upper_value` | field | `value_type` | public | Stores the upper z-value of the previous slice. |

### `GPlatesFileIO::CptReaderInternals::TryProcessTokensImpl<RegularCptFileFormat>`

| Member | Kind | Type | Access | Description |
|---|---|---|---|---|
| `operator()( const QStringList &tokens, ParserState<RegularCptFileFormat> &parser_state)` | operator | `bool` | public | — |

### `GPlatesFileIO::CptReaderInternals::TryProcessTokensImpl<CategoricalCptFileFormat<T> >`

| Member | Kind | Type | Access | Description |
|---|---|---|---|---|
| `operator()( const QStringList &tokens, ParserState<CategoricalCptFileFormat<T> > &parser_state)` | operator | `bool` | public | — |

### `GPlatesFileIO::CptReaderInternals::TryProcessLineImpl`

| Member | Kind | Type | Access | Description |
|---|---|---|---|---|
| `operator()( const QString &line, ParserState<CptFileFormat> &parser_state)` | operator | `void` | public | — |
| `try_process_tokens( const QStringList &tokens, ParserState<CptFileFormat> &parser_state)` | method | `bool` | public | — |

### `GPlatesFileIO::CptReader`

| Member | Kind | Type | Access | Description |
|---|---|---|---|---|
| `colour_palette_type` | typedef | `typename CptFileFormat::colour_palette_type` | public | — |
| `read_file( QTextStream &text_stream, ReadErrorAccumulation &errors, boost::shared_ptr<DataSource> data_source = boost::shared_ptr<DataSource>( new GenericDataSource( DataFormats::Cpt, "QTextStream")))` | method | `typename colour_palette_type::maybe_null_ptr_type` | public | Parses text from the provided text\_stream as a regular CPT file. |
| `read_file( const QString &filename, ReadErrorAccumulation &errors)` | method | `typename colour_palette_type::maybe_null_ptr_type` | public | A convenience function for reading the file with the given filename as a regular CPT file. read\_file() that takes a QTextStream as the first parameter. |

### `GPlatesFileIO::RegularCptReader`

*None.*

### `GPlatesFileIO::CategoricalCptReader`

| Member | Kind | Type | Access | Description |
|---|---|---|---|---|
| `Type` | typedef | `CptReader<CptReaderInternals::CategoricalCptFileFormat<T> >` | public | A file reader that reads a categorical CPT file and produces a colour palette that maps values of template type T to colours. |

### `GPlatesFileIO::IntegerCptReader`

| Member | Kind | Type | Access | Description |
|---|---|---|---|---|
| `colour_palette_type` | typedef | `GPlatesGui::ColourPalette<IntType>` | public | — |
| `read_file( const QString &filename, ReadErrorAccumulation &errors)` | method | `typename GPlatesGui::ColourPalette<IntType>::maybe_null_ptr_type` | public | — |

### `GPlatesFileIO::CptParser`

| Member | Kind | Type | Access | Description |
|---|---|---|---|---|
| `Model` | enum | `None` | public | — |
| `ColourData` | struct | `None` | public | — |
| `CategoricalEntry` | struct | `None` | public | — |
| `RegularEntry` | struct | `None` | public | — |
| `CptParser(const QString& file_path)` | constructor | `None` | public | — |
| `bfn_data()` | method | `std::vector<ColourData>` | public | — |
| `process_line( const QString& line)` | method | `void` | protected | — |
| `process_bfn( QStringList& tokens, ColourData& data)` | method | `void` | protected | Process background color, foreground color and NaN color definition. |
| `process_regular_line( QStringList& tokens)` | method | `void` | protected | Process regular cpt data. |
| `read_first_colour_data( QStringList& tokens)` | method | `ColourData` | protected | — |
| `read_second_colour_data( QStringList& tokens)` | method | `ColourData` | protected | — |
| `process_categorical_line( QStringList& tokens)` | method | `void` | protected | Process categorical cpt data. |
| `process_comment( const QString& line)` | method | `void` | protected | — |
| `split_into_tokens( const QString& line)` | method | `QStringList` | protected | Parse a line of cpt file according to GMT cpt specification.. |
| `parse_gmt_fill( const QString& token)` | method | `ColourData` | protected | — |
| `is_gmt_color_name( const QString& name)` | method | `bool` | protected | — |
| `is_valid_rgb( float r, float g, float b)` | method | `bool` | protected | — |
| `is_valid_hsv( float h, float s, float v)` | method | `bool` | protected | — |
| `is_valid_cmyk( float c, float m, float y, float k)` | method | `bool` | protected | — |
| `parse_rbg_data( QStringList& tokens, ColourData& data)` | method | `void` | protected | Given the raw data in QStringList, parse the data into ColourData. |
| `parse_hsv_data( QStringList& tokens, ColourData& data)` | method | `void` | protected | Given the raw data in QStringList, parse the data into ColourData. |
| `parse_cmyk_data( QStringList& tokens, ColourData& data)` | method | `void` | protected | Given the raw data in QStringList, parse the data into ColourData. |
| `d_default_model` | field | `Model` | protected | — |
| `d_back` | field | `ColourData` | protected | — |
| `d_fore` | field | `ColourData` | protected | — |
| `d_nan` | field | `ColourData` | protected | — |
| `d_categorical_entries` | field | `std::vector<CategoricalEntry>` | protected | — |
| `d_regular_entries` | field | `std::vector<RegularEntry>` | protected | — |

## Free functions and macros

| Name | Kind | Type / body | Description |
|---|---|---|---|
| `parse_components( const QStringList &tokens, unsigned int starting_index)` | function | `boost::tuples::null_type` | — |
| `operator()( const QStringList &tokens, ParserState<RegularCptFileFormat> &parser_state)` | operator | `bool` | — |
| `GPLATES_FILEIO_CPTREADER_H` | macro | `None` | — |
| `parse_token(const QString &token)` | function | `T` | — |
| `parse_components( const QStringList &tokens, unsigned int starting_index = 0)` | function | `ComponentsType` | Parses a series of string tokens, starting from starting\_index in tokens, into the other types specified by ComponentsType, which is expected to be a boost::tuple. |
| `in_rgb_range( double value)` | function | `bool` | Returns true if the value lies within the valid range of a "red", "green" or "blue" token in a CPT file. |
| `make_rgb_colour( double r, double g, double b)` | function | `GPlatesGui::Colour` | Creates a GPlates Colour from the RGB values specified in a CPT file. |
| `in_h_range( double value)` | function | `bool` | Returns true if the value lies within the valid range of a "hue" token in a CPT file. |
| `in_sv_range( double value)` | function | `bool` | Returns true if the value lies within the valid range of a "saturation" or "value" token in a CPT file. |
| `make_hsv_colour( double h, double s, double v)` | function | `GPlatesGui::Colour` | Creates a GPlates Colour from the HSV values specified in a CPT file. |
| `in_cmyk_range( double value)` | function | `bool` | Returns true if the value lies within the valid range of a "cyan", "magenta", "yellow" or "black" token in a CPT file. |
| `make_cmyk_colour( double c, double m, double y, double k)` | function | `GPlatesGui::Colour` | Creates a GPlates Colour from the CMYK values specified in a CPT file. |
| `in_grey_range( double value)` | function | `bool` | Returns true if the value lies within the valid range of a "grey" token in a CPT file. |
| `make_grey_colour( double value)` | function | `GPlatesGui::Colour` | Creates a GPlates Colour from the grey value specified in a CPT file. |
| `make_gmt_colour( const QString &name)` | function | `GPlatesGui::Colour` | Creates a GPlates Colour from a GMT colour name. |
| `is_pattern_fill_specification( const QString &token)` | function | `bool` | Returns true if it is in the format of a pattern fill. |
| `convert_tokens( const QStringList &tokens, unsigned int starting_index = 0)` | function | `boost::optional<GPlatesGui::Colour>` | Parses components and converts the parsed components into a colour. |
| `try_process_comment( const QString &line, ParserState<CptFileFormat> &parser_state)` | function | `bool` | Attempts to process a line in a regular or categorical CPT file as a comment. |
| `try_process_bfn( const QStringList &tokens, ParserState<CptFileFormat> &parser_state)` | function | `bool` | Attempts to process a line in a regular or categorical CPT file as a "BFN" line. |
| `try_process_rgb_or_hsv_or_cmyk_bfn( const QStringList &tokens, ParserState<CptFileFormat> &parser_state)` | function | `bool` | Delegates to the correct function depending on the current colour model. |
| `try_process_regular_cpt_colour_slice( const QStringList &tokens, ParserState<RegularCptFileFormat> &parser_state)` | function | `bool` | Attempts to process a regular CPT file line as a colour slice. |
| `try_process_regular_cpt_rgb_or_hsv_or_cmyk_colour_slice( const QStringList &tokens, ParserState<RegularCptFileFormat> &parser_state)` | function | `bool` | Delegates to the correct function depending on the current colour model. |
| `parse_categorical_fill( const QString &token)` | function | `boost::optional<GPlatesGui::Colour>` | Attempts to parse the fill specification on a categorical CPT line. |
| `try_process_categorical_cpt_colour_entry( const QStringList &tokens, ParserState<CategoricalCptFileFormat<T> > &parser_state)` | function | `bool` | Attempts to process a line as an entry in a categorical CPT file. |
| `try_process_line( const QString &line, ParserState<CptFileFormat> &parser_state)` | function | `void` | Attempts to parse a line in a CPT file. parser\_state.any\_successful\_line is set to true if the line was successfully parsed as a non-comment line. |

## Notes

The Doxygen on `CptReader::read_file` saying the caller must deallocate the returned memory is stale. `colour_palette_type::maybe_null_ptr_type` is a `boost::intrusive_ptr` and `GPlatesGui::ColourPalette` derives from `GPlatesUtils::ReferenceCount`, so the result is reference-counted; a null pointer, not an exception, is how the template reader signals "nothing usable in this file". `read_file(QTextStream&, …)` builds a fresh `GenericDataSource` in its default argument on every call.

Malformed input never aborts a read. Every candidate grammar returns `false` on failure and the line is dropped with an `InvalidRegularCptLine` / `InvalidCategoricalCptLine` recoverable error; `ParserState::error_reported_for_current_line` exists so that a candidate which already logged a specific error (pattern fill, unrecognised label) suppresses the generic one, and it is reset at the end of every line. A file only fails outright when *no* non-comment line parsed, which raises `NoLinesSuccessfullyParsed` as a terminating error. Out-of-order z-values are a `CptSliceNotMonotonicallyIncreasing` warning only — the entry is still added to the palette, and in the categorical case it is added before the check runs, so downstream code must not assume palette entries are sorted.

`COLOR_MODEL` is read from a comment and applies only to lines *after* it; changing it partway through emits `ColourModelChangedMidway` but is otherwise honoured. Pattern fills are not supported and the test for one is just "the token starts with `p`", so a GMT colour name beginning with `p` can be misread as a pattern fill and drop the line. `LowestValue<T>` is specialised for `double` and `int` only, and `parse_components<boost::tuples::null_type>` is an explicit specialisation defined in the `.cc`; a new `CptFileFormat` with a different `value_type` will not link. `TryProcessLineImpl::try_process_tokens` is declared but has no definition anywhere in the tree and is never called — the real dispatch is `TryProcessTokensImpl`.

`CptParser` behaves quite differently and is the rougher of the two. Its constructor does the whole parse and throws `GPlatesGlobal::LogException` if the file cannot be opened, but per-line failures are caught there and only passed to `qWarning()`, so construction can succeed with silently empty entry vectors and no `ReadErrorAccumulation` is involved at all. Its `split_into_tokens` honours single- and double-quoted keys, so it can read categorical keys containing spaces that the template reader — which splits on bare whitespace — cannot. `process_line` routes any line of three tokens or fewer to the categorical path, so BFN lines are only recognised when they have more than three tokens. `process_comment` only ever detects `COLOR_MODEL = HSV`: it builds an uppercased, space-stripped copy of the line and then matches the regular expression against the original line instead, and there is no CMYK or RGB branch, so `d_default_model` never becomes `CMYK`. `is_gmt_color_name` looks the name up verbatim while `CptReaderInternals::make_gmt_colour` lower-cases first, so the two readers disagree on capitalised GMT colour names.

The `.cc` disables `-Wstrict-overflow` for the whole translation unit because of `QStringList::at` on some g++/Qt combinations. `file-io` reaching into `gui` for `GMTColourNames` is acknowledged as wrong direction by a `TODO` in `CptParser::is_gmt_color_name`.

## Used by

| Unit | Component | References |
|---|---|---|
| [gui/Palette](../gui/Palette.md) | gui | 53 |
| [qt-widgets/ColouringDialog](../qt-widgets/ColouringDialog.md) | qt-widgets | 24 |
| [qt-widgets/DrawStyleDialog](../qt-widgets/DrawStyleDialog.md) | qt-widgets | 18 |
| [gui/ColourPaletteUtils](../gui/ColourPaletteUtils.md) | gui | 16 |
| [qt-widgets/HellingerSegmentDialog](../qt-widgets/HellingerSegmentDialog.md) | qt-widgets | 12 |
| [qt-widgets/TopologyNetworkResolverLayerOptionsWidget](../qt-widgets/TopologyNetworkResolverLayerOptionsWidget.md) | qt-widgets | 4 |
| [qt-widgets/AgeModelManagerDialog](../qt-widgets/AgeModelManagerDialog.md) | qt-widgets | 3 |
| [qt-widgets/VisualLayersListView](../qt-widgets/VisualLayersListView.md) | qt-widgets | 3 |
| [gui/CsvExport](../gui/CsvExport.md) | gui | 2 |
| [qt-widgets/ConfigureExportParametersDialog](../qt-widgets/ConfigureExportParametersDialog.md) | qt-widgets | 2 |
| [qt-widgets/ExportAnimationDialog](../qt-widgets/ExportAnimationDialog.md) | qt-widgets | 2 |
| [qt-widgets/VisualLayerWidget](../qt-widgets/VisualLayerWidget.md) | qt-widgets | 2 |
| [utils/UniqueId](../utils/UniqueId.md) | utils | 2 |
| [gui/CustomCompleter](../gui/CustomCompleter.md) | gui | 1 |
| [presentation/ViewState](../presentation/ViewState.md) | presentation | 1 |
| [qt-widgets/ChangeFeatureTypeDialog](../qt-widgets/ChangeFeatureTypeDialog.md) | qt-widgets | 1 |
| [qt-widgets/ColourScaleButton](../qt-widgets/ColourScaleButton.md) | qt-widgets | 1 |
| [qt-widgets/ColourScaleWidget](../qt-widgets/ColourScaleWidget.md) | qt-widgets | 1 |
| [qt-widgets/EditTimeSequenceWidget](../qt-widgets/EditTimeSequenceWidget.md) | qt-widgets | 1 |
| [qt-widgets/ExportFileNameTemplateWidget](../qt-widgets/ExportFileNameTemplateWidget.md) | qt-widgets | 1 |

*... and 12 more units.*

## Related

*None.*

## Explore

Run these from the `gplates-code` skill directory:

```bash
python scripts/gpq.py file src/file-io/CptReader.h
python scripts/gpq.py def GPlatesFileIO::CptParser --body
python scripts/gpq.py uses CptParser --kind class
python scripts/gpq.py hier CptParser
```
