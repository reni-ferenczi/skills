# maths

[Book TOC](../TOC.md)

89 unit page(s), 142 source file(s) documented here, 1 further file(s) listed below.

## Overview

`maths` is the geometric kernel of GPlates: the scalar type, the vectors, the
rotations and the four shapes in which every position on the globe is expressed.
Nothing above it computes on the sphere directly — a feature's geometry, a
reconstructed outline, a raster tile's extent and a picked vertex are all values
defined here. Two commitments run through the whole module. Comparison is
approximate: `Real` — aliased `real_t` by `types` and included almost everywhere
through that alias — is a `double` whose `operator<` means "less by more than
`EPSILON`", and `MathsUtils` holds that constant together with the degree/radian
conversions, so a tolerance change in one small header moves the behaviour of
geometry code that never mentions it. And geometry is immutable: `GeometryOnSphere`
and its four concrete shapes hand out only `const` pointers, are intrusively
reference-counted, and cache their derived quantities lazily inside themselves.
Reconstructing a feature therefore always builds a new geometry rather than editing
one, which is what makes the same geometry safely shareable between unrelated
callers, and what makes caching derived values on the geometry legal in the first
place.

The stack is easiest to read from the bottom. `GenericVectorOps3D` holds the single
implementation of dot, cross and scale that both `Vector3D` and `UnitVector3D`
forward to; the two share no base class precisely so that a unit vector cannot
inherit an operation capable of breaking its magnitude-1 invariant, and
`Vector3D::get_normalisation()` is the one sanctioned bridge back. `UnitVector3D` is
what carries the sphere — a position, a rotation axis and a cube-face axis are all
one — and `PointOnSphere` is nothing but one of them, deliberately kept a small
value type outside the polymorphic hierarchy because it is multiplied by every
vertex of every geometry in a reconstruction. `GreatCircleArc` pairs two points and
is the element type that `PolylineOnSphere` and `PolygonOnSphere` actually store,
which is why vertex iteration in both is an adapter riding an arc sequence, and why
`MultiPointOnSphere`, which stores points directly, is the odd one out.
`LatLonPoint` is the only door between degrees and unit vectors, and
`ConstGeometryOnSphereVisitor` the only sanctioned way back from the base type to a
concrete shape. On the rotation side `UnitQuaternion3D` is the representation and
`FiniteRotation` the plate-motion value built on it, with `Rotation` as the
time-independent sibling used for dragging the globe and laying out shapes, and
`CalculateVelocity` turning a pair of finite rotations into a velocity at a point.

Above that sits the machinery that keeps queries cheap. `AngularDistance` stores a
distance as a cosine so that comparisons never pay for an `acos`, and `AngularExtent`
adds the sine so that a bound can be grown and shrunk without leaving cosine space;
almost every spatial structure in the module is expressed in that pair.
`SmallCircleBounds` supplies the bounding circles that reject far-apart geometries
before a single arc is touched, `PolyGreatCircleArcBoundingTree` refines that per
geometry, and `CubeQuadTreePartition` — a loose quad tree on the six faces of a cube,
rebuilt for every geometry at every reconstruction time — is the global spatial index,
with `CubeCoordinateFrame` as the one definition of the cube's faces and axes and
`CubeQuadTree` as the payload-agnostic container beneath. Results have their own
vocabulary too: `GeometryIntersect` returns a graph of intersection locations that
keeps segment provenance, which is what lets per-vertex quantities survive
partitioning and what the topology machinery is built on, while `ProximityHitDetail`
is the shared answer type for hit tests, rankable by closeness before anyone knows
what was hit. `DateLineWrapper` is the exception to the module's usual inward focus:
it clips geometry at ±180° and converts it to lat/lon, because that conversion is a
whole-geometry operation and not a per-point one.

