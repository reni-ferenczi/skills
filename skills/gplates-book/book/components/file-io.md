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
| [ArbitraryNodeProcessor](../src/file-io/ArbitraryNodeProcessor.md) | 3 | 55 | 14 | Abstract interface for processing XML node data |
| [ArbitraryXmlProfile](../src/file-io/ArbitraryXmlProfile.md) | 2 | 67 | 35 | Abstract strategy interface for parsing arbitrary XML into a feature collection |
| [ArbitraryXmlReader](../src/file-io/ArbitraryXmlReader.md) | 2 | 233 | 25 | Singleton driver that reads XML via an injected ArbitraryXmlProfile |

#### Citcoms

| Unit | Tier | Lines | Fan-in | Description |
|---|---|---|---|---|
| [CitcomsFormatVelocityVectorFieldExport](../src/file-io/CitcomsFormatVelocityVectorFieldExport.md) | 3 | 383 | 2 | Exports velocity vector fields to CitcomS mantle simulation format |
| [CitcomsGMTFormatResolvedTopologicalBoundaryExport](../src/file-io/CitcomsGMTFormatResolvedTopologicalBoundaryExport.md) | 2 | 1029 | 42 | Writes CitcomS resolved topologies and subsegments as GMT multi-segment files |
| [CitcomsResolvedTopologicalBoundaryExport](../src/file-io/CitcomsResolvedTopologicalBoundaryExport.md) | 2 | 2016 | 138 | Orchestrates CitcomS resolved-topology export across output formats and file layouts |
| [CitcomsResolvedTopologicalBoundaryExportImpl](../src/file-io/CitcomsResolvedTopologicalBoundaryExportImpl.md) | 2 | 617 | 292 | Shared types and subsegment classification for the CitcomS resolved-topology exporters |

#### Error

| Unit | Tier | Lines | Fan-in | Description |
|---|---|---|---|---|
| [ErrorOpeningFileForReadingException](../src/file-io/ErrorOpeningFileForReadingException.md) | 2 | 127 | 534 | Thrown when a file cannot be opened for reading |
| [ErrorOpeningFileForWritingException](../src/file-io/ErrorOpeningFileForWritingException.md) | 2 | 125 | 242 | Thrown when a file cannot be opened for writing |
| [ErrorOpeningPipeFromGzipException](../src/file-io/ErrorOpeningPipeFromGzipException.md) | 3 | 142 | 2 | Exception when gzip decompression pipe cannot be opened for reading |
| [ErrorOpeningPipeToGzipException](../src/file-io/ErrorOpeningPipeToGzipException.md) | 3 | 142 | 1 | Exception when gzip compression pipe cannot be opened for writing |
| [ErrorWritingFeatureCollectionToFileFormatException](../src/file-io/ErrorWritingFeatureCollectionToFileFormatException.md) | 3 | 94 | 2 | Exception when file format constraints prevent writing valid data |

#### Export

| Unit | Tier | Lines | Fan-in | Description |
|---|---|---|---|---|
| [ExportTemplateFilenameSequence](../src/file-io/ExportTemplateFilenameSequence.md) | 2 | 540 | 241 | Iterable sequence of export filenames expanded from a printf-style template per frame |
| [ExportTemplateFilenameSequenceFormats](../src/file-io/ExportTemplateFilenameSequenceFormats.md) | 2 | 836 | 32 | One Format subclass per filename-template placeholder, matched and expanded per frame |
| [ExportTemplateFilenameSequenceImpl](../src/file-io/ExportTemplateFilenameSequenceImpl.md) | 3 | 809 | 1 | Generates export filenames by expanding format placeholders in templates |

#### Feature

