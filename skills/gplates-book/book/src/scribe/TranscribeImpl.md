# TranscribeImpl

[Book TOC](../../TOC.md) · [scribe](../../components/scribe.md) · cluster Community 429 · tier 3

| Source file | Kind | Lines |
|---|---|---|
| `src/scribe/TranscribeImpl.h` | C++ | 308 |

## Overview

[[[PROSE overview unit=scribe/TranscribeImpl tier=3]]]
Replace this whole block, markers included, with 1-3 paragraphs: what this unit is, why it exists, and how it fits the surrounding design. Do not restate the tables below.
[[[/PROSE]]]

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

[[[PROSE notes unit=scribe/TranscribeImpl tier=3]]]
Replace this whole block, markers included, with invariants, ownership, threading or gotchas that are not visible in the tables. Write *None.* if there is nothing worth saying.
[[[/PROSE]]]

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
