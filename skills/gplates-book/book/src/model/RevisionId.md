# RevisionId

[Book TOC](../../TOC.md) · [model](../../components/model.md) · cluster Community 204 · tier 2

| Source file | Kind | Lines |
|---|---|---|
| `src/model/RevisionId.h` | C++ | 119 |

## Overview

`RevisionId` wraps a `GPlatesUtils::UnicodeString` as a persistent, reasonably-unique
identifier for one revision of a feature, letting other features reference a
specific revision by ID rather than by pointer or by "current state". Unlike
`FeatureId` (built on `IdTypeGenerator`), it is a plain value type with no
interning or back-reference machinery — equality is a straight string comparison
via `is_equal_to()`, exposed as free `operator==`/`operator!=`.

The default constructor generates a fresh ID via `GPlatesUtils::generate_unique_id()`;
the string constructor is for reconstructing a `RevisionId` from a value already
present in a file being parsed, and it does not validate its input. Revision ID
strings are meant to conform to the XML NCName production, so that they remain
usable as XML IDs, but as the constructor comment notes, that conformance is not
enforced by this class.

## Declared types

| Name | Kind | Bases | Template | Subclasses | Description |
|---|---|---|---|---|---|
| [`GPlatesModel::RevisionId`](#gplatesmodelrevisionid) | class | — | — | 0 | A revision ID acts as a persistent unique identifier for a single revision of a feature. |

## Members

### `GPlatesModel::RevisionId`

| Member | Kind | Type | Access | Description |
|---|---|---|---|---|
| `RevisionId()` | constructor | `None` | public | — |
| `RevisionId( const GPlatesUtils::UnicodeString &id)` | constructor | `None` | public | Construct a revision ID from a UnicodeString instance. |
| `is_equal_to( const RevisionId &other)` | method | `bool` | public | Determine whether another RevisionId instance contains the same revision ID as this instance. |
| `d_id` | field | `GPlatesUtils::UnicodeString` | private | — |

## Free functions and macros

| Name | Kind | Type / body | Description |
|---|---|---|---|
| `GPLATES_MODEL_REVISIONID_H` | macro | `None` | — |
| `operator==( const RevisionId &ri1, const RevisionId &ri2)` | operator | `bool` | — |
| `operator!=( const RevisionId &ri1, const RevisionId &ri2)` | operator | `bool` | — |

## Notes

*None.*

## Used by

| Unit | Component | References |
|---|---|---|
| [model/FeatureRevision](FeatureRevision.md) | model | 10 |
| [model/FeatureHandle](FeatureHandle.md) | model | 9 |
| [property-values/GpmlFeatureSnapshotReference](../property-values/GpmlFeatureSnapshotReference.md) | property-values | 5 |
| [property-values/GpmlRevisionId](../property-values/GpmlRevisionId.md) | property-values | 5 |
| [file-io/GpmlStructuralTypeReaderUtils](../file-io/GpmlStructuralTypeReaderUtils.md) | file-io | 4 |
| [file-io/GpmlFeatureReaderImpl](../file-io/GpmlFeatureReaderImpl.md) | file-io | 2 |
| [file-io/GpmlFormatMultiPointVectorFieldExport](../file-io/GpmlFormatMultiPointVectorFieldExport.md) | file-io | 1 |
| [file-io/GpmlPropertyStructuralTypeReaderUtils](../file-io/GpmlPropertyStructuralTypeReaderUtils.md) | file-io | 1 |

## Related

*None.*

## Explore

Run these from the `gplates-code` skill directory:

```bash
python scripts/gpq.py file src/model/RevisionId.h
python scripts/gpq.py def GPlatesModel::RevisionId --body
python scripts/gpq.py uses RevisionId --kind class
python scripts/gpq.py hier RevisionId
```
