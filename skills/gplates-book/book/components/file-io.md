# file-io

[Book TOC](../TOC.md)

137 unit page(s), 247 source file(s) documented here, 3 further file(s) listed below.

## Overview

[[[PROSE component unit=component:file-io tier=1]]]
Replace this whole block, markers included, with 2-4 paragraphs: what this component is responsible for, the load-bearing units and how it connects to neighbouring components. Do not restate the unit table.
[[[/PROSE]]]

## Units

### `src/file-io`

#### Arbitrary

| Unit | Tier | Lines | Fan-in | Description |
|---|---|---|---|---|
| [ArbitraryNodeProcessor](../src/file-io/ArbitraryNodeProcessor.md) | 3 | 55 | 14 | (pending) |
| [ArbitraryXmlProfile](../src/file-io/ArbitraryXmlProfile.md) | 2 | 67 | 35 | (pending) |
| [ArbitraryXmlReader](../src/file-io/ArbitraryXmlReader.md) | 2 | 233 | 25 | (pending) |

#### Citcoms

| Unit | Tier | Lines | Fan-in | Description |
|---|---|---|---|---|
| [CitcomsFormatVelocityVectorFieldExport](../src/file-io/CitcomsFormatVelocityVectorFieldExport.md) | 3 | 383 | 2 | (pending) |
| [CitcomsGMTFormatResolvedTopologicalBoundaryExport](../src/file-io/CitcomsGMTFormatResolvedTopologicalBoundaryExport.md) | 2 | 1029 | 42 | (pending) |
| [CitcomsResolvedTopologicalBoundaryExport](../src/file-io/CitcomsResolvedTopologicalBoundaryExport.md) | 2 | 2016 | 138 | (pending) |
| [CitcomsResolvedTopologicalBoundaryExportImpl](../src/file-io/CitcomsResolvedTopologicalBoundaryExportImpl.md) | 2 | 617 | 292 | (pending) |

#### Error

| Unit | Tier | Lines | Fan-in | Description |
|---|---|---|---|---|
| [ErrorOpeningFileForReadingException](../src/file-io/ErrorOpeningFileForReadingException.md) | 2 | 127 | 534 | (pending) |
| [ErrorOpeningFileForWritingException](../src/file-io/ErrorOpeningFileForWritingException.md) | 2 | 125 | 242 | (pending) |
| [ErrorOpeningPipeFromGzipException](../src/file-io/ErrorOpeningPipeFromGzipException.md) | 3 | 142 | 2 | (pending) |
| [ErrorOpeningPipeToGzipException](../src/file-io/ErrorOpeningPipeToGzipException.md) | 3 | 142 | 1 | (pending) |
| [ErrorWritingFeatureCollectionToFileFormatException](../src/file-io/ErrorWritingFeatureCollectionToFileFormatException.md) | 3 | 94 | 2 | (pending) |

#### Export

| Unit | Tier | Lines | Fan-in | Description |
|---|---|---|---|---|
| [ExportTemplateFilenameSequence](../src/file-io/ExportTemplateFilenameSequence.md) | 2 | 540 | 241 | (pending) |
| [ExportTemplateFilenameSequenceFormats](../src/file-io/ExportTemplateFilenameSequenceFormats.md) | 2 | 836 | 32 | (pending) |
| [ExportTemplateFilenameSequenceImpl](../src/file-io/ExportTemplateFilenameSequenceImpl.md) | 3 | 809 | 1 | (pending) |

#### Feature

| Unit | Tier | Lines | Fan-in | Description |
|---|---|---|---|---|
| [FeatureCollectionFileFormat](../src/file-io/FeatureCollectionFileFormat.md) | 2 | 59 | 428 | (pending) |
| [FeatureCollectionFileFormatClassify](../src/file-io/FeatureCollectionFileFormatClassify.md) | 2 | 426 | 46 | (pending) |
| [FeatureCollectionFileFormatConfiguration](../src/file-io/FeatureCollectionFileFormatConfiguration.md) | 2 | 167 | 314 | (pending) |
| [FeatureCollectionFileFormatConfigurations](../src/file-io/FeatureCollectionFileFormatConfigurations.md) | 2 | 270 | 117 | (pending) |
| [FeatureCollectionFileFormatRegistry](../src/file-io/FeatureCollectionFileFormatRegistry.md) | 2 | 1336 | 149 | (pending) |

