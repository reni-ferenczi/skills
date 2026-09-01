# Real

[Book TOC](../../TOC.md) · [maths](../../components/maths.md) · cluster Community 107 · tier 1

| Source file | Kind | Lines |
|---|---|---|
| `src/maths/Real.h` | C++ | 540 |
| `src/maths/Real.cc` | C++ | 335 |

## Overview

`Real` is a `double` with different comparison semantics, and nothing else. Arithmetic, streaming
and the transcendental functions all forward straight to the underlying `double`; the whole point of
the class is that `operator<` is written as `r2.dval() - r1.dval() > EPSILON` (1e-12, from
`MathsUtils.h`), so "less than" means "less by more than a tolerance". Everything else follows from
Boost.Operators: the base is a chain of `less_than_comparable` → `equivalent` →
`equality_comparable`, so `==` is *defined* as "neither operand is less than the other", i.e. the
two values are within `EPSILON`. That chaining is deliberate rather than incidental — the comment
above the base list notes it keeps `sizeof(Real)` at 8 instead of the 16 that multiple inheritance
from several empty bases would produce, which matters because `real_t` (the alias in
`src/maths/types.h`) is `Real`, and it is the scalar of every vector, rotation and geometry type in
`GPlatesMaths`.

The reason for all this is that spherical geometry accumulates rounding error and then feeds it into
functions with hard domain boundaries. `acos` and `asin` in particular are handed dot products that
should lie in [-1, 1] but land at 1.0000000000000002; so the free functions here clamp: if the
argument is outside the domain but inside it *by `Real`'s own tolerant comparison*, they silently
return the value at the boundary (`asin` gives ±HALF_PI, `acos` gives 0 or PI, `sqrt` gives 0), and
only a genuinely out-of-range value raises `FunctionDomainException`. `atan2` is likewise defined to
return 0 at (0, 0) so it has no invalid domain at all. Callers that need the *exact* comparison
back — because the tolerant one would be wrong, as when testing the sign of a signed area or picking
the greater of two closeness values — use `is_precisely_greater_than` / `is_precisely_less_than`, or
the `is_strictly_*` free functions, which all bypass the epsilon.

The remaining surface is plumbing: NaN and infinity predicates in both member and free-template form
(over `boost::math::isnan` and friends), streaming to `std::ostream`, `QDebug` and `QTextStream` as
non-member overloads (again to keep the object small — the comment explains it is why `Real` does
not inherit `GPlatesUtils::QtStreamable`), and a private `transcribe` that delegates to the raw
`double` so `Real`, `float` and `double` are interchangeable in saved sessions and projects.

## Declared types

