# GpmlRasterBandNames

[Book TOC](../../TOC.md) · [property-values](../../components/property-values.md) · cluster Community 1072 · tier 2

| Source file | Kind | Lines |
|---|---|---|
| `src/property-values/GpmlRasterBandNames.h` | C++ | 215 |
| `src/property-values/GpmlRasterBandNames.cc` | C++ | 46 |

## Overview

`GpmlRasterBandNames` implements the `gpml:RasterBandNames` property value: an ordered list of `XsString` names, one per band, that a multi-band raster feature carries so consumers can identify which raster layer or channel a band corresponds to (for example when a raster co-registration or export step needs to pick a named band rather than an index). `app-logic/RasterLayerProxy` and `app-logic/ExtractRasterFeatureProperties` read this list to resolve raster layers by band name.

Like the other simple property values in this component, it stores its data by value and defers all mutation bookkeeping to `update_instance_id()`, called from `set_band_names()`.

## Declared types

| Name | Kind | Bases | Template | Subclasses | Description |
|---|---|---|---|---|---|
| [`GPlatesPropertyValues::GpmlRasterBandNames`](#gplatespropertyvaluesgpmlrasterbandnames) | class | [`GPlatesModel::PropertyValue`](../model/PropertyValue.md) | — | 0 | This class implements the PropertyValue which corresponds to "gpml:RasterBandNames". |

## Members

### `GPlatesPropertyValues::GpmlRasterBandNames`

| Member | Kind | Type | Access | Description |
|---|---|---|---|---|
| `non_null_ptr_type` | typedef | `GPlatesUtils::non_null_intrusive_ptr<GpmlRasterBandNames>` | public | A convenience typedef for GPlatesUtils::non\_null\_intrusive\_ptr\<GpmlRasterBandNames\>. |
| `non_null_ptr_to_const_type` | typedef | `GPlatesUtils::non_null_intrusive_ptr<const GpmlRasterBandNames>` | public | A convenience typedef for GPlatesUtils::non\_null\_intrusive\_ptr\<const GpmlRasterBandNames\>. |
| `~GpmlRasterBandNames()` | destructor | `None` | public | — |
| `band_names_list_type` | typedef | `std::vector<XsString::non_null_ptr_to_const_type>` | public | — |
| `create( const band_names_list_type &band_names_)` | method | `non_null_ptr_type` | public | Create a GpmlRasterBandNames instance from a collection of band\_names\_. |
| `create( ForwardIterator begin, ForwardIterator end)` | method | `non_null_ptr_type` | public | — |
| `clone()` | method | `non_null_ptr_type` | public | — |
| `deep_clone()` | method | `non_null_ptr_type` | public | — |
| `DEFINE_FUNCTION_DEEP_CLONE_AS_PROP_VAL()` | method | `None` | public | — |
| `set_band_names( const band_names_list_type &band_names_)` | method | `void` | public | Sets the internal band names. |
| `get_structural_type()` | method | `StructuralType` | public | Returns the structural type associated with this property value class. |
| `accept_visitor( GPlatesModel::ConstFeatureVisitor &visitor)` | method | `void` | public | Accept a ConstFeatureVisitor instance. |
| `accept_visitor( GPlatesModel::FeatureVisitor &visitor)` | method | `void` | public | Accept a FeatureVisitor instance. |
| `print_to` | field | `std::ostream` | public | — |
| `GpmlRasterBandNames( const band_names_list_type &band_names_)` | constructor | `None` | protected | This constructor should not be public, because we don't want to allow instantiation of this type on the stack. |
| `GpmlRasterBandNames( ForwardIterator begin, ForwardIterator end)` | constructor | `None` | protected | — |
| `GpmlRasterBandNames( const GpmlRasterBandNames &other)` | constructor | `None` | protected | This constructor should not be public, because we don't want to allow instantiation of this type on the stack. |
| `d_band_names` | field | `band_names_list_type` | private | — |
| `operator=` | field | `GpmlRasterBandNames` | private | This operator should never be defined, because we don't want/need to allow copy-assignment: All copying should use the virtual copy-constructor 'clone' (which will in turn use the copy-constructor); all "assignment" should really only be ... |

## Free functions and macros

| Name | Kind | Type / body | Description |
|---|---|---|---|
| `GPLATES_PROPERTYVALUES_GPMLRASTERBANDNAMES_H` | macro | `None` | — |

## Notes

*None.*

## Used by

| Unit | Component | References |
|---|---|---|
| [app-logic/ExtractRasterFeatureProperties](../app-logic/ExtractRasterFeatureProperties.md) | app-logic | 5 |
| [app-logic/RasterLayerParams](../app-logic/RasterLayerParams.md) | app-logic | 5 |
| [app-logic/RasterLayerProxy](../app-logic/RasterLayerProxy.md) | app-logic | 5 |
| [file-io/GpmlPropertyStructuralTypeReaderUtils](../file-io/GpmlPropertyStructuralTypeReaderUtils.md) | file-io | 3 |
| [gui/ExportRasterAnimationStrategy](../gui/ExportRasterAnimationStrategy.md) | gui | 3 |
| [file-io/GpmlOutputVisitor](../file-io/GpmlOutputVisitor.md) | file-io | 2 |
| [qt-widgets/CoRegistrationLayerConfigurationDialog](../qt-widgets/CoRegistrationLayerConfigurationDialog.md) | qt-widgets | 2 |
| [data-mining/GetValueFromPropertyVisitor](../data-mining/GetValueFromPropertyVisitor.md) | data-mining | 1 |
| [qt-widgets/ImportRasterDialog](../qt-widgets/ImportRasterDialog.md) | qt-widgets | 1 |
| [qt-widgets/RasterLayerOptionsWidget](../qt-widgets/RasterLayerOptionsWidget.md) | qt-widgets | 1 |
| [utils/GetPropertyAsPythonObjVisitor](../utils/GetPropertyAsPythonObjVisitor.md) | utils | 1 |
| [view-operations/RenderedGeometryFactory](../view-operations/RenderedGeometryFactory.md) | view-operations | 1 |
| [view-operations/RenderedResolvedRaster](../view-operations/RenderedResolvedRaster.md) | view-operations | 1 |

## Related

*None.*

## Explore

Run these from the `gplates-code` skill directory:

```bash
python scripts/gpq.py file src/property-values/GpmlRasterBandNames.h
python scripts/gpq.py def GPlatesPropertyValues::GpmlRasterBandNames --body
python scripts/gpq.py uses GpmlRasterBandNames --kind class
python scripts/gpq.py hier GpmlRasterBandNames
```
