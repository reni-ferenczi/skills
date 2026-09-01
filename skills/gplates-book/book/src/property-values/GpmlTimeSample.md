# GpmlTimeSample

[Book TOC](../../TOC.md) · [property-values](../../components/property-values.md) · cluster Community 909 · tier 2

| Source file | Kind | Lines |
|---|---|---|
| `src/property-values/GpmlTimeSample.h` | C++ | 187 |
| `src/property-values/GpmlTimeSample.cc` | C++ | 84 |

## Overview

`GpmlTimeSample` is a plain value type, not a `PropertyValue` itself: it is the element type held inside `GpmlIrregularSampling`, pairing a sampled `PropertyValue` (`value()`) with the `GmlTimeInstant` at which it was sampled (`valid_time()`), an optional human-readable `description()`, the sample's `StructuralType` (fixed at construction, no setter, since a sampling sequence must keep a single value type across all its samples), and an `is_disabled()` flag that lets a sample be switched off without removing it from the sequence.

This is the model used most heavily for total reconstruction sequences: `file-io/PlatesRotationFormatReader` and `qt-widgets/EditTotalReconstructionSequenceWidget` build and edit rotation sequences as lists of `GpmlTimeSample`, and `feature-visitors/TotalReconstructionSequenceRotationInterpolater` interpolates finite rotations between consecutive samples. `deep_clone()` recursively clones the wrapped value, the time instant and the optional description rather than sharing them, and `operator==` compares all fields by value (including a null-safe comparison of the optional description).

## Declared types

