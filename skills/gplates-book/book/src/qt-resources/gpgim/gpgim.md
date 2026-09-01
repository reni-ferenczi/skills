# gpgim

[Book TOC](../../../TOC.md) · [qt-resources](../../../components/qt-resources.md) · tier 2

| Source file | Kind | Lines |
|---|---|---|
| `src/qt-resources/gpgim/gpgim.xml` | GPGIM | 3201 |
| `src/qt-resources/gpgim/gpgim.xsd` | GPGIM | 146 |
| `src/qt-resources/gpgim/gpgim.xsl` | GPGIM | 470 |
| `src/qt-resources/gpgim/timescales/ICC2012.xml` | GPGIM | 306 |
| `src/qt-resources/gpgim/units.xml` | GPGIM | 319 |

## Overview

[[[PROSE overview unit=qt-resources/gpgim tier=2]]]
Replace this whole block, markers included, with 1-3 paragraphs: what this unit is, why it exists, and how it fits the surrounding design. Do not restate the tables below.
[[[/PROSE]]]

## Declared types

*None.*

## Members

*None.*

## Free functions and macros

*None.*

## Notes

[[[PROSE notes unit=qt-resources/gpgim tier=2]]]
Replace this whole block, markers included, with invariants, ownership, threading or gotchas that are not visible in the tables. Write *None.* if there is nothing worth saying.
[[[/PROSE]]]

## Used by

*Nothing in the tree references this unit.*

## Related

**GPGIM feature types**

