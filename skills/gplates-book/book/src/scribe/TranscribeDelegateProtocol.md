# TranscribeDelegateProtocol

[Book TOC](../../TOC.md) · [scribe](../../components/scribe.md) · cluster Community 527 · tier 2

| Source file | Kind | Lines |
|---|---|---|
| `src/scribe/TranscribeDelegateProtocol.h` | C++ | 146 |

## Overview

[[[PROSE overview unit=scribe/TranscribeDelegateProtocol tier=2]]]
Replace this whole block, markers included, with 1-3 paragraphs: what this unit is, why it exists, and how it fits the surrounding design. Do not restate the tables below.
[[[/PROSE]]]

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

[[[PROSE notes unit=scribe/TranscribeDelegateProtocol tier=2]]]
Replace this whole block, markers included, with invariants, ownership, threading or gotchas that are not visible in the tables. Write *None.* if there is nothing worth saying.
[[[/PROSE]]]

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
