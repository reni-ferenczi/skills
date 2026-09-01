# XmlElementName

[Book TOC](../../TOC.md) · [model](../../components/model.md) · cluster Community 138 · tier 2

| Source file | Kind | Lines |
|---|---|---|
| `src/model/XmlElementName.h` | C++ | 53 |

## Overview

[[[PROSE overview unit=model/XmlElementName tier=2]]]
Replace this whole block, markers included, with 1-3 paragraphs: what this unit is, why it exists, and how it fits the surrounding design. Do not restate the tables below.
[[[/PROSE]]]

## Declared types

| Name | Kind | Bases | Template | Subclasses | Description |
|---|---|---|---|---|---|
| [`GPlatesModel::XmlElementNameFactory`](#gplatesmodelxmlelementnamefactory) | class | — | — | 0 | — |
| [`GPlatesModel::XmlElementName`](#gplatesmodelxmlelementname) | typedef | — | — | 0 | — |

## Members

### `GPlatesModel::XmlElementNameFactory`

| Member | Kind | Type | Access | Description |
|---|---|---|---|---|
| `XmlElementNameFactory()` | constructor | `None` | private | — |

### `GPlatesModel::XmlElementName`

*None.*

## Free functions and macros

| Name | Kind | Type / body | Description |
|---|---|---|---|
| `GPLATES_MODEL_XMLELEMENTNAME_H` | macro | `None` | — |

## Notes

[[[PROSE notes unit=model/XmlElementName tier=2]]]
Replace this whole block, markers included, with invariants, ownership, threading or gotchas that are not visible in the tables. Write *None.* if there is nothing worth saying.
[[[/PROSE]]]

## Used by

| Unit | Component | References |
|---|---|---|
| [file-io/GpmlPropertyStructuralTypeReaderUtils](../file-io/GpmlPropertyStructuralTypeReaderUtils.md) | file-io | 129 |
| [file-io/GpmlStructuralTypeReaderUtils](../file-io/GpmlStructuralTypeReaderUtils.md) | file-io | 87 |
| [model/Gpgim](Gpgim.md) | model | 74 |
| [file-io/GpmlPropertyReader](../file-io/GpmlPropertyReader.md) | file-io | 15 |
| [model/XmlNode](XmlNode.md) | model | 12 |
| [file-io/GpmlFeatureReaderImpl](../file-io/GpmlFeatureReaderImpl.md) | file-io | 6 |
| [file-io/GpmlReader](../file-io/GpmlReader.md) | file-io | 4 |
| [model/XmlNodeUtils](XmlNodeUtils.md) | model | 4 |
| [file-io/GpmlUpgradeReaderUtils](../file-io/GpmlUpgradeReaderUtils.md) | file-io | 3 |
| [model/Metadata](Metadata.md) | model | 2 |

## Related

*None.*

## Explore

Run these from the `gplates-code` skill directory:

```bash
python scripts/gpq.py file src/model/XmlElementName.h
python scripts/gpq.py def GPlatesModel::XmlElementNameFactory --body
python scripts/gpq.py uses XmlElementNameFactory --kind class
python scripts/gpq.py hier XmlElementNameFactory
```
