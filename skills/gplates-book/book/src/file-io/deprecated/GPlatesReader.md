# GPlatesReader

[Book TOC](../../../TOC.md) · [file-io](../../../components/file-io.md) · cluster Community 489 · tier 3 · **deprecated**

| Source file | Kind | Lines |
|---|---|---|
| `src/file-io/deprecated/GPlatesReader.h` | C++ | 65 |
| `src/file-io/deprecated/GPlatesReader.cc` | C++ | 425 |

## Overview

[[[PROSE overview unit=file-io/deprecated/GPlatesReader tier=3]]]
Replace this whole block, markers included, with 1-3 paragraphs: what this unit is, why it exists, and how it fits the surrounding design. Do not restate the tables below.
[[[/PROSE]]]

## Declared types

| Name | Kind | Bases | Template | Subclasses | Description |
|---|---|---|---|---|---|
| [`Element`](#element) | typedef | — | — | 0 | — |
| [`Element_ptr`](#element_ptr) | typedef | — | — | 0 | — |
| [`ElementList`](#elementlist) | typedef | — | — | 0 | — |
| [`GPlatesFileIO::GPlatesReader`](#gplatesfileiogplatesreader) | class | [`Reader`](../ScalarField3DFileFormatReader.md) | — | 0 | GPlatesReader is responsible for converting an input stream in the GPlates data format into the GPlates internal representation. |

## Members

### `Element`

*None.*

### `Element_ptr`

*None.*

### `ElementList`

*None.*

### `GPlatesFileIO::GPlatesReader`

| Member | Kind | Type | Access | Description |
|---|---|---|---|---|
| `GPlatesReader(std::istream& istr)` | constructor | `None` | public | — |
| `Read()` | method | `GPlatesGeo::DataGroup` | public | Fill a DataGroup. |
| `_istr` | field | `std::istream` | private | — |

## Free functions and macros

| Name | Kind | Type / body | Description |
|---|---|---|---|
| `ReadError(const char* was_reading, unsigned int line)` | function | `void` | — |
| `InvalidDataError(const char* datatype, const char* got, const char* wanted, unsigned int line)` | function | `void` | — |
| `MultipleDefinitionError(const char* of_elem, const char* in_elem, const ElementList& list, unsigned int line)` | function | `void` | — |
| `ReadUnique(Element_ptr element, const char* to_read, const T& default_value)` | function | `T` | Read element to\_read, which should be unique within element. |
| `GetRotationGroupId(Element_ptr element)` | function | `GPlatesGlobal::rid_t` | Extract the RotationGroupId from the given element's content. |
| `GetDataType(Element_ptr element)` | function | `GeologicalData::DataType_t` | Extract the DataType from the given element's content. |
| `GetTimeWindow(Element_ptr element)` | function | `TimeWindow` | Extract the ages of appearance and disappearance from the given element's content. |
| `GetAttributes(Element_ptr)` | function | `GeologicalData::Attributes_t` | Extract the Attributes from the given element. |
| `GetLatLonPoint(Element_ptr element)` | function | `LatLonPoint` | Extract a LatLonPoint from the given text. |
| `GetPointData(Element_ptr element)` | function | `PointData` | Create a new PointData object from the given element. @pre element must refer to a \\\<pointdata\> element. |
| `GetCoordList(Element_ptr element)` | function | `PolylineOnSphere` | Create a new PolylineOnSphere object from the given element. @pre element must refer to a \\\<coordlist\> element. |
| `GetLineData(Element_ptr element)` | function | `LineData` | Create a new LineData object from the given element. @pre element must refer to a \\\<linedata\> element. |
| `GetDataGroup(Element_ptr element)` | function | `DataGroup` | Create a new DataGroup object from the given element. @pre element must refer to a \\\<datagroup\> element. @warning This method rearranges the order of the children. |
| `GetRootDataGroup(Element_ptr element)` | function | `DataGroup` | Handle meta data (title, and meta elements) in addition to normal datagroup stuff. |
| `_GPLATES_FILEIO_GPLATESREADER_H_` | macro | `None` | — |

## Notes

[[[PROSE notes unit=file-io/deprecated/GPlatesReader tier=3]]]
Replace this whole block, markers included, with invariants, ownership, threading or gotchas that are not visible in the tables. Write *None.* if there is nothing worth saying.
[[[/PROSE]]]

## Used by

| Unit | Component | References |
|---|---|---|
| [deprecated/controls/File](../../deprecated/controls/File.md) | deprecated | 4 |
| [deprecated/controls/Reconstruct](../../deprecated/controls/Reconstruct.md) | deprecated | 3 |
| [file-io/deprecated/NetCDFWriter](NetCDFWriter.md) | file-io | 1 |

## Related

*None.*

## Explore

Run these from the `gplates-code` skill directory:

```bash
python scripts/gpq.py file src/file-io/deprecated/GPlatesReader.h
python scripts/gpq.py def GPlatesFileIO::GPlatesReader --body
python scripts/gpq.py uses GPlatesReader --kind class
python scripts/gpq.py hier GPlatesReader
```
