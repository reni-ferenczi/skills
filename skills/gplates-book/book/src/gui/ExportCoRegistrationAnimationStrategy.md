# ExportCoRegistrationAnimationStrategy

[Book TOC](../../TOC.md) · [gui](../../components/gui.md) · cluster Community 1320 · tier 3

| Source file | Kind | Lines |
|---|---|---|
| `src/gui/ExportCoRegistrationAnimationStrategy.h` | C++ | 128 |
| `src/gui/ExportCoRegistrationAnimationStrategy.cc` | C++ | 169 |

## Overview

A concrete implementation of the animation export strategy pattern for co-registration data. Each frame during an animation export calls `do_export_iteration()`, which uses the `ExportAnimationContext` to compute co-registration results at the current reconstruction time and writes them to output files. Configuration controls filename templates with placeholders for layer names and other substitutions. The class uses intrusive pointers and the factory pattern via the static `create()` method to ensure proper lifetime management.

## Declared types

| Name | Kind | Bases | Template | Subclasses | Description |
|---|---|---|---|---|---|
| [`GPlatesGui::ExportCoRegistrationAnimationStrategy`](#gplatesguiexportcoregistrationanimationstrategy) | class | [`GPlatesGui::ExportAnimationStrategy`](ExportAnimationStrategy.md) | — | 0 | Concrete implementation of the ExportAnimationStrategy class for writing co-registration data at each timestep. |

## Members

### `GPlatesGui::ExportCoRegistrationAnimationStrategy`

| Member | Kind | Type | Access | Description |
|---|---|---|---|---|
| `non_null_ptr_type` | typedef | `GPlatesUtils::non_null_intrusive_ptr<ExportCoRegistrationAnimationStrategy>` | public | A convenience typedef for GPlatesUtils::non\_null\_intrusive\_ptr\<ExportCoRegistrationAnimationStrategy\>. |
| `Configuration` | class | `None` | public | Configuration options. |
| `const_configuration_ptr` | typedef | `boost::shared_ptr<const Configuration>` | public | Typedef for a shared pointer to const Configuration. |
| `create( ExportAnimationContext &export_animation_context, const const_configuration_ptr &export_configuration)` | method | `non_null_ptr_type` | public | — |
| `~ExportCoRegistrationAnimationStrategy()` | destructor | `None` | public | — |
| `do_export_iteration( std::size_t frame_index)` | method | `bool` | public | Does one frame of export. |
| `ExportCoRegistrationAnimationStrategy( GPlatesGui::ExportAnimationContext &export_animation_context, const const_configuration_ptr &export_configuration)` | constructor | `None` | protected | Protected constructor to prevent instantiation on the stack. |
| `d_configuration` | field | `const_configuration_ptr` | private | Export configuration parameters. |

## Free functions and macros

| Name | Kind | Type / body | Description |
|---|---|---|---|
| `substitute_placeholder( const QString &output_filebasename, const QString &placeholder, const QString &placeholder_replacement)` | function | `QString` | — |
| `calculate_output_basename( const QString &output_filename_prefix, const QString &layer_name)` | function | `QString` | — |
| `GPLATES_GUI_EXPORTCOREGISTRATIONANIMATIONSTRATEGY_H` | macro | `None` | — |

## Notes

The protected constructor and factory method via `create()` enforce use of intrusive pointers. The Configuration class hierarchy allows subclasses to extend export options while remaining compatible with the base strategy interface.

## Used by

| Unit | Component | References |
|---|---|---|
| [gui/ExportAnimationRegistry](ExportAnimationRegistry.md) | gui | 4 |

## Related

*None.*

## Explore

Run these from the `gplates-code` skill directory:

```bash
python scripts/gpq.py file src/gui/ExportCoRegistrationAnimationStrategy.h
python scripts/gpq.py def GPlatesGui::ExportCoRegistrationAnimationStrategy --body
python scripts/gpq.py uses ExportCoRegistrationAnimationStrategy --kind class
python scripts/gpq.py hier ExportCoRegistrationAnimationStrategy
```
