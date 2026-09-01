# TranscribeSmartPointerProtocol

[Book TOC](../../TOC.md) · [scribe](../../components/scribe.md) · cluster Community 89 · tier 3

| Source file | Kind | Lines |
|---|---|---|
| `src/scribe/TranscribeSmartPointerProtocol.h` | C++ | 67 |

## Overview

This unit provides a wrapper that enforces a uniform transcription protocol for all smart pointer types. It allows `boost::shared_ptr`, `boost::scoped_ptr`, `boost::intrusive_ptr`, `GPlatesUtils::non_null_intrusive_ptr`, and `std::unique_ptr` to be transcribed interchangeably, so code can switch between different smart pointer implementations without breaking serialization compatibility.

The function accepts a raw pointer reference and a boolean flag indicating ownership sharing. It delegates to `ScribeInternalAccess::transcribe_smart_pointer`, which handles the actual serialization strategy, while `CallStackTracker` records the call site for error reporting.

## Declared types

*None.*

## Members

*None.*

## Free functions and macros

| Name | Kind | Type / body | Description |
|---|---|---|---|
| `GPLATES_SCRIBE_TRANSCRIBESMARTPOINTERPROTOCOL_H` | macro | `None` | — |
| `transcribe_smart_pointer_protocol( const GPlatesUtils::CallStack::Trace &transcribe_source, // Use 'TRANSCRIBE_SOURCE' here Scribe &scribe, ObjectType *&object_ptr, bool shared_owner)` | function | `TranscribeResult` | Used to ensure different smart pointer types are transcribed such that they can be switched without breaking backward/forward compatibility. |

## Notes

*None.*

## Used by

| Unit | Component | References |
|---|---|---|
| [scribe/TranscribeBoost](TranscribeBoost.md) | scribe | 1 |
| [scribe/TranscribeNonNullIntrusivePtr](TranscribeNonNullIntrusivePtr.md) | scribe | 1 |
| [scribe/TranscribeStd](TranscribeStd.md) | scribe | 1 |

## Related

*None.*

## Explore

Run these from the `gplates-code` skill directory:

```bash
python scripts/gpq.py file src/scribe/TranscribeSmartPointerProtocol.h
```