| Unit | Tier | Lines | Fan-in | Description |
|---|---|---|---|---|
| [FeatureCollectionFileFormat](../src/file-io/FeatureCollectionFileFormat.md) | 2 | 59 | 428 | Enumerates every file format that can hold a feature collection |
| [FeatureCollectionFileFormatClassify](../src/file-io/FeatureCollectionFileFormatClassify.md) | 2 | 426 | 46 | Classifies features and feature collections by content kind, independent of file format |
| [FeatureCollectionFileFormatConfiguration](../src/file-io/FeatureCollectionFileFormatConfiguration.md) | 2 | 167 | 314 | Empty polymorphic base for per-file-format read/write configuration options |
| [FeatureCollectionFileFormatConfigurations](../src/file-io/FeatureCollectionFileFormatConfigurations.md) | 2 | 270 | 117 | Concrete Configuration subclasses for the GMT and OGR-backed file formats |
| [FeatureCollectionFileFormatRegistry](../src/file-io/FeatureCollectionFileFormatRegistry.md) | 2 | 1336 | 149 | Central map from Format to its detector, reader, writer and default configuration |

#### File

| Unit | Tier | Lines | Fan-in | Description |
|---|---|---|---|---|
| [File](../src/file-io/File.md) | 1 | 357 | 970 | binds a feature collection to the file it came from, owning it until the model takes over |
| [FileFormatNotSupportedException](../src/file-io/FileFormatNotSupportedException.md) | 2 | 73 | 41 | Exception thrown when a file format is recognised but unusable for the requested operation |
| [FileInfo](../src/file-io/FileInfo.md) | 2 | 274 | 76 | Qt-based wrapper around a loaded file's path, display name and writability checks |
| [FileLoadAbortedException](../src/file-io/FileLoadAbortedException.md) | 3 | 90 | 2 | Exception thrown when user cancels a file load operation |

#### G

| Unit | Tier | Lines | Fan-in | Description |
|---|---|---|---|---|
| [GMTFormatDeformationExport](../src/file-io/GMTFormatDeformationExport.md) | 3 | 713 | 6 | Exports deformation and strain information to GMT format |
| [GMTFormatFlowlineExport](../src/file-io/GMTFormatFlowlineExport.md) | 3 | 469 | 6 | Exports reconstructed flowlines to GMT format |
| [GMTFormatGeometryExporter](../src/file-io/GMTFormatGeometryExporter.md) | 2 | 367 | 23 | ConstGeometryOnSphereVisitor writing a GeometryOnSphere as GMT xy point records |
| [GMTFormatHeader](../src/file-io/GMTFormatHeader.md) | 2 | 1302 | 79 | Strategies for formatting and printing the \> comment header above a GMT feature |
| [GMTFormatMotionPathExport](../src/file-io/GMTFormatMotionPathExport.md) | 3 | 437 | 6 | Exports reconstructed motion paths to GMT format |
| [GMTFormatMultiPointVectorFieldExport](../src/file-io/GMTFormatMultiPointVectorFieldExport.md) | 3 | 522 | 7 | Exports velocity vector fields to GMT format |
| [GMTFormatReconstructedFeatureGeometryExport](../src/file-io/GMTFormatReconstructedFeatureGeometryExport.md) | 3 | 257 | 5 | Exports reconstructed feature geometries to GMT format |
| [GMTFormatReconstructedScalarCoverageExport](../src/file-io/GMTFormatReconstructedScalarCoverageExport.md) | 3 | 608 | 6 | Exports reconstructed scalar coverages to GMT format |
| [GMTFormatResolvedTopologicalGeometryExport](../src/file-io/GMTFormatResolvedTopologicalGeometryExport.md) | 3 | 405 | 2 | Exports resolved topological geometries and sections to GMT format |
| [GMTFormatWriter](../src/file-io/GMTFormatWriter.md) | 2 | 396 | 29 | ConstFeatureVisitor writing a feature collection to a GMT xy file with headers |

#### Gdal

| Unit | Tier | Lines | Fan-in | Description |
|---|---|---|---|---|
| [Gdal](../src/file-io/Gdal.md) | 3 | 40 | 0 | Wrapper header for GDAL includes with system-appropriate configuration |
| [GdalRasterReader](../src/file-io/GdalRasterReader.md) | 2 | 2815 | 5 | GDAL-backed raster reader with a Hilbert-curve block cache for fast windowed reads |
| [GdalRasterWriter](../src/file-io/GdalRasterWriter.md) | 2 | 1367 | 29 | GDAL-backed raster writer that buffers in memory before copying out to the file |
| [GdalUtils](../src/file-io/GdalUtils.md) | 2 | 593 | 88 | Shared GDAL/OGR driver registration, open/close and GDAL-1-vs-2 typedefs |