| Name | Kind | Bases | Template | Subclasses | Description |
|---|---|---|---|---|---|
| [`GPlatesPropertyValues::GpmlTimeSample`](#gplatespropertyvaluesgpmltimesample) | class | — | — | 0 | Since all the members of this class are of type boost::intrusive\_ptr or StructuralType (which wraps an StringSet::SharedIterator instance which points to a pre-allocated node in a StringSet), none of the construction, copy-construction or ... |

## Members

### `GPlatesPropertyValues::GpmlTimeSample`

| Member | Kind | Type | Access | Description |
|---|---|---|---|---|
| `GpmlTimeSample( GPlatesModel::PropertyValue::non_null_ptr_type value_, GmlTimeInstant::non_null_ptr_type valid_time_, boost::intrusive_ptr<XsString> description_, const StructuralType &value_type_, bool is_disabled_ = false)` | constructor | `None` | public | — |
| `GpmlTimeSample( const GpmlTimeSample &other)` | constructor | `None` | public | — |
| `deep_clone()` | method | `GpmlTimeSample` | public | — |
| `value()` | method | `GPlatesModel::PropertyValue::non_null_ptr_to_const_type` | public | Returns the 'const' time-dependent property value. |
| `set_value( GPlatesModel::PropertyValue::non_null_ptr_type v)` | method | `void` | public | — |
| `valid_time()` | method | `GmlTimeInstant::non_null_ptr_to_const_type` | public | Returns the 'const' time instant. |
| `set_valid_time( GmlTimeInstant::non_null_ptr_type vt)` | method | `void` | public | — |
| `description()` | method | `boost::intrusive_ptr<const XsString>` | public | — |
| `set_description( boost::intrusive_ptr<XsString> d)` | method | `void` | public | — |
| `is_disabled()` | method | `bool` | public | — |
| `set_disabled( bool is_disabled_)` | method | `void` | public | — |
| `operator==( const GpmlTimeSample &other)` | operator | `bool` | public | — |
| `d_value` | field | `GPlatesModel::PropertyValue::non_null_ptr_type` | private | — |
| `d_valid_time` | field | `GmlTimeInstant::non_null_ptr_type` | private | — |
| `d_description` | field | `boost::intrusive_ptr<XsString>` | private | This one is optional. |
| `d_value_type` | field | `StructuralType` | private | — |
| `d_is_disabled` | field | `bool` | private | — |

## Free functions and macros

| Name | Kind | Type / body | Description |
|---|---|---|---|
| `intrusive_ptr_eq( const boost::intrusive_ptr<GPlatesPropertyValues::XsString> &p1, const boost::intrusive_ptr<GPlatesPropertyValues::XsString> &p2)` | function | `bool` | — |
| `operator==( const GpmlTimeSample &other)` | operator | `bool` | — |
| `GPLATES_PROPERTYVALUES_GPMLTIMESAMPLE_H` | macro | `None` | — |

## Notes

`description()` may hold a null `boost::intrusive_ptr<XsString>`; callers must check it before dereferencing, and `operator==`/`deep_clone()` already handle the null case correctly, so prefer them over ad hoc comparisons.

## Used by

| Unit | Component | References |
|---|---|---|
| [file-io/PlatesRotationFormatReader](../file-io/PlatesRotationFormatReader.md) | file-io | 21 |
| [qt-widgets/EditTotalReconstructionSequenceWidget](../qt-widgets/EditTotalReconstructionSequenceWidget.md) | qt-widgets | 17 |
| [property-values/GpmlIrregularSampling](GpmlIrregularSampling.md) | property-values | 14 |
| [feature-visitors/TotalReconstructionSequenceRotationInterpolater](../feature-visitors/TotalReconstructionSequenceRotationInterpolater.md) | feature-visitors | 10 |
| [qt-widgets/TotalReconstructionSequencesDialog](../qt-widgets/TotalReconstructionSequencesDialog.md) | qt-widgets | 10 |
| [feature-visitors/PropertyValueFinder](../feature-visitors/PropertyValueFinder.md) | feature-visitors | 9 |
| [file-io/GMTFormatHeader](../file-io/GMTFormatHeader.md) | file-io | 9 |
| [file-io/PlatesRotationFileProxy](../file-io/PlatesRotationFileProxy.md) | file-io | 8 |
| [model/ModelUtils](../model/ModelUtils.md) | model | 8 |
| [file-io/CitcomsResolvedTopologicalBoundaryExportImpl](../file-io/CitcomsResolvedTopologicalBoundaryExportImpl.md) | file-io | 6 |
| [file-io/PlatesRotationFormatWriter](../file-io/PlatesRotationFormatWriter.md) | file-io | 6 |
| [app-logic/ReconstructionGraphPopulator](../app-logic/ReconstructionGraphPopulator.md) | app-logic | 5 |
| [feature-visitors/TotalReconstructionSequenceRotationInserter](../feature-visitors/TotalReconstructionSequenceRotationInserter.md) | feature-visitors | 5 |
| [file-io/GpmlStructuralTypeReaderUtils](../file-io/GpmlStructuralTypeReaderUtils.md) | file-io | 5 |
| [feature-visitors/TotalReconstructionSequenceTimePeriodFinder](../feature-visitors/TotalReconstructionSequenceTimePeriodFinder.md) | feature-visitors | 3 |
| [file-io/GpmlOutputVisitor](../file-io/GpmlOutputVisitor.md) | file-io | 3 |
| [app-logic/TopologyInternalUtils](../app-logic/TopologyInternalUtils.md) | app-logic | 2 |
| [data-mining/GetValueFromPropertyVisitor](../data-mining/GetValueFromPropertyVisitor.md) | data-mining | 2 |
| [feature-visitors/TopologySectionsFinder](../feature-visitors/TopologySectionsFinder.md) | feature-visitors | 2 |
| [file-io/deprecated/GpmlOnePointFiveOutputVisitor](../file-io/deprecated/GpmlOnePointFiveOutputVisitor.md) | file-io | 2 |

*... and 19 more units.*

## Related

*None.*

## Explore

Run these from the `gplates-code` skill directory:

```bash
python scripts/gpq.py file src/property-values/GpmlTimeSample.h
python scripts/gpq.py def GPlatesPropertyValues::GpmlTimeSample --body
python scripts/gpq.py uses GpmlTimeSample --kind class
python scripts/gpq.py hier GpmlTimeSample
```
