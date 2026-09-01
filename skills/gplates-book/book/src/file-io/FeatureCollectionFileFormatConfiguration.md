# FeatureCollectionFileFormatConfiguration

[Book TOC](../../TOC.md) · [file-io](../../components/file-io.md) · cluster Community 12 · tier 2

| Source file | Kind | Lines |
|---|---|---|
| `src/file-io/FeatureCollectionFileFormatConfiguration.h` | C++ | 167 |

## Overview

[[[PROSE overview unit=file-io/FeatureCollectionFileFormatConfiguration tier=2]]]
Replace this whole block, markers included, with 1-3 paragraphs: what this unit is, why it exists, and how it fits the surrounding design. Do not restate the tables below.
[[[/PROSE]]]

## Declared types

| Name | Kind | Bases | Template | Subclasses | Description |
|---|---|---|---|---|---|
| [`GPlatesFileIO::FeatureCollectionFileFormat::Configuration`](#gplatesfileiofeaturecollectionfileformatconfiguration) | class | — | — | 3 | Base class for specifying configuration options (such as for reading and/or writing a feature collection from/to a file). |

## Members

### `GPlatesFileIO::FeatureCollectionFileFormat::Configuration`

| Member | Kind | Type | Access | Description |
|---|---|---|---|---|
| `shared_ptr_to_const_type` | typedef | `boost::shared_ptr<const Configuration>` | public | Typedef for a shared pointer to const Configuration. |
| `shared_ptr_type` | typedef | `boost::shared_ptr<Configuration>` | public | Typedef for a shared pointer to Configuration. |
| `~Configuration()` | destructor | `None` | public | — |

## Free functions and macros

| Name | Kind | Type / body | Description |
|---|---|---|---|
| `GPLATES_FILE_IO_FEATURECOLLECTIONFILEFORMATCONFIGURATION_H` | macro | `None` | — |
| `dynamic_cast_configuration( const boost::shared_ptr<typename GPlatesUtils::CopyConst<ConfigurationDerivedType, Configuration>::type> &configuration)` | function | `boost::optional<boost::shared_ptr<ConfigurationDerivedType> >` | A convenience function to dynamic cast a shared pointer to a Configuration into a shared pointer to a derived type 'ConfigurationDerivedType'. |
| `dynamic_cast_configuration( const boost::optional<boost::shared_ptr< typename GPlatesUtils::CopyConst<ConfigurationDerivedType, Configuration>::type> > &configuration)` | function | `boost::optional<boost::shared_ptr<ConfigurationDerivedType> >` | Similar to the other overload of dynamic\_cast\_configuration but accepts a boost::optional. |
| `copy_cast_configuration( const Configuration::shared_ptr_to_const_type &configuration)` | function | `boost::optional<boost::shared_ptr<ConfigurationDerivedType> >` | A convenience function to dynamic cast a shared pointer to a Configuration into a shared pointer to a derived type 'ConfigurationDerivedType' and then return a \*copy\* of that (using the copy constructor of 'DerivedConfiguration'). |
| `copy_cast_configuration( const boost::optional<Configuration::shared_ptr_to_const_type> &configuration)` | function | `boost::optional<boost::shared_ptr<ConfigurationDerivedType> >` | Similar to the other overload of copy\_cast\_configuration but accepts a boost::optional. |

## Notes

[[[PROSE notes unit=file-io/FeatureCollectionFileFormatConfiguration tier=2]]]
Replace this whole block, markers included, with invariants, ownership, threading or gotchas that are not visible in the tables. Write *None.* if there is nothing worth saying.
[[[/PROSE]]]

## Used by

| Unit | Component | References |
|---|---|---|
| [gui/ExportAnimationRegistry](../gui/ExportAnimationRegistry.md) | gui | 88 |
| [file-io/FeatureCollectionFileFormatRegistry](FeatureCollectionFileFormatRegistry.md) | file-io | 37 |
| [file-io/File](File.md) | file-io | 35 |
| [qt-widgets/ManageFeatureCollectionsEditConfigurations](../qt-widgets/ManageFeatureCollectionsEditConfigurations.md) | qt-widgets | 25 |
| [file-io/FeatureCollectionFileFormatConfigurations](FeatureCollectionFileFormatConfigurations.md) | file-io | 13 |
| [qt-widgets/ExportVelocityOptionsWidget](../qt-widgets/ExportVelocityOptionsWidget.md) | qt-widgets | 13 |
| [gui/ExportRasterAnimationStrategy](../gui/ExportRasterAnimationStrategy.md) | gui | 9 |
| [gui/ExportStageRotationAnimationStrategy](../gui/ExportStageRotationAnimationStrategy.md) | gui | 9 |
| [gui/ExportTotalRotationAnimationStrategy](../gui/ExportTotalRotationAnimationStrategy.md) | gui | 9 |
| [file-io/OgrFeatureCollectionWriter](OgrFeatureCollectionWriter.md) | file-io | 7 |
| [file-io/OgrReader](OgrReader.md) | file-io | 7 |
| [file-io/PlatesRotationFileProxy](PlatesRotationFileProxy.md) | file-io | 7 |
| [gui/FileIOFeedback](../gui/FileIOFeedback.md) | gui | 7 |
| [app-logic/FeatureCollectionFileState](../app-logic/FeatureCollectionFileState.md) | app-logic | 6 |
| [gui/ExportNetRotationAnimationStrategy](../gui/ExportNetRotationAnimationStrategy.md) | gui | 6 |
| [file-io/GMTFormatWriter](GMTFormatWriter.md) | file-io | 5 |
| [gui/ExportVelocityAnimationStrategy](../gui/ExportVelocityAnimationStrategy.md) | gui | 4 |
| [qt-widgets/ManageFeatureCollectionsDialog](../qt-widgets/ManageFeatureCollectionsDialog.md) | qt-widgets | 4 |
| [presentation/TranscribeSession](../presentation/TranscribeSession.md) | presentation | 3 |
| [qt-widgets/GMTFileFormatConfigurationDialog](../qt-widgets/GMTFileFormatConfigurationDialog.md) | qt-widgets | 3 |

*... and 15 more units.*

## Related

*None.*

## Explore

Run these from the `gplates-code` skill directory:

```bash
python scripts/gpq.py file src/file-io/FeatureCollectionFileFormatConfiguration.h
python scripts/gpq.py def GPlatesFileIO::FeatureCollectionFileFormat::Configuration --body
python scripts/gpq.py uses Configuration --kind class
python scripts/gpq.py hier Configuration
```
