# AngularExtent

[Book TOC](../../TOC.md) · [maths](../../components/maths.md) · cluster Community 27 · tier 1

| Source file | Kind | Lines |
|---|---|---|
| `src/maths/AngularExtent.h` | C++ | 452 |
| `src/maths/AngularExtent.cc` | C++ | 108 |

## Overview

[[[PROSE overview unit=maths/AngularExtent tier=1]]]
Replace this whole block, markers included, with 1-3 paragraphs: what this unit is, why it exists, and how it fits the surrounding design. Do not restate the tables below.
[[[/PROSE]]]

## Declared types

| Name | Kind | Bases | Template | Subclasses | Description |
|---|---|---|---|---|---|
| [`GPlatesMaths::AngularExtent`](#gplatesmathsangularextent) | class | `boost::addable<AngularExtent, boost::addable<AngularExtent, AngularDistance, boost::subtractable<AngularExtent, boost::subtractable<AngularExtent, AngularDistance, boost::subtractable2_left<AngularExtent, AngularDistance, boost::less_than_comparable<AngularExtent, boost::less_than_comparable<AngularExtent, AngularDistance, boost::equivalent<AngularExtent, boost::equivalent<AngularExtent, AngularDistance, boost::equality_comparable<AngularExtent, boost::equality_comparable<AngularExtent, AngularDistance> > > > > > > > > > >` | — | 0 | An angular extent stored as cosine and sine instead of the actual angle. |

## Members

### `GPlatesMaths::AngularExtent`

| Member | Kind | Type | Access | Description |
|---|---|---|---|---|
| `ZERO` | field | `AngularExtent` | public | Angular extent of zero (radians). |
| `HALF_PI` | field | `AngularExtent` | public | Angular extent of PI/2 radians (90 degrees). |
| `PI` | field | `AngularExtent` | public | Angular extent of PI radians (180 degrees). |
| `create_from_cosine( const real_t &cosine)` | method | `AngularExtent` | public | Create from the cosine of the angular extent - the sine will be calculated when/if needed. |
| `create_from_cosine_and_sine( const real_t &cosine, const real_t &sine)` | method | `AngularExtent` | public | Create from the cosine and sine of the angular extent. |
| `create_from_angle( const real_t &angle)` | method | `AngularExtent` | public | Create from an angular extent (radians) in the range \[0, PI\]. |
| `AngularExtent( const AngularDistance &angular_distance)` | constructor | `None` | public | Create from the AngularDistance (containing the cosine) - the sine will be calculated when/if needed. |
| `get_angular_distance()` | method | `AngularDistance` | public | Convenience method to create a lightweight version of AngularExtent known as AngularDistance. |
| `operator+=` | field | `AngularExtent` | public | A member function for adding an angular extent to 'this' angular extent. |
| `operator-=` | field | `AngularExtent` | public | A member function for subtracting an angular extent from 'this' angular extent. |
| `operator<( const AngularExtent &rhs)` | operator | `bool` | public | Less than operator comparison with another AngularExtent. |
| `operator<( const AngularDistance &rhs)` | operator | `bool` | public | Less than operator comparison with AngularDistance. |
| `operator>( const AngularDistance &rhs)` | operator | `bool` | public | Greater than operator comparison with AngularDistance. |
| `is_precisely_less_than( const AngularExtentOrDistance &rhs)` | method | `bool` | public | Similar to 'operator\<' except does not have an epsilon test. |
| `is_precisely_greater_than( const AngularExtentOrDistance &rhs)` | method | `bool` | public | Similar to 'operator\>' except does not have an epsilon test. |
| `d_cosine` | field | `real_t` | private | — |
| `d_sine` | field | `boost::optional<real_t>` | private | Sine of angular extent - only calculated when needed. |
| `d_angle` | field | `boost::optional<real_t>` | private | Angular extent - only calculated when needed. |
| `AngularExtent( const real_t &cosine, boost::optional<real_t> sine = boost::none, boost::optional<real_t> angle = boost::none)` | constructor | `None` | private | — |

## Free functions and macros

| Name | Kind | Type / body | Description |
|---|---|---|---|
| `ZERO` | variable | `GPlatesMaths::AngularExtent` | — |
| `HALF_PI` | variable | `GPlatesMaths::AngularExtent` | — |
| `PI` | variable | `GPlatesMaths::AngularExtent` | — |
| `GPLATES_MATHS_ANGULAREXTENT_H` | macro | `None` | — |

## Notes

[[[PROSE notes unit=maths/AngularExtent tier=1]]]
Replace this whole block, markers included, with invariants, ownership, threading or gotchas that are not visible in the tables. Write *None.* if there is nothing worth saying.
[[[/PROSE]]]

## Used by

| Unit | Component | References |
|---|---|---|
| [maths/GeometryDistance](GeometryDistance.md) | maths | 74 |
| [maths/SmallCircleBounds](SmallCircleBounds.md) | maths | 71 |
| [app-logic/GeometryUtils](../app-logic/GeometryUtils.md) | app-logic | 63 |
| [app-logic/TopologyIntersections](../app-logic/TopologyIntersections.md) | app-logic | 52 |
| [feature-visitors/ViewFeatureGeometriesWidgetPopulator](../feature-visitors/ViewFeatureGeometriesWidgetPopulator.md) | feature-visitors | 42 |
| [file-io/OgrReader](../file-io/OgrReader.md) | file-io | 42 |
| [file-io/GpmlStructuralTypeReaderUtils](../file-io/GpmlStructuralTypeReaderUtils.md) | file-io | 36 |
| [maths/GreatCircleArc](GreatCircleArc.md) | maths | 35 |
| [app-logic/ReconstructLayerProxy](../app-logic/ReconstructLayerProxy.md) | app-logic | 34 |
| [qt-widgets/MovePoleWidget](../qt-widgets/MovePoleWidget.md) | qt-widgets | 33 |
| [view-operations/GeometryBuilder](../view-operations/GeometryBuilder.md) | view-operations | 33 |
| [maths/Rotation](Rotation.md) | maths | 32 |
| [maths/DateLineWrapper](DateLineWrapper.md) | maths | 29 |
| [file-io/GpmlOutputVisitor](../file-io/GpmlOutputVisitor.md) | file-io | 24 |
| [feature-visitors/QueryFeaturePropertiesWidgetPopulator](../feature-visitors/QueryFeaturePropertiesWidgetPopulator.md) | feature-visitors | 19 |
| [file-io/OgrGeometryExporter](../file-io/OgrGeometryExporter.md) | file-io | 19 |
| [maths/CubeQuadTreePartition](CubeQuadTreePartition.md) | maths | 18 |
| [file-io/GMTFormatGeometryExporter](../file-io/GMTFormatGeometryExporter.md) | file-io | 17 |
| [file-io/PlatesLineFormatGeometryExporter](../file-io/PlatesLineFormatGeometryExporter.md) | file-io | 17 |
| [file-io/PlatesLineFormatReader](../file-io/PlatesLineFormatReader.md) | file-io | 17 |

*... and 73 more units.*

## Related

*None.*

## Explore

Run these from the `gplates-code` skill directory:

```bash
python scripts/gpq.py file src/maths/AngularExtent.h
python scripts/gpq.py def GPlatesMaths::AngularExtent --body
python scripts/gpq.py uses AngularExtent --kind class
python scripts/gpq.py hier AngularExtent
```