| Feature | Class | Inherits | Default geometry | Description |
|---|---|---|---|---|
| `gml:AbstractFeature` | abstract | — | — | An identifiable real-world object in a selected domain of discourse. |
| `gpml:AbsoluteReferenceFrame` | abstract | `gpml:TotalReconstructionSequence` | — | A means of describing the motion of plates over time, relative to a fixed point or frame. |
| `gpml:AbstractFeature` | abstract | `gml:AbstractFeature` | — | Highest-level abstract parent of all GPML Features. |
| `gpml:AbstractField` | abstract | `gpml:TangibleFeature` | `gpml:outlineOf` | Abstract superclass for various field data, including stand-alone Contours and outlines. |
| `gpml:AbstractGeologicalContact` | abstract | `gpml:AbstractGeologicalPlane` | — | Abstract base for all Geological Contacts. |
| `gpml:AbstractGeologicalPlane` | abstract | `gpml:TangibleFeature` | `gpml:centerLineOf` | Abstract base for all Geological Surface Planes, including Surfaces such as Bedding Surfaces, Cleavage, intangible planes such as Fold Plane, as well as Contacts and Faults. |
| `gpml:AbstractRockUnit` | abstract | `gpml:TangibleFeature` | — | Abstract base for all geological rock units. |
| `gpml:ArtificialFeature` | abstract | `gpml:ReconstructableFeature` | — | Abstract base for geometry that has been arbitrarily created, or possibly derived from a TangibleFeature. |
| `gpml:AseismicRidge` | concrete | `gpml:TangibleFeature` | `gpml:unclassifiedGeometry` | Miscellaneous inactive ridge feature. |
| `gpml:BasicRockUnit` | concrete | `gpml:AbstractRockUnit` | `gpml:outlineOf` | Basic definition of a geological rock unit. |
| `gpml:Basin` | concrete | `gpml:TangibleFeature` | `gpml:outlineOf` | Regional scale depression of erosional or structural origin. |
| `gpml:Bathymetry` | concrete | `gpml:AbstractField` | — | Sea floor depth data, including bathymetric contours and grids. |
| `gpml:ClosedContinentalBoundary` | concrete | `gpml:ArtificialFeature` | `gpml:boundary` | Rigid closed polygon continental crust boundary that can be reconstructed to any time. |
| `gpml:ClosedPlateBoundary` | concrete | `gpml:ArtificialFeature` | `gpml:boundary` | Rigid closed polygon plate boundary that can be reconstructed to any time. |
| `gpml:Coastline` | concrete | `gpml:TangibleFeature` | `gpml:centerLineOf` | Present day coastline. |
| `gpml:ContinentalCrust` | concrete | `gpml:TangibleFeature` | `gpml:outlineOf` | Continental Crust |
| `gpml:ContinentalFragment` | concrete | `gpml:TangibleFeature` | `gpml:outlineOf` | A fragment of continental crust that has become detached. |
| `gpml:ContinentalRift` | concrete | `gpml:TectonicSection` | — | A spreading rift on continental crust. |
| `gpml:Craton` | concrete | `gpml:TangibleFeature` | `gpml:outlineOf` | Large portion of a continental plate that has been relatively undisturbed since the Precambrian era and includes both shield and platform layers. |
| `gpml:CrustalThickness` | concrete | `gpml:AbstractField` | — | Crustal thickness data, typically represented using grids, related to Isopach data. |
| `gpml:DeformingRegionEdge` | concrete | `gpml:TangibleFeature` | `gpml:centerLineOf` | Edge of a deforming region that is not a plate boundary. |
| `gpml:DisplacementPoint` | concrete | `gpml:ReconstructableFeature` | `gpml:position` | A position used to build deforming regions. |
| `gpml:DynamicTopography` | concrete | `gpml:AbstractField` | — | Elevation differences caused by the flow within the Earth's mantle. |
| `gpml:ExtendedContinentalCrust` | concrete | `gpml:TangibleFeature` | `gpml:outlineOf` | Continental crust which has been pulled apart. |
| `gpml:Fault` | concrete | `gpml:AbstractGeologicalContact` | — | Fracture in a rock body along which observable relative displacement has occurred between adjacent blocks. |
| `gpml:FeatureCollectionMetadata` | concrete | `gpml:TangibleFeature` | — | Contains metadata which applies to the whole feature collection. |
| `gpml:Flowline` | concrete | `gpml:TimeVariantFeature` | `gpml:seedPoints` | Tracks plate motion away from spreading ridges over time using half-stage rotations. |
| `gpml:FoldPlane` | concrete | `gpml:AbstractGeologicalPlane` | — | Inferred plane of geological folding. |
| `gpml:FossilCollection_large` | concrete | `gpml:BasicRockUnit` | — | A collection of large fossils. |
| `gpml:FossilCollection_medium` | concrete | `gpml:BasicRockUnit` | — | A collection of medium fossils. |
| `gpml:FossilCollection_small` | concrete | `gpml:BasicRockUnit` | — | A collection of small fossils. |
| `gpml:FractureZone` | concrete | `gpml:TectonicSection` | — | Inactive fracture in the crust that was once part of a Transform boundary. |
| `gpml:FractureZoneIdentification` | concrete | `gpml:TangibleFeature` | `gpml:position` | Pick to identify fracture zone. |
| `gpml:GeologicalLineation` | concrete | `gpml:TangibleFeature` | `gpml:centerLineOf` | Undefined linear region. |
| `gpml:GeologicalPlane` | concrete | `gpml:AbstractGeologicalPlane` | — | Surface plane indicator based on rock unit observations, e.g. Bedding and Cleavage planes. |
| `gpml:GlobalElevation` | concrete | `gpml:AbstractField` | — | Merged bathymetric and topographic elevation data. |
| `gpml:Gravimetry` | concrete | `gpml:AbstractField` | — | Gravity grids, outlines, and contours. |
| `gpml:HeatFlow` | concrete | `gpml:AbstractField` | — | Oceanic heat-flow data. |
| `gpml:HotSpot` | concrete | `gpml:TangibleFeature` | `gpml:position` | Location in the mantle linked with high igneous activity. |
| `gpml:HotSpotTrail` | concrete | `gpml:TangibleFeature` | `gpml:unclassifiedGeometry` | Used to track the paleo-movement of HotSpots. |
| `gpml:InferredPaleoBoundary` | concrete | `gpml:ArtificialFeature` | `gpml:centerLineOf` | Part of a plate boundary defined by hand for real-world geology that no longer exists. |
| `gpml:IslandArc` | concrete | `gpml:TangibleFeature` | `gpml:outlineOf` | Type of volcanic arc formed by plate tectonics as an oceanic plate subducts under another and produces magma which rises to form the arc. |
| `gpml:Isochron` | concrete | `gpml:TangibleFeature` | `gpml:centerLineOf` | Line defining points of equal age for oceanic crust. |
| `gpml:LargeIgneousProvince` | concrete | `gpml:TangibleFeature` | `gpml:outlineOf` | An extensive region of basalts resulting from flood basalt volcanism. |
| `gpml:MagneticAnomalyIdentification` | concrete | `gpml:TangibleFeature` | `gpml:position` | Magnetic 'pick' from sea floor magnetism ship-track data. See also MagneticAnomalyLineation. |
| `gpml:MagneticAnomalyLineation` | concrete | `gpml:TangibleFeature` | `gpml:centerLineOf` | Magnetic 'lineation' picked based on magnetic grid data. See also MagneticAnomalyIdentification. |
| `gpml:MagneticAnomalyShipTrack` | concrete | `gpml:TangibleFeature` | `gpml:centerLineOf` | Ship Track data for Magnetic 'pick's. |
| `gpml:Magnetics` | concrete | `gpml:AbstractField` | — | Magnetic field feature for grid data and contours. |
| `gpml:MantleDensity` | concrete | `gpml:AbstractField` | — | Density of the mantle, computed using Seismic Tomography. |
| `gpml:MeshNode` | concrete | `gpml:ReconstructableFeature` | `gpml:meshPoints` | Global positions to calculate plate velocities at. |
| `gpml:MidOceanRidge` | concrete | `gpml:TectonicSection` | — | A spreading rift on oceanic crust. |
| `gpml:MotionPath` | concrete | `gpml:ReconstructableFeature` | `gpml:seedPoints` | Tracks absolute plate motion over time. |
| `gpml:NavdatSample` | abstract | `gpml:TangibleFeature` | `gpml:position` | Abstract base class representing a sample from the North American Volcanic and Intrusive Rock Database (NAVDAT). |
| `gpml:NavdatSampleFelsicHigh` | concrete | `gpml:NavdatSample` | — | A sample from the NAVDAT database with high felsic chemical composition. |
| `gpml:NavdatSampleFelsicLow` | concrete | `gpml:NavdatSample` | — | A sample from the NAVDAT database with low felsic chemical composition. |
| `gpml:NavdatSampleIntermediate` | concrete | `gpml:NavdatSample` | — | A sample from the NAVDAT database with chemical composition intermediate between mafic and felsic. |
| `gpml:NavdatSampleMafic` | concrete | `gpml:NavdatSample` | — | A sample from the NAVDAT database with mafic chemical composition. |
| `gpml:OceanDrillSite` | concrete | `gpml:TangibleFeature` | `gpml:position` | An feature to hold data related to a single dilling site. |
| `gpml:OceanicAge` | concrete | `gpml:AbstractField` | — | Age of seafloor, for contours and grids. |
| `gpml:OceanicCrust` | concrete | `gpml:TangibleFeature` | `gpml:outlineOf` | Oceanic Crust |
| `gpml:OldPlatesGridMark` | concrete | `gpml:ArtificialFeature` | `gpml:centerLineOf` | Backwards-compatibility with PLATES "GR" code. |
| `gpml:Ophiolite` | concrete | `gpml:TangibleFeature` | `gpml:outlineOf` | Uplifted oceanic crust attached to edges of continental plates. |
| `gpml:OrogenicBelt` | concrete | `gpml:TectonicSection` | — | A linear or arcuate zone on a regional scale which has undergone compressional tectonics. |
| `gpml:PassiveContinentalBoundary` | concrete | `gpml:TectonicSection` | — | Border line between oceanic and continental crust. |
| `gpml:Pluton` | concrete | `gpml:TangibleFeature` | — | A body of intrusive igneous rock. |
| `gpml:PoliticalBoundary` | concrete | `gpml:ArtificialFeature` | `gpml:outlineOf` | A political boundary. |
| `gpml:PolygonCentroidPoint` | concrete | `gpml:ReconstructableFeature` | `gpml:position` | To be deprecated. Previously used to mark interior rigid blocks of topological networks. Now all polygon interiors automatically become rigid blocks. |
| `gpml:PseudoFault` | concrete | `gpml:TangibleFeature` | `gpml:centerLineOf` | Fault-like contact caused by ridge propagation. |
| `gpml:Raster` | concrete | `gpml:AbstractFeature` | — | Generic multi-band, geo-referenced gridded image data. |
| `gpml:ReconstructableFeature` | abstract | `gpml:TimeVariantFeature` | — | Parent of all GPML Features we may want to associate with a plateId and are reconstructable. |
| `gpml:ReconstructionFeature` | abstract | `gpml:AbstractFeature` | — | Top-level abstract class that all rotations inherit from. |
| `gpml:RockUnit_carbonate` | concrete | `gpml:BasicRockUnit` | — | A carbonate rock unit. |
| `gpml:RockUnit_chemical` | concrete | `gpml:BasicRockUnit` | — | A chemical rock unit. |
| `gpml:RockUnit_evaporite` | concrete | `gpml:BasicRockUnit` | — | An evaporite rock unit. |
| `gpml:RockUnit_indeterminate_igneous` | concrete | `gpml:BasicRockUnit` | — | An indeterminate\_igneous rock unit. |
| `gpml:RockUnit_metamorphic` | concrete | `gpml:BasicRockUnit` | — | A metamorphic rock unit. |
| `gpml:RockUnit_organic` | concrete | `gpml:BasicRockUnit` | — | An organic rock unit. |
| `gpml:RockUnit_plutonic` | concrete | `gpml:BasicRockUnit` | — | A plutonic rock unit. |
| `gpml:RockUnit_siliciclastic` | concrete | `gpml:BasicRockUnit` | — | A siliciclastic rock unit. |
| `gpml:RockUnit_volcanic` | concrete | `gpml:BasicRockUnit` | — | A volcanic rock unit. |
| `gpml:Roughness` | concrete | `gpml:AbstractField` | — | Roughness data computed from Gravity grids. |
| `gpml:ScalarCoverage` | concrete | `gpml:TangibleFeature` | `gpml:domainSet` | Arbitrary surface scalar data represented by a scalar value at each point in a geometry. |
| `gpml:ScalarField3D` | concrete | `gpml:AbstractFeature` | — | Generic 3D field of scalar values representing arbitrary sub-surface data. |
| `gpml:Seamount` | concrete | `gpml:TangibleFeature` | `gpml:position` | Igneous cone-shaped mountain that is below sea level. |
| `gpml:SedimentThickness` | concrete | `gpml:AbstractField` | — | Isopach data indicating sediment thickness using grids and/or contours. |
| `gpml:SlabEdge` | concrete | `gpml:TangibleFeature` | `gpml:centerLineOf` | A slab edge. |
| `gpml:SmallCircle` | concrete | `gpml:ReconstructableFeature` | `gpml:centre` | A global position and small circle radius for small circle visualisations. |
| `gpml:SpreadingAsymmetry` | concrete | `gpml:AbstractField` | — | Asymmetry in sea-floor spreading rate. |
| `gpml:SpreadingRate` | concrete | `gpml:AbstractField` | — | Sea-floor spreading rate. |
| `gpml:StrainMarker` | concrete | `gpml:TangibleFeature` | `gpml:position` | Location on the surface to show stain data computed from interpolation via a Topologicl Network feature. |
| `gpml:Stress` | concrete | `gpml:AbstractField` | — | Stress grids and contour data. |
| `gpml:SubductionZone` | concrete | `gpml:TectonicSection` | — | A zone of descending lithospheric plate. |
| `gpml:Suture` | concrete | `gpml:TangibleFeature` | `gpml:centerLineOf` | Large scale structural feature associated with continental collision, separating crust that once belonged to two different plates. |
| `gpml:TangibleFeature` | abstract | `gpml:ReconstructableFeature` | — | Abstract base for real geological features (compare with 'ArtificalFeature'). |
| `gpml:TectonicSection` | concrete | `gpml:TangibleFeature` | `gpml:centerLineOf` | Superclass to group ridgelike and related tectonic features together. |
| `gpml:TerraneBoundary` | concrete | `gpml:AbstractGeologicalContact` | — | Regional scale miscellaneous contact line between two rock units. |
| `gpml:TimeVariantFeature` | abstract | `gpml:AbstractFeature` | — | Abstract base class for all features that have a valid time period (compared to instantaneous features). |
| `gpml:Topography` | concrete | `gpml:AbstractField` | — | Elevation data, including topographic contours and grids. |
| `gpml:TopologicalClosedPlateBoundary` | concrete | `gpml:TopologicalFeature` | `gpml:boundary` | A plate boundary formed by rubber-banding vertex lists, which are obtained by intersecting the geometry of other features. |
| `gpml:TopologicalFeature` | abstract | `gpml:TimeVariantFeature` | — | Abstract base class for features that topologically reference geometries from other features. |
| `gpml:TopologicalNetwork` | concrete | `gpml:TopologicalFeature` | `gpml:network` | A triangulated region inside a topological boundary, comprising internal constraint geometries and excluding interior polygons, used to calculate velocities in deforming regions. |
| `gpml:TopologicalSlabBoundary` | concrete | `gpml:TopologicalClosedPlateBoundary` | — | A topological closed boundary around a subducting slab. |
| `gpml:TotalReconstructionSequence` | concrete | `gpml:ReconstructionFeature` | — | A sequence of total reconstruction poles for a specific fixed/moving plate pair. |
| `gpml:Transform` | concrete | `gpml:TectonicSection` | — | Regional scale strike-slip plate boundary. |
| `gpml:TransitionalCrust` | concrete | `gpml:TangibleFeature` | `gpml:outlineOf` | Undefined region between continental crust and oceanic crust. |
| `gpml:Unconformity` | concrete | `gpml:AbstractGeologicalContact` | — | Surface of contact between two differing rock units. |
| `gpml:UnknownContact` | concrete | `gpml:AbstractGeologicalContact` | — | Regional scale unknown geological contact line. |
| `gpml:VirtualGeomagneticPole` | concrete | `gpml:TangibleFeature` | `gpml:polePosition` | Magnetic pole location consistent with the observed direction of remanence at a particular location. |
| `gpml:Volcano` | concrete | `gpml:TangibleFeature` | `gpml:position` | An opening in the crust, which allows magma to escape from below. |

