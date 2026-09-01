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
| [CoRegistrationData](../src/app-logic/CoRegistrationData.md) | 2 | 178 | 202 | (pending) |
| [CoRegistrationLayerParams](../src/app-logic/CoRegistrationLayerParams.md) | 2 | 161 | 38 | (pending) |
| [CoRegistrationLayerProxy](../src/app-logic/CoRegistrationLayerProxy.md) | 2 | 838 | 103 | (pending) |
| [CoRegistrationLayerTask](../src/app-logic/CoRegistrationLayerTask.md) | 2 | 415 | 13 | (pending) |

#### Layer

| Unit | Tier | Lines | Fan-in | Description |
|---|---|---|---|---|
| [Layer](../src/app-logic/Layer.md) | 1 | 1173 | 992 | (pending) |
| [LayerInputChannelName](../src/app-logic/LayerInputChannelName.md) | 1 | 156 | 734 | (pending) |
| [LayerInputChannelType](../src/app-logic/LayerInputChannelType.md) | 2 | 227 | 78 | (pending) |
| [LayerParams](../src/app-logic/LayerParams.md) | 1 | 99 | 1270 | (pending) |
| [LayerParamsVisitor](../src/app-logic/LayerParamsVisitor.md) | 2 | 134 | 158 | (pending) |
| [LayerProxy](../src/app-logic/LayerProxy.md) | 1 | 110 | 554 | (pending) |
| [LayerProxyUtils](../src/app-logic/LayerProxyUtils.md) | 1 | 1120 | 2552 | (pending) |
| [LayerProxyVisitor](../src/app-logic/LayerProxyVisitor.md) | 1 | 230 | 228 | (pending) |
| [LayerTask](../src/app-logic/LayerTask.md) | 2 | 199 | 15 | (pending) |
| [LayerTaskRegistry](../src/app-logic/LayerTaskRegistry.md) | 2 | 435 | 101 | (pending) |
| [LayerTaskType](../src/app-logic/LayerTaskType.md) | 2 | 129 | 219 | (pending) |

#### Raster

| Unit | Tier | Lines | Fan-in | Description |
|---|---|---|---|---|
| [RasterLayerParams](../src/app-logic/RasterLayerParams.md) | 2 | 387 | 50 | (pending) |
| [RasterLayerProxy](../src/app-logic/RasterLayerProxy.md) | 1 | 1762 | 349 | (pending) |
| [RasterLayerTask](../src/app-logic/RasterLayerTask.md) | 3 | 490 | 2 | (pending) |

#### Reconstruct

| Unit | Tier | Lines | Fan-in | Description |
|---|---|---|---|---|
| [ReconstructContext](../src/app-logic/ReconstructContext.md) | 1 | 1715 | 381 | (pending) |
| [ReconstructGraph](../src/app-logic/ReconstructGraph.md) | 1 | 1766 | 118 | (pending) |
| [ReconstructGraphImpl](../src/app-logic/ReconstructGraphImpl.md) | 2 | 1064 | 43 | (pending) |
| [ReconstructHandle](../src/app-logic/ReconstructHandle.md) | 1 | 79 | 761 | (pending) |
| [ReconstructLayerParams](../src/app-logic/ReconstructLayerParams.md) | 2 | 196 | 13 | (pending) |
| [ReconstructLayerProxy](../src/app-logic/ReconstructLayerProxy.md) | 1 | 2795 | 285 | (pending) |
| [ReconstructLayerTask](../src/app-logic/ReconstructLayerTask.md) | 3 | 590 | 2 | (pending) |
| [ReconstructMethodByPlateId](../src/app-logic/ReconstructMethodByPlateId.md) | 2 | 974 | 35 | (pending) |
| [ReconstructMethodFiniteRotation](../src/app-logic/ReconstructMethodFiniteRotation.md) | 1 | 158 | 459 | (pending) |
| [ReconstructMethodFlowline](../src/app-logic/ReconstructMethodFlowline.md) | 3 | 445 | 2 | (pending) |
| [ReconstructMethodHalfStageRotation](../src/app-logic/ReconstructMethodHalfStageRotation.md) | 3 | 838 | 2 | (pending) |
| [ReconstructMethodInterface](../src/app-logic/ReconstructMethodInterface.md) | 1 | 480 | 396 | (pending) |
| [ReconstructMethodMotionPath](../src/app-logic/ReconstructMethodMotionPath.md) | 3 | 299 | 2 | (pending) |
| [ReconstructMethodRegistry](../src/app-logic/ReconstructMethodRegistry.md) | 2 | 578 | 16 | (pending) |
| [ReconstructMethodSmallCircle](../src/app-logic/ReconstructMethodSmallCircle.md) | 3 | 338 | 2 | (pending) |
| [ReconstructMethodType](../src/app-logic/ReconstructMethodType.md) | 2 | 58 | 385 | (pending) |
| [ReconstructMethodVirtualGeomagneticPole](../src/app-logic/ReconstructMethodVirtualGeomagneticPole.md) | 3 | 562 | 2 | (pending) |
| [ReconstructParams](../src/app-logic/ReconstructParams.md) | 2 | 624 | 102 | (pending) |
| [ReconstructScalarCoverageLayerParams](../src/app-logic/ReconstructScalarCoverageLayerParams.md) | 2 | 543 | 15 | (pending) |
| [ReconstructScalarCoverageLayerProxy](../src/app-logic/ReconstructScalarCoverageLayerProxy.md) | 2 | 1416 | 23 | (pending) |
| [ReconstructScalarCoverageLayerTask](../src/app-logic/ReconstructScalarCoverageLayerTask.md) | 3 | 359 | 2 | (pending) |
| [ReconstructScalarCoverageParams](../src/app-logic/ReconstructScalarCoverageParams.md) | 2 | 126 | 23 | (pending) |
| [ReconstructUtils](../src/app-logic/ReconstructUtils.md) | 2 | 870 | 43 | (pending) |

