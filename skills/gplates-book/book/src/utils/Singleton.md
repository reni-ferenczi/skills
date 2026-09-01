# Singleton

[Book TOC](../../TOC.md) · [utils](../../components/utils.md) · cluster Community 1662 · tier 2

| Source file | Kind | Lines |
|---|---|---|
| `src/utils/Singleton.h` | C++ | 341 |

## Overview

`Singleton<T, CreationPolicy, LifetimePolicy, InstanceTag>` is a policy-based CRTP base that gives a derived class `T` a static `instance()` returning the one-and-only `T&`, following the classic Alexandrescu-style singleton design. `CreationPolicy` (default `CreateUsingNew`) controls how the instance is allocated, and `LifetimePolicy` (default `DefaultLifetime`) controls destruction order and what happens if `instance()` is called after destruction (by default it throws `LogException` via `on_dead_reference()`, rather than silently resurrecting the object). The unused `InstanceTag` template parameter is a way to get multiple independent singleton instances of the same `T` without subclassing — each distinct tag type selects a different static instance.

Whether client code can construct `T` directly is controlled by which of the four `GPLATES_SINGLETON_*_CONSTRUCTOR_*` macros the derived class uses at the top of its definition: the non-`PUBLIC` variants make the constructor protected and friend only `CreateUsingNew<T>`, so `T` can only ever be created via `instance()`; the `PUBLIC` variants leave the constructor public so `T` can also be created directly, for example on the call stack, letting the caller bound the singleton's lifetime to a scope while `instance()` still returns that same object for the scope's duration. `Model::Gpgim`, `RenderedGeometryCollection`, colour-name registries and several other one-of-a-kind services in GPlates are built this way rather than as ad hoc global objects.

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

- Not thread-safe by default: define `GPLATES_SINGLETON_THREADSAFE` before including this header to get a `QMutexLocker` guarding `instance()`.
- The default `DefaultLifetime` schedules destruction with `std::atexit`, so instances are torn down in reverse creation order at program exit; calling `instance()` again after that point throws `GPlatesGlobal::LogException` rather than recreating the singleton.
- The instance pointer and destroyed-flag are function-local statics (not plain static data members), specifically to sidestep undefined static-initialization order across translation units.
- A derived class may instead be constructed directly (e.g. on the C++ call stack) when it exposes a public constructor via the `PUBLIC` macro variants; `instance()` still returns that same object while it is in scope, but a precondition assert fires if `instance()` was already called before the stack-allocated object is constructed.

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
