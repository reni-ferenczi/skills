# ScopeGuard

[Book TOC](../../../TOC.md) · [system-fixes](../../../components/system-fixes.md) · cluster Community 123 · tier 2

| Source file | Kind | Lines |
|---|---|---|
| `src/system-fixes/loki/ScopeGuard.h` | C++ | 382 |

## Overview

This header is a vendored piece of the Loki library implementing the "scope guard" idiom: an RAII object that runs a stored cleanup action on destruction unless explicitly told not to, giving exception-safe rollback of partially completed work without hand-written `try`/`catch` scaffolding. `Loki::ScopeGuardImplBase` holds the dismissed flag and drives cleanup through `SafeExecute`, a protected static template that calls the derived guard's `Execute()` and swallows any exception thrown while doing so, so a guard destructor never throws out of stack unwinding already in progress. `ScopeGuardImpl0` through `ScopeGuardImpl3` specialize this base to call a free function or callable bound to zero to three extra arguments, and `ObjScopeGuardImpl0` through `ObjScopeGuardImpl2` do the same for a member function invoked on a referenced object.

Guards are never constructed directly: the `MakeGuard`/`MakeObjGuard` overload sets pick the right template for the argument count and callable shape, and the result is meant to be bound to the `Loki::ScopeGuard` typedef (a `const` reference to `ScopeGuardImplBase`), not stored by value. `LOKI_ON_BLOCK_EXIT` and `LOKI_ON_BLOCK_EXIT_OBJ` wrap that pattern into a one-line macro that declares an anonymous, uniquely-named guard variable for the common "run this at the end of the current block" case.

## Declared types

