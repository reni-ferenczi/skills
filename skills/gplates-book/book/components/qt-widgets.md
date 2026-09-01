# qt-widgets

[Book TOC](../TOC.md)

239 unit page(s), 627 source file(s) documented here, 5 further file(s) listed below.

## Overview

[[[PROSE component unit=component:qt-widgets tier=1]]]
Replace this whole block, markers included, with 2-4 paragraphs: what this component is responsible for, the load-bearing units and how it connects to neighbouring components. Do not restate the unit table.
[[[/PROSE]]]

## Units

### `src/qt-widgets`

#### Choose

| Unit | Tier | Lines | Fan-in | Description |
|---|---|---|---|---|
| [ChooseBuiltinPaletteDialog](../src/qt-widgets/ChooseBuiltinPaletteDialog.md) | 3 | 1522 | 1 | Dialog for browsing and selecting from built-in color palettes organized by type |
| [ChooseColourButton](../src/qt-widgets/ChooseColourButton.md) | 2 | 165 | 33 | (pending) |
| [ChooseFeatureCollectionDialog](../src/qt-widgets/ChooseFeatureCollectionDialog.md) | 3 | 301 | 1 | Dialog wrapper for selecting a feature collection file with optional new collection creation |
| [ChooseFeatureCollectionWidget](../src/qt-widgets/ChooseFeatureCollectionWidget.md) | 2 | 542 | 100 | (pending) |
| [ChooseFeatureTypeWidget](../src/qt-widgets/ChooseFeatureTypeWidget.md) | 3 | 320 | 9 | Selection widget for choosing a feature type from GPGIM, optionally filtered by property type |
| [ChooseFontButton](../src/qt-widgets/ChooseFontButton.md) | 3 | 141 | 3 | Tool button for selecting a font and visually previewing the selected font family |
| [ChoosePropertyWidget](../src/qt-widgets/ChoosePropertyWidget.md) | 3 | 389 | 11 | Selection widget for choosing a property name constrained by feature type and property type |

#### Co

| Unit | Tier | Lines | Fan-in | Description |
|---|---|---|---|---|
| [CoRegistrationLayerConfigurationDialog](../src/qt-widgets/CoRegistrationLayerConfigurationDialog.md) | 3 | 2114 | 6 | Configuration dialog for co-registration layers that perform data mining on geometries and rasters |
| [CoRegistrationOptionsWidget](../src/qt-widgets/CoRegistrationOptionsWidget.md) | 3 | 277 | 1 | Options widget for co-registration layers in the visual layers panel |
| [CoRegistrationResultTableDialog](../src/qt-widgets/CoRegistrationResultTableDialog.md) | 3 | 560 | 2 | Dialog displaying co-registration computation results in a table |

#### Configure

| Unit | Tier | Lines | Fan-in | Description |
|---|---|---|---|---|
| [ConfigureCanvasToolGeometryRenderParametersDialog](../src/qt-widgets/ConfigureCanvasToolGeometryRenderParametersDialog.md) | 3 | 957 | 0 | Dialog for configuring visual appearance of canvas tool geometries |
| [ConfigureExportParametersDialog](../src/qt-widgets/ConfigureExportParametersDialog.md) | 2 | 1008 | 45 | (pending) |
| [ConfigureGraticulesDialog](../src/qt-widgets/ConfigureGraticulesDialog.md) | 3 | 360 | 9 | Dialog for configuring latitude/longitude grid appearance |
| [ConfigureTextOverlayDialog](../src/qt-widgets/ConfigureTextOverlayDialog.md) | 3 | 467 | 0 | Dialog for configuring text overlay appearance on globe or map |
| [ConfigureVelocityLegendOverlayDialog](../src/qt-widgets/ConfigureVelocityLegendOverlayDialog.md) | 3 | 840 | 0 | Dialog for configuring velocity legend overlay appearance on the map |

#### Create

| Unit | Tier | Lines | Fan-in | Description |
|---|---|---|---|---|
| [CreateFeatureAddOrEditPropertyDialog](../src/qt-widgets/CreateFeatureAddOrEditPropertyDialog.md) | 2 | 721 | 22 | (pending) |
| [CreateFeatureDialog](../src/qt-widgets/CreateFeatureDialog.md) | 2 | 3446 | 43 | (pending) |
| [CreateFeaturePropertiesPage](../src/qt-widgets/CreateFeaturePropertiesPage.md) | 3 | 1198 | 7 | Wizard page for adding properties to new features with GPGIM schema validation |
| [CreateSmallCircleDialog](../src/qt-widgets/CreateSmallCircleDialog.md) | 2 | 910 | 14 | (pending) |
| [CreateSmallCircleFeatureDialog](../src/qt-widgets/CreateSmallCircleFeatureDialog.md) | 3 | 600 | 19 | Multi-page wizard for creating features from small circles |
| [CreateTotalReconstructionSequenceDialog](../src/qt-widgets/CreateTotalReconstructionSequenceDialog.md) | 3 | 513 | 7 | Multi-page wizard for creating TotalReconstructionSequence features |
| [CreateVGPDialog](../src/qt-widgets/CreateVGPDialog.md) | 3 | 967 | 0 | Multi-page dialog for creating Virtual Geomagnetic Pole features |

#### Edit

