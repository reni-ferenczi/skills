# FeatureUtils

[Book TOC](../../TOC.md) · [utils](../../components/utils.md) · cluster Community 186 · tier 2

| Source file | Kind | Lines |
|---|---|---|
| `src/utils/FeatureUtils.h` | C++ | 115 |
| `src/utils/FeatureUtils.cc` | C++ | 295 |

## Overview

`FeatureUtils` is a grab bag of free functions for pulling a handful of
commonly needed values out of a `GPlatesModel::FeatureHandle` without the
caller having to write its own `ConstFeatureVisitor`. `get_recon_plate_id_as_int`,
`get_age`, `get_start_end_time` and `get_begin_time` all work the same way
internally: they walk the feature's top-level properties looking for a
`gpml:plateId`/`gml:TimePeriod` property, dispatching each one through the
file-private `PropertyFinder` visitor (declared in the `.cc`, not the header)
that records whichever of a plate ID, start time or end time it happens to
visit. `convert_property_name` and `get_shapefile_attribute` go the other
way, turning the `"gpml:name"`-style strings that come from shapefile
attribute mappings and similar text sources into a `GPlatesModel::PropertyName`
or a bare attribute name via a regular expression.

`get_age` and `get_begin_time` translate `GeoTimeInstant`'s distant-past and
distant-future sentinels into `GPlatesMaths::Real::positive_infinity()` and
`negative_infinity()` respectively, so callers get ordinary `Real` arithmetic
instead of having to special-case those sentinels themselves.

## Declared types

| Name | Kind | Bases | Template | Subclasses | Description |
|---|---|---|---|---|---|
| [`PropertyFinder`](#propertyfinder) | class | [`ConstFeatureVisitor`](../model/FeatureVisitor.md) | — | 0 | — |

## Members

### `PropertyFinder`

| Member | Kind | Type | Access | Description |
|---|---|---|---|---|
| `int_plate_id()` | method | `boost::optional<GPlatesModel::integer_plate_id_type>` | public | — |
| `start_time()` | method | `boost::optional<GPlatesPropertyValues::GeoTimeInstant>` | public | — |
| `end_time()` | method | `boost::optional<GPlatesPropertyValues::GeoTimeInstant>` | public | — |
| `visit_gpml_plate_id( ConstFeatureVisitor::gpml_plate_id_type& id)` | method | `void` | public | — |
| `visit_gpml_constant_value( ConstFeatureVisitor::gpml_constant_value_type &v)` | method | `void` | public | — |
| `visit_gml_time_period( ConstFeatureVisitor::gml_time_period_type &gml_time_period)` | method | `void` | public | — |
| `d_plate_id` | field | `boost::optional<GPlatesModel::integer_plate_id_type>` | private | — |
| `d_start_time` | field | `boost::optional<GPlatesPropertyValues::GeoTimeInstant>` | private | — |
| `d_end_time` | field | `boost::optional<GPlatesPropertyValues::GeoTimeInstant>` | private | — |

## Free functions and macros

| Name | Kind | Type / body | Description |
|---|---|---|---|
| `to_real(const GPlatesPropertyValues::GeoTimeInstant& time)` | function | `GPlatesMaths::Real` | — |
| `GPLATES_UTILS_FEATUREUTILS_H` | macro | `None` | — |
| `get_recon_plate_id_as_int( const GPlatesModel::FeatureHandle* feature_ptr)` | function | `boost::optional<GPlatesModel::integer_plate_id_type>` | — |
| `get_age( const GPlatesModel::FeatureHandle* feature_ptr, const GPlatesMaths::Real current_time)` | function | `boost::optional<GPlatesMaths::Real>` | — |
| `get_start_end_time( const GPlatesModel::FeatureHandle* feature_ptr)` | function | `boost::tuple< GPlatesMaths::Real, GPlatesMaths::Real>` | — |
| `get_begin_time( const GPlatesModel::FeatureHandle* feature_ptr)` | function | `boost::optional<GPlatesMaths::Real>` | — |
| `convert_property_name( const QString&)` | function | `boost::optional<GPlatesModel::PropertyName>` | — |
| `get_shapefile_attribute( const QString& name)` | function | `boost::optional<QString>` | — |
| `property_value_to_qstring( const GPlatesModel::PropertyValue& data)` | function | `QString` | — |

## Notes

Only `get_recon_plate_id_as_int` null-checks its `feature_ptr` argument;
`get_age`, `get_start_end_time` and `get_begin_time` dereference it directly
and will crash on a null feature handle.

## Used by

| Unit | Component | References |
|---|---|---|
| [utils/GetPropertyAsPythonObjVisitor](GetPropertyAsPythonObjVisitor.md) | utils | 28 |
| [api/PyFeature](../api/PyFeature.md) | api | 11 |
| [app-logic/CoRegistrationLayerProxy](../app-logic/CoRegistrationLayerProxy.md) | app-logic | 4 |
| [app-logic/PropertyExtractors](../app-logic/PropertyExtractors.md) | app-logic | 4 |
| [gui/GenericColourScheme](../gui/GenericColourScheme.md) | gui | 4 |
| [gui/CommandServer](../gui/CommandServer.md) | gui | 2 |
| [qt-widgets/KinematicGraphsDialog](../qt-widgets/KinematicGraphsDialog.md) | qt-widgets | 2 |
| [api/PyViewportWindow](../api/PyViewportWindow.md) | api | 1 |
| [gui/FeatureFocus](../gui/FeatureFocus.md) | gui | 1 |

## Related

*None.*

## Explore

Run these from the `gplates-code` skill directory:

```bash
python scripts/gpq.py file src/utils/FeatureUtils.h
python scripts/gpq.py def PropertyFinder --body
python scripts/gpq.py uses PropertyFinder --kind class
python scripts/gpq.py hier PropertyFinder
```
