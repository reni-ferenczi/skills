# GmlOrientableCurve

[Book TOC](../../TOC.md) · [property-values](../../components/property-values.md) · cluster Community 1050 · tier 2

| Source file | Kind | Lines |
|---|---|---|
| `src/property-values/GmlOrientableCurve.h` | C++ | 246 |
| `src/property-values/GmlOrientableCurve.cc` | C++ | 68 |

## Overview

`GmlOrientableCurve` is the `GPlatesModel::PropertyValue` for GML's
`gml:OrientableCurve`, which exists in the GML schema purely to attach a
direction and a set of XML attributes to another curve. GPlates only ever
wraps a `GmlLineString` as the `d_base_curve` (the type substitutable for
`gml:_Curve` in the schema is not enforced at construction time — the header
notes this is not verified), so in practice this class is a thin decorator:
it forwards `print_to()` straight to the base curve and holds a
`std::map<XmlAttributeName, XmlAttributeValue>` alongside it. `deep_clone()`
recursively clones `d_base_curve` rather than sharing it, so a deep-cloned
`GmlOrientableCurve` owns an independent copy of its geometry.

## Declared types

| Name | Kind | Bases | Template | Subclasses | Description |
|---|---|---|---|---|---|
| [`GPlatesPropertyValues::GmlOrientableCurve`](#gplatespropertyvaluesgmlorientablecurve) | class | [`GPlatesModel::PropertyValue`](../model/PropertyValue.md) | — | 0 | This class implements the PropertyValue which corresponds to "gml:OrientableCurve". |

## Members

### `GPlatesPropertyValues::GmlOrientableCurve`

| Member | Kind | Type | Access | Description |
|---|---|---|---|---|
| `non_null_ptr_type` | typedef | `GPlatesUtils::non_null_intrusive_ptr<GmlOrientableCurve>` | public | A convenience typedef for GPlatesUtils::non\_null\_intrusive\_ptr\<GmlOrientableCurve\>. |
| `non_null_ptr_to_const_type` | typedef | `GPlatesUtils::non_null_intrusive_ptr<const GmlOrientableCurve>` | public | A convenience typedef for GPlatesUtils::non\_null\_intrusive\_ptr\<const GmlOrientableCurve\>. |
| `~GmlOrientableCurve()` | destructor | `None` | public | — |
| `create( GmlLineString::non_null_ptr_type base_curve_, const std::map<GPlatesModel::XmlAttributeName, GPlatesModel::XmlAttributeValue> & xml_attributes_)` | method | `non_null_ptr_type` | public | Create a GmlOrientableCurve instance which contains a "base curve". |
| `clone()` | method | `non_null_ptr_type` | public | — |
| `deep_clone()` | method | `non_null_ptr_type` | public | — |
| `DEFINE_FUNCTION_DEEP_CLONE_AS_PROP_VAL()` | method | `None` | public | — |
| `base_curve()` | method | `GmlLineString::non_null_ptr_to_const_type` | public | Access the 'const' PropertyValue which is the "base curve" of this instance. |
| `set_base_curve( GmlLineString::non_null_ptr_type bc)` | method | `void` | public | Set the "base curve" of this instance to bc. |
| `get_structural_type()` | method | `StructuralType` | public | Returns the structural type associated with this property value class. |
| `accept_visitor( GPlatesModel::ConstFeatureVisitor &visitor)` | method | `void` | public | Accept a ConstFeatureVisitor instance. |
| `accept_visitor( GPlatesModel::FeatureVisitor &visitor)` | method | `void` | public | Accept a FeatureVisitor instance. |
| `print_to` | field | `std::ostream` | public | — |
| `GmlOrientableCurve( GmlLineString::non_null_ptr_type base_curve_, const std::map<GPlatesModel::XmlAttributeName, GPlatesModel::XmlAttributeValue> & xml_attributes_)` | constructor | `None` | protected | This constructor should not be public, because we don't want to allow instantiation of this type on the stack. |
| `GmlOrientableCurve( const GmlOrientableCurve &other)` | constructor | `None` | protected | This constructor should not be public, because we don't want to allow instantiation of this type on the stack. |
| `directly_modifiable_fields_equal( const GPlatesModel::PropertyValue &other)` | method | `bool` | protected | — |
| `d_base_curve` | field | `GmlLineString::non_null_ptr_type` | private | — |
| `d_xml_attributes` | field | `std::map<GPlatesModel::XmlAttributeName, GPlatesModel::XmlAttributeValue>` | private | — |
| `operator=` | field | `GmlOrientableCurve` | private | This operator should never be defined, because we don't want/need to allow copy-assignment: All copying should use the virtual copy-constructor 'clone' (which will in turn use the copy-constructor); all "assignment" should really only be ... |

## Free functions and macros

| Name | Kind | Type / body | Description |
|---|---|---|---|
| `GPLATES_PROPERTYVALUES_GMLORIENTABLECURVE_H` | macro | `None` | — |

## Notes

- `directly_modifiable_fields_equal()` compares both the base curve (by value,
  via `operator==`) and the XML attribute map; a `dynamic_cast` failure is
  treated as "should never happen" and returns `false` rather than throwing.
- `base_curve()` has both a `const` overload (returning
  `non_null_ptr_to_const_type`) and a non-`const` overload (returning
  `non_null_ptr_type`), so mutable access to the wrapped `GmlLineString` is
  available without going through `set_base_curve()`.

## Used by

| Unit | Component | References |
|---|---|---|
| [app-logic/ReconstructMethodHalfStageRotation](../app-logic/ReconstructMethodHalfStageRotation.md) | app-logic | 3 |
| [app-logic/TopologyInternalUtils](../app-logic/TopologyInternalUtils.md) | app-logic | 3 |
| [file-io/GpmlPropertyStructuralTypeReaderUtils](../file-io/GpmlPropertyStructuralTypeReaderUtils.md) | file-io | 3 |
| [app-logic/GeometryUtils](../app-logic/GeometryUtils.md) | app-logic | 2 |
| [app-logic/PartitionFeatureUtils](../app-logic/PartitionFeatureUtils.md) | app-logic | 2 |
| [app-logic/ReconstructMethodByPlateId](../app-logic/ReconstructMethodByPlateId.md) | app-logic | 2 |
| [app-logic/ScalarCoverageFeatureProperties](../app-logic/ScalarCoverageFeatureProperties.md) | app-logic | 2 |
| [app-logic/deprecated/ReconstructedFeatureGeometryPopulator](../app-logic/deprecated/ReconstructedFeatureGeometryPopulator.md) | app-logic | 2 |
| [feature-visitors/GeometryFinder](../feature-visitors/GeometryFinder.md) | feature-visitors | 2 |
| [feature-visitors/GeometryRotator](../feature-visitors/GeometryRotator.md) | feature-visitors | 2 |
| [feature-visitors/GeometrySetter](../feature-visitors/GeometrySetter.md) | feature-visitors | 2 |
| [feature-visitors/GeometryTypeFinder](../feature-visitors/GeometryTypeFinder.md) | feature-visitors | 2 |
| [feature-visitors/QueryFeaturePropertiesWidgetPopulator](../feature-visitors/QueryFeaturePropertiesWidgetPopulator.md) | feature-visitors | 2 |
| [feature-visitors/ViewFeatureGeometriesWidgetPopulator](../feature-visitors/ViewFeatureGeometriesWidgetPopulator.md) | feature-visitors | 2 |
| [file-io/GMTFormatHeader](../file-io/GMTFormatHeader.md) | file-io | 2 |
| [file-io/GpmlOutputVisitor](../file-io/GpmlOutputVisitor.md) | file-io | 2 |
| [file-io/OgrFeatureCollectionWriter](../file-io/OgrFeatureCollectionWriter.md) | file-io | 2 |
| [file-io/PlatesLineFormatWriter](../file-io/PlatesLineFormatWriter.md) | file-io | 2 |
| [file-io/deprecated/GpmlOnePointFiveOutputVisitor](../file-io/deprecated/GpmlOnePointFiveOutputVisitor.md) | file-io | 2 |
| [model/ModelUtils](../model/ModelUtils.md) | model | 2 |

*... and 13 more units.*

## Related

*None.*

## Explore

Run these from the `gplates-code` skill directory:

```bash
python scripts/gpq.py file src/property-values/GmlOrientableCurve.h
python scripts/gpq.py def GPlatesPropertyValues::GmlOrientableCurve --body
python scripts/gpq.py uses GmlOrientableCurve --kind class
python scripts/gpq.py hier GmlOrientableCurve
```
