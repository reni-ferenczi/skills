# LayerProxyVisitor

[Book TOC](../../TOC.md) · [app-logic](../../components/app-logic.md) · cluster Community 601 · tier 1

| Source file | Kind | Lines |
|---|---|---|
| `src/app-logic/LayerProxyVisitor.h` | C++ | 230 |

## Overview

A header-only Visitor over the closed set of `LayerProxy` subclasses. `LayerProxy`
declares two pure virtual `accept_visitor` overloads, one taking a
`ConstLayerProxyVisitor` and one a `LayerProxyVisitor`; each concrete proxy
implements them inline as `visitor.visit(GPlatesUtils::get_non_null_pointer(this))`,
which is the second half of the double dispatch. The visitor's overload set is
therefore the authoritative enumeration of the layer kinds the application knows
about — co-registration, raster, reconstruct, reconstruct-scalar-coverage,
reconstruction, 3D scalar field, topological geometry, topological network and
velocity field.

Const and non-const visitation share one definition. `LayerProxyVisitorBase` is
templated on the visited type, and every concrete proxy typedef is run through
`GPlatesUtils::CopyConst<LayerProxyType, X>`, which copies the const-ness of the
template argument onto `X`. Instantiating with `LayerProxy` gives visit overloads
taking `non_null_intrusive_ptr<RasterLayerProxy>`; instantiating with
`const LayerProxy` gives `non_null_intrusive_ptr<const RasterLayerProxy>`. The two
typedefs at the top of the header name those two instantiations, and callers use
those names rather than the template.

In practice this is used less for open-ended traversal than as a type-safe
substitute for `dynamic_cast`. `LayerProxyUtils::LayerProxyDerivedTypeFinder<T>`
derives from the visitor, overrides the single `visit` overload for `T`, and
collects what it finds; `LayerProxyUtils::get_layer_proxy_derived_type<T>()` and
`get_layer_proxy_derived_type_sequence()` wrap that into a
`boost::optional<T *>` or a filtered container. Most of the fan-in listed below
reaches this header through those two functions, not by writing a visitor of its
own.

## Declared types

