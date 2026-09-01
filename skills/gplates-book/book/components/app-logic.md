# app-logic

[Book TOC](../TOC.md)

145 unit page(s), 271 source file(s) documented here, 1 further file(s) listed below.

## Overview

[[[PROSE component unit=component:app-logic tier=1]]]
Replace this whole block, markers included, with 2-4 paragraphs: what this component is responsible for, the load-bearing units and how it connects to neighbouring components. Do not restate the unit table.
[[[/PROSE]]]

## Units

### `src/app-logic`

#### Co

| Unit | Tier | Lines | Fan-in | Description |
|---|---|---|---|---|
| [CoRegistrationData](../src/app-logic/CoRegistrationData.md) | 2 | 178 | 202 | ReconstructionGeometry wrapper holding a co-registration result data table |
| [CoRegistrationLayerParams](../src/app-logic/CoRegistrationLayerParams.md) | 2 | 161 | 38 | LayerParams holding a co-registration layer's configuration table |
| [CoRegistrationLayerProxy](../src/app-logic/CoRegistrationLayerProxy.md) | 2 | 838 | 103 | Co-registers reconstructed seed geometries against target geometries or rasters |
| [CoRegistrationLayerTask](../src/app-logic/CoRegistrationLayerTask.md) | 2 | 415 | 13 | Wires a co-registration layer's params and proxy into the reconstruct graph |

#### Layer

| Unit | Tier | Lines | Fan-in | Description |
|---|---|---|---|---|
| [Layer](../src/app-logic/Layer.md) | 1 | 1173 | 992 | (pending) |
| [LayerInputChannelName](../src/app-logic/LayerInputChannelName.md) | 1 | 156 | 734 | (pending) |
| [LayerInputChannelType](../src/app-logic/LayerInputChannelType.md) | 2 | 227 | 78 | Declares the data type and arity a layer's named input channel accepts |
| [LayerParams](../src/app-logic/LayerParams.md) | 1 | 99 | 1270 | (pending) |
| [LayerParamsVisitor](../src/app-logic/LayerParamsVisitor.md) | 2 | 134 | 158 | Templated double-dispatch base for visiting each concrete LayerParams subclass |
| [LayerProxy](../src/app-logic/LayerProxy.md) | 1 | 110 | 554 | (pending) |
| [LayerProxyUtils](../src/app-logic/LayerProxyUtils.md) | 1 | 1120 | 2552 | (pending) |
| [LayerProxyVisitor](../src/app-logic/LayerProxyVisitor.md) | 1 | 230 | 228 | (pending) |
| [LayerTask](../src/app-logic/LayerTask.md) | 2 | 199 | 15 | Abstract interface every concrete layer implementation plugs into the reconstruct graph through |
| [LayerTaskRegistry](../src/app-logic/LayerTaskRegistry.md) | 2 | 435 | 101 | Registry of factory closures used to create LayerTask instances by type |
| [LayerTaskType](../src/app-logic/LayerTaskType.md) | 2 | 129 | 219 | Enumeration of the nine layer kinds, transcribed by name for session/project compatibility |

#### Raster

| Unit | Tier | Lines | Fan-in | Description |
|---|---|---|---|---|
| [RasterLayerParams](../src/app-logic/RasterLayerParams.md) | 2 | 387 | 50 | Raster layer's selected band, per-band statistics, georeferencing, spatial reference system and type |
| [RasterLayerProxy](../src/app-logic/RasterLayerProxy.md) | 1 | 1762 | 349 | (pending) |
| [RasterLayerTask](../src/app-logic/RasterLayerTask.md) | 3 | 490 | 2 | Layer task for reconstructing geo-referenced raster data |

#### Reconstruct

