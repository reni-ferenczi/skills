# GpmlFiniteRotation

[Book TOC](../../TOC.md) · [property-values](../../components/property-values.md) · cluster Community 908 · tier 2

| Source file | Kind | Lines |
|---|---|---|
| `src/property-values/GpmlFiniteRotation.h` | C++ | 306 |
| `src/property-values/GpmlFiniteRotation.cc` | C++ | 111 |

## Overview

`GpmlFiniteRotation` is the property-value wrapper around a `GPlatesMaths::FiniteRotation`, i.e. a single pole-and-angle rotation used as one sample within a total reconstruction sequence (`GpmlIrregularSampling` holds a time series of these). Alongside the rotation it carries an optional `GPlatesModel::MetadataContainer` recording provenance metadata (e.g. rotation-file comment fields) attached to that sample.

Three overloaded `create` functions build an instance from an already-constructed `GPlatesMaths::FiniteRotation`, from a raw `(longitude, latitude)` Euler-pole pair plus an angle in degrees, or from `GmlPoint`/`GpmlMeasure` property values holding the same data; a fourth, `create_zero_rotation`, builds the identity rotation. The two Euler-pole overloads exist, per the header's own comment, purely to support ad hoc hard-coded feature construction and are not necessarily the "proper" way to build a rotation going forward. `is_zero_rotation` delegates to `GPlatesMaths::represents_identity_rotation` on the wrapped unit quaternion; a zero rotation has no determinate Euler pole, so callers that need to extract a pole from a `GpmlFiniteRotation` must check this first.

## Declared types

