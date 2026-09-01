# QtStreamable

[Book TOC](../../TOC.md) · [utils](../../components/utils.md) · cluster Community 5 · tier 2

| Source file | Kind | Lines |
|---|---|---|
| `src/utils/QtStreamable.h` | C++ | 111 |

## Overview

`QtStreamable<Derived>` is a CRTP mixin (the Barton-Nackman trick) that derives Qt debug-stream support from an existing `std::ostream` `operator<<`. A class that already defines `operator<<(std::ostream &, const Derived &)` gets `operator<<` for `QDebug` and `QTextStream` for free simply by inheriting `QtStreamable<Derived>`, instead of writing a second, near-duplicate streaming operator for Qt's stream types. Both friend operators work by formatting into a temporary `std::ostringstream`, converting the result to a `QString`, and writing that into the Qt stream — so the Qt-facing text always matches whatever the class's `std::ostream` operator already produces. With 176 classes across the maths, model, gui and file-io modules inheriting from it, this is the standard way value types in GPlates get `qDebug() <<` support.

## Declared types

| Name | Kind | Bases | Template | Subclasses | Description |
|---|---|---|---|---|---|
| [`GPlatesUtils::QtStreamable`](#gplatesutilsqtstreamable) | class | — | `<class Derived>` | 176 | If you provide the following operator for a class 'Derived': std::ostream & operator \<\<( std::ostream &os, const Derived &derived\_object); ...then if you inherit from 'QtStreamble' you can also do the following: qDebug() \<\< derived\_object; ... |

## Members

### `GPlatesUtils::QtStreamable`

*None.*

## Free functions and macros

| Name | Kind | Type / body | Description |
|---|---|---|---|
| `GPLATES_UTILS_QTSTREAMABLE_H` | macro | `None` | — |

## Notes

Inheriting `QtStreamable<Derived>` without also defining `operator<<(std::ostream &, const Derived &)` for `Derived` will fail to compile at the point of use (the friend operators call that operator internally), not at the class declaration.

## Used by

| Unit | Component | References |
|---|---|---|
| [feature-visitors/ToQvariantConverter](../feature-visitors/ToQvariantConverter.md) | feature-visitors | 6 |
| [file-io/PlatesRotationFormatWriter](../file-io/PlatesRotationFormatWriter.md) | file-io | 6 |
| [model/StringContentTypeGenerator](../model/StringContentTypeGenerator.md) | model | 5 |
| [feature-visitors/ShapefileAttributeFinder](../feature-visitors/ShapefileAttributeFinder.md) | feature-visitors | 4 |
| [file-io/PlatesLineFormatGeometryExporter](../file-io/PlatesLineFormatGeometryExporter.md) | file-io | 4 |
| [model/RevisionId](../model/RevisionId.md) | model | 4 |
| [file-io/GMTFormatGeometryExporter](../file-io/GMTFormatGeometryExporter.md) | file-io | 3 |
| [gui/MapProjection](../gui/MapProjection.md) | gui | 3 |
| [maths/LatLonPoint](../maths/LatLonPoint.md) | maths | 3 |
| [maths/PointOnSphere](../maths/PointOnSphere.md) | maths | 3 |
| [maths/UnitQuaternion3D](../maths/UnitQuaternion3D.md) | maths | 3 |
| [maths/UnitVector3D](../maths/UnitVector3D.md) | maths | 3 |
| [maths/Vector3D](../maths/Vector3D.md) | maths | 3 |
| [model/GpgimVersion](../model/GpgimVersion.md) | model | 3 |
| [property-values/GeoTimeInstant](../property-values/GeoTimeInstant.md) | property-values | 3 |
| [global/GPlatesException](../global/GPlatesException.md) | global | 2 |
| [gui/Colour](../gui/Colour.md) | gui | 2 |
| [maths/FiniteRotation](../maths/FiniteRotation.md) | maths | 2 |
| [model/PropertyValue](../model/PropertyValue.md) | model | 2 |
| [model/TopLevelProperty](../model/TopLevelProperty.md) | model | 2 |

*... and 5 more units.*

## Related

*None.*

## Explore

Run these from the `gplates-code` skill directory:

```bash
python scripts/gpq.py file src/utils/QtStreamable.h
python scripts/gpq.py def GPlatesUtils::QtStreamable --body
python scripts/gpq.py uses QtStreamable --kind class
python scripts/gpq.py hier QtStreamable
```