#### Reconstructed

| Unit | Tier | Lines | Fan-in | Description |
|---|---|---|---|---|
| [ReconstructedFeatureGeometry](../src/app-logic/ReconstructedFeatureGeometry.md) | 1 | 680 | 1116 | (pending) |
| [ReconstructedFeatureGeometryFinder](../src/app-logic/ReconstructedFeatureGeometryFinder.md) | 2 | 350 | 10 | (pending) |
| [ReconstructedFlowline](../src/app-logic/ReconstructedFlowline.md) | 2 | 283 | 28 | (pending) |
| [ReconstructedMotionPath](../src/app-logic/ReconstructedMotionPath.md) | 2 | 259 | 20 | (pending) |
| [ReconstructedScalarCoverage](../src/app-logic/ReconstructedScalarCoverage.md) | 2 | 419 | 55 | (pending) |
| [ReconstructedSmallCircle](../src/app-logic/ReconstructedSmallCircle.md) | 2 | 215 | 10 | (pending) |
| [ReconstructedVirtualGeomagneticPole](../src/app-logic/ReconstructedVirtualGeomagneticPole.md) | 2 | 242 | 32 | (pending) |

#### Reconstruction

| Unit | Tier | Lines | Fan-in | Description |
|---|---|---|---|---|
| [Reconstruction](../src/app-logic/Reconstruction.md) | 2 | 358 | 67 | (pending) |
| [ReconstructionFeatureProperties](../src/app-logic/ReconstructionFeatureProperties.md) | 2 | 399 | 93 | (pending) |
| [ReconstructionGeometry](../src/app-logic/ReconstructionGeometry.md) | 1 | 159 | 808 | (pending) |
| [ReconstructionGeometryFinder](../src/app-logic/ReconstructionGeometryFinder.md) | 2 | 353 | 26 | (pending) |
| [ReconstructionGeometryUtils](../src/app-logic/ReconstructionGeometryUtils.md) | 1 | 1766 | 280 | (pending) |
| [ReconstructionGeometryVisitor](../src/app-logic/ReconstructionGeometryVisitor.md) | 1 | 437 | 460 | (pending) |
| [ReconstructionGraph](../src/app-logic/ReconstructionGraph.md) | 1 | 362 | 279 | (pending) |
| [ReconstructionGraphBuilder](../src/app-logic/ReconstructionGraphBuilder.md) | 2 | 370 | 19 | (pending) |
| [ReconstructionGraphPopulator](../src/app-logic/ReconstructionGraphPopulator.md) | 2 | 417 | 4 | (pending) |
| [ReconstructionLayerParams](../src/app-logic/ReconstructionLayerParams.md) | 3 | 124 | 4 | (pending) |
| [ReconstructionLayerProxy](../src/app-logic/ReconstructionLayerProxy.md) | 2 | 629 | 52 | (pending) |
| [ReconstructionLayerTask](../src/app-logic/ReconstructionLayerTask.md) | 3 | 300 | 2 | (pending) |
| [ReconstructionParams](../src/app-logic/ReconstructionParams.md) | 2 | 171 | 16 | (pending) |
| [ReconstructionTree](../src/app-logic/ReconstructionTree.md) | 1 | 919 | 339 | (pending) |
| [ReconstructionTreeCreator](../src/app-logic/ReconstructionTreeCreator.md) | 1 | 800 | 157 | (pending) |

