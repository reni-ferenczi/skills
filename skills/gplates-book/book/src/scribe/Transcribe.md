# Transcribe

[Book TOC](../../TOC.md) · [scribe](../../components/scribe.md) · cluster Community 16 · tier 1

| Source file | Kind | Lines |
|---|---|---|
| `src/scribe/Transcribe.h` | C++ | 486 |

## Overview

This header declares — and only declares — the three customisation points a type must
satisfy to be transcribable. It is the contract half of the scribe library: `Scribe`
performs the machinery, this file defines what `Scribe` will call on your class. The
definitions live elsewhere (`TranscribeImpl.h` for the generic fallbacks,
`TranscribeStd.h` / `TranscribeQt.h` / `TranscribeBoost.h` for third-party types), and the
declarations are kept in a header this thin so that a client class's own header can pull in
the contract without dragging in `Scribe.h`.

`transcribe()` is the one every type needs; it is called for both directions, with
`transcribed_construct_data` telling it whether constructor parameters were already
handled. `transcribe_construct_data()` is needed only when the type has no default
constructor: it loads whatever the constructor needs, calls `ConstructObject::construct_object()`
and then tells the scribe where the loaded values ended up. `relocated()` is a notification,
called only when loading, and only matters for members the scribe cannot see through — in
practice a raw pointer that *owns* its pointee, since copying the enclosing object produces a
new pointee that other transcribed pointers must be redirected to. The Doxygen on all three
is the library's real tutorial; the worked `A`/`B`/`C` examples explain the intent better
than any summary.

Each has two implementations, and the choice is made by ordinary overload resolution rather
than by any registry. Non-intrusive: specialise or overload the free function in whatever
namespace the type lives in — it is found by ADL, so it need not be in `GPlatesScribe`, and
it displaces the generic template in `TranscribeImpl.h` entirely. Intrusive: declare
`friend class GPlatesScribe::Access;` and provide a private member `transcribe()` or a
private static `transcribe_construct_data()` / `relocated()`; the generic `transcribe()`
forwards to the member through `Access`, while the generic `transcribe_construct_data()` and
`relocated()` branch on `Access`'s `HasStaticMember*` metafunctions and otherwise fall back
to default-constructing and to doing nothing. The intrusive form is the one to reach for
whenever private state is involved. The header is explicit that GPlates classes declare
their own overload in their own header — this file is not a registry and should not
accumulate entries.

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

Only the declarations are here; the generic definitions are in `TranscribeImpl.h`, which
`Scribe.h` includes after the class body specifically to break a cyclic header dependency.
Including this header alone gives you the contract, not an implementation.

Two categories never reach the generic `transcribe()` and are rejected by static assertion
there. Pointers must be handed to `Scribe` directly, which treats them as objects in their
own right. Enumerations must have their own overload — normally built with
`transcribe_enum_protocol()` from `TranscribeEnumProtocol.h`, and for a private enum written
as a friend function defined inside the class body. The string ids given to enum values are
part of the archive format: renaming the enumerator is fine, changing its string id breaks
compatibility.

`transcribe()` runs in both directions, so a change to what it saves is automatically a
change to what it loads — which is the whole reason for the single-path design, and also
why a change that is not backward compatible has to be signalled deliberately, by bumping
the `ObjectTag` version at the affected call site.

`transcribe_construct_data()` is called only when the scribe has to *create* the object
(loading through an owning pointer, for instance); transcribing an already-constructed
object such as a data member calls `transcribe()` alone. Inside it, the `ConstructObject`
must not be dereferenced before `construct_object()` has been called, and every loaded
constructor value that ends up stored inside the new object must be reported with
`Scribe::relocated()` — except loaded *references*, which are never relocated.

`relocated()` fires only on the load path, and the default implementation does nothing,
which is correct for almost every type: the scribe already relocates whatever lies inside
the object's memory extent, including base subobjects and arrays. It is needed only when a
member pointer *owns* the memory it points at, so that copying the enclosing object created
a fresh pointee that other transcribed pointers must be redirected to.

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
