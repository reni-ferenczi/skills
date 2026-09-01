# TranscribeStd

[Book TOC](../../TOC.md) · [scribe](../../components/scribe.md) · cluster Community 563 · tier 3

| Source file | Kind | Lines |
|---|---|---|
| `src/scribe/TranscribeStd.h` | C++ | 900 |

## Overview

[[[PROSE overview unit=scribe/TranscribeStd tier=3]]]
Replace this whole block, markers included, with 1-3 paragraphs: what this unit is, why it exists, and how it fits the surrounding design. Do not restate the tables below.
[[[/PROSE]]]

## Declared types

| Name | Kind | Bases | Template | Subclasses | Description |
|---|---|---|---|---|---|
| [`GPlatesScribe::TranscribeSequence< std::set<T, Compare, Allocator> >`](#gplatesscribetranscribesequence-stdsett-compare-allocator-) | struct | — | `<typename T, class Compare, class Allocator>` | 0 | std::set transcribe sequence protocol implementation. |
| [`GPlatesScribe::TranscribeSequence< std::multiset<T, Compare, Allocator> >`](#gplatesscribetranscribesequence-stdmultisett-compare-allocator-) | struct | — | `<typename T, class Compare, class Allocator>` | 0 | std::multiset transcribe sequence protocol implementation. |
| [`GPlatesScribe::TranscribeMap< std::map<Key, T, Compare, Allocator> >`](#gplatesscribetranscribemap-stdmapkey-t-compare-allocator-) | struct | — | `<typename Key, typename T, class Compare, class Allocator>` | 0 | std::map transcribe mapping protocol implementation. |
| [`GPlatesScribe::TranscribeMap< std::multimap<Key, T, Compare, Allocator> >`](#gplatesscribetranscribemap-stdmultimapkey-t-compare-allocator-) | struct | — | `<typename Key, typename T, class Compare, class Allocator>` | 0 | std::multimap transcribe mapping protocol implementation. |

## Members

### `GPlatesScribe::TranscribeSequence< std::set<T, Compare, Allocator> >`

| Member | Kind | Type | Access | Description |
|---|---|---|---|---|
| `sequence_type` | typedef | `std::set<T, Compare, Allocator>` | public | — |
| `item_type` | typedef | `typename sequence_type::value_type` | public | — |
| `sequence_iterator` | typedef | `typename sequence_type::iterator` | public | — |
| `sequence_const_iterator` | typedef | `typename sequence_type::const_iterator` | public | — |
| `get_length( const sequence_type &sequence)` | method | `unsigned int` | public | — |
| `get_items( const sequence_type &sequence)` | method | `std::pair<sequence_const_iterator, sequence_const_iterator>` | public | — |
| `get_items( sequence_type &sequence)` | method | `std::pair<sequence_iterator, sequence_iterator>` | public | — |
| `clear( sequence_type &sequence)` | method | `void` | public | — |
| `add_item( sequence_type &sequence, const item_type &item)` | method | `bool` | public | — |

### `GPlatesScribe::TranscribeSequence< std::multiset<T, Compare, Allocator> >`

| Member | Kind | Type | Access | Description |
|---|---|---|---|---|
| `sequence_type` | typedef | `std::multiset<T, Compare, Allocator>` | public | — |
| `item_type` | typedef | `typename sequence_type::value_type` | public | — |
| `sequence_iterator` | typedef | `typename sequence_type::iterator` | public | — |
| `sequence_const_iterator` | typedef | `typename sequence_type::const_iterator` | public | — |
| `get_length( const sequence_type &sequence)` | method | `unsigned int` | public | — |
| `get_items( const sequence_type &sequence)` | method | `std::pair<sequence_const_iterator, sequence_const_iterator>` | public | — |
| `get_items( sequence_type &sequence)` | method | `std::pair<sequence_iterator, sequence_iterator>` | public | — |
| `clear( sequence_type &sequence)` | method | `void` | public | — |
| `add_item( sequence_type &sequence, const item_type &item)` | method | `bool` | public | — |

### `GPlatesScribe::TranscribeMap< std::map<Key, T, Compare, Allocator> >`

| Member | Kind | Type | Access | Description |
|---|---|---|---|---|
| `map_type` | typedef | `std::map<Key, T, Compare, Allocator>` | public | — |
| `key_type` | typedef | `typename map_type::key_type` | public | — |
| `mapped_type` | typedef | `typename map_type::mapped_type` | public | — |
| `map_iterator` | typedef | `typename map_type::iterator` | public | — |
| `map_const_iterator` | typedef | `typename map_type::const_iterator` | public | — |
| `get_length( const map_type &map)` | method | `unsigned int` | public | — |
| `get_items( const map_type &map)` | method | `std::pair<map_const_iterator, map_const_iterator>` | public | — |
| `get_items( map_type &map)` | method | `std::pair<map_iterator, map_iterator>` | public | — |
| `clear( map_type &map)` | method | `void` | public | — |
| `add_item( map_type &map, const key_type &key, const mapped_type &value)` | method | `boost::optional<map_iterator>` | public | — |

### `GPlatesScribe::TranscribeMap< std::multimap<Key, T, Compare, Allocator> >`

| Member | Kind | Type | Access | Description |
|---|---|---|---|---|
| `map_type` | typedef | `std::multimap<Key, T, Compare, Allocator>` | public | — |
| `key_type` | typedef | `typename map_type::key_type` | public | — |
| `mapped_type` | typedef | `typename map_type::mapped_type` | public | — |
| `map_iterator` | typedef | `typename map_type::iterator` | public | — |
| `map_const_iterator` | typedef | `typename map_type::const_iterator` | public | — |
| `get_length( const map_type &map)` | method | `unsigned int` | public | — |
| `get_items( const map_type &map)` | method | `std::pair<map_const_iterator, map_const_iterator>` | public | — |
| `get_items( map_type &map)` | method | `std::pair<map_iterator, map_iterator>` | public | — |
| `clear( map_type &map)` | method | `void` | public | — |
| `add_item( map_type &map, const key_type &key, const mapped_type &value)` | method | `boost::optional<map_iterator>` | public | — |

## Free functions and macros

| Name | Kind | Type / body | Description |
|---|---|---|---|
| `GPLATES_SCRIBE_TRANSCRIBESTD_H` | macro | `None` | — |
| `transcribe( Scribe &scribe, std::pair<T1, T2> &pair_object, bool transcribed_construct_data)` | function | `TranscribeResult` | — |
| `transcribe_construct_data( Scribe &scribe, ConstructObject< std::pair<T1, T2> > &pair_object)` | function | `TranscribeResult` | — |
| `transcribe( Scribe &scribe, std::unique_ptr<T> &unique_ptr_object, bool transcribed_construct_data)` | function | `TranscribeResult` | — |
| `transcribe( Scribe &scribe, std::deque<T, Allocator> &deque_object, bool transcribed_construct_data)` | function | `TranscribeResult` | — |
| `relocated( Scribe &scribe, const std::deque<T, Allocator> &relocated_deque_object, const std::deque<T, Allocator> &transcribed_deque_object)` | function | `void` | — |
| `transcribe( Scribe &scribe, std::list<T, Allocator> &list_object, bool transcribed_construct_data)` | function | `TranscribeResult` | — |
| `relocated( Scribe &scribe, const std::list<T, Allocator> &relocated_list_object, const std::list<T, Allocator> &transcribed_list_object)` | function | `void` | — |
| `transcribe( Scribe &scribe, std::map<Key, T, Compare, Allocator> &map_object, bool transcribed_construct_data)` | function | `TranscribeResult` | — |
| `relocated( Scribe &scribe, const std::map<Key, T, Compare, Allocator> &relocated_map_object, const std::map<Key, T, Compare, Allocator> &transcribed_map_object)` | function | `void` | — |
| `transcribe( Scribe &scribe, std::multimap<Key, T, Compare, Allocator> &multimap_object, bool transcribed_construct_data)` | function | `TranscribeResult` | — |
| `relocated( Scribe &scribe, const std::multimap<Key, T, Compare, Allocator> &relocated_multimap_object, const std::multimap<Key, T, Compare, Allocator> &transcribed_multimap_object)` | function | `void` | — |
| `transcribe( Scribe &scribe, std::set<T, Compare, Allocator> &set_object, bool transcribed_construct_data)` | function | `TranscribeResult` | — |
| `relocated( Scribe &scribe, const std::set<T, Compare, Allocator> &relocated_set_object, const std::set<T, Compare, Allocator> &transcribed_set_object)` | function | `void` | — |
| `transcribe( Scribe &scribe, std::multiset<T, Compare, Allocator> &multiset_object, bool transcribed_construct_data)` | function | `TranscribeResult` | — |
| `relocated( Scribe &scribe, const std::multiset<T, Compare, Allocator> &relocated_multiset_object, const std::multiset<T, Compare, Allocator> &transcribed_multiset_object)` | function | `void` | — |
| `transcribe( Scribe &scribe, std::priority_queue<T, Container, Compare> &priority_queue_object, bool transcribed_construct_data)` | function | `TranscribeResult` | — |
| `relocated( Scribe &scribe, const std::priority_queue<T, Container, Compare> &relocated_priority_queue_object, const std::priority_queue<T, Container, Compare> &transcribed_priority_queue_object)` | function | `void` | — |
| `transcribe( Scribe &scribe, std::queue<T, Container> &queue_object, bool transcribed_construct_data)` | function | `TranscribeResult` | — |
| `relocated( Scribe &scribe, const std::queue<T, Container> &relocated_queue_object, const std::queue<T, Container> &transcribed_queue_object)` | function | `void` | — |
| `transcribe( Scribe &scribe, std::stack<T, Container> &stack_object, bool transcribed_construct_data)` | function | `TranscribeResult` | — |
| `relocated( Scribe &scribe, const std::stack<T, Container> &relocated_stack_object, const std::stack<T, Container> &transcribed_stack_object)` | function | `void` | — |
| `transcribe( Scribe &scribe, std::vector<T, Allocator> &vector_object, bool transcribed_construct_data)` | function | `TranscribeResult` | — |
| `relocated( Scribe &scribe, const std::vector<T, Allocator> &relocated_vector_object, const std::vector<T, Allocator> &transcribed_vector_object)` | function | `void` | — |

## Notes

[[[PROSE notes unit=scribe/TranscribeStd tier=3]]]
Replace this whole block, markers included, with invariants, ownership, threading or gotchas that are not visible in the tables. Write *None.* if there is nothing worth saying.
[[[/PROSE]]]

## Used by

| Unit | Component | References |
|---|---|---|
| [scribe/TranscribeExternal](TranscribeExternal.md) | scribe | 1 |

## Related

*None.*

## Explore

Run these from the `gplates-code` skill directory:

```bash
python scripts/gpq.py file src/scribe/TranscribeStd.h
python scripts/gpq.py def GPlatesScribe::TranscribeMap< std::map<Key, T, Compare, Allocator> > --body
python scripts/gpq.py uses TranscribeMap< std::map<Key, T, Compare, Allocator> > --kind struct
python scripts/gpq.py hier TranscribeMap< std::map<Key, T, Compare, Allocator> >
```