Downward, `maths` rests on `global` for the assertion machinery and the exception
root that `MathematicalException` extends, on `utils` for the reference counting
behind every geometry and for Earth's radius in the velocity calculations, and on
`scribe` only so that scalars and geometries can be transcribed into saved sessions
and projects. Upward it is the widest dependency in the tree. `app-logic` is the
heaviest consumer: rotation files become `FiniteRotation`s, `ReconstructionTree`
caches one composed rotation per edge, and walking a plate circuit is quaternion
multiplication performed here — which is also why the argument order of `compose` is
documented so insistently. `opengl` shares `CubeCoordinateFrame` so that raster
tiling and geometry partitioning index the same globe face-for-face; `file-io`
crosses at `LatLonPoint` in both directions and at `DateLineWrapper` for OGR export,
which likewise serves the 2-D map painter in `gui`. `view-operations`,
`canvas-tools` and `qt-widgets` come in mainly through proximity — hit details
collected from everything under the cursor and sorted by closeness — and through
`GeometryType`, the plain enum that lets interface code say which kind of geometry
it is holding without depending on the geometry classes themselves. The
`src/maths/deprecated` subdirectory is a separate matter: earlier rotation-history
and grid classes kept in the tree but superseded by `FiniteRotation` and the
reconstruction code in `app-logic`.

## Units

### `src/maths`

#### Cube

| Unit | Tier | Lines | Fan-in | Description |
|---|---|---|---|---|
| [CubeCoordinateFrame](../src/maths/CubeCoordinateFrame.md) | 1 | 865 | 443 | The one convention for the cube around the globe: face axes, corners, edges, cross-face node offsets |
| [CubeQuadTree](../src/maths/CubeQuadTree.md) | 1 | 901 | 521 | Six quad trees on a cube plus a cube-root element; pure structure with no geometry knowledge |
| [CubeQuadTreeLocation](../src/maths/CubeQuadTreeLocation.md) | 2 | 546 | 84 | Value type identifying a cube-face quad-tree node, or the cube's root, by address |
| [CubeQuadTreePartition](../src/maths/CubeQuadTreePartition.md) | 1 | 2036 | 580 | Loose cube quad tree indexing geometries by bounding small circle, rebuilt each reconstruction time |
| [CubeQuadTreePartitionUtils](../src/maths/CubeQuadTreePartitionUtils.md) | 2 | 949 | 26 | Algorithms to mirror, merge and find intersections across CubeQuadTreePartition trees |

#### Geometry

| Unit | Tier | Lines | Fan-in | Description |
|---|---|---|---|---|
| [GeometryCrossing](../src/maths/GeometryCrossing.md) | 3 | 263 | 0 | Filters intersection graphs to identify true geometric crossings vs touches and overlaps |
| [GeometryDistance](../src/maths/GeometryDistance.md) | 2 | 2704 | 13 | Minimum angular distance, closest points and segment indices between any two geometry shapes |
| [GeometryForwardDeclarations](../src/maths/GeometryForwardDeclarations.md) | 3 | 51 | 0 | Forward declarations for spherical geometry classes to reduce compilation dependencies |
| [GeometryInterpolation](../src/maths/GeometryInterpolation.md) | 3 | 1730 | 0 | Interpolates between two polylines along small circle arcs with latitude and longitude alignment |
| [GeometryIntersect](../src/maths/GeometryIntersect.md) | 1 | 1848 | 270 | finds every crossing and vertex-touch between two polylines/polygons, robustly and with segment provenance |
| [GeometryOnSphere](../src/maths/GeometryOnSphere.md) | 1 | 112 | 893 | abstract root of the four sphere geometries: immutable, reference-counted, reached by visitor |
| [GeometryType](../src/maths/GeometryType.md) | 2 | 47 | 463 | Runtime tag distinguishing point, multi-point, polyline and polygon GeometryOnSphere shapes |

#### Invalid

