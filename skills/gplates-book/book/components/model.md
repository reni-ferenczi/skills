# model

[Book TOC](../TOC.md)

53 unit page(s), 81 source file(s) documented here, 1 further file(s) listed below.

## Overview

[[[PROSE component unit=component:model tier=1]]]
Replace this whole block, markers included, with 2-4 paragraphs: what this component is responsible for, the load-bearing units and how it connects to neighbouring components. Do not restate the unit table.
[[[/PROSE]]]

## Units

### `src/model`

| Unit | Tier | Lines | Fan-in | Description |
|---|---|---|---|---|
| [BasicHandle](../src/model/BasicHandle.md) | 1 | 1269 | 8260 | (pending) |
| [BasicRevision](../src/model/BasicRevision.md) | 2 | 495 | 56 | (pending) |
| [ChangesetHandle](../src/model/ChangesetHandle.md) | 2 | 218 | 62 | (pending) |
| [FeatureCollectionHandle](../src/model/FeatureCollectionHandle.md) | 1 | 241 | 1062 | (pending) |
| [FeatureCollectionRevision](../src/model/FeatureCollectionRevision.md) | 3 | 162 | 0 | Immutable snapshot of a feature collection's contents at one point in time |
| [FeatureHandle](../src/model/FeatureHandle.md) | 1 | 568 | 1995 | (pending) |
| [FeatureHandleWeakRefBackInserter](../src/model/FeatureHandleWeakRefBackInserter.md) | 3 | 149 | 6 | Output iterator adapter that converts strong feature handles to weak references |
| [FeatureId](../src/model/FeatureId.md) | 2 | 69 | 130 | (pending) |
| [FeatureRevision](../src/model/FeatureRevision.md) | 3 | 289 | 3 | Immutable snapshot of a feature's properties at one point in time |
| [FeatureStoreRootHandle](../src/model/FeatureStoreRootHandle.md) | 2 | 166 | 14 | (pending) |
| [FeatureStoreRootRevision](../src/model/FeatureStoreRootRevision.md) | 3 | 161 | 0 | Immutable snapshot of the root container of all loaded feature collections |
| [FeatureType](../src/model/FeatureType.md) | 1 | 55 | 600 | (pending) |
| [FeatureVisitor](../src/model/FeatureVisitor.md) | 1 | 961 | 5674 | (pending) |
| [Gpgim](../src/model/Gpgim.md) | 1 | 2617 | 144 | (pending) |
| [GpgimEnumerationType](../src/model/GpgimEnumerationType.md) | 2 | 128 | 84 | (pending) |
| [GpgimFeatureClass](../src/model/GpgimFeatureClass.md) | 2 | 459 | 190 | (pending) |
| [GpgimInitialisationException](../src/model/GpgimInitialisationException.md) | 2 | 124 | 39 | (pending) |
| [GpgimProperty](../src/model/GpgimProperty.md) | 1 | 542 | 423 | (pending) |
| [GpgimStructuralType](../src/model/GpgimStructuralType.md) | 2 | 237 | 60 | (pending) |
| [GpgimTemplateStructuralType](../src/model/GpgimTemplateStructuralType.md) | 2 | 132 | 14 | (pending) |
| [GpgimVersion](../src/model/GpgimVersion.md) | 2 | 399 | 18 | (pending) |
| [HandleTraits](../src/model/HandleTraits.md) | 1 | 310 | 275 | (pending) |
| [IdTypeGenerator](../src/model/IdTypeGenerator.md) | 2 | 352 | 10 | (pending) |
| [Metadata](../src/model/Metadata.md) | 1 | 1170 | 369 | (pending) |
| [Model](../src/model/Model.md) | 2 | 309 | 39 | (pending) |
| [ModelInterface](../src/model/ModelInterface.md) | 2 | 147 | 87 | (pending) |
| [ModelUtils](../src/model/ModelUtils.md) | 1 | 2099 | 348 | (pending) |
| [NotificationGuard](../src/model/NotificationGuard.md) | 2 | 205 | 25 | (pending) |
| [PropertyName](../src/model/PropertyName.md) | 1 | 55 | 1187 | (pending) |
| [PropertyValue](../src/model/PropertyValue.md) | 1 | 352 | 886 | (pending) |
| [QualifiedXmlName](../src/model/QualifiedXmlName.md) | 1 | 461 | 2032 | (pending) |
| [RevisionAwareIterator](../src/model/RevisionAwareIterator.md) | 1 | 518 | 183 | (pending) |
| [RevisionId](../src/model/RevisionId.md) | 2 | 119 | 31 | (pending) |
| [StringContentTypeGenerator](../src/model/StringContentTypeGenerator.md) | 2 | 151 | 20 | (pending) |
| [StringSetSingletons](../src/model/StringSetSingletons.md) | 2 | 266 | 60 | (pending) |
| [TopLevelProperty](../src/model/TopLevelProperty.md) | 2 | 291 | 91 | (pending) |
| [TopLevelPropertyInline](../src/model/TopLevelPropertyInline.md) | 1 | 482 | 255 | (pending) |
| [TopLevelPropertyRef](../src/model/TopLevelPropertyRef.md) | 2 | 250 | 30 | (pending) |
| [TranscribeQualifiedXmlName](../src/model/TranscribeQualifiedXmlName.md) | 3 | 110 | 0 | Serialization support for qualified XML names with namespace and local name |
| [TranscribeStringContentTypeGenerator](../src/model/TranscribeStringContentTypeGenerator.md) | 3 | 105 | 0 | Serialization support for string content using Scribe delegate protocol |
| [WeakObserver](../src/model/WeakObserver.md) | 1 | 551 | 2798 | (pending) |
| [WeakObserverPublisher](../src/model/WeakObserverPublisher.md) | 2 | 362 | 11 | (pending) |
| [WeakObserverVisitor](../src/model/WeakObserverVisitor.md) | 2 | 380 | 28 | (pending) |
| [WeakReference](../src/model/WeakReference.md) | 2 | 453 | 55 | (pending) |
| [WeakReferenceCallback](../src/model/WeakReferenceCallback.md) | 1 | 270 | 145 | (pending) |
| [WeakReferenceVisitors](../src/model/WeakReferenceVisitors.md) | 2 | 160 | 10 | (pending) |
| [XmlAttributeName](../src/model/XmlAttributeName.md) | 2 | 54 | 88 | (pending) |
| [XmlAttributeValue](../src/model/XmlAttributeValue.md) | 2 | 55 | 59 | (pending) |
| [XmlElementName](../src/model/XmlElementName.md) | 2 | 53 | 327 | (pending) |
| [XmlNode](../src/model/XmlNode.md) | 1 | 734 | 719 | (pending) |
| [XmlNodeUtils](../src/model/XmlNodeUtils.md) | 2 | 480 | 69 | (pending) |
| [types](../src/model/types.md) | 1 | 53 | 713 | (pending) |