#### File

| Unit | Tier | Lines | Fan-in | Description |
|---|---|---|---|---|
| [File](../src/file-io/File.md) | 1 | 357 | 970 | (pending) |
| [FileFormatNotSupportedException](../src/file-io/FileFormatNotSupportedException.md) | 2 | 73 | 41 | (pending) |
| [FileInfo](../src/file-io/FileInfo.md) | 2 | 274 | 76 | (pending) |
| [FileLoadAbortedException](../src/file-io/FileLoadAbortedException.md) | 3 | 90 | 2 | (pending) |

#### G

| Unit | Tier | Lines | Fan-in | Description |
|---|---|---|---|---|
| [GMTFormatDeformationExport](../src/file-io/GMTFormatDeformationExport.md) | 3 | 713 | 6 | (pending) |
| [GMTFormatFlowlineExport](../src/file-io/GMTFormatFlowlineExport.md) | 3 | 469 | 6 | (pending) |
| [GMTFormatGeometryExporter](../src/file-io/GMTFormatGeometryExporter.md) | 2 | 367 | 23 | (pending) |
| [GMTFormatHeader](../src/file-io/GMTFormatHeader.md) | 2 | 1302 | 79 | (pending) |
| [GMTFormatMotionPathExport](../src/file-io/GMTFormatMotionPathExport.md) | 3 | 437 | 6 | (pending) |
| [GMTFormatMultiPointVectorFieldExport](../src/file-io/GMTFormatMultiPointVectorFieldExport.md) | 3 | 522 | 7 | (pending) |
| [GMTFormatReconstructedFeatureGeometryExport](../src/file-io/GMTFormatReconstructedFeatureGeometryExport.md) | 3 | 257 | 5 | (pending) |
| [GMTFormatReconstructedScalarCoverageExport](../src/file-io/GMTFormatReconstructedScalarCoverageExport.md) | 3 | 608 | 6 | (pending) |
| [GMTFormatResolvedTopologicalGeometryExport](../src/file-io/GMTFormatResolvedTopologicalGeometryExport.md) | 3 | 405 | 2 | (pending) |
| [GMTFormatWriter](../src/file-io/GMTFormatWriter.md) | 2 | 396 | 29 | (pending) |

#### Gdal

| Unit | Tier | Lines | Fan-in | Description |
|---|---|---|---|---|
| [Gdal](../src/file-io/Gdal.md) | 3 | 40 | 0 | (pending) |
| [GdalRasterReader](../src/file-io/GdalRasterReader.md) | 2 | 2815 | 5 | (pending) |
| [GdalRasterWriter](../src/file-io/GdalRasterWriter.md) | 2 | 1367 | 29 | (pending) |
| [GdalUtils](../src/file-io/GdalUtils.md) | 2 | 593 | 88 | (pending) |

#### GpmlFeature

| Unit | Tier | Lines | Fan-in | Description |
|---|---|---|---|---|
| [GpmlFeatureReaderFactory](../src/file-io/GpmlFeatureReaderFactory.md) | 3 | 962 | 4 | (pending) |
| [GpmlFeatureReaderImpl](../src/file-io/GpmlFeatureReaderImpl.md) | 1 | 822 | 330 | (pending) |
| [GpmlFeatureReaderInterface](../src/file-io/GpmlFeatureReaderInterface.md) | 3 | 134 | 4 | (pending) |

#### GpmlFormat

