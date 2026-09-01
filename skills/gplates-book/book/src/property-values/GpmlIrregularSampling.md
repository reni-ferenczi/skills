# GpmlIrregularSampling

[Book TOC](../../TOC.md) · [property-values](../../components/property-values.md) · cluster Community 784 · tier 2

| Source file | Kind | Lines |
|---|---|---|
| `src/property-values/GpmlIrregularSampling.h` | C++ | 282 |
| `src/property-values/GpmlIrregularSampling.cc` | C++ | 184 |

## Overview

`GpmlIrregularSampling` is the property value for a GPML `IrregularSampling`: an ordered `std::vector<GpmlTimeSample>` (time-stamped property values, most commonly `GpmlFiniteRotation` poles for a total reconstruction sequence) together with an optional `GpmlInterpolationFunction` that says how to interpolate between consecutive samples, and the `StructuralType` of the sampled property. This is the container that gives a plate's rotation history its "reconstruction poles at these times, interpolated this way" shape.

`is_disabled`/`set_disabled` implement a convention layered on top of `GpmlFiniteRotation::metadata()` rather than a dedicated field: a sequence is considered disabled when any of its finite-rotation samples carries a `Metadata::DISABLED_SEQUENCE_FLAG` entry with content `"true"` (checked case-insensitively), and `set_disabled` enforces that by stripping the flag from every sample and, when disabling, re-adding it only to the first sample's metadata. This is how the total-reconstruction-sequence editing dialogs mark a rotation sequence as inactive without changing the property-value type.

## Declared types