| Name | Kind | Bases | Template | Subclasses | Description |
|---|---|---|---|---|---|
| [`GPlatesPropertyValues::GpmlFiniteRotation`](#gplatespropertyvaluesgpmlfiniterotation) | class | [`GPlatesModel::PropertyValue`](../model/PropertyValue.md) | — | 0 | This class implements the PropertyValue which corresponds to "gpml:FiniteRotation". |

## Members

### `GPlatesPropertyValues::GpmlFiniteRotation`

| Member | Kind | Type | Access | Description |
|---|---|---|---|---|
| `non_null_ptr_type` | typedef | `GPlatesUtils::non_null_intrusive_ptr<GpmlFiniteRotation>` | public | A convenience typedef for GPlatesUtils::non\_null\_intrusive\_ptr\<GpmlFiniteRotation\>. |
| `non_null_ptr_to_const_type` | typedef | `GPlatesUtils::non_null_intrusive_ptr<const GpmlFiniteRotation>` | public | A convenience typedef for GPlatesUtils::non\_null\_intrusive\_ptr\<const GpmlFiniteRotation\>. |
| `~GpmlFiniteRotation()` | destructor | `None` | public | — |
| `create( const GPlatesMaths::FiniteRotation &finite_rotation, boost::optional<const GPlatesModel::MetadataContainer &> metadata_ = boost::none)` | method | `non_null_ptr_type` | public | Create a GpmlFiniteRotation instance from a finite rotation and optional metadata. |
| `create( const std::pair<double, double> &gpml_euler_pole, const double &gml_angle_in_degrees, boost::optional<const GPlatesModel::MetadataContainer &> metadata_ = boost::none)` | method | `non_null_ptr_type` | public | Create a GpmlFiniteRotation instance from an Euler pole (longitude, latitude) and a rotation angle (units-of-measure: degrees). |
| `create( const GmlPoint::non_null_ptr_type &gpml_euler_pole, const GpmlMeasure::non_null_ptr_type &gml_angle_in_degrees, boost::optional<const GPlatesModel::MetadataContainer &> metadata_ = boost::none)` | method | `non_null_ptr_type` | public | Create a GpmlFiniteRotation instance from an Euler pole (longitude, latitude) and a rotation angle (units-of-measure: degrees). |
| `create_zero_rotation( boost::optional<const GPlatesModel::MetadataContainer &> metadata_ = boost::none)` | method | `non_null_ptr_type` | public | Create a GpmlFiniteRotation instance which represents a "zero" rotation. |
| `clone()` | method | `non_null_ptr_type` | public | — |
| `deep_clone()` | method | `non_null_ptr_type` | public | — |
| `DEFINE_FUNCTION_DEEP_CLONE_AS_PROP_VAL()` | method | `None` | public | — |
| `is_zero_rotation()` | method | `bool` | public | Return whether this GpmlFiniteRotation instance represents a "zero" rotation. |
| `set_finite_rotation( const GPlatesMaths::FiniteRotation &fr)` | method | `void` | public | Set the finite rotation within this instance to fr. |
| `set_metadata( const GPlatesModel::MetadataContainer &metadata_)` | method | `void` | public | — |
| `get_structural_type()` | method | `StructuralType` | public | Returns the structural type associated with this property value class. |
| `accept_visitor( GPlatesModel::ConstFeatureVisitor &visitor)` | method | `void` | public | Accept a ConstFeatureVisitor instance. |
| `accept_visitor( GPlatesModel::FeatureVisitor &visitor)` | method | `void` | public | Accept a FeatureVisitor instance. |
| `print_to` | field | `std::ostream` | public | — |
| `GpmlFiniteRotation( const GPlatesMaths::FiniteRotation &finite_rotation_, boost::optional<const GPlatesModel::MetadataContainer &> metadata_)` | constructor | `None` | protected | This constructor should not be public, because we don't want to allow instantiation of this type on the stack. |
| `GpmlFiniteRotation( const GpmlFiniteRotation &other)` | constructor | `None` | protected | This constructor should not be public, because we don't want to allow instantiation of this type on the stack. |
| `d_finite_rotation` | field | `GPlatesMaths::FiniteRotation` | private | — |
| `d_metadata` | field | `GPlatesModel::MetadataContainer` | private | — |
| `operator=` | field | `GpmlFiniteRotation` | private | This operator should never be defined, because we don't want/need to allow copy-assignment: All copying should use the virtual copy-constructor 'clone' (which will in turn use the copy-constructor); all "assignment" should really only be ... |

## Free functions and macros

| Name | Kind | Type / body | Description |
|---|---|---|---|
| `GPLATES_PROPERTYVALUES_GPMLFINITEROTATION_H` | macro | `None` | — |

## Notes

- A zero (identity) rotation has no determinate Euler pole; the header warns that attempting to compute an Euler pole from a zero-rotation instance throws.
- The header itself flags `MetadataContainer` as a known weak spot: a `const` `GpmlFiniteRotation::metadata()` reference still allows the caller to mutate the contained metadata objects in place, bypassing the model's revisioning.
- Copy-assignment is declared `private` and never defined; use `clone()` instead.

## Used by

| Unit | Component | References |
|---|---|---|
| [property-values/GpmlIrregularSampling](GpmlIrregularSampling.md) | property-values | 16 |
| [file-io/GpmlPropertyStructuralTypeReaderUtils](../file-io/GpmlPropertyStructuralTypeReaderUtils.md) | file-io | 5 |
| [data-mining/GetValueFromPropertyVisitor](../data-mining/GetValueFromPropertyVisitor.md) | data-mining | 2 |
| [file-io/GpmlOutputVisitor](../file-io/GpmlOutputVisitor.md) | file-io | 2 |
| [file-io/deprecated/GpmlOnePointFiveOutputVisitor](../file-io/deprecated/GpmlOnePointFiveOutputVisitor.md) | file-io | 2 |
| [utils/GetPropertyAsPythonObjVisitor](../utils/GetPropertyAsPythonObjVisitor.md) | utils | 2 |
| [app-logic/ReconstructionGraphPopulator](../app-logic/ReconstructionGraphPopulator.md) | app-logic | 1 |
| [feature-visitors/PropertyValueFinder](../feature-visitors/PropertyValueFinder.md) | feature-visitors | 1 |
| [feature-visitors/QueryFeaturePropertiesWidgetPopulator](../feature-visitors/QueryFeaturePropertiesWidgetPopulator.md) | feature-visitors | 1 |
| [feature-visitors/TopologySectionsFinder](../feature-visitors/TopologySectionsFinder.md) | feature-visitors | 1 |
| [feature-visitors/TotalReconstructionSequenceRotationInserter](../feature-visitors/TotalReconstructionSequenceRotationInserter.md) | feature-visitors | 1 |
| [feature-visitors/TotalReconstructionSequenceRotationInterpolater](../feature-visitors/TotalReconstructionSequenceRotationInterpolater.md) | feature-visitors | 1 |
| [file-io/PlatesLineFormatReader](../file-io/PlatesLineFormatReader.md) | file-io | 1 |
| [file-io/PlatesRotationFileProxy](../file-io/PlatesRotationFileProxy.md) | file-io | 1 |
| [file-io/PlatesRotationFormatReader](../file-io/PlatesRotationFormatReader.md) | file-io | 1 |
| [file-io/PlatesRotationFormatWriter](../file-io/PlatesRotationFormatWriter.md) | file-io | 1 |
| [model/ModelUtils](../model/ModelUtils.md) | model | 1 |
| [qt-widgets/CreateTotalReconstructionSequenceDialog](../qt-widgets/CreateTotalReconstructionSequenceDialog.md) | qt-widgets | 1 |
| [qt-widgets/EditTotalReconstructionSequenceDialog](../qt-widgets/EditTotalReconstructionSequenceDialog.md) | qt-widgets | 1 |
| [qt-widgets/EditTotalReconstructionSequenceWidget](../qt-widgets/EditTotalReconstructionSequenceWidget.md) | qt-widgets | 1 |

*... and 2 more units.*

## Related

*None.*

## Explore

Run these from the `gplates-code` skill directory:

```bash
python scripts/gpq.py file src/property-values/GpmlFiniteRotation.h
python scripts/gpq.py def GPlatesPropertyValues::GpmlFiniteRotation --body
python scripts/gpq.py uses GpmlFiniteRotation --kind class
python scripts/gpq.py hier GpmlFiniteRotation
```