### `src/model/deprecated`

| Unit | Tier | Lines | Fan-in | Description |
|---|---|---|---|---|
| [PythonWrapper](../src/model/deprecated/PythonWrapper.md) | 3 | 35 | 0 | Deprecated legacy Boost.Python module wrapper for the \_model module |


## Other files

| File | Kind | Lines |
|---|---|---|
| `src/model/CMakeLists.txt` | build | 95 |

## Depends on

| Component | References |
|---|---|
| [utils](utils.md) | 715 |
| [global](global.md) | 283 |
| [property-values](property-values.md) | 193 |
| [file-io](file-io.md) | 123 |
| [scribe](scribe.md) | 103 |
| [maths](maths.md) | 84 |
| [app-logic](app-logic.md) | 22 |
| [gui](gui.md) | 13 |
| [qt-widgets](qt-widgets.md) | 7 |
| [system-fixes](system-fixes.md) | 1 |

## Used by

| Component | References |
|---|---|
| [file-io](file-io.md) | 9531 |
| [app-logic](app-logic.md) | 7608 |
| [qt-widgets](qt-widgets.md) | 5269 |
| [property-values](property-values.md) | 1603 |
| [gui](gui.md) | 1265 |
| [feature-visitors](feature-visitors.md) | 1168 |
| [view-operations](view-operations.md) | 389 |
| [data-mining](data-mining.md) | 372 |
| [unit-test](unit-test.md) | 201 |
| [opengl](opengl.md) | 195 |
| [utils](utils.md) | 194 |
| [cli](cli.md) | 164 |
| [entry-points](entry-points.md) | 148 |
| [api](api.md) | 147 |
| [presentation](presentation.md) | 92 |
| [canvas-tools](canvas-tools.md) | 49 |
| [deprecated](deprecated.md) | 1 |
| [maths](maths.md) | 1 |

## Explore

Run these from the `gplates-code` skill directory:

```bash
python scripts/gpq.py tree src/model
python scripts/gpq.py sym . --mode sub --path src/model --defs-only
```
