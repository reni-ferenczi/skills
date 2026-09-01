# TranscribeMappingProtocol

[Book TOC](../../TOC.md) · [scribe](../../components/scribe.md) · cluster Community 89 · tier 2

| Source file | Kind | Lines |
|---|---|---|
| `src/scribe/TranscribeMappingProtocol.h` | C++ | 327 |

## Overview

`transcribe_mapping_protocol()` gives every associative-container-like type — `std::map`, `std::multimap`, `QMap`, `QMultiMap` — a single, uniform on-archive layout: a length, then that many key/value pairs each tagged with `ObjectTag::map_item_key()`/`map_item_value()`. Because the layout does not depend on the container's own implementation, an archive written with one mapping type can, in principle, be reloaded into a different one, and the format is stable even if the underlying container's memory layout changes between GPlates versions.

`TranscribeMap<MapType>` is the adaptor: the primary template only declares the operations `transcribe_mapping_protocol()` needs (`get_length()`, `get_items()`, `get_key()`/`get_value()`, `clear()`, `add_item()`), and each concrete mapping type must supply a specialisation implementing them (see `TranscribeStd.h`/`TranscribeQt.h`). `transcribe_mapping_protocol()` then drives loading and saving purely in terms of that adaptor, and `relocated_mapping_protocol()` is its companion for propagating a `Scribe::relocated()` notification (when a transcribed map is copied to its final location) onto each value in the map, since values are tracked as objects for identity but keys are not.

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

- If any key or value in the map returns `TRANSCRIBE_UNKNOWN_TYPE` while loading (for example a polymorphic pointer to a derived class the current build doesn't know), the whole map load fails with `TRANSCRIBE_UNKNOWN_TYPE` and the map is cleared — there is no way to skip just the unrecognised item through this protocol; a caller that needs to skip bad items must reimplement the protocol manually using the `ObjectTag` scheme described in the header.
- Only values are tracked/relocated (via `TRACK` and `scribe.relocated()`); keys are transcribed untracked, so `relocated_mapping_protocol()` only walks and relocates values, not keys.
- `add_item()` returning `boost::none` (e.g. a duplicate key for a type that forbids them) silently drops that item rather than failing the whole transcription.

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
