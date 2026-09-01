# TranscribeStringContentTypeGenerator

[Book TOC](../../TOC.md) · [model](../../components/model.md) · cluster Community 756 · tier 3

| Source file | Kind | Lines |
|---|---|---|
| `src/model/TranscribeStringContentTypeGenerator.h` | C++ | 105 |

## Overview

This header provides serialization support for the template class `StringContentTypeGenerator`, implementing Scribe transcribe methods that save and load string content. It uses the delegate protocol to make `StringContentTypeGenerator` and `UnicodeString` interchangeable during serialization — allowing the two types to be transcribed as equivalents of each other.

Like `TranscribeQualifiedXmlName`, the file is kept separate from the main `StringContentTypeGenerator.h` header to avoid pulling in the heavyweight Scribe framework into non-serialization code paths.

## Declared types

*None.*

## Members

*None.*

## Free functions and macros

| Name | Kind | Type / body | Description |
|---|---|---|---|
| `GPLATES_MODEL_TRANSCRIBESTRINGCONTENTTYPEGENERATOR_H` | macro | `None` | — |

## Notes

*None.*

## Used by

| Unit | Component | References |
|---|---|---|
| [presentation/TranscribeSession](../presentation/TranscribeSession.md) | presentation | 1 |

## Related

*None.*

## Explore

Run these from the `gplates-code` skill directory:

```bash
python scripts/gpq.py file src/model/TranscribeStringContentTypeGenerator.h
```