#### Resolved

| Unit | Tier | Lines | Fan-in | Description |
|---|---|---|---|---|
| [ResolvedRaster](../src/app-logic/ResolvedRaster.md) | 2 | 265 | 96 | (pending) |
| [ResolvedScalarField3D](../src/app-logic/ResolvedScalarField3D.md) | 2 | 215 | 13 | (pending) |
| [ResolvedSubSegmentRangeInSection](../src/app-logic/ResolvedSubSegmentRangeInSection.md) | 1 | 1495 | 519 | (pending) |
| [ResolvedTopologicalBoundary](../src/app-logic/ResolvedTopologicalBoundary.md) | 2 | 338 | 18 | (pending) |
| [ResolvedTopologicalGeometry](../src/app-logic/ResolvedTopologicalGeometry.md) | 2 | 317 | 5 | (pending) |
| [ResolvedTopologicalGeometrySubSegment](../src/app-logic/ResolvedTopologicalGeometrySubSegment.md) | 2 | 456 | 132 | (pending) |
| [ResolvedTopologicalLine](../src/app-logic/ResolvedTopologicalLine.md) | 2 | 336 | 19 | (pending) |
| [ResolvedTopologicalNetwork](../src/app-logic/ResolvedTopologicalNetwork.md) | 2 | 514 | 14 | (pending) |
| [ResolvedTopologicalSection](../src/app-logic/ResolvedTopologicalSection.md) | 2 | 133 | 28 | (pending) |
| [ResolvedTopologicalSharedSubSegment](../src/app-logic/ResolvedTopologicalSharedSubSegment.md) | 2 | 482 | 52 | (pending) |
| [ResolvedTopologicalSubSegmentImpl](../src/app-logic/ResolvedTopologicalSubSegmentImpl.md) | 2 | 1147 | 10 | (pending) |
| [ResolvedTriangulationDelaunay2](../src/app-logic/ResolvedTriangulationDelaunay2.md) | 1 | 1498 | 632 | (pending) |
| [ResolvedTriangulationNetwork](../src/app-logic/ResolvedTriangulationNetwork.md) | 1 | 3626 | 112 | (pending) |
| [ResolvedTriangulationUtils](../src/app-logic/ResolvedTriangulationUtils.md) | 2 | 296 | 38 | (pending) |
| [ResolvedVertexSourceInfo](../src/app-logic/ResolvedVertexSourceInfo.md) | 1 | 845 | 165 | (pending) |

#### Scalar

| Unit | Tier | Lines | Fan-in | Description |
|---|---|---|---|---|
| [ScalarCoverageEvolution](../src/app-logic/ScalarCoverageEvolution.md) | 2 | 2130 | 52 | (pending) |
| [ScalarCoverageFeatureProperties](../src/app-logic/ScalarCoverageFeatureProperties.md) | 2 | 635 | 83 | (pending) |
| [ScalarCoverageTimeSpan](../src/app-logic/ScalarCoverageTimeSpan.md) | 2 | 752 | 8 | (pending) |
| [ScalarField3DLayerParams](../src/app-logic/ScalarField3DLayerParams.md) | 2 | 346 | 44 | (pending) |
| [ScalarField3DLayerProxy](../src/app-logic/ScalarField3DLayerProxy.md) | 2 | 1281 | 34 | (pending) |
| [ScalarField3DLayerTask](../src/app-logic/ScalarField3DLayerTask.md) | 3 | 518 | 2 | (pending) |

#### Topology