| Unit | Tier | Lines | Fan-in | Description |
|---|---|---|---|---|
| [ReconstructContext](../src/app-logic/ReconstructContext.md) | 1 | 1715 | 381 | (pending) |
| [ReconstructGraph](../src/app-logic/ReconstructGraph.md) | 1 | 1766 | 118 | (pending) |
| [ReconstructGraphImpl](../src/app-logic/ReconstructGraphImpl.md) | 2 | 1064 | 43 | Private graph representation behind ReconstructGraph: layers, data nodes and input connections |
| [ReconstructHandle](../src/app-logic/ReconstructHandle.md) | 1 | 79 | 761 | (pending) |
| [ReconstructLayerParams](../src/app-logic/ReconstructLayerParams.md) | 2 | 196 | 13 | Reconstruct layer's ReconstructParams plus a topology-reconstruction prompt flag |
| [ReconstructLayerProxy](../src/app-logic/ReconstructLayerProxy.md) | 1 | 2795 | 285 | (pending) |
| [ReconstructLayerTask](../src/app-logic/ReconstructLayerTask.md) | 3 | 590 | 2 | Layer task that reconstructs feature geometries from input collections |
| [ReconstructMethodByPlateId](../src/app-logic/ReconstructMethodByPlateId.md) | 2 | 974 | 35 | Reconstructs a feature by rotating its present-day geometry using its plate ID |
| [ReconstructMethodFiniteRotation](../src/app-logic/ReconstructMethodFiniteRotation.md) | 1 | 158 | 459 | (pending) |
| [ReconstructMethodFlowline](../src/app-logic/ReconstructMethodFlowline.md) | 3 | 445 | 2 | Reconstructs flowline features by tracking plate motion through time |
| [ReconstructMethodHalfStageRotation](../src/app-logic/ReconstructMethodHalfStageRotation.md) | 3 | 838 | 2 | Reconstructs features using half-stage rotations from plate IDs |
| [ReconstructMethodInterface](../src/app-logic/ReconstructMethodInterface.md) | 1 | 480 | 396 | (pending) |
| [ReconstructMethodMotionPath](../src/app-logic/ReconstructMethodMotionPath.md) | 3 | 299 | 2 | Reconstructs motion path features showing point trajectories through time |
| [ReconstructMethodRegistry](../src/app-logic/ReconstructMethodRegistry.md) | 2 | 578 | 16 | Registry mapping ReconstructMethod::Type to construction/matching callbacks for ReconstructMethodInterface |
| [ReconstructMethodSmallCircle](../src/app-logic/ReconstructMethodSmallCircle.md) | 3 | 338 | 2 | Reconstruction method for small circle features; rotates the centre point via plate ID |
| [ReconstructMethodType](../src/app-logic/ReconstructMethodType.md) | 2 | 58 | 385 | Enumerates the ways a feature can be reconstructed into geometry |
| [ReconstructMethodVirtualGeomagneticPole](../src/app-logic/ReconstructMethodVirtualGeomagneticPole.md) | 3 | 562 | 2 | Reconstruction method for VGP (paleomagnetic pole) features with uncertainty parameters |
| [ReconstructParams](../src/app-logic/ReconstructParams.md) | 2 | 624 | 102 | Value object holding tunable options for reconstructing features into geometries |
| [ReconstructScalarCoverageLayerParams](../src/app-logic/ReconstructScalarCoverageLayerParams.md) | 2 | 543 | 15 | LayerParams for a reconstruct-scalar-coverage layer, tracking the selected scalar type and statistics |
| [ReconstructScalarCoverageLayerProxy](../src/app-logic/ReconstructScalarCoverageLayerProxy.md) | 2 | 1416 | 23 | LayerProxy that evolves scalar coverages (e.g. crustal thickness) over a deforming domain |
| [ReconstructScalarCoverageLayerTask](../src/app-logic/ReconstructScalarCoverageLayerTask.md) | 3 | 359 | 2 | Layer task for reconstructing and evolving scalar coverages like crustal thickness |
| [ReconstructScalarCoverageParams](../src/app-logic/ReconstructScalarCoverageParams.md) | 2 | 126 | 23 | Parameters object for configuring scalar coverage deformation/evolution |
| [ReconstructUtils](../src/app-logic/ReconstructUtils.md) | 2 | 870 | 43 | Free functions that reconstruct feature geometry to a palaeo time |

#### Reconstructed