| Unit | Tier | Lines | Fan-in | Description |
|---|---|---|---|---|
| [EditAffineTransformGeoreferencingWidget](../src/qt-widgets/EditAffineTransformGeoreferencingWidget.md) | 2 | 1213 | 19 | (pending) |
| [EditAgeWidget](../src/qt-widgets/EditAgeWidget.md) | 3 | 871 | 2 | Edit widget for composing GpmlAge property values |
| [EditAngleWidget](../src/qt-widgets/EditAngleWidget.md) | 3 | 254 | 2 | Edit widget for composing GpmlMeasure angle property values |
| [EditBooleanWidget](../src/qt-widgets/EditBooleanWidget.md) | 3 | 251 | 2 | Qt widget for editing boolean property values with a True/False combo box |
| [EditDoubleWidget](../src/qt-widgets/EditDoubleWidget.md) | 3 | 240 | 2 | Qt widget for editing double-precision floating-point property values |
| [EditEnumerationWidget](../src/qt-widgets/EditEnumerationWidget.md) | 3 | 369 | 2 | Qt widget for editing enumeration property values of multiple types configured via GPGIM |
| [EditExportParametersDialog](../src/qt-widgets/EditExportParametersDialog.md) | 3 | 483 | 2 | Dialog for editing export animation parameters including filename template and format options |
| [EditFeaturePropertiesWidget](../src/qt-widgets/EditFeaturePropertiesWidget.md) | 3 | 530 | 6 | Widget presenting a feature's properties in a table and allowing one-at-a-time editing |
| [EditGeometryWidget](../src/qt-widgets/EditGeometryWidget.md) | 2 | 1557 | 113 | (pending) |
| [EditIntegerWidget](../src/qt-widgets/EditIntegerWidget.md) | 3 | 238 | 2 | Qt widget for editing integer property values via spin box |
| [EditOldPlatesHeaderWidget](../src/qt-widgets/EditOldPlatesHeaderWidget.md) | 3 | 733 | 2 | Qt widget for editing GpmlOldPlatesHeader property values from old PLATES format polygon files |
| [EditPlateIdWidget](../src/qt-widgets/EditPlateIdWidget.md) | 3 | 379 | 14 | Qt widget for editing plate ID values with optional null support for optional properties |
| [EditPolarityChronIdWidget](../src/qt-widgets/EditPolarityChronIdWidget.md) | 3 | 301 | 2 | Editor widget for magnetic polarity chron identification data with era, major and minor region fields |
| [EditShapefileAttributesWidget](../src/qt-widgets/EditShapefileAttributesWidget.md) | 3 | 529 | 2 | Editor for shapefile attributes stored as key-value pairs with typed values |
| [EditStringListWidget](../src/qt-widgets/EditStringListWidget.md) | 3 | 932 | 2 | Editor for ordered sequences of strings with insert, delete, and append operations |
| [EditStringWidget](../src/qt-widgets/EditStringWidget.md) | 3 | 282 | 5 | Simple editor for XML schema string values |
| [EditTableActionWidget](../src/qt-widgets/EditTableActionWidget.md) | 2 | 258 | 70 | (pending) |
| [EditTableWidget](../src/qt-widgets/EditTableWidget.md) | 3 | 65 | 6 | Abstract interface for table-editing widgets handling row insertion and deletion |
| [EditTimeInstantWidget](../src/qt-widgets/EditTimeInstantWidget.md) | 3 | 262 | 2 | Editor for geological time instants as double values in millions of years |
| [EditTimePeriodWidget](../src/qt-widgets/EditTimePeriodWidget.md) | 2 | 722 | 13 | (pending) |
| [EditTimeSequenceWidget](../src/qt-widgets/EditTimeSequenceWidget.md) | 3 | 1667 | 3 | Editor for time period arrays displayed as flat sequences of time samples with auto-sorting and duplicate removal |
| [EditTotalReconstructionSequenceDialog](../src/qt-widgets/EditTotalReconstructionSequenceDialog.md) | 3 | 395 | 1 | Modal dialog for editing a single total reconstruction sequence feature and its plate IDs |
| [EditTotalReconstructionSequenceWidget](../src/qt-widgets/EditTotalReconstructionSequenceWidget.md) | 2 | 1620 | 12 | (pending) |
| [EditWidgetChooser](../src/qt-widgets/EditWidgetChooser.md) | 3 | 485 | 2 | Feature visitor that dispatches property values to appropriate editing widgets |
| [EditWidgetGroupBox](../src/qt-widgets/EditWidgetGroupBox.md) | 2 | 1268 | 64 | (pending) |

#### Export

| Unit | Tier | Lines | Fan-in | Description |
|---|---|---|---|---|
| [ExportAnimationDialog](../src/qt-widgets/ExportAnimationDialog.md) | 2 | 2044 | 15 | (pending) |
| [ExportCitcomsResolvedTopologyOptionsWidget](../src/qt-widgets/ExportCitcomsResolvedTopologyOptionsWidget.md) | 3 | 690 | 4 | Options panel for exporting resolved topology in CitcomS format |
| [ExportCoordinatesDialog](../src/qt-widgets/ExportCoordinatesDialog.md) | 3 | 1124 | 0 | Dialog for exporting a single geometry to coordinate files in various formats |
| [ExportDeformationOptionsWidget](../src/qt-widgets/ExportDeformationOptionsWidget.md) | 3 | 837 | 2 | Options panel for exporting deformation data such as strain and strain rates |
| [ExportFileNameTemplateWidget](../src/qt-widgets/ExportFileNameTemplateWidget.md) | 3 | 383 | 8 | Widget for editing filename templates used in batch exports with placeholder tokens |
| [ExportFileOptionsWidget](../src/qt-widgets/ExportFileOptionsWidget.md) | 3 | 246 | 10 | Reusable widget for controlling single vs. multiple file export output |
| [ExportFlowlineOptionsWidget](../src/qt-widgets/ExportFlowlineOptionsWidget.md) | 3 | 131 | 4 | Options panel for exporting flowlines with dateline and file output controls |
| [ExportImageOptionsWidget](../src/qt-widgets/ExportImageOptionsWidget.md) | 3 | 155 | 1 | Widget for collecting and managing image export options when exporting screenshots |
| [ExportImageResolutionOptionsWidget](../src/qt-widgets/ExportImageResolutionOptionsWidget.md) | 3 | 457 | 6 | Form widget for specifying image resolution and dimensions |
| [ExportMotionPathOptionsWidget](../src/qt-widgets/ExportMotionPathOptionsWidget.md) | 3 | 131 | 4 | Widget for collecting export options when exporting motion paths |
| [ExportNetRotationOptionsWidget](../src/qt-widgets/ExportNetRotationOptionsWidget.md) | 3 | 123 | 3 | Widget for collecting velocity method and delta time settings for net rotation export |
| [ExportOptionsWidget](../src/qt-widgets/ExportOptionsWidget.md) | 2 | 68 | 56 | (pending) |
| [ExportRasterOptionsWidget](../src/qt-widgets/ExportRasterOptionsWidget.md) | 3 | 1060 | 2 | Form widget for raster export resolution, geographic extents, and compression |
| [ExportReconstructedGeometryOptionsWidget](../src/qt-widgets/ExportReconstructedGeometryOptionsWidget.md) | 3 | 130 | 4 | Widget for collecting export options when exporting reconstructed geometries |
| [ExportResolvedTopologyOptionsWidget](../src/qt-widgets/ExportResolvedTopologyOptionsWidget.md) | 3 | 656 | 4 | Form widget for resolved topology export with type selection and polygon orientation |
| [ExportRotationOptionsWidget](../src/qt-widgets/ExportRotationOptionsWidget.md) | 3 | 287 | 4 | Sub-widget for common rotation export format options shared by exporters |
| [ExportScalarCoverageOptionsWidget](../src/qt-widgets/ExportScalarCoverageOptionsWidget.md) | 3 | 563 | 2 | User interface for configuring scalar coverage export options across GPML and GMT formats with optional deformation measures |
| [ExportStageRotationOnlyOptionsWidget](../src/qt-widgets/ExportStageRotationOnlyOptionsWidget.md) | 3 | 220 | 2 | Sub-widget for configuring stage-rotation-specific export parameters |
| [ExportStageRotationOptionsWidget](../src/qt-widgets/ExportStageRotationOptionsWidget.md) | 3 | 129 | 6 | Container widget combining rotation and stage-rotation-specific export options |
| [ExportSvgOptionsWidget](../src/qt-widgets/ExportSvgOptionsWidget.md) | 3 | 155 | 1 | User interface for configuring SVG export options with image resolution settings |
| [ExportTotalRotationOptionsWidget](../src/qt-widgets/ExportTotalRotationOptionsWidget.md) | 3 | 115 | 6 | Container widget for total rotation export options |
| [ExportVelocityCalculationOptionsWidget](../src/qt-widgets/ExportVelocityCalculationOptionsWidget.md) | 3 | 529 | 1 | Sub-widget for configuring velocity delta-time and boundary smoothing parameters |
| [ExportVelocityOptionsWidget](../src/qt-widgets/ExportVelocityOptionsWidget.md) | 3 | 1406 | 4 | User interface for velocity export with support for GPML, GMT, Terra, and CitcomS formats |

