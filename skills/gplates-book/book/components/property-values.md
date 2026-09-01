# property-values

[Book TOC](../TOC.md)

68 unit page(s), 125 source file(s) documented here, 1 further file(s) listed below.

## Overview

[[[PROSE component unit=component:property-values tier=1]]]
Replace this whole block, markers included, with 2-4 paragraphs: what this component is responsible for, the load-bearing units and how it connects to neighbouring components. Do not restate the unit table.
[[[/PROSE]]]

## Units

### Enumeration

| Unit | Tier | Lines | Fan-in | Description |
|---|---|---|---|---|
| [Enumeration](../src/property-values/Enumeration.md) | 2 | 220 | 114 | PropertyValue holding a GPML enumeration type paired with its selected member value |
| [EnumerationContent](../src/property-values/EnumerationContent.md) | 2 | 53 | 32 | Interned string type storing the selected member value of an Enumeration property |
| [EnumerationType](../src/property-values/EnumerationType.md) | 2 | 55 | 26 | Qualified XML name identifying which GPML enumeration an Enumeration property uses |

### Gml

| Unit | Tier | Lines | Fan-in | Description |
|---|---|---|---|---|
| [GmlDataBlock](../src/property-values/GmlDataBlock.md) | 2 | 266 | 48 | PropertyValue for gml:DataBlock holding a sequence of GmlDataBlockCoordinateList scalar coverages |
| [GmlDataBlockCoordinateList](../src/property-values/GmlDataBlockCoordinateList.md) | 2 | 383 | 110 | De-interleaved single-position values from a gml:DataBlock tupleList, tagged with a ValueObjectType |
| [GmlFile](../src/property-values/GmlFile.md) | 2 | 401 | 23 | PropertyValue for gml:File that also proxies raster bands when the file is a raster |
| [GmlGridEnvelope](../src/property-values/GmlGridEnvelope.md) | 3 | 287 | 8 | GML GridEnvelope property value representing a bounding box |
| [GmlLineString](../src/property-values/GmlLineString.md) | 2 | 262 | 28 | PropertyValue for gml:LineString wrapping a PolylineOnSphere |
| [GmlMultiPoint](../src/property-values/GmlMultiPoint.md) | 2 | 358 | 34 | PropertyValue for gml:MultiPoint, pairing a MultiPointOnSphere with per-point pos/coordinates provenance |
| [GmlOrientableCurve](../src/property-values/GmlOrientableCurve.md) | 2 | 314 | 23 | PropertyValue for gml:OrientableCurve, a thin directional decorator around a GmlLineString base curve |
| [GmlPoint](../src/property-values/GmlPoint.md) | 2 | 436 | 71 | PropertyValue for gml:Point, lazily bridging a spherical point and a 2D lat/lon (or projected) coordinate |
| [GmlPolygon](../src/property-values/GmlPolygon.md) | 2 | 259 | 19 | PropertyValue for gml:Polygon, an immutable-geometry wrapper around a PolygonOnSphere |
| [GmlRectifiedGrid](../src/property-values/GmlRectifiedGrid.md) | 2 | 486 | 10 | PropertyValue for gml:RectifiedGrid, bridging GML's grid model with GPlates' Georeferencing |
| [GmlTimeInstant](../src/property-values/GmlTimeInstant.md) | 2 | 301 | 30 | PropertyValue for gml:TimeInstant, a single GeoTimeInstant plus its XML attributes |
| [GmlTimePeriod](../src/property-values/GmlTimePeriod.md) | 2 | 446 | 31 | PropertyValue for gml:TimePeriod, a begin/end pair of GmlTimeInstant bounds with optional ordering checks |

### GpmlTopological

| Unit | Tier | Lines | Fan-in | Description |
|---|---|---|---|---|
| [GpmlTopologicalLine](../src/property-values/GpmlTopologicalLine.md) | 2 | 322 | 22 | Topological polyline defined as an ordered sequence of GpmlTopologicalSection elements |
| [GpmlTopologicalLineSection](../src/property-values/GpmlTopologicalLineSection.md) | 2 | 267 | 20 | Topological line section referencing another feature's geometry with optional reversal |
| [GpmlTopologicalNetwork](../src/property-values/GpmlTopologicalNetwork.md) | 2 | 428 | 31 | PropertyValue for a gpml:TopologicalNetwork's boundary sections and interior geometry delegates |
| [GpmlTopologicalPoint](../src/property-values/GpmlTopologicalPoint.md) | 3 | 245 | 0 | Topological section representing a point in topology operations |
| [GpmlTopologicalPolygon](../src/property-values/GpmlTopologicalPolygon.md) | 2 | 328 | 11 | PropertyValue for a gpml:TopologicalPolygon's ordered exterior boundary sections |
| [GpmlTopologicalSection](../src/property-values/GpmlTopologicalSection.md) | 2 | 194 | 47 | Abstract base PropertyValue for elements of a topological boundary or interior |

### Xs