| Unit | Tier | Lines | Fan-in | Description |
|---|---|---|---|---|
| [InvalidGreatCircleArcException](../src/maths/InvalidGreatCircleArcException.md) | 3 | 77 | 0 | Exception thrown when creating great-circle arcs that violate class invariants |
| [InvalidGridException](../src/maths/InvalidGridException.md) | 3 | 75 | 4 | Exception thrown when creating grids that violate grid invariants |
| [InvalidLatLonCoordinateException](../src/maths/InvalidLatLonCoordinateException.md) | 2 | 151 | 24 | Exception for an invalid latitude or longitude found while pairing a coordinate sequence |
| [InvalidLatLonException](../src/maths/InvalidLatLonException.md) | 2 | 140 | 9 | Exception thrown when a LatLonPoint is constructed from an invalid latitude or longitude |
| [InvalidOperationException](../src/maths/InvalidOperationException.md) | 3 | 75 | 6 | Raised when an invalid mathematical operation is attempted |
| [InvalidPolylineContainsOnlyOnePointException](../src/maths/InvalidPolylineContainsOnlyOnePointException.md) | 3 | 72 | 0 | Raised when a polyline contains only one point |
| [InvalidPolylineContainsZeroPointsException](../src/maths/InvalidPolylineContainsZeroPointsException.md) | 3 | 72 | 0 | Raised when a polyline contains no points |

#### Point

| Unit | Tier | Lines | Fan-in | Description |
|---|---|---|---|---|
| [PointInPolygon](../src/maths/PointInPolygon.md) | 2 | 1933 | 36 | Spherical point-in-polygon testing, from a cheap linear function to an O(log n) tree-based test |
| [PointLiesOnGreatCircleArc](../src/maths/PointLiesOnGreatCircleArc.md) | 3 | 176 | 1 | Function object testing whether a point lies on a great circle arc |
| [PointOnSphere](../src/maths/PointOnSphere.md) | 1 | 815 | 371 | the 24-byte unit-vector point every other spherical geometry is built from, plus its heap-allocated wrapper |
| [PointProximityHitDetail](../src/maths/PointProximityHitDetail.md) | 3 | 98 | 2 | Proximity hit information for single-point geometries |

#### Polygon

| Unit | Tier | Lines | Fan-in | Description |
|---|---|---|---|---|
| [PolygonFan](../src/maths/PolygonFan.md) | 2 | 456 | 24 | Builds a triangular fan mesh anchored at a polygon's centroid, for stencil-based interior fill rendering |
| [PolygonMesh](../src/maths/PolygonMesh.md) | 2 | 1558 | 31 | Triangulates a polygon's true interior region via gnomonic projection, CGAL Delaunay triangulation and edge-split refinement |
| [PolygonOnSphere](../src/maths/PolygonOnSphere.md) | 1 | 3415 | 1296 | closed spherical geometry of one exterior ring plus optional holes, with a lazy cache of derived values |
| [PolygonOrientation](../src/maths/PolygonOrientation.md) | 2 | 364 | 98 | Determines whether a polygon ring winds clockwise or counterclockwise viewed from above the globe |
| [PolygonPartitioner](../src/maths/PolygonPartitioner.md) | 2 | 1137 | 11 | Clips points, polylines and polygons against a fixed polygon, classifying pieces inside/outside/intersecting |
| [PolygonProximityHitDetail](../src/maths/PolygonProximityHitDetail.md) | 3 | 101 | 4 | Proximity hit information for polygon geometries |

#### Polyline

| Unit | Tier | Lines | Fan-in | Description |
|---|---|---|---|---|
| [PolylineEquivalencePredicates](../src/maths/PolylineEquivalencePredicates.md) | 3 | 110 | 1 | Function objects for testing polyline equivalence |
| [PolylineIntersections](../src/maths/PolylineIntersections.md) | 2 | 933 | 36 | Builds a traversable graph of intersections and partitioned segments for two geometries |
| [PolylineOnSphere](../src/maths/PolylineOnSphere.md) | 1 | 1601 | 158 | open chain of great circle arcs on the sphere, with a lazy cache of length, centroid and bounds |
| [PolylineProximityHitDetail](../src/maths/PolylineProximityHitDetail.md) | 3 | 101 | 3 | A concrete ProximityHitDetail subclass for polyline proximity hits |

#### Proximity

| Unit | Tier | Lines | Fan-in | Description |
|---|---|---|---|---|
| [ProximityCriteria](../src/maths/ProximityCriteria.md) | 3 | 120 | 1 | Parameter holder for proximity testing criteria on the sphere |
| [ProximityHitDetail](../src/maths/ProximityHitDetail.md) | 1 | 173 | 210 | the shared result vocabulary for geometry hit tests: closeness, optional vertex index, visitable subclasses |
| [ProximityHitDetailVisitor](../src/maths/ProximityHitDetailVisitor.md) | 2 | 146 | 6 | Abstract Visitor base for the ProximityHitDetail hierarchy, with a no-op default per hit type |