| Unit | Tier | Lines | Fan-in | Description |
|---|---|---|---|---|
| [ReconstructedFeatureGeometry](../src/app-logic/ReconstructedFeatureGeometry.md) | 1 | 680 | 1116 | (pending) |
| [ReconstructedFeatureGeometryFinder](../src/app-logic/ReconstructedFeatureGeometryFinder.md) | 2 | 350 | 10 | Weak observer visitor that collects the RFGs currently observing a given feature |
| [ReconstructedFlowline](../src/app-logic/ReconstructedFlowline.md) | 2 | 283 | 28 | RFG subclass holding the left/right traced polylines and plate IDs of a reconstructed flowline |
| [ReconstructedMotionPath](../src/app-logic/ReconstructedMotionPath.md) | 2 | 259 | 20 | RFG subclass holding the traced polyline of a reconstructed motion path |
| [ReconstructedScalarCoverage](../src/app-logic/ReconstructedScalarCoverage.md) | 2 | 419 | 55 | Pairs a reconstructed domain geometry with per-point scalar values evolving over time |
| [ReconstructedSmallCircle](../src/app-logic/ReconstructedSmallCircle.md) | 2 | 215 | 10 | RFG subclass holding the centre point and radius of a reconstructed small circle |
| [ReconstructedVirtualGeomagneticPole](../src/app-logic/ReconstructedVirtualGeomagneticPole.md) | 2 | 242 | 32 | RFG subclass carrying a reconstructed virtual geomagnetic pole and its palaeomagnetic parameters |

#### Reconstruction

| Unit | Tier | Lines | Fan-in | Description |
|---|---|---|---|---|
| [Reconstruction](../src/app-logic/Reconstruction.md) | 2 | 358 | 67 | Accumulated active-layer output of the reconstruct graph at one time and anchor plate |
| [ReconstructionFeatureProperties](../src/app-logic/ReconstructionFeatureProperties.md) | 2 | 399 | 93 | Feature visitor extracting common reconstruction-related properties in one pass |
| [ReconstructionGeometry](../src/app-logic/ReconstructionGeometry.md) | 1 | 159 | 808 | (pending) |
| [ReconstructionGeometryFinder](../src/app-logic/ReconstructionGeometryFinder.md) | 2 | 353 | 26 | Weak-observer visitor collecting the reconstruction geometries derived from a feature, optionally filtered |
| [ReconstructionGeometryUtils](../src/app-logic/ReconstructionGeometryUtils.md) | 1 | 1766 | 280 | (pending) |
| [ReconstructionGeometryVisitor](../src/app-logic/ReconstructionGeometryVisitor.md) | 1 | 437 | 460 | (pending) |
| [ReconstructionGraph](../src/app-logic/ReconstructionGraph.md) | 1 | 362 | 279 | (pending) |
| [ReconstructionGraphBuilder](../src/app-logic/ReconstructionGraphBuilder.md) | 2 | 370 | 19 | Incrementally builds an immutable ReconstructionGraph from inserted total reconstruction sequences |
| [ReconstructionGraphPopulator](../src/app-logic/ReconstructionGraphPopulator.md) | 2 | 417 | 4 | Feature visitor extracting Total Reconstruction Sequence features into a ReconstructionGraphBuilder |
| [ReconstructionLayerParams](../src/app-logic/ReconstructionLayerParams.md) | 3 | 124 | 4 | Qt-based wrapper for reconstruction layer parameters with visitor pattern and signals |
| [ReconstructionLayerProxy](../src/app-logic/ReconstructionLayerProxy.md) | 2 | 629 | 52 | Layer proxy that builds and caches ReconstructionTree objects for a rotation layer at requested times and anchors |
| [ReconstructionLayerTask](../src/app-logic/ReconstructionLayerTask.md) | 3 | 300 | 2 | Layer task that builds ReconstructionTree from rotation features; core engine of reconstruction |
| [ReconstructionParams](../src/app-logic/ReconstructionParams.md) | 2 | 171 | 16 | Comparable, serialisable settings bundle for building reconstruction trees, currently one flag |
| [ReconstructionTree](../src/app-logic/ReconstructionTree.md) | 1 | 919 | 339 | (pending) |
| [ReconstructionTreeCreator](../src/app-logic/ReconstructionTreeCreator.md) | 1 | 800 | 157 | (pending) |

#### Resolved

