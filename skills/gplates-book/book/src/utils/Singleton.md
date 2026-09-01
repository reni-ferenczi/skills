# Singleton

[Book TOC](../../TOC.md) · [utils](../../components/utils.md) · cluster Community 1662 · tier 2

| Source file | Kind | Lines |
|---|---|---|
| `src/utils/Singleton.h` | C++ | 341 |

## Overview

[[[PROSE overview unit=utils/Singleton tier=2]]]
Replace this whole block, markers included, with 1-3 paragraphs: what this unit is, why it exists, and how it fits the surrounding design. Do not restate the tables below.
[[[/PROSE]]]

## Declared types

| Name | Kind | Bases | Template | Subclasses | Description |
|---|---|---|---|---|---|
| [`GPlatesUtils::CreateUsingNew`](#gplatesutilscreateusingnew) | class | — | `<typename T>` | 0 | Singleton creation policy - allocates/constructs using operator new. |
| [`GPlatesUtils::DefaultLifetime`](#gplatesutilsdefaultlifetime) | class | — | `<typename T>` | 0 | Singleton lifetime policy - schedules singleton for destruction in reverse order of creation. |
| [`GPlatesUtils::Singleton`](#gplatesutilssingleton) | class | `boost::noncopyable` | `< typename T, template <typename> class CreationPolicy = CreateUsingNew, template <typename> class LifetimePolicy = DefaultLifetime, class InstanceTag = DefaultInstanceTag >` | 14 | — |

## Members

### `GPlatesUtils::CreateUsingNew`

| Member | Kind | Type | Access | Description |
|---|---|---|---|---|
| `create_instance()` | method | `T` | public | — |
| `destroy_instance( T *t)` | method | `void` | public | — |

### `GPlatesUtils::DefaultLifetime`

| Member | Kind | Type | Access | Description |
|---|---|---|---|---|
| `on_dead_reference()` | method | `void` | public | — |
| `schedule_for_destruction( T *singleton_instance, void (*destruction_function_ptr)())` | method | `void` | public | — |

### `GPlatesUtils::Singleton`

| Member | Kind | Type | Access | Description |
|---|---|---|---|---|
| `destroy()` | method | `void` | protected | — |
| `Singleton()` | constructor | `None` | protected | Only the derived singleton class 'T' can instantiate Singleton directly. |
| `~Singleton()` | destructor | `None` | protected | — |

## Free functions and macros

| Name | Kind | Type / body | Description |
|---|---|---|---|
| `GPLATES_UTILS_SINGLETON_H` | macro | `None` | — |
| `GPLATES_SINGLETON_CONSTRUCTOR_DECL` | macro_function | `protected: \ T(); \ friend class GPlatesUtils::CreateUsingNew<T>;` | Adds a default (protected) constructor and friend declaration. |
| `GPLATES_SINGLETON_CONSTRUCTOR_DEF` | macro_function | `protected: \ T() { } \ friend class GPlatesUtils::CreateUsingNew<T>;` | Adds a default (protected) constructor implementation and friend declaration. |
| `GPLATES_SINGLETON_PUBLIC_CONSTRUCTOR_DECL` | macro_function | `public: \ T();` | Adds a default (public) constructor and friend declaration. |
| `GPLATES_SINGLETON_PUBLIC_CONSTRUCTOR_DEF` | macro_function | `public: \ T() { }` | Adds a default (public) constructor implementation and friend declaration. |

## Notes

[[[PROSE notes unit=utils/Singleton tier=2]]]
Replace this whole block, markers included, with invariants, ownership, threading or gotchas that are not visible in the tables. Write *None.* if there is nothing worth saying.
[[[/PROSE]]]

## Used by

| Unit | Component | References |
|---|---|---|
| [model/StringSetSingletons](../model/StringSetSingletons.md) | model | 41 |
| [view-operations/UndoRedo](../view-operations/UndoRedo.md) | view-operations | 5 |
| [app-logic/GPlatesQtMsgHandler](../app-logic/GPlatesQtMsgHandler.md) | app-logic | 4 |
| [file-io/RotationAttributesRegistry](../file-io/RotationAttributesRegistry.md) | file-io | 4 |
| [file-io/TemporaryFileRegistry](../file-io/TemporaryFileRegistry.md) | file-io | 4 |
| [gui/Completionist](../gui/Completionist.md) | gui | 4 |
| [unit-test/TestSuiteFilter](../unit-test/TestSuiteFilter.md) | unit-test | 4 |
| [file-io/deprecated/FeaturePropertiesMap](../file-io/deprecated/FeaturePropertiesMap.md) | file-io | 3 |
| [gui/GMTColourNames](../gui/GMTColourNames.md) | gui | 3 |
| [gui/HTMLColourNames](../gui/HTMLColourNames.md) | gui | 3 |
| [gui/PlateIdColourPalettes](../gui/PlateIdColourPalettes.md) | gui | 3 |
| [model/Gpgim](../model/Gpgim.md) | model | 3 |
| [presentation/Application](../presentation/Application.md) | presentation | 3 |
| [scribe/ScribeExportRegistry](../scribe/ScribeExportRegistry.md) | scribe | 3 |
| [view-operations/RenderedGeometryCollection](../view-operations/RenderedGeometryCollection.md) | view-operations | 3 |
| [file-io/GpmlOutputVisitor](../file-io/GpmlOutputVisitor.md) | file-io | 1 |

## Related

*None.*

## Explore

Run these from the `gplates-code` skill directory:

```bash
python scripts/gpq.py file src/utils/Singleton.h
python scripts/gpq.py def GPlatesUtils::Singleton --body
python scripts/gpq.py uses Singleton --kind class
python scripts/gpq.py hier Singleton
```