#### Generate

| Unit | Tier | Lines | Fan-in | Description |
|---|---|---|---|---|
| [GenerateDeformingMeshPointsDialog](../src/qt-widgets/GenerateDeformingMeshPointsDialog.md) | 3 | 1867 | 0 | Wizard dialog for generating mesh points with crustal thickness properties |
| [GenerateVelocityDomainCitcomsDialog](../src/qt-widgets/GenerateVelocityDomainCitcomsDialog.md) | 3 | 757 | 0 | Dialog for generating CitcomS velocity domain mesh on a cube sphere |
| [GenerateVelocityDomainLatLonDialog](../src/qt-widgets/GenerateVelocityDomainLatLonDialog.md) | 3 | 1354 | 0 | Dialog for generating velocity domain points on a regular latitude/longitude grid |
| [GenerateVelocityDomainTerraDialog](../src/qt-widgets/GenerateVelocityDomainTerraDialog.md) | 3 | 1120 | 0 | Dialog for generating velocity domain points using the Terra icosahedral gridding library with configurable parameters |

#### Hellinger

| Unit | Tier | Lines | Fan-in | Description |
|---|---|---|---|---|
| [HellingerConfigurationDialog](../src/qt-widgets/HellingerConfigurationDialog.md) | 3 | 302 | 9 | Settings dialog for customizing visual appearance of Hellinger pole and ellipse visualization |
| [HellingerConfigurationWidget](../src/qt-widgets/HellingerConfigurationWidget.md) | 2 | 497 | 60 | (pending) |
| [HellingerDialog](../src/qt-widgets/HellingerDialog.md) | 2 | 3272 | 224 | (pending) |
| [HellingerFitWidget](../src/qt-widgets/HellingerFitWidget.md) | 2 | 2114 | 25 | (pending) |
| [HellingerModel](../src/qt-widgets/HellingerModel.md) | 1 | 1198 | 614 | (pending) |
| [HellingerNewSegmentWarning](../src/qt-widgets/HellingerNewSegmentWarning.md) | 3 | 364 | 10 | Dialog prompting user choice when creating a segment with an existing segment number |
| [HellingerPickWidget](../src/qt-widgets/HellingerPickWidget.md) | 3 | 1540 | 8 | Tree widget for displaying and managing Hellinger picks organized by segments |
| [HellingerPointDialog](../src/qt-widgets/HellingerPointDialog.md) | 3 | 646 | 11 | Modal dialog for creating or editing a single Hellinger pick with coordinates and metadata |
| [HellingerSegmentDialog](../src/qt-widgets/HellingerSegmentDialog.md) | 3 | 1215 | 5 | Modal dialog for creating or editing a Hellinger segment containing multiple picks |
| [HellingerStatsDialog](../src/qt-widgets/HellingerStatsDialog.md) | 3 | 254 | 2 | Dialog for viewing and exporting detailed results from Hellinger calculations |
| [HellingerThread](../src/qt-widgets/HellingerThread.md) | 2 | 448 | 39 | (pending) |

#### Kinematic

| Unit | Tier | Lines | Fan-in | Description |
|---|---|---|---|---|
| [KinematicGraphPicker](../src/qt-widgets/KinematicGraphPicker.md) | 3 | 291 | 4 | Picker for extracting and displaying information from kinematic graphs |
| [KinematicGraphsConfigurationDialog](../src/qt-widgets/KinematicGraphsConfigurationDialog.md) | 3 | 204 | 6 | Dialog for configuring kinematic graph calculation parameters |
| [KinematicGraphsConfigurationWidget](../src/qt-widgets/KinematicGraphsConfigurationWidget.md) | 2 | 442 | 27 | (pending) |
| [KinematicGraphsDialog](../src/qt-widgets/KinematicGraphsDialog.md) | 2 | 2040 | 38 | (pending) |

