# PropertyExtractors

[Book TOC](../../TOC.md) · [app-logic](../../components/app-logic.md) · cluster Community 1343 · tier 2

| Source file | Kind | Lines |
|---|---|---|
| `src/app-logic/PropertyExtractors.h` | C++ | 158 |
| `src/app-logic/PropertyExtractors.cc` | C++ | 94 |

## Overview

`PropertyExtractors` is a small family of functors that pull one attribute — plate id, age, or feature type — out of either a `GPlatesAppLogic::ReconstructionGeometry` or a `GPlatesModel::FeatureHandle`, each returning `boost::optional<return_type>` so "the geometry has no such property" is representable without exceptions. They exist so colouring and draw-style code (`GenericColourScheme`, `ColourSchemeContainer`, `DrawStyleManager`) can be parameterised over *what* to extract without caring how: `PlateIdPropertyExtractor` defers to `ReconstructionGeometryUtils::get_plate_id`/`GPlatesUtils::get_recon_plate_id_as_int`, `AgePropertyExtractor` computes age as time-of-formation minus the current reconstruction time (via `ApplicationState`, mapping the distant past/future to positive/negative infinity), and `FeatureTypePropertyExtractor` reads the feature type directly or via the geometry's owning feature.

`PropertyExtractorAdapter<Adaptee, ReturnType>` wraps one of these extractors to `static_cast` its result to a different `ReturnType`, letting code that expects a specific extractor return type reuse an extractor built for another.

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

- `AgePropertyExtractor` returns `GPlatesMaths::Real::positive_infinity()`/`negative_infinity()` for features with a distant-past/distant-future time of formation, rather than `boost::none`; only a missing time of formation produces `boost::none`.
- `AgePropertyExtractor` stores a reference to the `ApplicationState` it was constructed with, so its age is always relative to whatever `get_current_reconstruction_time()` returns at call time, not at construction time.

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