| Unit | Tier | Lines | Fan-in | Description |
|---|---|---|---|---|
| [TopologyGeometryResolver](../src/app-logic/TopologyGeometryResolver.md) | 2 | 1128 | 17 | (pending) |
| [TopologyGeometryResolverLayerProxy](../src/app-logic/TopologyGeometryResolverLayerProxy.md) | 2 | 2257 | 59 | (pending) |
| [TopologyGeometryResolverLayerTask](../src/app-logic/TopologyGeometryResolverLayerTask.md) | 3 | 566 | 2 | (pending) |
| [TopologyGeometryType](../src/app-logic/TopologyGeometryType.md) | 2 | 56 | 142 | (pending) |
| [TopologyInternalUtils](../src/app-logic/TopologyInternalUtils.md) | 2 | 1695 | 55 | (pending) |
| [TopologyIntersections](../src/app-logic/TopologyIntersections.md) | 2 | 1347 | 37 | (pending) |
| [TopologyNetworkLayerParams](../src/app-logic/TopologyNetworkLayerParams.md) | 2 | 129 | 9 | (pending) |
| [TopologyNetworkParams](../src/app-logic/TopologyNetworkParams.md) | 2 | 522 | 122 | (pending) |
| [TopologyNetworkResolver](../src/app-logic/TopologyNetworkResolver.md) | 3 | 1348 | 2 | (pending) |
| [TopologyNetworkResolverLayerProxy](../src/app-logic/TopologyNetworkResolverLayerProxy.md) | 2 | 1712 | 12 | (pending) |
| [TopologyNetworkResolverLayerTask](../src/app-logic/TopologyNetworkResolverLayerTask.md) | 3 | 513 | 2 | (pending) |
| [TopologyPointLocation](../src/app-logic/TopologyPointLocation.md) | 2 | 269 | 59 | (pending) |
| [TopologyReconstruct](../src/app-logic/TopologyReconstruct.md) | 1 | 4375 | 161 | (pending) |
| [TopologyReconstructedFeatureGeometry](../src/app-logic/TopologyReconstructedFeatureGeometry.md) | 2 | 342 | 33 | (pending) |
| [TopologyUtils](../src/app-logic/TopologyUtils.md) | 2 | 2232 | 62 | (pending) |

#### Velocity

| Unit | Tier | Lines | Fan-in | Description |
|---|---|---|---|---|
| [VelocityDeltaTime](../src/app-logic/VelocityDeltaTime.md) | 2 | 193 | 282 | (pending) |
| [VelocityFieldCalculatorLayerParams](../src/app-logic/VelocityFieldCalculatorLayerParams.md) | 2 | 160 | 9 | (pending) |
| [VelocityFieldCalculatorLayerProxy](../src/app-logic/VelocityFieldCalculatorLayerProxy.md) | 2 | 977 | 16 | (pending) |
| [VelocityFieldCalculatorLayerTask](../src/app-logic/VelocityFieldCalculatorLayerTask.md) | 3 | 476 | 2 | (pending) |
| [VelocityParams](../src/app-logic/VelocityParams.md) | 2 | 395 | 91 | (pending) |

#### Other