#### Manage

| Unit | Tier | Lines | Fan-in | Description |
|---|---|---|---|---|
| [ManageFeatureCollectionsActionWidget](../src/qt-widgets/ManageFeatureCollectionsActionWidget.md) | 2 | 486 | 36 | (pending) |
| [ManageFeatureCollectionsDialog](../src/qt-widgets/ManageFeatureCollectionsDialog.md) | 2 | 1746 | 17 | (pending) |
| [ManageFeatureCollectionsEditConfigurations](../src/qt-widgets/ManageFeatureCollectionsEditConfigurations.md) | 3 | 325 | 2 | Configuration handlers for saving feature collections in different formats with GMT and shapefile/OGR format support |

#### Open

| Unit | Tier | Lines | Fan-in | Description |
|---|---|---|---|---|
| [OpenDirectoryDialog](../src/qt-widgets/OpenDirectoryDialog.md) | 2 | 130 | 19 | (pending) |
| [OpenFileDialog](../src/qt-widgets/OpenFileDialog.md) | 2 | 203 | 45 | (pending) |
| [OpenProjectRelativeOrAbsoluteDialog](../src/qt-widgets/OpenProjectRelativeOrAbsoluteDialog.md) | 3 | 537 | 3 | Dialog for choosing between original or current file paths when opening a moved project |

#### Preferences

| Unit | Tier | Lines | Fan-in | Description |
|---|---|---|---|---|
| [PreferencesDialog](../src/qt-widgets/PreferencesDialog.md) | 3 | 405 | 0 | Main preferences dialog with categorized settings panes and advanced preferences table |
| [PreferencesPaneFiles](../src/qt-widgets/PreferencesPaneFiles.md) | 3 | 840 | 12 | Preference pane for file-related settings like default paths and file open/save behavior |
| [PreferencesPaneKinematicGraphs](../src/qt-widgets/PreferencesPaneKinematicGraphs.md) | 3 | 184 | 1 | Preference pane for kinematic graph settings including velocity calculations and warning thresholds |
| [PreferencesPaneNetwork](../src/qt-widgets/PreferencesPaneNetwork.md) | 3 | 325 | 1 | Preference pane for network configuration (proxy and server settings) |
| [PreferencesPanePython](../src/qt-widgets/PreferencesPanePython.md) | 3 | 455 | 1 | Preference pane for Python configuration (home directory and script paths) |
| [PreferencesPaneView](../src/qt-widgets/PreferencesPaneView.md) | 3 | 355 | 1 | Preference pane for view configuration (animation defaults and visibility options) |

#### Python

| Unit | Tier | Lines | Fan-in | Description |
|---|---|---|---|---|
| [PythonArgumentWidget](../src/qt-widgets/PythonArgumentWidget.md) | 3 | 284 | 10 | Base and concrete widget classes for Python script argument configuration |
| [PythonConsoleDialog](../src/qt-widgets/PythonConsoleDialog.md) | 3 | 2011 | 2 | Interactive Python console dialog with output redirection and execution control |
| [PythonExecutionMonitorWidget](../src/qt-widgets/PythonExecutionMonitorWidget.md) | 3 | 290 | 0 | Monitor widget for long-running Python script execution with cancellation controls |
| [PythonInitFailedDialog](../src/qt-widgets/PythonInitFailedDialog.md) | 3 | 255 | 3 | Modal dialog shown when Python initialization fails, with platform-specific installation instructions |
| [PythonReadlineDialog](../src/qt-widgets/PythonReadlineDialog.md) | 3 | 212 | 1 | Modal dialog for getting a single line of input from the Python console |

#### Raster

| Unit | Tier | Lines | Fan-in | Description |
|---|---|---|---|---|
| [RasterBandPage](../src/qt-widgets/RasterBandPage.md) | 3 | 421 | 1 | Wizard page for assigning names to raster bands during import |
| [RasterFeatureCollectionPage](../src/qt-widgets/RasterFeatureCollectionPage.md) | 3 | 189 | 1 | Wizard page for selecting feature collection and save options during raster import |
| [RasterGeoreferencingPage](../src/qt-widgets/RasterGeoreferencingPage.md) | 3 | 181 | 1 | Wizard page for defining raster spatial extent during import |
| [RasterLayerOptionsWidget](../src/qt-widgets/RasterLayerOptionsWidget.md) | 3 | 1023 | 11 | Options widget for configuring raster layer display and color mapping |
| [RasterPropertiesDialog](../src/qt-widgets/RasterPropertiesDialog.md) | 3 | 975 | 0 | Dialog for viewing and configuring raster properties and appearance |

#### Reconstruction

| Unit | Tier | Lines | Fan-in | Description |
|---|---|---|---|---|
| [ReconstructionLayerOptionsWidget](../src/qt-widgets/ReconstructionLayerOptionsWidget.md) | 3 | 428 | 1 | Provides options for reconstruction layers |
| [ReconstructionPoleWidget](../src/qt-widgets/ReconstructionPoleWidget.md) | 3 | 338 | 13 | Displays a single rotation pole with its parameters |
| [ReconstructionViewWidget](../src/qt-widgets/ReconstructionViewWidget.md) | 2 | 1019 | 180 | (pending) |

#### Scalar

| Unit | Tier | Lines | Fan-in | Description |
|---|---|---|---|---|
| [ScalarField3DDepthLayersPage](../src/qt-widgets/ScalarField3DDepthLayersPage.md) | 3 | 1539 | 1 | Wizard page for configuring 3D scalar field depth layers |
| [ScalarField3DFeatureCollectionPage](../src/qt-widgets/ScalarField3DFeatureCollectionPage.md) | 3 | 179 | 1 | Wizard page for selecting or creating a feature collection for imported scalar field data |
| [ScalarField3DGeoreferencingPage](../src/qt-widgets/ScalarField3DGeoreferencingPage.md) | 3 | 189 | 1 | Wizard page for specifying geographic extent and coordinate mapping of raster data |
| [ScalarField3DLayerOptionsWidget](../src/qt-widgets/ScalarField3DLayerOptionsWidget.md) | 3 | 5961 | 1 | Options widget for controlling 3D scalar field layer rendering parameters |

