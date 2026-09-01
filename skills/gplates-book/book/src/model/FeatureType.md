# FeatureType

[Book TOC](../../TOC.md) · [model](../../components/model.md) · cluster Community 138 · tier 1

| Source file | Kind | Lines |
|---|---|---|
| `src/model/FeatureType.h` | C++ | 55 |

## Overview

A feature's type is a qualified XML name such as `gpml:Isochron`, and this header
is the one-line declaration that makes it one: `FeatureType` is
`QualifiedXmlName<FeatureTypeFactory>`. The whole content of the file is the
choice of which string-interning pool feature-type names live in.
`FeatureTypeFactory` is a tag class whose only job is to name that pool —
`StringSetSingletons::feature_type_instance()` — so that feature-type local names
are interned separately from property names, namespaces and namespace aliases,
each of which has its own factory and its own singleton `StringSet`.

The point of the interning is that a `FeatureType` stores three `StringSet`
iterators rather than three strings. Copying is cheap, equality is an iterator
comparison rather than a string comparison, and every `gpml:Isochron` in a loaded
file shares one copy of the text. `QualifiedXmlName` also supplies the
`create_gpml`, `create_gml`, `create_gpgim` and `create_xsi` factories, which is
how most call sites build a `FeatureType` — the namespace is chosen by which
factory you call.

This header says nothing about which feature types are legal or what properties
they may carry. That is the GPGIM's job: `Gpgim` loads the feature-class
hierarchy from `gpgim.xml` and `GpgimFeatureClass` describes one class. A
`FeatureType` value is just a name, and constructing one that no feature class
defines is not an error at this level.

## Declared types

| Name | Kind | Bases | Template | Subclasses | Description |
|---|---|---|---|---|---|
| [`GPlatesModel::FeatureTypeFactory`](#gplatesmodelfeaturetypefactory) | class | — | — | 0 | — |
| [`GPlatesModel::FeatureType`](#gplatesmodelfeaturetype) | typedef | — | — | 0 | — |

## Members

### `GPlatesModel::FeatureTypeFactory`

| Member | Kind | Type | Access | Description |
|---|---|---|---|---|
| `FeatureTypeFactory()` | constructor | `None` | private | — |

### `GPlatesModel::FeatureType`

*None.*

## Free functions and macros

| Name | Kind | Type / body | Description |
|---|---|---|---|
| `GPLATES_MODEL_FEATURETYPE_H` | macro | `None` | — |

## Notes

**Equality ignores the namespace alias.** `QualifiedXmlName::is_equal_to`
compares only the namespace and the local name, so two `FeatureType`s that print
differently via `build_aliased_name()` can still compare equal. `operator<`,
however, falls back to comparing the name strings when the namespaces differ, so
map ordering is by text and is not the cheap iterator comparison that equality is.

**There is no default constructor** — a `FeatureType` always names something. That
is why `FeatureHandle::create()` requires one while `FeatureId` and `RevisionId`
are defaultable.

**The interning pools are process-wide singletons and are never pruned.** A
`FeatureType` is not tied to any `Model`, and the interned text stays alive for
the process; a name read from a file that is later unloaded is still in the set.
This is deliberate — it is what makes "is this name even loaded anywhere?" an
O(log n) set lookup instead of a walk over every feature.

**`build_aliased_name()` defeats the point of the class**, as its own comment
says: it builds a fresh string on every call. Use it for display, not in
comparisons or loops.

## Used by

| Unit | Component | References |
|---|---|---|
| [file-io/deprecated/FeaturePropertiesMap](../file-io/deprecated/FeaturePropertiesMap.md) | file-io | 106 |
| [file-io/PlatesLineFormatReader](../file-io/PlatesLineFormatReader.md) | file-io | 49 |
| [file-io/GpmlFeatureReaderFactory](../file-io/GpmlFeatureReaderFactory.md) | file-io | 45 |
| [gui/FeatureTypeColourPalette](../gui/FeatureTypeColourPalette.md) | gui | 45 |
| [file-io/PlatesFormatUtils](../file-io/PlatesFormatUtils.md) | file-io | 44 |
| [qt-widgets/ChooseFeatureTypeWidget](../qt-widgets/ChooseFeatureTypeWidget.md) | qt-widgets | 30 |
| [qt-widgets/CreateFeatureDialog](../qt-widgets/CreateFeatureDialog.md) | qt-widgets | 29 |
| [file-io/OgrReader](../file-io/OgrReader.md) | file-io | 26 |
| [model/Gpgim](Gpgim.md) | model | 23 |
| [model/GpgimFeatureClass](GpgimFeatureClass.md) | model | 17 |
| [qt-widgets/CreateFeaturePropertiesPage](../qt-widgets/CreateFeaturePropertiesPage.md) | qt-widgets | 13 |
| [file-io/PlatesRotationFileProxy](../file-io/PlatesRotationFileProxy.md) | file-io | 12 |
| [model/FeatureHandle](FeatureHandle.md) | model | 11 |
| [model/ModelUtils](ModelUtils.md) | model | 11 |
| [qt-widgets/CreateFeatureAddOrEditPropertyDialog](../qt-widgets/CreateFeatureAddOrEditPropertyDialog.md) | qt-widgets | 10 |
| [file-io/SymbolFileReader](../file-io/SymbolFileReader.md) | file-io | 8 |
| [app-logic/PlateVelocityUtils](../app-logic/PlateVelocityUtils.md) | app-logic | 7 |
| [property-values/GpmlFeatureReference](../property-values/GpmlFeatureReference.md) | property-values | 6 |
| [qt-widgets/AddPropertyDialog](../qt-widgets/AddPropertyDialog.md) | qt-widgets | 6 |
| [qt-widgets/ChangeFeatureTypeDialog](../qt-widgets/ChangeFeatureTypeDialog.md) | qt-widgets | 6 |

*... and 48 more units.*

## Related

*None.*

## Explore

Run these from the `gplates-code` skill directory:

```bash
python scripts/gpq.py file src/model/FeatureType.h
python scripts/gpq.py def GPlatesModel::FeatureTypeFactory --body
python scripts/gpq.py uses FeatureTypeFactory --kind class
python scripts/gpq.py hier FeatureTypeFactory
```
