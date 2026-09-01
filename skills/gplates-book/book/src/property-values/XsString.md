# XsString

[Book TOC](../../TOC.md) · [property-values](../../components/property-values.md) · cluster Community 1274 · tier 2

| Source file | Kind | Lines |
|---|---|---|
| `src/property-values/XsString.h` | C++ | 201 |
| `src/property-values/XsString.cc` | C++ | 38 |

## Overview

[[[PROSE overview unit=property-values/XsString tier=2]]]
Replace this whole block, markers included, with 1-3 paragraphs: what this unit is, why it exists, and how it fits the surrounding design. Do not restate the tables below.
[[[/PROSE]]]

## Declared types

| Name | Kind | Bases | Template | Subclasses | Description |
|---|---|---|---|---|---|
| [`GPlatesPropertyValues::XsString`](#gplatespropertyvaluesxsstring) | class | [`GPlatesModel::PropertyValue`](../model/PropertyValue.md) | — | 0 | — |

## Members

### `GPlatesPropertyValues::XsString`

| Member | Kind | Type | Access | Description |
|---|---|---|---|---|
| `non_null_ptr_type` | typedef | `GPlatesUtils::non_null_intrusive_ptr<XsString>` | public | A convenience typedef for GPlatesUtils::non\_null\_intrusive\_ptr\<XsString\>. |
| `non_null_ptr_to_const_type` | typedef | `GPlatesUtils::non_null_intrusive_ptr<const XsString>` | public | A convenience typedef for GPlatesUtils::non\_null\_intrusive\_ptr\<const XsString\>. |
| `~XsString()` | destructor | `None` | public | — |
| `create( const GPlatesUtils::UnicodeString &s)` | method | `non_null_ptr_type` | public | — |
| `clone()` | method | `non_null_ptr_type` | public | — |
| `deep_clone()` | method | `non_null_ptr_type` | public | — |
| `DEFINE_FUNCTION_DEEP_CLONE_AS_PROP_VAL()` | method | `None` | public | — |
| `set_value( const TextContent &tc)` | method | `void` | public | Set the TextContent contained within this XsString to tc. |
| `get_structural_type()` | method | `StructuralType` | public | Returns the structural type associated with this property value class. |
| `accept_visitor( GPlatesModel::ConstFeatureVisitor &visitor)` | method | `void` | public | Accept a ConstFeatureVisitor instance. |
| `accept_visitor( GPlatesModel::FeatureVisitor &visitor)` | method | `void` | public | Accept a FeatureVisitor instance. |
| `print_to` | field | `std::ostream` | public | — |
| `XsString( const GPlatesUtils::UnicodeString &s)` | constructor | `None` | protected | This constructor should not be public, because we don't want to allow instantiation of this type on the stack. |
| `XsString( const XsString &other)` | constructor | `None` | protected | This constructor should not be public, because we don't want to allow instantiation of this type on the stack. |
| `d_value` | field | `TextContent` | private | — |
| `operator=` | field | `XsString` | private | This operator should never be defined, because we don't want/need to allow copy-assignment: All copying should use the virtual copy-constructor 'clone' (which will in turn use the copy-constructor); all "assignment" should really only be ... |

## Free functions and macros

| Name | Kind | Type / body | Description |
|---|---|---|---|
| `GPLATES_PROPERTYVALUES_XSSTRING_H` | macro | `None` | — |

## Notes

[[[PROSE notes unit=property-values/XsString tier=2]]]
Replace this whole block, markers included, with invariants, ownership, threading or gotchas that are not visible in the tables. Write *None.* if there is nothing worth saying.
[[[/PROSE]]]

## Used by

| Unit | Component | References |
|---|---|---|
| [file-io/GpmlPropertyStructuralTypeReaderUtils](../file-io/GpmlPropertyStructuralTypeReaderUtils.md) | file-io | 11 |
| [property-values/GmlFile](GmlFile.md) | property-values | 9 |
| [property-values/GpmlKeyValueDictionaryElement](GpmlKeyValueDictionaryElement.md) | property-values | 8 |
| [feature-visitors/deprecated/XsStringFinder](../feature-visitors/deprecated/XsStringFinder.md) | feature-visitors | 6 |
| [property-values/GpmlTimeSample](GpmlTimeSample.md) | property-values | 5 |
| [file-io/GmapReader](../file-io/GmapReader.md) | file-io | 3 |
| [property-values/GmlRectifiedGrid](GmlRectifiedGrid.md) | property-values | 3 |
| [data-mining/GetValueFromPropertyVisitor](../data-mining/GetValueFromPropertyVisitor.md) | data-mining | 2 |
| [gui/ExportRasterAnimationStrategy](../gui/ExportRasterAnimationStrategy.md) | gui | 2 |
| [qt-widgets/EditStringWidget](../qt-widgets/EditStringWidget.md) | qt-widgets | 2 |
| [utils/GetPropertyAsPythonObjVisitor](../utils/GetPropertyAsPythonObjVisitor.md) | utils | 2 |
| [app-logic/ExtractRasterFeatureProperties](../app-logic/ExtractRasterFeatureProperties.md) | app-logic | 1 |
| [app-logic/ExtractScalarField3DFeatureProperties](../app-logic/ExtractScalarField3DFeatureProperties.md) | app-logic | 1 |
| [app-logic/ResolvedTopologicalNetwork](../app-logic/ResolvedTopologicalNetwork.md) | app-logic | 1 |
| [app-logic/TopologyInternalUtils](../app-logic/TopologyInternalUtils.md) | app-logic | 1 |
| [app-logic/TopologyNetworkResolver](../app-logic/TopologyNetworkResolver.md) | app-logic | 1 |
| [app-logic/deprecated/PaleomagUtils](../app-logic/deprecated/PaleomagUtils.md) | app-logic | 1 |
| [canvas-tools/BuildTopology](../canvas-tools/BuildTopology.md) | canvas-tools | 1 |
| [canvas-tools/EditTopology](../canvas-tools/EditTopology.md) | canvas-tools | 1 |
| [data-mining/CheckAttrTypeVisitor](../data-mining/CheckAttrTypeVisitor.md) | data-mining | 1 |

*... and 40 more units.*

## Related

*None.*

## Explore

Run these from the `gplates-code` skill directory:

```bash
python scripts/gpq.py file src/property-values/XsString.h
python scripts/gpq.py def GPlatesPropertyValues::XsString --body
python scripts/gpq.py uses XsString --kind class
python scripts/gpq.py hier XsString
```
