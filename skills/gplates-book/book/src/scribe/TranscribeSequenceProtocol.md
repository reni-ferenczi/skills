# TranscribeSequenceProtocol

[Book TOC](../../TOC.md) · [scribe](../../components/scribe.md) · cluster Community 1505 · tier 2

| Source file | Kind | Lines |
|---|---|---|
| `src/scribe/TranscribeSequenceProtocol.h` | C++ | 326 |

## Overview

[[[PROSE overview unit=scribe/TranscribeSequenceProtocol tier=2]]]
Replace this whole block, markers included, with 1-3 paragraphs: what this unit is, why it exists, and how it fits the surrounding design. Do not restate the tables below.
[[[/PROSE]]]

## Declared types

| Name | Kind | Bases | Template | Subclasses | Description |
|---|---|---|---|---|---|
| [`GPlatesScribe::TranscribeSequence`](#gplatesscribetranscribesequence) | struct | — | `<class SequenceType>` | 0 | Specialisations of this class implement sequence functions used in transcribe\_sequence\_protocol. |

## Members

### `GPlatesScribe::TranscribeSequence`

| Member | Kind | Type | Access | Description |
|---|---|---|---|---|
| `sequence_type` | typedef | `SequenceType` | public | — |
| `item_type` | typedef | `typename sequence_type::value_type` | public | — |
| `sequence_iterator` | typedef | `typename sequence_type::iterator` | public | — |
| `sequence_const_iterator` | typedef | `typename sequence_type::const_iterator` | public | — |
| `get_length( const sequence_type &sequence)` | method | `unsigned int` | public | Get length of existing sequence (for saving). |
| `get_items( const sequence_type &sequence)` | method | `std::pair<sequence_const_iterator, sequence_const_iterator>` | public | Get (begin, end) range of const-iterators over existing sequence (for saving and loading). |
| `get_items( sequence_type &sequence)` | method | `std::pair<sequence_iterator, sequence_iterator>` | public | Get (begin, end) range of iterators over existing sequence (for saving and loading). |
| `clear( sequence_type &sequence)` | method | `void` | public | Make sure sequence is empty (for loading). |
| `add_item( sequence_type &sequence, const item_type &item)` | method | `bool` | public | Add a loaded item to a sequence (for loading). |

## Free functions and macros

| Name | Kind | Type / body | Description |
|---|---|---|---|
| `GPLATES_SCRIBE_TRANSCRIBESEQUENCEPROTOCOL_H` | macro | `None` | — |
| `transcribe_sequence_protocol( const GPlatesUtils::CallStack::Trace &transcribe_source, // Use 'TRANSCRIBE_SOURCE' here Scribe &scribe, SequenceType &sequence)` | function | `TranscribeResult` | Used to ensure different sequence types are transcribed such that they can be switched without breaking backward/forward compatibility. |
| `transcribe_sequence_protocol( const GPlatesUtils::CallStack::Trace &transcribe_source, Scribe &scribe, SequenceType &sequence)` | function | `TranscribeResult` | — |
| `relocated_sequence_protocol( Scribe &scribe, const SequenceType &relocated_sequence, const SequenceType &transcribed_sequence)` | function | `void` | — |

## Notes

[[[PROSE notes unit=scribe/TranscribeSequenceProtocol tier=2]]]
Replace this whole block, markers included, with invariants, ownership, threading or gotchas that are not visible in the tables. Write *None.* if there is nothing worth saying.
[[[/PROSE]]]

## Used by

| Unit | Component | References |
|---|---|---|
| [scribe/TranscribeStd](TranscribeStd.md) | scribe | 19 |
| [scribe/TranscribeQt](TranscribeQt.md) | scribe | 8 |
| [scribe/TranscriptionScribeContext](TranscriptionScribeContext.md) | scribe | 1 |

## Related

*None.*

## Explore

Run these from the `gplates-code` skill directory:

```bash
python scripts/gpq.py file src/scribe/TranscribeSequenceProtocol.h
python scripts/gpq.py def GPlatesScribe::TranscribeSequence --body
python scripts/gpq.py uses TranscribeSequence --kind struct
python scripts/gpq.py hier TranscribeSequence
```