#### Small

| Unit | Tier | Lines | Fan-in | Description |
|---|---|---|---|---|
| [SmallCircle](../src/maths/SmallCircle.md) | 2 | 384 | 47 | A circle of latitude around an arbitrary axis, stored as axis plus cosine of colatitude |
| [SmallCircleArc](../src/maths/SmallCircleArc.md) | 2 | 266 | 108 | A bounded arc of a small circle defined by axis, start point and angular extent |
| [SmallCircleBounds](../src/maths/SmallCircleBounds.md) | 1 | 2613 | 105 | Spherical bounding volumes: a centred small circle, or two concentric ones bounding an annulus, plus their builders |
| [SmallCircleCoverageMesh](../src/maths/SmallCircleCoverageMesh.md) | 3 | 238 | 0 | A triangular mesh that covers a region bounded by a small circle |
| [SmallCircleProximityHitDetail](../src/maths/SmallCircleProximityHitDetail.md) | 3 | 96 | 0 | A concrete ProximityHitDetail subclass for small circle proximity hits |

#### Unable

| Unit | Tier | Lines | Fan-in | Description |
|---|---|---|---|---|
| [UnableToExtendPointlikeArcException](../src/maths/UnableToExtendPointlikeArcException.md) | 3 | 80 | 0 | Exception when extending a pointlike great circle arc |
| [UnableToIntersectEquivalentGreatCirclesException](../src/maths/UnableToIntersectEquivalentGreatCirclesException.md) | 3 | 79 | 0 | Exception when intersecting equivalent great circles |
| [UnableToNormaliseZeroVectorException](../src/maths/UnableToNormaliseZeroVectorException.md) | 3 | 65 | 1 | Exception when normalizing a zero vector |

#### Violated

| Unit | Tier | Lines | Fan-in | Description |
|---|---|---|---|---|
| [ViolatedClassInvariantException](../src/maths/ViolatedClassInvariantException.md) | 3 | 76 | 7 | Exception thrown when mathematical class invariants are violated |
| [ViolatedDirVectorInvariantException](../src/maths/ViolatedDirVectorInvariantException.md) | 3 | 75 | 0 | Exception thrown when direction vector invariants are violated |
| [ViolatedSmallCircleInvariantException](../src/maths/ViolatedSmallCircleInvariantException.md) | 3 | 75 | 0 | Exception thrown when small circle invariants are violated |
| [ViolatedUnitVectorInvariantException](../src/maths/ViolatedUnitVectorInvariantException.md) | 3 | 74 | 1 | Exception thrown when unit vector invariants are violated |

#### Other

