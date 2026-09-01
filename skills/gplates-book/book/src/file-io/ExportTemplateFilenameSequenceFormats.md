# ExportTemplateFilenameSequenceFormats

[Book TOC](../../TOC.md) · [file-io](../../components/file-io.md) · cluster Community 205 · tier 2

| Source file | Kind | Lines |
|---|---|---|
| `src/file-io/ExportTemplateFilenameSequenceFormats.h` | C++ | 491 |
| `src/file-io/ExportTemplateFilenameSequenceFormats.cc` | C++ | 345 |

## Overview

This header defines the individual format-specifier classes that
`ExportTemplateFilenameSequenceImpl` (the private implementation behind
`file-io/ExportTemplateFilenameSequence`) matches against a filename template
and expands per frame. Each placeholder from the template syntax — `%%`,
`%P`, `%A`, `%R`, `%n`/`%u`, `%f`/`%d`, `%T`/`%D` — gets its own `Format`
subclass (`PercentCharacterFormat`, `PlaceholderFormat`,
`ReconstructionAnchorPlateIdFormat`, `DefaultReconstructionTreeLayerNameFormat`,
`FrameNumberFormat`, `ReconstructionTimePrintfFormat`, `DateTimeFormat`), so
adding a new placeholder means adding one new `Format` implementation rather
than extending a monolithic parser.

Each subclass exposes a static `match_format()` that tests whether a format
specifier starts at the current position in the remaining template text and,
if so, returns how many characters it consumed, plus a virtual
`expand_format_string()` that renders the specifier's text for a given frame
index, reconstruction time and date/time. `Format::get_variation_type()`
classifies a specifier as varying with reconstruction time/frame, varying
only across iterators (the `%T`/`%D` timestamp captured once per iterator),
or constant, which lets the caller decide how much of an expansion can be
cached. The `format_types` `boost::mpl::vector` lists every concrete `Format`
in the order matching is attempted; `ReconstructionTimePrintfFormat` is
deliberately last so a printf-style catch-all cannot shadow a more specific
specifier added later.

## Declared types