| Unit | Tier | Lines | Fan-in | Description |
|---|---|---|---|---|
| [GpmlFormatDeformationExport](../src/file-io/GpmlFormatDeformationExport.md) | 3 | 508 | 2 | (pending) |
| [GpmlFormatMultiPointVectorFieldExport](../src/file-io/GpmlFormatMultiPointVectorFieldExport.md) | 3 | 438 | 6 | (pending) |
| [GpmlFormatReconstructedScalarCoverageExport](../src/file-io/GpmlFormatReconstructedScalarCoverageExport.md) | 3 | 464 | 5 | (pending) |

#### GpmlProperty

| Unit | Tier | Lines | Fan-in | Description |
|---|---|---|---|---|
| [GpmlPropertyReader](../src/file-io/GpmlPropertyReader.md) | 2 | 1076 | 23 | (pending) |
| [GpmlPropertyStructuralTypeReader](../src/file-io/GpmlPropertyStructuralTypeReader.md) | 1 | 529 | 1813 | (pending) |
| [GpmlPropertyStructuralTypeReaderUtils](../src/file-io/GpmlPropertyStructuralTypeReaderUtils.md) | 2 | 1641 | 131 | (pending) |

#### GpmlReader

| Unit | Tier | Lines | Fan-in | Description |
|---|---|---|---|---|
| [GpmlReader](../src/file-io/GpmlReader.md) | 3 | 507 | 4 | (pending) |
| [GpmlReaderException](../src/file-io/GpmlReaderException.md) | 2 | 94 | 68 | (pending) |
| [GpmlReaderUtils](../src/file-io/GpmlReaderUtils.md) | 2 | 266 | 69 | (pending) |

#### Gsml

| Unit | Tier | Lines | Fan-in | Description |
|---|---|---|---|---|
| [GsmlConst](../src/file-io/GsmlConst.md) | 3 | 70 | 19 | (pending) |
| [GsmlFeatureHandlers](../src/file-io/GsmlFeatureHandlers.md) | 3 | 241 | 6 | (pending) |
| [GsmlFeaturesDef](../src/file-io/GsmlFeaturesDef.md) | 3 | 133 | 15 | (pending) |
| [GsmlNodeProcessor](../src/file-io/GsmlNodeProcessor.md) | 3 | 133 | 7 | (pending) |
| [GsmlNodeProcessorFactory](../src/file-io/GsmlNodeProcessorFactory.md) | 3 | 206 | 8 | (pending) |
| [GsmlPropertyDef](../src/file-io/GsmlPropertyDef.md) | 2 | 144 | 37 | (pending) |
| [GsmlPropertyHandlers](../src/file-io/GsmlPropertyHandlers.md) | 2 | 824 | 23 | (pending) |

#### Ogr

| Unit | Tier | Lines | Fan-in | Description |
|---|---|---|---|---|
| [Ogr](../src/file-io/Ogr.md) | 3 | 35 | 0 | (pending) |
| [OgrException](../src/file-io/OgrException.md) | 3 | 76 | 15 | (pending) |
| [OgrFeatureCollectionWriter](../src/file-io/OgrFeatureCollectionWriter.md) | 3 | 1989 | 1 | (pending) |
| [OgrFormatFlowlineExport](../src/file-io/OgrFormatFlowlineExport.md) | 3 | 326 | 2 | (pending) |
| [OgrFormatMotionPathExport](../src/file-io/OgrFormatMotionPathExport.md) | 3 | 301 | 2 | (pending) |
| [OgrFormatReconstructedFeatureGeometryExport](../src/file-io/OgrFormatReconstructedFeatureGeometryExport.md) | 3 | 437 | 3 | (pending) |
| [OgrFormatResolvedTopologicalGeometryExport](../src/file-io/OgrFormatResolvedTopologicalGeometryExport.md) | 3 | 638 | 6 | (pending) |
| [OgrGeometryExporter](../src/file-io/OgrGeometryExporter.md) | 2 | 373 | 12 | (pending) |
| [OgrReader](../src/file-io/OgrReader.md) | 2 | 2799 | 7 | (pending) |
| [OgrUtils](../src/file-io/OgrUtils.md) | 2 | 1358 | 94 | (pending) |
| [OgrWriter](../src/file-io/OgrWriter.md) | 2 | 1596 | 21 | (pending) |

