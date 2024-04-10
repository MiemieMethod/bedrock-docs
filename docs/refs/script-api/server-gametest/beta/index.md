# `@minecraft/server-gametest`

> 文档版本：1.21.0.20

`@minecraft/server-gametest`模块的`1.0.0-beta`版本，UUID为`6f4b6893-1bb6-42fd-b458-7fa3d0c89616`。该模块是script_api.@minecraft/server-gametest.description

/// info | 依赖
该模块依赖于以下模块：

- `@minecraft/common`|`1.0.0`|`77ec12b4-1b2b-4c98-8d34-d1cd63f849d5`
- `@minecraft/server`|`1.8.0`|`b26a4d4c-afdf-4690-88f8-931846312678`
///

## 函数

/// define
`register`


///

script_api.@minecraft/server-gametest.register.description

```js
static register(testClassName: string, testName: string, testFunction: (arg: Test) => void): RegistrationBuilder
```

/// html | div.result
//// define
`testClassName`：`string`

- script_api.@minecraft/server-gametest.register.testclassname.description


////

//// define
`testName`：`string`

- script_api.@minecraft/server-gametest.register.testname.description


////

//// define
`testFunction`：<code>(<a href="./test/">Test</a>) =&gt; void</code>

- script_api.@minecraft/server-gametest.register.testfunction.description


////

//// define
返回值：[`RegistrationBuilder`](./registrationbuilder.md)

- script_api.@minecraft/server-gametest.register.return


////

///


/// define
`registerAsync`


///

script_api.@minecraft/server-gametest.registerasync.description

```js
static registerAsync(testClassName: string, testName: string, testFunction: (arg: Test) => Promise<void>): RegistrationBuilder
```

/// html | div.result
//// define
`testClassName`：`string`

- script_api.@minecraft/server-gametest.registerasync.testclassname.description


////

//// define
`testName`：`string`

- script_api.@minecraft/server-gametest.registerasync.testname.description


////

//// define
`testFunction`：<code>(<a href="./test/">Test</a>) =&gt; Promise<void></code>

- script_api.@minecraft/server-gametest.registerasync.testfunction.description


////

//// define
返回值：[`RegistrationBuilder`](./registrationbuilder.md)

- script_api.@minecraft/server-gametest.registerasync.return


////

///


## 类

|类|描述|
|---|---|
|[`FenceConnectivity`](./fenceconnectivity.md)||
|[`GameTestSequence`](./gametestsequence.md)||
|[`NavigationResult`](./navigationresult.md)||
|[`RegistrationBuilder`](./registrationbuilder.md)||
|[`SculkSpreader`](./sculkspreader.md)||
|[`SimulatedPlayer`](./simulatedplayer.md)||
|[`Tags`](./tags.md)||
|[`Test`](./test.md)||

## 接口

|接口|描述|
|---|---|
|[`GameTestErrorContext`](./gametesterrorcontext.md)||
|[`MoveToOptions`](./movetooptions.md)||

## 枚举

|枚举|描述|
|---|---|
|[`GameTestErrorType`](./gametesterrortype.md)||
|[`LookDuration`](./lookduration.md)||

## 错误

|错误|描述|
|---|---|
|[`GameTestError`](./gametesterror.md)||