#### GpmlFeature

| Unit | Tier | Lines | Fan-in | Description |
|---|---|---|---|---|
| [GpmlFeatureReaderFactory](../src/file-io/GpmlFeatureReaderFactory.md) | 3 | 962 | 4 | Creates feature readers configured for a specific GPGIM version with upgrade logic for older versions |
| [GpmlFeatureReaderImpl](../src/file-io/GpmlFeatureReaderImpl.md) | 1 | 822 | 330 | chain of readers, one per GPGIM feature class, turning a GPML element into a feature |
| [GpmlFeatureReaderInterface](../src/file-io/GpmlFeatureReaderInterface.md) | 3 | 134 | 4 | Wrapper interface for reading individual features from GPML XML using an implementation backend |

#### GpmlFormat

| Unit | Tier | Lines | Fan-in | Description |
|---|---|---|---|---|
| [GpmlFormatDeformationExport](../src/file-io/GpmlFormatDeformationExport.md) | 3 | 508 | 2 | Exports deformation data (strain, strain rates) from reconstructed features to GPML format |
| [GpmlFormatMultiPointVectorFieldExport](../src/file-io/GpmlFormatMultiPointVectorFieldExport.md) | 3 | 438 | 6 | Exports velocity vector fields from plate reconstruction to GPML VelocityField features |
| [GpmlFormatReconstructedScalarCoverageExport](../src/file-io/GpmlFormatReconstructedScalarCoverageExport.md) | 3 | 464 | 5 | Exports reconstructed scalar coverages (domain geometries with per-point scalars) to GPML format |

#### GpmlProperty

| Unit | Tier | Lines | Fan-in | Description |
|---|---|---|---|---|
| [GpmlPropertyReader](../src/file-io/GpmlPropertyReader.md) | 2 | 1076 | 23 | Reads one named feature property by validating it against a GpgimProperty |
| [GpmlPropertyStructuralTypeReader](../src/file-io/GpmlPropertyStructuralTypeReader.md) | 1 | 529 | 1813 | dispatch table from GPML structural type name to the function that parses it |
| [GpmlPropertyStructuralTypeReaderUtils](../src/file-io/GpmlPropertyStructuralTypeReaderUtils.md) | 2 | 1641 | 131 | Parses GPML/GML structural types that can appear directly as feature properties |

#### GpmlReader

| Unit | Tier | Lines | Fan-in | Description |
|---|---|---|---|---|
| [GpmlReader](../src/file-io/GpmlReader.md) | 3 | 507 | 4 | Reads GPML XML files into the GPlates feature model, handling version detection and file path resolution |
| [GpmlReaderException](../src/file-io/GpmlReaderException.md) | 2 | 94 | 68 | Exception thrown when a GPML XML element cannot be parsed as its expected type |
| [GpmlReaderUtils](../src/file-io/GpmlReaderUtils.md) | 2 | 266 | 69 | Bundles GPML reader state and provides uniform read-error-reporting helpers |

#### Gsml

| Unit | Tier | Lines | Fan-in | Description |
|---|---|---|---|---|
| [GsmlConst](../src/file-io/GsmlConst.md) | 3 | 70 | 19 | XML namespace declarations for GeoSciML and related standards as strings for XQuery expressions |
| [GsmlFeatureHandlers](../src/file-io/GsmlFeatureHandlers.md) | 3 | 241 | 6 | Parses and creates GPlates features from GeoSciML XML during file import |
| [GsmlFeaturesDef](../src/file-io/GsmlFeaturesDef.md) | 3 | 133 | 15 | Metadata definition of supported GeoSciML feature types and their property schemas |
| [GsmlNodeProcessor](../src/file-io/GsmlNodeProcessor.md) | 3 | 133 | 7 | Processor executing XQueries against GSML XML and invoking a handler on each result |
| [GsmlNodeProcessorFactory](../src/file-io/GsmlNodeProcessorFactory.md) | 3 | 206 | 8 | Orchestrates GSML property extraction by creating and executing property-specific node processors |
| [GsmlPropertyDef](../src/file-io/GsmlPropertyDef.md) | 2 | 144 | 37 | Table of GSML property-to-XPath-to-handler bindings used by the GeoSciML reader |
| [GsmlPropertyHandlers](../src/file-io/GsmlPropertyHandlers.md) | 2 | 824 | 23 | Parses matched GSML/GML XML fragments into GPML property values on a feature |

