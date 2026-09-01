# TextContent

[Book TOC](../../TOC.md) · [property-values](../../components/property-values.md) · cluster Community 7 · tier 2

| Source file | Kind | Lines |
|---|---|---|
| `src/property-values/TextContent.h` | C++ | 55 |

## Overview

`TextContent` is a `GPlatesModel::StringContentTypeGenerator<TextContentFactory>` instantiation: an interned Unicode string used wherever a property value stores free-text content, most notably as the payload type behind `XsString`. `TextContentFactory` exists only to hand `StringContentTypeGenerator` the process-wide `GPlatesUtils::StringSet` it should intern into, via `GPlatesModel::StringSetSingletons::text_content_instance()`; its constructor is private, so the class is never instantiated and serves purely as a compile-time tag.

Because `StringContentTypeGenerator` stores a shared-string iterator rather than a copy of the text, every `TextContent` instance with the same characters shares one underlying string, and equality reduces to comparing iterators instead of strings.

## Declared types

| Name | Kind | Bases | Template | Subclasses | Description |
|---|---|---|---|---|---|
| [`GPlatesPropertyValues::TextContentFactory`](#gplatespropertyvaluestextcontentfactory) | class | — | — | 0 | — |
| [`GPlatesPropertyValues::TextContent`](#gplatespropertyvaluestextcontent) | typedef | — | — | 0 | — |

## Members

### `GPlatesPropertyValues::TextContentFactory`

| Member | Kind | Type | Access | Description |
|---|---|---|---|---|
| `TextContentFactory()` | constructor | `None` | private | — |

### `GPlatesPropertyValues::TextContent`

*None.*

## Free functions and macros

| Name | Kind | Type / body | Description |
|---|---|---|---|
| `GPLATES_PROPERTYVALUES_TEXTCONTENT_H` | macro | `None` | — |

## Notes

*None.*

## Used by

| Unit | Component | References |
|---|---|---|
| [app-logic/RasterLayerProxy](../app-logic/RasterLayerProxy.md) | app-logic | 19 |
| [property-values/ProxiedRasterCache](ProxiedRasterCache.md) | property-values | 11 |
| [property-values/GpmlOldPlatesHeader](GpmlOldPlatesHeader.md) | property-values | 7 |
| [property-values/GpmlStringList](GpmlStringList.md) | property-values | 6 |
| [app-logic/RasterLayerParams](../app-logic/RasterLayerParams.md) | app-logic | 5 |
| [app-logic/ScalarField3DLayerProxy](../app-logic/ScalarField3DLayerProxy.md) | app-logic | 5 |
| [property-values/XsString](XsString.md) | property-values | 5 |
| [app-logic/ExtractScalarField3DFeatureProperties](../app-logic/ExtractScalarField3DFeatureProperties.md) | app-logic | 4 |
| [feature-visitors/deprecated/XsStringFinder](../feature-visitors/deprecated/XsStringFinder.md) | feature-visitors | 4 |
| [qt-widgets/EditStringListWidget](../qt-widgets/EditStringListWidget.md) | qt-widgets | 4 |
| [gui/ExportRasterAnimationStrategy](../gui/ExportRasterAnimationStrategy.md) | gui | 3 |
| [presentation/TranscribeSession](../presentation/TranscribeSession.md) | presentation | 2 |
| [qt-widgets/EditStringWidget](../qt-widgets/EditStringWidget.md) | qt-widgets | 2 |
| [qt-widgets/RasterLayerOptionsWidget](../qt-widgets/RasterLayerOptionsWidget.md) | qt-widgets | 2 |
| [app-logic/ExtractRasterFeatureProperties](../app-logic/ExtractRasterFeatureProperties.md) | app-logic | 1 |
| [file-io/GpmlOutputVisitor](../file-io/GpmlOutputVisitor.md) | file-io | 1 |
| [file-io/GsmlPropertyHandlers](../file-io/GsmlPropertyHandlers.md) | file-io | 1 |
| [file-io/PlatesFormatUtils](../file-io/PlatesFormatUtils.md) | file-io | 1 |
| [view-operations/RenderedGeometryFactory](../view-operations/RenderedGeometryFactory.md) | view-operations | 1 |

## Related

*None.*

## Explore

Run these from the `gplates-code` skill directory:

```bash
python scripts/gpq.py file src/property-values/TextContent.h
python scripts/gpq.py def GPlatesPropertyValues::TextContentFactory --body
python scripts/gpq.py uses TextContentFactory --kind class
python scripts/gpq.py hier TextContentFactory
```