| Unit | Tier | Lines | Fan-in | Description |
|---|---|---|---|---|
| [ResolvedRaster](../src/app-logic/ResolvedRaster.md) | 2 | 265 | 96 | ReconstructionGeometry wrapping the layer proxies behind a resolved raster feature |
| [ResolvedScalarField3D](../src/app-logic/ResolvedScalarField3D.md) | 2 | 215 | 13 | ReconstructionGeometry wrapping the ScalarField3DLayerProxy behind a resolved 3D scalar field feature |
| [ResolvedSubSegmentRangeInSection](../src/app-logic/ResolvedSubSegmentRangeInSection.md) | 1 | 1495 | 519 | (pending) |
| [ResolvedTopologicalBoundary](../src/app-logic/ResolvedTopologicalBoundary.md) | 2 | 338 | 18 | Resolved topological polygon built from an ordered sequence of boundary sub-segments |
| [ResolvedTopologicalGeometry](../src/app-logic/ResolvedTopologicalGeometry.md) | 2 | 317 | 5 | Abstract base for resolved topological polygons/polylines, sharing feature bookkeeping and cached plate ID/formation time |
| [ResolvedTopologicalGeometrySubSegment](../src/app-logic/ResolvedTopologicalGeometrySubSegment.md) | 2 | 456 | 132 | One clipped run of a topological section's vertices contributing to a resolved topology |
| [ResolvedTopologicalLine](../src/app-logic/ResolvedTopologicalLine.md) | 2 | 336 | 19 | Resolved topological polyline, assembled from sub-segments with lazy per-vertex source tracking |
| [ResolvedTopologicalNetwork](../src/app-logic/ResolvedTopologicalNetwork.md) | 2 | 514 | 14 | Resolved deforming-network topology wrapping a triangulated interior and boundary sub-segments |
| [ResolvedTopologicalSection](../src/app-logic/ResolvedTopologicalSection.md) | 2 | 133 | 28 | Groups every shared sub-segment derived from one topological-section feature across all resolved topologies |
| [ResolvedTopologicalSharedSubSegment](../src/app-logic/ResolvedTopologicalSharedSubSegment.md) | 2 | 482 | 52 | A section sub-segment paired with every resolved topology that shares it, each with its own reversal flag |
| [ResolvedTopologicalSubSegmentImpl](../src/app-logic/ResolvedTopologicalSubSegmentImpl.md) | 2 | 1147 | 10 | Shared implementation of vertex-source-info and sub-sub-segment lookup for both sub-segment classes |
| [ResolvedTriangulationDelaunay2](../src/app-logic/ResolvedTriangulationDelaunay2.md) | 1 | 1498 | 632 | (pending) |
| [ResolvedTriangulationNetwork](../src/app-logic/ResolvedTriangulationNetwork.md) | 1 | 3626 | 112 | (pending) |
| [ResolvedTriangulationUtils](../src/app-logic/ResolvedTriangulationUtils.md) | 2 | 296 | 38 | Header-only CGAL/PointOnSphere conversion and interpolation helpers for the ResolvedTriangulation code |
| [ResolvedVertexSourceInfo](../src/app-logic/ResolvedVertexSourceInfo.md) | 1 | 845 | 165 | (pending) |

#### Scalar

| Unit | Tier | Lines | Fan-in | Description |
|---|---|---|---|---|
| [ScalarCoverageEvolution](../src/app-logic/ScalarCoverageEvolution.md) | 2 | 2130 | 52 | Evolves crustal-thickness and tectonic-subsidence scalar values on a deforming network over time |
| [ScalarCoverageFeatureProperties](../src/app-logic/ScalarCoverageFeatureProperties.md) | 2 | 635 | 83 | Recognises and extracts domain/range scalar coverage data from ordinary features by property-name convention |
| [ScalarCoverageTimeSpan](../src/app-logic/ScalarCoverageTimeSpan.md) | 2 | 752 | 8 | Public front end combining evolved and non-evolved scalar coverage values over a geometry time span |
| [ScalarField3DLayerParams](../src/app-logic/ScalarField3DLayerParams.md) | 2 | 346 | 44 | Layer parameters caching a 3D scalar field feature and its file-derived statistics |
| [ScalarField3DLayerProxy](../src/app-logic/ScalarField3DLayerProxy.md) | 2 | 1281 | 34 | Layer proxy resolving a 3D scalar field plus its cross-section and surface-mask geometry inputs |
| [ScalarField3DLayerTask](../src/app-logic/ScalarField3DLayerTask.md) | 3 | 518 | 2 | Layer task for 3D scalar field visualization via volume rendering |

#### Topology

