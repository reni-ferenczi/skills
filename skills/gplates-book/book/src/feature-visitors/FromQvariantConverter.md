# FromQvariantConverter

[Book TOC](../../TOC.md) · [feature-visitors](../../components/feature-visitors.md) · cluster Community 580 · tier 2

| Source file | Kind | Lines |
|---|---|---|
| `src/feature-visitors/FromQvariantConverter.h` | C++ | 151 |
| `src/feature-visitors/FromQvariantConverter.cc` | C++ | 162 |

## Overview

`FromQvariantConverter` runs the `ToQvariantConverter` conversion in reverse: given a `QVariant` edited in a Qt view, it re-derives the `GPlatesModel::PropertyValue` that should replace an existing one. The caller hands it the target `QVariant` in the constructor, then calls `accept_visitor(this)` on the *existing* property value; whichever `visit_*` override fires tells the converter what concrete type to build, and `get_property_value()` returns the freshly constructed replacement. This double-dispatch is why the class cannot manufacture a property value out of nothing — it always needs an existing value of the right type to visit first. It backs edits made through `FeaturePropertyTableModel`.

Only a handful of property-value types are actually converted (`GmlTimeInstant`, `GpmlPlateId`, `XsBoolean`, `XsDouble`, `XsInteger`, `XsString`); `GpmlConstantValue` is transparently unwrapped by re-visiting its wrapped value.

## Declared types

| Name | Kind | Bases | Template | Subclasses | Description |
|---|---|---|---|---|---|
| [`GPlatesFeatureVisitors::FromQvariantConverter`](#gplatesfeaturevisitorsfromqvariantconverter) | class | [`GPlatesModel::ConstFeatureVisitor`](../model/FeatureVisitor.md) | — | 0 | The FromQvariantConverter feature-visitor is used to create a property value from a QVariant, if possible. |

## Members

### `GPlatesFeatureVisitors::FromQvariantConverter`

| Member | Kind | Type | Access | Description |
|---|---|---|---|---|
| `FromQvariantConverter( const QVariant &new_property_value)` | constructor | `None` | public | — |
| `~FromQvariantConverter()` | destructor | `None` | public | — |
| `get_property_value()` | method | `boost::optional<GPlatesModel::PropertyValue::non_null_ptr_type>` | public | Returns the PropertyValue that has been created from the given QVariant. |
| `visit_enumeration( const GPlatesPropertyValues::Enumeration &enumeration)` | method | `void` | protected | — |
| `visit_gml_time_instant( const GPlatesPropertyValues::GmlTimeInstant &gml_time_instant)` | method | `void` | protected | — |
| `visit_gpml_constant_value( const GPlatesPropertyValues::GpmlConstantValue &gpml_constant_value)` | method | `void` | protected | — |
| `visit_gpml_plate_id( const GPlatesPropertyValues::GpmlPlateId &gpml_plate_id)` | method | `void` | protected | — |
| `visit_gpml_old_plates_header( const GPlatesPropertyValues::GpmlOldPlatesHeader &gpml_old_plates_header)` | method | `void` | protected | — |
| `visit_xs_boolean( const GPlatesPropertyValues::XsBoolean &xs_boolean)` | method | `void` | protected | — |
| `visit_xs_double( const GPlatesPropertyValues::XsDouble &xs_double)` | method | `void` | protected | — |
| `visit_xs_integer( const GPlatesPropertyValues::XsInteger& xs_integer)` | method | `void` | protected | — |
| `visit_xs_string( const GPlatesPropertyValues::XsString &xs_string)` | method | `void` | protected | — |
| `set_return_value( GPlatesModel::PropertyValue::non_null_ptr_type new_value)` | method | `void` | private | — |
| `d_property_value` | field | `boost::optional<GPlatesModel::PropertyValue::non_null_ptr_type>` | private | The newly created PropertyValue. |
| `d_qvariant` | field | `QVariant` | private | The QVariant that we must convert into a PropertyValue. |

## Free functions and macros

| Name | Kind | Type / body | Description |
|---|---|---|---|
| `GPLATES_FEATUREVISITORS_FROMQVARIANTCONVERTER_H` | macro | `None` | — |

## Notes

`set_return_value()` only stores the first value it is offered; a second call is silently ignored. Combined with only the first `PropertyValue` of a multi-valued `TopLevelPropertyInline` being visited, this means the converter always yields at most one replacement. `visit_enumeration` and `visit_gpml_old_plates_header` are no-ops, so converting either of those types leaves `get_property_value()` at `boost::none` — always check the `boost::optional` before dereferencing it.

## Used by

| Unit | Component | References |
|---|---|---|
| [gui/FeaturePropertyTableModel](../gui/FeaturePropertyTableModel.md) | gui | 14 |

## Related

*None.*

## Explore

Run these from the `gplates-code` skill directory:

```bash
python scripts/gpq.py file src/feature-visitors/FromQvariantConverter.h
python scripts/gpq.py def GPlatesFeatureVisitors::FromQvariantConverter --body
python scripts/gpq.py uses FromQvariantConverter --kind class
python scripts/gpq.py hier FromQvariantConverter
```
