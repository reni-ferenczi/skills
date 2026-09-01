# GpmlPropertyStructuralTypeReader

[Book TOC](../../TOC.md) · [file-io](../../components/file-io.md) · cluster Community 845 · tier 1

| Source file | Kind | Lines |
|---|---|---|
| `src/file-io/GpmlPropertyStructuralTypeReader.h` | C++ | 194 |
| `src/file-io/GpmlPropertyStructuralTypeReader.cc` | C++ | 335 |

## Overview

[[[PROSE overview unit=file-io/GpmlPropertyStructuralTypeReader tier=1]]]
Replace this whole block, markers included, with 1-3 paragraphs: what this unit is, why it exists, and how it fits the surrounding design. Do not restate the tables below.
[[[/PROSE]]]

## Declared types

| Name | Kind | Bases | Template | Subclasses | Description |
|---|---|---|---|---|---|
| [`GPlatesFileIO::GpmlPropertyStructuralTypeReader`](#gplatesfileiogpmlpropertystructuraltypereader) | class | [`GPlatesUtils::ReferenceCount<GpmlPropertyStructuralTypeReader>`](../utils/ReferenceCount.md) | — | 0 | This class encapsulates mappings from (fully qualified) structural type names (for feature properties only) to creation functions that read them from a GPML file (XML element nodes). structural type name -----\> creation\_function NOTE: Only ... |

## Members

### `GPlatesFileIO::GpmlPropertyStructuralTypeReader`

| Member | Kind | Type | Access | Description |
|---|---|---|---|---|
| `non_null_ptr_type` | typedef | `GPlatesUtils::non_null_intrusive_ptr<GpmlPropertyStructuralTypeReader>` | public | A convenience typedef for a shared pointer to a non-const GpmlPropertyStructuralTypeReader. |
| `non_null_ptr_to_const_type` | typedef | `GPlatesUtils::non_null_intrusive_ptr<const GpmlPropertyStructuralTypeReader>` | public | A convenience typedef for a shared pointer to a const GpmlPropertyStructuralTypeReader. |
| `structural_type_reader_function_type` | typedef | `boost::function< GPlatesModel::PropertyValue::non_null_ptr_type ( const GPlatesModel::XmlElementNode::non_null_ptr_type &, const GPlatesModel::GpgimVersion &/*gpml_file_version*/, ...` | public | Typedef for a function that reads a structural type (returned as a PropertyValue) from an XML element node. |
| `create()` | method | `non_null_ptr_type` | public | Creates a GpmlPropertyStructuralTypeReader object containing all structural types specified in the GPGIM (including the time-dependent wrapper structural types such as 'gpml:ConstantValue'). |
| `create_empty()` | method | `non_null_ptr_type` | public | Creates a GpmlPropertyStructuralTypeReader object with \*no\* structural types defined. |
| `~GpmlPropertyStructuralTypeReader()` | destructor | `None` | public | — |
| `get_structural_type_reader_function( const GPlatesPropertyValues::StructuralType &structural_type)` | method | `boost::optional<structural_type_reader_function_type>` | public | Returns the structural type reader function associated with the specified (fully qualified) structural type. |
| `add_time_dependent_wrapper_structural_types()` | method | `void` | public | Adds the time-dependent wrapper structural types. |
| `add_native_structural_types()` | method | `void` | public | Adds all native (non-enumeration) property structural types defined in the GPGIM. |
| `add_enumeration_structural_types()` | method | `void` | public | Adds all enumeration types defined in the GPGIM. |
| `add_structural_type( const GPlatesPropertyValues::StructuralType &structural_type, const structural_type_reader_function_type &reader_function)` | method | `void` | public | Adds an arbitrary structural type with its associated reader function. |
| `structural_type_reader_map_type` | typedef | `std::map< GPlatesPropertyValues::StructuralType, structural_type_reader_function_type>` | private | Typedef for a map of structural type to structural reader function. |
| `d_structural_type_reader_map` | field | `structural_type_reader_map_type` | private | — |
| `GpmlPropertyStructuralTypeReader()` | constructor | `None` | private | — |
| `add_all_structural_types()` | method | `void` | private | — |

## Free functions and macros

| Name | Kind | Type / body | Description |
|---|---|---|---|
| `GPLATES_FILEIO_GPMLPROPERTYSTRUCTURALTYPEREADER_H` | macro | `None` | — |

## Notes

[[[PROSE notes unit=file-io/GpmlPropertyStructuralTypeReader tier=1]]]
Replace this whole block, markers included, with invariants, ownership, threading or gotchas that are not visible in the tables. Write *None.* if there is nothing worth saying.
[[[/PROSE]]]

## Used by

| Unit | Component | References |
|---|---|---|
| [file-io/GpmlStructuralTypeReaderUtils](GpmlStructuralTypeReaderUtils.md) | file-io | 615 |
| [file-io/GpmlPropertyStructuralTypeReaderUtils](GpmlPropertyStructuralTypeReaderUtils.md) | file-io | 569 |
| [file-io/GpmlUpgradeReaderUtils](GpmlUpgradeReaderUtils.md) | file-io | 165 |
| [file-io/GpmlFeatureReaderFactory](GpmlFeatureReaderFactory.md) | file-io | 141 |
| [file-io/GpmlPropertyReader](GpmlPropertyReader.md) | file-io | 135 |
| [file-io/GpmlFeatureReaderImpl](GpmlFeatureReaderImpl.md) | file-io | 84 |
| [entry-points/gplates_demo_no_gui_main](../entry-points/gplates_demo_no_gui_main.md) | entry-points | 65 |
| [file-io/GpmlReader](GpmlReader.md) | file-io | 26 |
| [file-io/FeatureCollectionFileFormatRegistry](FeatureCollectionFileFormatRegistry.md) | file-io | 21 |
| [file-io/GpmlFeatureReaderInterface](GpmlFeatureReaderInterface.md) | file-io | 2 |

## Related

*None.*

## Explore

Run these from the `gplates-code` skill directory:

```bash
python scripts/gpq.py file src/file-io/GpmlPropertyStructuralTypeReader.h
python scripts/gpq.py def GPlatesFileIO::GpmlPropertyStructuralTypeReader --body
python scripts/gpq.py uses GpmlPropertyStructuralTypeReader --kind class
python scripts/gpq.py hier GpmlPropertyStructuralTypeReader
```
