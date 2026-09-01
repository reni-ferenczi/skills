# SpatialReferenceSystem

[Book TOC](../../TOC.md) · [property-values](../../components/property-values.md) · cluster Community 1238 · tier 2

| Source file | Kind | Lines |
|---|---|---|
| `src/property-values/SpatialReferenceSystem.h` | C++ | 145 |
| `src/property-values/SpatialReferenceSystem.cc` | C++ | 102 |

## Overview

`SpatialReferenceSystem` wraps GDAL/OGR's `OGRSpatialReference`, giving GPlates code a reference-counted handle it can pass around (via `non_null_ptr_type`) instead of managing the C-API's own reference counting directly. `create()` clones the given `OGRSpatialReference` into a freshly allocated one owned by this object, and `get_WGS84()` provides a shared, lazily-constructed constant for the common WGS84 case, including a GDAL-3.0-specific `SetAxisMappingStrategy()` call to keep longitude-first, latitude-second axis order across GDAL versions.

`get_ogr_srs()` exposes the wrapped `OGRSpatialReference` by reference for callers — such as `CoordinateTransformation` and the OGR/GDAL readers and writers — that need to hand it directly to OGR/GDAL APIs.

## Declared types

| Name | Kind | Bases | Template | Subclasses | Description |
|---|---|---|---|---|---|
| [`GPlatesPropertyValues::SpatialReferenceSystem`](#gplatespropertyvaluesspatialreferencesystem) | class | [`GPlatesUtils::ReferenceCount<SpatialReferenceSystem>`](../utils/ReferenceCount.md) | — | 0 | A spatial reference system. |

## Members

### `GPlatesPropertyValues::SpatialReferenceSystem`

| Member | Kind | Type | Access | Description |
|---|---|---|---|---|
| `non_null_ptr_type` | typedef | `GPlatesUtils::non_null_intrusive_ptr<SpatialReferenceSystem>` | public | — |
| `non_null_ptr_to_const_type` | typedef | `GPlatesUtils::non_null_intrusive_ptr<const SpatialReferenceSystem>` | public | — |
| `get_WGS84()` | method | `non_null_ptr_to_const_type` | public | Spatial reference system for standard "WGS84". |
| `create( const OGRSpatialReference &ogr_srs)` | method | `non_null_ptr_type` | public | Creates a spatial reference system. |
| `~SpatialReferenceSystem()` | destructor | `None` | public | — |
| `is_geographic()` | method | `bool` | public | Returns true if this spatial reference system is a geographic coordinate system. |
| `is_projected()` | method | `bool` | public | Returns true if this spatial reference system is a projected coordinate system. |
| `is_wgs84()` | method | `bool` | public | Returns true if the spatial reference system is WGS84. |
| `OGRSpatialReferenceReleaser` | struct | `None` | private | Release our reference count (ie, decrement OGR reference count in OGRSpatialReference) when all our boost 'd\_ogr\_srs' references to the OGRSpatialReference object are destroyed. |
| `d_ogr_srs` | field | `boost::shared_ptr<OGRSpatialReference>` | private | — |
| `SpatialReferenceSystem( const OGRSpatialReference &ogr_srs)` | constructor | `None` | private | — |

## Free functions and macros

| Name | Kind | Type / body | Description |
|---|---|---|---|
| `operator()( OGRSpatialReference *ogr_srs)` | operator | `void` | — |
| `GPLATES_PROPERTY_VALUES_SPATIALREFERENCESYSTEM_H` | macro | `None` | — |
| `DISABLE_MSVC_WARNING` | variable | `PUSH_MSVC_WARNINGS` | — |

## Notes

The wrapped `OGRSpatialReference` is deliberately allocated with `OSRNewSpatialReference()` rather than `new`, so it lives in OGR's own memory heap — on Windows, each DLL can have a separate heap, so an object allocated by GPlates and freed by OGR (or vice versa) could otherwise corrupt memory. `OGRSpatialReferenceReleaser` releases it via `OSRRelease()` (an OGR reference-count decrement, not necessarily a delete) instead of a plain destructor call, because `get_ogr_srs()` lets external OGR/GDAL code take its own reference to the same object; the underlying `OGRSpatialReference` is only actually destroyed once every such reference, not just this wrapper, has released it.

## Used by

| Unit | Component | References |
|---|---|---|
| [property-values/CoordinateTransformation](CoordinateTransformation.md) | property-values | 23 |
| [file-io/FeatureCollectionFileFormatConfigurations](../file-io/FeatureCollectionFileFormatConfigurations.md) | file-io | 10 |
| [file-io/OgrWriter](../file-io/OgrWriter.md) | file-io | 7 |
| [qt-widgets/OgrSrsWriteOptionDialog](../qt-widgets/OgrSrsWriteOptionDialog.md) | qt-widgets | 7 |
| [property-values/ProxiedRasterCache](ProxiedRasterCache.md) | property-values | 6 |
| [app-logic/ExtractRasterFeatureProperties](../app-logic/ExtractRasterFeatureProperties.md) | app-logic | 4 |
| [file-io/OgrFeatureCollectionWriter](../file-io/OgrFeatureCollectionWriter.md) | file-io | 4 |
| [file-io/RasterReader](../file-io/RasterReader.md) | file-io | 4 |
| [file-io/RasterWriter](../file-io/RasterWriter.md) | file-io | 4 |
| [gui/ExportRasterAnimationStrategy](../gui/ExportRasterAnimationStrategy.md) | gui | 4 |
| [app-logic/RasterLayerParams](../app-logic/RasterLayerParams.md) | app-logic | 3 |
| [app-logic/RasterLayerProxy](../app-logic/RasterLayerProxy.md) | app-logic | 3 |
| [file-io/GdalRasterWriter](../file-io/GdalRasterWriter.md) | file-io | 3 |
| [file-io/OgrReader](../file-io/OgrReader.md) | file-io | 3 |
| [gui/FileIOFeedback](../gui/FileIOFeedback.md) | gui | 3 |
| [property-values/GmlFile](GmlFile.md) | property-values | 3 |
| [file-io/GsmlPropertyHandlers](../file-io/GsmlPropertyHandlers.md) | file-io | 2 |
| [qt-widgets/ImportScalarField3DDialog](../qt-widgets/ImportScalarField3DDialog.md) | qt-widgets | 2 |
| [file-io/GdalRasterReader](../file-io/GdalRasterReader.md) | file-io | 1 |
| [file-io/RgbaRasterReader](../file-io/RgbaRasterReader.md) | file-io | 1 |

*... and 1 more units.*

## Related

*None.*

## Explore

Run these from the `gplates-code` skill directory:

```bash
python scripts/gpq.py file src/property-values/SpatialReferenceSystem.h
python scripts/gpq.py def GPlatesPropertyValues::SpatialReferenceSystem --body
python scripts/gpq.py uses SpatialReferenceSystem --kind class
python scripts/gpq.py hier SpatialReferenceSystem
```
