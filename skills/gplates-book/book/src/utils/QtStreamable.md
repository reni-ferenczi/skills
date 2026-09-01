# QtStreamable

[Book TOC](../../TOC.md) · [utils](../../components/utils.md) · cluster Community 5 · tier 2

| Source file | Kind | Lines |
|---|---|---|
| `src/utils/QtStreamable.h` | C++ | 111 |

## Overview

[[[PROSE overview unit=utils/QtStreamable tier=2]]]
Replace this whole block, markers included, with 1-3 paragraphs: what this unit is, why it exists, and how it fits the surrounding design. Do not restate the tables below.
[[[/PROSE]]]

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

[[[PROSE notes unit=utils/QtStreamable tier=2]]]
Replace this whole block, markers included, with invariants, ownership, threading or gotchas that are not visible in the tables. Write *None.* if there is nothing worth saying.
[[[/PROSE]]]

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