#### Ogr

| Unit | Tier | Lines | Fan-in | Description |
|---|---|---|---|---|
| [Ogr](../src/file-io/Ogr.md) | 3 | 35 | 0 | Convenience header ensuring GDAL version macros are available when using OGR |
| [OgrException](../src/file-io/OgrException.md) | 3 | 76 | 15 | Exception class thrown when OGR encounters errors during file I/O operations |
| [OgrFeatureCollectionWriter](../src/file-io/OgrFeatureCollectionWriter.md) | 3 | 1989 | 1 | Exports feature collections to OGR formats with configurable model-to-attribute property mapping |
| [OgrFormatFlowlineExport](../src/file-io/OgrFormatFlowlineExport.md) | 3 | 326 | 2 | Exports reconstructed flowline objects to ESRI Shapefile format with seed points and metadata |
| [OgrFormatMotionPathExport](../src/file-io/OgrFormatMotionPathExport.md) | 3 | 301 | 2 | Exports reconstructed motion path objects to ESRI Shapefile format with seed points and metadata |
| [OgrFormatReconstructedFeatureGeometryExport](../src/file-io/OgrFormatReconstructedFeatureGeometryExport.md) | 3 | 437 | 3 | Exports reconstructed feature geometries to ESRI Shapefile format, excluding flowlines and motion paths |
| [OgrFormatResolvedTopologicalGeometryExport](../src/file-io/OgrFormatResolvedTopologicalGeometryExport.md) | 3 | 638 | 6 | Exports resolved topological geometries to OGR format with optional CitcomS variants |
| [OgrGeometryExporter](../src/file-io/OgrGeometryExporter.md) | 2 | 373 | 12 | Adapts the GeometryOnSphere visitor hierarchy to OgrWriter's per-geometry-type write calls |
| [OgrReader](../src/file-io/OgrReader.md) | 2 | 2799 | 7 | Static GDAL/OGR-backed reader for shapefiles and other OGR vector formats, successor to ShapefileReader |
| [OgrUtils](../src/file-io/OgrUtils.md) | 2 | 1358 | 94 | Shared helpers for OGR feature-type/geometry mapping, the attribute-mapping sidecar file, and export key-value dictionaries |
| [OgrWriter](../src/file-io/OgrWriter.md) | 2 | 1596 | 21 | Low-level OGR feature writer that lazily creates one data source and layer per geometry type |

#### Plates

| Unit | Tier | Lines | Fan-in | Description |
|---|---|---|---|---|
| [PlatesFormatUtils](../src/file-io/PlatesFormatUtils.md) | 3 | 698 | 12 | Maps GPlates geological feature types to PLATES4 header data type codes |
| [PlatesLineFormatGeometryExporter](../src/file-io/PlatesLineFormatGeometryExporter.md) | 3 | 450 | 4 | Visitor converting geometries to PLATES4 pen-coded coordinate sequences |
| [PlatesLineFormatHeaderVisitor](../src/file-io/PlatesLineFormatHeaderVisitor.md) | 2 | 539 | 70 | Reconstructs or synthesizes a PLATES4 header line for a feature being exported |
| [PlatesLineFormatReader](../src/file-io/PlatesLineFormatReader.md) | 3 | 2259 | 1 | Reads PLATES line-format files and converts them to GPlates GPML features |
| [PlatesLineFormatWriter](../src/file-io/PlatesLineFormatWriter.md) | 3 | 485 | 1 | Feature visitor writing GPlates features to PLATES4 line format with headers |
| [PlatesRotationFileProxy](../src/file-io/PlatesRotationFileProxy.md) | 1 | 2927 | 191 | .grot rotation format support, keeping the file's own text as editable segments beside the model |
| [PlatesRotationFormatReader](../src/file-io/PlatesRotationFormatReader.md) | 3 | 930 | 1 | Reads PLATES rotation-format ASCII files and materializes them as total reconstruction sequence features grouped by reference frame pairs |
| [PlatesRotationFormatWriter](../src/file-io/PlatesRotationFormatWriter.md) | 2 | 675 | 96 | Feature visitor writing total reconstruction sequences back out as PLATES4 .rot or GROT lines |