| Name | Kind | Bases | Template | Subclasses | Description |
|---|---|---|---|---|---|
| [`Loki::ScopeGuardImplBase`](#lokiscopeguardimplbase) | class | — | — | 7 | — |
| [`Loki::ScopeGuard`](#lokiscopeguard) | typedef | — | — | 0 | \\typedef typedef const ScopeGuardImplBase& ScopeGuard ExceptionGroup See Andrei's and Petru Marginean's CUJ article http://www.cuj.com/documents/s=8000/cujcexp1812alexandr/alexandr.htm Changes to the original code by Joshua Lehrer: ... |
| [`Loki::ScopeGuardImpl0`](#lokiscopeguardimpl0) | class | [`ScopeGuardImplBase`](ScopeGuard.md) | `<typename F>` | 0 | — |
| [`Loki::ScopeGuardImpl1`](#lokiscopeguardimpl1) | class | [`ScopeGuardImplBase`](ScopeGuard.md) | `<typename F, typename P1>` | 0 | — |
| [`Loki::ScopeGuardImpl2`](#lokiscopeguardimpl2) | class | [`ScopeGuardImplBase`](ScopeGuard.md) | `<typename F, typename P1, typename P2>` | 0 | — |
| [`Loki::ScopeGuardImpl3`](#lokiscopeguardimpl3) | class | [`ScopeGuardImplBase`](ScopeGuard.md) | `<typename F, typename P1, typename P2, typename P3>` | 0 | — |
| [`Loki::ObjScopeGuardImpl0`](#lokiobjscopeguardimpl0) | class | [`ScopeGuardImplBase`](ScopeGuard.md) | `<class Obj, typename MemFun>` | 0 | — |
| [`Loki::ObjScopeGuardImpl1`](#lokiobjscopeguardimpl1) | class | [`ScopeGuardImplBase`](ScopeGuard.md) | `<class Obj, typename MemFun, typename P1>` | 0 | — |
| [`Loki::ObjScopeGuardImpl2`](#lokiobjscopeguardimpl2) | class | [`ScopeGuardImplBase`](ScopeGuard.md) | `<class Obj, typename MemFun, typename P1, typename P2>` | 0 | — |

## Members

### `Loki::ScopeGuardImplBase`

| Member | Kind | Type | Access | Description |
|---|---|---|---|---|
| `operator =` | field | `ScopeGuardImplBase` | private | — |
| `~ScopeGuardImplBase()` | destructor | `None` | protected | — |
| `ScopeGuardImplBase(const ScopeGuardImplBase& other)` | constructor | `None` | protected | — |
| `SafeExecute(J& j)` | method | `void` | protected | — |
| `dismissed_` | field | `bool` | protected | — |
| `ScopeGuardImplBase()` | constructor | `None` | public | — |
| `Dismiss()` | method | `void` | public | — |
| `silence_unused_variable_warning()` | method | `void` | public | Calling this avoids the 'unused variable' warning on some compilers. |

### `Loki::ScopeGuard`

*None.*

### `Loki::ScopeGuardImpl0`

| Member | Kind | Type | Access | Description |
|---|---|---|---|---|
| `MakeGuard(F fun)` | method | `ScopeGuardImpl0<F>` | public | — |
| `~ScopeGuardImpl0()` | destructor | `None` | public | — |
| `Execute()` | method | `void` | public | — |
| `ScopeGuardImpl0(F fun)` | constructor | `None` | protected | — |
| `fun_` | field | `F` | protected | — |

### `Loki::ScopeGuardImpl1`

| Member | Kind | Type | Access | Description |
|---|---|---|---|---|
| `MakeGuard(F fun, P1 p1)` | method | `ScopeGuardImpl1<F, P1>` | public | — |
| `~ScopeGuardImpl1()` | destructor | `None` | public | — |
| `Execute()` | method | `void` | public | — |
| `ScopeGuardImpl1(F fun, P1 p1)` | constructor | `None` | protected | — |
| `fun_` | field | `F` | protected | — |
| `p1_` | field | `P1` | protected | — |

### `Loki::ScopeGuardImpl2`

| Member | Kind | Type | Access | Description |
|---|---|---|---|---|
| `MakeGuard(F fun, P1 p1, P2 p2)` | method | `ScopeGuardImpl2<F, P1, P2>` | public | — |
| `~ScopeGuardImpl2()` | destructor | `None` | public | — |
| `Execute()` | method | `void` | public | — |
| `ScopeGuardImpl2(F fun, P1 p1, P2 p2)` | constructor | `None` | protected | — |
| `fun_` | field | `F` | protected | — |
| `p1_` | field | `P1` | protected | — |
| `p2_` | field | `P2` | protected | — |

### `Loki::ScopeGuardImpl3`

| Member | Kind | Type | Access | Description |
|---|---|---|---|---|
| `MakeGuard(F fun, P1 p1, P2 p2, P3 p3)` | method | `ScopeGuardImpl3<F, P1, P2, P3>` | public | — |
| `~ScopeGuardImpl3()` | destructor | `None` | public | — |
| `Execute()` | method | `void` | public | — |
| `ScopeGuardImpl3(F fun, P1 p1, P2 p2, P3 p3)` | constructor | `None` | protected | — |
| `fun_` | field | `F` | protected | — |
| `p1_` | field | `P1` | protected | — |
| `p2_` | field | `P2` | protected | — |
| `p3_` | field | `P3` | protected | — |

### `Loki::ObjScopeGuardImpl0`

| Member | Kind | Type | Access | Description |
|---|---|---|---|---|
| `MakeObjGuard(Obj& obj, MemFun memFun)` | method | `ObjScopeGuardImpl0<Obj, MemFun>` | public | — |
| `~ObjScopeGuardImpl0()` | destructor | `None` | public | — |
| `Execute()` | method | `void` | public | — |
| `ObjScopeGuardImpl0(Obj& obj, MemFun memFun)` | constructor | `None` | protected | — |
| `obj_` | field | `Obj` | protected | — |
| `memFun_` | field | `MemFun` | protected | — |

### `Loki::ObjScopeGuardImpl1`

| Member | Kind | Type | Access | Description |
|---|---|---|---|---|
| `MakeObjGuard(Obj& obj, MemFun memFun, P1 p1)` | method | `ObjScopeGuardImpl1<Obj, MemFun, P1>` | public | — |
| `~ObjScopeGuardImpl1()` | destructor | `None` | public | — |
| `Execute()` | method | `void` | public | — |
| `ObjScopeGuardImpl1(Obj& obj, MemFun memFun, P1 p1)` | constructor | `None` | protected | — |
| `obj_` | field | `Obj` | protected | — |
| `memFun_` | field | `MemFun` | protected | — |
| `p1_` | field | `P1` | protected | — |

### `Loki::ObjScopeGuardImpl2`

| Member | Kind | Type | Access | Description |
|---|---|---|---|---|
| `MakeObjGuard(Obj& obj, MemFun memFun, P1 p1, P2 p2)` | method | `ObjScopeGuardImpl2<Obj, MemFun, P1, P2>` | public | — |
| `~ObjScopeGuardImpl2()` | destructor | `None` | public | — |
| `Execute()` | method | `void` | public | — |
| `ObjScopeGuardImpl2(Obj& obj, MemFun memFun, P1 p1, P2 p2)` | constructor | `None` | protected | — |
| `obj_` | field | `Obj` | protected | — |
| `memFun_` | field | `MemFun` | protected | — |
| `p1_` | field | `P1` | protected | — |
| `p2_` | field | `P2` | protected | — |

## Free functions and macros

| Name | Kind | Type / body | Description |
|---|---|---|---|
| `LOKI_SCOPEGUARD_H_` | macro | `None` | — |
| `MakeGuard(F fun)` | function | `ScopeGuardImpl0<F>` | — |
| `MakeGuard(F fun, P1 p1)` | function | `ScopeGuardImpl1<F, P1>` | — |
| `MakeGuard(F fun, P1 p1, P2 p2)` | function | `ScopeGuardImpl2<F, P1, P2>` | — |
| `MakeGuard(F fun, P1 p1, P2 p2, P3 p3)` | function | `ScopeGuardImpl3<F, P1, P2, P3>` | — |
| `MakeObjGuard(Obj& obj, MemFun memFun)` | function | `ObjScopeGuardImpl0<Obj, MemFun>` | — |
| `MakeGuard(Ret(Obj2::*memFun)(), Obj1 &obj)` | function | `ObjScopeGuardImpl0<Obj1,Ret(Obj2::*)()>` | — |
| `MakeGuard(Ret(Obj2::*memFun)(), Obj1 *obj)` | function | `ObjScopeGuardImpl0<Obj1,Ret(Obj2::*)()>` | — |
| `MakeObjGuard(Obj& obj, MemFun memFun, P1 p1)` | function | `ObjScopeGuardImpl1<Obj, MemFun, P1>` | — |
| `MakeGuard(Ret(Obj2::*memFun)(P1a), Obj1 &obj, P1b p1)` | function | `ObjScopeGuardImpl1<Obj1,Ret(Obj2::*)(P1a),P1b>` | — |
| `MakeGuard(Ret(Obj2::*memFun)(P1a), Obj1 *obj, P1b p1)` | function | `ObjScopeGuardImpl1<Obj1,Ret(Obj2::*)(P1a),P1b>` | — |
| `MakeObjGuard(Obj& obj, MemFun memFun, P1 p1, P2 p2)` | function | `ObjScopeGuardImpl2<Obj, MemFun, P1, P2>` | — |
| `MakeGuard(Ret(Obj2::*memFun)(P1a,P2a), Obj1 &obj, P1b p1, P2b p2)` | function | `ObjScopeGuardImpl2<Obj1,Ret(Obj2::*)(P1a,P2a),P1b,P2b>` | — |
| `MakeGuard(Ret(Obj2::*memFun)(P1a,P2a), Obj1 *obj, P1b p1, P2b p2)` | function | `ObjScopeGuardImpl2<Obj1,Ret(Obj2::*)(P1a,P2a),P1b,P2b>` | — |
| `LOKI_CONCATENATE_DIRECT` | macro_function | `s1##s2` | — |
| `LOKI_CONCATENATE` | macro_function | `LOKI_CONCATENATE_DIRECT(s1, s2)` | — |
| `LOKI_ANONYMOUS_VARIABLE` | macro_function | `LOKI_CONCATENATE(str, __LINE__)` | — |
| `LOKI_ON_BLOCK_EXIT` | macro | `Loki::ScopeGuard LOKI_ANONYMOUS_VARIABLE(scopeGuard) = Loki::MakeGuard` | — |
| `LOKI_ON_BLOCK_EXIT_OBJ` | macro | `Loki::ScopeGuard LOKI_ANONYMOUS_VARIABLE(scopeGuard) = Loki::MakeObjGuard` | — |

## Notes

- A guard must be bound to `Loki::ScopeGuard` (a reference) rather than copied or stored by value: `ScopeGuardImplBase`'s copy constructor dismisses the source, transferring cleanup responsibility to the copy, so copying a guard elsewhere silently disarms the original.
- `SafeExecute` swallows every exception thrown by `Execute()`; a failure during rollback is discarded rather than reported, so cleanup actions that can fail should not rely on the guard to surface that failure.
- `dismissed_` is `mutable` and `Dismiss()` is `const`, so a guard held through a `const Loki::ScopeGuard` reference can still be dismissed.

## Used by

| Unit | Component | References |
|---|---|---|
| [utils/KeyValueCache](../../utils/KeyValueCache.md) | utils | 10 |
| [utils/ObjectPool](../../utils/ObjectPool.md) | utils | 4 |
| [file-io/PlatesRotationFormatReader](../../file-io/PlatesRotationFormatReader.md) | file-io | 1 |

## Related

*None.*

## Explore

Run these from the `gplates-code` skill directory:

```bash
python scripts/gpq.py file src/system-fixes/loki/ScopeGuard.h
python scripts/gpq.py def Loki::ScopeGuardImplBase --body
python scripts/gpq.py uses ScopeGuardImplBase --kind class
python scripts/gpq.py hier ScopeGuardImplBase
```
