# ScribeInternalAccess

[Book TOC](../../TOC.md) · [scribe](../../components/scribe.md) · cluster Community 349 · tier 2

| Source file | Kind | Lines |
|---|---|---|
| `src/scribe/ScribeInternalAccess.h` | C++ | 253 |

## Overview

`ScribeInternalAccess` is a friendship gatekeeper for `Scribe`: rather than grant `friend` to every protocol function that needs a private `Scribe` member, `Scribe` grants friendship to this one class, which then re-exposes exactly the private members each protocol needs as private static wrapper functions, and grants friendship itself only to those specific protocol functions and templates (the `transcribe_smart_pointer_protocol`, `transcribe_delegate_protocol`/`save_delegate_protocol`/`load_delegate_protocol` free functions, `LoadRef`, `TranscribeOwningPointerTemplate`, the `TranscribeUtils` loaders, and `transcribe(Scribe&, boost::shared_ptr<T>&, bool)`). This keeps the set of code that can reach into `Scribe`'s internals — its object tracking, its construct/delegate/smart-pointer transcription machinery, and its internal `Bool`/`LoadRef` constructors — small and explicit, so `Scribe`'s object-type-checking invariants cannot be bypassed by an unrelated piece of code that happens to also be a friend.

Every member here is `private`, so nothing outside the `friend` list declared at the bottom of the class can call through it; the class exists purely as an indirection layer, not as an API any other code is meant to use directly.

## Declared types

| Name | Kind | Bases | Template | Subclasses | Description |
|---|---|---|---|---|---|
| [`GPlatesScribe::ScribeInternalAccess`](#gplatesscribescribeinternalaccess) | class | — | — | 0 | Limit access to the internals of class Scribe to a few functions. |

## Members

### `GPlatesScribe::ScribeInternalAccess`

| Member | Kind | Type | Access | Description |
|---|---|---|---|---|
| `untrack( Scribe &scribe, ObjectType &object, bool discard)` | method | `void` | private | — |
| `transcribe_construct( Scribe &scribe, ConstructObject<ObjectType> &object, TranscriptionScribeContext::object_id_type object_id, unsigned int options)` | method | `bool` | private | — |
| `transcribe_smart_pointer( Scribe &scribe, ObjectType *&object_ptr, bool shared_owner)` | method | `bool` | private | — |
| `transcribe_delegate( Scribe &scribe, ObjectType &object)` | method | `bool` | private | — |
| `save_delegate( Scribe &scribe, const ObjectType &object)` | method | `void` | private | — |
| `load_delegate( const GPlatesUtils::CallStack::Trace &transcribe_source, Scribe &scribe)` | method | `LoadRef<ObjectType>` | private | — |
| `create_load_ref( const GPlatesUtils::CallStack::Trace &transcribe_source, Scribe &scribe, ObjectType *object, bool release)` | method | `LoadRef<ObjectType>` | private | — |
| `create_bool( const GPlatesUtils::CallStack::Trace &transcribe_source, bool result, bool require_check)` | method | `Scribe::Bool` | private | — |
| `reset( Scribe &scribe, boost::shared_ptr<T> &shared_ptr_object, T *raw_ptr)` | method | `void` | private | — |
| `reset( Scribe &scribe, boost::shared_ptr<const T> &shared_ptr_object, const T *raw_ptr)` | method | `void` | private | — |

## Free functions and macros

| Name | Kind | Type / body | Description |
|---|---|---|---|
| `GPLATES_SCRIBE_SCRIBEINTERNALACCESS_H` | macro | `None` | — |
| `transcribe(Scribe &, boost::shared_ptr<T> &, bool)` | function | `TranscribeResult` | — |
| `transcribe_smart_pointer_protocol( const GPlatesUtils::CallStack::Trace &, Scribe &, ObjectType *&, bool)` | function | `TranscribeResult` | — |
| `load_smart_pointer_from_raw_pointer( const GPlatesUtils::CallStack::Trace &, Scribe &, SmartPtrType &, const ObjectTag &, bool)` | function | `Scribe::Bool` | — |
| `load_raw_pointer_and_object_from_smart_pointer( const GPlatesUtils::CallStack::Trace &, Scribe &, ObjectType &, ObjectRawPtrType &, const ObjectTag &, bool)` | function | `Scribe::Bool` | — |
| `load_raw_pointer_and_object_from_smart_pointer( const GPlatesUtils::CallStack::Trace &, Scribe &, ObjectRawPtrType &, const ObjectTag &, bool)` | function | `LoadRef<ObjectType>` | — |

## Notes

Adding a new caller of a `Scribe` private member means adding both a wrapper method here and a corresponding `friend` declaration naming that exact function or class template — there is no broader escape hatch. Because `ScribeInternalAccess` is `Scribe`'s only friend, any new internal `Scribe` functionality that a protocol needs must be routed through this class rather than by befriending `Scribe` directly elsewhere.

## Used by

| Unit | Component | References |
|---|---|---|
| [scribe/TranscribeUtils](TranscribeUtils.md) | scribe | 32 |
| [unit-test/TranscribeTest](../unit-test/TranscribeTest.md) | unit-test | 24 |
| [presentation/TranscribeSession](../presentation/TranscribeSession.md) | presentation | 18 |
| [presentation/ProjectSession](../presentation/ProjectSession.md) | presentation | 17 |
| [scribe/Scribe](Scribe.md) | scribe | 17 |
| [presentation/InternalSession](../presentation/InternalSession.md) | presentation | 12 |
| [scribe/TranscribeBoost](TranscribeBoost.md) | scribe | 7 |
| [scribe/TranscribeMappingProtocol](TranscribeMappingProtocol.md) | scribe | 3 |
| [scribe/TranscribeSequenceProtocol](TranscribeSequenceProtocol.md) | scribe | 3 |
| [scribe/TranscribeStd](TranscribeStd.md) | scribe | 3 |
| [model/TranscribeStringContentTypeGenerator](../model/TranscribeStringContentTypeGenerator.md) | model | 2 |
| [scribe/TranscribeDelegateProtocol](TranscribeDelegateProtocol.md) | scribe | 2 |
| [scribe/TranscribeNonNullIntrusivePtr](TranscribeNonNullIntrusivePtr.md) | scribe | 2 |
| [scribe/ScribeInternalUtilsImpl](ScribeInternalUtilsImpl.md) | scribe | 1 |
| [scribe/ScribeLoadRefImpl](ScribeLoadRefImpl.md) | scribe | 1 |
| [scribe/TranscribeArray](TranscribeArray.md) | scribe | 1 |
| [scribe/TranscribeSmartPointerProtocol](TranscribeSmartPointerProtocol.md) | scribe | 1 |

## Related

*None.*

## Explore

Run these from the `gplates-code` skill directory:

```bash
python scripts/gpq.py file src/scribe/ScribeInternalAccess.h
python scripts/gpq.py def GPlatesScribe::ScribeInternalAccess --body
python scripts/gpq.py uses ScribeInternalAccess --kind class
python scripts/gpq.py hier ScribeInternalAccess
```
