# `/volumearea`

> 文档版本：1.20.80.24

`/volumearea`命令Add, remove, or list volumes in the current dimension.

/// note | 执行条件
该命令需要权限等级：`gamedirectors`|`1`。该命令需要开启作弊。
///

## 用法

/// tab | `重载1`
```mcfunction
/volumearea add <identifier:string> <from:x y z> <to:x y z> [name:string]
```

//// html | div.result
///// define
`mode`: <!-- md:samp VolumeAreaAdd -->

- 枚举类型。枚举值如下：

|值|描述|
|---|---|
|`add`||


`identifier`: <!-- md:samp string -->

- 基本类型。

`from`: <!-- md:samp x y z -->

- 基本类型。

`to`: <!-- md:samp x y z -->

- 基本类型。

`name`: <!-- md:samp string -->

- 基本类型。


/////

////

///

/// tab | `重载2`
```mcfunction
/volumearea remove <name:string>
```

//// html | div.result
///// define
`mode`: <!-- md:samp VolumeAreaRemove -->

- 枚举类型。枚举值如下：

|值|描述|
|---|---|
|`remove`||


`name`: <!-- md:samp string -->

- 基本类型。


/////

////

///

/// tab | `重载3`
```mcfunction
/volumearea remove <position:x y z>
```

//// html | div.result
///// define
`mode`: <!-- md:samp VolumeAreaRemove -->

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
/volumearea remove_all
```

//// html | div.result
///// define
`mode`: <!-- md:samp VolumeAreaRemoveAll -->

- 枚举类型。枚举值如下：

|值|描述|
|---|---|
|`remove_all`||



/////

////

///

/// tab | `重载5`
```mcfunction
/volumearea list all-dimensions
```

//// html | div.result
///// define
`mode`: <!-- md:samp VolumeAreaList -->

- 枚举类型。枚举值如下：

|值|描述|
|---|---|
|`list`||


`all-dimensions`: <!-- md:samp VolumeAreaAllDimensions -->

- 枚举类型。枚举值如下：

|值|描述|
|---|---|
|`all-dimensions`||



/////

////

///
