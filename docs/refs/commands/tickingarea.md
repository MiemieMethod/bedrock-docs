# /tickingarea

> 文档版本：1.20.80.24

`/tickingarea`命令Add, remove, or list ticking areas.

/// note | 执行条件
该命令需要权限等级：`gamedirectors`|`1`。该命令需要开启作弊。
///

## 用法

/// tab | `重载1`
```mcfunction
/tickingarea add <from:x y z> <to:x y z> [name:string] [preload:Boolean]
```

//// html | div.result
///// define
`mode`: <!-- md:samp TickingAreaModeAdd -->

- 枚举类型。枚举值如下：

|值|描述|
|---|---|
|`add`||


`from`: <!-- md:samp x y z -->

- 基本类型。

`to`: <!-- md:samp x y z -->

- 基本类型。

`name`: <!-- md:samp string -->

- 基本类型。

`preload`: <!-- md:samp Boolean -->

- 枚举类型。枚举值如下：

|值|描述|
|---|---|
|`true`||
|`false`||



/////

////

///

/// tab | `重载2`
```mcfunction
/tickingarea add circle <center:x y z> <radius:int> [name:string] [preload:Boolean]
```

//// html | div.result
///// define
`mode`: <!-- md:samp TickingAreaModeAdd -->

- 枚举类型。枚举值如下：

|值|描述|
|---|---|
|`add`||


`circle`: <!-- md:samp AddTickingAreaType -->

- 枚举类型。枚举值如下：

|值|描述|
|---|---|
|`circle`||


`center`: <!-- md:samp x y z -->

- 基本类型。

`radius`: <!-- md:samp int -->

- 基本类型。

`name`: <!-- md:samp string -->

- 基本类型。

`preload`: <!-- md:samp Boolean -->

- 枚举类型。枚举值如下：

|值|描述|
|---|---|
|`true`||
|`false`||



/////

////

///

/// tab | `重载3`
```mcfunction
/tickingarea remove <position:x y z>
```

//// html | div.result
///// define
`mode`: <!-- md:samp TickingAreaModeRemove -->

- 枚举类型。枚举值如下：

|值|描述|
|---|---|
|`remove`||


`position`: <!-- md:samp x y z -->

- 基本类型。


/////

////

///

/// tab | `重载4`
```mcfunction
/tickingarea remove <name:string>
```

//// html | div.result
///// define
`mode`: <!-- md:samp TickingAreaModeRemove -->

- 枚举类型。枚举值如下：

|值|描述|
|---|---|
|`remove`||


`name`: <!-- md:samp string -->

- 基本类型。


/////

////

///

/// tab | `重载5`
```mcfunction
/tickingarea remove_all
```

//// html | div.result
///// define
`mode`: <!-- md:samp TickingAreaModeRemoveAll -->

- 枚举类型。枚举值如下：

|值|描述|
|---|---|
|`remove_all`||



/////

////

///

/// tab | `重载6`
```mcfunction
/tickingarea list all-dimensions
```

//// html | div.result
///// define
`mode`: <!-- md:samp TickingAreaModeList -->

- 枚举类型。枚举值如下：

|值|描述|
|---|---|
|`list`||


`all-dimensions`: <!-- md:samp AllDimensions -->

- 枚举类型。枚举值如下：

|值|描述|
|---|---|
|`all-dimensions`||



/////

////

///

/// tab | `重载7`
```mcfunction
/tickingarea preload <position:x y z> [preload:Boolean]
```

//// html | div.result
///// define
`mode`: <!-- md:samp TickingAreaModePreload -->

- 枚举类型。枚举值如下：

|值|描述|
|---|---|
|`preload`||


`position`: <!-- md:samp x y z -->

- 基本类型。

`preload`: <!-- md:samp Boolean -->

- 枚举类型。枚举值如下：

|值|描述|
|---|---|
|`true`||
|`false`||



/////

////

///

/// tab | `重载8`
```mcfunction
/tickingarea preload <name:string> [preload:Boolean]
```

//// html | div.result
///// define
`mode`: <!-- md:samp TickingAreaModePreload -->

- 枚举类型。枚举值如下：

|值|描述|
|---|---|
|`preload`||


`name`: <!-- md:samp string -->

- 基本类型。

`preload`: <!-- md:samp Boolean -->

- 枚举类型。枚举值如下：

|值|描述|
|---|---|
|`true`||
|`false`||



/////

////

///