#### Set

| Unit | Tier | Lines | Fan-in | Description |
|---|---|---|---|---|
| [SetCameraViewpointDialog](../src/qt-widgets/SetCameraViewpointDialog.md) | 2 | 260 | 149 | (pending) |
| [SetProjectionDialog](../src/qt-widgets/SetProjectionDialog.md) | 3 | 337 | 1 | Dialog for selecting map projection and configuring projection parameters |
| [SetTopologyReconstructionParametersDialog](../src/qt-widgets/SetTopologyReconstructionParametersDialog.md) | 3 | 1376 | 1 | Dialog for configuring topology-based feature geometry reconstruction parameters |
| [SetVGPVisibilityDialog](../src/qt-widgets/SetVGPVisibilityDialog.md) | 3 | 621 | 0 | Dialog for controlling Virtual Geomagnetic Pole visibility in reconstruction layers |

#### Shapefile

| Unit | Tier | Lines | Fan-in | Description |
|---|---|---|---|---|
| [ShapefileAttributeMapperDialog](../src/qt-widgets/ShapefileAttributeMapperDialog.md) | 3 | 252 | 6 | Dialog for mapping shapefile/OGR attributes to model properties |
| [ShapefileAttributeRemapperDialog](../src/qt-widgets/ShapefileAttributeRemapperDialog.md) | 3 | 251 | 1 | Dialog for remapping existing shapefile/OGR attribute associations |
| [ShapefileAttributeViewerDialog](../src/qt-widgets/ShapefileAttributeViewerDialog.md) | 3 | 548 | 0 | Dialog displaying raw shapefile attributes extracted from features |
| [ShapefileAttributeWidget](../src/qt-widgets/ShapefileAttributeWidget.md) | 2 | 786 | 11 | (pending) |
| [ShapefileFileFormatConfigurationDialog](../src/qt-widgets/ShapefileFileFormatConfigurationDialog.md) | 3 | 274 | 1 | Dialog for configuring OGR/shapefile file format and attribute options |
| [ShapefilePropertyMapper](../src/qt-widgets/ShapefilePropertyMapper.md) | 3 | 189 | 2 | Property mapper guiding users through shapefile attribute mapping |

#### Topology

| Unit | Tier | Lines | Fan-in | Description |
|---|---|---|---|---|
| [TopologyGeometryResolverLayerOptionsWidget](../src/qt-widgets/TopologyGeometryResolverLayerOptionsWidget.md) | 3 | 437 | 1 | Layer options widget for topology geometry resolver visualization |
| [TopologyNetworkResolverLayerOptionsWidget](../src/qt-widgets/TopologyNetworkResolverLayerOptionsWidget.md) | 3 | 3283 | 1 | Layer options widget for topology network strain rate visualization and rift parameters |
| [TopologyToolsWidget](../src/qt-widgets/TopologyToolsWidget.md) | 2 | 1326 | 13 | (pending) |

#### Visual

| Unit | Tier | Lines | Fan-in | Description |
|---|---|---|---|---|
| [VisualLayerWidget](../src/qt-widgets/VisualLayerWidget.md) | 2 | 2230 | 18 | (pending) |
| [VisualLayersComboBox](../src/qt-widgets/VisualLayersComboBox.md) | 3 | 294 | 11 | Combobox for selecting visual layers with type-based filtering |
| [VisualLayersDelegate](../src/qt-widgets/VisualLayersDelegate.md) | 3 | 305 | 14 | Item delegate for rendering and editing visual layers in list view |
| [VisualLayersDialog](../src/qt-widgets/VisualLayersDialog.md) | 3 | 116 | 0 | Top-level dialog window displaying the visual layers management interface |
| [VisualLayersListView](../src/qt-widgets/VisualLayersListView.md) | 3 | 328 | 1 | List view of visual layers with drag-and-drop support and persistent editing |
| [VisualLayersWidget](../src/qt-widgets/VisualLayersWidget.md) | 3 | 500 | 2 | Main interface for managing visual layers with add, hide/show, and styling controls |

#### Other

