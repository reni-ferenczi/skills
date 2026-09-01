# TranscribeImpl

[Book TOC](../../TOC.md) · [scribe](../../components/scribe.md) · cluster Community 429 · tier 3

| Source file | Kind | Lines |
|---|---|---|
| `src/scribe/TranscribeImpl.h` | C++ | 308 |

## Overview

This is the core transcription framework for user-defined classes. The main `transcribe()` function gates all object serialization and delegates to `Access::transcribe()` after enforcing compile-time constraints: no pointers (which require special handling) and no unhandled enums (which must be explicitly transcribed). The framework provides two customization points via optional static methods: `transcribe_construct_data()` to control object construction during load (or use default-constructor semantics if absent), and `relocated()` to handle any relocation side effects (or do nothing if absent; most types need neither). Detection of these methods uses SFINAE via the `Access` helper class, allowing the framework to adapt to both custom and default behaviors.

## Declared types

*None.*

## Members

*None.*

## Free functions and macros

| Name | Kind | Type / body | Description |
|---|---|---|---|
| `GPLATES_SCRIBE_TRANSCRIBEIMPL_H` | macro | `None` | — |
| `transcribe( Scribe &scribe, ObjectType &object, bool transcribed_construct_data)` | function | `TranscribeResult` | — |
| `transcribe_construct_data_impl( Scribe &scribe, ConstructObject<ObjectType> &object, boost::mpl::true_)` | function | `TranscribeResult` | Delegate to the static class method 'transcribe\_construct\_data()' declared in class 'ObjectType'. |
| `transcribe_construct_data_impl( Scribe &scribe, ConstructObject<ObjectType> &object, boost::mpl::false_)` | function | `TranscribeResult` | The default implementation when 'ObjectType' does \*not\* have a static class method 'transcribe\_construct\_data()'. |
| `transcribe_construct_data( Scribe &scribe, ConstructObject<ObjectType> &object)` | function | `TranscribeResult` | — |
| `relocated_impl( Scribe &scribe, const ObjectType &relocated_object, const ObjectType &transcribed_object, boost::mpl::true_)` | function | `void` | Delegate to the static class method 'relocated()' declared in class 'ObjectType'. |
| `relocated_impl( Scribe &scribe, const ObjectType &relocated_object, const ObjectType &transcribed_object, boost::mpl::false_)` | function | `void` | The default implementation when 'ObjectType' does \*not\* have a static class method 'relocated()'. |
| `relocated( Scribe &scribe, const ObjectType &relocated_object, const ObjectType &transcribed_object)` | function | `void` | — |

## Notes

Pointer types and enumerations are rejected by compile-time assertions and cannot pass through this generic transcriber; they require their own specializations. Any enumeration type must explicitly provide a transcribe overload using `TranscribeEnumProtocol.h`, and private nested enums must do so as friend functions. The framework automatically relocates all data members and base classes; most types need no custom `relocated()` implementation unless they hold pointers to external objects that require manual update.

## Used by

| Unit | Component | References |
|---|---|---|
| [scribe/Scribe](Scribe.md) | scribe | 1 |

## Related

*None.*

## Explore

Run these from the `gplates-code` skill directory:

```bash
python scripts/gpq.py file src/scribe/TranscribeImpl.h
```
