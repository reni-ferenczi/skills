# GpmlKeyValueDictionary

[Book TOC](../../TOC.md) · [property-values](../../components/property-values.md) · cluster Community 1052 · tier 2

| Source file | Kind | Lines |
|---|---|---|
| `src/property-values/GpmlKeyValueDictionary.h` | C++ | 212 |
| `src/property-values/GpmlKeyValueDictionary.cc` | C++ | 82 |

## Overview

`GpmlKeyValueDictionary` is the property value for a GPML `KeyValueDictionary`: an ordered `std::vector<GpmlKeyValueDictionaryElement>`, each element pairing a key with a typed value. It is how GPlates represents arbitrary attribute tables attached to a feature — most visibly the shapefile/OGR attribute-mapping machinery (`OgrUtils`, `OgrFeatureCollectionWriter`, `EditShapefileAttributesWidget`) round-trips shapefile attribute columns through this type, since GPML has no native per-source attribute schema of its own.

`elements()` exposes the underlying vector by reference (both const and non-const overloads), so callers add, remove or reorder key/value pairs directly on the vector rather than through dedicated mutator methods.

## Declared types

| Name | Kind | Bases | Template | Subclasses | Description |
|---|---|---|---|---|---|
| [`GPlatesPropertyValues::GpmlKeyValueDictionary`](#gplatespropertyvaluesgpmlkeyvaluedictionary) | class | [`GPlatesModel::PropertyValue`](../model/PropertyValue.md) | — | 0 | — |

## Members

### `GPlatesPropertyValues::GpmlKeyValueDictionary`

| Member | Kind | Type | Access | Description |
|---|---|---|---|---|
| `non_null_ptr_type` | typedef | `GPlatesUtils::non_null_intrusive_ptr<GpmlKeyValueDictionary>` | public | A convenience typedef for GPlatesUtils::non\_null\_intrusive\_ptr\<GpmlKeyValueDictionary\>. |
| `non_null_ptr_to_const_type` | typedef | `GPlatesUtils::non_null_intrusive_ptr<const GpmlKeyValueDictionary>` | public | A convenience typedef for GPlatesUtils::non\_null\_intrusive\_ptr\<const GpmlKeyValueDictionary\>. |
| `~GpmlKeyValueDictionary()` | destructor | `None` | public | — |
| `create()` | method | `non_null_ptr_type` | public | — |
| `create( const std::vector<GpmlKeyValueDictionaryElement> &elements)` | method | `non_null_ptr_type` | public | — |
| `clone()` | method | `non_null_ptr_type` | public | — |
| `deep_clone()` | method | `GpmlKeyValueDictionary::non_null_ptr_type` | public | — |
| `DEFINE_FUNCTION_DEEP_CLONE_AS_PROP_VAL()` | method | `None` | public | — |
| `get_structural_type()` | method | `StructuralType` | public | Returns the structural type associated with this property value class. |
| `accept_visitor( GPlatesModel::ConstFeatureVisitor &visitor)` | method | `void` | public | Accept a ConstFeatureVisitor instance. |
| `accept_visitor( GPlatesModel::FeatureVisitor &visitor)` | method | `void` | public | Accept a FeatureVisitor instance. |
| `is_empty()` | method | `bool` | public | — |
| `num_elements()` | method | `int` | public | FIXME: Why does this return an 'int', rather than a 'std::vector\<T\>::size\_type'? |
| `print_to` | field | `std::ostream` | public | — |
| `GpmlKeyValueDictionary()` | constructor | `None` | protected | This constructor should not be public, because we don't want to allow instantiation of this type on the stack. |
| `GpmlKeyValueDictionary( const std::vector<GpmlKeyValueDictionaryElement> &elements_)` | constructor | `None` | protected | This constructor should not be public, because we don't want to allow instantiation of this type on the stack. |
| `GpmlKeyValueDictionary( const GpmlKeyValueDictionary &other)` | constructor | `None` | protected | This constructor should not be public, because we don't want to allow instantiation of this type on the stack. |
| `directly_modifiable_fields_equal( const PropertyValue &other)` | method | `bool` | protected | — |
| `d_elements` | field | `std::vector<GPlatesPropertyValues::GpmlKeyValueDictionaryElement>` | private | — |
| `operator=` | field | `GpmlKeyValueDictionary` | private | This operator should never be defined, because we don't want/need to allow copy-assignment: All copying should use the virtual copy-constructor 'clone' (which will in turn use the copy-constructor); all "assignment" should really only be ... |

## Free functions and macros

| Name | Kind | Type / body | Description |
|---|---|---|---|
| `GPLATES_PROPERTYVALUES_GPMLKEYVALUEDICTIONARY_H` | macro | `None` | — |

## Notes

- The protected copy constructor only forwards to `PropertyValue(other)`; it never initialises `d_elements` from `other.d_elements`. As a result, `clone()` (which uses this copy constructor) produces a dictionary with an **empty** element vector, silently dropping every key/value pair. `deep_clone()` happens to still work correctly, because it repopulates `dup->d_elements` itself by iterating `d_elements` on the original and pushing deep-cloned elements — but any code that calls `clone()` directly on a non-empty dictionary loses its contents.
- `num_elements()` returns `int`, not `std::vector<T>::size_type`, per the header's own `FIXME`.

## Used by

| Unit | Component | References |
|---|---|---|
| [file-io/OgrUtils](../file-io/OgrUtils.md) | file-io | 71 |
| [file-io/OgrFeatureCollectionWriter](../file-io/OgrFeatureCollectionWriter.md) | file-io | 34 |
| [file-io/OgrGeometryExporter](../file-io/OgrGeometryExporter.md) | file-io | 9 |
| [file-io/OgrWriter](../file-io/OgrWriter.md) | file-io | 8 |
| [file-io/PlatesRotationFileProxy](../file-io/PlatesRotationFileProxy.md) | file-io | 7 |
| [qt-widgets/EditShapefileAttributesWidget](../qt-widgets/EditShapefileAttributesWidget.md) | qt-widgets | 7 |
| [file-io/OgrFormatFlowlineExport](../file-io/OgrFormatFlowlineExport.md) | file-io | 5 |
| [file-io/OgrFormatMotionPathExport](../file-io/OgrFormatMotionPathExport.md) | file-io | 5 |
| [data-mining/CheckAttrTypeVisitor](../data-mining/CheckAttrTypeVisitor.md) | data-mining | 4 |
| [file-io/GMTFormatHeader](../file-io/GMTFormatHeader.md) | file-io | 4 |
| [file-io/GpmlPropertyStructuralTypeReaderUtils](../file-io/GpmlPropertyStructuralTypeReaderUtils.md) | file-io | 4 |
| [file-io/OgrFormatReconstructedFeatureGeometryExport](../file-io/OgrFormatReconstructedFeatureGeometryExport.md) | file-io | 3 |
| [qt-widgets/MetadataDialog](../qt-widgets/MetadataDialog.md) | qt-widgets | 3 |
| [feature-visitors/KeyValueDictionaryFinder](../feature-visitors/KeyValueDictionaryFinder.md) | feature-visitors | 2 |
| [file-io/GpmlStructuralTypeReaderUtils](../file-io/GpmlStructuralTypeReaderUtils.md) | file-io | 2 |
| [file-io/OgrFormatResolvedTopologicalGeometryExport](../file-io/OgrFormatResolvedTopologicalGeometryExport.md) | file-io | 2 |
| [qt-widgets/ShapefileAttributeViewerDialog](../qt-widgets/ShapefileAttributeViewerDialog.md) | qt-widgets | 2 |
| [unit-test/FeatureHandleTest](../unit-test/FeatureHandleTest.md) | unit-test | 2 |
| [api/PyFeature](../api/PyFeature.md) | api | 1 |
| [data-mining/GetValueFromPropertyVisitor](../data-mining/GetValueFromPropertyVisitor.md) | data-mining | 1 |

*... and 9 more units.*

## Related

*None.*

## Explore

Run these from the `gplates-code` skill directory:

```bash
python scripts/gpq.py file src/property-values/GpmlKeyValueDictionary.h
python scripts/gpq.py def GPlatesPropertyValues::GpmlKeyValueDictionary --body
python scripts/gpq.py uses GpmlKeyValueDictionary --kind class
python scripts/gpq.py hier GpmlKeyValueDictionary
```