| Unit | Tier | Lines | Fan-in | Description |
|---|---|---|---|---|
| [AngularDistance](../src/maths/AngularDistance.md) | 1 | 244 | 3228 | Lightweight spherical distance held as a cosine, the size of a double, for comparison-only use |
| [AngularExtent](../src/maths/AngularExtent.md) | 1 | 560 | 1170 | Angular distance that can be grown and shrunk, carrying lazily computed sine and angle |
| [AzimuthalEqualAreaProjection](../src/maths/AzimuthalEqualAreaProjection.md) | 2 | 320 | 104 | Lambert azimuthal equal-area projection centred on an arbitrary point, not just a pole |
| [CalculateVelocity](../src/maths/CalculateVelocity.md) | 2 | 457 | 149 | Computes plate velocity vectors and stage rotations from pairs of finite rotations |
| [CartesianConvMatrix3D](../src/maths/CartesianConvMatrix3D.md) | 2 | 350 | 8 | Change-of-basis matrix between geocentric and local North/East/Down frames at a point |
| [Centroid](../src/maths/Centroid.md) | 2 | 636 | 31 | Three weighting schemes (point-average, arc-length, area) for spherical geometry centroids |
| [ConstGeometryOnSphereVisitor](../src/maths/ConstGeometryOnSphereVisitor.md) | 2 | 125 | 111 | Abstract Visitor base for read-only traversal of concrete geometry-on-sphere types |
| [DateLineWrapper](../src/maths/DateLineWrapper.md) | 1 | 4466 | 350 | clips polylines and polygons at the dateline and converts them to lat/lon for map views and OGR export |
| [EllipseGenerator](../src/maths/EllipseGenerator.md) | 2 | 206 | 32 | Samples points on an oriented ellipse on the sphere via one tangent-plane rotation |
| [FiniteRotation](../src/maths/FiniteRotation.md) | 1 | 1155 | 2110 | the plate-motion value type: an Euler-pole rotation held as a unit quaternion, with composition and SLERP |
| [FiniteRotationSnapshotTable](../src/maths/FiniteRotationSnapshotTable.md) | 3 | 60 | 0 | Snapshot of the rotation hierarchy at a particular geological time |
| [FunctionDomainException](../src/maths/FunctionDomainException.md) | 2 | 76 | 56 | Exception thrown when a math function's argument falls outside its valid domain |
| [GeneratePoints](../src/maths/GeneratePoints.md) | 2 | 732 | 6 | Generates uniform point distributions across the globe, a lat/lon box, or a polygon |
| [GenericVectorOps3D](../src/maths/GenericVectorOps3D.md) | 1 | 111 | 682 | the single shared implementation of 3-D vector arithmetic behind Vector3D and UnitVector3D |
| [GnomonicProjection](../src/maths/GnomonicProjection.md) | 2 | 409 | 12 | Projects sphere points to and from a tangent plane, preserving great circles as lines |
| [GreatCircle](../src/maths/GreatCircle.md) | 2 | 288 | 29 | A whole great circle stored as its axis, with containment, equivalence and tessellation helpers |
| [GreatCircleArc](../src/maths/GreatCircleArc.md) | 1 | 2026 | 837 | the edge primitive of spherical geometry: two endpoints plus lazily cached length and rotation axis |
| [HighPrecision](../src/maths/HighPrecision.md) | 2 | 140 | 27 | Stream wrapper that prints one value at 18 significant digits, then restores precision |
| [IndeterminateArcRotationAxisException](../src/maths/IndeterminateArcRotationAxisException.md) | 3 | 81 | 1 | Exception thrown for zero-length great-circle arcs with indeterminate rotation axes |
| [IndeterminateResultException](../src/maths/IndeterminateResultException.md) | 3 | 75 | 7 | Exception thrown when mathematical calculations produce indeterminate results |
| [LatLonPoint](../src/maths/LatLonPoint.md) | 1 | 256 | 2111 | degrees latitude/longitude boundary type and the only conversion to and from unit-vector positions |
| [MathematicalException](../src/maths/MathematicalException.md) | 2 | 50 | 20 | Common base class for every exception thrown by the GPlatesMaths module |
| [MathsUtils](../src/maths/MathsUtils.md) | 1 | 328 | 699 | the epsilon constants, approximate comparisons and degree/radian conversions the whole maths module rests on |
| [MultiPointOnSphere](../src/maths/MultiPointOnSphere.md) | 1 | 739 | 1875 | immutable ordered bag of points as a GeometryOnSphere, with lazily cached centroid and bounding small circle |
| [MultiPointProximityHitDetail](../src/maths/MultiPointProximityHitDetail.md) | 3 | 100 | 2 | Proximity hit information for multi-point geometries |
| [PolyGreatCircleArcBoundingTree](../src/maths/PolyGreatCircleArcBoundingTree.md) | 2 | 743 | 99 | Binary bounding-small-circle tree over a sequence of great circle arcs, shared by polylines and polygons |
| [Real](../src/maths/Real.md) | 1 | 875 | 629 | the epsilon-tolerant double used as the scalar of every GPlatesMaths type, with domain-guarded functions |
| [Rotation](../src/maths/Rotation.md) | 1 | 696 | 194 | time-independent axis-angle rotation backed by a unit quaternion, applied to vectors and whole geometries |
| [SphericalArea](../src/maths/SphericalArea.md) | 2 | 592 | 14 | Free functions computing signed spherical areas of polygons and point/edge triangles |
| [SphericalSubdivision](../src/maths/SphericalSubdivision.md) | 2 | 533 | 41 | Two recursive whole-sphere subdivision schemes exposed via a shared visitor traversal |
| [TrailingLatLonCoordinateException](../src/maths/TrailingLatLonCoordinateException.md) | 3 | 128 | 1 | Exception for odd-length latitude/longitude coordinate sequences |
| [UnitQuaternion3D](../src/maths/UnitQuaternion3D.md) | 1 | 988 | 366 | The unit-norm quaternion underneath every finite rotation, with axis/angle recovery and slerp scaffolding |
| [UnitVector3D](../src/maths/UnitVector3D.md) | 1 | 611 | 1281 | Magnitude-1 3D vector enforced at construction; the type that represents a position or axis on the globe |
| [Vector3D](../src/maths/Vector3D.md) | 1 | 403 | 248 | Unconstrained 3D vector, the invariant-free counterpart that holds non-unit results |
| [types](../src/maths/types.md) | 1 | 49 | 798 | Header holding the module-wide real\_t alias for the epsilon-comparing Real, plus a vestigial rotation-id alias |

