# MathsUtils

[Book TOC](../../TOC.md) · [maths](../../components/maths.md) · cluster Community 766 · tier 1

| Source file | Kind | Lines |
|---|---|---|
| `src/maths/MathsUtils.h` | C++ | 261 |
| `src/maths/MathsUtils.cc` | C++ | 67 |

## Overview

[[[PROSE overview unit=maths/MathsUtils tier=1]]]
Replace this whole block, markers included, with 1-3 paragraphs: what this unit is, why it exists, and how it fits the surrounding design. Do not restate the tables below.
[[[/PROSE]]]

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

[[[PROSE notes unit=maths/MathsUtils tier=1]]]
Replace this whole block, markers included, with invariants, ownership, threading or gotchas that are not visible in the tables. Write *None.* if there is nothing worth saying.
[[[/PROSE]]]

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
