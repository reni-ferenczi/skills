# GpmlFiniteRotationSlerp

[Book TOC](../../TOC.md) · [property-values](../../components/property-values.md) · cluster Community 1498 · tier 3

| Source file | Kind | Lines |
|---|---|---|
| `src/property-values/GpmlFiniteRotationSlerp.h` | C++ | 150 |

## Overview

[[[PROSE overview unit=property-values/GpmlFiniteRotationSlerp tier=3]]]
Replace this whole block, markers included, with 1-3 paragraphs: what this unit is, why it exists, and how it fits the surrounding design. Do not restate the tables below.
[[[/PROSE]]]

## Declared types

| Name | Kind | Bases | Template | Subclasses | Description |
|---|---|---|---|---|---|
| [`GPlatesPropertyValues::GpmlFiniteRotationSlerp`](#gplatespropertyvaluesgpmlfiniterotationslerp) | class | [`GpmlInterpolationFunction`](GpmlInterpolationFunction.md) | — | 0 | — |

## Members

### `GPlatesPropertyValues::GpmlFiniteRotationSlerp`

| Member | Kind | Type | Access | Description |
|---|---|---|---|---|
| `non_null_ptr_type` | typedef | `GPlatesUtils::non_null_intrusive_ptr<GpmlFiniteRotationSlerp>` | public | A convenience typedef for GPlatesUtils::non\_null\_intrusive\_ptr\<GpmlFiniteRotationSlerp\>. |
| `non_null_ptr_to_const_type` | typedef | `GPlatesUtils::non_null_intrusive_ptr<const GpmlFiniteRotationSlerp>` | public | A convenience typedef for GPlatesUtils::non\_null\_intrusive\_ptr\<const GpmlFiniteRotationSlerp\>. |
| `~GpmlFiniteRotationSlerp()` | destructor | `None` | public | — |
| `create( const StructuralType &value_type_)` | method | `non_null_ptr_type` | public | — |
| `clone()` | method | `non_null_ptr_type` | public | — |
| `deep_clone()` | method | `non_null_ptr_type` | public | — |
| `DEFINE_FUNCTION_DEEP_CLONE_AS_PROP_VAL()` | method | `None` | public | — |
| `DEFINE_FUNCTION_DEEP_CLONE_AS_INTERP_FUNC()` | method | `None` | public | — |
| `accept_visitor( GPlatesModel::ConstFeatureVisitor &visitor)` | method | `void` | public | Accept a ConstFeatureVisitor instance. |
| `accept_visitor( GPlatesModel::FeatureVisitor &visitor)` | method | `void` | public | Accept a FeatureVisitor instance. |
| `GpmlFiniteRotationSlerp( const StructuralType &value_type_)` | constructor | `None` | protected | This constructor should not be public, because we don't want to allow instantiation of this type on the stack. |
| `GpmlFiniteRotationSlerp( const GpmlFiniteRotationSlerp &other)` | constructor | `None` | protected | This constructor should not be public, because we don't want to allow instantiation of this type on the stack. |
| `operator=` | field | `GpmlFiniteRotationSlerp` | private | This operator should never be defined, because we don't want/need to allow copy-assignment: All copying should use the virtual copy-constructor 'clone' (which will in turn use the copy-constructor); all "assignment" should really only be ... |

## Free functions and macros

| Name | Kind | Type / body | Description |
|---|---|---|---|
| `GPLATES_PROPERTYVALUES_GPMLFINITEROTATIONSLERP_H` | macro | `None` | — |

## Notes

[[[PROSE notes unit=property-values/GpmlFiniteRotationSlerp tier=3]]]
Replace this whole block, markers included, with invariants, ownership, threading or gotchas that are not visible in the tables. Write *None.* if there is nothing worth saying.
[[[/PROSE]]]

## Used by

| Unit | Component | References |
|---|---|---|
| [data-mining/GetValueFromPropertyVisitor](../data-mining/GetValueFromPropertyVisitor.md) | data-mining | 2 |
| [utils/GetPropertyAsPythonObjVisitor](../utils/GetPropertyAsPythonObjVisitor.md) | utils | 2 |
| [app-logic/ReconstructionGraphPopulator](../app-logic/ReconstructionGraphPopulator.md) | app-logic | 1 |
| [feature-visitors/QueryFeaturePropertiesWidgetPopulator](../feature-visitors/QueryFeaturePropertiesWidgetPopulator.md) | feature-visitors | 1 |
| [feature-visitors/TopologySectionsFinder](../feature-visitors/TopologySectionsFinder.md) | feature-visitors | 1 |
| [feature-visitors/TotalReconstructionSequenceRotationInserter](../feature-visitors/TotalReconstructionSequenceRotationInserter.md) | feature-visitors | 1 |
| [feature-visitors/TotalReconstructionSequenceRotationInterpolater](../feature-visitors/TotalReconstructionSequenceRotationInterpolater.md) | feature-visitors | 1 |
| [file-io/GpmlOutputVisitor](../file-io/GpmlOutputVisitor.md) | file-io | 1 |
| [file-io/GpmlStructuralTypeReaderUtils](../file-io/GpmlStructuralTypeReaderUtils.md) | file-io | 1 |
| [file-io/PlatesLineFormatReader](../file-io/PlatesLineFormatReader.md) | file-io | 1 |
| [file-io/PlatesRotationFileProxy](../file-io/PlatesRotationFileProxy.md) | file-io | 1 |
| [file-io/PlatesRotationFormatReader](../file-io/PlatesRotationFormatReader.md) | file-io | 1 |
| [file-io/deprecated/GpmlOnePointFiveOutputVisitor](../file-io/deprecated/GpmlOnePointFiveOutputVisitor.md) | file-io | 1 |
| [model/ModelUtils](../model/ModelUtils.md) | model | 1 |
| [qt-widgets/EditTotalReconstructionSequenceWidget](../qt-widgets/EditTotalReconstructionSequenceWidget.md) | qt-widgets | 1 |

## Related

*None.*

## Explore

Run these from the `gplates-code` skill directory:

```bash
python scripts/gpq.py file src/property-values/GpmlFiniteRotationSlerp.h
python scripts/gpq.py def GPlatesPropertyValues::GpmlFiniteRotationSlerp --body
python scripts/gpq.py uses GpmlFiniteRotationSlerp --kind class
python scripts/gpq.py hier GpmlFiniteRotationSlerp
```
