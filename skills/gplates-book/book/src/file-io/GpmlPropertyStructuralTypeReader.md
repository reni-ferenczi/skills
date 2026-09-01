# GpmlPropertyStructuralTypeReader

[Book TOC](../../TOC.md) · [file-io](../../components/file-io.md) · cluster Community 845 · tier 1

| Source file | Kind | Lines |
|---|---|---|
| `src/file-io/GpmlPropertyStructuralTypeReader.h` | C++ | 194 |
| `src/file-io/GpmlPropertyStructuralTypeReader.cc` | C++ | 335 |

## Overview

This is the dispatch table that answers "given the structural type name on this GPML element, which function parses it into a `GPlatesModel::PropertyValue`?". It is a single `std::map` from `GPlatesPropertyValues::StructuralType` to a `boost::function`, and every parsing function it hands out lives in `GpmlPropertyStructuralTypeReaderUtils`. `GpmlPropertyReader` holds one of these and consults it once per property; `GpmlFeatureReaderFactory` threads it down into every `GpmlFeatureReader` in a chain. In practice the whole GPML read path shares the one instance created by `FeatureCollectionFileFormatRegistry`, which is why the class is reference-counted rather than a free function table.

Three sources feed the map, and the separation matters. Time-dependent wrappers (`gpml:ConstantValue`, `gpml:IrregularSampling`, `gpml:PiecewiseAggregation`) and the aggregate types `gpml:Array` and `gpml:KeyValueDictionary` are bound with `boost::cref(*this)` so that the reader is passed back into their own parse function — these types contain nested property values, so parsing is recursive through the same table. Native leaf types (the `xsi:`, `gml:` and non-enumeration `gpml:` entries) are a hard-coded list bound directly to their `create_*` functions. Enumerations are not hard-coded at all: they are enumerated from `GPlatesModel::Gpgim::instance().get_property_enumeration_types()` and all bound to the same `create_gpml_enumeration` with the `GpgimEnumerationType` captured, so adding an enumeration to `gpgim.xml` needs no C++ change while adding a native type does.

`create_empty` plus the individual `add_*` methods exist for the old-GPML upgrade path rather than for general use. `GpmlUpgradeReaderUtils` builds a throwaway reader containing only the time-dependent wrappers plus its own reader functions for structural types that no longer exist in the current GPGIM (`gpml:TopologicalInterior`, and an old-format `gpml:TopologicalPolygon`), so that a deprecated property can be parsed with old semantics and then rewritten into a current one. `add_structural_type` is the hook for that: it overwrites whatever entry the type already had.

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

The recursive entries capture `boost::cref(*this)`, so a `GpmlPropertyStructuralTypeReader` must not be copied or moved after its map is populated — the bound references would dangle. It is only ever created through the static factories into a `non_null_intrusive_ptr`, which keeps that safe as long as you do not add another construction path.

Adding a native structural type means editing `add_native_structural_types` *and* the GPGIM XML. `add_all_structural_types` cross-checks the finished map against `Gpgim::instance().get_property_structural_types()` and, for anything the GPGIM declares but the map lacks, emits only a `qWarning()` — the code says outright that it perhaps should throw. So a type you forgot to register produces a console warning at startup and then silently fails to parse at load time, with the property demoted to an `UninterpretedPropertyValue` by the readers above. The check does not run in the other direction: a map entry with no GPGIM counterpart is not reported.

The class holds an unguarded `std::map` and calls `Gpgim::instance()`, so construction depends on the GPGIM singleton already being loaded. Lookups are const and thread-safe against each other, but the `add_*` methods mutate the map and must not run concurrently with a read — in practice the shared instance is fully populated by `create()` before any file is opened, and the upgrade path builds its own private instance instead of mutating the shared one. Follow that pattern rather than adding types to the shared reader.

`add_structural_type` and the other `add_*` methods use `operator[]` assignment, so a later registration silently replaces an earlier one for the same type. `add_enumeration_structural_types` therefore overrides any hard-coded native entry that happens to share a structural type name with a GPGIM enumeration. Note that a nested type like `gpml:TopologicalSection`, which can never be a top-level feature property, is deliberately absent from this map; those are parsed by the enclosing type's function directly.

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