| Unit | Tier | Lines | Fan-in | Description |
|---|---|---|---|---|
| [AboutDialog](../src/qt-widgets/AboutDialog.md) | 3 | 375 | 1 | (pending) |
| [AbstractCustomPropertiesWidget](../src/qt-widgets/AbstractCustomPropertiesWidget.md) | 3 | 71 | 7 | (pending) |
| [AbstractEditWidget](../src/qt-widgets/AbstractEditWidget.md) | 1 | 387 | 346 | (pending) |
| [ActionButtonBox](../src/qt-widgets/ActionButtonBox.md) | 2 | 195 | 22 | (pending) |
| [AddNewLayerDialog](../src/qt-widgets/AddNewLayerDialog.md) | 3 | 275 | 5 | (pending) |
| [AddPropertyDialog](../src/qt-widgets/AddPropertyDialog.md) | 2 | 908 | 16 | (pending) |
| [AgeModelManagerDialog](../src/qt-widgets/AgeModelManagerDialog.md) | 3 | 527 | 0 | (pending) |
| [AnimateControlWidget](../src/qt-widgets/AnimateControlWidget.md) | 3 | 577 | 1 | (pending) |
| [AnimateDialog](../src/qt-widgets/AnimateDialog.md) | 3 | 973 | 0 | (pending) |
| [ApplyReconstructionPoleAdjustmentDialog](../src/qt-widgets/ApplyReconstructionPoleAdjustmentDialog.md) | 2 | 1321 | 35 | (pending) |
| [AssignReconstructionPlateIdsDialog](../src/qt-widgets/AssignReconstructionPlateIdsDialog.md) | 2 | 2426 | 22 | (pending) |
| [CalculateReconstructionPoleDialog](../src/qt-widgets/CalculateReconstructionPoleDialog.md) | 3 | 628 | 0 | (pending) |
| [CanvasToolBarDockWidget](../src/qt-widgets/CanvasToolBarDockWidget.md) | 3 | 2326 | 4 | (pending) |
| [ChangeFeatureTypeDialog](../src/qt-widgets/ChangeFeatureTypeDialog.md) | 3 | 573 | 2 | Dialog for changing a feature's type while reconciling properties according to new type constraints |
| [ChangePropertyWidget](../src/qt-widgets/ChangePropertyWidget.md) | 3 | 354 | 2 | Helper widget for renaming a property when it becomes invalid under a new feature type |
| [ColourScaleButton](../src/qt-widgets/ColourScaleButton.md) | 2 | 384 | 155 | (pending) |
| [ColourScaleWidget](../src/qt-widgets/ColourScaleWidget.md) | 3 | 379 | 16 | Renders annotated colour scale bar with optional logarithmic scaling |
| [ColouringDialog](../src/qt-widgets/ColouringDialog.md) | 3 | 1839 | 0 | Dialog for managing colour schemes applied to features or globally |
| [ConfigValueEditorWidget](../src/qt-widgets/ConfigValueEditorWidget.md) | 3 | 164 | 9 | Composite editor widget combining text input with reset-to-default button |
| [ConnectWFSDialog](../src/qt-widgets/ConnectWFSDialog.md) | 1 | 853 | 366 | (pending) |
| [DatelineWrapOptionsWidget](../src/qt-widgets/DatelineWrapOptionsWidget.md) | 2 | 249 | 27 | (pending) |
| [DigitisationWidget](../src/qt-widgets/DigitisationWidget.md) | 3 | 713 | 3 | Task panel widget for digitizing geometric features on the map |
| [DockWidget](../src/qt-widgets/DockWidget.md) | 2 | 372 | 15 | (pending) |
| [DrawStyleDialog](../src/qt-widgets/DrawStyleDialog.md) | 2 | 1656 | 7 | (pending) |
| [ElidedLabel](../src/qt-widgets/ElidedLabel.md) | 3 | 335 | 12 | Custom label widget that automatically elides text with ellipsis when too wide |
| [FeaturePropertiesDialog](../src/qt-widgets/FeaturePropertiesDialog.md) | 3 | 476 | 3 | Main dialog for viewing and editing feature properties across three tabbed interfaces |
| [FeatureSummaryWidget](../src/qt-widgets/FeatureSummaryWidget.md) | 3 | 724 | 2 | Task panel displaying metadata of the currently focused feature |
| [FileDialogFilter](../src/qt-widgets/FileDialogFilter.md) | 2 | 152 | 22 | (pending) |
| [FiniteRotationCalculatorDialog](../src/qt-widgets/FiniteRotationCalculatorDialog.md) | 3 | 1732 | 0 | Utility dialog for computing finite rotation operations on a sphere |
| [FlowlinePropertiesWidget](../src/qt-widgets/FlowlinePropertiesWidget.md) | 3 | 289 | 1 | Custom properties widget for specifying flowline point roles and computing equivalent centres |
| [FriendlyLineEdit](../src/qt-widgets/FriendlyLineEdit.md) | 2 | 468 | 70 | (pending) |
| [GMTFileFormatConfigurationDialog](../src/qt-widgets/GMTFileFormatConfigurationDialog.md) | 3 | 242 | 2 | Configuration dialog for GMT file export header format |
| [GMenuButton](../src/qt-widgets/GMenuButton.md) | 3 | 198 | 2 | Menu button providing full-screen access to the main menu bar |
| [GPlatesDialog](../src/qt-widgets/GPlatesDialog.md) | 2 | 137 | 344 | (pending) |
| [GlobeAndMapWidget](../src/qt-widgets/GlobeAndMapWidget.md) | 2 | 842 | 53 | (pending) |
| [GlobeCanvas](../src/qt-widgets/GlobeCanvas.md) | 2 | 2425 | 53 | (pending) |
| [GpgimVersionWarningDialog](../src/qt-widgets/GpgimVersionWarningDialog.md) | 3 | 526 | 0 | Dialog warning about GPGIM version mismatches when loading or saving files |
| [ImportRasterDialog](../src/qt-widgets/ImportRasterDialog.md) | 2 | 1064 | 45 | (pending) |
| [ImportScalarField3DDialog](../src/qt-widgets/ImportScalarField3DDialog.md) | 2 | 994 | 50 | (pending) |
| [InformationDialog](../src/qt-widgets/InformationDialog.md) | 2 | 238 | 92 | (pending) |
| [InsertVGPReconstructionPoleDialog](../src/qt-widgets/InsertVGPReconstructionPoleDialog.md) | 3 | 554 | 1 | Dialog for inserting a Virtual Geomagnetic Pole reconstruction pole |
| [InsertionPointWidget](../src/qt-widgets/InsertionPointWidget.md) | 3 | 137 | 1 | Lightweight widget displaying an insertion point arrow and cancel button |
| [InvalidPropertyValueException](../src/qt-widgets/InvalidPropertyValueException.md) | 3 | 78 | 10 | Exception thrown when edit widgets cannot create valid property values |
| [LatLonCoordinatesTable](../src/qt-widgets/LatLonCoordinatesTable.md) | 3 | 1008 | 8 | Tree widget wrapper displaying geometries and their lat/lon coordinates |
| [LayerOptionsWidget](../src/qt-widgets/LayerOptionsWidget.md) | 2 | 75 | 58 | (pending) |
| [LeaveFullScreenButton](../src/qt-widgets/LeaveFullScreenButton.md) | 3 | 147 | 2 | Button widget for exiting full-screen mode |
| [LicenseDialog](../src/qt-widgets/LicenseDialog.md) | 3 | 108 | 0 | Dialog displaying the GNU General Public License version 2 |
| [LightingWidget](../src/qt-widgets/LightingWidget.md) | 3 | 448 | 1 | Task panel widget for adjusting scene lighting parameters including lighting toggles, ambient intensity, and view-frame attachment |
| [LinkWidget](../src/qt-widgets/LinkWidget.md) | 2 | 236 | 20 | (pending) |
| [LogDialog](../src/qt-widgets/LogDialog.md) | 3 | 436 | 0 | Dialog displaying application log messages with filtering by severity and text search for users who don't run from terminal |
| [MapCanvas](../src/qt-widgets/MapCanvas.md) | 3 | 963 | 7 | QGraphicsScene subclass rendering 2D map view with OpenGL, supporting image export and frame-to-frame caching |
| [MapView](../src/qt-widgets/MapView.md) | 2 | 1389 | 42 | (pending) |
| [MeasureDistanceWidget](../src/qt-widgets/MeasureDistanceWidget.md) | 3 | 1004 | 1 | Task panel displaying quick and feature-based distance measurements with coordinate and area information |
| [MergeReconstructionLayersDialog](../src/qt-widgets/MergeReconstructionLayersDialog.md) | 3 | 653 | 8 | Dialog for selecting Reconstruction Tree layers to merge into a target layer with bulk select/clear actions |
| [MetadataDialog](../src/qt-widgets/MetadataDialog.md) | 3 | 2830 | 3 | Comprehensive metadata editor for feature collections, rotation sequences, and poles with support for contributors, creators, and timescales |
| [MissingSessionFilesDialog](../src/qt-widgets/MissingSessionFilesDialog.md) | 3 | 437 | 6 | Dialog for remapping missing files when loading projects or sessions with file browse replacement options |
| [ModifyGeometryWidget](../src/qt-widgets/ModifyGeometryWidget.md) | 3 | 232 | 1 | Task panel widget for displaying lat/lon coordinates of geometry being modified by canvas tools |
| [ModifyReconstructionPoleWidget](../src/qt-widgets/ModifyReconstructionPoleWidget.md) | 2 | 1788 | 23 | (pending) |
| [MovePoleWidget](../src/qt-widgets/MovePoleWidget.md) | 2 | 1090 | 22 | (pending) |
| [NoActiveEditWidgetException](../src/qt-widgets/NoActiveEditWidgetException.md) | 3 | 59 | 2 | Exception raised when EditWidgetGroupBox's precondition of at least one active edit widget is violated |
| [OgrSrsWriteOptionDialog](../src/qt-widgets/OgrSrsWriteOptionDialog.md) | 3 | 264 | 5 | Dialog for choosing how to write spatial reference systems when exporting OGR vector data |
| [PoleSequenceTableWidget](../src/qt-widgets/PoleSequenceTableWidget.md) | 3 | 185 | 11 | Qt widget displaying a table of rotation poles with fixed/moving plate IDs and time ranges |
| [ProgressDialog](../src/qt-widgets/ProgressDialog.md) | 2 | 211 | 474 | (pending) |
| [ProjectionControlWidget](../src/qt-widgets/ProjectionControlWidget.md) | 3 | 321 | 2 | Control widget for switching map projections via combobox and keyboard shortcuts |
| [PropertyValueNotSupportedException](../src/qt-widgets/PropertyValueNotSupportedException.md) | 3 | 66 | 0 | Exception thrown when edit widgets encounter unsupported property value types |
| [QtWidgetUtils](../src/qt-widgets/QtWidgetUtils.md) | 2 | 284 | 278 | (pending) |
| [QueryFeaturePropertiesWidget](../src/qt-widgets/QueryFeaturePropertiesWidget.md) | 3 | 662 | 2 | Widget displaying feature properties and reconstruction parameters in a tree |
| [ReadErrorAccumulationDialog](../src/qt-widgets/ReadErrorAccumulationDialog.md) | 2 | 897 | 13 | (pending) |
| [ReconstructLayerOptionsWidget](../src/qt-widgets/ReconstructLayerOptionsWidget.md) | 3 | 847 | 1 | Shows options for reconstructed geometry layers in the visual layers widget |
| [ReconstructScalarCoverageLayerOptionsWidget](../src/qt-widgets/ReconstructScalarCoverageLayerOptionsWidget.md) | 3 | 776 | 1 | Manages visualization options for reconstructed scalar coverages |
| [RemappedColourPaletteWidget](../src/qt-widgets/RemappedColourPaletteWidget.md) | 3 | 905 | 8 | Manages color palette selection and value range mapping |
| [ResizeToContentsTextEdit](../src/qt-widgets/ResizeToContentsTextEdit.md) | 3 | 227 | 0 | QTextEdit subclass that automatically resizes to document content |
| [SaveFileDialog](../src/qt-widgets/SaveFileDialog.md) | 2 | 261 | 65 | (pending) |
| [SaveFileDialogImpl](../src/qt-widgets/SaveFileDialogImpl.md) | 3 | 478 | 2 | Provides platform-specific implementations of save file dialogs |
| [SceneView](../src/qt-widgets/SceneView.md) | 3 | 190 | 9 | Abstract base class for viewport implementations (globe 3D and map 2D) |
| [SearchResultsDockWidget](../src/qt-widgets/SearchResultsDockWidget.md) | 3 | 448 | 12 | Tabbed dock widget displaying clicked geometries and topology sections |
| [SelectionWidget](../src/qt-widgets/SelectionWidget.md) | 2 | 466 | 37 | (pending) |
| [SmallCircleWidget](../src/qt-widgets/SmallCircleWidget.md) | 2 | 601 | 43 | (pending) |
| [SnapNearbyVerticesWidget](../src/qt-widgets/SnapNearbyVerticesWidget.md) | 3 | 471 | 1 | Configuration widget for vertex snapping during geometry editing |
| [SpecifyAnchoredPlateIdDialog](../src/qt-widgets/SpecifyAnchoredPlateIdDialog.md) | 3 | 455 | 0 | Dialog for specifying anchored plate ID with quick-select from feature properties |
| [SymbolManagerDialog](../src/qt-widgets/SymbolManagerDialog.md) | 3 | 178 | 0 | Dialog for managing drawing symbols |
| [TaskPanel](../src/qt-widgets/TaskPanel.md) | 2 | 1047 | 18 | (pending) |
| [TaskPanelWidget](../src/qt-widgets/TaskPanelWidget.md) | 2 | 107 | 23 | (pending) |
| [TimeControlWidget](../src/qt-widgets/TimeControlWidget.md) | 3 | 392 | 0 | Widget for navigating reconstruction time with spinbox and step buttons |
| [TimeDependentRasterPage](../src/qt-widgets/TimeDependentRasterPage.md) | 3 | 1557 | 1 | Wizard page for assembling time-dependent raster sequences with time value assignment |
| [TotalReconstructionPolesDialog](../src/qt-widgets/TotalReconstructionPolesDialog.md) | 3 | 1532 | 1 | Dialog for examining and exporting total reconstruction poles data |
| [TotalReconstructionSequencesDialog](../src/qt-widgets/TotalReconstructionSequencesDialog.md) | 2 | 2844 | 170 | (pending) |
| [TrinketIcon](../src/qt-widgets/TrinketIcon.md) | 3 | 236 | 18 | Interactive icon widget for status bar display with click callbacks |
| [UninitialisedEditWidgetException](../src/qt-widgets/UninitialisedEditWidgetException.md) | 3 | 60 | 19 | Exception for edit widget precondition violation |
| [UnsavedChangesWarningDialog](../src/qt-widgets/UnsavedChangesWarningDialog.md) | 3 | 404 | 6 | Warning dialog for operations that would lose unsaved changes |
| [VelocityFieldCalculatorLayerOptionsWidget](../src/qt-widgets/VelocityFieldCalculatorLayerOptionsWidget.md) | 3 | 1371 | 1 | Options panel for configuring velocity field calculator layers |
| [VelocityMethodWidget](../src/qt-widgets/VelocityMethodWidget.md) | 2 | 475 | 20 | (pending) |
| [ViewFeatureGeometriesWidget](../src/qt-widgets/ViewFeatureGeometriesWidget.md) | 3 | 398 | 2 | Displays feature geometries including reconstructed form at current time |
| [ViewportWindow](../src/qt-widgets/ViewportWindow.md) | 1 | 3971 | 196 | (pending) |
| [ZoomControlWidget](../src/qt-widgets/ZoomControlWidget.md) | 3 | 342 | 0 | Compact zoom control with spinbox and buttons for zoom in/out/reset |
| [ZoomSliderWidget](../src/qt-widgets/ZoomSliderWidget.md) | 3 | 311 | 2 | Vertical slider widget for controlling viewport zoom with add/subtract icon buttons |

