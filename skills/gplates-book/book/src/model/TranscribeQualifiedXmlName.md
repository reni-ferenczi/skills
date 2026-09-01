# TranscribeQualifiedXmlName

[Book TOC](../../TOC.md) · [model](../../components/model.md) · cluster Community 1645 · tier 3

| Source file | Kind | Lines |
|---|---|---|
| `src/model/TranscribeQualifiedXmlName.h` | C++ | 110 |

## Overview

This header provides serialization support for the template class `QualifiedXmlName`, implementing the Scribe transcribe methods that save and load the three components of a qualified XML name — the namespace URI, namespace alias, and local name. The implementations handle both object construction during loading and state transcription during save/load cycles.

The file is kept separate from the main `QualifiedXmlName.h` header to avoid pulling in the heavyweight Scribe framework into code that does not serialize.

## Declared types

*None.*

## Members

*None.*

## Free functions and macros

| Name | Kind | Type / body | Description |
|---|---|---|---|
| `GPLATES_MODEL_TRANSCRIBEQUALIFIEDXMLNAME_H` | macro | `None` | — |

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
python scripts/gpq.py file src/model/TranscribeQualifiedXmlName.h
```
