# ScribeObjectTag

[Book TOC](../../TOC.md) · [scribe](../../components/scribe.md) · cluster Community 738 · tier 2

| Source file | Kind | Lines |
|---|---|---|
| `src/scribe/ScribeObjectTag.h` | C++ | 468 |
| `src/scribe/ScribeObjectTag.cc` | C++ | 134 |

## Overview

[[[PROSE overview unit=scribe/ScribeObjectTag tier=2]]]
Replace this whole block, markers included, with 1-3 paragraphs: what this unit is, why it exists, and how it fits the surrounding design. Do not restate the tables below.
[[[/PROSE]]]

## Declared types

| Name | Kind | Bases | Template | Subclasses | Description |
|---|---|---|---|---|---|
| [`GPlatesScribe::ObjectTag`](#gplatesscribeobjecttag) | class | — | — | 0 | An object tag is used to identify a transcribed object within the transcription. |

## Members

### `GPlatesScribe::ObjectTag`

| Member | Kind | Type | Access | Description |
|---|---|---|---|---|
| `SectionType` | enum | `None` | public | Each section in an object tag can be: - a tag (name/version), or - an array index, or - an array size. |
| `Section` | class | `None` | public | An object tag is divided into one or more sections. |
| `ObjectTag()` | constructor | `None` | public | An empty object tag. |
| `ObjectTag( const std::string &tag_name, unsigned int tag_version = 0)` | constructor | `None` | public | Create a single-entry object tag from the specified tag name and version. |
| `ObjectTag( const char *tag_name, unsigned int tag_version = 0)` | constructor | `None` | public | Same as other constructor but the tag name is specified as a NULL-terminated string. |
| `operator()( const std::string &suffix_tag_name, unsigned int suffix_tag_version = 0)` | operator | `ObjectTag` | public | Returns a copy of this object tag, but with a suffix tag appended. |
| `operator[]( unsigned int array_index)` | operator | `ObjectTag` | public | Returns a copy of this object tag, but with an additional array indexation using the sequence protocol (ie, 'item' for array items). |
| `sequence_item( unsigned int sequence_index)` | method | `ObjectTag` | public | Same as operator\[\]. |
| `map_item_key( unsigned int map_index)` | method | `ObjectTag` | public | Returns a copy of this object tag, but with an additional array indexation using the mapping protocol (ie, 'item\_key' for map keys). |
| `map_item_value( unsigned int map_index)` | method | `ObjectTag` | public | Returns a copy of this object tag, but with an additional array indexation using the mapping protocol (ie, 'item\_value' for map values). |
| `array_item( unsigned int array_index, const std::string &array_item_tag_name, unsigned int array_item_tag_version = 0)` | method | `ObjectTag` | public | Same as sequence\_item, map\_item\_key and map\_item\_value except can specify the array indexing tag name/version instead of relying on the sequence protocol (which uses 'item' for sequence items) or the mapping protocol (which uses 'item\_key' ... |
| `sequence_size()` | method | `ObjectTag` | public | Returns a copy of this object tag that will be used to query the size of an array using the sequence protocol (ie, 'size' for sequence size). |
| `map_size()` | method | `ObjectTag` | public | Returns a copy of this object tag that will be used to query the size of a map using the mapping protocol (ie, 'size' for map size). |
| `array_size( const std::string &array_size_tag_name, unsigned int array_size_tag_version = 0)` | method | `ObjectTag` | public | Same as sequence\_size and map\_size except can specify the array size tag name/version (instead of relying on sequence or mapping protocol - both of which use 'size' for array size). |
| `get_sections` | field | `std::vector<Section>` | public | Returns the sections of this object tag. |
| `SEQUENCE_PROTOCOL_ITEM_TAG_NAME` | field | `std::string` | private | The object tag name/version used by the sequence protocol for the sequence items. |
| `SEQUENCE_PROTOCOL_ITEM_TAG_VERSION` | field | `unsigned int` | private | — |
| `SEQUENCE_PROTOCOL_SIZE_TAG_NAME` | field | `std::string` | private | The object tag name/version used by the sequence protocol for the sequence size. |
| `SEQUENCE_PROTOCOL_SIZE_TAG_VERSION` | field | `unsigned int` | private | — |
| `MAPPING_PROTOCOL_ITEM_KEY_TAG_NAME` | field | `std::string` | private | The object tag name/version used by the mapping protocol for the map keys. |
| `MAPPING_PROTOCOL_ITEM_KEY_TAG_VERSION` | field | `unsigned int` | private | — |
| `MAPPING_PROTOCOL_ITEM_VALUE_TAG_NAME` | field | `std::string` | private | The object tag name/version used by the mapping protocol for the map values. |
| `MAPPING_PROTOCOL_ITEM_VALUE_TAG_VERSION` | field | `unsigned int` | private | — |
| `MAPPING_PROTOCOL_SIZE_TAG_NAME` | field | `std::string` | private | The object tag name/version used by the mapping protocol for the map size. |
| `MAPPING_PROTOCOL_SIZE_TAG_VERSION` | field | `unsigned int` | private | — |
| `d_sections` | field | `std::vector<Section>` | private | — |
| `ObjectTag( const ObjectTag &rhs, unsigned int num_sections_to_reserve)` | constructor | `None` | private | A small optimisation to reduce std::vector reallocations by reserving enough space for a subsequent 'push\_back()'. |
| `add_tag_section( const std::string &tag_name, unsigned int tag_version)` | method | `ObjectTag` | private | — |
| `add_array_index_section( unsigned int array_index, const std::string &array_item_tag_name, unsigned int array_item_tag_version)` | method | `ObjectTag` | private | — |
| `add_array_size_section( const std::string &array_size_tag_name, unsigned int array_size_tag_version)` | method | `ObjectTag` | private | — |

## Free functions and macros

| Name | Kind | Type / body | Description |
|---|---|---|---|
| `SEQUENCE_PROTOCOL_ITEM_TAG_NAME` | variable | `std::string` | — |
| `SEQUENCE_PROTOCOL_ITEM_TAG_VERSION` | variable | `unsigned int` | — |
| `SEQUENCE_PROTOCOL_SIZE_TAG_NAME` | variable | `std::string` | — |
| `SEQUENCE_PROTOCOL_SIZE_TAG_VERSION` | variable | `unsigned int` | — |
| `MAPPING_PROTOCOL_ITEM_KEY_TAG_NAME` | variable | `std::string` | — |
| `MAPPING_PROTOCOL_ITEM_KEY_TAG_VERSION` | variable | `unsigned int` | — |
| `MAPPING_PROTOCOL_ITEM_VALUE_TAG_NAME` | variable | `std::string` | — |
| `MAPPING_PROTOCOL_ITEM_VALUE_TAG_VERSION` | variable | `unsigned int` | — |
| `MAPPING_PROTOCOL_SIZE_TAG_NAME` | variable | `std::string` | — |
| `MAPPING_PROTOCOL_SIZE_TAG_VERSION` | variable | `unsigned int` | — |
| `GPLATES_SCRIBE_SCRIBEOBJECTTAG_H` | macro | `None` | — |

## Notes

[[[PROSE notes unit=scribe/ScribeObjectTag tier=2]]]
Replace this whole block, markers included, with invariants, ownership, threading or gotchas that are not visible in the tables. Write *None.* if there is nothing worth saying.
[[[/PROSE]]]

## Used by

| Unit | Component | References |
|---|---|---|
| [presentation/TranscribeSession](../presentation/TranscribeSession.md) | presentation | 66 |
| [scribe/TranscriptionScribeContext](TranscriptionScribeContext.md) | scribe | 48 |
| [scribe/Scribe](Scribe.md) | scribe | 40 |
| [scribe/TranscribeUtils](TranscribeUtils.md) | scribe | 27 |
| [scribe/TranscribeMappingProtocol](TranscribeMappingProtocol.md) | scribe | 10 |
| [scribe/TranscribeArray](TranscribeArray.md) | scribe | 8 |
| [scribe/ScribeInternalAccess](ScribeInternalAccess.md) | scribe | 7 |
| [scribe/TranscribeSequenceProtocol](TranscribeSequenceProtocol.md) | scribe | 4 |
| [data-mining/CoRegConfigurationTable](../data-mining/CoRegConfigurationTable.md) | data-mining | 3 |
| [scribe/TranscribeQt](TranscribeQt.md) | scribe | 2 |
| [gui/BuiltinColourPaletteType](../gui/BuiltinColourPaletteType.md) | gui | 1 |

## Related

*None.*

## Explore

Run these from the `gplates-code` skill directory:

```bash
python scripts/gpq.py file src/scribe/ScribeObjectTag.h
python scripts/gpq.py def GPlatesScribe::ObjectTag --body
python scripts/gpq.py uses ObjectTag --kind class
python scripts/gpq.py hier ObjectTag
```
