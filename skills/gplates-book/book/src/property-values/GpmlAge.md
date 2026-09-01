# GpmlAge

[Book TOC](../../TOC.md) · [property-values](../../components/property-values.md) · cluster Community 466 · tier 2

| Source file | Kind | Lines |
|---|---|---|
| `src/property-values/GpmlAge.h` | C++ | 558 |
| `src/property-values/GpmlAge.cc` | C++ | 337 |

## Overview

`GpmlAge` is the `GPlatesModel::PropertyValue` for `gpml:Age`, and unlike the
simple `gml:validTime` numeric ages elsewhere in this component, it is meant
to carry real, possibly messy geological age data. The header is explicit
about why: it must support an age expressed as an absolute number in Ma
(`d_age_absolute`), a named stratigraphic or geomagnetic band from a
`TimescaleBand`/`TimescaleName` pair (`d_age_named`, `d_timescale`), or both
at once, because legacy data and pragmatic UI editing both demand it — the
class makes no attempt to force a single canonical representation. The same
pattern repeats for uncertainty: it can be a simple `d_uncertainty_plusminus`
in My, or an asymmetric youngest/oldest range where each end is independently
either an absolute value or a named band. `age_type()` and
`uncertainty_type()` are convenience methods that classify which combination
of optionals is currently populated (`AgeDefinition::AGE_ABSOLUTE`/`AGE_NAMED`/
`AGE_BOTH`/`AGE_NONE` and the analogous `UncertaintyDefinition` values), so
callers such as `EditAgeWidget` don't have to re-derive that logic themselves.

Every setter is independent and side-effect-free with respect to the other
fields: setting an absolute age does not clear a named age, and setting the
plus-or-minus uncertainty does not clear the range uncertainty. The header
states this is deliberate — callers (typically a UI populating every field
explicitly from its widgets) are expected to clear what they mean to clear
themselves, rather than have the setters guess and silently drop data.

## Declared types

