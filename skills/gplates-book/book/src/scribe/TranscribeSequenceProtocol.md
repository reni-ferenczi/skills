# TranscribeSequenceProtocol

[Book TOC](../../TOC.md) · [scribe](../../components/scribe.md) · cluster Community 1505 · tier 2

| Source file | Kind | Lines |
|---|---|---|
| `src/scribe/TranscribeSequenceProtocol.h` | C++ | 326 |

## Overview

This header gives every sequence-like container (`std::vector`, `std::list`, `std::set`, `QList`, `QSet`, and so on) a single, shared wire format, so that a data member's concrete container type can be changed later without breaking backward or forward compatibility with archives written by older versions of GPlates. `transcribe_sequence_protocol()` implements that wire format directly: it writes a `sequence_size` object tag followed by that many indexed items, and on load it clears the target sequence first, transcribes each item, then relocates them into their final container in a second pass (needed because `push_back`-style growth can reallocate and invalidate the tracked-item addresses `Scribe` handed out during loading). Per-container behaviour — how to get the length, iterate items, clear the container and add a loaded item — is factored out into the `TranscribeSequence` template, which the primary definition implements generically for any STL-vector-like sequence; container types with different semantics (e.g. set-like containers that reject duplicates) are expected to specialise it, as `add_item()`'s boolean return (added vs. rejected as a duplicate) already anticipates. `relocated_sequence_protocol()` is the matching half used when a transcribed sequence is later relocated (e.g. because it lives inside a relocated parent object), walking both the old and new sequences in lockstep and calling `scribe.relocated()` on each corresponding pair of items.

Because `TRANSCRIBE_UNKNOWN_TYPE` can occur per element (for example a polymorphic pointer to a derived class this build doesn't know about), the protocol is deliberately transparent: `ObjectTag::sequence_size()` and `ObjectTag::sequence_item(index)` are documented as public API so a caller who needs to skip unknown elements individually, instead of failing the whole sequence, can drive the same tags directly rather than going through `transcribe_sequence_protocol()`.

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

- On load, `transcribe_sequence_protocol()` clears the destination sequence up front; if any item fails to transcribe it clears the sequence again before returning, so a caller must not assume a partially-filled sequence survives a non-`TRANSCRIBE_SUCCESS` result.
- A mismatch between the recorded sequence length and the number of items actually saved or loaded is asserted as `Exceptions::ScribeLibraryError`, not a user error — it indicates a bug in a `TranscribeSequence` specialisation rather than a bad archive.
- Adding a new container type means specialising `TranscribeSequence` for it; the primary template only works for vector-like sequences that support `push_back` and never reject an added item.

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