#### Plates

| Unit | Tier | Lines | Fan-in | Description |
|---|---|---|---|---|
| [PlatesFormatUtils](../src/file-io/PlatesFormatUtils.md) | 3 | 698 | 12 | (pending) |
| [PlatesLineFormatGeometryExporter](../src/file-io/PlatesLineFormatGeometryExporter.md) | 3 | 450 | 4 | (pending) |
| [PlatesLineFormatHeaderVisitor](../src/file-io/PlatesLineFormatHeaderVisitor.md) | 2 | 539 | 70 | (pending) |
| [PlatesLineFormatReader](../src/file-io/PlatesLineFormatReader.md) | 3 | 2259 | 1 | (pending) |
| [PlatesLineFormatWriter](../src/file-io/PlatesLineFormatWriter.md) | 3 | 485 | 1 | (pending) |
| [PlatesRotationFileProxy](../src/file-io/PlatesRotationFileProxy.md) | 1 | 2927 | 191 | (pending) |
| [PlatesRotationFormatReader](../src/file-io/PlatesRotationFormatReader.md) | 3 | 930 | 1 | (pending) |
| [PlatesRotationFormatWriter](../src/file-io/PlatesRotationFormatWriter.md) | 2 | 675 | 96 | (pending) |

#### Raster

| Unit | Tier | Lines | Fan-in | Description |
|---|---|---|---|---|
| [RasterBandReader](../src/file-io/RasterBandReader.md) | 2 | 207 | 331 | (pending) |
| [RasterBandReaderHandle](../src/file-io/RasterBandReaderHandle.md) | 2 | 145 | 17 | (pending) |
| [RasterFileCache](../src/file-io/RasterFileCache.md) | 3 | 377 | 4 | (pending) |
| [RasterFileCacheFormat](../src/file-io/RasterFileCacheFormat.md) | 1 | 881 | 537 | (pending) |
| [RasterFileCacheFormatReader](../src/file-io/RasterFileCacheFormatReader.md) | 3 | 516 | 6 | (pending) |
| [RasterReader](../src/file-io/RasterReader.md) | 2 | 899 | 192 | (pending) |
| [RasterWriter](../src/file-io/RasterWriter.md) | 2 | 680 | 123 | (pending) |

#### Read

| Unit | Tier | Lines | Fan-in | Description |
|---|---|---|---|---|
| [ReadErrorAccumulation](../src/file-io/ReadErrorAccumulation.md) | 1 | 154 | 731 | (pending) |
| [ReadErrorMessages](../src/file-io/ReadErrorMessages.md) | 2 | 784 | 12 | (pending) |
| [ReadErrorOccurrence](../src/file-io/ReadErrorOccurrence.md) | 1 | 395 | 285 | (pending) |
| [ReadErrorUtils](../src/file-io/ReadErrorUtils.md) | 2 | 217 | 44 | (pending) |
| [ReadErrors](../src/file-io/ReadErrors.md) | 1 | 309 | 1358 | (pending) |

#### Reconstructed

| Unit | Tier | Lines | Fan-in | Description |
|---|---|---|---|---|
| [ReconstructedFeatureGeometryExport](../src/file-io/ReconstructedFeatureGeometryExport.md) | 2 | 392 | 29 | (pending) |
| [ReconstructedFlowlineExport](../src/file-io/ReconstructedFlowlineExport.md) | 3 | 368 | 3 | (pending) |
| [ReconstructedMotionPathExport](../src/file-io/ReconstructedMotionPathExport.md) | 3 | 367 | 3 | (pending) |
| [ReconstructedScalarCoverageExport](../src/file-io/ReconstructedScalarCoverageExport.md) | 3 | 361 | 10 | (pending) |

#### Other

