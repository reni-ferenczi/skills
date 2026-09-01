# GpmlFeatureSnapshotReference

[Book TOC](../../TOC.md) · [property-values](../../components/property-values.md) · cluster Community 204 · tier 3

| Source file | Kind | Lines |
|---|---|---|
| `src/property-values/GpmlFeatureSnapshotReference.h` | C++ | 207 |
| `src/property-values/GpmlFeatureSnapshotReference.cc` | C++ | 38 |

## Overview

[[[PROSE overview unit=property-values/GpmlFeatureSnapshotReference tier=3]]]
Replace this whole block, markers included, with 1-3 paragraphs: what this unit is, why it exists, and how it fits the surrounding design. Do not restate the tables below.
[[[/PROSE]]]

## Declared types

| Name | Kind | Bases | Template | Subclasses | Description |
|---|---|---|---|---|---|
| [`GPlatesPropertyValues::GpmlFeatureSnapshotReference`](#gplatespropertyvaluesgpmlfeaturesnapshotreference) | class | [`GPlatesModel::PropertyValue`](../model/PropertyValue.md) | — | 0 | — |

## Members

### `GPlatesPropertyValues::GpmlFeatureSnapshotReference`

| Member | Kind | Type | Access | Description |
|---|---|---|---|---|
| `non_null_ptr_type` | typedef | `GPlatesUtils::non_null_intrusive_ptr<GpmlFeatureSnapshotReference>` | public | A convenience typedef for GPlatesUtils::non\_null\_intrusive\_ptr\<GpmlFeatureSnapshotReference\>. |
| `non_null_ptr_to_const_type` | typedef | `GPlatesUtils::non_null_intrusive_ptr<const GpmlFeatureSnapshotReference>` | public | A convenience typedef for GPlatesUtils::non\_null\_intrusive\_ptr\<const GpmlFeatureSnapshotReference\>. |
| `~GpmlFeatureSnapshotReference()` | destructor | `None` | public | — |
| `create( const GPlatesModel::FeatureId &feature_, const GPlatesModel::RevisionId &revision_, const GPlatesModel::FeatureType &value_type_)` | method | `non_null_ptr_type` | public | — |
| `clone()` | method | `non_null_ptr_type` | public | — |
| `deep_clone()` | method | `non_null_ptr_type` | public | — |
| `DEFINE_FUNCTION_DEEP_CLONE_AS_PROP_VAL()` | method | `None` | public | — |
| `feature_id()` | method | `GPlatesModel::FeatureId` | public | — |
| `revision_id()` | method | `GPlatesModel::RevisionId` | public | — |
| `get_structural_type()` | method | `StructuralType` | public | Returns the structural type associated with this property value class. |
| `accept_visitor( GPlatesModel::ConstFeatureVisitor &visitor)` | method | `void` | public | Accept a ConstFeatureVisitor instance. |
| `accept_visitor( GPlatesModel::FeatureVisitor &visitor)` | method | `void` | public | Accept a FeatureVisitor instance. |
| `print_to` | field | `std::ostream` | public | — |
| `GpmlFeatureSnapshotReference( const GPlatesModel::FeatureId &feature_, const GPlatesModel::RevisionId &revision_, const GPlatesModel::FeatureType &value_type_)` | constructor | `None` | protected | This constructor should not be public, because we don't want to allow instantiation of this type on the stack. |
| `GpmlFeatureSnapshotReference( const GpmlFeatureSnapshotReference &other)` | constructor | `None` | protected | This constructor should not be public, because we don't want to allow instantiation of this type on the stack. |
| `d_feature` | field | `GPlatesModel::FeatureId` | private | — |
| `d_revision` | field | `GPlatesModel::RevisionId` | private | — |
| `d_value_type` | field | `GPlatesModel::FeatureType` | private | — |
| `operator=` | field | `GpmlFeatureSnapshotReference` | private | This operator should never be defined, because we don't want/need to allow copy-assignment: All copying should use the virtual copy-constructor 'clone' (which will in turn use the copy-constructor); all "assignment" should really only be ... |

## Free functions and macros

| Name | Kind | Type / body | Description |
|---|---|---|---|
| `GPLATES_PROPERTYVALUES_GPMLFEATURESNAPSHOTREFERENCE_H` | macro | `None` | — |

## Notes

[[[PROSE notes unit=property-values/GpmlFeatureSnapshotReference tier=3]]]
Replace this whole block, markers included, with invariants, ownership, threading or gotchas that are not visible in the tables. Write *None.* if there is nothing worth saying.
[[[/PROSE]]]

## Used by

| Unit | Component | References |
|---|---|---|
| [file-io/GpmlPropertyStructuralTypeReaderUtils](../file-io/GpmlPropertyStructuralTypeReaderUtils.md) | file-io | 3 |
| [file-io/GpmlFormatMultiPointVectorFieldExport](../file-io/GpmlFormatMultiPointVectorFieldExport.md) | file-io | 2 |
| [data-mining/GetValueFromPropertyVisitor](../data-mining/GetValueFromPropertyVisitor.md) | data-mining | 1 |
| [feature-visitors/TopologySectionsFinder](../feature-visitors/TopologySectionsFinder.md) | feature-visitors | 1 |
| [file-io/GMTFormatHeader](../file-io/GMTFormatHeader.md) | file-io | 1 |
| [file-io/GpmlFormatDeformationExport](../file-io/GpmlFormatDeformationExport.md) | file-io | 1 |
| [file-io/GpmlFormatReconstructedScalarCoverageExport](../file-io/GpmlFormatReconstructedScalarCoverageExport.md) | file-io | 1 |
| [file-io/GpmlOutputVisitor](../file-io/GpmlOutputVisitor.md) | file-io | 1 |
| [utils/GetPropertyAsPythonObjVisitor](../utils/GetPropertyAsPythonObjVisitor.md) | utils | 1 |

## Related

*None.*

## Explore

Run these from the `gplates-code` skill directory:

```bash
python scripts/gpq.py file src/property-values/GpmlFeatureSnapshotReference.h
python scripts/gpq.py def GPlatesPropertyValues::GpmlFeatureSnapshotReference --body
python scripts/gpq.py uses GpmlFeatureSnapshotReference --kind class
python scripts/gpq.py hier GpmlFeatureSnapshotReference
```
