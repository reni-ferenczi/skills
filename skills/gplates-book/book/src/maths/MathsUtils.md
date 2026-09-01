# MathsUtils

[Book TOC](../../TOC.md) · [maths](../../components/maths.md) · cluster Community 766 · tier 1

| Source file | Kind | Lines |
|---|---|---|
| `src/maths/MathsUtils.h` | C++ | 261 |
| `src/maths/MathsUtils.cc` | C++ | 67 |

## Overview

This header defines the tolerances that the rest of GPlates compares floating-point
numbers with. It is a small file with very large consequences: `GPlatesMaths::EPSILON`
is what makes `Real::operator<` — and therefore `Real`'s `==`, `UnitVector3D`'s `==`,
`PointOnSphere`'s `==`, `GreatCircleArc`'s zero-length test and every "closeness"
comparison in `maths` — approximate rather than exact. `GEO_TIMES_EPSILON` plays the
same role for reconstruction time, where `GeoTimeInstant` needs two times a fraction of
a day apart to count as the same instant. Changing a constant here changes the behaviour
of geometry code that never mentions this file.

The comments are worth reading before touching the values, because they record how the
numbers were arrived at and that the author was not confident in them. `EPSILON` started
as 1e-14 — two orders of magnitude above IEEE 754 machine epsilon, chosen to absorb
accumulated error from chains of operations such as rotating a unit vector by a matrix
and then re-checking its magnitude — and was loosened to 1e-12 in 2004 because 1e-14
turned out to be too strict. `TIGHTER_EPSILON` sits marginally below `EPSILON` and
exists so `are_slightly_more_strictly_equal` can be a shade stricter than
`are_almost_exactly_equal`. `is_in_range` widens both of its bounds by `EPSILON`, which
is why the latitude and longitude checks in `LatLonPoint` accept values a hair outside
their nominal ranges.

The degree/radian conversions are the other half of the file. They are templates
dispatched on `boost::is_integral` for one specific reason, spelled out in the comment:
an integer literal argument must not be truncated back to `int` by the `T(...)`
construction, so the integral overload returns `double`. Otherwise `T` passes straight
through, which is what lets the same call site work for `double` and for
`GPlatesMaths::Real`. `has_infinity_and_nan` and `assert_has_infinity_and_nan` are a
startup platform check rather than general utilities — all three entry points
(`gplates_main.cc`, `gplates_demo_no_gui_main.cc`, `gplates_unit_test_main.cc`) call the
assert form early, because `Real`'s NaN and infinity handling assumes those values
exist.

## Declared types

*None.*

## Members

*None.*

## Free functions and macros

| Name | Kind | Type / body | Description |
|---|---|---|---|
| `type_has_infinity_and_nan()` | function | `bool` | — |
| `GPLATES_MATHS_MATHUTILS_H` | macro | `None` | — |
| `EPSILON` | variable | `double` | The "standard" epsilon used in GPlates for floating-point comparisons. |
| `TIGHTER_EPSILON` | variable | `double` | A tighter epsilon: TIGHTER\_EPSILON \< EPSILON. |
| `GEO_TIMES_EPSILON` | variable | `double` | An epsilon suitable for the comparison of geological times. |
| `are_almost_exactly_equal( T value1, T value2)` | function | `bool` | — |
| `are_slightly_more_strictly_equal( T value1, T value2)` | function | `bool` | — |
| `are_geo_times_approximately_equal( T value1, T value2)` | function | `bool` | JB's original commentary moved here from FloatingPointComparisons.h: Determine whether the two geological times geo\_time1 and geo\_time2 are equal (within a small epsilon). |
| `is_in_range( T value, T minimum, T maximum)` | function | `bool` | — |
| `PI` | variable | `double` | \\f$ \\pi \\f$, the ratio of the circumference to the diameter of a circle. |
| `HALF_PI` | variable | `double` | \\f$ \\frac{\\pi}{2} \\f$. |
| `convert_deg_to_rad( const T &value_in_degrees, boost::false_type/*is_integral*/)` | function | `T` | — |
| `convert_deg_to_rad( int value_in_degrees, boost::true_type/*is_integral*/)` | function | `double` | — |
| `convert_rad_to_deg( const T &value_in_radians, boost::false_type/*is_integral*/)` | function | `T` | — |
| `convert_rad_to_deg( int value_in_radians, boost::true_type/*is_integral*/)` | function | `double` | — |
| `convert_deg_to_rad( const T &value_in_degrees)` | function | `typename boost::mpl::if_<boost::is_integral<T>, double, T>::type` | Converts degrees to radians. |
| `convert_rad_to_deg( const T &value_in_radians)` | function | `typename boost::mpl::if_<boost::is_integral<T>, double, T>::type` | Converts radians to degrees. |
| `has_infinity_and_nan()` | function | `bool` | Returns true if the float and double built-in types have infinity and NaN. |
| `assert_has_infinity_and_nan()` | function | `void` | Terminates the application with an error message if the float and double built-in types do not have infinity and NaN. |