| Name | Kind | Bases | Template | Subclasses | Description |
|---|---|---|---|---|---|
| [`GPlatesPropertyValues::GpmlIrregularSampling`](#gplatespropertyvaluesgpmlirregularsampling) | class | [`GPlatesModel::PropertyValue`](../model/PropertyValue.md) | — | 0 | — |

## Members

### `GPlatesPropertyValues::GpmlIrregularSampling`

| Member | Kind | Type | Access | Description |
|---|---|---|---|---|
| `non_null_ptr_type` | typedef | `GPlatesUtils::non_null_intrusive_ptr<GpmlIrregularSampling>` | public | A convenience typedef for GPlatesUtils::non\_null\_intrusive\_ptr\<GpmlIrregularSampling\>. |
| `non_null_ptr_to_const_type` | typedef | `GPlatesUtils::non_null_intrusive_ptr<const GpmlIrregularSampling>` | public | A convenience typedef for GPlatesUtils::non\_null\_intrusive\_ptr\<const GpmlIrregularSampling\>. |
| `~GpmlIrregularSampling()` | destructor | `None` | public | — |
| `create( const GpmlTimeSample &first_time_sample, GpmlInterpolationFunction::maybe_null_ptr_type interp_func, const StructuralType &value_type_)` | method | `non_null_ptr_type` | public | — |
| `create( const std::vector<GpmlTimeSample> &time_samples_, GpmlInterpolationFunction::maybe_null_ptr_type interp_func, const StructuralType &value_type_)` | method | `non_null_ptr_type` | public | — |
| `clone()` | method | `non_null_ptr_type` | public | — |
| `deep_clone()` | method | `non_null_ptr_type` | public | — |
| `DEFINE_FUNCTION_DEEP_CLONE_AS_PROP_VAL()` | method | `None` | public | — |
| `interpolation_function()` | method | `GpmlInterpolationFunction::maybe_null_ptr_to_const_type` | public | Returns the 'const' interpolation function. |
| `set_interpolation_function( GpmlInterpolationFunction::maybe_null_ptr_type i)` | method | `void` | public | Sets the internal interpolation function. |
| `get_structural_type()` | method | `StructuralType` | public | Returns the structural type associated with this property value class. |
| `accept_visitor( GPlatesModel::ConstFeatureVisitor &visitor)` | method | `void` | public | Accept a ConstFeatureVisitor instance. |
| `accept_visitor( GPlatesModel::FeatureVisitor &visitor)` | method | `void` | public | Accept a FeatureVisitor instance. |
| `print_to` | field | `std::ostream` | public | — |
| `is_disabled()` | method | `bool` | public | — |
| `set_disabled( bool flag)` | method | `void` | public | — |
| `contain_disabled_sequence_flag()` | method | `bool` | protected | — |
| `GpmlIrregularSampling( const GpmlTimeSample &first_time_sample, GpmlInterpolationFunction::maybe_null_ptr_type interp_func, const StructuralType &value_type_)` | constructor | `None` | protected | This constructor should not be public, because we don't want to allow instantiation of this type on the stack. |
| `GpmlIrregularSampling( const std::vector<GpmlTimeSample> &time_samples_, GpmlInterpolationFunction::maybe_null_ptr_type interp_func, const StructuralType &value_type_)` | constructor | `None` | protected | This constructor should not be public, because we don't want to allow instantiation of this type on the stack. |
| `GpmlIrregularSampling( const GpmlIrregularSampling &other)` | constructor | `None` | protected | This constructor should not be public, because we don't want to allow instantiation of this type on the stack. |
| `directly_modifiable_fields_equal( const PropertyValue &other)` | method | `bool` | protected | — |
| `d_time_samples` | field | `std::vector<GpmlTimeSample>` | private | — |
| `d_interpolation_function` | field | `GpmlInterpolationFunction::maybe_null_ptr_type` | private | — |
| `d_value_type` | field | `StructuralType` | private | — |
| `operator=` | field | `GpmlIrregularSampling` | private | This operator should never be defined, because we don't want/need to allow copy-assignment: All copying should use the virtual copy-constructor 'clone' (which will in turn use the copy-constructor); all "assignment" should really only be ... |

## Free functions and macros

| Name | Kind | Type / body | Description |
|---|---|---|---|
| `maybe_null_ptr_eq( const GPlatesPropertyValues::GpmlInterpolationFunction::maybe_null_ptr_type &p1, const GPlatesPropertyValues::GpmlInterpolationFunction::maybe_null_ptr_type &p2)` | function | `bool` | — |
| `GPLATES_PROPERTYVALUES_GPMLIRREGULARSAMPLING_H` | macro | `None` | — |

## Notes

- `set_disabled` silently does nothing (after logging a `qWarning`) when `time_samples()` is empty, and the disabled-flag convention only has an effect on samples whose value is a `GpmlFiniteRotation`; samples holding other property-value types are left untouched by both `set_disabled` and `contain_disabled_sequence_flag`.
- `print_to` is a stub (`"{ GpmlIrregularSampling }"`); do not rely on it for debugging output — the `FIXME` in the `.cc` says it was never filled in.
- `value_type()` has no setter: the sampled property's structural type is fixed at construction and must never change.
- `deep_clone` recurses into every `GpmlTimeSample` and, when present, into the interpolation function via `deep_clone_as_interp_func()`.

## Used by

| Unit | Component | References |
|---|---|---|
| [qt-widgets/EditTotalReconstructionSequenceWidget](../qt-widgets/EditTotalReconstructionSequenceWidget.md) | qt-widgets | 8 |
| [file-io/GpmlOutputVisitor](../file-io/GpmlOutputVisitor.md) | file-io | 4 |
| [file-io/GpmlPropertyStructuralTypeReaderUtils](../file-io/GpmlPropertyStructuralTypeReaderUtils.md) | file-io | 4 |
| [qt-widgets/TotalReconstructionSequencesDialog](../qt-widgets/TotalReconstructionSequencesDialog.md) | qt-widgets | 4 |
| [feature-visitors/TotalReconstructionSequenceRotationInterpolater](../feature-visitors/TotalReconstructionSequenceRotationInterpolater.md) | feature-visitors | 3 |
| [feature-visitors/TotalReconstructionSequenceTimePeriodFinder](../feature-visitors/TotalReconstructionSequenceTimePeriodFinder.md) | feature-visitors | 3 |
| [file-io/GMTFormatHeader](../file-io/GMTFormatHeader.md) | file-io | 3 |
| [file-io/deprecated/GpmlOnePointFiveOutputVisitor](../file-io/deprecated/GpmlOnePointFiveOutputVisitor.md) | file-io | 3 |
| [app-logic/MotionPathUtils](../app-logic/MotionPathUtils.md) | app-logic | 2 |
| [app-logic/ReconstructionGraphPopulator](../app-logic/ReconstructionGraphPopulator.md) | app-logic | 2 |
| [app-logic/TRSUtils](../app-logic/TRSUtils.md) | app-logic | 2 |
| [feature-visitors/PropertyValueFinder](../feature-visitors/PropertyValueFinder.md) | feature-visitors | 2 |
| [qt-widgets/CreateTotalReconstructionSequenceDialog](../qt-widgets/CreateTotalReconstructionSequenceDialog.md) | qt-widgets | 2 |
| [qt-widgets/EditTotalReconstructionSequenceDialog](../qt-widgets/EditTotalReconstructionSequenceDialog.md) | qt-widgets | 2 |
| [app-logic/FlowlineGeometryPopulator](../app-logic/FlowlineGeometryPopulator.md) | app-logic | 1 |
| [app-logic/FlowlineUtils](../app-logic/FlowlineUtils.md) | app-logic | 1 |
| [app-logic/MotionPathGeometryPopulator](../app-logic/MotionPathGeometryPopulator.md) | app-logic | 1 |
| [data-mining/GetValueFromPropertyVisitor](../data-mining/GetValueFromPropertyVisitor.md) | data-mining | 1 |
| [feature-visitors/QueryFeaturePropertiesWidgetPopulator](../feature-visitors/QueryFeaturePropertiesWidgetPopulator.md) | feature-visitors | 1 |
| [feature-visitors/TopologySectionsFinder](../feature-visitors/TopologySectionsFinder.md) | feature-visitors | 1 |

*... and 14 more units.*

## Related

*None.*

## Explore

Run these from the `gplates-code` skill directory:

```bash
python scripts/gpq.py file src/property-values/GpmlIrregularSampling.h
python scripts/gpq.py def GPlatesPropertyValues::GpmlIrregularSampling --body
python scripts/gpq.py uses GpmlIrregularSampling --kind class
python scripts/gpq.py hier GpmlIrregularSampling
```