#### Raster

| Unit | Tier | Lines | Fan-in | Description |
|---|---|---|---|---|
| [RasterBandReader](../src/file-io/RasterBandReader.md) | 2 | 207 | 331 | RasterReader adapter bound to one fixed band number |
| [RasterBandReaderHandle](../src/file-io/RasterBandReaderHandle.md) | 2 | 145 | 17 | Copyable handle to a RasterBandReader stored inside a proxied RawRaster |
| [RasterFileCache](../src/file-io/RasterFileCache.md) | 3 | 377 | 4 | Utility for creating and managing disk caches of mipmapped raster files to avoid regeneration |
| [RasterFileCacheFormat](../src/file-io/RasterFileCacheFormat.md) | 1 | 881 | 537 | on-disk layout, versioning and filename policy for GPlates block-encoded raster and mipmap cache files |
| [RasterFileCacheFormatReader](../src/file-io/RasterFileCacheFormatReader.md) | 3 | 516 | 6 | Reads cached raster images stored in blocks arranged in a Hilbert curve for optimal disk locality |
| [RasterReader](../src/file-io/RasterReader.md) | 2 | 899 | 192 | Format-independent facade over the RGBA and GDAL raster-reading backends |
| [RasterWriter](../src/file-io/RasterWriter.md) | 2 | 680 | 123 | Format-independent facade over the RGBA and GDAL raster-writing backends |

#### Read

| Unit | Tier | Lines | Fan-in | Description |
|---|---|---|---|---|
| [ReadErrorAccumulation](../src/file-io/ReadErrorAccumulation.md) | 1 | 154 | 731 | bucket of read problems that every file reader fills, classified by consequence rather than cause |
| [ReadErrorMessages](../src/file-io/ReadErrorMessages.md) | 2 | 784 | 12 | Translates ReadErrors::Description and ReadErrors::Result codes into user-facing text |
| [ReadErrorOccurrence](../src/file-io/ReadErrorOccurrence.md) | 1 | 395 | 285 | one reported read problem: an abstract data source and location plus a description and result code |
| [ReadErrorUtils](../src/file-io/ReadErrorUtils.md) | 2 | 217 | 44 | Groups and summarises a ReadErrorAccumulation for reporting |
| [ReadErrors](../src/file-io/ReadErrors.md) | 1 | 309 | 1358 | the enum vocabulary every reader uses to report what went wrong and what GPlates did about it |

#### Reconstructed

| Unit | Tier | Lines | Fan-in | Description |
|---|---|---|---|---|
| [ReconstructedFeatureGeometryExport](../src/file-io/ReconstructedFeatureGeometryExport.md) | 2 | 392 | 29 | Exports ReconstructedFeatureGeometry batches to GMT, Shapefile, OGRGMT or GeoJSON |
| [ReconstructedFlowlineExport](../src/file-io/ReconstructedFlowlineExport.md) | 3 | 368 | 3 | Exports reconstructed flowlines (paths traced by plate points) to GMT, Shapefile, OGR GMT and GeoJSON formats |
| [ReconstructedMotionPathExport](../src/file-io/ReconstructedMotionPathExport.md) | 3 | 367 | 3 | Exports reconstructed motion paths (instantaneous plate point displacements) to GMT, Shapefile, OGR GMT and GeoJSON formats |
| [ReconstructedScalarCoverageExport](../src/file-io/ReconstructedScalarCoverageExport.md) | 3 | 361 | 10 | Exports reconstructed scalar coverages (point-sampled scalar fields) with optional strain data to GPML and GMT formats |

#### Other

