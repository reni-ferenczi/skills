# Real

[Book TOC](../../TOC.md) · [maths](../../components/maths.md) · cluster Community 107 · tier 1

| Source file | Kind | Lines |
|---|---|---|
| `src/maths/Real.h` | C++ | 540 |
| `src/maths/Real.cc` | C++ | 335 |

## Overview

[[[PROSE overview unit=maths/Real tier=1]]]
Replace this whole block, markers included, with 1-3 paragraphs: what this unit is, why it exists, and how it fits the surrounding design. Do not restate the tables below.
[[[/PROSE]]]

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

[[[PROSE notes unit=maths/Real tier=1]]]
Replace this whole block, markers included, with invariants, ownership, threading or gotchas that are not visible in the tables. Write *None.* if there is nothing worth saying.
[[[/PROSE]]]

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