| Unit | Tier | Lines | Fan-in | Description |
|---|---|---|---|---|
| [XsBoolean](../src/property-values/XsBoolean.md) | 3 | 228 | 6 | Property value class for XML Schema boolean type |
| [XsDouble](../src/property-values/XsDouble.md) | 2 | 229 | 15 | PropertyValue for a scalar xsi:double, GPML's floating-point property type |
| [XsInteger](../src/property-values/XsInteger.md) | 3 | 228 | 2 | Property value class for XML Schema integer type |
| [XsString](../src/property-values/XsString.md) | 2 | 239 | 38 | PropertyValue for xsi:string text, backed by interned TextContent |

### Other

| Unit | Tier | Lines | Fan-in | Description |
|---|---|---|---|---|
| [CoordinateTransformation](../src/property-values/CoordinateTransformation.md) | 2 | 505 | 63 | Wraps GDAL's OGRCoordinateTransformation to convert coordinates between two spatial reference systems |
| [GeoTimeInstant](../src/property-values/GeoTimeInstant.md) | 1 | 613 | 1175 | the scalar geological-time value type, with distant past and distant future as first-class instants |
| [Georeferencing](../src/property-values/Georeferencing.md) | 1 | 1192 | 556 | the six-coefficient affine transform mapping raster pixels to lat-lon, in GDAL's parameter order |
| [GpmlAge](../src/property-values/GpmlAge.md) | 2 | 895 | 102 | PropertyValue for gpml:Age, holding absolute and/or named geological age data with independent uncertainty fields |
| [GpmlArray](../src/property-values/GpmlArray.md) | 3 | 298 | 2 | GPML array property value holding heterogeneous collection of property values |
| [GpmlConstantValue](../src/property-values/GpmlConstantValue.md) | 2 | 318 | 54 | Property-value wrapper marking an inner value as constant across all reconstruction times |
| [GpmlFeatureReference](../src/property-values/GpmlFeatureReference.md) | 2 | 261 | 19 | Property value holding a FeatureId plus the expected FeatureType of the referenced feature |
| [GpmlFeatureSnapshotReference](../src/property-values/GpmlFeatureSnapshotReference.md) | 3 | 245 | 3 | Reference to a specific snapshot of a feature |
| [GpmlFiniteRotation](../src/property-values/GpmlFiniteRotation.md) | 2 | 417 | 21 | Property-value wrapper around a single pole-and-angle finite rotation sample plus metadata |
| [GpmlFiniteRotationSlerp](../src/property-values/GpmlFiniteRotationSlerp.md) | 3 | 150 | 0 | SLERP interpolation function for finite rotations |
| [GpmlHotSpotTrailMark](../src/property-values/GpmlHotSpotTrailMark.md) | 2 | 416 | 16 | Property value for one point along a hot-spot trail, with optional width and age data |
| [GpmlInterpolationFunction](../src/property-values/GpmlInterpolationFunction.md) | 2 | 209 | 27 | Abstract base for interpolation-function property values used by GpmlIrregularSampling |
| [GpmlIrregularSampling](../src/property-values/GpmlIrregularSampling.md) | 2 | 466 | 25 | Time-sampled property value holding an ordered vector of GpmlTimeSample plus an interpolation function |
| [GpmlKeyValueDictionary](../src/property-values/GpmlKeyValueDictionary.md) | 2 | 294 | 155 | Property value holding an ordered vector of key/value dictionary elements |
| [GpmlKeyValueDictionaryElement](../src/property-values/GpmlKeyValueDictionaryElement.md) | 2 | 181 | 23 | Single key/value pair value type stored inside a GpmlKeyValueDictionary |
| [GpmlMeasure](../src/property-values/GpmlMeasure.md) | 3 | 290 | 5 | Numeric measurement property value with XML attributes |
| [GpmlMetadata](../src/property-values/GpmlMetadata.md) | 3 | 159 | 2 | Feature collection metadata as a property value |
| [GpmlOldPlatesHeader](../src/property-values/GpmlOldPlatesHeader.md) | 2 | 592 | 61 | PLATES4 line-format header fields wrapped as a GPML property value |
| [GpmlPiecewiseAggregation](../src/property-values/GpmlPiecewiseAggregation.md) | 3 | 287 | 2 | Time-dependent property value with interval-based aggregation |
| [GpmlPlateId](../src/property-values/GpmlPlateId.md) | 3 | 232 | 4 | Tectonic plate identifier property value |
| [GpmlPolarityChronId](../src/property-values/GpmlPolarityChronId.md) | 3 | 298 | 5 | Property value for polarity chron identifier with optional era, major region and minor region attributes |
| [GpmlPropertyDelegate](../src/property-values/GpmlPropertyDelegate.md) | 2 | 241 | 18 | Reference to a named property on another feature, by feature id and expected value type |
| [GpmlRasterBandNames](../src/property-values/GpmlRasterBandNames.md) | 2 | 261 | 20 | Ordered list of band names carried by a multi-band raster feature |
| [GpmlRevisionId](../src/property-values/GpmlRevisionId.md) | 3 | 219 | 2 | Property value wrapping a revision identifier |
| [GpmlScalarField3DFile](../src/property-values/GpmlScalarField3DFile.md) | 3 | 235 | 2 | Property value for 3D scalar field file references |
| [GpmlStringList](../src/property-values/GpmlStringList.md) | 2 | 399 | 63 | Editable, order-preserving list of plain strings attached to a feature |
| [GpmlTimeSample](../src/property-values/GpmlTimeSample.md) | 2 | 271 | 133 | One time-instant sample (value, time, description, disabled flag) inside GpmlIrregularSampling |
| [GpmlTimeWindow](../src/property-values/GpmlTimeWindow.md) | 2 | 218 | 82 | One time-period window (value, period, value type) inside GpmlPiecewiseAggregation |
| [OldVersionPropertyValue](../src/property-values/OldVersionPropertyValue.md) | 3 | 242 | 0 | Property value for reading deprecated old-version GPML property types |
| [ProxiedRasterCache](../src/property-values/ProxiedRasterCache.md) | 3 | 326 | 2 | Cached raster band proxies with file modification detection |
| [ProxiedRasterResolver](../src/property-values/ProxiedRasterResolver.md) | 2 | 1170 | 14 | Resolves a proxied RawRaster into real pixel or mipmap data read from disk |
| [RasterStatistics](../src/property-values/RasterStatistics.md) | 2 | 45 | 315 | Optional min/max/mean/standard-deviation statistics for a raster band |
| [RasterType](../src/property-values/RasterType.md) | 1 | 298 | 347 | runtime tag for raster element types, plus the two maps between that tag and real C++ types |
| [RawRaster](../src/property-values/RawRaster.md) | 1 | 1401 | 794 | in-memory raster pixel data as a closed set of policy-based template instantiations with a matching visitor |
| [RawRasterUtils](../src/property-values/RawRasterUtils.md) | 1 | 1203 | 305 | the visitor and tag-dispatch layer that answers questions about a raster held as a RawRaster reference |
| [ScalarCoverageStatistics](../src/property-values/ScalarCoverageStatistics.md) | 2 | 57 | 42 | Required min/max/mean/standard-deviation statistics for a scalar coverage |
| [SpatialReferenceSystem](../src/property-values/SpatialReferenceSystem.md) | 2 | 247 | 82 | Reference-counted wrapper around GDAL/OGR's OGRSpatialReference |
| [StructuralType](../src/property-values/StructuralType.md) | 2 | 55 | 668 | Qualified XML name identifying a property value's GPML/GML structural type |
| [TextContent](../src/property-values/TextContent.md) | 2 | 55 | 73 | Interned Unicode string typedef for free-text property value content |
| [TimescaleBand](../src/property-values/TimescaleBand.md) | 2 | 58 | 28 | Interned string typedef naming bands within a geological timescale |
| [TimescaleName](../src/property-values/TimescaleName.md) | 3 | 59 | 12 | StringSetSingleton typedef for timescale names used in age properties |
| [UninterpretedPropertyValue](../src/property-values/UninterpretedPropertyValue.md) | 3 | 217 | 2 | Property value wrapping uninterpreted XML elements for unparseable properties |
| [ValueObjectType](../src/property-values/ValueObjectType.md) | 2 | 53 | 162 | Qualified XML name typedef for scalar-coverage value object types |


