# GmlTimePeriod

[Book TOC](../../TOC.md) · [property-values](../../components/property-values.md) · cluster Community 783 · tier 2

| Source file | Kind | Lines |
|---|---|---|
| `src/property-values/GmlTimePeriod.h` | C++ | 319 |
| `src/property-values/GmlTimePeriod.cc` | C++ | 127 |

## Overview

`GmlTimePeriod` is the `GPlatesModel::PropertyValue` for `gml:TimePeriod`: a
pair of `GmlTimeInstant` bounds, `d_begin` (the older, less recent time) and
`d_end` (the more recent time), used throughout the model to express a
feature's `gml:validTime` or a reconstructable geometry's temporal validity.
`contains()` tests whether a `GeoTimeInstant` (or a raw `double`, via the
overload that wraps it in one) falls within `[begin, end]` inclusive of both
endpoints.

The class documents an invariant — begin must not be later than end — but
does not enforce it unconditionally: `create()`, `set_begin()` and
`set_end()` all take a `check_begin_end_times` flag that defaults to `false`,
because, as the header explains, real files in the wild violate this
ordering. Only when a caller opts in does a violation raise
`BeginTimeLaterThanEndTimeException` (a `GPlatesGlobal::PreconditionViolationError`).

## Declared types

| Name | Kind | Bases | Template | Subclasses | Description |
|---|---|---|---|---|---|
| [`GPlatesPropertyValues::GmlTimePeriod`](#gplatespropertyvaluesgmltimeperiod) | class | [`GPlatesModel::PropertyValue`](../model/PropertyValue.md) | — | 0 | This class implements the PropertyValue which corresponds to "gml:TimePeriod". |

## Members

### `GPlatesPropertyValues::GmlTimePeriod`

| Member | Kind | Type | Access | Description |
|---|---|---|---|---|
| `non_null_ptr_type` | typedef | `GPlatesUtils::non_null_intrusive_ptr<GmlTimePeriod>` | public | A convenience typedef for GPlatesUtils::non\_null\_intrusive\_ptr\<GmlTimePeriod\>. |
| `non_null_ptr_to_const_type` | typedef | `GPlatesUtils::non_null_intrusive_ptr<const GmlTimePeriod>` | public | A convenience typedef for GPlatesUtils::non\_null\_intrusive\_ptr\<const GmlTimePeriod\>. |
| `BeginTimeLaterThanEndTimeException` | class | `None` | public | A time period's begin time should be earlier than its end time. |
| `~GmlTimePeriod()` | destructor | `None` | public | — |
| `create( GmlTimeInstant::non_null_ptr_type begin_, GmlTimeInstant::non_null_ptr_type end_, bool check_begin_end_times = false)` | method | `non_null_ptr_type` | public | Create a GmlTimePeriod instance which begins at begin\_ and ends at end\_. |
| `clone()` | method | `non_null_ptr_type` | public | — |
| `deep_clone()` | method | `GmlTimePeriod::non_null_ptr_type` | public | — |
| `DEFINE_FUNCTION_DEEP_CLONE_AS_PROP_VAL()` | method | `None` | public | — |
| `begin()` | method | `GmlTimeInstant::non_null_ptr_to_const_type` | public | Return the 'const' "begin" attribute of this GmlTimePeriod instance. |
| `set_begin( GmlTimeInstant::non_null_ptr_type begin_, bool check_begin_end_times = false)` | method | `void` | public | Set the "begin" attribute of this GmlTimePeriod instance. |
| `end()` | method | `GmlTimeInstant::non_null_ptr_to_const_type` | public | Return the "end" attribute of this GmlTimePeriod instance. |
| `set_end( GmlTimeInstant::non_null_ptr_type end_, bool check_begin_end_times = false)` | method | `void` | public | Set the "end" attribute of this GmlTimePeriod instance. |
| `contains( const GeoTimeInstant &geo_time)` | method | `bool` | public | Determine whether geo\_time lies within the temporal span of this GmlTimePeriod instance. |
| `contains( const double &geo_time)` | method | `bool` | public | Determine whether geo\_time lies within the temporal span of this GmlTimePeriod instance. |
| `get_structural_type()` | method | `StructuralType` | public | Returns the structural type associated with this property value class. |
| `accept_visitor( GPlatesModel::ConstFeatureVisitor &visitor)` | method | `void` | public | Accept a ConstFeatureVisitor instance. |
| `accept_visitor( GPlatesModel::FeatureVisitor &visitor)` | method | `void` | public | Accept a FeatureVisitor instance. |
| `print_to` | field | `std::ostream` | public | — |
| `GmlTimePeriod( GmlTimeInstant::non_null_ptr_type begin_, GmlTimeInstant::non_null_ptr_type end_)` | constructor | `None` | protected | This constructor should not be public, because we don't want to allow instantiation of this type on the stack. |
| `GmlTimePeriod( const GmlTimePeriod &other)` | constructor | `None` | protected | This constructor should not be public, because we don't want to allow instantiation of this type on the stack. |
| `directly_modifiable_fields_equal( const PropertyValue &other)` | method | `bool` | protected | — |
| `d_begin` | field | `GmlTimeInstant::non_null_ptr_type` | private | — |
| `d_end` | field | `GmlTimeInstant::non_null_ptr_type` | private | — |
| `operator=` | field | `GmlTimePeriod` | private | This operator should never be defined, because we don't want/need to allow copy-assignment: All copying should use the virtual copy-constructor 'clone' (which will in turn use the copy-constructor); all "assignment" should really only be ... |

## Free functions and macros

| Name | Kind | Type / body | Description |
|---|---|---|---|
| `GPLATES_PROPERTYVALUES_GMLTIMEPERIOD_H` | macro | `None` | — |

## Notes

- Because `check_begin_end_times` defaults to `false` everywhere, a
  `GmlTimePeriod` can legitimately exist with begin later than end; code that
  relies on the ordering (such as `contains()`) will simply behave oddly
  rather than fail loudly unless the caller passed `true`.
- `begin()` and `end()` each have a non-`const` overload returning
  `GmlTimeInstant::non_null_ptr_type`, so a caller can mutate the pointed-to
  `GmlTimeInstant` directly (e.g. via its own `set_time_position()`) without
  going through `GmlTimePeriod::set_begin()`/`set_end()` — that path bypasses
  the begin/end ordering check entirely, even when the caller would otherwise
  want it.
- `deep_clone()` recursively deep-clones both `d_begin` and `d_end`, unlike
  the plain `clone()` used internally, which only copies the intrusive
  pointers.

## Used by

| Unit | Component | References |
|---|---|---|
| [feature-visitors/deprecated/GmlTimePeriodFinder](../feature-visitors/deprecated/GmlTimePeriodFinder.md) | feature-visitors | 8 |
| [app-logic/PartitionFeatureUtils](../app-logic/PartitionFeatureUtils.md) | app-logic | 4 |
| [file-io/GpmlPropertyStructuralTypeReaderUtils](../file-io/GpmlPropertyStructuralTypeReaderUtils.md) | file-io | 4 |
| [file-io/OgrReader](../file-io/OgrReader.md) | file-io | 4 |
| [qt-widgets/EditTimePeriodWidget](../qt-widgets/EditTimePeriodWidget.md) | qt-widgets | 4 |
| [app-logic/ReconstructionFeatureProperties](../app-logic/ReconstructionFeatureProperties.md) | app-logic | 3 |
| [app-logic/FlowlineUtils](../app-logic/FlowlineUtils.md) | app-logic | 2 |
| [app-logic/SmallCircleGeometryPopulator](../app-logic/SmallCircleGeometryPopulator.md) | app-logic | 2 |
| [file-io/GpmlPropertyStructuralTypeReader](../file-io/GpmlPropertyStructuralTypeReader.md) | file-io | 2 |
| [file-io/GsmlPropertyHandlers](../file-io/GsmlPropertyHandlers.md) | file-io | 2 |
| [file-io/PlatesFormatUtils](../file-io/PlatesFormatUtils.md) | file-io | 2 |
| [gui/TopologyTools](../gui/TopologyTools.md) | gui | 2 |
| [model/ModelUtils](../model/ModelUtils.md) | model | 2 |
| [app-logic/MotionPathUtils](../app-logic/MotionPathUtils.md) | app-logic | 1 |
| [app-logic/PlateVelocityUtils](../app-logic/PlateVelocityUtils.md) | app-logic | 1 |
| [app-logic/ReconstructMethodByPlateId](../app-logic/ReconstructMethodByPlateId.md) | app-logic | 1 |
| [app-logic/ReconstructMethodFlowline](../app-logic/ReconstructMethodFlowline.md) | app-logic | 1 |
| [app-logic/ReconstructMethodHalfStageRotation](../app-logic/ReconstructMethodHalfStageRotation.md) | app-logic | 1 |
| [app-logic/ReconstructMethodMotionPath](../app-logic/ReconstructMethodMotionPath.md) | app-logic | 1 |
| [app-logic/ReconstructMethodVirtualGeomagneticPole](../app-logic/ReconstructMethodVirtualGeomagneticPole.md) | app-logic | 1 |

*... and 32 more units.*

## Related

*None.*

## Explore

Run these from the `gplates-code` skill directory:

```bash
python scripts/gpq.py file src/property-values/GmlTimePeriod.h
python scripts/gpq.py def GPlatesPropertyValues::GmlTimePeriod --body
python scripts/gpq.py uses GmlTimePeriod --kind class
python scripts/gpq.py hier GmlTimePeriod
```