| Unit | Tier | Lines | Fan-in | Description |
|---|---|---|---|---|
| [AgeModelCollection](../src/app-logic/AgeModelCollection.md) | 2 | 333 | 123 | (pending) |
| [AppLogicUtils](../src/app-logic/AppLogicUtils.md) | 1 | 260 | 377 | (pending) |
| [ApplicationState](../src/app-logic/ApplicationState.md) | 1 | 1221 | 2130 | (pending) |
| [AssignPlateIds](../src/app-logic/AssignPlateIds.md) | 2 | 681 | 173 | (pending) |
| [DeformationStrain](../src/app-logic/DeformationStrain.md) | 1 | 549 | 234 | (pending) |
| [DeformationStrainRate](../src/app-logic/DeformationStrainRate.md) | 2 | 358 | 91 | (pending) |
| [DependentTopologicalSectionLayers](../src/app-logic/DependentTopologicalSectionLayers.md) | 2 | 456 | 124 | (pending) |
| [ExtractRasterFeatureProperties](../src/app-logic/ExtractRasterFeatureProperties.md) | 2 | 573 | 80 | (pending) |
| [ExtractScalarField3DFeatureProperties](../src/app-logic/ExtractScalarField3DFeatureProperties.md) | 2 | 344 | 50 | (pending) |
| [FeatureCollectionFileIO](../src/app-logic/FeatureCollectionFileIO.md) | 2 | 613 | 119 | (pending) |
| [FeatureCollectionFileState](../src/app-logic/FeatureCollectionFileState.md) | 1 | 1106 | 922 | (pending) |
| [FlowlineGeometryPopulator](../src/app-logic/FlowlineGeometryPopulator.md) | 2 | 649 | 5 | (pending) |
| [FlowlineUtils](../src/app-logic/FlowlineUtils.md) | 2 | 950 | 111 | (pending) |
| [GPlatesQtMsgHandler](../src/app-logic/GPlatesQtMsgHandler.md) | 2 | 785 | 53 | (pending) |
| [GenerateVelocityDomainCitcoms](../src/app-logic/GenerateVelocityDomainCitcoms.md) | 2 | 480 | 6 | (pending) |
| [GenerateVelocityDomainTerra](../src/app-logic/GenerateVelocityDomainTerra.md) | 2 | 412 | 34 | (pending) |
| [GenericPartitionFeatureTask](../src/app-logic/GenericPartitionFeatureTask.md) | 3 | 348 | 1 | (pending) |
| [GeometryCookieCutter](../src/app-logic/GeometryCookieCutter.md) | 2 | 1150 | 83 | (pending) |
| [GeometryUtils](../src/app-logic/GeometryUtils.md) | 1 | 2011 | 431 | (pending) |
| [LogModel](../src/app-logic/LogModel.md) | 2 | 445 | 65 | (pending) |
| [LogToModelHandler](../src/app-logic/LogToModelHandler.md) | 3 | 121 | 1 | (pending) |
| [MotionPathGeometryPopulator](../src/app-logic/MotionPathGeometryPopulator.md) | 3 | 478 | 2 | (pending) |
| [MotionPathUtils](../src/app-logic/MotionPathUtils.md) | 2 | 497 | 53 | (pending) |
| [MultiPointVectorField](../src/app-logic/MultiPointVectorField.md) | 1 | 529 | 911 | (pending) |
| [NetRotationUtils](../src/app-logic/NetRotationUtils.md) | 2 | 343 | 60 | (pending) |
| [PalaeomagUtils](../src/app-logic/PalaeomagUtils.md) | 2 | 219 | 12 | (pending) |
| [PartitionFeatureTask](../src/app-logic/PartitionFeatureTask.md) | 2 | 170 | 13 | (pending) |
| [PartitionFeatureUtils](../src/app-logic/PartitionFeatureUtils.md) | 1 | 2076 | 116 | (pending) |
| [PlateVelocityUtils](../src/app-logic/PlateVelocityUtils.md) | 2 | 1559 | 67 | (pending) |
| [PropertyExtractors](../src/app-logic/PropertyExtractors.md) | 2 | 252 | 14 | (pending) |
| [RotationUtils](../src/app-logic/RotationUtils.md) | 2 | 690 | 51 | (pending) |
| [SmallCircleGeometryPopulator](../src/app-logic/SmallCircleGeometryPopulator.md) | 3 | 301 | 1 | (pending) |
| [TRSUtils](../src/app-logic/TRSUtils.md) | 2 | 379 | 34 | (pending) |
| [TimeSpanUtils](../src/app-logic/TimeSpanUtils.md) | 1 | 1295 | 190 | (pending) |
| [UserPreferences](../src/app-logic/UserPreferences.md) | 1 | 993 | 231 | (pending) |
| [VgpPartitionFeatureTask](../src/app-logic/VgpPartitionFeatureTask.md) | 3 | 203 | 1 | (pending) |

### `src/app-logic/deprecated`

| Unit | Tier | Lines | Fan-in | Description |
|---|---|---|---|---|
| [PaleomagUtils](../src/app-logic/deprecated/PaleomagUtils.md) | 3 | 575 | 10 | (pending) |
| [PaleomagWorkflow](../src/app-logic/deprecated/PaleomagWorkflow.md) | 3 | 465 | 0 | (pending) |
| [PlateVelocityWorkflow](../src/app-logic/deprecated/PlateVelocityWorkflow.md) | 3 | 438 | 0 | (pending) |
| [PropertyValuePropogator](../src/app-logic/deprecated/PropertyValuePropogator.md) | 3 | 511 | 0 | (pending) |
| [ReconstructedFeatureGeometryPopulator](../src/app-logic/deprecated/ReconstructedFeatureGeometryPopulator.md) | 3 | 664 | 0 | (pending) |


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
