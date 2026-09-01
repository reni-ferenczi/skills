# unicode

[Book TOC](../../TOC.md) · [global](../../components/global.md) · cluster Community 1 · tier 3

| Source file | Kind | Lines |
|---|---|---|
| `src/global/unicode.h` | C++ | 32 |

## Overview

A convenience header that provides access to `UnicodeString` utilities from the `utils` module. This header makes Unicode string functionality available throughout the codebase via inclusion in the global namespace. It is used by file I/O writers, the data model, property-value handlers, and utility modules to support internationalized string handling.

## Declared types

*None.*

## Members

*None.*

## Free functions and macros

| Name | Kind | Type / body | Description |
|---|---|---|---|
| `GPLATES_GLOBAL_UNICODE_H` | macro | `None` | — |

## Notes

*None.*

## Used by

| Unit | Component | References |
|---|---|---|
| [file-io/GMTFormatWriter](../file-io/GMTFormatWriter.md) | file-io | 1 |
| [file-io/PlatesFormatUtils](../file-io/PlatesFormatUtils.md) | file-io | 1 |
| [file-io/PlatesLineFormatHeaderVisitor](../file-io/PlatesLineFormatHeaderVisitor.md) | file-io | 1 |
| [file-io/PlatesLineFormatWriter](../file-io/PlatesLineFormatWriter.md) | file-io | 1 |
| [file-io/PlatesRotationFormatWriter](../file-io/PlatesRotationFormatWriter.md) | file-io | 1 |
| [file-io/XmlOutputInterface](../file-io/XmlOutputInterface.md) | file-io | 1 |
| [model/IdTypeGenerator](../model/IdTypeGenerator.md) | model | 1 |
| [model/RevisionId](../model/RevisionId.md) | model | 1 |
| [model/TopLevelPropertyInline](../model/TopLevelPropertyInline.md) | model | 1 |
| [property-values/GmlFile](../property-values/GmlFile.md) | property-values | 1 |
| [property-values/GpmlOldPlatesHeader](../property-values/GpmlOldPlatesHeader.md) | property-values | 1 |
| [utils/IdStringSet](../utils/IdStringSet.md) | utils | 1 |
| [utils/StringSet](../utils/StringSet.md) | utils | 1 |
| [utils/UnicodeStringUtils](../utils/UnicodeStringUtils.md) | utils | 1 |
| [utils/UniqueId](../utils/UniqueId.md) | utils | 1 |

## Related

*None.*

## Explore

Run these from the `gplates-code` skill directory:

```bash
python scripts/gpq.py file src/global/unicode.h
```