| Unit | Tier | Lines | Fan-in | Description |
|---|---|---|---|---|
| [AgeModelReader](../src/file-io/AgeModelReader.md) | 3 | 231 | 2 | (pending) |
| [CptReader](../src/file-io/CptReader.md) | 1 | 2623 | 156 | (pending) |
| [DeformationExport](../src/file-io/DeformationExport.md) | 2 | 482 | 171 | (pending) |
| [GeometryExporter](../src/file-io/GeometryExporter.md) | 2 | 56 | 19 | (pending) |
| [GeoscimlProfile](../src/file-io/GeoscimlProfile.md) | 3 | 244 | 3 | (pending) |
| [GmapReader](../src/file-io/GmapReader.md) | 2 | 603 | 28 | (pending) |
| [GpmlOutputVisitor](../src/file-io/GpmlOutputVisitor.md) | 2 | 2166 | 115 | (pending) |
| [GpmlStructuralTypeReaderUtils](../src/file-io/GpmlStructuralTypeReaderUtils.md) | 2 | 2531 | 171 | (pending) |
| [GpmlUpgradeReaderUtils](../src/file-io/GpmlUpgradeReaderUtils.md) | 2 | 1459 | 25 | (pending) |
| [GzipFile](../src/file-io/GzipFile.md) | 2 | 726 | 11 | (pending) |
| [HellingerReader](../src/file-io/HellingerReader.md) | 2 | 1094 | 16 | (pending) |
| [HellingerWriter](../src/file-io/HellingerWriter.md) | 2 | 294 | 137 | (pending) |
| [LineReader](../src/file-io/LineReader.md) | 2 | 221 | 27 | (pending) |
| [LogToFileHandler](../src/file-io/LogToFileHandler.md) | 3 | 324 | 1 | (pending) |
| [MipmappedRasterFormatReader](../src/file-io/MipmappedRasterFormatReader.md) | 2 | 490 | 39 | (pending) |
| [MipmappedRasterFormatWriter](../src/file-io/MipmappedRasterFormatWriter.md) | 2 | 1380 | 3 | (pending) |
| [MultiPointVectorFieldExport](../src/file-io/MultiPointVectorFieldExport.md) | 2 | 741 | 67 | (pending) |
| [Proj](../src/file-io/Proj.md) | 3 | 51 | 0 | (pending) |
| [PropertyMapper](../src/file-io/PropertyMapper.md) | 2 | 125 | 343 | (pending) |
| [ReconstructionGeometryExportImpl](../src/file-io/ReconstructionGeometryExportImpl.md) | 1 | 624 | 205 | (pending) |
| [ResolvedTopologicalGeometryExport](../src/file-io/ResolvedTopologicalGeometryExport.md) | 3 | 604 | 5 | (pending) |
| [RgbaRasterReader](../src/file-io/RgbaRasterReader.md) | 3 | 1248 | 1 | (pending) |
| [RgbaRasterWriter](../src/file-io/RgbaRasterWriter.md) | 3 | 326 | 2 | (pending) |
| [RotationAttributesRegistry](../src/file-io/RotationAttributesRegistry.md) | 2 | 209 | 106 | (pending) |
| [ScalarField3DFileFormat](../src/file-io/ScalarField3DFileFormat.md) | 2 | 301 | 195 | (pending) |
| [ScalarField3DFileFormatReader](../src/file-io/ScalarField3DFileFormatReader.md) | 2 | 994 | 108 | (pending) |
| [ShapefileXmlReader](../src/file-io/ShapefileXmlReader.md) | 3 | 181 | 1 | (pending) |
| [ShapefileXmlWriter](../src/file-io/ShapefileXmlWriter.md) | 3 | 200 | 2 | (pending) |
| [SourceRasterFileCacheFormatReader](../src/file-io/SourceRasterFileCacheFormatReader.md) | 2 | 519 | 33 | (pending) |
| [StandaloneBundle](../src/file-io/StandaloneBundle.md) | 3 | 382 | 4 | (pending) |
| [SymbolFileReader](../src/file-io/SymbolFileReader.md) | 3 | 182 | 2 | (pending) |
| [TemporaryFileRegistry](../src/file-io/TemporaryFileRegistry.md) | 3 | 157 | 6 | (pending) |
| [TerraFormatVelocityVectorFieldExport](../src/file-io/TerraFormatVelocityVectorFieldExport.md) | 3 | 299 | 1 | (pending) |
| [XmlOutputInterface](../src/file-io/XmlOutputInterface.md) | 2 | 751 | 137 | (pending) |
| [XmlWriter](../src/file-io/XmlWriter.md) | 1 | 634 | 479 | (pending) |

