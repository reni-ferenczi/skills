# ProxiedRasterCache

[Book TOC](../../TOC.md) · [property-values](../../components/property-values.md) · cluster Community 494 · tier 3

| Source file | Kind | Lines |
|---|---|---|
| `src/property-values/ProxiedRasterCache.h` | C++ | 127 |
| `src/property-values/ProxiedRasterCache.cc` | C++ | 199 |

## Overview

[[[PROSE overview unit=property-values/ProxiedRasterCache tier=3]]]
Replace this whole block, markers included, with 1-3 paragraphs: what this unit is, why it exists, and how it fits the surrounding design. Do not restate the tables below.
[[[/PROSE]]]

## Declared types

| Name | Kind | Bases | Template | Subclasses | Description |
|---|---|---|---|---|---|
| [`(anonymous)::ConcreteProxiedRasterCacheImpl`](#anonymousconcreteproxiedrastercacheimpl) | class | [`ProxiedRasterCacheInternals::ProxiedRasterCacheImpl`](ProxiedRasterCache.md) | — | 0 | — |
| [`GPlatesPropertyValues::ProxiedRasterCache`](#gplatespropertyvaluesproxiedrastercache) | class | [`GPlatesUtils::ReferenceCount<ProxiedRasterCache>`](../utils/ReferenceCount.md) | — | 0 | This class maintains updated proxied RawRasters for each band in a given raster file. |
| [`GPlatesPropertyValues::ProxiedRasterCacheInternals::ProxiedRasterCacheImpl`](#gplatespropertyvaluesproxiedrastercacheinternalsproxiedrastercacheimpl) | class | — | — | 1 | — |

## Members

### `(anonymous)::ConcreteProxiedRasterCacheImpl`

| Member | Kind | Type | Access | Description |
|---|---|---|---|---|
| `ConcreteProxiedRasterCacheImpl( const TextContent &file_name, GPlatesFileIO::ReadErrorAccumulation *read_errors = NULL)` | constructor | `None` | public | — |
| `get_spatial_reference_system()` | method | `boost::optional<SpatialReferenceSystem::non_null_ptr_to_const_type>` | public | FIXME: This will no longer be needed once we store the raster spatial reference system in a new property value. |
| `set_file_name( const TextContent &file_name, GPlatesFileIO::ReadErrorAccumulation *read_errors)` | method | `void` | public | — |
| `update_proxied_raw_rasters( bool force, GPlatesFileIO::ReadErrorAccumulation *read_errors = NULL)` | method | `void` | private | If force is true, will update proxied RawRasters if file exists. |
| `d_file_name` | field | `TextContent` | private | — |
| `d_file_name_as_qstring` | field | `QString` | private | — |
| `d_last_modified` | field | `QDateTime` | private | — |
| `d_proxied_raw_rasters` | field | `std::vector<RawRaster::non_null_ptr_type>` | private | — |
| `d_spatial_reference_system` | field | `boost::optional<SpatialReferenceSystem::non_null_ptr_to_const_type>` | private | — |

### `GPlatesPropertyValues::ProxiedRasterCache`

| Member | Kind | Type | Access | Description |
|---|---|---|---|---|
| `non_null_ptr_type` | typedef | `GPlatesUtils::non_null_intrusive_ptr<ProxiedRasterCache>` | public | — |
| `non_null_ptr_to_const_type` | typedef | `GPlatesUtils::non_null_intrusive_ptr<const ProxiedRasterCache>` | public | — |
| `create( const TextContent &file_name, GPlatesFileIO::ReadErrorAccumulation *read_errors = NULL)` | method | `non_null_ptr_type` | public | — |
| `proxied_raw_rasters` | field | `std::vector<RawRaster::non_null_ptr_type>` | public | — |
| `get_spatial_reference_system()` | method | `boost::optional<SpatialReferenceSystem::non_null_ptr_to_const_type>` | public | FIXME: This will no longer be needed once we store the raster spatial reference system in a new property value. |
| `set_file_name( const TextContent &file_name, GPlatesFileIO::ReadErrorAccumulation *read_errors = NULL)` | method | `void` | public | — |
| `ProxiedRasterCache( const TextContent &file_name, GPlatesFileIO::ReadErrorAccumulation *read_errors)` | constructor | `None` | private | — |
| `d_impl` | field | `boost::scoped_ptr<ProxiedRasterCacheInternals::ProxiedRasterCacheImpl>` | private | — |

### `GPlatesPropertyValues::ProxiedRasterCacheInternals::ProxiedRasterCacheImpl`

| Member | Kind | Type | Access | Description |
|---|---|---|---|---|
| `~ProxiedRasterCacheImpl()` | destructor | `None` | public | — |
| `proxied_raw_rasters` | field | `std::vector<RawRaster::non_null_ptr_type>` | public | — |
| `get_spatial_reference_system()` | method | `boost::optional<SpatialReferenceSystem::non_null_ptr_to_const_type>` | public | FIXME: This will no longer be needed once we store the raster spatial reference system in a new property value. |
| `set_file_name( const TextContent &file_name, GPlatesFileIO::ReadErrorAccumulation *read_errors)` | method | `void` | public | — |

## Free functions and macros

| Name | Kind | Type / body | Description |
|---|---|---|---|
| `GPLATES_PROPERTYVALUES_PROXIEDRASTERCACHE_H` | macro | `None` | — |

## Notes

[[[PROSE notes unit=property-values/ProxiedRasterCache tier=3]]]
Replace this whole block, markers included, with invariants, ownership, threading or gotchas that are not visible in the tables. Write *None.* if there is nothing worth saying.
[[[/PROSE]]]

## Used by

| Unit | Component | References |
|---|---|---|
| [property-values/GmlFile](GmlFile.md) | property-values | 3 |

## Related

*None.*

## Explore

Run these from the `gplates-code` skill directory:

```bash
python scripts/gpq.py file src/property-values/ProxiedRasterCache.h
python scripts/gpq.py def (anonymous)::ConcreteProxiedRasterCacheImpl --body
python scripts/gpq.py uses ConcreteProxiedRasterCacheImpl --kind class
python scripts/gpq.py hier ConcreteProxiedRasterCacheImpl
```
