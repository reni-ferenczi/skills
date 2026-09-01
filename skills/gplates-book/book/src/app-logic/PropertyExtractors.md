# PropertyExtractors

[Book TOC](../../TOC.md) · [app-logic](../../components/app-logic.md) · cluster Community 1343 · tier 2

| Source file | Kind | Lines |
|---|---|---|
| `src/app-logic/PropertyExtractors.h` | C++ | 158 |
| `src/app-logic/PropertyExtractors.cc` | C++ | 94 |

## Overview

[[[PROSE overview unit=app-logic/PropertyExtractors tier=2]]]
Replace this whole block, markers included, with 1-3 paragraphs: what this unit is, why it exists, and how it fits the surrounding design. Do not restate the tables below.
[[[/PROSE]]]

## Declared types

| Name | Kind | Bases | Template | Subclasses | Description |
|---|---|---|---|---|---|
| [`GPlatesAppLogic::PropertyExtractorAdapter`](#gplatesapplogicpropertyextractoradapter) | class | — | `<typename Adaptee, typename ReturnType>` | 0 | — |
| [`GPlatesAppLogic::PlateIdPropertyExtractor`](#gplatesapplogicplateidpropertyextractor) | class | — | — | 0 | Extracts the plate ID for use by GenericColourScheme. |
| [`GPlatesAppLogic::AgePropertyExtractor`](#gplatesapplogicagepropertyextractor) | class | — | — | 0 | Extracts the age for use by GenericColourScheme. |
| [`GPlatesAppLogic::FeatureTypePropertyExtractor`](#gplatesapplogicfeaturetypepropertyextractor) | class | — | — | 0 | Extracts the feature type for use by GenericColourScheme. |

## Members

### `GPlatesAppLogic::PropertyExtractorAdapter`

| Member | Kind | Type | Access | Description |
|---|---|---|---|---|
| `return_type` | typedef | `ReturnType` | public | — |
| `PropertyExtractorAdapter( const Adaptee &adaptee = Adaptee())` | constructor | `None` | public | — |
| `operator()(const ArguType& argu)` | operator | `boost::optional<return_type>` | public | — |
| `d_adaptee` | field | `Adaptee` | private | — |

### `GPlatesAppLogic::PlateIdPropertyExtractor`

| Member | Kind | Type | Access | Description |
|---|---|---|---|---|
| `return_type` | typedef | `GPlatesModel::integer_plate_id_type` | public | — |
| `operator()( const GPlatesAppLogic::ReconstructionGeometry &reconstruction_geometry)` | operator | `boost::optional<return_type>` | public | — |
| `operator()( const GPlatesModel::FeatureHandle& feature)` | operator | `boost::optional<return_type>` | public | — |

### `GPlatesAppLogic::AgePropertyExtractor`

| Member | Kind | Type | Access | Description |
|---|---|---|---|---|
| `return_type` | typedef | `GPlatesMaths::Real` | public | — |
| `AgePropertyExtractor( ApplicationState &application_state)` | constructor | `None` | public | — |
| `operator()( const GPlatesAppLogic::ReconstructionGeometry &reconstruction_geometry)` | operator | `boost::optional<return_type>` | public | — |
| `operator()( const GPlatesModel::FeatureHandle& feature)` | operator | `boost::optional<return_type>` | public | — |
| `d_application_state` | field | `ApplicationState` | private | — |

### `GPlatesAppLogic::FeatureTypePropertyExtractor`

| Member | Kind | Type | Access | Description |
|---|---|---|---|---|
| `return_type` | typedef | `GPlatesModel::FeatureType` | public | — |
| `operator()( const GPlatesAppLogic::ReconstructionGeometry &reconstruction_geometry)` | operator | `boost::optional<return_type>` | public | — |
| `operator()( const GPlatesModel::FeatureHandle& feature)` | operator | `boost::optional<return_type>` | public | — |

## Free functions and macros

| Name | Kind | Type / body | Description |
|---|---|---|---|
| `operator()( const GPlatesAppLogic::ReconstructionGeometry &reconstruction_geometry)` | operator | `boost::optional<GPlatesAppLogic::PlateIdPropertyExtractor::return_type>` | — |
| `operator()( const GPlatesModel::FeatureHandle& feature)` | operator | `boost::optional<GPlatesAppLogic::PlateIdPropertyExtractor::return_type>` | — |
| `operator()( const GPlatesAppLogic::ReconstructionGeometry &reconstruction_geometry)` | operator | `boost::optional<GPlatesAppLogic::AgePropertyExtractor::return_type>` | — |
| `operator()( const GPlatesAppLogic::ReconstructionGeometry &reconstruction_geometry)` | operator | `boost::optional<GPlatesAppLogic::FeatureTypePropertyExtractor::return_type>` | — |
| `GPLATES_APP_LOGIC_PROPERTYEXTRACTORS_H` | macro | `None` | — |

## Notes

[[[PROSE notes unit=app-logic/PropertyExtractors tier=2]]]
Replace this whole block, markers included, with invariants, ownership, threading or gotchas that are not visible in the tables. Write *None.* if there is nothing worth saying.
[[[/PROSE]]]

## Used by

| Unit | Component | References |
|---|---|---|
| [gui/ColourSchemeContainer](../gui/ColourSchemeContainer.md) | gui | 6 |
| [qt-widgets/ColouringDialog](../qt-widgets/ColouringDialog.md) | qt-widgets | 5 |
| [presentation/ReconstructionGeometryRenderer](../presentation/ReconstructionGeometryRenderer.md) | presentation | 4 |
| [gui/DrawStyleManager](../gui/DrawStyleManager.md) | gui | 3 |
| [qt-widgets/DrawStyleDialog](../qt-widgets/DrawStyleDialog.md) | qt-widgets | 1 |

## Related

*None.*

## Explore

Run these from the `gplates-code` skill directory:

```bash
python scripts/gpq.py file src/app-logic/PropertyExtractors.h
python scripts/gpq.py def GPlatesAppLogic::PropertyExtractorAdapter --body
python scripts/gpq.py uses PropertyExtractorAdapter --kind class
python scripts/gpq.py hier PropertyExtractorAdapter
```
