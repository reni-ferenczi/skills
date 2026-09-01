# UnicodeString

[Book TOC](../../TOC.md) · [utils](../../components/utils.md) · cluster Community 116 · tier 1

| Source file | Kind | Lines |
|---|---|---|
| `src/utils/UnicodeString.h` | C++ | 219 |
| `src/utils/UnicodeString.cc` | C++ | 155 |

## Overview

[[[PROSE overview unit=utils/UnicodeString tier=1]]]
Replace this whole block, markers included, with 1-3 paragraphs: what this unit is, why it exists, and how it fits the surrounding design. Do not restate the tables below.
[[[/PROSE]]]

## Declared types

| Name | Kind | Bases | Template | Subclasses | Description |
|---|---|---|---|---|---|
| [`GPlatesUtils::UnicodeString`](#gplatesutilsunicodestring) | class | [`GPlatesUtils::QtStreamable<UnicodeString>`](QtStreamable.md) | — | 0 | A wrapper class around QString which mirrors the interface of ICU's UnicodeString as needed. http://icu-project.org/apiref/icu4c/classUnicodeString.html |

## Members

### `GPlatesUtils::UnicodeString`

| Member | Kind | Type | Access | Description |
|---|---|---|---|---|
| `UnicodeString()` | constructor | `None` | public | — |
| `UnicodeString( const QString &qs)` | constructor | `None` | public | — |
| `UnicodeString( const char *s)` | constructor | `None` | public | Construct a UnicodeString instance from a null-terminated array of chars. http://icu-project.org/apiref/icu4c/classUnicodeString.html#2e81e482db97eb362b6d0d62ff331ca3 It seems that this constructor is not explicit in ICU UnicodeString. |
| `isEmpty()` | method | `bool` | public | Determine if this string is empty. http://icu-project.org/apiref/icu4c/classUnicodeString.html#4004ef18a48eafbefc4bbc67cb12dcdf |
| `length()` | method | `boost::int32_t` | public | Return the length of the UnicodeString object. |
| `indexOf( const UnicodeString &text)` | method | `boost::int32_t` | public | Locate in this the first occurrence of the characters in text, using bitwise comparison. http://icu-project.org/apiref/icu4c/classUnicodeString.html#8f3956140af1d4d9d255e5da837b297c |
| `indexOf( const UnicodeString &text, boost::int32_t start)` | method | `boost::int32_t` | public | Locate in this the first occurrence of the characters in text starting at offset start, using bitwise comparison. http://icu-project.org/apiref/icu4c/classUnicodeString.html#81248ae2f8f2700f808c3fdf14a2ee67 |
| `extractBetween( boost::int32_t start, boost::int32_t limit, UnicodeString &target)` | method | `void` | public | Copy the characters in the range \[start, limit) into the UnicodeString target. http://icu-project.org/apiref/icu4c/classUnicodeString.html#d8946e6ca397f9b37a60a6a3c1a2ab93 |
| `removeBetween` | field | `UnicodeString` | public | Remove the characters in the range \[start, limit) from the UnicodeString object. http://icu-project.org/apiref/icu4c/classUnicodeString.html#46ca3daa10b0bcbcc4d75da6b7496f4e |
| `d_qstring` | field | `QString` | private | — |
| `transcribe( GPlatesScribe::Scribe &scribe, bool transcribed_construct_data)` | method | `GPlatesScribe::TranscribeResult` | private | — |

## Free functions and macros

| Name | Kind | Type / body | Description |
|---|---|---|---|
| `GPLATES_UTILS_UNICODESTRING_H` | macro | `None` | — |
| `GPLATES_ICU_BOOL` | macro_function | `(b)` | The ICU UnicodeString binary comparison operators returned a UBool rather than a bool, which caused problems. |
| `operator==( const UnicodeString &us1, const UnicodeString &us2)` | operator | `bool` | — |
| `operator<( const UnicodeString &us1, const UnicodeString &us2)` | operator | `bool` | — |
| `operator+( const UnicodeString &us1, const UnicodeString &us2)` | operator | `UnicodeString` | — |
| `operator<<` | variable | `ostream` | — |

## Notes

[[[PROSE notes unit=utils/UnicodeString tier=1]]]
Replace this whole block, markers included, with invariants, ownership, threading or gotchas that are not visible in the tables. Write *None.* if there is nothing worth saying.
[[[/PROSE]]]

## Used by

| Unit | Component | References |
|---|---|---|
| [file-io/PlatesFormatUtils](../file-io/PlatesFormatUtils.md) | file-io | 99 |
| [file-io/PlatesRotationFileProxy](../file-io/PlatesRotationFileProxy.md) | file-io | 54 |
| [app-logic/GeometryUtils](../app-logic/GeometryUtils.md) | app-logic | 48 |
| [file-io/OgrReader](../file-io/OgrReader.md) | file-io | 46 |
| [file-io/PlatesLineFormatReader](../file-io/PlatesLineFormatReader.md) | file-io | 37 |
| [property-values/GpmlOldPlatesHeader](../property-values/GpmlOldPlatesHeader.md) | property-values | 29 |
| [app-logic/FlowlineUtils](../app-logic/FlowlineUtils.md) | app-logic | 23 |
| [file-io/GsmlPropertyHandlers](../file-io/GsmlPropertyHandlers.md) | file-io | 20 |
| [file-io/XmlOutputInterface](../file-io/XmlOutputInterface.md) | file-io | 18 |
| [file-io/OgrFeatureCollectionWriter](../file-io/OgrFeatureCollectionWriter.md) | file-io | 17 |
| [file-io/PlatesLineFormatHeaderVisitor](../file-io/PlatesLineFormatHeaderVisitor.md) | file-io | 15 |
| [app-logic/PartitionFeatureUtils](../app-logic/PartitionFeatureUtils.md) | app-logic | 14 |
| [entry-points/gplates_demo_no_gui_main](../entry-points/gplates_demo_no_gui_main.md) | entry-points | 12 |
| [file-io/PlatesRotationFormatWriter](../file-io/PlatesRotationFormatWriter.md) | file-io | 11 |
| [qt-widgets/MetadataDialog](../qt-widgets/MetadataDialog.md) | qt-widgets | 10 |
| [utils/XmlNamespaces](XmlNamespaces.md) | utils | 10 |
| [presentation/TopologyNetworkVisualLayerParams](../presentation/TopologyNetworkVisualLayerParams.md) | presentation | 8 |
| [qt-widgets/PythonConsoleDialog](../qt-widgets/PythonConsoleDialog.md) | qt-widgets | 8 |
| [qt-widgets/TopologyNetworkResolverLayerOptionsWidget](../qt-widgets/TopologyNetworkResolverLayerOptionsWidget.md) | qt-widgets | 8 |
| [presentation/TranscribeSession](../presentation/TranscribeSession.md) | presentation | 7 |

*... and 119 more units.*

## Related

*None.*

## Explore

Run these from the `gplates-code` skill directory:

```bash
python scripts/gpq.py file src/utils/UnicodeString.h
python scripts/gpq.py def GPlatesUtils::UnicodeString --body
python scripts/gpq.py uses UnicodeString --kind class
python scripts/gpq.py hier UnicodeString
```
