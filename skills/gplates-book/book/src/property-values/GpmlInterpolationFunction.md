# GpmlInterpolationFunction

[Book TOC](../../TOC.md) · [property-values](../../components/property-values.md) · cluster Community 1051 · tier 2

| Source file | Kind | Lines |
|---|---|---|
| `src/property-values/GpmlInterpolationFunction.h` | C++ | 169 |
| `src/property-values/GpmlInterpolationFunction.cc` | C++ | 40 |

## Overview

[[[PROSE overview unit=property-values/GpmlInterpolationFunction tier=2]]]
Replace this whole block, markers included, with 1-3 paragraphs: what this unit is, why it exists, and how it fits the surrounding design. Do not restate the tables below.
[[[/PROSE]]]

## Declared types

| Name | Kind | Bases | Template | Subclasses | Description |
|---|---|---|---|---|---|
| [`GPlatesPropertyValues::GpmlInterpolationFunction`](#gplatespropertyvaluesgpmlinterpolationfunction) | class | [`GPlatesModel::PropertyValue`](../model/PropertyValue.md) | — | 1 | This is an abstract class, because it derives from class PropertyValue, which contains the pure virtual member functions clone and accept\_visitor, which this class does not override with non-pure-virtual definitions. |

## Members

### `GPlatesPropertyValues::GpmlInterpolationFunction`

| Member | Kind | Type | Access | Description |
|---|---|---|---|---|
| `maybe_null_ptr_type` | typedef | `boost::intrusive_ptr<GpmlInterpolationFunction>` | public | A convenience typedef for boost::intrusive\_ptr\<GpmlInterpolationFunction\>. |
| `maybe_null_ptr_to_const_type` | typedef | `boost::intrusive_ptr<const GpmlInterpolationFunction>` | public | A convenience typedef for boost::intrusive\_ptr\<const GpmlInterpolationFunction\>. |
| `non_null_ptr_type` | typedef | `GPlatesUtils::non_null_intrusive_ptr<GpmlInterpolationFunction>` | public | A convenience typedef for GPlatesUtils::non\_null\_intrusive\_ptr\<GpmlInterpolationFunction\>. |
| `non_null_ptr_to_const_type` | typedef | `GPlatesUtils::non_null_intrusive_ptr<const GpmlInterpolationFunction>` | public | A convenience typedef for GPlatesUtils::non\_null\_intrusive\_ptr\<const GpmlInterpolationFunction\>. |
| `GpmlInterpolationFunction( const StructuralType &value_type_)` | constructor | `None` | public | Construct a GpmlInterpolationFunction instance. |
| `GpmlInterpolationFunction( const GpmlInterpolationFunction &other)` | constructor | `None` | public | Construct a GpmlInterpolationFunction instance which is a copy of other. |
| `~GpmlInterpolationFunction()` | destructor | `None` | public | — |
| `deep_clone_as_interp_func()` | method | `GpmlInterpolationFunction::non_null_ptr_type` | public | — |
| `get_structural_type()` | method | `StructuralType` | public | Returns the structural type associated with this property value class. |
| `print_to` | field | `std::ostream` | public | — |
| `d_value_type` | field | `StructuralType` | private | — |
| `operator=` | field | `GpmlInterpolationFunction` | private | This operator should never be defined, because we don't want/need to allow copy-assignment: All copying should use the virtual copy-constructor 'clone' (which will in turn use the copy-constructor); all "assignment" should really only be ... |

## Free functions and macros

| Name | Kind | Type / body | Description |
|---|---|---|---|
| `GPLATES_PROPERTYVALUES_GPMLINTERPOLATIONFUNCTION_H` | macro | `None` | — |
| `DEFINE_FUNCTION_DEEP_CLONE_AS_INTERP_FUNC` | macro_function | `virtual \ const GpmlInterpolationFunction::non_null_ptr_type \ deep_clone_as_interp_func() const \ { \ return deep_clone(); \ }` | This macro is used to define the virtual function 'deep\_clone\_as\_interp\_func' inside a class which derives from InterpolationFunction. |

## Notes

[[[PROSE notes unit=property-values/GpmlInterpolationFunction tier=2]]]
Replace this whole block, markers included, with invariants, ownership, threading or gotchas that are not visible in the tables. Write *None.* if there is nothing worth saying.
[[[/PROSE]]]

## Used by

| Unit | Component | References |
|---|---|---|
| [property-values/GpmlIrregularSampling](GpmlIrregularSampling.md) | property-values | 17 |
| [file-io/GpmlStructuralTypeReaderUtils](../file-io/GpmlStructuralTypeReaderUtils.md) | file-io | 5 |
| [property-values/GpmlFiniteRotationSlerp](GpmlFiniteRotationSlerp.md) | property-values | 4 |
| [file-io/GpmlPropertyStructuralTypeReaderUtils](../file-io/GpmlPropertyStructuralTypeReaderUtils.md) | file-io | 3 |
| [data-mining/GetValueFromPropertyVisitor](../data-mining/GetValueFromPropertyVisitor.md) | data-mining | 2 |
| [utils/GetPropertyAsPythonObjVisitor](../utils/GetPropertyAsPythonObjVisitor.md) | utils | 2 |
| [file-io/PlatesRotationFileProxy](../file-io/PlatesRotationFileProxy.md) | file-io | 1 |
| [file-io/PlatesRotationFormatReader](../file-io/PlatesRotationFormatReader.md) | file-io | 1 |

## Related

*None.*

## Explore

Run these from the `gplates-code` skill directory:

```bash
python scripts/gpq.py file src/property-values/GpmlInterpolationFunction.h
python scripts/gpq.py def GPlatesPropertyValues::GpmlInterpolationFunction --body
python scripts/gpq.py uses GpmlInterpolationFunction --kind class
python scripts/gpq.py hier GpmlInterpolationFunction
```
