# LineReader

[Book TOC](../../TOC.md) · [file-io](../../components/file-io.md) · cluster Community 411 · tier 2

| Source file | Kind | Lines |
|---|---|---|
| `src/file-io/LineReader.h` | C++ | 120 |
| `src/file-io/LineReader.cc` | C++ | 101 |

## Overview

[[[PROSE overview unit=file-io/LineReader tier=2]]]
Replace this whole block, markers included, with 1-3 paragraphs: what this unit is, why it exists, and how it fits the surrounding design. Do not restate the tables below.
[[[/PROSE]]]

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

[[[PROSE notes unit=file-io/LineReader tier=2]]]
Replace this whole block, markers included, with invariants, ownership, threading or gotchas that are not visible in the tables. Write *None.* if there is nothing worth saying.
[[[/PROSE]]]

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
