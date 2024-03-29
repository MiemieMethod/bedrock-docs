# `/teleport`

> 文档版本：1.20.80.24

`/teleport`命令Teleports entities (players, mobs, etc.).

/// note | 执行条件
该命令需要权限等级：`gamedirectors`|`1`。该命令需要开启作弊。
///

## 用法

/// tab | 重载1
```mcfunction
/teleport <destination:x y z> [checkForBlocks:Boolean]
```

//// html | div.result
///// define
`destination`: <!-- md:samp x y z -->

- 基本类型。

`checkForBlocks`: <!-- md:samp Boolean -->

- 枚举类型。枚举值如下：

|值|描述|
|---|---|
|`true`||
|`false`||



/////

////

///

/// tab | 重载2
```mcfunction
/teleport <destination:x y z> [yRot:value] [xRot:value] [checkForBlocks:Boolean]
```

//// html | div.result
///// define
`destination`: <!-- md:samp x y z -->

- 基本类型。

`yRot`: <!-- md:samp value -->

- 基本类型。

`xRot`: <!-- md:samp value -->

- 基本类型。

`checkForBlocks`: <!-- md:samp Boolean -->

- 枚举类型。枚举值如下：

|值|描述|
|---|---|
|`true`||
|`false`||



/////

////

///

/// tab | 重载3
```mcfunction
/teleport <destination:x y z> facing <lookAtPosition:x y z> [checkForBlocks:Boolean]
```

//// html | div.result
///// define
`destination`: <!-- md:samp x y z -->

- 基本类型。

`facing`: <!-- md:samp TeleportFacing -->

- 枚举类型。枚举值如下：

|值|描述|
|---|---|
|`facing`||


`lookAtPosition`: <!-- md:samp x y z -->

- 基本类型。

`checkForBlocks`: <!-- md:samp Boolean -->

- 枚举类型。枚举值如下：

|值|描述|
|---|---|
|`true`||
|`false`||



/////

////

///

/// tab | 重载4
```mcfunction
/teleport <destination:x y z> facing <lookAtEntity:target> [checkForBlocks:Boolean]
```

//// html | div.result
///// define
`destination`: <!-- md:samp x y z -->

- 基本类型。

`facing`: <!-- md:samp TeleportFacing -->

- 枚举类型。枚举值如下：

|值|描述|
|---|---|
|`facing`||


`lookAtEntity`: <!-- md:samp target -->

- 基本类型。

`checkForBlocks`: <!-- md:samp Boolean -->

- 枚举类型。枚举值如下：

|值|描述|
|---|---|
|`true`||
|`false`||



/////

////

///

/// tab | 重载5
```mcfunction
/teleport <victim:target> <destination:x y z> [yRot:value] [xRot:value] [checkForBlocks:Boolean]
```

//// html | div.result
///// define
`victim`: <!-- md:samp target -->

- 基本类型。

`destination`: <!-- md:samp x y z -->

- 基本类型。

`yRot`: <!-- md:samp value -->

- 基本类型。

`xRot`: <!-- md:samp value -->

- 基本类型。

`checkForBlocks`: <!-- md:samp Boolean -->

- 枚举类型。枚举值如下：

|值|描述|
|---|---|
|`true`||
|`false`||



/////

////

///

/// tab | 重载6
```mcfunction
/teleport <victim:target> <destination:x y z> [checkForBlocks:Boolean]
```

//// html | div.result
///// define
`victim`: <!-- md:samp target -->

- 基本类型。

`destination`: <!-- md:samp x y z -->

- 基本类型。

`checkForBlocks`: <!-- md:samp Boolean -->

- 枚举类型。枚举值如下：

|值|描述|
|---|---|
|`true`||
|`false`||



/////

////

///

/// tab | 重载7
```mcfunction
/teleport <victim:target> <destination:x y z> facing <lookAtPosition:x y z> [checkForBlocks:Boolean]
```

//// html | div.result
///// define
`victim`: <!-- md:samp target -->

- 基本类型。

`destination`: <!-- md:samp x y z -->

- 基本类型。

`facing`: <!-- md:samp TeleportFacing -->

- 枚举类型。枚举值如下：

|值|描述|
|---|---|
|`facing`||


`lookAtPosition`: <!-- md:samp x y z -->

- 基本类型。

`checkForBlocks`: <!-- md:samp Boolean -->

- 枚举类型。枚举值如下：

|值|描述|
|---|---|
|`true`||
|`false`||



/////

////

///

/// tab | 重载8
```mcfunction
/teleport <victim:target> <destination:x y z> facing <lookAtEntity:target> [checkForBlocks:Boolean]
```

//// html | div.result
///// define
`victim`: <!-- md:samp target -->

- 基本类型。

`destination`: <!-- md:samp x y z -->

- 基本类型。

`facing`: <!-- md:samp TeleportFacing -->

- 枚举类型。枚举值如下：

|值|描述|
|---|---|
|`facing`||


`lookAtEntity`: <!-- md:samp target -->

- 基本类型。

`checkForBlocks`: <!-- md:samp Boolean -->

- 枚举类型。枚举值如下：

|值|描述|
|---|---|
|`true`||
|`false`||



/////

////

///

/// tab | 重载9
```mcfunction
/teleport <destination:target>
```

//// html | div.result
///// define
`destination`: <!-- md:samp target -->

- 基本类型。


/////

////

///

/// tab | 重载10
```mcfunction
/teleport <victim:target> <destination:target> [checkForBlocks:Boolean]
```

//// html | div.result
///// define
`victim`: <!-- md:samp target -->

- 基本类型。

`destination`: <!-- md:samp target -->

- 基本类型。

`checkForBlocks`: <!-- md:samp Boolean -->

- 枚举类型。枚举值如下：

|值|描述|
|---|---|
|`true`||
|`false`||



/////

////

///
