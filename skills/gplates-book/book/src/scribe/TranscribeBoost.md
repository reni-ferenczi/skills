# TranscribeBoost

[Book TOC](../../TOC.md) · [scribe](../../components/scribe.md) · cluster Community 323 · tier 3

| Source file | Kind | Lines |
|---|---|---|
| `src/scribe/TranscribeBoost.h` | C++ | 753 |

## Overview

This unit provides transcription support for Boost library types used throughout GPlates. It covers smart pointers (`intrusive_ptr`, `optional`, `scoped_ptr`, `shared_ptr`, `weak_ptr`) via overloads of the transcribe function. The most complex support is for `boost::variant`, which requires all stored types to be export-registered and offers three transcription modes depending on whether the variant is default-constructable: direct transcription if the first type is default-constructable, or explicit save/load construction otherwise. Variants use `SaveVariantVisitor`, `LoadVariant`, and `RelocateVariantVisitor` to handle the type-switching logic; since variant storage is inline (stack-based), relocation is handled automatically by the Scribe framework.

## Declared types

| Name | Kind | Bases | Template | Subclasses | Description |
|---|---|---|---|---|---|
| [`GPlatesScribe::Implementation::SaveVariantVisitor`](#gplatesscribeimplementationsavevariantvisitor) | class | `boost::static_visitor<>` | — | 0 | — |
| [`GPlatesScribe::Implementation::LoadVariant`](#gplatesscribeimplementationloadvariant) | class | — | `<class VariantType>` | 0 | Class for loading into an \*existing\* (already constructed) variant. |
| [`GPlatesScribe::Implementation::RelocateVariantVisitor`](#gplatesscribeimplementationrelocatevariantvisitor) | class | `boost::static_visitor<>` | `<class VariantType>` | 0 | — |

## Members

### `GPlatesScribe::Implementation::SaveVariantVisitor`

| Member | Kind | Type | Access | Description |
|---|---|---|---|---|
| `SaveVariantVisitor( Scribe &scribe)` | constructor | `None` | public | — |
| `operator()( const BoundedType &value)` | operator | `void` | public | — |
| `d_scribe` | field | `Scribe` | private | — |

### `GPlatesScribe::Implementation::LoadVariant`

| Member | Kind | Type | Access | Description |
|---|---|---|---|---|
| `LoadVariant( VariantType &variant)` | constructor | `None` | public | — |
| `construct_object( const BoundedType &value)` | method | `void` | public | — |
| `d_variant` | field | `VariantType` | private | — |

### `GPlatesScribe::Implementation::RelocateVariantVisitor`

| Member | Kind | Type | Access | Description |
|---|---|---|---|---|
| `RelocateVariantVisitor( Scribe &scribe, const VariantType &relocated_variant)` | constructor | `None` | public | — |
| `operator()( const T &transcribed_variant_value)` | operator | `void` | public | — |
| `d_scribe` | field | `Scribe` | private | — |
| `d_relocated_variant` | field | `VariantType` | private | — |

## Free functions and macros

| Name | Kind | Type / body | Description |
|---|---|---|---|
| `GPLATES_SCRIBE_TRANSCRIBEBOOST_H` | macro | `None` | — |
| `transcribe( Scribe &scribe, boost::intrusive_ptr<T> &intrusive_ptr_object, bool transcribed_construct_data)` | function | `TranscribeResult` | — |
| `transcribe( Scribe &scribe, boost::optional<T> &optional_object, bool transcribed_construct_data)` | function | `TranscribeResult` | — |
| `relocated( Scribe &scribe, const boost::optional<T> &relocated_optional_object, const boost::optional<T> &transcribed_optional_object)` | function | `void` | — |
| `transcribe( Scribe &scribe, boost::optional<T &> &optional_object_reference, bool transcribed_construct_data)` | function | `TranscribeResult` | — |
| `relocated( Scribe &scribe, const boost::optional<T &> &relocated_optional_object, const boost::optional<T &> &transcribed_optional_object)` | function | `void` | — |
| `transcribe( Scribe &scribe, boost::scoped_ptr<T> &scoped_ptr_object, bool transcribed_construct_data)` | function | `TranscribeResult` | — |
| `transcribe( Scribe &scribe, boost::shared_ptr<T> &shared_ptr_object, bool transcribed_construct_data)` | function | `TranscribeResult` | — |
| `transcribe( Scribe &scribe, boost::weak_ptr<T> &weak_ptr_object, bool transcribed_construct_data)` | function | `TranscribeResult` | — |
| `save_variant( Scribe &scribe, const boost::variant<BOOST_VARIANT_ENUM_PARAMS(T)> &variant_object)` | function | `void` | — |
| `load_variant( Scribe &scribe, ConstructObjectType &variant_object, const std::type_info &stored_type_info, boost::mpl::false_)` | function | `TranscribeResult` | — |
| `load_variant( Scribe &scribe, ConstructObjectType &variant_object, const std::type_info &stored_type_info, boost::mpl::true_)` | function | `TranscribeResult` | — |
| `load_variant( Scribe &scribe, ConstructObjectType &variant_object)` | function | `TranscribeResult` | — |
| `load_variant( Scribe &scribe, LoadVariant< boost::variant<BOOST_VARIANT_ENUM_PARAMS(T)> > &variant_object)` | function | `TranscribeResult` | — |
| `transcribe( Scribe &scribe, boost::variant<BOOST_VARIANT_ENUM_PARAMS(T)> &variant_object, bool transcribed_construct_data)` | function | `TranscribeResult` | — |
| `transcribe_construct_data( Scribe &scribe, ConstructObject< boost::variant<BOOST_VARIANT_ENUM_PARAMS(T)> > &variant_object)` | function | `TranscribeResult` | — |
| `relocated( Scribe &scribe, const boost::variant<BOOST_VARIANT_ENUM_PARAMS(T)> &relocated_variant_object, const boost::variant<BOOST_VARIANT_ENUM_PARAMS(T)> &transcribed_variant_object)` | function | `void` | We don't need to relocate boost::variant because its internal object is stored directly (inline) in the variant class and the Scribe library handles this for us. |

## Notes

All types stored in a `boost::variant` must be export-registered for serialization to succeed. A variant is only default-constructable if its first type parameter is default-constructable; variants that are not default-constructable must use explicit save/load construction (`scribe.load<>()`) or be initialized with a dummy value before transcription. Variant relocation is automatic because the variant stores its value inline; the Scribe framework does not need explicit relocation callbacks.

## Used by

| Unit | Component | References |
|---|---|---|
| [scribe/TranscribeExternal](TranscribeExternal.md) | scribe | 1 |

## Related

*None.*

## Explore

Run these from the `gplates-code` skill directory:

```bash
python scripts/gpq.py file src/scribe/TranscribeBoost.h
python scripts/gpq.py def GPlatesScribe::Implementation::LoadVariant --body
python scripts/gpq.py uses LoadVariant --kind class
python scripts/gpq.py hier LoadVariant
```
