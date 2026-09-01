# GLScalarField3DGenerator

[Book TOC](../../TOC.md) · [opengl](../../components/opengl.md) · cluster Community 844 · tier 2

| Source file | Kind | Lines |
|---|---|---|
| `src/opengl/GLScalarField3DGenerator.h` | C++ | 204 |
| `src/opengl/GLScalarField3DGenerator.cc` | C++ | 1044 |

## Overview

[[[PROSE overview unit=opengl/GLScalarField3DGenerator tier=2]]]
Replace this whole block, markers included, with 1-3 paragraphs: what this unit is, why it exists, and how it fits the surrounding design. Do not restate the tables below.
[[[/PROSE]]]

## Declared types

| Name | Kind | Bases | Template | Subclasses | Description |
|---|---|---|---|---|---|
| [`GPlatesOpenGL::GLScalarField3DGenerator`](#gplatesopenglglscalarfield3dgenerator) | class | [`GPlatesUtils::ReferenceCount<GLScalarField3DGenerator>`](../utils/ReferenceCount.md) | — | 0 | Generates a 3D sub-surface scalar field from a sequence of concentric depth layer 2D rasters. |

## Members

### `GPlatesOpenGL::GLScalarField3DGenerator`

| Member | Kind | Type | Access | Description |
|---|---|---|---|---|
| `non_null_ptr_type` | typedef | `GPlatesUtils::non_null_intrusive_ptr<GLScalarField3DGenerator>` | public | A convenience typedef for a shared pointer to a non-const GLScalarField3DGenerator. |
| `non_null_ptr_to_const_type` | typedef | `GPlatesUtils::non_null_intrusive_ptr<const GLScalarField3DGenerator>` | public | A convenience typedef for a shared pointer to a const GLScalarField3DGenerator. |
| `DepthLayer` | struct | `None` | public | A single depth layer contributing to the 3D scalar field. |
| `depth_layer_seq_type` | typedef | `std::vector<DepthLayer>` | public | — |
| `is_supported( GLRenderer &renderer)` | method | `bool` | public | Returns true if generation of 3D scalar fields is supported on the runtime system. |
| `create( GLRenderer &renderer, const QString &scalar_field_filename, const GPlatesPropertyValues::Georeferencing::non_null_ptr_to_const_type &georeferencing, const GPlatesPropertyValues::CoordinateTransformation::non_null_ptr_to_const_type &coordinate_transformation, unsigned int depth_layer_width, unsigned int depth_la ...` | method | `non_null_ptr_type` | public | Creates a GLScalarField3DGenerator object. scalar\_field\_filename is name of the file to contain the generated scalar field. georeferencing all depth layer rasters have the same georeferencing. depth\_layers the depth layer rasters used to ... |
| `generate_scalar_field( GLRenderer &renderer, GPlatesFileIO::ReadErrorAccumulation *read_errors)` | method | `bool` | public | Generate and write the scalar field to file. |
| `d_scalar_field_filename` | field | `QString` | private | — |
| `d_georeferencing` | field | `GPlatesPropertyValues::Georeferencing::non_null_ptr_to_const_type` | private | — |
| `d_coordinate_transformation` | field | `GPlatesPropertyValues::CoordinateTransformation::non_null_ptr_to_const_type` | private | — |
| `d_depth_layers` | field | `depth_layer_seq_type` | private | — |
| `d_depth_layers_source` | field | `boost::optional<GLScalarFieldDepthLayersSource::non_null_ptr_type>` | private | — |
| `d_multi_resolution_raster` | field | `boost::optional<GLMultiResolutionRaster::non_null_ptr_type>` | private | — |
| `d_cube_face_dimension` | field | `unsigned int` | private | — |
| `GLScalarField3DGenerator( GLRenderer &renderer, const QString &scalar_field_filename, const GPlatesPropertyValues::Georeferencing::non_null_ptr_to_const_type &georeferencing, const GPlatesPropertyValues::CoordinateTransformation::non_null_ptr_to_const_type &coordinate_transformation, unsigned int depth_layer_width, uns ...` | constructor | `None` | private | Constructor. |
| `initialise_multi_resolution_raster( GLRenderer &renderer, GPlatesFileIO::ReadErrorAccumulation *read_errors)` | method | `bool` | private | — |
| `initialise_cube_face_dimension( GLRenderer &renderer)` | method | `void` | private | — |
| `report_recoverable_error( GPlatesFileIO::ReadErrorAccumulation *read_errors, GPlatesFileIO::ReadErrors::Description description)` | method | `void` | private | — |
| `report_failure_to_begin( GPlatesFileIO::ReadErrorAccumulation *read_errors, GPlatesFileIO::ReadErrors::Description description)` | method | `void` | private | — |
| `generate_scalar_field_depth_tile( GLRenderer &renderer, QDataStream &out, unsigned int depth_layer_index, const std::vector<GLMultiResolutionRaster::tile_handle_type> &source_raster_tile_handles, const GLPixelBuffer::shared_ptr_type &pixel_buffer, unsigned int tile_resolution, double &tile_scalar_min, double &tile_scal ...` | method | `void` | private | — |
| `generate_scalar_field_tile_mask( GLRenderer &renderer, const GLPixelBuffer::shared_ptr_type &pixel_buffer, unsigned int tile_resolution, std::vector<GPlatesFileIO::ScalarField3DFileFormat::MaskDataSample> &mask_data_array)` | method | `void` | private | — |

## Free functions and macros

| Name | Kind | Type / body | Description |
|---|---|---|---|
| `RENDER_TEST_SCALAR_FIELD_VERTEX_SHADER` | variable | `char` | — |
| `RENDER_TEST_SCALAR_FIELD_FRAGMENT_SHADER` | variable | `char` | — |
| `GPLATES_OPENGL_GLSCALARFIELD3DGENERATOR_H` | macro | `None` | — |

## Notes

[[[PROSE notes unit=opengl/GLScalarField3DGenerator tier=2]]]
Replace this whole block, markers included, with invariants, ownership, threading or gotchas that are not visible in the tables. Write *None.* if there is nothing worth saying.
[[[/PROSE]]]

## Used by

| Unit | Component | References |
|---|---|---|
| [qt-widgets/ImportScalarField3DDialog](../qt-widgets/ImportScalarField3DDialog.md) | qt-widgets | 9 |

## Related

*None.*

## Explore

Run these from the `gplates-code` skill directory:

```bash
python scripts/gpq.py file src/opengl/GLScalarField3DGenerator.h
python scripts/gpq.py def GPlatesOpenGL::GLScalarField3DGenerator --body
python scripts/gpq.py uses GLScalarField3DGenerator --kind class
python scripts/gpq.py hier GLScalarField3DGenerator
```