| Unit | Tier | Lines | Fan-in | Description |
|---|---|---|---|---|
| [TopologyGeometryResolver](../src/app-logic/TopologyGeometryResolver.md) | 2 | 1128 | 17 | Resolves topological polygon/line properties into ResolvedTopologicalBoundary and ResolvedTopologicalLine geometries |
| [TopologyGeometryResolverLayerProxy](../src/app-logic/TopologyGeometryResolverLayerProxy.md) | 2 | 2257 | 59 | Layer proxy resolving topological line and boundary geometries and their velocities |
| [TopologyGeometryResolverLayerTask](../src/app-logic/TopologyGeometryResolverLayerTask.md) | 3 | 566 | 2 | Layer task that resolves topological boundaries and lines by walking section references |
| [TopologyGeometryType](../src/app-logic/TopologyGeometryType.md) | 2 | 56 | 142 | Enum distinguishing how a topological feature resolves: line, boundary or network |
| [TopologyInternalUtils](../src/app-logic/TopologyInternalUtils.md) | 2 | 1695 | 55 | Shared free-function toolbox for reading and writing raw topological GPML property values |
| [TopologyIntersections](../src/app-logic/TopologyIntersections.md) | 2 | 1347 | 37 | Computes where one topological section is cut by its two neighbouring sections |
| [TopologyNetworkLayerParams](../src/app-logic/TopologyNetworkLayerParams.md) | 2 | 129 | 9 | LayerParams holding one topological network layer's deformation settings |
| [TopologyNetworkParams](../src/app-logic/TopologyNetworkParams.md) | 2 | 522 | 122 | Value object holding strain-rate smoothing, clamping and rift parameters for a network |
| [TopologyNetworkResolver](../src/app-logic/TopologyNetworkResolver.md) | 3 | 1348 | 2 | Resolves topological network features at a reconstruction time, assembling boundary sections and interior geometries |
| [TopologyNetworkResolverLayerProxy](../src/app-logic/TopologyNetworkResolverLayerProxy.md) | 2 | 1712 | 12 | Layer proxy resolving topological network geometries and their velocities |
| [TopologyNetworkResolverLayerTask](../src/app-logic/TopologyNetworkResolverLayerTask.md) | 3 | 513 | 2 | Layer task orchestrating resolution of topological networks from feature collections |
| [TopologyPointLocation](../src/app-logic/TopologyPointLocation.md) | 2 | 269 | 59 | Compact record of where a point sits relative to resolved topologies at one time |
| [TopologyReconstruct](../src/app-logic/TopologyReconstruct.md) | 1 | 4375 | 161 | (pending) |
| [TopologyReconstructedFeatureGeometry](../src/app-logic/TopologyReconstructedFeatureGeometry.md) | 2 | 342 | 33 | Reconstructed feature geometry produced by the topology reconstruction pipeline, with per-point deformation |
| [TopologyUtils](../src/app-logic/TopologyUtils.md) | 2 | 2232 | 62 | Resolves topological lines, boundaries and networks, and de-duplicates their shared boundary sub-segments |

#### Velocity

| Unit | Tier | Lines | Fan-in | Description |
|---|---|---|---|---|
| [VelocityDeltaTime](../src/app-logic/VelocityDeltaTime.md) | 2 | 193 | 282 | Enum and helper turning a delta-time choice into the pair of times to reconstruct and difference |
| [VelocityFieldCalculatorLayerParams](../src/app-logic/VelocityFieldCalculatorLayerParams.md) | 2 | 160 | 9 | LayerParams holding the VelocityParams configuration for a velocity-field-calculator layer |
| [VelocityFieldCalculatorLayerProxy](../src/app-logic/VelocityFieldCalculatorLayerProxy.md) | 2 | 977 | 16 | Lazily computes and caches velocity fields at domain points, optionally on rigid or deforming surfaces |
| [VelocityFieldCalculatorLayerTask](../src/app-logic/VelocityFieldCalculatorLayerTask.md) | 3 | 476 | 2 | Layer task calculating velocity fields on mesh points inside static or dynamic polygons |
| [VelocityParams](../src/app-logic/VelocityParams.md) | 2 | 395 | 91 | Value type configuring how a velocity layer solves and smooths velocities |

#### Other

