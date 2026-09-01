# TranscribeDelegateProtocol

[Book TOC](../../TOC.md) · [scribe](../../components/scribe.md) · cluster Community 527 · tier 2

| Source file | Kind | Lines |
|---|---|---|
| `src/scribe/TranscribeDelegateProtocol.h` | C++ | 146 |

## Overview

This header provides the "delegate" transcribe protocol: a way to write a type's `transcribe()` function so that it archives exactly like some other type, with no extra tag or wrapper structure of its own. A wrapper struct that holds a single `QString`, for instance, can delegate its transcription to that `QString` member via `transcribe_delegate_protocol()`, so the archived data is indistinguishable from having saved the `QString` directly — a plain `QString` can later be loaded back into the wrapper, or vice versa. Delegating instead of adding a named property (`scribe.transcribe(TRANSCRIBE_SOURCE, wrapper.qstring, "qstring")`) is what preserves that backward/forward compatibility between the two types.

`save_delegate_protocol()` and `load_delegate_protocol()` split the same idea across the save and load paths for types that have no default constructor, where `load_delegate_protocol()` returns a `LoadRef<ObjectType>` instead of transcribing into an existing instance. All three forward to the internal `ScribeInternalAccess::transcribe_delegate()`/`save_delegate()`/`load_delegate()` entry points, and each wraps the call in a `GPlatesUtils::CallStackTracker` so a transcription exception raised inside the delegate reports the call site that invoked it.

## Declared types

*None.*

## Members

*None.*

## Free functions and macros

| Name | Kind | Type / body | Description |
|---|---|---|---|
| `GPLATES_SCRIBE_TRANSCRIBEDELEGATEPROTOCOL_H` | macro | `None` | — |
| `transcribe_delegate_protocol( const GPlatesUtils::CallStack::Trace &transcribe_source, // Use 'TRANSCRIBE_SOURCE' here Scribe &scribe, ObjectType &object)` | function | `TranscribeResult` | transcribe( GPlatesScribe::Scribe &scribe, QStringWrapper &wrapper, bool transcribed\_construct\_data) { return transcribe\_delegate\_protocol(TRANSCRIBE\_SOURCE, scribe, wrapper.qstring); } Note that there are no options in ... |
| `save_delegate_protocol( const GPlatesUtils::CallStack::Trace &transcribe_source, // Use 'TRANSCRIBE_SOURCE' here Scribe &scribe, const ObjectType &object)` | function | `void` | Similar to transcribe\_delegate\_protocol but used on the \*save\* path when need to use load\_delegate\_protocol on the \*load\* path. |
| `load_delegate_protocol( const GPlatesUtils::CallStack::Trace &transcribe_source, // Use 'TRANSCRIBE_SOURCE' here Scribe &scribe)` | function | `LoadRef<ObjectType>` | Similar to transcribe\_delegate\_protocol but used on the \*load\* path when ObjectType has no default constructor. |

## Notes

- `transcribe_delegate_protocol()` takes no options, and the delegated-to object is not tracked for object identity/sharing the way `scribe.transcribe()` normally tracks objects — do not use it where the delegated object's identity needs to be preserved across the archive.
- Delegating is only transcription-compatible with the target type as long as no extra named property is introduced; adding one (as the header's counter-example shows) breaks the cross-type load/save compatibility that this protocol exists to provide.

## Used by

| Unit | Component | References |
|---|---|---|
| [model/TranscribeStringContentTypeGenerator](../model/TranscribeStringContentTypeGenerator.md) | model | 5 |
| [property-values/GeoTimeInstant](../property-values/GeoTimeInstant.md) | property-values | 4 |
| [maths/Real](../maths/Real.md) | maths | 2 |
| [presentation/TranscribeSession](../presentation/TranscribeSession.md) | presentation | 2 |
| [unit-test/TranscribeTest](../unit-test/TranscribeTest.md) | unit-test | 2 |
| [utils/UnicodeString](../utils/UnicodeString.md) | utils | 2 |

## Related

*None.*

## Explore

Run these from the `gplates-code` skill directory:

```bash
python scripts/gpq.py file src/scribe/TranscribeDelegateProtocol.h
```
