# LineReader

[Book TOC](../../TOC.md) · [file-io](../../components/file-io.md) · cluster Community 411 · tier 2

| Source file | Kind | Lines |
|---|---|---|
| `src/file-io/LineReader.h` | C++ | 120 |
| `src/file-io/LineReader.cc` | C++ | 101 |

## Overview

`LineReader` is a small buffered line-reading wrapper around `QTextStream`,
built for the hand-written line-oriented parsers such as
`PlatesLineFormatReader` and `PlatesRotationFormatReader` that need one line
of lookahead — `peekline` returns the next line without consuming it, and a
following `getline` returns that same line. It deliberately reads through a
`QFile`/`QString` rather than `std::istream`/`std::string` so filenames and
file content with Unicode characters are handled correctly, and it forces
`UTF-8` decoding on the underlying stream in the constructor. Inheriting from
`GPlatesUtils::SafeBool<LineReader>` lets client code write `while (reader)`
to mean "a line is still available", without exposing an unsafe implicit
conversion to `bool`.

## Declared types

| Name | Kind | Bases | Template | Subclasses | Description |
|---|---|---|---|---|---|
| [`GPlatesFileIO::LineReader`](#gplatesfileiolinereader) | class | [`GPlatesUtils::SafeBool<LineReader>`](../utils/SafeBool.md)<br>`boost::noncopyable` | — | 0 | Reads lines in a text file allowing client to peek ahead one line. |

## Members

### `GPlatesFileIO::LineReader`

| Member | Kind | Type | Access | Description |
|---|---|---|---|---|
| `LineReader( QFile &input)` | constructor | `None` | public | — |
| `getline( QString &line)` | method | `bool` | public | Reads the next line and returns true if there is one. |
| `peekline( QString &line)` | method | `bool` | public | Peeks at the next line and returns true if there is one. |
| `boolean_test()` | method | `bool` | public | SafeBool base class provides operator bool(). |
| `line_number()` | method | `unsigned int` | public | — |
| `d_text_stream` | field | `QTextStream` | private | — |
| `d_line_number` | field | `unsigned int` | private | — |
| `d_buffered_line` | field | `QString` | private | — |
| `d_have_buffered_line` | field | `bool` | private | — |
| `readline( QString &line)` | method | `bool` | private | — |

## Free functions and macros

| Name | Kind | Type / body | Description |
|---|---|---|---|
| `GPLATES_FILEIO_LINEREADER_H` | macro | `None` | — |

## Notes

`line_number()` counts lines actually consumed via `getline`; a pending
`peekline` result does not advance it until `getline` is called to retrieve
it. The class does not own the `QFile` passed to its constructor — the caller
must keep it alive and open for the `LineReader`'s lifetime. As the header's
`TODO` notes, `QTextStream::readLine()` recognises `"\n"` and `"\r\n"` but not
the old classic-Mac `"\r"`-only convention, and a single file mixing newline
styles is not specially handled.

## Used by

| Unit | Component | References |
|---|---|---|
| [file-io/PlatesLineFormatReader](PlatesLineFormatReader.md) | file-io | 23 |
| [file-io/PlatesRotationFormatReader](PlatesRotationFormatReader.md) | file-io | 6 |

## Related

*None.*

## Explore

Run these from the `gplates-code` skill directory:

```bash
python scripts/gpq.py file src/file-io/LineReader.h
python scripts/gpq.py def GPlatesFileIO::LineReader --body
python scripts/gpq.py uses LineReader --kind class
python scripts/gpq.py hier LineReader
```
