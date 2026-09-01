# StringContentTypeGenerator

[Book TOC](../../TOC.md) · [model](../../components/model.md) · cluster Community 756 · tier 2

| Source file | Kind | Lines |
|---|---|---|
| `src/model/StringContentTypeGenerator.h` | C++ | 151 |

## Overview

[[[PROSE overview unit=model/StringContentTypeGenerator tier=2]]]
Replace this whole block, markers included, with 1-3 paragraphs: what this unit is, why it exists, and how it fits the surrounding design. Do not restate the tables below.
[[[/PROSE]]]

## Declared types

| Name | Kind | Bases | Template | Subclasses | Description |
|---|---|---|---|---|---|
| [`GPlatesModel::StringContentTypeGenerator`](#gplatesmodelstringcontenttypegenerator) | class | — | `<typename SingletonType>` | 0 | This class provides an efficient means of containing text content, which is a Unicode string. |

## Members

### `GPlatesModel::StringContentTypeGenerator`

| Member | Kind | Type | Access | Description |
|---|---|---|---|---|
| `is_loaded( const GPlatesUtils::UnicodeString &s)` | method | `bool` | public | Determine whether an arbitrary Unicode string is a member of the collection of loaded text content instances (without inserting the Unicode string into the collection). |
| `StringContentTypeGenerator( const GPlatesUtils::UnicodeString &s)` | constructor | `None` | public | Instantiate a new StringContent instance for the given string. explicit |
| `is_equal_to( const StringContentTypeGenerator &other)` | method | `bool` | public | Determine whether another StringContent instance contains the same text content as this instance. |
| `d_ss_iter` | field | `GPlatesUtils::StringSet::SharedIterator` | private | — |
| `transcribe_construct_data( GPlatesScribe::Scribe &scribe, GPlatesScribe::ConstructObject< StringContentTypeGenerator<SingletonType> > &string_content)` | method | `GPlatesScribe::TranscribeResult` | private | NOTE: Implementation is in "TranscribeStringContentTypeGenerator.h" to avoid including "Scribe.h" here. |
| `transcribe( GPlatesScribe::Scribe &scribe, bool transcribed_construct_data)` | method | `GPlatesScribe::TranscribeResult` | private | NOTE: Implementation is in "TranscribeStringContentTypeGenerator.h" to avoid including "Scribe.h" here. |

## Free functions and macros

| Name | Kind | Type / body | Description |
|---|---|---|---|
| `GPLATES_MODEL_STRINGCONTENTTYPEGENERATOR_H` | macro | `None` | — |
| `operator==( const StringContentTypeGenerator<SingletonType> &c1, const StringContentTypeGenerator<SingletonType> &c2)` | operator | `bool` | — |
| `operator!=( const StringContentTypeGenerator<SingletonType> &c1, const StringContentTypeGenerator<SingletonType> &c2)` | operator | `bool` | — |

## Notes

[[[PROSE notes unit=model/StringContentTypeGenerator tier=2]]]
Replace this whole block, markers included, with invariants, ownership, threading or gotchas that are not visible in the tables. Write *None.* if there is nothing worth saying.
[[[/PROSE]]]

## Used by

| Unit | Component | References |
|---|---|---|
| [model/TranscribeStringContentTypeGenerator](TranscribeStringContentTypeGenerator.md) | model | 7 |
| [property-values/EnumerationContent](../property-values/EnumerationContent.md) | property-values | 4 |
| [property-values/TextContent](../property-values/TextContent.md) | property-values | 4 |
| [property-values/TimescaleBand](../property-values/TimescaleBand.md) | property-values | 4 |
| [property-values/TimescaleName](../property-values/TimescaleName.md) | property-values | 4 |
| [file-io/XmlWriter](../file-io/XmlWriter.md) | file-io | 2 |
| [model/XmlAttributeValue](XmlAttributeValue.md) | model | 2 |

## Related

*None.*

## Explore

Run these from the `gplates-code` skill directory:

```bash
python scripts/gpq.py file src/model/StringContentTypeGenerator.h
python scripts/gpq.py def GPlatesModel::StringContentTypeGenerator --body
python scripts/gpq.py uses StringContentTypeGenerator --kind class
python scripts/gpq.py hier StringContentTypeGenerator
```
