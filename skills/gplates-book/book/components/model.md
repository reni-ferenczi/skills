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
| [BasicHandle](../src/model/BasicHandle.md) | 1 | 1269 | 8260 | Template base giving every model handle its revision, parent link, active flag and weak-ref notifications |
| [BasicRevision](../src/model/BasicRevision.md) | 2 | 495 | 56 | Shared child-collection bookkeeping template inherited by all Revision classes |
| [ChangesetHandle](../src/model/ChangesetHandle.md) | 2 | 218 | 62 | RAII grouping of model transactions into one user-undoable changeset |
| [FeatureCollectionHandle](../src/model/FeatureCollectionHandle.md) | 1 | 241 | 1062 | Middle handle level: the load/save/unload unit holding features, plus its untyped metadata tags map |
| [FeatureCollectionRevision](../src/model/FeatureCollectionRevision.md) | 3 | 162 | 0 | Immutable snapshot of a feature collection's contents at one point in time |
| [FeatureHandle](../src/model/FeatureHandle.md) | 1 | 568 | 1995 | Bottom handle level: feature type, feature ID and the revisioned list of top-level properties |
| [FeatureHandleWeakRefBackInserter](../src/model/FeatureHandleWeakRefBackInserter.md) | 3 | 149 | 6 | Output iterator adapter that converts strong feature handles to weak references |
| [FeatureId](../src/model/FeatureId.md) | 2 | 69 | 130 | Persistent interned string identifier features use to reference each other |
| [FeatureRevision](../src/model/FeatureRevision.md) | 3 | 289 | 3 | Immutable snapshot of a feature's properties at one point in time |
| [FeatureStoreRootHandle](../src/model/FeatureStoreRootHandle.md) | 2 | 166 | 14 | Persistent handle to the single root of the model's revisioned feature hierarchy |
| [FeatureStoreRootRevision](../src/model/FeatureStoreRootRevision.md) | 3 | 161 | 0 | Immutable snapshot of the root container of all loaded feature collections |
| [FeatureType](../src/model/FeatureType.md) | 1 | 55 | 600 | The interned qualified XML name identifying a feature's type, such as gpml:Isochron |
| [FeatureVisitor](../src/model/FeatureVisitor.md) | 1 | 961 | 5674 | The Visitor interface for walking features and property values, in const and non-const flavours |
| [Gpgim](../src/model/Gpgim.md) | 1 | 2617 | 144 | parses gpgim.xml at startup and answers every schema question about feature types and properties |
| [GpgimEnumerationType](../src/model/GpgimEnumerationType.md) | 2 | 128 | 84 | GPGIM structural type describing an enumeration's allowed values |
| [GpgimFeatureClass](../src/model/GpgimFeatureClass.md) | 2 | 459 | 190 | GPGIM feature-type node in the feature-class inheritance tree, with its properties |
| [GpgimInitialisationException](../src/model/GpgimInitialisationException.md) | 2 | 124 | 39 | Exception thrown when parsing the GPGIM XML file fails at startup |
| [GpgimProperty](../src/model/GpgimProperty.md) | 1 | 542 | 423 | one property definition from the GPGIM: name, allowed structural types, multiplicity, time-dependence |
| [GpgimStructuralType](../src/model/GpgimStructuralType.md) | 2 | 237 | 60 | Base description of a property's structural value type in the GPGIM |
| [GpgimTemplateStructuralType](../src/model/GpgimTemplateStructuralType.md) | 2 | 132 | 14 | GPGIM structural type that is a template instantiation with structural plus value type |
| [GpgimVersion](../src/model/GpgimVersion.md) | 2 | 399 | 18 | Parses, validates and orders the GPGIM's own MAJOR.MINOR.REVISION version number |
| [HandleTraits](../src/model/HandleTraits.md) | 1 | 310 | 275 | the model's containment tree expressed as typedefs, so BasicHandle can be written once for all handles |
| [IdTypeGenerator](../src/model/IdTypeGenerator.md) | 2 | 352 | 10 | Template producing interned, back-referenceable ID types like feature IDs |
| [Metadata](../src/model/Metadata.md) | 1 | 1170 | 369 | rotation-file metadata: per-pole name/content pairs plus the structured Dublin Core file header |
| [Model](../src/model/Model.md) | 2 | 309 | 39 | Concrete Model tier implementation owning the feature store root, hidden behind ModelInterface |
| [ModelInterface](../src/model/ModelInterface.md) | 2 | 147 | 87 | Cheaply-copyable p-impl handle that is the only public way to reach a Model |
| [ModelUtils](../src/model/ModelUtils.md) | 1 | 2099 | 348 | the GPGIM-checking layer for building and editing feature properties, including time-dependent wrappers |
| [NotificationGuard](../src/model/NotificationGuard.md) | 2 | 205 | 25 | RAII object that batches and merges a Model's pending change notifications |
| [PropertyName](../src/model/PropertyName.md) | 1 | 55 | 1187 | interned namespace-qualified name of a feature's top-level property, and the string pool behind it |
| [PropertyValue](../src/model/PropertyValue.md) | 1 | 352 | 886 | abstract base of every GPML/GML value: ref-counting, visitor dispatch, structural type, deep clone |
| [QualifiedXmlName](../src/model/QualifiedXmlName.md) | 1 | 461 | 2032 | interned namespace-qualified XML name shared by feature types, property names and structural types |
| [RevisionAwareIterator](../src/model/RevisionAwareIterator.md) | 1 | 518 | 183 | weak-ref plus index iterator over the children of any feature-store handle, never left on a stale revision |
| [RevisionId](../src/model/RevisionId.md) | 2 | 119 | 31 | Persistent string identifier for one revision of a feature |
| [StringContentTypeGenerator](../src/model/StringContentTypeGenerator.md) | 2 | 151 | 20 | Template behind interned text-content property values such as TextContent |
| [StringSetSingletons](../src/model/StringSetSingletons.md) | 2 | 266 | 60 | Process-wide interned StringSet/IdStringSet singletons behind the model's qualified-name types |
| [TopLevelProperty](../src/model/TopLevelProperty.md) | 2 | 291 | 91 | Abstract base class for a feature's top-level properties |
| [TopLevelPropertyInline](../src/model/TopLevelPropertyInline.md) | 1 | 482 | 255 | the only concrete top-level property: name, XML attributes and property values held inline |
| [TopLevelPropertyRef](../src/model/TopLevelPropertyRef.md) | 2 | 250 | 30 | Proxy returned when dereferencing a feature's property iterator, routing writes through undo/redo |
| [TranscribeQualifiedXmlName](../src/model/TranscribeQualifiedXmlName.md) | 3 | 110 | 0 | Serialization support for qualified XML names with namespace and local name |
| [TranscribeStringContentTypeGenerator](../src/model/TranscribeStringContentTypeGenerator.md) | 3 | 105 | 0 | Serialization support for string content using Scribe delegate protocol |
| [WeakObserver](../src/model/WeakObserver.md) | 1 | 551 | 2798 | intrusive doubly-linked back-pointer letting non-owning observers survive destruction of a model handle |
| [WeakObserverPublisher](../src/model/WeakObserverPublisher.md) | 2 | 362 | 11 | Publisher side of the observer pattern backing WeakReference/WeakObserver subscriptions |
| [WeakObserverVisitor](../src/model/WeakObserverVisitor.md) | 2 | 380 | 28 | Abstract Visitor interface dispatched over a publisher's weak observers |
| [WeakReference](../src/model/WeakReference.md) | 2 | 453 | 55 | Smart handle to a Model object that observes but does not keep it alive |
| [WeakReferenceCallback](../src/model/WeakReferenceCallback.md) | 1 | 270 | 145 | the model's change-notification interface: virtuals a WeakReference invokes when its handle changes |
| [WeakReferenceVisitors](../src/model/WeakReferenceVisitors.md) | 2 | 160 | 10 | WeakObserverVisitor implementations forwarding publisher lifecycle events to WeakReference callbacks |
| [XmlAttributeName](../src/model/XmlAttributeName.md) | 2 | 54 | 88 | Interned qualified name type for an XML attribute name |
| [XmlAttributeValue](../src/model/XmlAttributeValue.md) | 2 | 55 | 59 | Interned string type for XML attribute values, shared via a StringSet singleton |
| [XmlElementName](../src/model/XmlElementName.md) | 2 | 53 | 327 | Interned qualified name type for XML element names, shared via a StringSet singleton |
| [XmlNode](../src/model/XmlNode.md) | 1 | 734 | 719 | uninterpreted in-memory DOM built from a QXmlStreamReader so GPML subtrees can be revisited and re-emitted |
| [XmlNodeUtils](../src/model/XmlNodeUtils.md) | 2 | 480 | 69 | Visitors and helpers for pulling element names, text and qualified names out of an XML node tree |
| [types](../src/model/types.md) | 1 | 53 | 713 | include-cycle-free home of the plate-id and container-index typedefs shared across the whole tree |

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
