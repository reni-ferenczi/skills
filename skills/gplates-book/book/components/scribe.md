# scribe

[Book TOC](../TOC.md)

43 unit page(s), 61 source file(s) documented here, 2 further file(s) listed below.

## Overview

[[[PROSE component unit=component:scribe tier=1]]]
Replace this whole block, markers included, with 2-4 paragraphs: what this component is responsible for, the load-bearing units and how it connects to neighbouring components. Do not restate the unit table.
[[[/PROSE]]]

## Units

| Unit | Tier | Lines | Fan-in | Description |
|---|---|---|---|---|
| [Scribe](../src/scribe/Scribe.md) | 1 | 7428 | 2179 | (pending) |
| [ScribeAccess](../src/scribe/ScribeAccess.md) | 1 | 460 | 175 | (pending) |
| [ScribeArchiveCommon](../src/scribe/ScribeArchiveCommon.md) | 2 | 351 | 260 | (pending) |
| [ScribeArchiveReader](../src/scribe/ScribeArchiveReader.md) | 2 | 87 | 103 | (pending) |
| [ScribeArchiveWriter](../src/scribe/ScribeArchiveWriter.md) | 2 | 82 | 28 | (pending) |
| [ScribeBinaryArchiveReader](../src/scribe/ScribeBinaryArchiveReader.md) | 2 | 490 | 48 | (pending) |
| [ScribeBinaryArchiveWriter](../src/scribe/ScribeBinaryArchiveWriter.md) | 2 | 518 | 8 | (pending) |
| [ScribeConstructObject](../src/scribe/ScribeConstructObject.md) | 2 | 260 | 13 | (pending) |
| [ScribeExceptions](../src/scribe/ScribeExceptions.md) | 1 | 1591 | 631 | (pending) |
| [ScribeExportExternal](../src/scribe/ScribeExportExternal.md) | 3 | 93 | 0 | Macro to register fundamental and external library types for Scribe serialization |
| [ScribeExportRegistration](../src/scribe/ScribeExportRegistration.md) | 3 | 235 | 4 | Macro framework for registering polymorphic classes and variant types with Scribe |
| [ScribeExportRegistry](../src/scribe/ScribeExportRegistry.md) | 2 | 335 | 83 | (pending) |
| [ScribeInternalAccess](../src/scribe/ScribeInternalAccess.md) | 2 | 253 | 139 | (pending) |
| [ScribeInternalUtils](../src/scribe/ScribeInternalUtils.md) | 2 | 520 | 123 | (pending) |
| [ScribeInternalUtilsImpl](../src/scribe/ScribeInternalUtilsImpl.md) | 3 | 88 | 0 | Template implementation for serializing objects owned by pointers |
| [ScribeLoadRef](../src/scribe/ScribeLoadRef.md) | 2 | 192 | 212 | (pending) |
| [ScribeLoadRefImpl](../src/scribe/ScribeLoadRefImpl.md) | 2 | 237 | 5 | (pending) |
| [ScribeObjectTag](../src/scribe/ScribeObjectTag.md) | 2 | 602 | 212 | (pending) |
| [ScribeOptions](../src/scribe/ScribeOptions.md) | 2 | 54 | 196 | (pending) |
| [ScribeSaveLoadConstructObject](../src/scribe/ScribeSaveLoadConstructObject.md) | 2 | 201 | 7 | (pending) |
| [ScribeTextArchiveReader](../src/scribe/ScribeTextArchiveReader.md) | 2 | 498 | 7 | (pending) |
| [ScribeTextArchiveWriter](../src/scribe/ScribeTextArchiveWriter.md) | 2 | 526 | 6 | (pending) |
| [ScribeVoidCastRegistry](../src/scribe/ScribeVoidCastRegistry.md) | 2 | 829 | 5 | (pending) |
| [ScribeXmlArchiveReader](../src/scribe/ScribeXmlArchiveReader.md) | 2 | 853 | 10 | (pending) |
| [ScribeXmlArchiveWriter](../src/scribe/ScribeXmlArchiveWriter.md) | 2 | 602 | 5 | (pending) |
| [Transcribe](../src/scribe/Transcribe.md) | 1 | 486 | 250 | (pending) |
| [TranscribeArray](../src/scribe/TranscribeArray.md) | 3 | 265 | 0 | Serialization support for static C++ arrays including multidimensional arrays |
| [TranscribeBoost](../src/scribe/TranscribeBoost.md) | 3 | 753 | 0 | Serialization support for Boost library types: smart pointers and variants |
| [TranscribeContext](../src/scribe/TranscribeContext.md) | 2 | 48 | 19 | (pending) |
| [TranscribeDelegateProtocol](../src/scribe/TranscribeDelegateProtocol.md) | 2 | 146 | 11 | (pending) |
| [TranscribeEnumProtocol](../src/scribe/TranscribeEnumProtocol.md) | 2 | 374 | 212 | (pending) |
| [TranscribeExternal](../src/scribe/TranscribeExternal.md) | 3 | 58 | 0 | Umbrella header aggregating transcription support for external libraries |
| [TranscribeImpl](../src/scribe/TranscribeImpl.md) | 3 | 308 | 0 | Core framework for transcribing user-defined classes with customization points |
| [TranscribeMappingProtocol](../src/scribe/TranscribeMappingProtocol.md) | 2 | 327 | 11 | (pending) |
| [TranscribeNonNullIntrusivePtr](../src/scribe/TranscribeNonNullIntrusivePtr.md) | 3 | 130 | 0 | Serialization support for GPlatesUtils::non\_null\_intrusive\_ptr |
| [TranscribeQt](../src/scribe/TranscribeQt.md) | 2 | 841 | 4 | (pending) |
| [TranscribeResult](../src/scribe/TranscribeResult.md) | 2 | 87 | 385 | (pending) |
| [TranscribeSequenceProtocol](../src/scribe/TranscribeSequenceProtocol.md) | 2 | 326 | 25 | (pending) |
| [TranscribeSmartPointerProtocol](../src/scribe/TranscribeSmartPointerProtocol.md) | 3 | 67 | 0 | Unified protocol for transcribing heterogeneous smart pointer types without breaking backward compatibility |
| [TranscribeStd](../src/scribe/TranscribeStd.md) | 3 | 900 | 0 | Transcription support for standard library containers |
| [TranscribeUtils](../src/scribe/TranscribeUtils.md) | 2 | 1192 | 46 | (pending) |
| [Transcription](../src/scribe/Transcription.md) | 1 | 1672 | 1150 | (pending) |
| [TranscriptionScribeContext](../src/scribe/TranscriptionScribeContext.md) | 2 | 1967 | 6 | (pending) |

