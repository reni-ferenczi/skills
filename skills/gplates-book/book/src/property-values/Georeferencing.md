# Georeferencing

[Book TOC](../../TOC.md) · [property-values](../../components/property-values.md) · cluster Community 603 · tier 1

| Source file | Kind | Lines |
|---|---|---|
| `src/property-values/Georeferencing.h` | C++ | 590 |
| `src/property-values/Georeferencing.cc` | C++ | 602 |

## Overview

`Georeferencing` holds the six-coefficient affine transform that maps raster pixel coordinates to geographic coordinates. It is not a `PropertyValue` — it derives only from `GPlatesUtils::ReferenceCount` and is passed around as `non_null_ptr_to_const_type`. The property value that actually lives in a feature is `GmlRectifiedGrid`, whose `convert_to_georeferencing()` builds a `Georeferencing` from the GML origin and offset vectors and caches it in a `mutable boost::optional`. From there the same object is handed to `GPlatesFileIO::RasterReader` / `RasterWriter` (the GDAL back end copies `parameters_type::components` straight into and out of GDAL's geotransform array), to `GPlatesAppLogic::RasterLayerProxy` and `RasterLayerParams`, to `GPlatesOpenGL::GLMultiResolutionRaster` for rendering, and to `GPlatesQtWidgets::EditAffineTransformGeoreferencingWidget` for editing. So it is the one neutral currency for "where is this raster on the globe", sitting between the GML model representation and everything that consumes rasters.

The parameter order is GDAL's, not ESRI's, and both `parameters_type` and `lat_lon_extents_type` are POD aggregates whose named fields overlay a `components[]` array through an anonymous union — that is what lets the GDAL reader and writer loop over them by index. The class stores *only* the affine form; the header discusses control-point georeferencing as the other general approach but a comment on the class states it is not implemented.

The design decision that drives most of the API is that the stored transform always uses **pixel registration**, with `top_left_x/y_coordinate` naming the top-left *corner of the top-left pixel box*, exactly as GDAL stores it. Grid-line registered data (NetCDF grids, where the data points sit *on* the grid lines and the extents describe pixel *centres*) is converted at the boundary: every `create`, `set_parameters`, `set_lat_lon_extents`, `reset_to_global_extents`, `get_parameters` and `get_lat_lon_extents` takes a `convert_from_/to_grid_line_registration` flag, and the private `convert_to_pixel_registration` overloads do the half-pixel shift. The `.cc` carries the algebra showing that only the origin coefficients C and F change under that conversion — the pixel width and height components are unaffected — and it is worth reading before touching any of it.

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

**The registration *flags* and the registration *methods* do different things.** `convert_from_/to_grid_line_registration` reinterprets the same set of data points — the transform's A, B, D and E coefficients are unchanged and only the origin moves by half a pixel. `contract_grid_line_to_pixel_registration` and `expand_pixel_to_grid_line_registration` genuinely rescale: they multiply the pixel width and height components by `(N-1)/N` (or its inverse) as well as shifting the origin, because they move the data points themselves. They are not the inverse of the flags, and mixing them up silently stretches the raster by one pixel.

**`expand_pixel_to_grid_line_registration` divides by `raster_width - 1`.** Neither it nor `contract_grid_line_to_pixel_registration` asserts on its dimensions, so a raster of width or height 1 (or 0) produces infinities or NaNs rather than an error. The lat-lon-extents overload of `convert_to_pixel_registration` *does* assert, through `GPlatesGlobal::Assert<PreconditionViolationError>`: dimensions must be non-zero for pixel registration and at least 2 for grid-line registration, because grid-line spacing is computed over `N-1` intervals. That covers only the entry points that take raster dimensions — `create(raster_width, raster_height, ...)`, `create(lat_lon_extents, ...)`, `set_lat_lon_extents` and `reset_to_global_extents`; `create()`, `create(parameters, ...)` and `set_parameters` take no dimensions and assert nothing.

**`get_lat_lon_extents` is partial, in two ways.** It returns `boost::none` if the transform rotates or shears (the B and D components are not almost-exactly zero), because extents cannot represent that; and it returns `boost::none` if the top or bottom *pixel centre* latitude falls outside `[-90, 90]`. Note the invariant it is testing: pixel *boxes* are allowed outside that range — global grid-line-registered extents necessarily put the top box edge above 90 — but centres are not. The check uses a deliberately loose `LATITUDE_EPISLON` of 1e-4 (spelt that way in the source) so that a round trip through grid-line registration does not push a legitimate raster out of range. `set_lat_lon_extents` does *not* validate this, so it is possible to store extents that a later `get_lat_lon_extents` cannot give back.

**Extents are signed, not ordered.** `top < bottom` or `left > right` is legal and means the raster is drawn flipped vertically or horizontally; equal values give a zero-height or zero-width raster. Do not normalise the ordering when you touch this data.

**Ownership.** The constructors and copy constructor are private and there is no assignment operator, so instances only ever exist behind `non_null_intrusive_ptr` from a `create` overload. Most consumers hold `non_null_ptr_to_const_type` and treat the object as immutable and shared; the mutators are for the editing widgets, which work on their own instance. `GPlatesUtils::ReferenceCount` uses `boost::detail::atomic_count`, so sharing a pointer across threads is safe; the object's *contents* are not protected, and since the whole state is one POD struct there is nothing stopping a concurrent `set_parameters` from tearing.

**`create()` with no arguments gives all-zero parameters,** which is a degenerate transform mapping every pixel to the origin — it is a placeholder to be filled in by `set_parameters`, not a usable default.

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