## Notes

**The comparisons are absolute, not relative.** Every one of them computes
`value1 - value2` and tests it against a fixed epsilon. That is a reasonable tolerance
for the unit-magnitude vectors, dot products and cosines this file was written for, all
of which live in [-1, 1]. It degenerates towards exact equality for large magnitudes: at
a value of around 1e4 the 1e-12 band is already down to a few ulps, so
`are_almost_exactly_equal` on projected map coordinates or long time spans is not doing
what its name suggests. The `T` template parameter also has to be something whose
difference converts to `double`, so it is not meaningful for unsigned integer types.

**`Real` does not use these templates on itself.** `Real.h` declares
`are_almost_exactly_equal`, `are_slightly_more_strictly_equal` and `is_in_range` as
friend overloads that unwrap to the raw `double` and then call the versions here,
explicitly "for consistency". `Real::operator<` inlines the `EPSILON` comparison
directly. So a change to `EPSILON` propagates to `Real` through two separate paths, and
both must stay in agreement.

**Constant definitions, not declarations.** `EPSILON`, `TIGHTER_EPSILON`,
`GEO_TIMES_EPSILON`, `PI` and `HALF_PI` are `static const double` at namespace scope in
a header, so each translation unit that includes it gets its own copy with internal
linkage. The values are identical, but their addresses are not, and they are not
external symbols you can inspect from a single place.

`assert_has_infinity_and_nan` calls `exit(1)` after a `qWarning`. It does not throw, so
it cannot be caught, mocked, or exercised by a test — the check is deliberately fatal and
happens before anything else runs.

The `FIXME` on `EPSILON` is still open: the header records that the value was guessed
rather than derived, and was already loosened once when the original guess proved too
strict.

## Used by

| Unit | Component | References |
|---|---|---|
| [gui/SimpleGlobeOrientation](../gui/SimpleGlobeOrientation.md) | gui | 74 |
| [unit-test/RealTest](../unit-test/RealTest.md) | unit-test | 31 |
| [unit-test/TranscribeTest](../unit-test/TranscribeTest.md) | unit-test | 25 |
| [opengl/GLNormalMapSource](../opengl/GLNormalMapSource.md) | opengl | 23 |
| [gui/GlobeRenderedGeometryLayerPainter](../gui/GlobeRenderedGeometryLayerPainter.md) | gui | 20 |
| [property-values/GeoTimeInstant](../property-values/GeoTimeInstant.md) | property-values | 20 |
| [gui/AgeColourPalettes](../gui/AgeColourPalettes.md) | gui | 18 |
| [utils/FeatureUtils](../utils/FeatureUtils.md) | utils | 18 |
| [app-logic/GenerateVelocityDomainTerra](../app-logic/GenerateVelocityDomainTerra.md) | app-logic | 16 |
| [gui/SceneLightingParameters](../gui/SceneLightingParameters.md) | gui | 15 |
| [maths/AzimuthalEqualAreaProjection](AzimuthalEqualAreaProjection.md) | maths | 15 |
| [app-logic/ResolvedTriangulationDelaunay2](../app-logic/ResolvedTriangulationDelaunay2.md) | app-logic | 13 |
| [app-logic/TimeSpanUtils](../app-logic/TimeSpanUtils.md) | app-logic | 13 |
| [gui/AnimationController](../gui/AnimationController.md) | gui | 12 |
| [gui/GraticuleSettings](../gui/GraticuleSettings.md) | gui | 12 |
| [opengl/GLMultiResolutionRaster](../opengl/GLMultiResolutionRaster.md) | opengl | 12 |
| [gui/Mipmapper](../gui/Mipmapper.md) | gui | 11 |
| [opengl/GLStateSets](../opengl/GLStateSets.md) | opengl | 11 |
| [gui/MapGrid](../gui/MapGrid.md) | gui | 10 |
| [opengl/GLScalarFieldDepthLayersSource](../opengl/GLScalarFieldDepthLayersSource.md) | opengl | 10 |

*... and 142 more units.*

## Related

*None.*

## Explore

Run these from the `gplates-code` skill directory:

```bash
python scripts/gpq.py file src/maths/MathsUtils.h
```
