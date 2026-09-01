# CopyOnWrite

[Book TOC](../../TOC.md) · [utils](../../components/utils.md) · cluster Community 891 · tier 3

| Source file | Kind | Lines |
|---|---|---|
| `src/utils/CopyOnWrite.h` | C++ | 506 |

## Overview

`CopyOnWrite` is a template wrapper that provides copy-on-write semantics for smart pointers—`non_null_intrusive_ptr`, `boost::intrusive_ptr`, and `boost::shared_ptr`. It minimizes copying by sharing the pointed-to object between copies as long as both remain read-only, but clones the object when one copy requests mutable access, ensuring isolation.

The wrapper maintains a flag tracking whether any copy has been given mutable access. On construction, it clones the input to ensure the new instance is independent. On copy construction, it shares the pointer if the source is still shareable (unmodified), otherwise it clones. When `get_non_const()` is called, it clones if the object is both shareable and currently shared by others, then marks the wrapper non-shareable to prevent further sharing. The default copy policy expects types to implement a `clone()` method returning the appropriate smart pointer type.

## Declared types

| Name | Kind | Bases | Template | Subclasses | Description |
|---|---|---|---|---|---|
| [`GPlatesUtils::DefaultCopyOnWritePolicy<non_null_intrusive_ptr<T,H> >`](#gplatesutilsdefaultcopyonwritepolicynon_null_intrusive_ptrth-) | class | — | `<class T, class H>` | 0 | Default copy policy for GPlatesUtils::non\_null\_intrusive\_ptr assumes a 'clone()' method that returns a non\_null\_intrusive\_ptr. |
| [`GPlatesUtils::CopyOnWrite<non_null_intrusive_ptr<T,H>, CopyPolicy>`](#gplatesutilscopyonwritenon_null_intrusive_ptrth-copypolicy) | class | — | `<class T, class H, template <class> class CopyPolicy>` | 0 | Partial specialisation of CopyOnWrite for GPlatesUtils::non\_null\_intrusive\_ptr. |
| [`GPlatesUtils::DefaultCopyOnWritePolicy<boost::intrusive_ptr<T> >`](#gplatesutilsdefaultcopyonwritepolicyboostintrusive_ptrt-) | class | — | `<class T>` | 0 | Default copy policy for boost::intrusive\_ptr assumes a 'clone()' method that returns either a boost::intrusive\_ptr or a non\_null\_intrusive\_ptr. |
| [`GPlatesUtils::CopyOnWrite<boost::intrusive_ptr<T>, CopyPolicy>`](#gplatesutilscopyonwriteboostintrusive_ptrt-copypolicy) | class | — | `<class T, template <class> class CopyPolicy>` | 0 | Partial specialisation of CopyOnWrite for boost::intrusive\_ptr. |
| [`GPlatesUtils::DefaultCopyOnWritePolicy<boost::shared_ptr<T> >`](#gplatesutilsdefaultcopyonwritepolicyboostshared_ptrt-) | class | — | `<class T>` | 0 | Default copy policy for boost::shared\_ptr assumes a 'clone()' method that returns a boost::shared\_ptr. |
| [`GPlatesUtils::CopyOnWrite<boost::shared_ptr<T>, CopyPolicy>`](#gplatesutilscopyonwriteboostshared_ptrt-copypolicy) | class | — | `<class T, template <class> class CopyPolicy>` | 0 | Partial specialisation of CopyOnWrite for boost::shared\_ptr. |

## Members

### `GPlatesUtils::DefaultCopyOnWritePolicy<non_null_intrusive_ptr<T,H> >`

| Member | Kind | Type | Access | Description |
|---|---|---|---|---|
| `copy( const non_null_intrusive_ptr<T,H> &value)` | method | `non_null_intrusive_ptr<T,H>` | public | — |

### `GPlatesUtils::CopyOnWrite<non_null_intrusive_ptr<T,H>, CopyPolicy>`

| Member | Kind | Type | Access | Description |
|---|---|---|---|---|
| `non_null_ptr_type` | typedef | `non_null_intrusive_ptr<T, H>` | public | — |
| `non_null_ptr_to_const_type` | typedef | `non_null_intrusive_ptr<const T, H>` | public | — |
| `CopyOnWrite( const non_null_ptr_type &value)` | method | `None` | public | Constructor creates a copy of the referenced value. |
| `CopyOnWrite( const CopyOnWrite &other)` | method | `None` | public | Copy constructor copies/clones if other is not shareable (if client has non-const reference to the value of other). |
| `get()` | method | `non_null_ptr_to_const_type` | public | Return 'const' reference to value. |
| `get_const()` | method | `non_null_ptr_to_const_type` | public | — |
| `get_non_const()` | method | `non_null_ptr_type` | public | — |
| `get_non_const( boost::mpl::true_/*'T' is const*/)` | method | `non_null_ptr_type` | private | — |
| `get_non_const( boost::mpl::false_/*'T' is not const*/)` | method | `non_null_ptr_type` | private | — |
| `d_value` | field | `non_null_ptr_type` | private | — |
| `d_shareable` | field | `bool` | private | — |

### `GPlatesUtils::DefaultCopyOnWritePolicy<boost::intrusive_ptr<T> >`

| Member | Kind | Type | Access | Description |
|---|---|---|---|---|
| `copy( const boost::intrusive_ptr<T> &value)` | method | `boost::intrusive_ptr<T>` | public | — |

### `GPlatesUtils::CopyOnWrite<boost::intrusive_ptr<T>, CopyPolicy>`

| Member | Kind | Type | Access | Description |
|---|---|---|---|---|
| `intrusive_ptr_type` | typedef | `boost::intrusive_ptr<T>` | public | — |
| `intrusive_ptr_to_const_type` | typedef | `boost::intrusive_ptr<const T>` | public | — |
| `CopyOnWrite( const intrusive_ptr_type &value)` | method | `None` | public | — |
| `CopyOnWrite( const CopyOnWrite &other)` | method | `None` | public | — |
| `get()` | method | `intrusive_ptr_to_const_type` | public | — |
| `get_const()` | method | `intrusive_ptr_to_const_type` | public | — |
| `get_non_const()` | method | `intrusive_ptr_type` | public | — |
| `get_non_const( boost::mpl::true_)` | method | `intrusive_ptr_type` | private | — |
| `get_non_const( boost::mpl::false_)` | method | `intrusive_ptr_type` | private | — |
| `d_value` | field | `intrusive_ptr_type` | private | — |
| `d_shareable` | field | `bool` | private | — |

### `GPlatesUtils::DefaultCopyOnWritePolicy<boost::shared_ptr<T> >`

| Member | Kind | Type | Access | Description |
|---|---|---|---|---|
| `copy( const boost::shared_ptr<T> &value)` | method | `boost::shared_ptr<T>` | public | — |

### `GPlatesUtils::CopyOnWrite<boost::shared_ptr<T>, CopyPolicy>`

| Member | Kind | Type | Access | Description |
|---|---|---|---|---|
| `shared_ptr_type` | typedef | `boost::shared_ptr<T>` | public | — |
| `shared_ptr_to_const_type` | typedef | `boost::shared_ptr<const T>` | public | — |
| `CopyOnWrite( const shared_ptr_type &value)` | method | `None` | public | — |
| `CopyOnWrite( const CopyOnWrite &other)` | method | `None` | public | — |
| `get()` | method | `shared_ptr_to_const_type` | public | — |
| `get_const()` | method | `shared_ptr_to_const_type` | public | — |
| `get_non_const()` | method | `shared_ptr_type` | public | — |
| `get_non_const( boost::mpl::true_)` | method | `shared_ptr_type` | private | — |
| `get_non_const( boost::mpl::false_)` | method | `shared_ptr_type` | private | — |
| `d_value` | field | `shared_ptr_type` | private | — |
| `d_shareable` | field | `bool` | private | — |

## Free functions and macros

| Name | Kind | Type / body | Description |
|---|---|---|---|
| `GPLATES_UTILS_COPYONWRITEPOINTER_H` | macro | `None` | — |

## Notes

Wrapped types must implement a `clone()` method returning the same smart pointer type; the default policies call this to create independent copies. When the template parameter is `const` (e.g., `non_null_intrusive_ptr<const T>`), the wrapper does not perform copy-on-write since the pointed-to object is immutable. The wrapper is not thread-safe; concurrent calls to `get_non_const()` on different copies may race on reference counting. Assignment uses the copy-and-swap idiom, making it exception-safe.

## Used by

*Nothing in the tree references this unit.*

## Related

*None.*

## Explore

Run these from the `gplates-code` skill directory:

```bash
python scripts/gpq.py file src/utils/CopyOnWrite.h
python scripts/gpq.py def GPlatesUtils::CopyOnWrite<non_null_intrusive_ptr<T,H>, CopyPolicy> --body
python scripts/gpq.py uses CopyOnWrite<non_null_intrusive_ptr<T,H>, CopyPolicy> --kind class
python scripts/gpq.py hier CopyOnWrite<non_null_intrusive_ptr<T,H>, CopyPolicy>
```
