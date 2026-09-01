# PointerTraits

[Book TOC](../../TOC.md) · [global](../../components/global.md) · cluster Community 138 · tier 1

| Source file | Kind | Lines |
|---|---|---|
| `src/global/PointerTraits.h` | C++ | 89 |

## Overview

A header-dependency breaker, not a smart-pointer abstraction. GPlates classes conventionally publish `typedef GPlatesUtils::non_null_intrusive_ptr<Foo> non_null_ptr_type` inside `Foo`, which means any header that merely *names* `Foo::non_null_ptr_type` must include `Foo.h` in full — a forward declaration is not enough to resolve a nested typedef. `GPlatesGlobal::PointerTraits<Foo>::non_null_ptr_type` spells the same type without opening `Foo`, so the dependent header needs only a forward declaration of `Foo` plus this one small header. The whole file is that trick: a base template holding the typedef, and a derived primary template that exists so individual types can be specialised later without every user changing.

The problem it solves is cyclic includes among templates, and that is where you find it in practice. `GPlatesModel::BasicHandle` and `GPlatesModel::BasicRevision` are mutually recursive templates parameterised on handle types whose own headers include theirs, and they name child, revision and handle pointer types entirely through `PointerTraits`; `GPlatesAppLogic` layer proxies use it the same way to refer to `ReconstructedFeatureGeometry`, `ResolvedRaster`, `ResolvedScalarField3D` and each other's proxy types without pulling in those headers. `GPlatesAppLogic::CoRegistrationLayerProxy` uses it to hold a pointer to `GPlatesOpenGL::GLRasterCoRegistration` while keeping the OpenGL header out of app-logic.

Reach for it when a header would otherwise have to include another header solely for a pointer typedef, and especially when doing so would close a cycle. Where there is no cycle, the plain `Foo::non_null_ptr_type` spelling remains the norm and is much more readable.

## Declared types

| Name | Kind | Bases | Template | Subclasses | Description |
|---|---|---|---|---|---|
| [`GPlatesGlobal::PointerTraitsInternal::PointerTraitsBase`](#gplatesglobalpointertraitsinternalpointertraitsbase) | struct | — | `<class T>` | 1 | — |
| [`GPlatesGlobal::PointerTraits`](#gplatesglobalpointertraits) | struct | [`PointerTraitsInternal::PointerTraitsBase<T>`](PointerTraits.md) | `<class T>` | 0 | PointerTraits provides type information about smart pointers to GPlates objects. |

## Members

### `GPlatesGlobal::PointerTraitsInternal::PointerTraitsBase`

| Member | Kind | Type | Access | Description |
|---|---|---|---|---|
| `non_null_ptr_type` | typedef | `GPlatesUtils::non_null_intrusive_ptr<T>` | public | — |

### `GPlatesGlobal::PointerTraits`

*None.*

## Free functions and macros

| Name | Kind | Type / body | Description |
|---|---|---|---|
| `GPLATES_GLOBAL_POINTERTRAITS_H` | macro | `None` | — |

## Notes

- **The documented extension point is unused.** The header explains how to specialise `PointerTraits<Foo>`, but the 2.5.0 tree contains no specialisation, so `PointerTraits<T>::non_null_ptr_type` is always exactly `GPlatesUtils::non_null_intrusive_ptr<T>`. If you add one, inherit `PointerTraitsInternal::PointerTraitsBase<T>` as the comment instructs — a specialisation that forgets to will silently drop `non_null_ptr_type` and break every existing use of that type.
- **There is no `non_null_ptr_to_const_type`.** By design: write `PointerTraits<const T>::non_null_ptr_type` for the const flavour. This differs from the `non_null_ptr_to_const_type` typedef most classes publish themselves, so the two spellings are not symmetric.
- The alias hardwires `non_null_intrusive_ptr`'s default `NullIntrusivePointerHandler`. It is only interchangeable with a class's own `non_null_ptr_type` while that typedef also uses the default handler.
- **It defers the include, it does not eliminate it.** `non_null_intrusive_ptr` calls unqualified `intrusive_ptr_add_ref` / `intrusive_ptr_release` on copy and destruction, so the complete type is still needed wherever the pointer is actually copied, dereferenced or destroyed — normally the `.cc`. The header-only saving is what matters, and it is what breaks the cycle.
- Inside a template, the nested typedef is dependent: you must write `typename GPlatesGlobal::PointerTraits<T>::non_null_ptr_type`, as `BasicHandle` and `BasicRevision` do throughout.
- Readability cost is real. A signature written in `PointerTraits` form is considerably harder to read than the direct typedef, and the compiler errors from it name the traits template rather than the class. Use it only where the include cycle forces it.

## Used by

| Unit | Component | References |
|---|---|---|
| [model/BasicHandle](../model/BasicHandle.md) | model | 46 |
| [model/ModelUtils](../model/ModelUtils.md) | model | 25 |
| [model/FeatureHandle](../model/FeatureHandle.md) | model | 23 |
| [presentation/ViewState](../presentation/ViewState.md) | presentation | 20 |
| [property-values/RawRasterUtils](../property-values/RawRasterUtils.md) | property-values | 17 |
| [model/TopLevelPropertyRef](../model/TopLevelPropertyRef.md) | model | 16 |
| [model/BasicRevision](../model/BasicRevision.md) | model | 15 |
| [model/HandleTraits](../model/HandleTraits.md) | model | 15 |
| [file-io/RasterBandReader](../file-io/RasterBandReader.md) | file-io | 13 |
| [model/TopLevelPropertyInline](../model/TopLevelPropertyInline.md) | model | 13 |
| [app-logic/DependentTopologicalSectionLayers](../app-logic/DependentTopologicalSectionLayers.md) | app-logic | 11 |
| [model/FeatureRevision](../model/FeatureRevision.md) | model | 10 |
| [qt-widgets/GlobeAndMapWidget](../qt-widgets/GlobeAndMapWidget.md) | qt-widgets | 10 |
| [app-logic/GeometryUtils](../app-logic/GeometryUtils.md) | app-logic | 8 |
| [feature-visitors/FromQvariantConverter](../feature-visitors/FromQvariantConverter.md) | feature-visitors | 8 |
| [opengl/GLMultiResolutionRaster](../opengl/GLMultiResolutionRaster.md) | opengl | 8 |
| [opengl/GLOffScreenContext](../opengl/GLOffScreenContext.md) | opengl | 8 |
| [property-values/GpmlTimeSample](../property-values/GpmlTimeSample.md) | property-values | 8 |
| [property-values/GpmlTimeWindow](../property-values/GpmlTimeWindow.md) | property-values | 8 |
| [qt-widgets/CreateFeaturePropertiesPage](../qt-widgets/CreateFeaturePropertiesPage.md) | qt-widgets | 7 |

*... and 78 more units.*

## Related

*None.*

## Explore

Run these from the `gplates-code` skill directory:

```bash
python scripts/gpq.py file src/global/PointerTraits.h
python scripts/gpq.py def GPlatesGlobal::PointerTraits --body
python scripts/gpq.py uses PointerTraits --kind struct
python scripts/gpq.py hier PointerTraits
```
