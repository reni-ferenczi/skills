# ScribeExportRegistration

[Book TOC](../../TOC.md) · [scribe](../../components/scribe.md) · cluster Community 16 · tier 3

| Source file | Kind | Lines |
|---|---|---|
| `src/scribe/ScribeExportRegistration.h` | C++ | 235 |

## Overview

[[[PROSE overview unit=scribe/ScribeExportRegistration tier=3]]]
Replace this whole block, markers included, with 1-3 paragraphs: what this unit is, why it exists, and how it fits the surrounding design. Do not restate the tables below.
[[[/PROSE]]]

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

[[[PROSE notes unit=scribe/ScribeExportRegistration tier=3]]]
Replace this whole block, markers included, with invariants, ownership, threading or gotchas that are not visible in the tables. Write *None.* if there is nothing worth saying.
[[[/PROSE]]]

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
