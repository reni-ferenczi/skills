# ScribeExportExternal

[Book TOC](../../TOC.md) · [scribe](../../components/scribe.md) · cluster Community 16 · tier 3

| Source file | Kind | Lines |
|---|---|---|
| `src/scribe/ScribeExportExternal.h` | C++ | 93 |

## Overview

The `SCRIBE_EXPORT_EXTERNAL` macro registers types from external libraries — C++ standard library, Qt framework, and scribe utilities — so the `Scribe` serialization framework can serialize and deserialize them. It maps each type to a stable string identifier that persists across session saves and loads. The macro covers fundamental arithmetic types (integers, floating-point), standard containers like `std::string`, Qt types (`QString`, `QByteArray`, `QStringList`), and the scribe utility `FilePath` class.

## Declared types

*None.*

## Members

*None.*

## Free functions and macros

| Name | Kind | Type / body | Description |
|---|---|---|---|
| `GPLATES_SCRIBE_SCRIBEEXPORTEXTERNAL_H` | macro | `None` | — |
| `SCRIBE_EXPORT_EXTERNAL` | macro | `((char, "char")) \ ((signed char, "signed char")) \ ((unsigned char, "unsigned char")) \ \ ((short, "short")) \ ((unsigned short, "unsigned short")) \ \ ((int, "int")) \ ((unsigned ...` | Scribe export registered classes/types for \*external\* libraries. |

## Notes

Changing the string identifiers in this macro breaks backward and forward compatibility with saved projects and sessions. The serialized type identifiers are permanent; any modification must be coordinated with migration logic to handle old-format files.

## Used by

| Unit | Component | References |
|---|---|---|
| [entry-points/ScribeExportGPlates](../entry-points/ScribeExportGPlates.md) | entry-points | 1 |
| [entry-points/ScribeExportGPlatesDemoNoGui](../entry-points/ScribeExportGPlatesDemoNoGui.md) | entry-points | 1 |
| [entry-points/ScribeExportGPlatesUnitTest](../entry-points/ScribeExportGPlatesUnitTest.md) | entry-points | 1 |
| [entry-points/ScribeExportPyGPlates](../entry-points/ScribeExportPyGPlates.md) | entry-points | 1 |

## Related

*None.*

## Explore

Run these from the `gplates-code` skill directory:

```bash
python scripts/gpq.py file src/scribe/ScribeExportExternal.h
```
