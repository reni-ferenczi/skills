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
| [Scribe](../src/scribe/Scribe.md) | 1 | 7428 | 2179 | the transcribing engine: moves a live object graph into a Transcription and back, tracking object identity |
| [ScribeAccess](../src/scribe/ScribeAccess.md) | 1 | 460 | 175 | the single class a client type befriends so the scribe can reach its private transcribe hooks |
| [ScribeArchiveCommon](../src/scribe/ScribeArchiveCommon.md) | 2 | 351 | 260 | Shared signature strings, format-version numbers and element names for the three archive formats |
| [ScribeArchiveReader](../src/scribe/ScribeArchiveReader.md) | 2 | 87 | 103 | Abstract base for reading a Transcription out of a text, binary or XML archive |
| [ScribeArchiveWriter](../src/scribe/ScribeArchiveWriter.md) | 2 | 82 | 28 | Abstract base for writing a Transcription to a text, binary or XML archive |
| [ScribeBinaryArchiveReader](../src/scribe/ScribeBinaryArchiveReader.md) | 2 | 490 | 48 | Decodes a Transcription from a QDataStream using the binary archive's varint layout |
| [ScribeBinaryArchiveWriter](../src/scribe/ScribeBinaryArchiveWriter.md) | 2 | 518 | 8 | Encodes a Transcription onto a QDataStream using the binary archive's varint layout |
| [ScribeConstructObject](../src/scribe/ScribeConstructObject.md) | 2 | 260 | 13 | Placement-constructs a transcribed object in place when it has no default constructor |
| [ScribeExceptions](../src/scribe/ScribeExceptions.md) | 1 | 1591 | 631 | every scribe failure type under one catchable base; compatibility problems are return codes, not these |
| [ScribeExportExternal](../src/scribe/ScribeExportExternal.md) | 3 | 93 | 0 | Macro to register fundamental and external library types for Scribe serialization |
| [ScribeExportRegistration](../src/scribe/ScribeExportRegistration.md) | 3 | 235 | 4 | Macro framework for registering polymorphic classes and variant types with Scribe |
| [ScribeExportRegistry](../src/scribe/ScribeExportRegistry.md) | 2 | 335 | 83 | Singleton registry mapping class id names and type\_info to constructible concrete types |
| [ScribeInternalAccess](../src/scribe/ScribeInternalAccess.md) | 2 | 253 | 139 | Sole friend of Scribe, re-exposing to a few protocols only the private members each one needs |
| [ScribeInternalUtils](../src/scribe/ScribeInternalUtils.md) | 2 | 520 | 123 | Internal plumbing for object-address identity, type-erased pointer transcription and relocation callbacks |
| [ScribeInternalUtilsImpl](../src/scribe/ScribeInternalUtilsImpl.md) | 3 | 88 | 0 | Template implementation for serializing objects owned by pointers |
| [ScribeLoadRef](../src/scribe/ScribeLoadRef.md) | 2 | 192 | 212 | Reference handle returned by Scribe::load()/load\_reference(), valid only after checking is\_valid() |
| [ScribeLoadRefImpl](../src/scribe/ScribeLoadRefImpl.md) | 2 | 237 | 5 | Out-of-line LoadRef implementation, split out to avoid a header cycle with Scribe |
| [ScribeObjectTag](../src/scribe/ScribeObjectTag.md) | 2 | 602 | 212 | Immutable, chainable path key used to address a transcribed object within a Transcription |
| [ScribeOptions](../src/scribe/ScribeOptions.md) | 2 | 54 | 196 | Bit-flag constants (TRACK, EXCLUSIVE\_OWNER, SHARED\_OWNER) passed to Scribe::transcribe() |
| [ScribeSaveLoadConstructObject](../src/scribe/ScribeSaveLoadConstructObject.md) | 2 | 201 | 7 | Concrete ConstructObject implementations backing constructor transcription for save, stack-load and heap-load |
| [ScribeTextArchiveReader](../src/scribe/ScribeTextArchiveReader.md) | 2 | 498 | 7 | ArchiveReader that parses the human-readable text archive format into a Transcription |
| [ScribeTextArchiveWriter](../src/scribe/ScribeTextArchiveWriter.md) | 2 | 526 | 6 | ArchiveWriter that serialises a Transcription into the human-readable text archive format |
| [ScribeVoidCastRegistry](../src/scribe/ScribeVoidCastRegistry.md) | 2 | 829 | 5 | Runtime graph of registered base/derived links used to cast void pointers between them |
| [ScribeXmlArchiveReader](../src/scribe/ScribeXmlArchiveReader.md) | 2 | 853 | 10 | ArchiveReader that reconstructs a Transcription by parsing it back out of XML |
| [ScribeXmlArchiveWriter](../src/scribe/ScribeXmlArchiveWriter.md) | 2 | 602 | 5 | ArchiveWriter that serialises a Transcription to XML, the write side of XmlArchiveReader |
| [Transcribe](../src/scribe/Transcribe.md) | 1 | 486 | 250 | declares the three customisation points a type must satisfy to be transcribable |
| [TranscribeArray](../src/scribe/TranscribeArray.md) | 3 | 265 | 0 | Serialization support for static C++ arrays including multidimensional arrays |
| [TranscribeBoost](../src/scribe/TranscribeBoost.md) | 3 | 753 | 0 | Serialization support for Boost library types: smart pointers and variants |
| [TranscribeContext](../src/scribe/TranscribeContext.md) | 2 | 48 | 19 | Per-type extra state a transcribe() implementation needs but the archive doesn't carry |
| [TranscribeDelegateProtocol](../src/scribe/TranscribeDelegateProtocol.md) | 2 | 146 | 11 | Lets a type transcribe identically to another type it wraps, with no extra tag |
| [TranscribeEnumProtocol](../src/scribe/TranscribeEnumProtocol.md) | 2 | 374 | 212 | Transcribes an enum by name instead of integer value for backward/forward compatibility |
| [TranscribeExternal](../src/scribe/TranscribeExternal.md) | 3 | 58 | 0 | Umbrella header aggregating transcription support for external libraries |
| [TranscribeImpl](../src/scribe/TranscribeImpl.md) | 3 | 308 | 0 | Core framework for transcribing user-defined classes with customization points |
| [TranscribeMappingProtocol](../src/scribe/TranscribeMappingProtocol.md) | 2 | 327 | 11 | Uniform archive layout (size + key/value pairs) shared by every associative container type |
| [TranscribeNonNullIntrusivePtr](../src/scribe/TranscribeNonNullIntrusivePtr.md) | 3 | 130 | 0 | Serialization support for GPlatesUtils::non\_null\_intrusive\_ptr |
| [TranscribeQt](../src/scribe/TranscribeQt.md) | 2 | 841 | 4 | transcribe() overloads for Qt value types and containers, built on the shared protocols |
| [TranscribeResult](../src/scribe/TranscribeResult.md) | 2 | 87 | 385 | Status enum returned by every scribe transcribe call: success, incompatible, or unknown type |
| [TranscribeSequenceProtocol](../src/scribe/TranscribeSequenceProtocol.md) | 2 | 326 | 25 | Shared wire format so any std::vector/list/set/QList/QSet can be transcribed interchangeably |
| [TranscribeSmartPointerProtocol](../src/scribe/TranscribeSmartPointerProtocol.md) | 3 | 67 | 0 | Unified protocol for transcribing heterogeneous smart pointer types without breaking backward compatibility |
| [TranscribeStd](../src/scribe/TranscribeStd.md) | 3 | 900 | 0 | Transcription support for standard library containers |
| [TranscribeUtils](../src/scribe/TranscribeUtils.md) | 2 | 1192 | 46 | File-path transcription helpers plus raw/smart-pointer archive-compatibility bridges |
| [Transcription](../src/scribe/Transcription.md) | 1 | 1672 | 1150 | in-memory random-access form of transcribed state, shared by Scribe and the archive readers and writers |
| [TranscriptionScribeContext](../src/scribe/TranscriptionScribeContext.md) | 2 | 1967 | 6 | Bridges Scribe's object-graph calls to the tagged composite/primitive Transcription tree |

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