## Other files

| File | Kind | Lines |
|---|---|---|
| `src/property-values/CMakeLists.txt` | build | 140 |

## Depends on

| Component | References |
|---|---|
| [model](model.md) | 1603 |
| [utils](utils.md) | 383 |
| [file-io](file-io.md) | 176 |
| [maths](maths.md) | 167 |
| [global](global.md) | 130 |
| [gui](gui.md) | 105 |
| [feature-visitors](feature-visitors.md) | 95 |
| [scribe](scribe.md) | 55 |
| [system-fixes](system-fixes.md) | 3 |
| [qt-widgets](qt-widgets.md) | 1 |
| [data-mining](data-mining.md) | 1 |

## Used by

| Component | References |
|---|---|
| [file-io](file-io.md) | 2478 |
| [qt-widgets](qt-widgets.md) | 1178 |
| [app-logic](app-logic.md) | 1059 |
| [gui](gui.md) | 586 |
| [feature-visitors](feature-visitors.md) | 409 |
| [opengl](opengl.md) | 348 |
| [model](model.md) | 193 |
| [presentation](presentation.md) | 118 |
| [utils](utils.md) | 116 |
| [unit-test](unit-test.md) | 110 |
| [data-mining](data-mining.md) | 97 |
| [cli](cli.md) | 42 |
| [scribe](scribe.md) | 21 |
| [view-operations](view-operations.md) | 19 |
| [entry-points](entry-points.md) | 17 |
| [api](api.md) | 5 |
| [canvas-tools](canvas-tools.md) | 2 |
| [maths](maths.md) | 1 |

## Explore

Run these from the `gplates-code` skill directory:

```bash
python scripts/gpq.py tree src/property-values
python scripts/gpq.py sym . --mode sub --path src/property-values --defs-only
```
