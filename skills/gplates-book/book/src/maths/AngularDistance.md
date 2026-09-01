# AngularDistance

[Book TOC](../../TOC.md) · [maths](../../components/maths.md) · cluster Community 27 · tier 1

| Source file | Kind | Lines |
|---|---|---|
| `src/maths/AngularDistance.h` | C++ | 208 |
| `src/maths/AngularDistance.cc` | C++ | 36 |

## Overview

A distance on the unit sphere, stored as the cosine of the angle rather than the
angle itself. The point of the class is that the natural way to obtain such a
distance — a dot product of two unit vectors — already *is* the cosine, and the
natural things to do with it (compare it against another distance, compare it
against a threshold) can be done directly on cosines. Converting to an angle
would mean an `acos` per comparison, which the header puts at roughly 100 cycles;
`calculate_angle()` exists for when the caller genuinely wants radians, and
deliberately does not cache the result so that the object stays the size of a
`double`.

It is the return type of the whole `GeometryDistance` family — `minimum_distance`
between points, great circle arcs, polylines and polygons — where a distance is
produced for every candidate pair and almost all of them are only ever compared.
Its heavier sibling `AngularExtent` also carries the sine and the angle so that
extents can be added and subtracted; `AngularExtent::get_angular_distance()`
converts down, and `AngularExtent`'s constructor converts back up. The split is
deliberate: `AngularDistance` is what you return from a calculation,
`AngularExtent` is what you use as a threshold or a bound you want to grow or
shrink.

Only `operator<` is written by hand; every other relational and equality operator
comes from the chained `boost::less_than_comparable` / `boost::equivalent` /
`boost::equality_comparable` bases. The chaining (rather than plain multiple
inheritance from three empty bases) is what keeps `sizeof(AngularDistance)` at 8
rather than 16, which matters because these objects are returned by value from
inner loops.

## Declared types