| Unit | Tier | Lines | Fan-in | Description |
|---|---|---|---|---|
| [AgeModelCollection](../src/app-logic/AgeModelCollection.md) | 2 | 333 | 123 | Named age models mapping magnetic chrons to ages, with one active model |
| [AppLogicUtils](../src/app-logic/AppLogicUtils.md) | 1 | 260 | 377 | (pending) |
| [ApplicationState](../src/app-logic/ApplicationState.md) | 1 | 1221 | 2130 | (pending) |
| [AssignPlateIds](../src/app-logic/AssignPlateIds.md) | 2 | 681 | 173 | Cookie-cuts features against partitioning polygons and assigns plate ids |
| [DeformationStrain](../src/app-logic/DeformationStrain.md) | 1 | 549 | 234 | (pending) |
| [DeformationStrainRate](../src/app-logic/DeformationStrainRate.md) | 2 | 358 | 91 | Instantaneous rate-of-deformation tensor and its scalar invariants |
| [DependentTopologicalSectionLayers](../src/app-logic/DependentTopologicalSectionLayers.md) | 2 | 456 | 124 | Tracks which section layers actually feed a resolved topology layer |
| [ExtractRasterFeatureProperties](../src/app-logic/ExtractRasterFeatureProperties.md) | 2 | 573 | 80 | Visitor that extracts georeferencing, SRS, proxied rasters and band names from a raster feature |
| [ExtractScalarField3DFeatureProperties](../src/app-logic/ExtractScalarField3DFeatureProperties.md) | 2 | 344 | 50 | Visitor that extracts the scalar field filename from a scalar field feature |
| [FeatureCollectionFileIO](../src/app-logic/FeatureCollectionFileIO.md) | 2 | 613 | 119 | Central entry point for loading, saving, reloading and unloading feature collection files |
| [FeatureCollectionFileState](../src/app-logic/FeatureCollectionFileState.md) | 1 | 1106 | 922 | (pending) |
| [FlowlineGeometryPopulator](../src/app-logic/FlowlineGeometryPopulator.md) | 2 | 649 | 5 | Feature visitor that reconstructs flowline features into ReconstructedFlowline geometries |
| [FlowlineUtils](../src/app-logic/FlowlineUtils.md) | 2 | 950 | 111 | Flowline feature detection, property extraction and half-stage rotation maths |
| [GPlatesQtMsgHandler](../src/app-logic/GPlatesQtMsgHandler.md) | 2 | 785 | 53 | Installs a Qt message handler and captures stdout/stderr into the log |
| [GenerateVelocityDomainCitcoms](../src/app-logic/GenerateVelocityDomainCitcoms.md) | 2 | 480 | 6 | Generates the 12-diamond CitcomS spherical velocity mesh |
| [GenerateVelocityDomainTerra](../src/app-logic/GenerateVelocityDomainTerra.md) | 2 | 412 | 34 | Generates the icosahedral Terra velocity mesh split by MPI processor |
| [GenericPartitionFeatureTask](../src/app-logic/GenericPartitionFeatureTask.md) | 3 | 348 | 1 | Partitions feature geometry by reconstructed plates and assigns plate IDs |
| [GeometryCookieCutter](../src/app-logic/GeometryCookieCutter.md) | 2 | 1150 | 83 | Partitions arbitrary geometry against a prioritised, sorted set of reconstructed plate polygons |
| [GeometryUtils](../src/app-logic/GeometryUtils.md) | 1 | 2011 | 431 | (pending) |
| [LogModel](../src/app-logic/LogModel.md) | 2 | 445 | 65 | Qt list model backing the log viewer, buffering and de-duplicating flooded messages |
| [LogToModelHandler](../src/app-logic/LogToModelHandler.md) | 3 | 121 | 1 | Routes Qt messages into the application's log model |
| [MotionPathGeometryPopulator](../src/app-logic/MotionPathGeometryPopulator.md) | 3 | 478 | 2 | Reconstructs motion path features by tracing seed point trajectories |
| [MotionPathUtils](../src/app-logic/MotionPathUtils.md) | 2 | 497 | 53 | Feature visitors and helpers for reconstructing gpml:MotionPath features into motion tracks |
| [MultiPointVectorField](../src/app-logic/MultiPointVectorField.md) | 1 | 529 | 911 | (pending) |
| [NetRotationUtils](../src/app-logic/NetRotationUtils.md) | 2 | 343 | 60 | Point-by-point net-rotation math: per-point contribution, plate-id accumulation, pole/xyz conversion |
| [PalaeomagUtils](../src/app-logic/PalaeomagUtils.md) | 2 | 219 | 12 | Feature visitor pulling site, pole, plate id and age off a VirtualGeomagneticPole feature |
| [PartitionFeatureTask](../src/app-logic/PartitionFeatureTask.md) | 2 | 170 | 13 | Strategy interface for assigning partitioning-polygon properties to a feature, plus its ordered pipeline |
| [PartitionFeatureUtils](../src/app-logic/PartitionFeatureUtils.md) | 1 | 2076 | 116 | (pending) |
| [PlateVelocityUtils](../src/app-logic/PlateVelocityUtils.md) | 2 | 1559 | 67 | Solves velocities over static polygons, topological boundaries and networks, plus basic velocity/stage-rotation math |
| [PropertyExtractors](../src/app-logic/PropertyExtractors.md) | 2 | 252 | 14 | Functors extracting plate id, age or feature type from a ReconstructionGeometry or feature, for colouring |
| [RotationUtils](../src/app-logic/RotationUtils.md) | 2 | 690 | 51 | Half-stage spreading rotations, stage poles between two trees, and short-path total-rotation adjustment |
| [SmallCircleGeometryPopulator](../src/app-logic/SmallCircleGeometryPopulator.md) | 3 | 301 | 1 | Feature visitor that creates reconstructed small circle geometries from SmallCircle features |
| [TRSUtils](../src/app-logic/TRSUtils.md) | 2 | 379 | 34 | Finds and summarises the plate IDs and pole samples of a Total Reconstruction Sequence feature |
| [TimeSpanUtils](../src/app-logic/TimeSpanUtils.md) | 1 | 1295 | 190 | (pending) |
| [UserPreferences](../src/app-logic/UserPreferences.md) | 1 | 993 | 231 | (pending) |
| [VgpPartitionFeatureTask](../src/app-logic/VgpPartitionFeatureTask.md) | 3 | 203 | 1 | Partitions VirtualGeomagneticPole features by assigning plate IDs from sample site locations |

