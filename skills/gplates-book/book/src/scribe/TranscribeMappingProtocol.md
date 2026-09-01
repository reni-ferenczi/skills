# TranscribeMappingProtocol

[Book TOC](../../TOC.md) · [scribe](../../components/scribe.md) · cluster Community 89 · tier 2

| Source file | Kind | Lines |
|---|---|---|
| `src/scribe/TranscribeMappingProtocol.h` | C++ | 327 |

## Overview

[[[PROSE overview unit=scribe/TranscribeMappingProtocol tier=2]]]
Replace this whole block, markers included, with 1-3 paragraphs: what this unit is, why it exists, and how it fits the surrounding design. Do not restate the tables below.
[[[/PROSE]]]

## Declared types

| Name | Kind | Bases | Template | Subclasses | Description |
|---|---|---|---|---|---|
| [`GPlatesScribe::TranscribeMap`](#gplatesscribetranscribemap) | struct | — | `<class MapType>` | 1 | Specialisations of this class implement mapping functions used in transcribe\_mapping\_protocol. |

## Members

### `GPlatesScribe::TranscribeMap`

| Member | Kind | Type | Access | Description |
|---|---|---|---|---|
| `map_type` | typedef | `MapType` | public | The following typedefs and functions should be implemented in specialisation. |
| `key_type` | typedef | `typename map_type::key_type` | public | — |
| `mapped_type` | typedef | `typename map_type::mapped_type` | public | — |
| `map_iterator` | typedef | `typename map_type::iterator` | public | — |
| `map_const_iterator` | typedef | `typename map_type::const_iterator` | public | — |
| `get_length( const map_type &map)` | method | `unsigned int` | public | Get length of existing map (for saving). |
| `get_items( const map_type &map)` | method | `std::pair<map_const_iterator, map_const_iterator>` | public | Get (begin, end) range of const-iterators over existing map (for loading). |
| `get_items( map_type &map)` | method | `std::pair<map_iterator, map_iterator>` | public | Get (begin, end) range of iterators over existing map (for saving). |
| `get_key` | field | `key_type` | public | Get the key associated with the specified iterator (for saving). |
| `get_value` | field | `mapped_type` | public | Get the value associated with the specified iterator (for saving and loading). |
| `clear( map_type &map)` | method | `void` | public | Make sure map is empty (for loading). |
| `add_item( map_type &map, const key_type &key, const mapped_type &value)` | method | `boost::optional<map_iterator>` | public | Add a loaded item to a map (for loading). |

## Free functions and macros

| Name | Kind | Type / body | Description |
|---|---|---|---|
| `GPLATES_SCRIBE_TRANSCRIBEMAPPINGPROTOCOL_H` | macro | `None` | — |
| `transcribe_mapping_protocol( const GPlatesUtils::CallStack::Trace &transcribe_source, // Use 'TRANSCRIBE_SOURCE' here Scribe &scribe, MapType &map)` | function | `TranscribeResult` | Used to ensure different mapping types are transcribed such that they can be switched without breaking backward/forward compatibility. |
| `transcribe_mapping_protocol( const GPlatesUtils::CallStack::Trace &transcribe_source, Scribe &scribe, MapType &map)` | function | `TranscribeResult` | — |
| `relocated_mapping_protocol( Scribe &scribe, const MapType &relocated_map, const MapType &transcribed_map)` | function | `void` | — |

## Notes

[[[PROSE notes unit=scribe/TranscribeMappingProtocol tier=2]]]
Replace this whole block, markers included, with invariants, ownership, threading or gotchas that are not visible in the tables. Write *None.* if there is nothing worth saying.
[[[/PROSE]]]

## Used by

| Unit | Component | References |
|---|---|---|
| [scribe/TranscribeStd](TranscribeStd.md) | scribe | 7 |
| [scribe/TranscribeQt](TranscribeQt.md) | scribe | 6 |

## Related

*None.*

## Explore

Run these from the `gplates-code` skill directory:

```bash
python scripts/gpq.py file src/scribe/TranscribeMappingProtocol.h
python scripts/gpq.py def GPlatesScribe::TranscribeMap --body
python scripts/gpq.py uses TranscribeMap --kind struct
python scripts/gpq.py hier TranscribeMap
```
