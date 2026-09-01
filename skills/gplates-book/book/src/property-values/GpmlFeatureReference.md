# GpmlFeatureReference

[Book TOC](../../TOC.md) · [property-values](../../components/property-values.md) · cluster Community 1155 · tier 2

| Source file | Kind | Lines |
|---|---|---|
| `src/property-values/GpmlFeatureReference.h` | C++ | 223 |
| `src/property-values/GpmlFeatureReference.cc` | C++ | 38 |

## Overview

[[[PROSE overview unit=property-values/GpmlFeatureReference tier=2]]]
Replace this whole block, markers included, with 1-3 paragraphs: what this unit is, why it exists, and how it fits the surrounding design. Do not restate the tables below.
[[[/PROSE]]]

## Declared types

| Name | Kind | Bases | Template | Subclasses | Description |
|---|---|---|---|---|---|
| [`GPlatesPropertyValues::GpmlFeatureReference`](#gplatespropertyvaluesgpmlfeaturereference) | class | [`GPlatesModel::PropertyValue`](../model/PropertyValue.md) | — | 0 | — |

## Members

### `GPlatesPropertyValues::GpmlFeatureReference`

| Member | Kind | Type | Access | Description |
|---|---|---|---|---|
| `non_null_ptr_type` | typedef | `GPlatesUtils::non_null_intrusive_ptr<GpmlFeatureReference>` | public | A convenience typedef for GPlatesUtils::non\_null\_intrusive\_ptr\<GpmlFeatureReference\>. |
| `non_null_ptr_to_const_type` | typedef | `GPlatesUtils::non_null_intrusive_ptr<const GpmlFeatureReference>` | public | A convenience typedef for GPlatesUtils::non\_null\_intrusive\_ptr\<const GpmlFeatureReference\>. |
| `~GpmlFeatureReference()` | destructor | `None` | public | — |
| `create( const GPlatesModel::FeatureId &feature_, const GPlatesModel::FeatureType &value_type_)` | method | `non_null_ptr_type` | public | — |
| `clone()` | method | `non_null_ptr_type` | public | — |
| `deep_clone()` | method | `non_null_ptr_type` | public | — |
| `DEFINE_FUNCTION_DEEP_CLONE_AS_PROP_VAL()` | method | `None` | public | — |
| `feature_id()` | method | `GPlatesModel::FeatureId` | public | — |
| `get_structural_type()` | method | `StructuralType` | public | Returns the structural type associated with this property value class. |
| `accept_visitor( GPlatesModel::ConstFeatureVisitor &visitor)` | method | `void` | public | Accept a ConstFeatureVisitor instance. |
| `accept_visitor( GPlatesModel::FeatureVisitor &visitor)` | method | `void` | public | Accept a FeatureVisitor instance. |
| `print_to` | field | `std::ostream` | public | — |
| `GpmlFeatureReference( const GPlatesModel::FeatureId &feature_, const GPlatesModel::FeatureType &value_type_)` | constructor | `None` | protected | This constructor should not be public, because we don't want to allow instantiation of this type on the stack. |
| `GpmlFeatureReference( const GPlatesModel::FeatureId &feature_, const GPlatesModel::FeatureType &value_type_, const GPlatesUtils::UnicodeString &description_)` | constructor | `None` | protected | This constructor should not be public, because we don't want to allow instantiation of this type on the stack. |
| `GpmlFeatureReference( const GpmlFeatureReference &other)` | constructor | `None` | protected | This constructor should not be public, because we don't want to allow instantiation of this type on the stack. |
| `d_feature` | field | `GPlatesModel::FeatureId` | private | — |
| `d_value_type` | field | `GPlatesModel::FeatureType` | private | — |
| `operator=` | field | `GpmlFeatureReference` | private | This operator should never be defined, because we don't want/need to allow copy-assignment: All copying should use the virtual copy-constructor 'clone' (which will in turn use the copy-constructor); all "assignment" should really only be ... |

## Free functions and macros

| Name | Kind | Type / body | Description |
|---|---|---|---|
| `GPLATES_PROPERTYVALUES_GPMLFEATUREREFERENCE_H` | macro | `None` | — |

## Notes

[[[PROSE notes unit=property-values/GpmlFeatureReference tier=2]]]
Replace this whole block, markers included, with invariants, ownership, threading or gotchas that are not visible in the tables. Write *None.* if there is nothing worth saying.
[[[/PROSE]]]

## Used by

| Unit | Component | References |
|---|---|---|
| [file-io/GMTFormatHeader](../file-io/GMTFormatHeader.md) | file-io | 5 |
| [file-io/GpmlOutputVisitor](../file-io/GpmlOutputVisitor.md) | file-io | 5 |
| [feature-visitors/TopologySectionsFinder](../feature-visitors/TopologySectionsFinder.md) | feature-visitors | 4 |
| [file-io/GpmlPropertyStructuralTypeReaderUtils](../file-io/GpmlPropertyStructuralTypeReaderUtils.md) | file-io | 3 |
| [gui/TopologyTools](../gui/TopologyTools.md) | gui | 3 |
| [file-io/PlatesLineFormatReader](../file-io/PlatesLineFormatReader.md) | file-io | 2 |
| [qt-widgets/CreateFeatureDialog](../qt-widgets/CreateFeatureDialog.md) | qt-widgets | 2 |
| [data-mining/GetValueFromPropertyVisitor](../data-mining/GetValueFromPropertyVisitor.md) | data-mining | 1 |
| [file-io/GMTFormatDeformationExport](../file-io/GMTFormatDeformationExport.md) | file-io | 1 |
| [file-io/GMTFormatReconstructedScalarCoverageExport](../file-io/GMTFormatReconstructedScalarCoverageExport.md) | file-io | 1 |
| [utils/GetPropertyAsPythonObjVisitor](../utils/GetPropertyAsPythonObjVisitor.md) | utils | 1 |

## Related

*None.*

## Explore

Run these from the `gplates-code` skill directory:

```bash
python scripts/gpq.py file src/property-values/GpmlFeatureReference.h
python scripts/gpq.py def GPlatesPropertyValues::GpmlFeatureReference --body
python scripts/gpq.py uses GpmlFeatureReference --kind class
python scripts/gpq.py hier GpmlFeatureReference
```
