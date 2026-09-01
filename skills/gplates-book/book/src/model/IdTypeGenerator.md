# IdTypeGenerator

[Book TOC](../../TOC.md) · [model](../../components/model.md) · cluster Community 885 · tier 2

| Source file | Kind | Lines |
|---|---|---|
| `src/model/IdTypeGenerator.h` | C++ | 352 |

## Overview

`IdTypeGenerator` is the template that produces GPlates' ID types (feature IDs,
revision IDs and the like): a Unicode string interned into a `SingletonType`
(a `GPlatesUtils::IdStringSet`, one instance per ID kind, see `StringSetSingletons`),
so that two IDs with equal text share the same underlying string and can be
compared for equality by comparing iterators instead of characters, and checking
whether an ID string is already in use is an O(log n) set lookup rather than a scan
over every feature. Use `QualifiedXmlName` instead for XML qualified names like
`gml:Point`, and `StringContentTypeGenerator` for other interned strings that
are not IDs.

An ID can optionally be *defined* by one object — the "back-reference target" —
via `set_back_ref_target()`, which registers a nested `BackRef` (an RAII node
linked into the ID's back-reference list; it deregisters itself automatically on
destruction). A `FeatureId`, for example, back-references the `FeatureHandle` that
defines it, but not the `GpmlPropertyDelegate` instances that merely reference the
same ID; `find_back_ref_targets()` walks that list to recover the defining objects
for a given ID string. Copying or copy-assigning an `IdTypeGenerator` never copies
the back-reference, since the source object's back-reference names *its* container,
which is not necessarily the copy's container.

## Declared types

| Name | Kind | Bases | Template | Subclasses | Description |
|---|---|---|---|---|---|
| [`GPlatesModel::IdTypeGenerator`](#gplatesmodelidtypegenerator) | class | `boost::less_than_comparable< IdTypeGenerator<SingletonType, BackRefTargetType>, boost::equality_comparable< IdTypeGenerator<SingletonType, BackRefTargetType> > >` | `<typename SingletonType, typename BackRefTargetType>` | 0 | This class provides an efficient means of containing an ID, which is a Unicode string. |

## Members

### `GPlatesModel::IdTypeGenerator`

| Member | Kind | Type | Access | Description |
|---|---|---|---|---|
| `back_ref_target_type` | typedef | `BackRefTargetType` | public | — |
| `back_ref_list_type` | typedef | `GPlatesUtils::IdStringSet::back_ref_list_type` | public | — |
| `shared_iterator_type` | typedef | `GPlatesUtils::IdStringSet::SharedIterator` | public | — |
| `BackRef` | class | `None` | public | An RAII class which encapsulates the idea of being a back-reference in a list of registered back-references for a given ID. |
| `is_loaded( const GPlatesUtils::UnicodeString &s)` | method | `bool` | public | Determine whether an arbitrary Unicode string is a member of the collection of loaded ID instances (without inserting the Unicode string into the collection). |
| `IdTypeGenerator()` | constructor | `None` | public | — |
| `IdTypeGenerator( const GPlatesUtils::UnicodeString &s)` | constructor | `None` | public | Instantiate a new ID instance from a UnicodeString instance. |
| `IdTypeGenerator( const IdTypeGenerator &other)` | constructor | `None` | public | Copy constructor. |
| `set_back_ref_target( back_ref_target_type &target)` | method | `void` | public | Set the back-reference target for this ID instance. |
| `find_back_ref_targets( Inserter inserter)` | method | `void` | public | Find all the back-reference targets for this ID. |
| `is_equal_to( const IdTypeGenerator &other)` | method | `bool` | public | Determine whether another Id instance contains the same text content as this instance. |
| `operator==( const IdTypeGenerator &other)` | operator | `bool` | public | Equality comparison operator - inequality operator provided by 'boost::equality\_comparable'. |
| `operator<( const IdTypeGenerator &other)` | operator | `bool` | public | Less-than operator - provided so IdTypeGenerator can be used as a key in std::map. |
| `d_sh_iter` | field | `shared_iterator_type` | private | — |
| `d_back_ref_ptr` | field | `boost::scoped_ptr<const BackRef>` | private | This is a scoped\_ptr, so that it cannot be shared between IdTypeGenerator instances which are copied or copy-assigned. |

## Free functions and macros

| Name | Kind | Type / body | Description |
|---|---|---|---|
| `GPLATES_MODEL_IDTYPEGENERATOR_H` | macro | `None` | — |

## Notes

A `BackRef` is non-copyable and expected to be heap-allocated; `d_back_ref_ptr` is a
`boost::scoped_ptr` specifically so a back-reference can never end up shared between
two `IdTypeGenerator` instances produced by copying. The base classes are chained
(`less_than_comparable<..., equality_comparable<...>>`) rather than inherited in
parallel, to avoid growing `sizeof(IdTypeGenerator)` with multiple empty bases.

## Used by

| Unit | Component | References |
|---|---|---|
| [presentation/ReconstructionGeometryRenderer](../presentation/ReconstructionGeometryRenderer.md) | presentation | 3 |
| [view-operations/VisibleReconstructionGeometryExport](../view-operations/VisibleReconstructionGeometryExport.md) | view-operations | 3 |
| [model/FeatureId](FeatureId.md) | model | 2 |
| [app-logic/TopologyInternalUtils](../app-logic/TopologyInternalUtils.md) | app-logic | 1 |
| [model/FeatureHandle](FeatureHandle.md) | model | 1 |
| [model/ModelUtils](ModelUtils.md) | model | 1 |

## Related

*None.*

## Explore

Run these from the `gplates-code` skill directory:

```bash
python scripts/gpq.py file src/model/IdTypeGenerator.h
python scripts/gpq.py def GPlatesModel::IdTypeGenerator --body
python scripts/gpq.py uses IdTypeGenerator --kind class
python scripts/gpq.py hier IdTypeGenerator
```