| Unit | Tier | Lines | Fan-in | Description |
|---|---|---|---|---|
| [AgeModelReader](../src/file-io/AgeModelReader.md) | 3 | 231 | 2 | Parses tab-delimited age model files for geological chronology data |
| [CptReader](../src/file-io/CptReader.md) | 1 | 2623 | 156 | GMT colour palette (.cpt) parsing: a traits-driven template reader plus a separate newer parser |
| [DeformationExport](../src/file-io/DeformationExport.md) | 2 | 482 | 171 | Writes per-point deformation strain and stretch data to GPML or GMT format |
| [GeometryExporter](../src/file-io/GeometryExporter.md) | 2 | 56 | 19 | Single-method interface letting callers export any GeometryOnSphere polymorphically |
| [GeoscimlProfile](../src/file-io/GeoscimlProfile.md) | 3 | 244 | 3 | Parses GeoSciML XML documents and populates a feature collection with GeoSciML features |
| [GmapReader](../src/file-io/GmapReader.md) | 2 | 603 | 28 | Parses GMAP-format virtual geomagnetic pole (VGP) files into a feature collection |
| [GpmlOutputVisitor](../src/file-io/GpmlOutputVisitor.md) | 2 | 2166 | 115 | Writes visited features and property values out as GPML/GML XML |
| [GpmlStructuralTypeReaderUtils](../src/file-io/GpmlStructuralTypeReaderUtils.md) | 2 | 2531 | 171 | Parses GPML/GML structural types nested inside other structural types, not standalone properties |
| [GpmlUpgradeReaderUtils](../src/file-io/GpmlUpgradeReaderUtils.md) | 2 | 1459 | 25 | Decorator feature readers that let old-GPGIM-version GPML files load under the current schema |
| [GzipFile](../src/file-io/GzipFile.md) | 2 | 726 | 11 | QIODevice adapter that streams gzip compression/decompression through zlib |
| [HellingerReader](../src/file-io/HellingerReader.md) | 2 | 1094 | 16 | Parses Hellinger .pick and .com plate-fitting text files into a HellingerModel |
| [HellingerWriter](../src/file-io/HellingerWriter.md) | 2 | 294 | 137 | Serialises a HellingerModel back to Hellinger .pick and .com text file formats |
| [LineReader](../src/file-io/LineReader.md) | 2 | 221 | 27 | Buffered UTF-8 line reader over QTextStream with one line of lookahead |
| [LogToFileHandler](../src/file-io/LogToFileHandler.md) | 3 | 324 | 1 | Logs Qt messages to file or stream with severity filtering and platform-aware fallback directories |
| [MipmappedRasterFormatReader](../src/file-io/MipmappedRasterFormatReader.md) | 2 | 490 | 39 | Reads regions of a specific level from a GPlates mipmapped raster cache file |
| [MipmappedRasterFormatWriter](../src/file-io/MipmappedRasterFormatWriter.md) | 2 | 1380 | 3 | Generates the mipmap cache files consumed by MipmappedRasterFormatReader |
| [MultiPointVectorFieldExport](../src/file-io/MultiPointVectorFieldExport.md) | 2 | 741 | 67 | Groups and dispatches velocity multi-point vector fields to GPML, GMT, Terra or CitcomS export formats |
| [Proj](../src/file-io/Proj.md) | 3 | 51 | 0 | Compatibility wrapper that includes the appropriate PROJ header for the detected library version |
| [PropertyMapper](../src/file-io/PropertyMapper.md) | 2 | 125 | 343 | Abstract interface for mapping shapefile attribute fields onto GPlates model properties |
| [ReconstructionGeometryExportImpl](../src/file-io/ReconstructionGeometryExportImpl.md) | 1 | 624 | 205 | shared regrouping of flat reconstruction-geometry sequences into file-and-feature hierarchies for export |
| [ResolvedTopologicalGeometryExport](../src/file-io/ResolvedTopologicalGeometryExport.md) | 3 | 604 | 5 | Exports resolved topological geometries and sections (plate boundary-respecting geometries) to GMT, Shapefile, OGR GMT and GeoJSON formats |
| [RgbaRasterReader](../src/file-io/RgbaRasterReader.md) | 3 | 1248 | 1 | Loads RGBA raster images with caching for spatial locality |
| [RgbaRasterWriter](../src/file-io/RgbaRasterWriter.md) | 3 | 326 | 2 | Writes RGBA rasters to image files |
| [RotationAttributesRegistry](../src/file-io/RotationAttributesRegistry.md) | 2 | 209 | 106 | Schema of known metadata attribute names in GPlates-extended rotation files |
| [ScalarField3DFileFormat](../src/file-io/ScalarField3DFileFormat.md) | 2 | 301 | 195 | On-disk binary layout constants and record structs for GPlates 3D scalar field files |
| [ScalarField3DFileFormatReader](../src/file-io/ScalarField3DFileFormatReader.md) | 2 | 994 | 108 | Version-dispatching reader for scalar field files, with random-access reads by layer or tile |
| [ShapefileXmlReader](../src/file-io/ShapefileXmlReader.md) | 3 | 181 | 1 | Parses GPlates shapefile property mapping XML files |
| [ShapefileXmlWriter](../src/file-io/ShapefileXmlWriter.md) | 3 | 200 | 2 | Serializes property mappings to shapefile XML files |
| [SourceRasterFileCacheFormatReader](../src/file-io/SourceRasterFileCacheFormatReader.md) | 2 | 519 | 33 | Region-based reader interface for a decoded source raster's on-disk cache |
| [StandaloneBundle](../src/file-io/StandaloneBundle.md) | 3 | 382 | 4 | Locates bundled resources in standalone GPlates and pyGPlates distributions |
| [SymbolFileReader](../src/file-io/SymbolFileReader.md) | 3 | 182 | 2 | Parses symbol mapping files for feature rendering |
| [TemporaryFileRegistry](../src/file-io/TemporaryFileRegistry.md) | 3 | 157 | 6 | Tracks temporary files for deletion at application exit |
| [TerraFormatVelocityVectorFieldExport](../src/file-io/TerraFormatVelocityVectorFieldExport.md) | 3 | 299 | 1 | Exports velocity vector fields to Terra text format |
| [XmlOutputInterface](../src/file-io/XmlOutputInterface.md) | 2 | 751 | 137 | Hand-rolled indenting XML writer used by the deprecated GPML 1.5 output path |
| [XmlWriter](../src/file-io/XmlWriter.md) | 1 | 634 | 479 | QXmlStreamWriter façade that preserves the originating document's namespace prefixes when writing GPML |