| Name | Kind | Bases | Template | Subclasses | Description |
|---|---|---|---|---|---|
| [`GPlatesAppLogic::LayerProxyVisitor`](#gplatesapplogiclayerproxyvisitor) | typedef | — | — | 1 | Typedef for visitor over non-const LayerProxy objects. |
| [`GPlatesAppLogic::ConstLayerProxyVisitor`](#gplatesapplogicconstlayerproxyvisitor) | typedef | — | — | 0 | Typedef for visitor over const LayerProxy objects. |
| [`GPlatesAppLogic::LayerProxyVisitorBase`](#gplatesapplogiclayerproxyvisitorbase) | class | — | `<class LayerProxyType>` | 1 | This class defines an abstract interface for a Visitor to visit layer proxy objects. |

## Members

### `GPlatesAppLogic::LayerProxyVisitor`

*None.*

### `GPlatesAppLogic::ConstLayerProxyVisitor`

*None.*

### `GPlatesAppLogic::LayerProxyVisitorBase`

| Member | Kind | Type | Access | Description |
|---|---|---|---|---|
| `co_registration_layer_proxy_type` | typedef | `typename GPlatesUtils::CopyConst< LayerProxyType, CoRegistrationLayerProxy>::type` | public | Typedef for CoRegistrationLayerProxy of appropriate const-ness. |
| `raster_layer_proxy_type` | typedef | `typename GPlatesUtils::CopyConst< LayerProxyType, RasterLayerProxy>::type` | public | Typedef for RasterLayerProxy of appropriate const-ness. |
| `reconstruct_layer_proxy_type` | typedef | `typename GPlatesUtils::CopyConst< LayerProxyType, ReconstructLayerProxy>::type` | public | Typedef for ReconstructLayerProxy of appropriate const-ness. |
| `reconstruct_scalar_coverage_layer_proxy_type` | typedef | `typename GPlatesUtils::CopyConst< LayerProxyType, ReconstructScalarCoverageLayerProxy>::type` | public | Typedef for ReconstructScalarCoverageLayerProxy of appropriate const-ness. |
| `reconstruction_layer_proxy_type` | typedef | `typename GPlatesUtils::CopyConst< LayerProxyType, ReconstructionLayerProxy>::type` | public | Typedef for ReconstructionLayerProxy of appropriate const-ness. |
| `scalar_field_3d_layer_proxy_type` | typedef | `typename GPlatesUtils::CopyConst< LayerProxyType, ScalarField3DLayerProxy>::type` | public | Typedef for ScalarField3DLayerProxy of appropriate const-ness. |
| `topology_geometry_resolver_layer_proxy_type` | typedef | `typename GPlatesUtils::CopyConst< LayerProxyType, TopologyGeometryResolverLayerProxy>::type` | public | Typedef for TopologyGeometryResolverLayerProxy of appropriate const-ness. |
| `topology_network_resolver_layer_proxy_type` | typedef | `typename GPlatesUtils::CopyConst< LayerProxyType, TopologyNetworkResolverLayerProxy>::type` | public | Typedef for TopologyNetworkResolverLayerProxy of appropriate const-ness. |
| `velocity_field_calculator_layer_proxy_type` | typedef | `typename GPlatesUtils::CopyConst< LayerProxyType, VelocityFieldCalculatorLayerProxy>::type` | public | Typedef for VelocityFieldCalculatorLayerProxy of appropriate const-ness. |
| `~LayerProxyVisitorBase()` | destructor | `None` | public | We'll make this function pure virtual so that the class is abstract. |
| `visit( const GPlatesUtils::non_null_intrusive_ptr<co_registration_layer_proxy_type> &layer_proxy)` | method | `void` | public | Override this function in your own derived class. |
| `visit( const GPlatesUtils::non_null_intrusive_ptr<raster_layer_proxy_type> &layer_proxy)` | method | `void` | public | Override this function in your own derived class. |
| `visit( const GPlatesUtils::non_null_intrusive_ptr<reconstruct_layer_proxy_type> &layer_proxy)` | method | `void` | public | Override this function in your own derived class. |
| `visit( const GPlatesUtils::non_null_intrusive_ptr<reconstruct_scalar_coverage_layer_proxy_type> &layer_proxy)` | method | `void` | public | Override this function in your own derived class. |
| `visit( const GPlatesUtils::non_null_intrusive_ptr<reconstruction_layer_proxy_type> &layer_proxy)` | method | `void` | public | Override this function in your own derived class. |
| `visit( const GPlatesUtils::non_null_intrusive_ptr<scalar_field_3d_layer_proxy_type> &layer_proxy)` | method | `void` | public | Override this function in your own derived class. |
| `visit( const GPlatesUtils::non_null_intrusive_ptr<topology_geometry_resolver_layer_proxy_type> &layer_proxy)` | method | `void` | public | Override this function in your own derived class. |
| `visit( const GPlatesUtils::non_null_intrusive_ptr<topology_network_resolver_layer_proxy_type> &layer_proxy)` | method | `void` | public | Override this function in your own derived class. |
| `visit( const GPlatesUtils::non_null_intrusive_ptr<velocity_field_calculator_layer_proxy_type> &layer_proxy)` | method | `void` | public | Override this function in your own derived class. |

## Free functions and macros

| Name | Kind | Type / body | Description |
|---|---|---|---|
| `GPLATES_APP_LOGIC_LAYERPROXYVISITOR_H` | macro | `None` | — |

## Notes

Every `visit` overload has an empty inline body, so a derived visitor overrides
only the cases it cares about and silently ignores the rest — there is no
"unhandled proxy type" diagnostic. That default is also why the destructor is
declared pure virtual and then given an out-of-line definition: without it nothing
in the class would be pure and the class would not be abstract.

Overriding one overload hides the whole overload set, so a derived visitor must
write `using base_class_type::visit;` (as `LayerProxyDerivedTypeFinder` does) or
its remaining `accept_visitor` calls will not compile.

Adding a new `LayerProxy` subclass means editing this header: a forward
declaration, a `CopyConst` typedef and a `visit` overload. Skipping it is normally
a compile error in the new subclass's `accept_visitor`, but a proxy derived from an
*existing* proxy will bind to the base's overload and be reported as the base type
by `get_layer_proxy_derived_type`.

`visit` receives a `non_null_intrusive_ptr`, so the proxy is reference-counted for
the duration of the call, but `LayerProxyDerivedTypeFinder` stores raw pointers
(`layer_proxy.get()`). Results from `get_layer_proxy_derived_type` are only valid
while the caller still holds its own reference to the proxy.

## Used by

| Unit | Component | References |
|---|---|---|
| [opengl/GLVisualLayers](../opengl/GLVisualLayers.md) | opengl | 23 |
| [presentation/LayerOutputRenderer](../presentation/LayerOutputRenderer.md) | presentation | 21 |
| [app-logic/TopologyGeometryResolverLayerTask](TopologyGeometryResolverLayerTask.md) | app-logic | 17 |
| [app-logic/ReconstructLayerTask](ReconstructLayerTask.md) | app-logic | 15 |
| [app-logic/ResolvedRaster](ResolvedRaster.md) | app-logic | 15 |
| [app-logic/LayerProxyUtils](LayerProxyUtils.md) | app-logic | 10 |
| [app-logic/RasterLayerTask](RasterLayerTask.md) | app-logic | 10 |
| [app-logic/ScalarField3DLayerTask](ScalarField3DLayerTask.md) | app-logic | 10 |
| [app-logic/VelocityFieldCalculatorLayerTask](VelocityFieldCalculatorLayerTask.md) | app-logic | 10 |
| [app-logic/ScalarField3DLayerProxy](ScalarField3DLayerProxy.md) | app-logic | 8 |
| [app-logic/VelocityFieldCalculatorLayerProxy](VelocityFieldCalculatorLayerProxy.md) | app-logic | 8 |
| [gui/ExportRasterAnimationStrategy](../gui/ExportRasterAnimationStrategy.md) | gui | 8 |
| [app-logic/Reconstruction](Reconstruction.md) | app-logic | 7 |
| [qt-widgets/CoRegistrationLayerConfigurationDialog](../qt-widgets/CoRegistrationLayerConfigurationDialog.md) | qt-widgets | 6 |
| [app-logic/CoRegistrationLayerProxy](CoRegistrationLayerProxy.md) | app-logic | 5 |
| [app-logic/ReconstructLayerProxy](ReconstructLayerProxy.md) | app-logic | 5 |
| [app-logic/TopologyGeometryResolverLayerProxy](TopologyGeometryResolverLayerProxy.md) | app-logic | 5 |
| [gui/ExportScalarCoverageAnimationStrategy](../gui/ExportScalarCoverageAnimationStrategy.md) | gui | 5 |
| [gui/ExportVelocityAnimationStrategy](../gui/ExportVelocityAnimationStrategy.md) | gui | 5 |
| [app-logic/ReconstructGraph](ReconstructGraph.md) | app-logic | 4 |

*... and 14 more units.*

## Related

*None.*

## Explore

Run these from the `gplates-code` skill directory:

```bash
python scripts/gpq.py file src/app-logic/LayerProxyVisitor.h
python scripts/gpq.py def GPlatesAppLogic::LayerProxyVisitorBase --body
python scripts/gpq.py uses LayerProxyVisitorBase --kind class
python scripts/gpq.py hier LayerProxyVisitorBase
```