### `src/qt-widgets/deprecated`

| Unit | Tier | Lines | Fan-in | Description |
|---|---|---|---|---|
| [CalculateStagePoleDialog](../src/qt-widgets/deprecated/CalculateStagePoleDialog.md) | 3 | 451 | 0 | Dialog for calculating stage pole rotation axis from two plate IDs at two times |
| [CreateFeatureIdListDialog](../src/qt-widgets/deprecated/CreateFeatureIdListDialog.md) | 3 | 342 | 0 | Dialog for building and managing a list of feature IDs with save/load/add/remove operations |
| [CreateFeatureIdListModel](../src/qt-widgets/deprecated/CreateFeatureIdListModel.md) | 3 | 238 | 3 | Qt item model wrapping a list of feature ID strings for display in a list view |
| [CreateTopologyWidget](../src/qt-widgets/deprecated/CreateTopologyWidget.md) | 3 | 818 | 0 | Widget for displaying and managing reconstructed feature geometries during topology creation |
| [DigitisationUndoParadoxException](../src/qt-widgets/deprecated/DigitisationUndoParadoxException.md) | 3 | 98 | 0 | Exception thrown when digitisation undo/redo stack enters an inconsistent state |
| [SmallCircleManager](../src/qt-widgets/deprecated/SmallCircleManager.md) | 3 | 547 | 0 | Dialog for managing a collection of small circles displayed in a table and on the globe |