| Name | Kind | Bases | Template | Subclasses | Description |
|---|---|---|---|---|---|
| [`GPlatesPropertyValues::GpmlAge`](#gplatespropertyvaluesgpmlage) | class | [`GPlatesModel::PropertyValue`](../model/PropertyValue.md) | — | 0 | This class implements the PropertyValue which corresponds to "gpml:Age". |

## Members

### `GPlatesPropertyValues::GpmlAge`

| Member | Kind | Type | Access | Description |
|---|---|---|---|---|
| `AgeDefinition` | struct | `None` | public | For convenience methods to use to indicate to callers what format the user has defined this GpmlAge with. |
| `UncertaintyDefinition` | struct | `None` | public | For convenience methods to use to indicate to callers what format the user has defined this GpmlAge's uncertainty values with. |
| `non_null_ptr_type` | typedef | `GPlatesUtils::non_null_intrusive_ptr<GpmlAge>` | public | A convenience typedef for GPlatesUtils::non\_null\_intrusive\_ptr\<GpmlAge\>. |
| `non_null_ptr_to_const_type` | typedef | `GPlatesUtils::non_null_intrusive_ptr<const GpmlAge>` | public | A convenience typedef for GPlatesUtils::non\_null\_intrusive\_ptr\<const GpmlAge\>. |
| `~GpmlAge()` | destructor | `None` | public | — |
| `create( boost::optional<double> age_absolute, boost::optional<TimescaleBand> age_named, boost::optional<TimescaleName> timescale, boost::optional<double> uncertainty_plusminus, boost::optional<double> uncertainty_youngest_absolute, boost::optional<TimescaleBand> uncertainty_youngest_named, boost::optional<double> uncer ...` | method | `non_null_ptr_type` | public | This creation function is here purely for the simple, hard-coded construction of features. |
| `create( boost::optional<double> age_absolute, boost::optional<QString> age_named, boost::optional<QString> timescale, boost::optional<double> uncertainty_plusminus, boost::optional<double> uncertainty_youngest_absolute, boost::optional<QString> uncertainty_youngest_named, boost::optional<double> uncertainty_oldest_abso ...` | method | `non_null_ptr_type` | public | Create a GpmlAge instance. |
| `create()` | method | `non_null_ptr_type` | public | Create a GpmlAge instance. |
| `clone()` | method | `non_null_ptr_type` | public | — |
| `deep_clone()` | method | `GpmlAge::non_null_ptr_type` | public | — |
| `DEFINE_FUNCTION_DEEP_CLONE_AS_PROP_VAL()` | method | `None` | public | — |
| `get_age_absolute` | field | `boost::optional<double>` | public | Return the absolute age, if such data is explicitly present, of this GpmlAge. |
| `set_age_absolute( boost::optional<double> age_maybe)` | method | `void` | public | Set the absolute age of this GpmlAge. |
| `get_age_named` | field | `boost::optional<TimescaleBand>` | public | Return the named (stratigraphic,geomagnetic) age, if such data is explicitly present, of this GpmlAge. |
| `set_age_named( boost::optional<TimescaleBand> age_maybe)` | method | `void` | public | Set the named (stratigraphic,geomagnetic) age of this GpmlAge. |
| `set_age_named( const QString &age)` | method | `void` | public | As set\_age\_named(TimescaleBand), but sometimes all you have is a QString... |
| `age_type()` | method | `AgeDefinition::AgeDefinitionType` | public | Convenience method to quickly determine how this Age has been defined. |
| `get_timescale` | field | `boost::optional<TimescaleName>` | public | Return the name of the geological or geomagnetic (or who knows what else) timescale used by this GpmlAge. |
| `set_timescale( boost::optional<TimescaleName> timescale_maybe)` | method | `void` | public | Set the name of the timescale used by this GpmlAge. |
| `set_timescale( const QString &timescale)` | method | `void` | public | As set\_timescale(TimescaleName), but sometimes all you have is a QString... |
| `get_uncertainty_plusminus` | field | `boost::optional<double>` | public | A GpmlAge can express uncertainties in one of two ways; a simple plus-or-minus value expressed in My or an asymmetric young \<=\> old range. |
| `set_uncertainty_plusminus( boost::optional<double> uncertainty_maybe)` | method | `void` | public | Set the uncertainty of this GpmlAge to a simple plus-or-minus value expressed in My. |
| `get_uncertainty_youngest_absolute` | field | `boost::optional<double>` | public | A GpmlAge can express uncertainties in one of two ways; a simple plus-or-minus value expressed in My or an asymmetric young \<=\> old range. |
| `set_uncertainty_youngest_absolute( boost::optional<double> uncertainty_maybe)` | method | `void` | public | Set the youngest part of the uncertainty range of this GpmlAge to an absolute value in Ma. |
| `get_uncertainty_youngest_named` | field | `boost::optional<TimescaleBand>` | public | A GpmlAge can express uncertainties in one of two ways; a simple plus-or-minus value expressed in My or an asymmetric young \<=\> old range. |
| `set_uncertainty_youngest_named( boost::optional<TimescaleBand> uncertainty_maybe)` | method | `void` | public | Set the youngest part of the uncertainty range of this GpmlAge to a named value from some timescale. |
| `set_uncertainty_youngest_named( const QString &uncertainty)` | method | `void` | public | As set\_uncertainty\_youngest\_named(TimescaleBand), but sometimes all you have is a QString... |
| `get_uncertainty_oldest_absolute` | field | `boost::optional<double>` | public | A GpmlAge can express uncertainties in one of two ways; a simple plus-or-minus value expressed in My or an asymmetric young \<=\> old range. |
| `set_uncertainty_oldest_absolute( boost::optional<double> uncertainty_maybe)` | method | `void` | public | Set the oldest part of the uncertainty range of this GpmlAge to an absolute value in Ma. |
| `get_uncertainty_oldest_named` | field | `boost::optional<TimescaleBand>` | public | A GpmlAge can express uncertainties in one of two ways; a simple plus-or-minus value expressed in My or an asymmetric young \<=\> old range. |
| `set_uncertainty_oldest_named( boost::optional<TimescaleBand> uncertainty_maybe)` | method | `void` | public | Set the oldest part of the uncertainty range of this GpmlAge to a named value from some timescale. |
| `set_uncertainty_oldest_named( const QString &uncertainty)` | method | `void` | public | As set\_uncertainty\_oldest\_named(TimescaleBand), but sometimes all you have is a QString... |
| `uncertainty_type()` | method | `UncertaintyDefinition::UncertaintyDefinitionType` | public | Convenience method to quickly determine how this Age's uncertainty data has been defined. |
| `get_structural_type()` | method | `StructuralType` | public | Returns the structural type associated with this property value class. |
| `accept_visitor( GPlatesModel::ConstFeatureVisitor &visitor)` | method | `void` | public | Accept a ConstFeatureVisitor instance. |
| `accept_visitor( GPlatesModel::FeatureVisitor &visitor)` | method | `void` | public | Accept a FeatureVisitor instance. |
| `print_to` | field | `std::ostream` | public | — |
| `GpmlAge( boost::optional<double> age_absolute, boost::optional<TimescaleBand> age_named, boost::optional<TimescaleName> timescale, boost::optional<double> uncertainty_plusminus, boost::optional<double> uncertainty_youngest_absolute, boost::optional<TimescaleBand> uncertainty_youngest_named, boost::optional<double> unce ...` | constructor | `None` | protected | This constructor should not be public, because we don't want to allow instantiation of this type on the stack. |
| `GpmlAge( const GpmlAge &other)` | constructor | `None` | protected | This constructor should not be public, because we don't want to allow instantiation of this type on the stack. |
| `d_age_absolute` | field | `boost::optional<double>` | private | A gpml:Age can have its age specified as an absolute (numeric) age in Ma. |
| `d_age_named` | field | `boost::optional<TimescaleBand>` | private | A gpml:Age can also have its age specified as a named (stratigraphic or otherwise) age, such as "Paleogene" or "Late Triassic". |
| `d_timescale` | field | `boost::optional<TimescaleName>` | private | A gpml:Age can (and is strongly encouraged to) have a stratigraphic or geomagnetic timescale associated with it. |
| `d_uncertainty_plusminus` | field | `boost::optional<double>` | private | A gpml:Age can have an associated uncertainty. |
| `d_uncertainty_youngest_absolute` | field | `boost::optional<double>` | private | A gpml:Age can alternatively represent uncertainty information as an asymmetric age range, with a 'youngest' and 'oldest' age estimate. |
| `d_uncertainty_youngest_named` | field | `boost::optional<TimescaleBand>` | private | — |
| `d_uncertainty_oldest_absolute` | field | `boost::optional<double>` | private | — |
| `d_uncertainty_oldest_named` | field | `boost::optional<TimescaleBand>` | private | — |
| `operator=` | field | `GpmlAge` | private | This operator should never be defined, because we don't want/need to allow copy-assignment: All copying should use the virtual copy-constructor 'clone' (which will in turn use the copy-constructor); all "assignment" should really only be ... |

## Free functions and macros

| Name | Kind | Type / body | Description |
|---|---|---|---|
| `convert_to_band_maybe( const QString &str)` | function | `boost::optional<GPlatesPropertyValues::TimescaleBand>` | — |
| `convert_to_band_maybe( const boost::optional<QString> &str_maybe)` | function | `boost::optional<GPlatesPropertyValues::TimescaleBand>` | — |
| `convert_to_name_maybe( const QString &str)` | function | `boost::optional<GPlatesPropertyValues::TimescaleName>` | — |
| `convert_to_name_maybe( const boost::optional<QString> &str_maybe)` | function | `boost::optional<GPlatesPropertyValues::TimescaleName>` | — |
| `GPLATES_PROPERTYVALUES_GPMLAGE_H` | macro | `None` | — |

## Notes

- No field is authoritative over another: `d_age_absolute` and `d_age_named`
  can disagree, and the header explicitly declines to define which one wins
  once both are present — that decision is left to callers.
- The uncertainty range fields (`d_uncertainty_youngest_absolute`/`_named`,
  `d_uncertainty_oldest_absolute`/`_named`) are constrained to hold at most one
  of absolute-or-named per end (a design choice the header attributes to
  keeping the `EditAgeWidget` UI tractable), but nothing in the type system
  enforces this — it is only upheld by convention in the setters.
- `set_timescale()` records the timescale name only; it does not convert any
  already-stored absolute ages into that timescale, nor validate that any
  named age actually belongs to it.
- `deep_clone()` is equivalent to `clone()` here, since every field is a
  `boost::optional` of a value type or a `StringSet`-backed handle, not a
  pointer to another mutable `PropertyValue`.

## Used by

| Unit | Component | References |
|---|---|---|
| [qt-widgets/EditAgeWidget](../qt-widgets/EditAgeWidget.md) | qt-widgets | 56 |
| [feature-visitors/ToQvariantConverter](../feature-visitors/ToQvariantConverter.md) | feature-visitors | 25 |
| [file-io/GpmlOutputVisitor](../file-io/GpmlOutputVisitor.md) | file-io | 22 |
| [file-io/GpmlPropertyStructuralTypeReaderUtils](../file-io/GpmlPropertyStructuralTypeReaderUtils.md) | file-io | 3 |
| [qt-widgets/EditWidgetChooser](../qt-widgets/EditWidgetChooser.md) | qt-widgets | 1 |

## Related

*None.*

## Explore

Run these from the `gplates-code` skill directory:

```bash
python scripts/gpq.py file src/property-values/GpmlAge.h
python scripts/gpq.py def GPlatesPropertyValues::GpmlAge --body
python scripts/gpq.py uses GpmlAge --kind class
python scripts/gpq.py hier GpmlAge
```
