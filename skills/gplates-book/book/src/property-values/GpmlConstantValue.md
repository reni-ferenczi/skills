# GpmlConstantValue

[Book TOC](../../TOC.md) · [property-values](../../components/property-values.md) · cluster Community 649 · tier 2

| Source file | Kind | Lines |
|---|---|---|
| `src/property-values/GpmlConstantValue.h` | C++ | 249 |
| `src/property-values/GpmlConstantValue.cc` | C++ | 69 |

## Overview

`GpmlConstantValue` is the GPML `TimeConstantPropertyValue` wrapper: it holds a single inner `PropertyValue` (`d_value`) that is presented as being constant across all reconstruction times, plus the `StructuralType` of that inner value and an optional textual `description`. It exists because GPML property values that can vary in time (e.g. irregular samples, piecewise aggregations) share a structural-type slot with values that never vary, and `GpmlConstantValue` is the "never varies" case in that time-dependent-property-value family.

Because GPlates property values are always heap-allocated and managed through `non_null_intrusive_ptr`, construction goes exclusively through the `create` factory functions, with the constructors kept `protected`. `deep_clone` recurses into the wrapped value via `deep_clone_as_prop_val`, so cloning a `GpmlConstantValue` also clones whatever it wraps rather than sharing it. `accept_visitor` dispatches to `visit_gpml_constant_value` on `GPlatesModel::FeatureVisitor`/`ConstFeatureVisitor`, which is how feature visitors that only care about the wrapped value (rather than the constant-value envelope) get at it.

## Declared types

