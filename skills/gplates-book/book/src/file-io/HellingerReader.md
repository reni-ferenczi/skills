# HellingerReader

[Book TOC](../../TOC.md) · [file-io](../../components/file-io.md) · cluster Community 344 · tier 2

| Source file | Kind | Lines |
|---|---|---|
| `src/file-io/HellingerReader.h` | C++ | 84 |
| `src/file-io/HellingerReader.cc` | C++ | 1010 |

## Overview

[[[PROSE overview unit=file-io/HellingerReader tier=2]]]
Replace this whole block, markers included, with 1-3 paragraphs: what this unit is, why it exists, and how it fits the surrounding design. Do not restate the tables below.
[[[/PROSE]]]

## Declared types

| Name | Kind | Bases | Template | Subclasses | Description |
|---|---|---|---|---|---|
| [`GPlatesFileIO::HellingerReader`](#gplatesfileiohellingerreader) | class | — | — | 0 | The HellingerReader class |

## Members

### `GPlatesFileIO::HellingerReader`

| Member | Kind | Type | Access | Description |
|---|---|---|---|---|
| `HellingerReader()` | constructor | `None` | public | — |
| `read_pick_file( const QString &filename, GPlatesQtWidgets::HellingerModel &hellinger_model, ReadErrorAccumulation &read_errors)` | method | `bool` | public | read\_pick\_file - Read and parse the contents of a text .pick file, putting the contents into hellinger\_model. |
| `read_com_file( const QString &filename, GPlatesQtWidgets::HellingerModel& hellinger_model, ReadErrorAccumulation &read_errors)` | method | `bool` | public | — |
| `read_error_ellipse( const QString &filename, GPlatesQtWidgets::HellingerModel& hellinger_model, const GPlatesQtWidgets::HellingerPlatePairType &type = GPlatesQtWidgets::PLATES_1_2_PAIR_TYPE)` | method | `void` | public | — |
| `read_fit_results_from_temporary_fit_file( const QString &filename, GPlatesQtWidgets::HellingerModel& hellinger_model)` | method | `void` | public | — |

## Free functions and macros

| Name | Kind | Type / body | Description |
|---|---|---|---|
| `MIN_NUM_FIELDS` | variable | `int` | — |
| `plate_index_represents_an_enabled_pick( const GPlatesQtWidgets::HellingerPlateIndex &plate_index)` | function | `bool` | — |
| `latitude_ok( const QString &s, double &latitude)` | function | `bool` | — |
| `longitude_ok( const QString &s, double &longitude)` | function | `bool` | — |
| `angle_ok( const QString &s, double &angle)` | function | `bool` | angle\_ok |
| `initial_guess_ok(const QString &line,double &lat, double &lon, double &rho)` | function | `bool` | initial\_guess\_ok true if the fields lat,lon,rho can be parsed correctly from the QString line. lat,lon and rho are filled with their parsed values on successful return. |
| `boolean_line_ok(const QString &line, bool &result)` | function | `bool` | boolean\_line\_ok - returns true of line consists of upper- or lower-case "y" or "n", returns false otherwise. |
| `create_two_way_plate_index_set()` | function | `std::set<GPlatesQtWidgets::HellingerPlateIndex>` | — |
| `create_three_way_plate_index_set()` | function | `std::set<GPlatesQtWidgets::HellingerPlateIndex>` | — |
| `pick_fields_are_ok( const QStringList &fields, GPlatesQtWidgets::HellingerPick &pick, int &segment)` | function | `bool` | pick\_fields\_are\_ok Returns true if it was possible to build a pick structure from |
| `try_to_extract_nsegments_from_first_line( const QString &line)` | function | `boost::optional<int>` | test\_first\_line - 3-way pick files may have a single integer in the first line representing the total number of segments. |
| `parse_pick_line( const QString &line, GPlatesQtWidgets::hellinger_model_type &pick_data)` | function | `void` | — |
| `parse_two_plate_com_line( const QString &line, GPlatesQtWidgets::HellingerComFileStructure &hellinger_com_file, unsigned int &line_number)` | function | `void` | — |
| `read_file_and_guess( QTextStream &stream, GPlatesQtWidgets::HellingerComFileStructure &hellinger_com_file, unsigned int &line_number)` | function | `void` | — |
| `read_file_and_guesses( QTextStream &stream, GPlatesQtWidgets::HellingerComFileStructure &hellinger_com_file, unsigned int &line_number)` | function | `void` | — |
| `read_search_and_grid_options( QTextStream &stream, GPlatesQtWidgets::HellingerComFileStructure &hellinger_com_file, unsigned int &line_number)` | function | `void` | — |
| `read_amoeba_iterations( QTextStream &stream, GPlatesQtWidgets::HellingerComFileStructure &hellinger_com_file, unsigned int &line_number)` | function | `void` | — |
| `read_confidence_and_kappa( QTextStream &stream, GPlatesQtWidgets::HellingerComFileStructure &hellinger_com_file, unsigned int &line_number)` | function | `void` | — |
| `read_output_filenames( const GPlatesQtWidgets::HellingerPlatePairType &pair_type, QTextStream &stream, GPlatesQtWidgets::HellingerComFileStructure &hellinger_com_file, unsigned int &line_number)` | function | `void` | — |
| `parse_two_plate_com_lines( QTextStream &stream, GPlatesQtWidgets::HellingerComFileStructure &hellinger_com_file, unsigned int &line_number)` | function | `void` | parse\_two\_plate\_com\_lines - parse the fields in a hellinger1 ".com" file and store them in hellinger\_com\_file for error reporting. |
| `parse_three_plate_com_lines( QTextStream &stream, GPlatesQtWidgets::HellingerComFileStructure &hellinger_com_file, unsigned int &line_number)` | function | `void` | — |
| `parse_filename_for_chron_string( QString filepath)` | function | `QString` | parse\_filename\_for\_chron\_string the string lying between the last dash ("-") or last underscore ("\_") (whichever lies closest to the end) and the last full stop ("."). |
| `determine_com_file_type_from_third_line( const QString &line)` | function | `GPlatesQtWidgets::HellingerFitType` | determine\_com\_file\_type\_from\_third\_line Distinguish two-way and three-way .com file based on the contents of the third line. |
| `determine_fit_type( QTextStream &stream)` | function | `GPlatesQtWidgets::HellingerFitType` | determine\_fit\_type - determines whether the file represented by stream is a 2-way or 3-way .com file, based solely on the form of the third line. stream is reset to the start of the file before returning. |
| `GPLATES_FILEIO_PICKFILEREADER_H` | macro | `None` | — |

## Notes

[[[PROSE notes unit=file-io/HellingerReader tier=2]]]
Replace this whole block, markers included, with invariants, ownership, threading or gotchas that are not visible in the tables. Write *None.* if there is nothing worth saying.
[[[/PROSE]]]

## Used by

| Unit | Component | References |
|---|---|---|
| [qt-widgets/HellingerDialog](../qt-widgets/HellingerDialog.md) | qt-widgets | 17 |

## Related

*None.*

## Explore

Run these from the `gplates-code` skill directory:

```bash
python scripts/gpq.py file src/file-io/HellingerReader.h
python scripts/gpq.py def GPlatesFileIO::HellingerReader --body
python scripts/gpq.py uses HellingerReader --kind class
python scripts/gpq.py hier HellingerReader
```
