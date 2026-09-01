# ScribeExportRegistration

[Book TOC](../../TOC.md) · [scribe](../../components/scribe.md) · cluster Community 16 · tier 3

| Source file | Kind | Lines |
|---|---|---|
| `src/scribe/ScribeExportRegistration.h` | C++ | 235 |

## Overview

This unit defines the macro framework for registering polymorphic classes and variant types with the `Scribe` serialization system. Polymorphic classes (those with virtual methods) and types used in `boost::variant` objects must be registered so that when a base-class pointer or variant is transcribed, the loader knows which derived type to instantiate. Each module defines a `SCRIBE_EXPORT_<module>` macro listing its types; the `SCRIBE_EXPORT_REGISTRATION` macro takes the combined registry and invokes `ExportRegistry::register_class_type<T>()` for each at program startup. The macros use Boost.Preprocessor to expand a sequence of (type, id-string) tuples into individual registration calls.

## Declared types

*None.*

## Members

*None.*

## Free functions and macros

| Name | Kind | Type / body | Description |
|---|---|---|---|
| `GPLATES_SCRIBE_SCRIBEEXPORTREGISTRATION_H` | macro | `None` | — |
| `SCRIBE_EXPORT_REGISTRATION` | macro_function | `GPlatesScribe::Access::export_registered_classes_type \ GPlatesScribe::Access::export_register_classes() \ { \ export_registered_classes_type export_registered_classes; \ \ \` | This macro should be used in a '.cc' file associated with the program being compiled/linked. |
| `GPLATES_ACCESS_EXPORT_REGISTER_CLASS_TYPE` | macro_function | `export_registered_classes.push_back( \ boost::cref( \ GPlatesScribe::ExportRegistry::instance().register_class_type<class_type>(class_id_name)));` | Only class Access can form the expression 'register\_class\_type\<class\_type\>' because 'class\_type' might be a private nested class of a parent class and only class Access can privately access that parent class (assuming it has a friend ... |
| `GPLATES_ACCESS_EXPORT_REGISTER_CLASS_TYPE_MACRO` | macro_function | `GPLATES_ACCESS_EXPORT_REGISTER_CLASS_TYPE( \ BOOST_PP_TUPLE_ELEM(2, 0, elem), \ BOOST_PP_TUPLE_ELEM(2, 1, elem))` | — |

## Notes

The string identifiers (`ClassIdName`) in each registration are permanent once written to a transcribed archive; changing them breaks compatibility between GPlates releases. If a class is renamed or moved to a different namespace, keep its original identifier. All identifiers must be unique across the entire registration set. Abstract classes with pure virtual methods cannot be registered; attempting to do so causes a compile-time error. Private nested classes require a `friend class GPlatesScribe::Access` declaration in the parent class.

## Used by

| Unit | Component | References |
|---|---|---|
| [entry-points/ScribeExportGPlates](../entry-points/ScribeExportGPlates.md) | entry-points | 2 |
| [entry-points/ScribeExportGPlatesDemoNoGui](../entry-points/ScribeExportGPlatesDemoNoGui.md) | entry-points | 2 |
| [entry-points/ScribeExportGPlatesUnitTest](../entry-points/ScribeExportGPlatesUnitTest.md) | entry-points | 2 |
| [entry-points/ScribeExportPyGPlates](../entry-points/ScribeExportPyGPlates.md) | entry-points | 2 |

## Related

*None.*

## Explore

Run these from the `gplates-code` skill directory:

```bash
python scripts/gpq.py file src/scribe/ScribeExportRegistration.h
```
