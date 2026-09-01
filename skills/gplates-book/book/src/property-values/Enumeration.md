# Enumeration

[Book TOC](../../TOC.md) · [property-values](../../components/property-values.md) · cluster Community 1069 · tier 2

| Source file | Kind | Lines |
|---|---|---|
| `src/property-values/Enumeration.h` | C++ | 181 |
| `src/property-values/Enumeration.cc` | C++ | 39 |

## Overview

[[[PROSE overview unit=property-values/Enumeration tier=2]]]
Replace this whole block, markers included, with 1-3 paragraphs: what this unit is, why it exists, and how it fits the surrounding design. Do not restate the tables below.
[[[/PROSE]]]

## Declared types

| Name | Kind | Bases | Template | Subclasses | Description |
|---|---|---|---|---|---|
| [`GPlatesPropertyValues::Enumeration`](#gplatespropertyvaluesenumeration) | class | [`GPlatesModel::PropertyValue`](../model/PropertyValue.md) | — | 0 | — |

## Members

### `GPlatesPropertyValues::Enumeration`

| Member | Kind | Type | Access | Description |
|---|---|---|---|---|
| `non_null_ptr_type` | typedef | `GPlatesUtils::non_null_intrusive_ptr<Enumeration>` | public | — |
| `non_null_ptr_to_const_type` | typedef | `GPlatesUtils::non_null_intrusive_ptr<const Enumeration>` | public | — |
| `~Enumeration()` | destructor | `None` | public | — |
| `create( const EnumerationType &enum_type, const GPlatesUtils::UnicodeString &enum_content)` | method | `non_null_ptr_type` | public | — |
| `clone()` | method | `non_null_ptr_type` | public | — |
| `deep_clone()` | method | `Enumeration::non_null_ptr_type` | public | — |
| `DEFINE_FUNCTION_DEEP_CLONE_AS_PROP_VAL()` | method | `None` | public | — |
| `set_value( const EnumerationContent &new_value)` | method | `void` | public | Set the content of this enumeration to new\_value. |
| `get_structural_type()` | method | `StructuralType` | public | Returns the structural type associated with this property value class. |
| `accept_visitor( GPlatesModel::ConstFeatureVisitor &visitor)` | method | `void` | public | — |
| `accept_visitor( GPlatesModel::FeatureVisitor &visitor)` | method | `void` | public | — |
| `print_to` | field | `std::ostream` | public | — |
| `Enumeration( const EnumerationType &enum_type, const GPlatesUtils::UnicodeString &enum_content)` | constructor | `None` | protected | — |
| `Enumeration( const Enumeration &other)` | constructor | `None` | protected | — |
| `d_type` | field | `EnumerationType` | private | — |
| `d_value` | field | `EnumerationContent` | private | — |
| `operator=` | field | `Enumeration` | private | — |

## Free functions and macros

| Name | Kind | Type / body | Description |
|---|---|---|---|
| `GPLATES_PROPERTYVALUES_ENUMERATION_H` | macro | `None` | — |

## Notes

[[[PROSE notes unit=property-values/Enumeration tier=2]]]
Replace this whole block, markers included, with invariants, ownership, threading or gotchas that are not visible in the tables. Write *None.* if there is nothing worth saying.
[[[/PROSE]]]

## Used by

| Unit | Component | References |
|---|---|---|
| [file-io/GpmlPropertyStructuralTypeReaderUtils](../file-io/GpmlPropertyStructuralTypeReaderUtils.md) | file-io | 112 |
| [file-io/GpmlPropertyStructuralTypeReader](../file-io/GpmlPropertyStructuralTypeReader.md) | file-io | 3 |
| [qt-widgets/EditEnumerationWidget](../qt-widgets/EditEnumerationWidget.md) | qt-widgets | 3 |
| [app-logic/ReconstructionFeatureProperties](../app-logic/ReconstructionFeatureProperties.md) | app-logic | 2 |
| [app-logic/ReconstructMethodHalfStageRotation](../app-logic/ReconstructMethodHalfStageRotation.md) | app-logic | 1 |
| [app-logic/RotationUtils](../app-logic/RotationUtils.md) | app-logic | 1 |
| [data-mining/GetValueFromPropertyVisitor](../data-mining/GetValueFromPropertyVisitor.md) | data-mining | 1 |
| [feature-visitors/FromQvariantConverter](../feature-visitors/FromQvariantConverter.md) | feature-visitors | 1 |
| [feature-visitors/QueryFeaturePropertiesWidgetPopulator](../feature-visitors/QueryFeaturePropertiesWidgetPopulator.md) | feature-visitors | 1 |
| [feature-visitors/ToQvariantConverter](../feature-visitors/ToQvariantConverter.md) | feature-visitors | 1 |
| [feature-visitors/TopologySectionsFinder](../feature-visitors/TopologySectionsFinder.md) | feature-visitors | 1 |
| [file-io/CitcomsResolvedTopologicalBoundaryExportImpl](../file-io/CitcomsResolvedTopologicalBoundaryExportImpl.md) | file-io | 1 |
| [file-io/GMTFormatHeader](../file-io/GMTFormatHeader.md) | file-io | 1 |
| [file-io/GpmlOutputVisitor](../file-io/GpmlOutputVisitor.md) | file-io | 1 |
| [file-io/GpmlStructuralTypeReaderUtils](../file-io/GpmlStructuralTypeReaderUtils.md) | file-io | 1 |
| [file-io/OgrUtils](../file-io/OgrUtils.md) | file-io | 1 |
| [file-io/PlatesFormatUtils](../file-io/PlatesFormatUtils.md) | file-io | 1 |
| [file-io/PlatesLineFormatHeaderVisitor](../file-io/PlatesLineFormatHeaderVisitor.md) | file-io | 1 |
| [file-io/PlatesLineFormatReader](../file-io/PlatesLineFormatReader.md) | file-io | 1 |
| [presentation/ReconstructionGeometryRenderer](../presentation/ReconstructionGeometryRenderer.md) | presentation | 1 |

*... and 3 more units.*

## Related

*None.*

## Explore

Run these from the `gplates-code` skill directory:

```bash
python scripts/gpq.py file src/property-values/Enumeration.h
python scripts/gpq.py def GPlatesPropertyValues::Enumeration --body
python scripts/gpq.py uses Enumeration --kind class
python scripts/gpq.py hier Enumeration
```