## Other files

| File | Kind | Lines |
|---|---|---|
| `src/scribe/CMakeLists.txt` | build | 76 |
| `src/scribe/DesignRationale.txt` | doc | 156 |

## Depends on

| Component | References |
|---|---|
| [utils](utils.md) | 770 |
| [global](global.md) | 689 |
| [maths](maths.md) | 84 |
| [property-values](property-values.md) | 21 |
| [unit-test](unit-test.md) | 5 |
| [system-fixes](system-fixes.md) | 2 |

## Used by

| Component | References |
|---|---|
| [unit-test](unit-test.md) | 1263 |
| [presentation](presentation.md) | 686 |
| [gui](gui.md) | 395 |
| [app-logic](app-logic.md) | 270 |
| [data-mining](data-mining.md) | 176 |
| [view-operations](view-operations.md) | 157 |
| [model](model.md) | 103 |
| [property-values](property-values.md) | 55 |
| [utils](utils.md) | 37 |
| [maths](maths.md) | 17 |
| [entry-points](entry-points.md) | 12 |
| [feature-visitors](feature-visitors.md) | 2 |
| [file-io](file-io.md) | 2 |

## Explore

Run these from the `gplates-code` skill directory:

```bash
python scripts/gpq.py tree src/scribe
python scripts/gpq.py sym . --mode sub --path src/scribe --defs-only
```