### `src/app-logic/deprecated`

| Unit | Tier | Lines | Fan-in | Description |
|---|---|---|---|---|
| [PaleomagUtils](../src/app-logic/deprecated/PaleomagUtils.md) | 3 | 575 | 10 | Utilities for paleomagnetic data detection and rendering |
| [PaleomagWorkflow](../src/app-logic/deprecated/PaleomagWorkflow.md) | 3 | 465 | 0 | Workflow for managing paleomagnetic feature collections and rendering |
| [PlateVelocityWorkflow](../src/app-logic/deprecated/PlateVelocityWorkflow.md) | 3 | 438 | 0 | Workflow for managing plate velocity feature collections and calculations |
| [PropertyValuePropogator](../src/app-logic/deprecated/PropertyValuePropogator.md) | 3 | 511 | 0 | Assigns properties to features using cookie-cutter geometry with partitioning polygons |
| [ReconstructedFeatureGeometryPopulator](../src/app-logic/deprecated/ReconstructedFeatureGeometryPopulator.md) | 3 | 664 | 0 | Visitor that reconstructs feature geometries by applying plate circuit rotations at a specified reconstruction time |


## Other files

| File | Kind | Lines |
|---|---|---|
| `src/app-logic/CMakeLists.txt` | build | 277 |

## Depends on

| Component | References |
|---|---|
| [model](model.md) | 7608 |
| [maths](maths.md) | 4425 |
| [utils](utils.md) | 1374 |
| [global](global.md) | 1160 |
| [property-values](property-values.md) | 1059 |
| [scribe](scribe.md) | 270 |
| [file-io](file-io.md) | 182 |
| [opengl](opengl.md) | 177 |
| [gui](gui.md) | 150 |
| [feature-visitors](feature-visitors.md) | 108 |
| [data-mining](data-mining.md) | 71 |
| [view-operations](view-operations.md) | 58 |
| [qt-widgets](qt-widgets.md) | 53 |
| [presentation](presentation.md) | 25 |
| [unit-test](unit-test.md) | 10 |
| [api](api.md) | 4 |

## Used by

| Component | References |
|---|---|
| [qt-widgets](qt-widgets.md) | 4437 |
| [gui](gui.md) | 2834 |
| [presentation](presentation.md) | 2072 |
| [file-io](file-io.md) | 1115 |
| [opengl](opengl.md) | 616 |
| [view-operations](view-operations.md) | 609 |
| [data-mining](data-mining.md) | 428 |
| [feature-visitors](feature-visitors.md) | 182 |
| [cli](cli.md) | 153 |
| [entry-points](entry-points.md) | 152 |
| [canvas-tools](canvas-tools.md) | 140 |
| [api](api.md) | 120 |
| [model](model.md) | 22 |
| [unit-test](unit-test.md) | 20 |
| [maths](maths.md) | 7 |

## Explore

Run these from the `gplates-code` skill directory:

```bash
python scripts/gpq.py tree src/app-logic
python scripts/gpq.py sym . --mode sub --path src/app-logic --defs-only
```
