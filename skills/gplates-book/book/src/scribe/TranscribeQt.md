# TranscribeQt

[Book TOC](../../TOC.md) · [scribe](../../components/scribe.md) · cluster Community 919 · tier 2

| Source file | Kind | Lines |
|---|---|---|
| `src/scribe/TranscribeQt.h` | C++ | 432 |
| `src/scribe/TranscribeQt.cc` | C++ | 409 |

## Overview

[[[PROSE overview unit=scribe/TranscribeQt tier=2]]]
Replace this whole block, markers included, with 1-3 paragraphs: what this unit is, why it exists, and how it fits the surrounding design. Do not restate the tables below.
[[[/PROSE]]]

## Declared types

| Name | Kind | Bases | Template | Subclasses | Description |
|---|---|---|---|---|---|
| [`GPlatesScribe::TranscribeSequence< QSet<T> >`](#gplatesscribetranscribesequence-qsett-) | struct | — | `<typename T>` | 0 | QSet transcribe sequence protocol implementation. |
| [`GPlatesScribe::TranscribeMap< QMap<Key, T> >`](#gplatesscribetranscribemap-qmapkey-t-) | struct | — | `<class Key, class T>` | 0 | QMap transcribe mapping protocol implementation. |
| [`GPlatesScribe::TranscribeMap< QMultiMap<Key, T> >`](#gplatesscribetranscribemap-qmultimapkey-t-) | struct | [`TranscribeMap< QMap<Key, T> >`](TranscribeMappingProtocol.md) | `<class Key, class T>` | 0 | QMultiMap transcribe mapping protocol implementation. |

## Members

### `GPlatesScribe::TranscribeSequence< QSet<T> >`

| Member | Kind | Type | Access | Description |
|---|---|---|---|---|
| `sequence_type` | typedef | `QSet<T>` | public | — |
| `item_type` | typedef | `typename sequence_type::value_type` | public | — |
| `sequence_iterator` | typedef | `typename sequence_type::iterator` | public | — |
| `sequence_const_iterator` | typedef | `typename sequence_type::const_iterator` | public | — |
| `get_length( const sequence_type &sequence)` | method | `unsigned int` | public | — |
| `get_items( const sequence_type &sequence)` | method | `std::pair<sequence_const_iterator, sequence_const_iterator>` | public | — |
| `get_items( sequence_type &sequence)` | method | `std::pair<sequence_iterator, sequence_iterator>` | public | — |
| `clear( sequence_type &sequence)` | method | `void` | public | — |
| `add_item( sequence_type &sequence, const item_type &item)` | method | `bool` | public | — |

### `GPlatesScribe::TranscribeMap< QMap<Key, T> >`

| Member | Kind | Type | Access | Description |
|---|---|---|---|---|
| `map_type` | typedef | `QMap<Key, T>` | public | — |
| `key_type` | typedef | `typename map_type::key_type` | public | — |
| `mapped_type` | typedef | `typename map_type::mapped_type` | public | — |
| `map_iterator` | typedef | `typename map_type::iterator` | public | — |
| `map_const_iterator` | typedef | `typename map_type::const_iterator` | public | — |
| `get_length( const map_type &map)` | method | `unsigned int` | public | — |
| `get_items( const map_type &map)` | method | `std::pair<map_const_iterator, map_const_iterator>` | public | — |
| `get_items( map_type &map)` | method | `std::pair<map_iterator, map_iterator>` | public | — |
| `clear( map_type &map)` | method | `void` | public | — |
| `add_item( map_type &map, const key_type &key, const mapped_type &value)` | method | `boost::optional<map_iterator>` | public | — |

### `GPlatesScribe::TranscribeMap< QMultiMap<Key, T> >`

*None.*

## Free functions and macros

| Name | Kind | Type / body | Description |
|---|---|---|---|
| `C_LOCALE(QLocale::c())` | function | `QLocale` | Use the "C" locale to convert QDateTime to and from the archive. |
| `TRANSCRIBE_QT_STREAM_VERSION` | variable | `unsigned int` | The QDataStream serialisation version used for streaming QVariant and QDateTime. |
| `TRANSCRIBE_QT_STREAM_BYTE_ORDER` | variable | `QDataStream::ByteOrder` | The QDataStream byte order used for streaming QVariant and QDateTime. |
| `GPLATES_SCRIBE_TRANSCRIBEQT_H` | macro | `None` | — |
| `transcribe( Scribe &scribe, QByteArray &qbytearray_object, bool transcribed_construct_data)` | function | `TranscribeResult` | Transcribe QByteArray by converting it to base 64 encoding. |
| `transcribe( Scribe &scribe, QDateTime &qdatetime_object, bool transcribed_construct_data)` | function | `TranscribeResult` | Transcribe QDateTime. |
| `transcribe( Scribe &scribe, QString &qstring_object, bool transcribed_construct_data)` | function | `TranscribeResult` | Transcribe QString by converting it to UTF8 format. |
| `transcribe( Scribe &scribe, QVariant &qvariant_object, bool transcribed_construct_data)` | function | `TranscribeResult` | Transcribe QVariant. |
| `transcribe( Scribe &scribe, QStringList &string_list_object, bool transcribed_construct_data)` | function | `TranscribeResult` | Transcribe QStringList. |
| `transcribe( Scribe &scribe, QList<T> &list_object, bool transcribed_construct_data)` | function | `TranscribeResult` | — |
| `transcribe( Scribe &scribe, QMap<Key, T> &map_object, bool transcribed_construct_data)` | function | `TranscribeResult` | — |
| `transcribe( Scribe &scribe, QMultiMap<Key, T> &multimap_object, bool transcribed_construct_data)` | function | `TranscribeResult` | — |
| `transcribe( Scribe &scribe, QQueue<T> &queue_object, bool transcribed_construct_data)` | function | `TranscribeResult` | — |
| `transcribe( Scribe &scribe, QSet<T> &set_object, bool transcribed_construct_data)` | function | `TranscribeResult` | — |
| `transcribe( Scribe &scribe, QStack<T> &stack_object, bool transcribed_construct_data)` | function | `TranscribeResult` | — |
| `transcribe( Scribe &scribe, QVector<T> &vector_object, bool transcribed_construct_data)` | function | `TranscribeResult` | — |

## Notes

[[[PROSE notes unit=scribe/TranscribeQt tier=2]]]
Replace this whole block, markers included, with invariants, ownership, threading or gotchas that are not visible in the tables. Write *None.* if there is nothing worth saying.
[[[/PROSE]]]

## Used by

| Unit | Component | References |
|---|---|---|
| [scribe/Scribe](Scribe.md) | scribe | 3 |
| [scribe/TranscribeExternal](TranscribeExternal.md) | scribe | 1 |
| [scribe/TranscribeUtils](TranscribeUtils.md) | scribe | 1 |

## Related

*None.*

## Explore

Run these from the `gplates-code` skill directory:

```bash
python scripts/gpq.py file src/scribe/TranscribeQt.h
python scripts/gpq.py def GPlatesScribe::TranscribeMap< QMap<Key, T> > --body
python scripts/gpq.py uses TranscribeMap< QMap<Key, T> > --kind struct
python scripts/gpq.py hier TranscribeMap< QMap<Key, T> >
```