| Name | Kind | Bases | Template | Subclasses | Description |
|---|---|---|---|---|---|
| [`GPlatesMaths::AngularDistance`](#gplatesmathsangulardistance) | class | `boost::less_than_comparable<AngularDistance, boost::equivalent<AngularDistance, boost::equality_comparable<AngularDistance> > >` | — | 0 | An angular distance stored as cosine instead of the actual angle. |

## Members

### `GPlatesMaths::AngularDistance`

| Member | Kind | Type | Access | Description |
|---|---|---|---|---|
| `ZERO` | field | `AngularDistance` | public | Angular distance of zero (radians). |
| `HALF_PI` | field | `AngularDistance` | public | Angular distance of PI/2 radians (90 degrees). |
| `PI` | field | `AngularDistance` | public | Angular distance of PI radians (180 degrees). |
| `create_from_cosine( const real_t &cosine)` | method | `AngularDistance` | public | Create from the cosine of the angular distance. |
| `create_from_angle( const real_t &angle)` | method | `AngularDistance` | public | Create from an angular distance (radians) in the range \[0, PI\]. |
| `calculate_angle()` | method | `real_t` | public | Calculates the angular distance (radians) from the cosine of the angular distance. |
| `operator<( const AngularDistance &rhs)` | operator | `bool` | public | Less than operator - all other operators (\<=, \>, \>=, ==, !=) provided by boost::less\_than\_comparable, boost::equivalent and boost::equality\_comparable. |
| `is_precisely_less_than( const AngularExtentOrDistance &rhs)` | method | `bool` | public | Similar to 'operator\<' except does not have an epsilon test. |
| `is_precisely_greater_than( const AngularExtentOrDistance &rhs)` | method | `bool` | public | Similar to 'operator\>' except does not have an epsilon test. |
| `d_cosine` | field | `real_t` | private | — |
| `AngularDistance( const real_t &cosine)` | constructor | `None` | private | — |

## Free functions and macros

| Name | Kind | Type / body | Description |
|---|---|---|---|
| `ZERO` | variable | `GPlatesMaths::AngularDistance` | — |
| `HALF_PI` | variable | `GPlatesMaths::AngularDistance` | — |
| `PI` | variable | `GPlatesMaths::AngularDistance` | — |
| `GPLATES_MATHS_ANGULARDISTANCE_H` | macro | `None` | — |

## Notes

**Comparisons run backwards.** The stored value is a cosine, which is
monotonically *decreasing* over `[0, PI]`, so `operator<` returns
`d_cosine > rhs.d_cosine`. Every comparison in this class and in `AngularExtent`
reverses the same way. Getting this wrong compiles cleanly and silently inverts
the meaning of a distance test.

**The domain is `[0, PI]`, and only one entry point enforces it.**
`create_from_angle()` asserts the range with `GPlatesGlobal::Assert` and throws
`PreconditionViolationError`; `create_from_cosine()` performs no check at all, so
a cosine outside `[-1, 1]` — for example a dot product of vectors that were not
actually normalised — produces an object whose `calculate_angle()` is NaN. The
half-globe limit is the same one great circle arcs live under.

**Equality is an epsilon test and is not transitive.** `d_cosine` is
`GPlatesMaths::Real`, whose comparisons are fuzzy to `GPlatesMaths::EPSILON`, and
`boost::equivalent` synthesises `==` as `!(a < b) && !(b < a)`. So `==` on
`AngularDistance` means "within epsilon in cosine", which is not an equivalence
relation. Do not use these objects as keys in an ordered container expecting a
strict weak ordering, and note that the epsilon is on the *cosine*, so the
implied angular tolerance is coarse near 0 and PI and finest near PI/2.
`is_precisely_less_than()` and `is_precisely_greater_than()` are the escape
hatch: they go through `Real::dval()` and compare raw doubles.

**The `is_precisely_*` templates are duck-typed.** They accept anything with a
`get_cosine()` returning a `Real`, which is how the same code serves both
`AngularDistance` and `AngularExtent`; there is no concept check, so a wrong
argument type fails deep inside the template.

`ZERO`, `HALF_PI` and `PI` are namespace-scope objects defined in
`AngularDistance.cc`, so they are subject to the usual cross-translation-unit
static initialisation order rule — do not read them from another translation
unit's static initialiser.

## Used by

| Unit | Component | References |
|---|---|---|
| [app-logic/ResolvedTriangulationNetwork](../app-logic/ResolvedTriangulationNetwork.md) | app-logic | 236 |
| [maths/SmallCircleBounds](SmallCircleBounds.md) | maths | 194 |
| [opengl/GLRasterCoRegistration](../opengl/GLRasterCoRegistration.md) | opengl | 189 |
| [app-logic/GeometryUtils](../app-logic/GeometryUtils.md) | app-logic | 181 |
| [maths/GeometryDistance](GeometryDistance.md) | maths | 173 |
| [gui/MapRenderedGeometryLayerPainter](../gui/MapRenderedGeometryLayerPainter.md) | gui | 158 |
| [app-logic/TopologyReconstruct](../app-logic/TopologyReconstruct.md) | app-logic | 157 |
| [opengl/GLIntersectPrimitives](../opengl/GLIntersectPrimitives.md) | opengl | 131 |
| [app-logic/ResolvedSubSegmentRangeInSection](../app-logic/ResolvedSubSegmentRangeInSection.md) | app-logic | 110 |
| [app-logic/PlateVelocityUtils](../app-logic/PlateVelocityUtils.md) | app-logic | 98 |
| [gui/TopologyTools](../gui/TopologyTools.md) | gui | 88 |
| [opengl/GLScalarField3D](../opengl/GLScalarField3D.md) | opengl | 82 |
| [maths/GreatCircleArc](GreatCircleArc.md) | maths | 74 |
| [presentation/ReconstructionGeometryRenderer](../presentation/ReconstructionGeometryRenderer.md) | presentation | 73 |
| [utils/GeometryCreationUtils](../utils/GeometryCreationUtils.md) | utils | 61 |
| [maths/PolygonPartitioner](PolygonPartitioner.md) | maths | 58 |
| [maths/FiniteRotation](FiniteRotation.md) | maths | 56 |
| [qt-widgets/EditGeometryWidget](../qt-widgets/EditGeometryWidget.md) | qt-widgets | 49 |
| [view-operations/InsertVertexGeometryOperation](../view-operations/InsertVertexGeometryOperation.md) | view-operations | 49 |
| [view-operations/GeometryBuilder](../view-operations/GeometryBuilder.md) | view-operations | 48 |

*... and 86 more units.*

## Related

*None.*

## Explore

Run these from the `gplates-code` skill directory:

```bash
python scripts/gpq.py file src/maths/AngularDistance.h
python scripts/gpq.py def GPlatesMaths::AngularDistance --body
python scripts/gpq.py uses AngularDistance --kind class
python scripts/gpq.py hier AngularDistance
```