| Name | Kind | Bases | Template | Subclasses | Description |
|---|---|---|---|---|---|
| [`GPlatesPropertyValues::GpmlConstantValue`](#gplatespropertyvaluesgpmlconstantvalue) | class | [`GPlatesModel::PropertyValue`](../model/PropertyValue.md) | — | 0 | — |

## Members

### `GPlatesPropertyValues::GpmlConstantValue`

| Member | Kind | Type | Access | Description |
|---|---|---|---|---|
| `non_null_ptr_type` | typedef | `GPlatesUtils::non_null_intrusive_ptr<GpmlConstantValue>` | public | A convenience typedef for GPlatesUtils::non\_null\_intrusive\_ptr\<GpmlConstantValue\>. |
| `non_null_ptr_to_const_type` | typedef | `GPlatesUtils::non_null_intrusive_ptr<const GpmlConstantValue>` | public | A convenience typedef for GPlatesUtils::non\_null\_intrusive\_ptr\<const GpmlConstantValue\>. |
| `~GpmlConstantValue()` | destructor | `None` | public | — |
| `create( GPlatesModel::PropertyValue::non_null_ptr_type value_, const StructuralType &value_type_)` | method | `non_null_ptr_type` | public | — |
| `create( GPlatesModel::PropertyValue::non_null_ptr_type value_, const StructuralType &value_type_, const GPlatesUtils::UnicodeString &description_)` | method | `non_null_ptr_type` | public | — |
| `clone()` | method | `non_null_ptr_type` | public | — |
| `deep_clone()` | method | `non_null_ptr_type` | public | — |
| `DEFINE_FUNCTION_DEEP_CLONE_AS_PROP_VAL()` | method | `None` | public | — |
| `value()` | method | `GPlatesModel::PropertyValue::non_null_ptr_to_const_type` | public | — |
| `set_value( GPlatesModel::PropertyValue::non_null_ptr_type v)` | method | `void` | public | Sets the internal property value. |
| `set_description( const GPlatesUtils::UnicodeString &new_description)` | method | `void` | public | — |
| `get_structural_type()` | method | `StructuralType` | public | Returns the structural type associated with this property value class. |
| `accept_visitor( GPlatesModel::ConstFeatureVisitor &visitor)` | method | `void` | public | Accept a ConstFeatureVisitor instance. |
| `accept_visitor( GPlatesModel::FeatureVisitor &visitor)` | method | `void` | public | Accept a FeatureVisitor instance. |
| `print_to` | field | `std::ostream` | public | — |
| `GpmlConstantValue( GPlatesModel::PropertyValue::non_null_ptr_type value_, const StructuralType &value_type_)` | constructor | `None` | protected | This constructor should not be public, because we don't want to allow instantiation of this type on the stack. |
| `GpmlConstantValue( GPlatesModel::PropertyValue::non_null_ptr_type value_, const StructuralType &value_type_, const GPlatesUtils::UnicodeString &description_)` | constructor | `None` | protected | This constructor should not be public, because we don't want to allow instantiation of this type on the stack. |
| `GpmlConstantValue( const GpmlConstantValue &other)` | constructor | `None` | protected | This constructor should not be public, because we don't want to allow instantiation of this type on the stack. |
| `directly_modifiable_fields_equal( const PropertyValue &other)` | method | `bool` | protected | — |
| `d_value` | field | `GPlatesModel::PropertyValue::non_null_ptr_type` | private | — |
| `d_value_type` | field | `StructuralType` | private | — |
| `d_description` | field | `GPlatesUtils::UnicodeString` | private | — |
| `operator=` | field | `GpmlConstantValue` | private | This operator should never be defined, because we don't want/need to allow copy-assignment: All copying should use the virtual copy-constructor 'clone' (which will in turn use the copy-constructor); all "assignment" should really only be ... |

## Free functions and macros

| Name | Kind | Type / body | Description |
|---|---|---|---|
| `GPLATES_PROPERTYVALUES_GPMLCONSTANTVALUE_H` | macro | `None` | — |

## Notes

- `value_type()` has no setter: the structural type of the wrapped value is fixed at construction and must never change for the life of the instance.
- `directly_modifiable_fields_equal` compares the wrapped value by dereferenced equality (`*d_value == *other.d_value`) after a `dynamic_cast`, and treats a failed cast as inequality rather than propagating the exception.
- Copy-assignment is declared `private` and never defined; use `clone()` (which uses the protected copy constructor) instead of assigning instances.

## Used by

| Unit | Component | References |
|---|---|---|
| [file-io/GMTFormatHeader](../file-io/GMTFormatHeader.md) | file-io | 13 |
| [app-logic/ExtractScalarField3DFeatureProperties](../app-logic/ExtractScalarField3DFeatureProperties.md) | app-logic | 9 |
| [app-logic/ExtractRasterFeatureProperties](../app-logic/ExtractRasterFeatureProperties.md) | app-logic | 4 |
| [app-logic/PalaeomagUtils](../app-logic/PalaeomagUtils.md) | app-logic | 4 |
| [data-mining/CheckAttrTypeVisitor](../data-mining/CheckAttrTypeVisitor.md) | data-mining | 4 |
| [feature-visitors/TotalReconstructionSequencePlateIdFinder](../feature-visitors/TotalReconstructionSequencePlateIdFinder.md) | feature-visitors | 4 |
| [file-io/GpmlPropertyStructuralTypeReaderUtils](../file-io/GpmlPropertyStructuralTypeReaderUtils.md) | file-io | 4 |
| [feature-visitors/deprecated/PlateIdFinder](../feature-visitors/deprecated/PlateIdFinder.md) | feature-visitors | 3 |
| [app-logic/RasterLayerParams](../app-logic/RasterLayerParams.md) | app-logic | 2 |
| [app-logic/ScalarCoverageFeatureProperties](../app-logic/ScalarCoverageFeatureProperties.md) | app-logic | 2 |
| [app-logic/TRSUtils](../app-logic/TRSUtils.md) | app-logic | 2 |
| [feature-visitors/FeatureClassifier](../feature-visitors/FeatureClassifier.md) | feature-visitors | 2 |
| [feature-visitors/GeometryFinder](../feature-visitors/GeometryFinder.md) | feature-visitors | 2 |
| [feature-visitors/GeometryRotator](../feature-visitors/GeometryRotator.md) | feature-visitors | 2 |
| [feature-visitors/GeometrySetter](../feature-visitors/GeometrySetter.md) | feature-visitors | 2 |
| [feature-visitors/GeometryTypeFinder](../feature-visitors/GeometryTypeFinder.md) | feature-visitors | 2 |
| [file-io/GmapReader](../file-io/GmapReader.md) | file-io | 2 |
| [model/ModelUtils](../model/ModelUtils.md) | model | 2 |
| [qt-widgets/EditBooleanWidget](../qt-widgets/EditBooleanWidget.md) | qt-widgets | 2 |
| [utils/GetPropertyAsPythonObjVisitor](../utils/GetPropertyAsPythonObjVisitor.md) | utils | 2 |

*... and 53 more units.*

## Related

*None.*

## Explore

Run these from the `gplates-code` skill directory:

```bash
python scripts/gpq.py file src/property-values/GpmlConstantValue.h
python scripts/gpq.py def GPlatesPropertyValues::GpmlConstantValue --body
python scripts/gpq.py uses GpmlConstantValue --kind class
python scripts/gpq.py hier GpmlConstantValue
```