### `src/file-io/deprecated`

| Unit | Tier | Lines | Fan-in | Description |
|---|---|---|---|---|
| [FeaturePropertiesMap](../src/file-io/deprecated/FeaturePropertiesMap.md) | 3 | 1503 | 0 | Maps GPML feature types to their valid properties and parsing functions |
| [FileFormat](../src/file-io/deprecated/FileFormat.md) | 3 | 92 | 3 | Metadata container for a file format with name, suffixes, and reader/writer |
| [GPlatesReader](../src/file-io/deprecated/GPlatesReader.md) | 3 | 490 | 8 | Parses the legacy GPlates data format into internal representation |
| [GpmlOnePointFiveOutputVisitor](../src/file-io/deprecated/GpmlOnePointFiveOutputVisitor.md) | 3 | 497 | 0 | Visitor that serializes features to GPML 1.5 XML format |
| [NetCDFReader](../src/file-io/deprecated/NetCDFReader.md) | 3 | 450 | 2 | Parses NetCDF raster files into grid data |
| [NetCDFWriter](../src/file-io/deprecated/NetCDFWriter.md) | 3 | 226 | 22 | Writes grid data to NetCDF raster format |
| [PythonWrapper](../src/file-io/deprecated/PythonWrapper.md) | 3 | 34 | 0 | Empty Boost.Python wrapper for deprecated file-io module |
| [Reader](../src/file-io/deprecated/Reader.md) | 3 | 65 | 3 | Abstract base class defining the file reader interface |
| [Writer](../src/file-io/deprecated/Writer.md) | 3 | 55 | 2 | Abstract base class interface for file writers in the deprecated FileFormat infrastructure |
| [XMLParser](../src/file-io/deprecated/XMLParser.md) | 3 | 463 | 22 | DOM-like wrapper around expat XML parser for parsing XML documents into element trees |


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
