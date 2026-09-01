# ReadErrors

[Book TOC](../../TOC.md) · [file-io](../../components/file-io.md) · cluster Community 7 · tier 1

| Source file | Kind | Lines |
|---|---|---|
| `src/file-io/ReadErrors.h` | C++ | 309 |

## Overview

[[[PROSE overview unit=file-io/ReadErrors tier=1]]]
Replace this whole block, markers included, with 1-3 paragraphs: what this unit is, why it exists, and how it fits the surrounding design. Do not restate the tables below.
[[[/PROSE]]]

## Declared types

| Name | Kind | Bases | Template | Subclasses | Description |
|---|---|---|---|---|---|
| [`GPlatesFileIO::ReadErrors::Description`](#gplatesfileioreaderrorsdescription) | enum | — | — | 0 | — |
| [`GPlatesFileIO::ReadErrors::Result`](#gplatesfileioreaderrorsresult) | enum | — | — | 0 | — |
| [`GPlatesFileIO::ReadErrors::Severity`](#gplatesfileioreaderrorsseverity) | enum | — | — | 0 | Enumeration of possible error categories, for a simple way to report how severe an accumulation of errors is (ReadErrorAccumulation::most\_severe\_error\_type()). |

## Members

### `GPlatesFileIO::ReadErrors::Description`

| Member | Kind | Type | Access | Description |
|---|---|---|---|---|
| `CommentMovingPlateIdAfterNonCommentSequence` | enumerator | `None` | — | These are specific to PLATES rotation-format reading. |
| `ErrorReadingFixedPlateId` | enumerator | `None` | — | — |
| `ErrorReadingGeoTime` | enumerator | `None` | — | — |
| `ErrorReadingMovingPlateId` | enumerator | `None` | — | — |
| `ErrorReadingPoleLatitude` | enumerator | `None` | — | — |
| `ErrorReadingPoleLongitude` | enumerator | `None` | — | — |
| `InvalidPoleLatitude` | enumerator | `None` | — | — |
| `ErrorReadingRotationAngle` | enumerator | `None` | — | — |
| `InvalidPoleLongitude` | enumerator | `None` | — | — |
| `MovingPlateIdEqualsFixedPlateId` | enumerator | `None` | — | — |
| `NoCommentFound` | enumerator | `None` | — | — |
| `NoExclMarkToStartComment` | enumerator | `None` | — | — |
| `SamePlateIdsButDuplicateGeoTime` | enumerator | `None` | — | — |
| `SamePlateIdsButEarlierGeoTime` | enumerator | `None` | — | — |
| `PoleTakesLongRotationPathRelativeToPrevPole` | enumerator | `None` | — | — |
| `InvalidPlatesRegionNumber` | enumerator | `None` | — | The following are specific to PLATES line-format reading. |
| `InvalidPlatesReferenceNumber` | enumerator | `None` | — | — |
| `InvalidPlatesStringNumber` | enumerator | `None` | — | — |
| `InvalidPlatesGeographicDescription` | enumerator | `None` | — | — |
| `InvalidPlatesPlateIdNumber` | enumerator | `None` | — | — |
| `InvalidPlatesAgeOfAppearance` | enumerator | `None` | — | — |
| `InvalidPlatesAgeOfDisappearance` | enumerator | `None` | — | — |
| `InvalidPlatesDataTypeCode` | enumerator | `None` | — | — |
| `InvalidPlatesDataTypeCodeNumber` | enumerator | `None` | — | — |
| `InvalidPlatesDataTypeCodeNumberAdditional` | enumerator | `None` | — | — |
| `InvalidPlatesConjugatePlateIdNumber` | enumerator | `None` | — | — |
| `InvalidPlatesColourCode` | enumerator | `None` | — | — |
| `InvalidPlatesNumberOfPoints` | enumerator | `None` | — | — |
| `UnknownPlatesDataTypeCode` | enumerator | `None` | — | — |
| `MissingPlatesPolylinePoint` | enumerator | `None` | — | — |
| `MissingPlatesHeaderSecondLine` | enumerator | `None` | — | — |
| `InvalidPlatesPolylinePoint` | enumerator | `None` | — | — |
| `InvalidPlatesPolylinePlotterCode` | enumerator | `None` | — | — |
| `InvalidPlatesPolylineLatitude` | enumerator | `None` | — | — |
| `InvalidPlatesPolylineLongitude` | enumerator | `None` | — | — |
| `AdjacentSkipToPlotterCodes` | enumerator | `None` | — | — |
| `AmbiguousPlatesIceShelfCode` | enumerator | `None` | — | — |
| `MoreThanOneDistinctPoint` | enumerator | `None` | — | — |
| `NoValidGeometriesInPlatesFeature` | enumerator | `None` | — | — |
| `InvalidMultipointGeometry` | enumerator | `None` | — | — |
| `MissingPlatepolygonBoundaryFeature` | enumerator | `None` | — | The following are specific to GPlates 8 hydrid PLATES line-format. |
| `InvalidPlatepolygonBoundaryFeature` | enumerator | `None` | — | — |
| `ErrorReadingVectorFile` | enumerator | `None` | — | The following apply to OGR-supported file format import. |
| `NoLayersFoundInFile` | enumerator | `None` | — | — |
| `MultipleLayersInFile` | enumerator | `None` | — | — |
| `ErrorReadingOgrLayer` | enumerator | `None` | — | — |
| `NoFeaturesFoundInOgrFile` | enumerator | `None` | — | — |
| `ErrorReadingOgrGeometry` | enumerator | `None` | — | — |
| `TwoPointFiveDGeometryDetected` | enumerator | `None` | — | — |
| `LessThanTwoPointsInLineString` | enumerator | `None` | — | — |
| `InteriorRingsInShapefile` | enumerator | `None` | — | — |
| `UnsupportedGeometryType` | enumerator | `None` | — | — |
| `NoLatitudeShapeData` | enumerator | `None` | — | — |
| `NoLongitudeShapeData` | enumerator | `None` | — | — |
| `InvalidOgrLatitude` | enumerator | `None` | — | — |
| `InvalidOgrLongitude` | enumerator | `None` | — | — |
| `NoPlateIdFound` | enumerator | `None` | — | — |
| `InvalidShapefilePlateIdNumber` | enumerator | `None` | — | — |
| `UnrecognisedOgrFeatureType` | enumerator | `None` | — | — |
| `InvalidShapefileAgeOfAppearance` | enumerator | `None` | — | — |
| `InvalidShapefileAgeOfDisappearance` | enumerator | `None` | — | — |
| `InvalidShapefileConjugatePlateIdNumber` | enumerator | `None` | — | — |
| `InvalidOgrPoint` | enumerator | `None` | — | — |
| `InvalidOgrMultiPoint` | enumerator | `None` | — | — |
| `InvalidOgrPolyline` | enumerator | `None` | — | — |
| `InvalidOgrPolygon` | enumerator | `None` | — | — |
| `InvalidShapefileReconstructionMethod` | enumerator | `None` | — | — |
| `InvalidShapefileSpreadingAsymmetry` | enumerator | `None` | — | — |
| `InvalidShapefileGeometryImportTime` | enumerator | `None` | — | — |
| `UnableToMatchOgrGeometryWithFeature` | enumerator | `None` | — | — |
| `NoGeometriesFoundInMultiGeometry` | enumerator | `None` | — | — |
| `InsufficientMemoryToLoadRaster` | enumerator | `None` | — | The following relate to raster files in general. |
| `ErrorGeneratingTexture` | enumerator | `None` | — | — |
| `UnrecognisedRasterFileType` | enumerator | `None` | — | — |
| `ErrorReadingRasterFile` | enumerator | `None` | — | — |
| `ErrorReadingRasterBand` | enumerator | `None` | — | — |
| `InvalidRegionInRaster` | enumerator | `None` | — | — |
| `ErrorInSystemLibraries` | enumerator | `None` | — | The following relate to GDAL-readable raster files. |
| `NoRasterSetsFound` | enumerator | `None` | — | The following relate to time-dependent raster file sets. |
| `MultipleRasterSetsFound` | enumerator | `None` | — | — |
| `DepthLayerRasterIsNotNumerical` | enumerator | `None` | — | The following relate to importing 3D scalar field files. |
| `DuplicateProperty` | enumerator | `None` | — | The following apply to GPML import |
| `NecessaryPropertyNotFound` | enumerator | `None` | — | — |
| `UnknownValueType` | enumerator | `None` | — | — |
| `BadOrMissingTargetForValueType` | enumerator | `None` | — | — |
| `InvalidBoolean` | enumerator | `None` | — | — |
| `InvalidDouble` | enumerator | `None` | — | — |
| `InvalidGeoTime` | enumerator | `None` | — | — |
| `InvalidInt` | enumerator | `None` | — | — |
| `InvalidLatLonPoint` | enumerator | `None` | — | — |
| `InvalidLong` | enumerator | `None` | — | — |
| `InvalidPointsInPolyline` | enumerator | `None` | — | — |
| `InsufficientDistinctPointsInPolyline` | enumerator | `None` | — | — |
| `AntipodalAdjacentPointsInPolyline` | enumerator | `None` | — | — |
| `InvalidPointsInPolygon` | enumerator | `None` | — | — |
| `InsufficientPointsInPolygon` | enumerator | `None` | — | — |
| `InsufficientDistinctPointsInPolygon` | enumerator | `None` | — | — |
| `AntipodalAdjacentPointsInPolygon` | enumerator | `None` | — | — |
| `InvalidEnumerationValue` | enumerator | `None` | — | — |
| `InvalidString` | enumerator | `None` | — | — |
| `InvalidUnsignedInt` | enumerator | `None` | — | — |
| `InvalidUnsignedLong` | enumerator | `None` | — | — |
| `InvalidTupleList` | enumerator | `None` | — | — |
| `MissingNamespaceAlias` | enumerator | `None` | — | — |
| `NonUniqueStructuralElement` | enumerator | `None` | — | — |
| `StructuralElementNotFound` | enumerator | `None` | — | — |
| `UnexpectedStructuralElement` | enumerator | `None` | — | — |
| `UnexpectedPropertyStructuralElement` | enumerator | `None` | — | — |
| `PropertyNameNotRecognisedInFeatureType` | enumerator | `None` | — | — |
| `TimeDependentPropertyStructuralElementNotFound` | enumerator | `None` | — | — |
| `TimeDependentPropertyStructuralElementFound` | enumerator | `None` | — | — |
| `IncorrectTimeDependentPropertyStructuralElementFound` | enumerator | `None` | — | — |
| `TooManyChildrenInElement` | enumerator | `None` | — | — |
| `UnexpectedEmptyString` | enumerator | `None` | — | — |
| `UnrecognisedChildFound` | enumerator | `None` | — | — |
| `DuplicateIdentityProperty` | enumerator | `None` | — | — |
| `DuplicateRevisionProperty` | enumerator | `None` | — | — |
| `UnrecognisedFeatureCollectionElement` | enumerator | `None` | — | — |
| `UnrecognisedFeatureType` | enumerator | `None` | — | — |
| `IncorrectRootElementName` | enumerator | `None` | — | — |
| `MissingVersionAttribute` | enumerator | `None` | — | — |
| `MalformedVersionAttribute` | enumerator | `None` | — | — |
| `PartiallySupportedVersionAttribute` | enumerator | `None` | — | — |
| `ParseError` | enumerator | `None` | — | — |
| `UnexpectedNonEmptyAttributeList` | enumerator | `None` | — | — |
| `DuplicateRasterBandName` | enumerator | `None` | — | — |
| `MismatchingRangeParametersSizeAndTupleSize` | enumerator | `None` | — | — |
| `GmapError` | enumerator | `None` | — | The following are specific to GMAP vgp files FIXME: This is a generic GmapError, we should add more field-specific errors. |
| `GmapFieldFormatError` | enumerator | `None` | — | — |
| `InvalidRegularCptLine` | enumerator | `None` | — | The following are specific to regular and categorical GMT CPT files. |
| `InvalidCategoricalCptLine` | enumerator | `None` | — | — |
| `CptSliceNotMonotonicallyIncreasing` | enumerator | `None` | — | — |
| `ColourModelChangedMidway` | enumerator | `None` | — | — |
| `NoLinesSuccessfullyParsed` | enumerator | `None` | — | — |
| `CptFileTypeNotDeduced` | enumerator | `None` | — | — |
| `UnrecognisedLabel` | enumerator | `None` | — | — |
| `PatternFillInLine` | enumerator | `None` | — | — |
| `HellingerPickFormatError` | enumerator | `None` | — | The following are specific to Hellinger-fit-related file formats. |
| `InvalidHellingerComFileFormat` | enumerator | `None` | — | — |
| `HellingerFileError` | enumerator | `None` | — | — |
| `ErrorOpeningFileForReading` | enumerator | `None` | — | The following are generic to all local files |
| `FileFormatNotSupported` | enumerator | `None` | — | — |
| `FileIsEmpty` | enumerator | `None` | — | — |
| `NoFeaturesFoundInFile` | enumerator | `None` | — | — |
| `ErrorReadingFile` | enumerator | `None` | — | — |

### `GPlatesFileIO::ReadErrors::Result`

| Member | Kind | Type | Access | Description |
|---|---|---|---|---|
| `EmptyCommentCreated` | enumerator | `None` | — | These are specific to PLATES rotation-format reading. |
| `ExclMarkInsertedAtCommentStart` | enumerator | `None` | — | — |
| `MovingPlateIdChangedToMatchEarlierSequence` | enumerator | `None` | — | — |
| `NewOverlappingSequenceBegun` | enumerator | `None` | — | — |
| `PoleDiscarded` | enumerator | `None` | — | — |
| `PoleAdjustedToShortRotationPathRelativeToPrevPole` | enumerator | `None` | — | — |
| `UnclassifiedFeatureCreated` | enumerator | `None` | — | The following are specific to PLATES line-format reading. |
| `FeatureDiscarded` | enumerator | `None` | — | — |
| `NoGeometryCreatedByMovement` | enumerator | `None` | — | — |
| `MultipleLayersIgnored` | enumerator | `None` | — | The following are specific to OGR-supported file format reading. |
| `GeometryFlattenedTo2D` | enumerator | `None` | — | — |
| `GeometryIgnored` | enumerator | `None` | — | — |
| `OnlyExteriorRingRead` | enumerator | `None` | — | — |
| `NoPlateIdLoadedForFile` | enumerator | `None` | — | TODO: I think we can remove NoPlateIdLoadedForFile, and its corresponding messages. |
| `NoPlateIdCreatedForFeature` | enumerator | `None` | — | — |
| `NoConjugatePlateIdCreatedForFeature` | enumerator | `None` | — | — |
| `NoLeftPlateIdCreatedForFeature` | enumerator | `None` | — | — |
| `NoRightPlateIdCreatedForFeature` | enumerator | `None` | — | — |
| `AttributeIgnored` | enumerator | `None` | — | — |
| `UnclassifiedOgrFeatureCreated` | enumerator | `None` | — | — |
| `FeatureIgnored` | enumerator | `None` | — | — |
| `NoRasterSetsLoaded` | enumerator | `None` | — | The following relate to time-dependent raster file sets. |
| `OnlyFirstRasterSetLoaded` | enumerator | `None` | — | — |
| `ElementIgnored` | enumerator | `None` | — | The following are specific to GPML reading. |
| `ParsingStoppedPrematurely` | enumerator | `None` | — | — |
| `ElementNameChanged` | enumerator | `None` | — | — |
| `ElementNotNameChanged` | enumerator | `None` | — | — |
| `AssumingCurrentVersion` | enumerator | `None` | — | — |
| `PropertyConvertedToTimeDependent` | enumerator | `None` | — | — |
| `PropertyConvertedFromTimeDependent` | enumerator | `None` | — | — |
| `PropertyConvertedBetweenTimeDependentTypes` | enumerator | `None` | — | — |
| `PropertyNotInterpreted` | enumerator | `None` | — | — |
| `AttributesIgnored` | enumerator | `None` | — | — |
| `GmapFeatureIgnored` | enumerator | `None` | — | The following are specific to GMAP vgp files |
| `CptLineIgnored` | enumerator | `None` | — | The following are specific to regular and categorical GMT CPT files. |
| `HellingerComFileNotImported` | enumerator | `None` | — | The following are specific to hellinger-fit-related files. |
| `HellingerPickIgnored` | enumerator | `None` | — | — |
| `HellingerFileNotOpened` | enumerator | `None` | — | — |
| `FileNotLoaded` | enumerator | `None` | — | The following are generic to all local files |
| `FileNotImported` | enumerator | `None` | — | — |
| `NoAction` | enumerator | `None` | — | — |

### `GPlatesFileIO::ReadErrors::Severity`

| Member | Kind | Type | Access | Description |
|---|---|---|---|---|
| `NothingWrong` | enumerator | `None` | — | — |
| `Warning` | enumerator | `None` | — | — |
| `RecoverableError` | enumerator | `None` | — | — |
| `TerminatingError` | enumerator | `None` | — | — |
| `FailureToBegin` | enumerator | `None` | — | — |

## Free functions and macros

| Name | Kind | Type / body | Description |
|---|---|---|---|
| `GPLATES_FILEIO_READERRORS_H` | macro | `None` | — |

## Notes

[[[PROSE notes unit=file-io/ReadErrors tier=1]]]
Replace this whole block, markers included, with invariants, ownership, threading or gotchas that are not visible in the tables. Write *None.* if there is nothing worth saying.
[[[/PROSE]]]

## Used by

| Unit | Component | References |
|---|---|---|
| [file-io/ReadErrorMessages](ReadErrorMessages.md) | file-io | 379 |
| [file-io/OgrReader](OgrReader.md) | file-io | 168 |
| [file-io/PlatesRotationFormatReader](PlatesRotationFormatReader.md) | file-io | 112 |
| [file-io/GpmlStructuralTypeReaderUtils](GpmlStructuralTypeReaderUtils.md) | file-io | 101 |
| [file-io/PlatesLineFormatReader](PlatesLineFormatReader.md) | file-io | 75 |
| [file-io/GpmlPropertyReader](GpmlPropertyReader.md) | file-io | 74 |
| [file-io/GpmlReaderUtils](GpmlReaderUtils.md) | file-io | 57 |
| [file-io/CptReader](CptReader.md) | file-io | 49 |
| [file-io/HellingerReader](HellingerReader.md) | file-io | 48 |
| [file-io/GpmlReader](GpmlReader.md) | file-io | 37 |
| [file-io/GdalRasterReader](GdalRasterReader.md) | file-io | 36 |
| [file-io/GpmlUpgradeReaderUtils](GpmlUpgradeReaderUtils.md) | file-io | 32 |
| [file-io/GmapReader](GmapReader.md) | file-io | 31 |
| [file-io/RgbaRasterReader](RgbaRasterReader.md) | file-io | 26 |
| [file-io/ReadErrorOccurrence](ReadErrorOccurrence.md) | file-io | 25 |
| [file-io/GpmlFeatureReaderImpl](GpmlFeatureReaderImpl.md) | file-io | 20 |
| [file-io/FeatureCollectionFileFormatRegistry](FeatureCollectionFileFormatRegistry.md) | file-io | 16 |
| [opengl/GLScalarField3DGenerator](../opengl/GLScalarField3DGenerator.md) | opengl | 15 |
| [file-io/ReadErrorAccumulation](ReadErrorAccumulation.md) | file-io | 12 |
| [file-io/GpmlPropertyStructuralTypeReaderUtils](GpmlPropertyStructuralTypeReaderUtils.md) | file-io | 11 |

*... and 14 more units.*

## Related

*None.*

## Explore

Run these from the `gplates-code` skill directory:

```bash
python scripts/gpq.py file src/file-io/ReadErrors.h
python scripts/gpq.py def GPlatesFileIO::ReadErrors::Description --body
python scripts/gpq.py uses Description --kind enum
```
