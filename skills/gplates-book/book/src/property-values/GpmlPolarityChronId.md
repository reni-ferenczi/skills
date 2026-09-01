# GpmlPolarityChronId

[Book TOC](../../TOC.md) · [property-values](../../components/property-values.md) · cluster Community 948 · tier 3

| Source file | Kind | Lines |
|---|---|---|
| `src/property-values/GpmlPolarityChronId.h` | C++ | 248 |
| `src/property-values/GpmlPolarityChronId.cc` | C++ | 50 |

## Overview

Encodes a polarity chron identifier from the GPML model, with three optional attributes: an era code (text), a major region number, and a minor region code. All three attributes are optional and may be absent; when set, they trigger instance-id updates to track property changes. This class inherits from `PropertyValue` and enforces heap allocation via protected constructors to integrate with GPlates' memory-managed property value system.

## Declared types

| Name | Kind | Bases | Template | Subclasses | Description |
|---|---|---|---|---|---|
| [`GPlatesPropertyValues::GpmlPolarityChronId`](#gplatespropertyvaluesgpmlpolaritychronid) | class | [`GPlatesModel::PropertyValue`](../model/PropertyValue.md) | — | 0 | This class implements the PropertyValue which corresponds to "gpml:PolarityChronId". |

## Members

### `GPlatesPropertyValues::GpmlPolarityChronId`

| Member | Kind | Type | Access | Description |
|---|---|---|---|---|
| `non_null_ptr_type` | typedef | `GPlatesUtils::non_null_intrusive_ptr<GpmlPolarityChronId>` | public | A convenience typedef for GPlatesUtils::non\_null\_intrusive\_ptr\<GpmlPolarityChronId\>. |
| `non_null_ptr_to_const_type` | typedef | `GPlatesUtils::non_null_intrusive_ptr<const GpmlPolarityChronId>` | public | A convenience typedef for GPlatesUtils::non\_null\_intrusive\_ptr\<const GpmlPolarityChronId\>. |
| `~GpmlPolarityChronId()` | destructor | `None` | public | — |
| `create( boost::optional<QString> era, boost::optional<unsigned int> major_region, boost::optional<QString> minor_region)` | method | `non_null_ptr_type` | public | Create a GpmlPolarityChronId instance. |
| `clone()` | method | `non_null_ptr_type` | public | — |
| `deep_clone()` | method | `non_null_ptr_type` | public | — |
| `DEFINE_FUNCTION_DEEP_CLONE_AS_PROP_VAL()` | method | `None` | public | — |
| `set_era( const QString &era)` | method | `void` | public | Set the "era" attribute of this GpmlPolarityChronId instance. |
| `set_major_region( unsigned int major_region)` | method | `void` | public | Set the "major region" attribute of this GpmlPolarityChronId instance. |
| `set_minor_region( const QString &minor_region)` | method | `void` | public | Set the "minor region" attribute of this GpmlPolarityChronId instance. |
| `get_structural_type()` | method | `StructuralType` | public | Returns the structural type associated with this property value class. |
| `accept_visitor( GPlatesModel::ConstFeatureVisitor &visitor)` | method | `void` | public | Accept a ConstFeatureVisitor instance. |
| `accept_visitor( GPlatesModel::FeatureVisitor &visitor)` | method | `void` | public | Accept a FeatureVisitor instance. |
| `print_to` | field | `std::ostream` | public | — |
| `GpmlPolarityChronId( boost::optional<QString> era, boost::optional<unsigned int> major_region, boost::optional<QString> minor_region)` | constructor | `None` | protected | This constructor should not be public, because we don't want to allow instantiation of this type on the stack. |
| `GpmlPolarityChronId( const GpmlPolarityChronId &other)` | constructor | `None` | protected | This constructor should not be public, because we don't want to allow instantiation of this type on the stack. |
| `d_era` | field | `boost::optional<QString>` | private | — |
| `d_major_region` | field | `boost::optional<unsigned int>` | private | — |
| `d_minor_region` | field | `boost::optional<QString>` | private | — |
| `operator=` | field | `GpmlPolarityChronId` | private | This operator should never be defined, because we don't want/need to allow copy-assignment: All copying should use the virtual copy-constructor 'clone' (which will in turn use the copy-constructor); all "assignment" should really only be ... |

## Free functions and macros

| Name | Kind | Type / body | Description |
|---|---|---|---|
| `GPLATES_PROPERTYVALUES_GPMLPOLARITYCHRONID_H` | macro | `None` | — |

## Notes

*None.*

## Used by

| Unit | Component | References |
|---|---|---|
| [qt-widgets/EditPolarityChronIdWidget](../qt-widgets/EditPolarityChronIdWidget.md) | qt-widgets | 4 |
| [file-io/GpmlPropertyStructuralTypeReaderUtils](../file-io/GpmlPropertyStructuralTypeReaderUtils.md) | file-io | 3 |
| [data-mining/GetValueFromPropertyVisitor](../data-mining/GetValueFromPropertyVisitor.md) | data-mining | 1 |
| [data-mining/PopulateShapeFileAttributesVisitor](../data-mining/PopulateShapeFileAttributesVisitor.md) | data-mining | 1 |
| [feature-visitors/ShapefileAttributeFinder](../feature-visitors/ShapefileAttributeFinder.md) | feature-visitors | 1 |
| [feature-visitors/ToQvariantConverter](../feature-visitors/ToQvariantConverter.md) | feature-visitors | 1 |
| [feature-visitors/TopologySectionsFinder](../feature-visitors/TopologySectionsFinder.md) | feature-visitors | 1 |
| [file-io/GMTFormatHeader](../file-io/GMTFormatHeader.md) | file-io | 1 |
| [file-io/GpmlOutputVisitor](../file-io/GpmlOutputVisitor.md) | file-io | 1 |
| [utils/GetPropertyAsPythonObjVisitor](../utils/GetPropertyAsPythonObjVisitor.md) | utils | 1 |

## Related

*None.*

## Explore

Run these from the `gplates-code` skill directory:

```bash
python scripts/gpq.py file src/property-values/GpmlPolarityChronId.h
python scripts/gpq.py def GPlatesPropertyValues::GpmlPolarityChronId --body
python scripts/gpq.py uses GpmlPolarityChronId --kind class
python scripts/gpq.py hier GpmlPolarityChronId
```
