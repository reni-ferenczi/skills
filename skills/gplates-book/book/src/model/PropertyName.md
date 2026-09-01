# PropertyName

[Book TOC](../../TOC.md) · [model](../../components/model.md) · cluster Community 138 · tier 1

| Source file | Kind | Lines |
|---|---|---|
| `src/model/PropertyName.h` | C++ | 55 |

## Overview

`PropertyName` is the interned, namespace-qualified name of a top-level property of a
feature — `gpml:reconstructionPlateId`, `gml:validTime`, and so on. It is nothing more
than `QualifiedXmlName` instantiated on `PropertyNameFactory`, and `PropertyNameFactory`
in turn does nothing but name the process-wide string pool that property names live in:
its single static `instance()` forwards to `StringSetSingletons::property_name_instance()`.
The class is uninstantiable on purpose — its only constructor is private and never
defined — because it is a compile-time tag, not an object.

That indirection is what keeps the seven `QualifiedXmlName` instantiations in the tree
apart. `FeatureType`, `StructuralType`, `XmlAttributeName`, `XmlElementName`,
`EnumerationType` and `ValueObjectType` are built the same way, each with its own factory
tag and its own `GPlatesUtils::StringSet` singleton, so a property name and a feature type
that happen to spell the same word are stored in different pools and are different types.
Every `TopLevelProperty` carries one `PropertyName`, `Gpgim` keys its property definitions
by it, and the readers and writers in `file-io` construct them from XML through the
`create_gpml` / `create_gml` named constructors inherited from `QualifiedXmlName`.

## Declared types

| Name | Kind | Bases | Template | Subclasses | Description |
|---|---|---|---|---|---|
| [`GPlatesModel::PropertyNameFactory`](#gplatesmodelpropertynamefactory) | class | — | — | 0 | — |
| [`GPlatesModel::PropertyName`](#gplatesmodelpropertyname) | typedef | — | — | 0 | — |

## Members

### `GPlatesModel::PropertyNameFactory`

| Member | Kind | Type | Access | Description |
|---|---|---|---|---|
| `PropertyNameFactory()` | constructor | `None` | private | — |

### `GPlatesModel::PropertyName`

*None.*

## Free functions and macros

| Name | Kind | Type / body | Description |
|---|---|---|---|
| `GPLATES_MODEL_PROPERTYNAME_H` | macro | `None` | — |

## Notes

All the behaviour — comparison, lifetime, construction cost — comes from
`QualifiedXmlName`; read its notes before changing anything here. Two points are specific
to this header:

- There is no implicit conversion between name kinds. `QualifiedXmlName`'s cross-type
  constructor is `explicit` and re-inserts the local name into the target instantiation's
  `StringSet`, so writing `FeatureType(some_property_name)` is a fresh interning in a
  different pool, not a cast.
- `StringSetSingletons::property_name_instance()` is a `GPlatesUtils::Singleton` created
  lazily on first use, and that singleton template is not thread-safe unless
  `GPLATES_SINGLETON_THREADSAFE` is defined (it is not, in this build). Constructing
  `PropertyName` values from more than one thread races on the shared `std::set`.

## Used by

| Unit | Component | References |
|---|---|---|
| [file-io/deprecated/FeaturePropertiesMap](../file-io/deprecated/FeaturePropertiesMap.md) | file-io | 194 |
| [qt-widgets/CreateFeatureDialog](../qt-widgets/CreateFeatureDialog.md) | qt-widgets | 73 |
| [file-io/PlatesLineFormatReader](../file-io/PlatesLineFormatReader.md) | file-io | 72 |
| [file-io/GpmlUpgradeReaderUtils](../file-io/GpmlUpgradeReaderUtils.md) | file-io | 36 |
| [app-logic/ScalarCoverageFeatureProperties](../app-logic/ScalarCoverageFeatureProperties.md) | app-logic | 28 |
| [app-logic/PartitionFeatureUtils](../app-logic/PartitionFeatureUtils.md) | app-logic | 27 |
| [file-io/OgrFeatureCollectionWriter](../file-io/OgrFeatureCollectionWriter.md) | file-io | 27 |
| [model/ModelUtils](ModelUtils.md) | model | 25 |
| [file-io/CitcomsGMTFormatResolvedTopologicalBoundaryExport](../file-io/CitcomsGMTFormatResolvedTopologicalBoundaryExport.md) | file-io | 24 |
| [file-io/OgrReader](../file-io/OgrReader.md) | file-io | 24 |
| [feature-visitors/FeatureClassifier](../feature-visitors/FeatureClassifier.md) | feature-visitors | 23 |
| [file-io/GpmlFeatureReaderFactory](../file-io/GpmlFeatureReaderFactory.md) | file-io | 22 |
| [file-io/OgrUtils](../file-io/OgrUtils.md) | file-io | 21 |
| [model/Gpgim](Gpgim.md) | model | 21 |
| [app-logic/ExtractRasterFeatureProperties](../app-logic/ExtractRasterFeatureProperties.md) | app-logic | 18 |
| [file-io/GpmlFormatMultiPointVectorFieldExport](../file-io/GpmlFormatMultiPointVectorFieldExport.md) | file-io | 18 |
| [app-logic/deprecated/PaleomagUtils](../app-logic/deprecated/PaleomagUtils.md) | app-logic | 17 |
| [app-logic/ReconstructionFeatureProperties](../app-logic/ReconstructionFeatureProperties.md) | app-logic | 15 |
| [app-logic/deprecated/ReconstructedFeatureGeometryPopulator](../app-logic/deprecated/ReconstructedFeatureGeometryPopulator.md) | app-logic | 14 |
| [file-io/GsmlPropertyHandlers](../file-io/GsmlPropertyHandlers.md) | file-io | 13 |

*... and 105 more units.*

## Related

*None.*

## Explore

Run these from the `gplates-code` skill directory:

```bash
python scripts/gpq.py file src/model/PropertyName.h
python scripts/gpq.py def GPlatesModel::PropertyNameFactory --body
python scripts/gpq.py uses PropertyNameFactory --kind class
python scripts/gpq.py hier PropertyNameFactory
```