### `src/file-io/deprecated`

| Unit | Tier | Lines | Fan-in | Description |
|---|---|---|---|---|
| [FeaturePropertiesMap](../src/file-io/deprecated/FeaturePropertiesMap.md) | 3 | 1503 | 0 | (pending) |
| [FileFormat](../src/file-io/deprecated/FileFormat.md) | 3 | 92 | 3 | (pending) |
| [GPlatesReader](../src/file-io/deprecated/GPlatesReader.md) | 3 | 490 | 8 | (pending) |
| [GpmlOnePointFiveOutputVisitor](../src/file-io/deprecated/GpmlOnePointFiveOutputVisitor.md) | 3 | 497 | 0 | (pending) |
| [NetCDFReader](../src/file-io/deprecated/NetCDFReader.md) | 3 | 450 | 2 | (pending) |
| [NetCDFWriter](../src/file-io/deprecated/NetCDFWriter.md) | 3 | 226 | 22 | (pending) |
| [PythonWrapper](../src/file-io/deprecated/PythonWrapper.md) | 3 | 34 | 0 | (pending) |
| [Reader](../src/file-io/deprecated/Reader.md) | 3 | 65 | 3 | (pending) |
| [Writer](../src/file-io/deprecated/Writer.md) | 3 | 55 | 2 | (pending) |
| [XMLParser](../src/file-io/deprecated/XMLParser.md) | 3 | 463 | 22 | (pending) |


## Other files

| File | Kind | Lines |
|---|---|---|
| `src/file-io/CMakeLists.txt` | build | 246 |
| `src/file-io/deprecated/HOWTO-add_support_for_a_new_feature` | other | 0 |
| `src/file-io/deprecated/HOWTO-add_support_for_a_new_property_type` | other | 0 |

## Depends on

| Component | References |
|---|---|
| [model](model.md) | 9531 |
| [property-values](property-values.md) | 2478 |
| [maths](maths.md) | 2405 |
| [utils](utils.md) | 1408 |
| [app-logic](app-logic.md) | 1115 |
| [global](global.md) | 910 |
| [gui](gui.md) | 483 |
| [qt-widgets](qt-widgets.md) | 384 |
| [feature-visitors](feature-visitors.md) | 224 |
| [opengl](opengl.md) | 27 |
| [unit-test](unit-test.md) | 19 |
| [system-fixes](system-fixes.md) | 6 |
| [data-mining](data-mining.md) | 5 |
| [api](api.md) | 3 |
| [scribe](scribe.md) | 2 |
| [view-operations](view-operations.md) | 1 |

## Used by

| Component | References |
|---|---|
| [qt-widgets](qt-widgets.md) | 1548 |
| [gui](gui.md) | 828 |
| [opengl](opengl.md) | 430 |
| [cli](cli.md) | 259 |
| [app-logic](app-logic.md) | 182 |
| [property-values](property-values.md) | 176 |
| [model](model.md) | 123 |
| [entry-points](entry-points.md) | 118 |
| [unit-test](unit-test.md) | 74 |
| [presentation](presentation.md) | 60 |
| [api](api.md) | 56 |
| [view-operations](view-operations.md) | 52 |
| [data-mining](data-mining.md) | 34 |
| [feature-visitors](feature-visitors.md) | 34 |
| [utils](utils.md) | 28 |
| [deprecated](deprecated.md) | 15 |
| [canvas-tools](canvas-tools.md) | 3 |
| [maths](maths.md) | 1 |

## Explore

Run these from the `gplates-code` skill directory:

```bash
python scripts/gpq.py tree src/file-io
python scripts/gpq.py sym . --mode sub --path src/file-io --defs-only
```