**GPGIM property types**

| Property | Value types | Multiplicity | Description |
|---|---|---|---|
| `gml:description` | `xsi:string` | 0..1 | A description of the feature. |
| `gml:name` | `xsi:string` | 0..* | A descriptive name of the feature. |
| `gml:validTime` | `gml:TimePeriod` | 0..1 | The period of time the feature is in existence. |
| `gpml:absoluteReferenceFrame` | `gpml:AbsoluteReferenceFrameEnumeration` | 1 | Type of absolute reference frame. |
| `gpml:age` | `gpml:Age` | 0..1 | Geological age of the Feature. |
| `gpml:ageOfAccretion` | `gpml:Age` | 0..1 | Geological age that this feature was accreted onto its current crust. |
| `gpml:angularRadius` | `gpml:measure` | 1 | Angular radius. |
| `gpml:anomalyIdentificationConfidence` | `gpml:AnomalyIdentificationConfidenceRating` | 0..1 | Confidence rating for the identification of the 'end' that the anomaly was picked at, based on the data source. |
| `gpml:averageAge` | `xsi:double` | 1 | Average magnetisation age (GeologicalTime of magnetisation) based on multiple sites. |
| `gpml:averageDeclination` | `xsi:double` | 0..1 | Average direction in stratigraphic coordinates, declination. |
| `gpml:averageInclination` | `xsi:double` | 0..1 | Average direction in stratigraphic coordinates, inclination. |
| `gpml:averageSampleSitePosition` | `gml:Point` | 0..1 | Average sample-site position (based on multiple sites). |
| `gpml:bandNames` | `gpml:RasterBandNames` | 1 | The names of the raster bands in a raster. |
| `gpml:boundary` | `gml:Polygon, gpml:TopologicalPolygon, gml:OrientableCurve, gml:LineString` | 0..* | A static or topological (plate) boundary depending on the feature type. |
| `gpml:boundaryCoverage` | `gml:DataBlock` | 0..1 | Coverage (per-point scalar values) corresponding to a 'gpml:boundary' geometry. |
| `gpml:centerLineOf` | `gml:Point, gml:OrientableCurve, gml:LineString, gml:MultiPoint, gml:Polygon, gpml:TopologicalLine` | 0..* | The central line defining the feature's geometry. |
| `gpml:centerLineOfCoverage` | `gml:DataBlock` | 0..* | Coverage (per-point scalar values) corresponding to a 'gpml:centerLineOf' geometry. |
| `gpml:centre` | `gml:Point` | 1 | Centre of a small circle. |
| `gpml:conjugate` | `gpml:FeatureReference` | 0..* | A reference to the 'pair' or 'twin' of the isochron. |
| `gpml:conjugatePlateId` | `gpml:plateId` | 0..* | A reference to the plate Id that has the 'pair' or 'twin' of the feature. |
| `gpml:coreData` | `xsi:string` | 0..1 | A URL for Core Data |
| `gpml:coreRecovered` | `xsi:double` | 0..1 | Length of Core Recovered in meters. |
| `gpml:crust` | `gpml:ContinentalBoundaryCrustEnumeration` | 0..1 | The type of the crust contained within a boundary. |
| `gpml:dataDictionary` | `gpml:KeyValueDictionary` | 0..* | A set of data, stored as KeyValueDictionary: 'key=value' pairs: key1=value1, key2=value2, key3=value3, etc. |
| `gpml:dataSeries` | `xsi:string` | 0..* | A series of data, as 'datum=value' pairs in simple text string form: 'data1=value1, datum2=value2, dataum3=value3', etc. |
| `gpml:depthToBasement` | `xsi:double` | 0..1 | Depth to basement rock at the sample site. |
| `gpml:dipAngle` | `gpml:measure` | 0..1 | Used to describe the angle a surface "dips" from the horizontal, usually in degrees. |
| `gpml:dipSide` | `gpml:DipSideEnumeration` | 0..1 | Used to specify the dip direction of the plane. |
| `gpml:dipSlip` | `gpml:DipSlipEnumeration` | 0..1 | The motion along the 'dip', or cross-section line of the Fault. |
| `gpml:doi` | `xsi:string` | 0..* | Digital Object Identifier, can be looked up via http://www.doi.org/. |
| `gpml:domainSet` | `gml:Point, gml:OrientableCurve, gml:LineString, gml:MultiPoint, gml:Polygon, gml:RectifiedGrid` | 1 | The region-of-interest of a coverage or raster on which the corresponding 'gpml:rangeSet' is based. |
| `gpml:edge` | `gpml:ContinentalBoundaryEdgeEnumeration` | 0..1 | Enumerates whether a continental boundary is the inner or outer boundary in the broad area of change between continental and oceanic crust. |
| `gpml:errorBounds` | `gml:Point, gml:OrientableCurve, gml:LineString, gml:MultiPoint, gml:Polygon, gpml:TopologicalPolygon` | 0..* | An optional error boundary for the feature. |
| `gpml:evidence` | `gpml:FeatureReference` | 0..* | Features listed as evidence of the HotSpotTrail. |
| `gpml:expedition` | `xsi:string` | 0..1 | The name or identifer of the Expedition related to this feature |
| `gpml:file` | `gpml:ScalarField3DFile` | 1 | Type of annotation for a FoldPlane. Appears as symbols along the line of the fold. |
| `gpml:fixedReferenceFrame` | `gpml:plateId` | 1 | The plate Id for which motion is treated as 'fixed'. |
| `gpml:foldAnnotation` | `gpml:FoldPlaneAnnotationEnumeration` | 0..1 | Type of annotation for a FoldPlane. Appears as symbols along the line of the fold. |
| `gpml:geometryImportTime` | `gml:TimeInstant` | 0..1 | The geological time that the feature's geometry was imported. |
| `gpml:hole` | `xsi:string` | 0..1 | The identifer for the drill hole |
| `gpml:identificationMethod` | `xsi:string` | 0..* | Method used for identifying this Feature or its characteristics. |
| `gpml:initialReportVolume` | `xsi:string` | 0..1 | URL for the drill hole data |
| `gpml:isActive` | `xsi:boolean` | 0..1 | Time-dependent boolean indicates when the feature is active over time. |
| `gpml:islandArc` | `gpml:FeatureReference` | 0..* | Multiple small island arcs potentially forming part of a large subduction zone. |
| `gpml:leftPlate` | `gpml:plateId` | 0..1 | Annotation property describing the plate on the "left" side of the feature. |
| `gpml:leftUnit` | `gpml:FeatureReference` | 0..1 | Defines what is on the "Left" side of the contact, using an AbstractRockUnit. |
| `gpml:locationNames` | `gpml:StringList` | 0..1 | List of location, dredge or drill site names. |
| `gpml:logData` | `xsi:string` | 0..1 | A URL for Log Data |
| `gpml:mark` | `gpml:HotSpotTrailMark` | 1..* | Forms a table of hotspot position and age, using HotSpotTrailMark to represent each row. |
| `gpml:meshPoints` | `gml:Point, gml:MultiPoint` | 1 | Global positions to calculate plate velocities at. |
| `gpml:meshPointsCoverage` | `gml:DataBlock` | 0..1 | Coverage (per-point scalar values) corresponding to a 'gpml:meshPoints' geometry. |
| `gpml:metadata` | `gpml:GpmlMetadata` | 0..1 | The metadata for feature collection. |
| `gpml:motion` | `gpml:StrikeSlipEnumeration` | 0..1 | The motion along the 'strike', or map-view line of the Transform. |
| `gpml:movingReferenceFrame` | `gpml:plateId` | 1 | The 'conjugate' or 'moving' plate Id. |
| `gpml:mprsAttributes` | `gpml:KeyValueDictionary` | 0..1 | Moving Plate Rotation Sequence attributes. |
| `gpml:multiPosition` | `gml:MultiPoint` | 0..1 | When a feature’s geometry is described as a multiple points, it is appropriate to use the MultiPoint geometry. |
| `gpml:multiPositionCoverage` | `gml:DataBlock` | 0..1 | Coverage (per-point scalar values) corresponding to a 'gpml:multiPosition' geometry. |
| `gpml:network` | `gpml:TopologicalNetwork, gml:Polygon` | 1 | A topological network used to define a deforming region. |
| `gpml:oldPlatesHeader` | `gpml:OldPlatesHeader` | 0..1 | Metadata imported from a PLATES data file. |
| `gpml:outlineOf` | `gml:Point, gml:OrientableCurve, gml:LineString, gml:MultiPoint, gml:Polygon, gpml:TopologicalPolygon` | 0..* | Geometry specifying a closed or partial outline. |
| `gpml:outlineOfCoverage` | `gml:DataBlock` | 0..* | Coverage (per-point scalar values) corresponding to a 'gpml:outlineOf' geometry. |
| `gpml:pick` | `gpml:FeatureReference` | 0..* | An (optional) reference to the MagneticAnomalyIdentification s recorded from this ship track data. |
| `gpml:polarityChronId` | `gpml:PolarityChronId` | 0..1 | The string name of the polarity chron based on the geomagnetic reversal timescale. |
| `gpml:polarityChronOffset` | `xsi:double` | 0..1 | Specifies the location on the polarity chron, from youngest to oldest. |
| `gpml:polarityChronOrientation` | `gpml:MagneticOrientationEnumeration` | 0..1 | Specifies the magnetic orientation of the chron, normal or reverse. |
| `gpml:poleA95` | `xsi:double` | 0..1 | Error circle based on uncertainty of the average of pole positions. |
| `gpml:poleDm` | `xsi:double` | 0..1 | VGP uncertainty, meridian. |
| `gpml:poleDp` | `xsi:double` | 0..1 | VGP uncertainty, parallel latitude. |
| `gpml:polePosition` | `gml:Point` | 0..1 | Virtual geomagnetic pole. |
| `gpml:position` | `gml:Point` | 0..1 | When a feature’s geometry is described as a point, it is appropriate to use the Point geometry. |
| `gpml:primarySlipComponent` | `gpml:SlipComponentEnumeration` | 0..1 | For Faults with both Dip-Slip and Strike-Slip motion (sometimes termed "Oblique Slip"), this property indicates which of Dip-Slip or Strike-Slip is the primary component of the motion, if any. |
| `gpml:program` | `xsi:string` | 0..* | An identifer for the scientific Program related to this feature |
| `gpml:publication` | `xsi:string` | 0..* | An identifer for publications related to this feature |
| `gpml:quality` | `gpml:DataQualityEnumeration` | 0..1 | Quality of source data; e.g. are both flanks preserved for Isochrons? are they Synthetic Isochrons? |
| `gpml:rangeSet` | `gml:DataBlock, gml:File` | 1 | The coverage or raster values at the corresponding 'gpml:domainSet' region-of-interest. |
| `gpml:reconstructionMethod` | `gpml:ReconstructionMethodEnumeration` | 0..1 | The method used to reconstruct feature geometry to paleo times. |
| `gpml:reconstructionPlateId` | `gpml:plateId` | 0..1 | The plateID that will be used for reconstruction purposes. |
| `gpml:reference` | `xsi:string` | 0..* | External reference related to this feature e.g. journal citation, name of a published paper. |
| `gpml:relativePlate` | `gpml:plateId` | 1 | The plate that something is relative to. |
| `gpml:rheaFault` | `xsi:string` | 0..1 | Rhea fault. |
| `gpml:riftEdgeLengthThresholdDegrees` | `xsi:double` | 0..1 | Rift edges in network triangulation shorter than this length, in degrees, will not be further sub-divided. |
| `gpml:riftExponentialStretchingConstant` | `xsi:double` | 0..1 | Controls exponential variation of stretching across rift profile in network triangulation. |
| `gpml:riftLeftPlate` | `gpml:plateId` | 0..1 | One of the two conjugate rigid plates bounding a rift topological network. |
| `gpml:riftRightPlate` | `gpml:plateId` | 0..1 | One of the two conjugate rigid plates bounding a rift topological network. |
| `gpml:riftStrainRateResolutionLog10` | `xsi:double` | 0..1 | Rift edges in network triangulation are sub-divided until strain rate matches exponential curve within this tolerance (10^resolution, in units of 1/second). |
| `gpml:rightPlate` | `gpml:plateId` | 0..1 | Annotation property describing the plate on the "right" side of the feature. |
| `gpml:rightUnit` | `gpml:FeatureReference` | 0..1 | Defines what is on the "Right" side of the contact, using an AbstractRockUnit. |
| `gpml:sedimentThickness` | `xsi:double` | 0..1 | Sediment Thickness at the sample site. |
| `gpml:seedPoints` | `gml:Point, gml:MultiPoint` | 1 | The points from which the Flowline and MotionPath time-paths are generated. |
| `gpml:shapefileAttributes` | `gpml:KeyValueDictionary` | 0..1 | Attribute data imported from a Shapefile data file. |
| `gpml:shipTrack` | `gpml:FeatureReference` | 0..1 | Optional reference to the MagneticAnomalyShipTrack that this pick originates from. |
| `gpml:shipTrackName` | `xsi:string` | 0..1 | Optional text string referencing some ship track or cruise name (not necessarily a MagneticAnomalyShipTrack) that this pick originates from. For example, this could be an NGDC ID. |
| `gpml:side` | `gpml:ContinentalBoundarySideEnumeration` | 0..1 | Indicates which direction leads to the continental crust. |
| `gpml:site` | `xsi:string` | 0..1 | Site name for this feature |
| `gpml:slabEdgeType` | `xsi:string` | 0..1 | The type of slab edge. |
| `gpml:slabFlatLying` | `xsi:boolean` | 0..1 | Whether the slab is flat lying or not. |
| `gpml:slabFlatLyingDepth` | `xsi:double` | 0..1 | The slab flat lying depth. |
| `gpml:spreadingAsymmetry` | `xsi:double` | 0..1 | The asymmetry of ridge spreading, in the range \[-1,1\], where the value 0 represents symmetric (half-stage) rotation, the value -1 represents zero stage rotation (left plate) and the value 1 represents full-stage rotation (right plate). |
| `gpml:strikeSlip` | `gpml:StrikeSlipEnumeration` | 0..1 | The motion along the 'strike', or map-view line of the Fault. |
| `gpml:subcategory` | `xsi:string` | 0..* | A free-form text string to optionally assign one or more subcategories to a feature type. |
| `gpml:subductionPolarity` | `gpml:SubductionPolarityEnumeration` | 0..1 | Indicates which side of the line (when following the vertices in order) that the over-riding plate is on. |
| `gpml:subductionZoneAge` | `xsi:double` | 0..1 | Age of subduction zone. |
| `gpml:subductionZoneConvergence` | `xsi:double` | 0..1 | Convergence rate of subduction zone in cm/year. |
| `gpml:subductionZoneDeepDip` | `xsi:double` | 0..1 | Subduction zone deep dig. |
| `gpml:subductionZoneDepth` | `xsi:double` | 0..1 | Subduction zone depth. |
| `gpml:subductionZoneSystem` | `xsi:string` | 0..1 | A unique name for a collection of Subduction Zones forming a continuous system of subduction. |
| `gpml:subductionZoneSystemOrder` | `xsi:integer` | 0..1 | The order where this subduction zone appears in the system (note: this is zero-based sequence) |
| `gpml:supersededRevision` | `gpml:revisionId` | 0..* | Lists all revisions of this feature that were superseded by this one. |
| `gpml:times` | — | 1 | An array of time instants. |
| `gpml:totalReconstructionPole` | `gpml:FiniteRotation` | 1 | A sequence of FiniteRotations and associated gml:TimeInstants, with FiniteRotationSlerp interpolation between them. |
| `gpml:trail` | `gpml:FeatureReference` | 0..* | HotSpots can be associated with zero, one, or more HotSpotTrails. |
| `gpml:truncatedSection` | `gpml:FeatureReference` | 0..* | Optional references to other Features that the user has indicated are supposed to be the same feature. |
| `gpml:unclassifiedGeometry` | `gml:Point, gml:OrientableCurve, gml:LineString, gml:MultiPoint, gml:Polygon, gpml:TopologicalLine, gpml:TopologicalPolygon` | 0..* | All geometry defined for the feature where the purpose is not given or is unclear. |
| `gpml:unclassifiedGeometryCoverage` | `gml:DataBlock` | 0..* | Coverage (per-point scalar values) corresponding to a 'gpml:unclassifiedGeometry' geometry. |
| `gpml:waterDepth` | `xsi:double` | 0..1 | Water Depth in meters at the sample site. |


## Explore

Run these from the `gplates-code` skill directory:

```bash
python scripts/gpq.py file src/qt-resources/gpgim/gpgim.xml
python scripts/gpq.py gpgim Isochron
```
