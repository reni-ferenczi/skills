# Georeferencing

[Book TOC](../../TOC.md) · [property-values](../../components/property-values.md) · cluster Community 603 · tier 1

| Source file | Kind | Lines |
|---|---|---|
| `src/property-values/Georeferencing.h` | C++ | 590 |
| `src/property-values/Georeferencing.cc` | C++ | 602 |

## Overview

[[[PROSE overview unit=property-values/Georeferencing tier=1]]]
Replace this whole block, markers included, with 1-3 paragraphs: what this unit is, why it exists, and how it fits the surrounding design. Do not restate the tables below.
[[[/PROSE]]]

## Declared types

| Name | Kind | Bases | Template | Subclasses | Description |
|---|---|---|---|---|---|
| [`GPlatesPropertyValues::Georeferencing`](#gplatespropertyvaluesgeoreferencing) | class | [`GPlatesUtils::ReferenceCount<Georeferencing>`](../utils/ReferenceCount.md) | — | 0 | The Georeferencing class stores information relating to the georeferencing of raster images. |

## Members

### `GPlatesPropertyValues::Georeferencing`

| Member | Kind | Type | Access | Description |
|---|---|---|---|---|
| `non_null_ptr_type` | typedef | `GPlatesUtils::non_null_intrusive_ptr<Georeferencing>` | public | — |
| `non_null_ptr_to_const_type` | typedef | `GPlatesUtils::non_null_intrusive_ptr<const Georeferencing>` | public | — |
| `parameters_type` | struct | `None` | public | The parameters that specify the affine transform. |
| `lat_lon_extents_type` | struct | `None` | public | A convenience structure for conversions to and from the affine transform and lat-lon extents. |
| `create()` | method | `non_null_ptr_type` | public | Default constructor. |
| `create( unsigned int raster_width, unsigned int raster_height, bool convert_from_grid_line_registration = false)` | method | `non_null_ptr_type` | public | Creates an affine transform that maps a raster to the entire globe. |
| `create( const lat_lon_extents_type &lat_lon_extents, unsigned int raster_width, unsigned int raster_height, bool convert_from_grid_line_registration = false)` | method | `non_null_ptr_type` | public | Creates an affine transform that maps a raster to the specified lat-lon extents. |
| `create( const parameters_type &parameters, bool convert_from_grid_line_registration = false)` | method | `non_null_ptr_type` | public | Creates an affine transform with the specified parameters. |
| `get_parameters( bool convert_to_grid_line_registration = false)` | method | `parameters_type` | public | Retrieves the affine transform parameters. |
| `set_parameters( const parameters_type &parameters, bool convert_from_grid_line_registration = false)` | method | `void` | public | Sets the affine transform parameters. |
| `get_lat_lon_extents( unsigned int raster_width, unsigned int raster_height, bool convert_to_grid_line_registration = false)` | method | `boost::optional<lat_lon_extents_type>` | public | Retrieves the affine transform parameters as lat-lon extents. |
| `set_lat_lon_extents( const lat_lon_extents_type &lat_lon_extents, unsigned int raster_width, unsigned int raster_height, bool convert_from_grid_line_registration = false)` | method | `void` | public | Sets the affine transform parameters using lat-lon extents. |
| `reset_to_global_extents( unsigned int raster_width, unsigned int raster_height, bool convert_from_grid_line_registration = false)` | method | `void` | public | Resets the affine transform so that the raster covers the entire globe. |
| `contract_grid_line_to_pixel_registration( unsigned int raster_width, unsigned int raster_height)` | method | `void` | public | Contract from grid line registration to pixel registration. |
| `expand_pixel_to_grid_line_registration( unsigned int raster_width, unsigned int raster_height)` | method | `void` | public | Expand from pixel registration to grid line registration. |
| `GLOBAL_LAT_LON_EXTENTS` | field | `lat_lon_extents_type` | private | Global lat-lon extents (latitude range \[-90, 90\] and longitude range \[-180, 180\]). |
| `convert_to_pixel_registration( parameters_type parameters, bool convert_from_grid_line_registration)` | method | `parameters_type` | private | Convert parameters to pixel registration (if convert\_from\_grid\_line\_registration is true), otherwise simply returns parameters. |
| `convert_to_pixel_registration( const lat_lon_extents_type &lat_lon_extents, unsigned int raster_width, unsigned int raster_height, bool convert_from_grid_line_registration)` | method | `parameters_type` | private | Convert lat-lon extents (as pixel or grid line registration) to pixel registration parameters. |
| `Georeferencing( const parameters_type &parameters)` | constructor | `None` | private | — |
| `Georeferencing( const Georeferencing &other)` | constructor | `None` | private | — |
| `d_parameters` | field | `parameters_type` | private | — |

## Free functions and macros

| Name | Kind | Type / body | Description |
|---|---|---|---|
| `MIN_LATITUDE` | variable | `double` | — |
| `MAX_LATITUDE` | variable | `double` | — |
| `LATITUDE_EPISLON` | variable | `double` | Enough to account for transformations back and forth between grid line registration. |
| `GLOBAL_LAT_LON_EXTENTS` | variable | `GPlatesPropertyValues::Georeferencing::lat_lon_extents_type` | — |
| `GPLATES_PROPERTYVALUES_GEOREFERENCING_H` | macro | `None` | — |

## Notes

[[[PROSE notes unit=property-values/Georeferencing tier=1]]]
Replace this whole block, markers included, with invariants, ownership, threading or gotchas that are not visible in the tables. Write *None.* if there is nothing worth saying.
[[[/PROSE]]]

## Used by

| Unit | Component | References |
|---|---|---|
| [gui/ExportRasterAnimationStrategy](../gui/ExportRasterAnimationStrategy.md) | gui | 83 |
| [file-io/GdalRasterWriter](../file-io/GdalRasterWriter.md) | file-io | 69 |
| [qt-widgets/EditAffineTransformGeoreferencingWidget](../qt-widgets/EditAffineTransformGeoreferencingWidget.md) | qt-widgets | 52 |
| [utils/Profile](../utils/Profile.md) | utils | 34 |
| [qt-widgets/ExportRasterOptionsWidget](../qt-widgets/ExportRasterOptionsWidget.md) | qt-widgets | 32 |
| [opengl/GLMatrix](../opengl/GLMatrix.md) | opengl | 27 |
| [property-values/GmlRectifiedGrid](GmlRectifiedGrid.md) | property-values | 27 |
| [file-io/RasterWriter](../file-io/RasterWriter.md) | file-io | 24 |
| [opengl/GLMultiResolutionRaster](../opengl/GLMultiResolutionRaster.md) | opengl | 19 |
| [app-logic/RasterLayerParams](../app-logic/RasterLayerParams.md) | app-logic | 18 |
| [scribe/TranscriptionScribeContext](../scribe/TranscriptionScribeContext.md) | scribe | 15 |
| [qt-widgets/ImportRasterDialog](../qt-widgets/ImportRasterDialog.md) | qt-widgets | 13 |
| [qt-widgets/TopologyNetworkResolverLayerOptionsWidget](../qt-widgets/TopologyNetworkResolverLayerOptionsWidget.md) | qt-widgets | 12 |
| [qt-widgets/GlobeCanvas](../qt-widgets/GlobeCanvas.md) | qt-widgets | 11 |
| [app-logic/ExtractRasterFeatureProperties](../app-logic/ExtractRasterFeatureProperties.md) | app-logic | 10 |
| [qt-widgets/RasterGeoreferencingPage](../qt-widgets/RasterGeoreferencingPage.md) | qt-widgets | 9 |
| [gui/ExportAnimationRegistry](../gui/ExportAnimationRegistry.md) | gui | 8 |
| [qt-widgets/GenerateDeformingMeshPointsDialog](../qt-widgets/GenerateDeformingMeshPointsDialog.md) | qt-widgets | 8 |
| [qt-widgets/ScalarField3DGeoreferencingPage](../qt-widgets/ScalarField3DGeoreferencingPage.md) | qt-widgets | 8 |
| [opengl/GLRenderer](../opengl/GLRenderer.md) | opengl | 7 |

*... and 44 more units.*

## Related

*None.*

## Explore

Run these from the `gplates-code` skill directory:

```bash
python scripts/gpq.py file src/property-values/Georeferencing.h
python scripts/gpq.py def GPlatesPropertyValues::Georeferencing --body
python scripts/gpq.py uses Georeferencing --kind class
python scripts/gpq.py hier Georeferencing
```