| Name | Kind | Bases | Template | Subclasses | Description |
|---|---|---|---|---|---|
| [`GPlatesMaths::Real`](#gplatesmathsreal) | class | `boost::less_than_comparable<Real, boost::equivalent<Real, boost::equality_comparable<Real> > >` | — | 0 | An instance of this class is a floating-point approximation to an element of the field of real numbers. |

## Members

### `GPlatesMaths::Real`

| Member | Kind | Type | Access | Description |
|---|---|---|---|---|
| `Real()` | constructor | `None` | public | NOTE: For same reason we are \*not\* inheriting from 'GPlatesUtils::QtStreamable\<Real\>' and instead explicitly providing 'operator \<\<' overloads as non-member functions. public GPlatesUtils::QtStreamable\<Real\> |
| `Real( const double &d)` | constructor | `None` | public | — |
| `is_precisely_greater_than( const double &d)` | method | `bool` | public | — |
| `is_precisely_less_than( const double &d)` | method | `bool` | public | — |
| `is_nan()` | method | `bool` | public | — |
| `is_infinity()` | method | `bool` | public | — |
| `is_positive_infinity()` | method | `bool` | public | — |
| `is_negative_infinity()` | method | `bool` | public | — |
| `is_finite()` | method | `bool` | public | — |
| `quiet_nan()` | method | `Real` | public | — |
| `positive_infinity()` | method | `Real` | public | — |
| `negative_infinity()` | method | `Real` | public | — |
| `_dval` | field | `double` | private | — |
| `transcribe( GPlatesScribe::Scribe &scribe, bool transcribed_construct_data)` | method | `GPlatesScribe::TranscribeResult` | private | — |

## Free functions and macros

| Name | Kind | Type / body | Description |
|---|---|---|---|
| `operator <<( QDebug dbg, const Real &r)` | operator | `QDebug` | — |
| `GPLATES_MATHS_REAL_H` | macro | `None` | — |
| `operator<<` | variable | `std::ostream` | — |
| `operator>>` | variable | `std::istream` | — |
| `operator <<` | variable | `QTextStream` | Gives us: QTextStream text\_stream(device); text\_stream \<\< r; |
| `are_almost_exactly_equal( const Real &r1, const Real &r2)` | function | `bool` | Returns whether the two supplied real numbers r1 and r2 are equal to within the standard equality tolerance. |
| `are_slightly_more_strictly_equal( const Real &r1, const Real &r2)` | function | `bool` | Returns whether the two supplied real numbers r1 and r2 are equal to within a slightly stricter tolerance than the standard equality tolerance, aka GPlatesMaths::EPSILON. |
| `is_in_range( const Real &value, const Real &minimum, const Real &maximum)` | function | `bool` | — |
| `operator<( const Real &r1, const Real &r2)` | operator | `bool` | All of the other operators are supplied by Boost operators. |
| `abs( const Real &r1)` | function | `Real` | — |
| `is_strictly_positive( const Real &r)` | function | `bool` | Using the exact value of the Real, return whether it is positive (ie. greater than exact zero) or not. |
| `is_strictly_negative( const Real &r)` | function | `bool` | Using the exact value of the Real, return whether it is negative (ie. less than exact zero) or not. |
| `is_strictly_greater_than_one( const Real &r)` | function | `bool` | Using the exact value of the Real, return whether it is greater than exact one or not. |
| `is_strictly_less_than_minus_one( const Real &r)` | function | `bool` | Using the exact value of the Real, return whether it is greater than exact minus-one or not. |
| `operator+(Real r1, Real r2)` | operator | `Real` | — |
| `operator-(Real r1, Real r2)` | operator | `Real` | — |
| `operator*(Real r1, Real r2)` | operator | `Real` | — |
| `operator/(Real r1, Real r2)` | operator | `Real` | — |
| `operator-(Real r)` | operator | `Real` | — |
| `sin(Real r)` | function | `Real` | — |
| `cos(Real r)` | function | `Real` | — |
| `tan(Real r)` | function | `Real` | — |
| `sqrt( const Real &r)` | function | `Real` | Calculate the square-root of r. r must be non-negative. |
| `asin( const Real &r)` | function | `Real` | Calculate the arc sine of r. @r must lie in the valid domain of the arc sine function, the closed range \[-1, 1\]. |
| `acos( const Real &r)` | function | `Real` | Calculate the arc cosine of r. @r must lie in the valid domain of the arc cosine function, the closed range \[-1, 1\]. |
| `atan2( const Real &y, const Real &x)` | function | `Real` | Calculate the two-variable arc tangent of y and x. |
| `is_nan( T d)` | function | `bool` | — |
| `is_infinity( T d)` | function | `bool` | — |
| `is_positive_infinity( T d)` | function | `bool` | — |
| `is_negative_infinity( T d)` | function | `bool` | — |
| `is_finite( T d)` | function | `bool` | — |
| `quiet_nan()` | function | `T` | The following assumes std::numeric\_limits\<double\>::is\_iec559 is true. |
| `positive_infinity()` | function | `T` | — |
| `negative_infinity()` | function | `T` | — |

## Notes

**Equality is not transitive, and the ordering is not a strict weak ordering.** `a == b` means
`|a - b| <= EPSILON`, so `a == b` and `b == c` does not give `a == c`. That makes `Real` unsafe as a
`std::map` or `std::set` key and unsafe for `std::sort`, `std::lower_bound` and anything else that
requires a strict weak ordering — the standard library's preconditions are violated, not merely
strained. Sort on `dval()` if you need an ordering you can rely on.

**EPSILON is absolute, not relative.** It is a fixed 1e-12 difference. Two values around 1e9 will
compare equal only if they are bitwise near-identical (the tolerance is far below their ULP), while
two values around 1e-13 always compare equal to each other and to zero. `Real` is calibrated for
quantities of order one — direction cosines, unit-sphere coordinates, radians — which is what the
rest of `GPlatesMaths` deals in. It is the wrong type for very large or very small magnitudes.

**Conversion from `double` is implicit.** The single-argument constructor is not `explicit`, so a
`double` silently becomes a `Real` in any comparison or overload resolution, picking up the epsilon
semantics with it. That is convenient in expressions and a trap when you meant an exact comparison;
`is_precisely_greater_than` and `is_precisely_less_than` take a raw `double` for exactly this
reason.

**Domain corrections are silent.** `sqrt`, `asin` and `acos` clamp a slightly-out-of-domain argument
to the boundary and return without any diagnostic — the "we should log that we corrected this here"
FIXMEs are still open, and the `std::cerr` traces are behind a `WARNINGS` macro that the top of
`Real.cc` deliberately leaves undefined. If a result looks pinned at exactly 0, PI or ±PI/2, suspect
a clamp upstream.

**Out-of-domain aborts in debug builds.** The failure path goes through
`GPlatesGlobal::Assert<FunctionDomainException>`, which throws only when `GPLATES_DEBUG` is *not*
defined; in a debug build it calls `GPlatesGlobal::Abort` instead. Do not write a debug-build test
that expects to catch `FunctionDomainException` from `acos`.

**`0.0` is the one exact comparison in the file.** `atan2` compares both arguments against zero with
`==`, with a comment noting zero is the only floating-point value for which exact equality is valid
— but since `Real::operator==` is the epsilon one, that comparison actually accepts anything within
1e-12 of zero.

## Used by

| Unit | Component | References |
|---|---|---|
| [gui/GlobeRenderedGeometryLayerPainter](../gui/GlobeRenderedGeometryLayerPainter.md) | gui | 44 |
| [unit-test/TranscribeTest](../unit-test/TranscribeTest.md) | unit-test | 30 |
| [unit-test/RealTest](../unit-test/RealTest.md) | unit-test | 29 |
| [app-logic/TopologyNetworkParams](../app-logic/TopologyNetworkParams.md) | app-logic | 24 |
| [utils/FeatureUtils](../utils/FeatureUtils.md) | utils | 23 |
| [gui/AgeColourPalettes](../gui/AgeColourPalettes.md) | gui | 22 |
| [property-values/GeoTimeInstant](../property-values/GeoTimeInstant.md) | property-values | 20 |
| [app-logic/ResolvedTriangulationNetwork](../app-logic/ResolvedTriangulationNetwork.md) | app-logic | 18 |
| [maths/AzimuthalEqualAreaProjection](AzimuthalEqualAreaProjection.md) | maths | 17 |
| [maths/GeometryInterpolation](GeometryInterpolation.md) | maths | 15 |
| [maths/GreatCircleArc](GreatCircleArc.md) | maths | 12 |
| [opengl/GLRasterCoRegistration](../opengl/GLRasterCoRegistration.md) | opengl | 12 |
| [app-logic/PropertyExtractors](../app-logic/PropertyExtractors.md) | app-logic | 10 |
| [gui/BuiltinColourPalettes](../gui/BuiltinColourPalettes.md) | gui | 10 |
| [app-logic/GenerateVelocityDomainTerra](../app-logic/GenerateVelocityDomainTerra.md) | app-logic | 9 |
| [maths/GeneratePoints](GeneratePoints.md) | maths | 9 |
| [maths/SphericalArea](SphericalArea.md) | maths | 9 |
| [scribe/ScribeTextArchiveWriter](../scribe/ScribeTextArchiveWriter.md) | scribe | 9 |
| [scribe/ScribeXmlArchiveWriter](../scribe/ScribeXmlArchiveWriter.md) | scribe | 9 |
| [maths/CartesianConvMatrix3D](CartesianConvMatrix3D.md) | maths | 8 |

*... and 121 more units.*

## Related

*None.*

## Explore

Run these from the `gplates-code` skill directory:

```bash
python scripts/gpq.py file src/maths/Real.h
python scripts/gpq.py def GPlatesMaths::Real --body
python scripts/gpq.py uses Real --kind class
python scripts/gpq.py hier Real
```
