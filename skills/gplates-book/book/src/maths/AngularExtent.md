# AngularExtent

[Book TOC](../../TOC.md) · [maths](../../components/maths.md) · cluster Community 27 · tier 1

| Source file | Kind | Lines |
|---|---|---|
| `src/maths/AngularExtent.h` | C++ | 452 |
| `src/maths/AngularExtent.cc` | C++ | 108 |

## Overview

The arithmetic counterpart of `AngularDistance`: an angle in `[0, PI]` held as its
cosine, plus a lazily computed sine and a lazily computed angle. Where
`AngularDistance` exists to be returned and compared cheaply, `AngularExtent`
exists to be *adjusted* — grown and shrunk — which is why it carries the sine.
`operator+=` and `operator-=` use the angle-sum identities
`cos(a±b) = cos a cos b ∓ sin a sin b` and `sin(a±b) = sin a cos b ± cos a sin b`,
so adding two extents costs four multiplies and no `acos`.

That capability is what makes region-of-interest queries possible without ever
leaving cosine space. `BoundingSmallCircle` and `InnerOuterBoundingSmallCircle`
in `SmallCircleBounds` store their radii as `AngularExtent` and expose
`expand()` / `contract()` directly in terms of it; a "everything within 10 km of
this geometry" query becomes "expand the bounding circle by the angle subtended
by 10 km, then do an ordinary overlap test". The same objects are what
`GeometryDistance` takes as its optional `minimum_distance_threshold`, letting
the distance routines reject candidate pairs by a single cosine comparison, and
what `CubeQuadTreePartition` traversals use to prune subtrees.

Conversion between the two types is explicit in both directions —
`get_angular_distance()` down, the `AngularExtent(const AngularDistance &)`
constructor up — and the mixed-type operator set means an `AngularExtent` can be
compared with, added to and subtracted from an `AngularDistance` without the
caller writing the conversion. The declared base list is one deeply chained
template rather than a dozen sibling bases purely to stop the empty boost
operator bases from inflating the object; the effective operator set is
enumerated in the comments in the header.

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

**Arithmetic saturates, it does not wrap.** The class invariant is that the angle
stays in `[0, PI]`, and both operators enforce it: `operator+=` clamps to `PI`
(cosine `-1`) and `operator-=` clamps to `ZERO` (cosine `1`). This is not an error
path, it is the intended semantics — a bounding small circle of radius PI already
covers the globe, and contracting past zero would be meaningless. It does mean
`a + b - b != a` in general, and that `-=` cannot be used to detect
"the threshold was exceeded".

**`operator+=` has two code paths with different cost and different precision.**
If either cosine is strictly negative — i.e. either angle exceeds PI/2 — the
angle-sum identity is abandoned, because beyond PI the cosine stops being a
one-to-one encoding of the angle. That branch calls `acos` on both operands, adds
the angles, and clamps. Large extents therefore cost roughly two `acos` per
addition; the header notes this is expected to be rare.

**Comparisons run backwards and are epsilon-fuzzy.** As in `AngularDistance`,
`operator<` returns `d_cosine > rhs.d_cosine`, and because `d_cosine` is
`GPlatesMaths::Real` the comparison carries an epsilon; `boost::equivalent`
derives `==` from it, so equality means "within epsilon in cosine". Use
`is_precisely_less_than()` / `is_precisely_greater_than()` when an exact
comparison is required — they compare raw doubles via `Real::dval()` and are
templated on anything exposing `get_cosine()`, so they work against either type.

**`const` methods mutate the object.** `d_sine` and `d_angle` are `mutable`
`boost::optional` caches filled on first call to `get_sine()` and `get_angle()`.
Two threads calling `get_sine()` concurrently on the same `const AngularExtent &`
is a data race. Because `SmallCircleBounds` hands out `const AngularExtent &`
from its bounding circles, sharing one bound across worker threads is exactly the
situation where this bites.

**Nothing validates cosine against sine.** `create_from_cosine_and_sine()` takes
the caller's word that both describe the same angle — the header says so
explicitly — and inconsistent inputs silently corrupt every subsequent addition
and subtraction. When only a cosine is supplied, `get_sine()` derives it as
`sqrt(1 - cos²)`, which is correct precisely because the angle is constrained to
`[0, PI]` where the sine is non-negative.

**Converting from `AngularDistance` is not free.** The conversion constructor
copies only the cosine, so the first `+=` or `-=` involving a converted value
pays a `sqrt` to recover the sine. The `operator+=`/`operator-=` overloads taking
an `AngularDistance` are convenience wrappers around exactly that conversion.
`AngularExtent` is also several times the size of `AngularDistance` — cosine plus
two `boost::optional<Real>` — so it is the wrong type to return from a
tight-loop distance calculation.

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
