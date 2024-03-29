# `/gametest`

> 文档版本：1.20.80.24

`/gametest`命令Interacts with gametest.

/// note | 执行条件
该命令需要权限等级：`gamedirectors`|`1`。该命令需要开启作弊。
///

## 用法

/// tab | `重载1`
```mcfunction
/gametest runthis
```

//// html | div.result
///// define
`mode`: <!-- md:samp GameTestModeRunThis -->

- 枚举类型。枚举值如下：

|值|描述|
|---|---|
|`runthis`||



/////

////

///

/// tab | `重载2`
```mcfunction
/gametest run <testName:GameTestName> [rotationSteps:int]
```

//// html | div.result
///// define
`mode`: <!-- md:samp GameTestModeRun -->

- 枚举类型。枚举值如下：

|值|描述|
|---|---|
|`run`||


`testName`: <!-- md:samp GameTestName -->

- 基本类型。

`rotationSteps`: <!-- md:samp int -->

- 基本类型。


/////

////

///

/// tab | `重载3`
```mcfunction
/gametest run <testName:GameTestName> <stopOnFailure:Boolean> <repeatCount:int> [rotationSteps:int]
```

//// html | div.result
///// define
`mode`: <!-- md:samp GameTestModeRun -->

- 枚举类型。枚举值如下：

|值|描述|
|---|---|
|`run`||


`testName`: <!-- md:samp GameTestName -->

- 基本类型。

`stopOnFailure`: <!-- md:samp Boolean -->

- 枚举类型。枚举值如下：

|值|描述|
|---|---|
|`true`||
|`false`||


`repeatCount`: <!-- md:samp int -->

- 基本类型。

`rotationSteps`: <!-- md:samp int -->

- 基本类型。


/////

////

///

/// tab | `重载4`
```mcfunction
/gametest runset [tag:GameTestTag] [rotationSteps:int]
```

//// html | div.result
///// define
`mode`: <!-- md:samp GameTestModeRunSet -->

- 枚举类型。枚举值如下：

|值|描述|
|---|---|
|`runset`||


`tag`: <!-- md:samp GameTestTag -->

- 基本类型。

`rotationSteps`: <!-- md:samp int -->

- 基本类型。


/////

////

///

/// tab | `重载5`
```mcfunction
/gametest runsetuntilfail [tag:GameTestTag] [rotationSteps:int]
```

//// html | div.result
///// define
`mode`: <!-- md:samp GameTestModeRunSetUntilFail -->

- 枚举类型。枚举值如下：

|值|描述|
|---|---|
|`runsetuntilfail`||


`tag`: <!-- md:samp GameTestTag -->

- 基本类型。

`rotationSteps`: <!-- md:samp int -->

- 基本类型。


/////

////

///

/// tab | `重载6`
```mcfunction
/gametest clearall
```

//// html | div.result
///// define
`mode`: <!-- md:samp GameTestModeClearAll -->

- 枚举类型。枚举值如下：

|值|描述|
|---|---|
|`clearall`||



/////

////

///

/// tab | `重载7`
```mcfunction
/gametest pos
```

//// html | div.result
///// define
`mode`: <!-- md:samp GameTestModeShowPosition -->

- 枚举类型。枚举值如下：

|值|描述|
|---|---|
|`pos`||



/////

////

///

/// tab | `重载8`
```mcfunction
/gametest create <testName:string> [width:int] [height:int] [depth:int]
```

//// html | div.result
///// define
`mode`: <!-- md:samp GameTestModeCreateTest -->

- 枚举类型。枚举值如下：

|值|描述|
|---|---|
|`create`||


`testName`: <!-- md:samp string -->

- 基本类型。

`width`: <!-- md:samp int -->

- 基本类型。

`height`: <!-- md:samp int -->

- 基本类型。

`depth`: <!-- md:samp int -->

- 基本类型。


/////

////

///

/// tab | `重载9`
```mcfunction
/gametest runthese
```

//// html | div.result
///// define
`mode`: <!-- md:samp GameTestRunNearbyTests -->

- 枚举类型。枚举值如下：

|值|描述|
|---|---|
|`runthese`||



/////

////

///

/// tab | `重载10`
```mcfunction
/gametest stopall
```

//// html | div.result
///// define
`mode`: <!-- md:samp GameTestStopTests -->

- 枚举类型。枚举值如下：

|值|描述|
|---|---|
|`stopall`||



/////

////

///