| Name | Kind | Bases | Template | Subclasses | Description |
|---|---|---|---|---|---|
| [`GPlatesFileIO::ExportTemplateFilename::format_types`](#gplatesfileioexporttemplatefilenameformat_types) | typedef | — | — | 0 | Add all Format types here. |
| [`GPlatesFileIO::ExportTemplateFilename::Format`](#gplatesfileioexporttemplatefilenameformat) | class | — | — | 7 | Abstract base class for different types of format used in the template filename. |
| [`GPlatesFileIO::ExportTemplateFilename::PercentCharacterFormat`](#gplatesfileioexporttemplatefilenamepercentcharacterformat) | class | [`Format`](ExportTemplateFilenameSequenceFormats.md) | — | 0 | Simple format pattern percent '%' character. |
| [`GPlatesFileIO::ExportTemplateFilename::PlaceholderFormat`](#gplatesfileioexporttemplatefilenameplaceholderformat) | class | [`Format`](ExportTemplateFilenameSequenceFormats.md) | — | 0 | Simple format pattern for a placeholder. |
| [`GPlatesFileIO::ExportTemplateFilename::ReconstructionAnchorPlateIdFormat`](#gplatesfileioexporttemplatefilenamereconstructionanchorplateidformat) | class | [`Format`](ExportTemplateFilenameSequenceFormats.md) | — | 0 | Simple format pattern for reconstruction anchor plate id. |
| [`GPlatesFileIO::ExportTemplateFilename::DefaultReconstructionTreeLayerNameFormat`](#gplatesfileioexporttemplatefilenamedefaultreconstructiontreelayernameformat) | class | [`Format`](ExportTemplateFilenameSequenceFormats.md) | — | 0 | Simple format pattern for the layer name of the default reconstruction tree layer. |
| [`GPlatesFileIO::ExportTemplateFilename::FrameNumberFormat`](#gplatesfileioexporttemplatefilenameframenumberformat) | class | [`Format`](ExportTemplateFilenameSequenceFormats.md) | — | 0 | Format pattern for frame number or index. |
| [`GPlatesFileIO::ExportTemplateFilename::ReconstructionTimePrintfFormat`](#gplatesfileioexporttemplatefilenamereconstructiontimeprintfformat) | class | [`Format`](ExportTemplateFilenameSequenceFormats.md) | — | 0 | Format pattern for reconstruction time in printf-style format. |
| [`GPlatesFileIO::ExportTemplateFilename::DateTimeFormat`](#gplatesfileioexporttemplatefilenamedatetimeformat) | class | [`Format`](ExportTemplateFilenameSequenceFormats.md) | — | 0 | Format pattern for date/time. |

## Members

### `GPlatesFileIO::ExportTemplateFilename::format_types`

*None.*

### `GPlatesFileIO::ExportTemplateFilename::Format`

| Member | Kind | Type | Access | Description |
|---|---|---|---|---|
| `Variation` | enum | `None` | public | Enumeration that specified whether a format varies with reconstruction time, or varies across sequence iterators or is constant always. |
| `~Format()` | destructor | `None` | public | — |
| `get_variation_type()` | method | `Variation` | public | Returns Variation enum specifying whether this format varies with reconstruction time, or varies across sequence iterators or is constant always. |
| `expand_format_string( std::size_t sequence_index, const double &reconstruction_time, const QDateTime &date_time)` | method | `QString` | public | Converts this format to a QString potentially using the current index and reconstruction time in the sequence and the date/time. |

### `GPlatesFileIO::ExportTemplateFilename::PercentCharacterFormat`

| Member | Kind | Type | Access | Description |
|---|---|---|---|---|
| `VARIATION_TYPE` | field | `Variation` | public | How this format varies. |
| `match_format( const QString &rest_of_filename_template)` | method | `boost::optional<int>` | public | Returns true if the start of rest\_of\_filename\_template matches the format specifier for this class. |
| `get_variation_type()` | method | `Variation` | public | The format variation type. |
| `expand_format_string( std::size_t sequence_index, const double &reconstruction_time, const QDateTime &date_time)` | method | `QString` | public | — |

### `GPlatesFileIO::ExportTemplateFilename::PlaceholderFormat`

| Member | Kind | Type | Access | Description |
|---|---|---|---|---|
| `VARIATION_TYPE` | field | `Variation` | public | How this format varies. |
| `match_format( const QString &rest_of_filename_template)` | method | `boost::optional<int>` | public | Returns true if the start of rest\_of\_filename\_template matches the format specifier for this class. |
| `get_variation_type()` | method | `Variation` | public | The format variation type. |
| `expand_format_string( std::size_t sequence_index, const double &reconstruction_time, const QDateTime &date_time)` | method | `QString` | public | — |

### `GPlatesFileIO::ExportTemplateFilename::ReconstructionAnchorPlateIdFormat`

| Member | Kind | Type | Access | Description |
|---|---|---|---|---|
| `VARIATION_TYPE` | field | `Variation` | public | How this format varies. |
| `match_format( const QString &rest_of_filename_template)` | method | `boost::optional<int>` | public | Returns true if the start of rest\_of\_filename\_template matches the format specifier for this class. |
| `ReconstructionAnchorPlateIdFormat( const GPlatesModel::integer_plate_id_type &anchor_plate_id)` | constructor | `None` | public | — |
| `get_variation_type()` | method | `Variation` | public | The format variation type. |
| `expand_format_string( std::size_t sequence_index, const double &reconstruction_time, const QDateTime &date_time)` | method | `QString` | public | — |
| `d_reconstruction_anchor_plate_id` | field | `GPlatesModel::integer_plate_id_type` | private | — |

### `GPlatesFileIO::ExportTemplateFilename::DefaultReconstructionTreeLayerNameFormat`

| Member | Kind | Type | Access | Description |
|---|---|---|---|---|
| `VARIATION_TYPE` | field | `Variation` | public | How this format varies. |
| `match_format( const QString &rest_of_filename_template)` | method | `boost::optional<int>` | public | Returns true if the start of rest\_of\_filename\_template matches the format specifier for this class. |
| `DefaultReconstructionTreeLayerNameFormat( const QString &default_recon_tree_layer_name)` | constructor | `None` | public | — |
| `get_variation_type()` | method | `Variation` | public | The format variation type. |
| `expand_format_string( std::size_t sequence_index, const double &reconstruction_time, const QDateTime &date_time)` | method | `QString` | public | — |
| `d_default_recon_tree_layer_name` | field | `QString` | private | — |

### `GPlatesFileIO::ExportTemplateFilename::FrameNumberFormat`

| Member | Kind | Type | Access | Description |
|---|---|---|---|---|
| `VARIATION_TYPE` | field | `Variation` | public | How this format varies. |
| `match_format( const QString &rest_of_filename_template)` | method | `boost::optional<int>` | public | Returns true if the start of rest\_of\_filename\_template matches the format specifier for this class. |
| `FrameNumberFormat( const QString &format_string, std::size_t sequence_size)` | constructor | `None` | public | — |
| `get_variation_type()` | method | `Variation` | public | The format variation type. |
| `expand_format_string( std::size_t sequence_index, const double &reconstruction_time, const QDateTime &date_time)` | method | `QString` | public | — |
| `d_max_digits` | field | `int` | private | — |
| `d_use_frame_number` | field | `bool` | private | Is frame number \[1,N\] otherwise it's \[0,N-1\]. |
| `calc_max_digits( std::size_t sequence_size)` | method | `void` | private | Calculate maximum number of digits. |

### `GPlatesFileIO::ExportTemplateFilename::ReconstructionTimePrintfFormat`

| Member | Kind | Type | Access | Description |
|---|---|---|---|---|
| `VARIATION_TYPE` | field | `Variation` | public | How this format varies. |
| `match_format( const QString &rest_of_filename_template)` | method | `boost::optional<int>` | public | Returns true if the start of rest\_of\_filename\_template matches the format specifier for this class. |
| `ReconstructionTimePrintfFormat( const QString &format_string)` | constructor | `None` | public | — |
| `get_variation_type()` | method | `Variation` | public | The format variation type. |
| `expand_format_string( std::size_t sequence_index, const double &reconstruction_time, const QDateTime &date_time)` | method | `QString` | public | — |
| `d_format_string` | field | `std::string` | private | — |
| `d_is_integer_format` | field | `bool` | private | — |
| `get_full_regular_expression` | field | `QRegExp` | private | Returns regular expression used to match reconstruction time printf-style. |
| `get_integer_regular_expression` | field | `QRegExp` | private | Returns regular expression used to match reconstruction time printf-style integer. |

### `GPlatesFileIO::ExportTemplateFilename::DateTimeFormat`

| Member | Kind | Type | Access | Description |
|---|---|---|---|---|
| `VARIATION_TYPE` | field | `Variation` | public | How this format varies. |
| `match_format( const QString &rest_of_filename_template)` | method | `boost::optional<int>` | public | Returns true if the start of rest\_of\_filename\_template matches the format specifier for this class. |
| `DateTimeFormat( const QString &format_string)` | constructor | `None` | public | — |
| `get_variation_type()` | method | `Variation` | public | The format variation type. |
| `expand_format_string( std::size_t sequence_index, const double &reconstruction_time, const QDateTime &date_time)` | method | `QString` | public | — |
| `d_date_time_format` | field | `QString` | private | — |
| `HOURS_MINS_SECS_WITH_DASHES_SPECIFIER` | field | `QString` | private | — |
| `YEAR_MONTH_DAY_WITH_DASHES_SPECIFIER` | field | `QString` | private | — |

## Free functions and macros

| Name | Kind | Type / body | Description |
|---|---|---|---|
| `VARIATION_TYPE` | variable | `GPlatesFileIO::ExportTemplateFilename::Format::Variation` | — |
| `HOURS_MINS_SECS_WITH_DASHES_SPECIFIER` | variable | `QString` | — |
| `YEAR_MONTH_DAY_WITH_DASHES_SPECIFIER` | variable | `QString` | — |
| `GPLATES_FILE_IO_EXPORTTEMPLATEFILENAMESEQUENCEFORMATS_H` | macro | `None` | — |

## Notes

- The order of `format_types` is load-bearing, not cosmetic: matching walks
  the list in order and stops at the first `match_format()` success, and the
  comment on `format_types` explains why `ReconstructionTimePrintfFormat`
  must stay last — a new specifier inserted after it risks being swallowed by
  the printf-style matcher instead of being recognised.
- `DefaultReconstructionTreeLayerNameFormat` silently rewrites spaces in the
  layer name to underscores in its constructor because some operating
  systems mishandle spaces in filenames; other whitespace is left untouched
  (marked `TODO` in the source).
- `PlaceholderFormat` (`%P`) is the one specifier that is matched but not
  substituted here — `expand_format_string()` for it is defined out-of-line
  in the `.cc` and returns the placeholder itself, leaving expansion to the
  caller as documented on `ExportTemplateFilename::PLACEHOLDER_FORMAT_STRING`
  in `file-io/ExportTemplateFilenameSequence`.

## Used by

| Unit | Component | References |
|---|---|---|
| [file-io/ExportTemplateFilenameSequenceImpl](ExportTemplateFilenameSequenceImpl.md) | file-io | 34 |

## Related

*None.*

## Explore

Run these from the `gplates-code` skill directory:

```bash
python scripts/gpq.py file src/file-io/ExportTemplateFilenameSequenceFormats.h
python scripts/gpq.py def GPlatesFileIO::ExportTemplateFilename::Format --body
python scripts/gpq.py uses Format --kind class
python scripts/gpq.py hier Format
```
