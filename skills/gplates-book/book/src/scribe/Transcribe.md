# Transcribe

[Book TOC](../../TOC.md) · [scribe](../../components/scribe.md) · cluster Community 16 · tier 1

| Source file | Kind | Lines |
|---|---|---|
| `src/scribe/Transcribe.h` | C++ | 486 |

## Overview

[[[PROSE overview unit=scribe/Transcribe tier=1]]]
Replace this whole block, markers included, with 1-3 paragraphs: what this unit is, why it exists, and how it fits the surrounding design. Do not restate the tables below.
[[[/PROSE]]]

## Declared types

*None.*

## Members

*None.*

## Free functions and macros

| Name | Kind | Type / body | Description |
|---|---|---|---|
| `GPLATES_SCRIBE_TRANSCRIBE_H` | macro | `None` | — |
| `transcribe( Scribe &scribe, ObjectType &object, bool transcribed_construct_data)` | function | `TranscribeResult` | else // loading { // Load 'x'. |
| `transcribe_construct_data( Scribe &scribe, ConstructObject<ObjectType> &object)` | function | `TranscribeResult` | // Load 'y'. |
| `relocated( Scribe &scribe, const ObjectType &relocated_object, const ObjectType &transcribed_object)` | function | `void` | scribe.transcribe(TRANSCRIBE\_SOURCE, refb, "ref\_b", GPlatesScribe::TRACK); assert(ref\_b.p == transcribed\_b.b); B relocated\_b(transcribed\_b); assert(ref\_b.p == relocated\_b.b); // Scribe has no references to relocate because nothing ... |

## Notes

[[[PROSE notes unit=scribe/Transcribe tier=1]]]
Replace this whole block, markers included, with invariants, ownership, threading or gotchas that are not visible in the tables. Write *None.* if there is nothing worth saying.
[[[/PROSE]]]

## Used by

| Unit | Component | References |
|---|---|---|
| [view-operations/ScalarField3DRenderParameters](../view-operations/ScalarField3DRenderParameters.md) | view-operations | 38 |
| [unit-test/TranscribeTest](../unit-test/TranscribeTest.md) | unit-test | 34 |
| [gui/BuiltinColourPalettes](../gui/BuiltinColourPalettes.md) | gui | 22 |
| [app-logic/TopologyNetworkParams](../app-logic/TopologyNetworkParams.md) | app-logic | 19 |
| [gui/BuiltinColourPaletteType](../gui/BuiltinColourPaletteType.md) | gui | 14 |
| [data-mining/RegionOfInterestFilter](../data-mining/RegionOfInterestFilter.md) | data-mining | 11 |
| [model/QualifiedXmlName](../model/QualifiedXmlName.md) | model | 11 |
| [model/StringContentTypeGenerator](../model/StringContentTypeGenerator.md) | model | 11 |
| [property-values/GeoTimeInstant](../property-values/GeoTimeInstant.md) | property-values | 11 |
| [app-logic/VelocityParams](../app-logic/VelocityParams.md) | app-logic | 9 |
| [gui/Symbol](../gui/Symbol.md) | gui | 9 |
| [presentation/TopologyNetworkVisualLayerParams](../presentation/TopologyNetworkVisualLayerParams.md) | presentation | 7 |
| [app-logic/ReconstructParams](../app-logic/ReconstructParams.md) | app-logic | 6 |
| [app-logic/ReconstructScalarCoverageParams](../app-logic/ReconstructScalarCoverageParams.md) | app-logic | 6 |
| [app-logic/ReconstructionParams](../app-logic/ReconstructionParams.md) | app-logic | 6 |
| [data-mining/CoRegFilter](../data-mining/CoRegFilter.md) | data-mining | 6 |
| [data-mining/SeedSelfFilter](../data-mining/SeedSelfFilter.md) | data-mining | 6 |
| [gui/Colour](../gui/Colour.md) | gui | 6 |
| [gui/GraticuleSettings](../gui/GraticuleSettings.md) | gui | 6 |
| [maths/Real](../maths/Real.md) | maths | 6 |

*... and 19 more units.*

## Related

*None.*

## Explore

Run these from the `gplates-code` skill directory:

```bash
python scripts/gpq.py file src/scribe/Transcribe.h
```