### `src/maths/deprecated`

| Unit | Tier | Lines | Fan-in | Description |
|---|---|---|---|---|
| [GridOnSphere](../src/maths/deprecated/GridOnSphere.md) | 3 | 530 | 3 | Parametric representation of a rectangular grid on sphere surface |
| [PolylineIntersections_test](../src/maths/deprecated/PolylineIntersections_test.md) | 3 | 3999 | 0 | Regression test suite for polyline intersection and partitioning |
| [PythonWrapper](../src/maths/deprecated/PythonWrapper.md) | 3 | 43 | 0 | Boost.Python module wrapping core maths types for Python |
| [RotationHistory](../src/maths/deprecated/RotationHistory.md) | 3 | 241 | 0 | Container for rotation sequences describing plate motion history |
| [RotationSequence](../src/maths/deprecated/RotationSequence.md) | 3 | 631 | 7 | time-dependent sequence of plate rotations supporting interpolation and future extrapolation |
| [StageRotation](../src/maths/deprecated/StageRotation.md) | 3 | 326 | 0 | difference between finite rotations representing angular displacement over time |


## Other files

| File | Kind | Lines |
|---|---|---|
| `src/maths/CMakeLists.txt` | build | 147 |

## Depends on

| Component | References |
|---|---|
| [global](global.md) | 726 |
| [utils](utils.md) | 523 |
| [gui](gui.md) | 34 |
| [data-mining](data-mining.md) | 19 |
| [qt-widgets](qt-widgets.md) | 18 |
| [opengl](opengl.md) | 18 |
| [scribe](scribe.md) | 17 |
| [app-logic](app-logic.md) | 7 |
| [view-operations](view-operations.md) | 4 |
| [deprecated](deprecated.md) | 2 |
| [model](model.md) | 1 |
| [file-io](file-io.md) | 1 |
| [system-fixes](system-fixes.md) | 1 |
| [property-values](property-values.md) | 1 |
| [unit-test](unit-test.md) | 1 |

## Used by

| Component | References |
|---|---|
| [app-logic](app-logic.md) | 4425 |
| [opengl](opengl.md) | 3183 |
| [file-io](file-io.md) | 2405 |
| [gui](gui.md) | 2136 |
| [view-operations](view-operations.md) | 1688 |
| [qt-widgets](qt-widgets.md) | 1496 |
| [feature-visitors](feature-visitors.md) | 395 |
| [canvas-tools](canvas-tools.md) | 390 |
| [utils](utils.md) | 271 |
| [presentation](presentation.md) | 219 |
| [property-values](property-values.md) | 167 |
| [unit-test](unit-test.md) | 163 |
| [data-mining](data-mining.md) | 152 |
| [cli](cli.md) | 84 |
| [model](model.md) | 84 |
| [scribe](scribe.md) | 84 |
| [entry-points](entry-points.md) | 39 |
| [deprecated](deprecated.md) | 22 |
| [api](api.md) | 7 |

## Explore

Run these from the `gplates-code` skill directory:

```bash
python scripts/gpq.py tree src/maths
python scripts/gpq.py sym . --mode sub --path src/maths --defs-only
```