## Other files

| File | Kind | Lines |
|---|---|---|
| `src/qt-widgets/AddHellWidgetUi.ui` | Qt form | 136 |
| `src/qt-widgets/CMakeLists.txt` | build | 628 |
| `src/qt-widgets/deprecated/BuildTopologyWidgetUi.ui` | Qt form | 314 |
| `src/qt-widgets/deprecated/EditTopologyWidgetUi.ui` | Qt form | 262 |
| `src/qt-widgets/deprecated/MotionTrackPropertiesWidgetUi.ui` | Qt form | 38 |

## Depends on

| Component | References |
|---|---|
| [gui](gui.md) | 7008 |
| [model](model.md) | 5269 |
| [app-logic](app-logic.md) | 4437 |
| [presentation](presentation.md) | 2350 |
| [file-io](file-io.md) | 1548 |
| [maths](maths.md) | 1496 |
| [property-values](property-values.md) | 1178 |
| [global](global.md) | 827 |
| [view-operations](view-operations.md) | 653 |
| [utils](utils.md) | 578 |
| [opengl](opengl.md) | 494 |
| [feature-visitors](feature-visitors.md) | 394 |
| [data-mining](data-mining.md) | 167 |
| [api](api.md) | 159 |
| [canvas-tools](canvas-tools.md) | 95 |
| [unit-test](unit-test.md) | 21 |
| [cli](cli.md) | 8 |
| [entry-points](entry-points.md) | 1 |

## Used by

| Component | References |
|---|---|
| [gui](gui.md) | 779 |
| [file-io](file-io.md) | 384 |
| [canvas-tools](canvas-tools.md) | 275 |
| [presentation](presentation.md) | 64 |
| [app-logic](app-logic.md) | 53 |
| [api](api.md) | 30 |
| [maths](maths.md) | 18 |
| [entry-points](entry-points.md) | 14 |
| [view-operations](view-operations.md) | 14 |
| [data-mining](data-mining.md) | 13 |
| [unit-test](unit-test.md) | 13 |
| [feature-visitors](feature-visitors.md) | 12 |
| [model](model.md) | 7 |
| [utils](utils.md) | 7 |
| [cli](cli.md) | 4 |
| [opengl](opengl.md) | 4 |
| [deprecated](deprecated.md) | 1 |
| [property-values](property-values.md) | 1 |

## Explore

Run these from the `gplates-code` skill directory:

```bash
python scripts/gpq.py tree src/qt-widgets
python scripts/gpq.py sym . --mode sub --path src/qt-widgets --defs-only
```
