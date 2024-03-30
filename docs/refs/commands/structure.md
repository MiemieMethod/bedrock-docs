# `/structure`

> 文档版本：1.20.80.24

`/structure`命令Saves or loads a structure in the world.

/// settings | 执行条件
该命令需要权限等级：`gamedirectors`|`1`。该命令需要开启作弊。
///

## 用法

/// tab | 重载1
```mcfunction
/structure save <name:string> <from:x y z> <to:x y z> [saveMode:StructureSaveMode]
```

//// html | div.result
///// define
`action`: <!-- md:samp StructureSaveAction -->

- 枚举类型。单值枚举，请直接使用`save`。

`name`: <!-- md:samp string -->

- 基本类型。

`from`: <!-- md:samp x y z -->

- 基本类型。

`to`: <!-- md:samp x y z -->

- 基本类型。

`saveMode`: <!-- md:samp StructureSaveMode -->

- 枚举类型。枚举值如下：

|值|描述|
|---|---|
|`disk`||
|`memory`||



/////

////

///

/// tab | 重载2
```mcfunction
/structure save <name:string> <from:x y z> <to:x y z> [includeEntities:Boolean] [saveMode:StructureSaveMode] [includeBlocks:Boolean]
```

//// html | div.result
///// define
`action`: <!-- md:samp StructureSaveAction -->

- 枚举类型。单值枚举，请直接使用`save`。

`name`: <!-- md:samp string -->

- 基本类型。

`from`: <!-- md:samp x y z -->

- 基本类型。

`to`: <!-- md:samp x y z -->

- 基本类型。

`includeEntities`: <!-- md:samp Boolean -->

- 枚举类型。枚举值如下：

|值|描述|
|---|---|
|`true`||
|`false`||


`saveMode`: <!-- md:samp StructureSaveMode -->

- 枚举类型。枚举值如下：

|值|描述|
|---|---|
|`disk`||
|`memory`||


`includeBlocks`: <!-- md:samp Boolean -->

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
/structure delete <name:string>
```

//// html | div.result
///// define
`action`: <!-- md:samp StructureDeleteAction -->

- 枚举类型。单值枚举，请直接使用`delete`。

`name`: <!-- md:samp string -->

- 基本类型。


/////

////

///

/// tab | 重载6
```mcfunction
/structure load <name:string> <to:x y z> [rotation:Rotation] [mirror:Mirror] [includeEntities:Boolean] [includeBlocks:Boolean] [waterlogged:Boolean] [integrity:float] [seed:string]
```

//// html | div.result
///// define
`action`: <!-- md:samp StructureLoadAction -->

- 枚举类型。单值枚举，请直接使用`load`。

`name`: <!-- md:samp string -->

- 基本类型。

`to`: <!-- md:samp x y z -->

- 基本类型。

`rotation`: <!-- md:samp Rotation -->

- 枚举类型。枚举值如下：

|值|描述|
|---|---|
|`0_degrees`||
|`90_degrees`||
|`180_degrees`||
|`270_degrees`||


`mirror`: <!-- md:samp Mirror -->

- 枚举类型。枚举值如下：

|值|描述|
|---|---|
|`x`||
|`z`||
|`none`||
|`xz`||


`includeEntities`: <!-- md:samp Boolean -->

- 枚举类型。枚举值如下：

|值|描述|
|---|---|
|`true`||
|`false`||


`includeBlocks`: <!-- md:samp Boolean -->

- 枚举类型。枚举值如下：

|值|描述|
|---|---|
|`true`||
|`false`||


`waterlogged`: <!-- md:samp Boolean -->

- 枚举类型。枚举值如下：

|值|描述|
|---|---|
|`true`||
|`false`||


`integrity`: <!-- md:samp float -->

- 基本类型。

`seed`: <!-- md:samp string -->

- 基本类型。


/////

////

///

/// tab | 重载7
```mcfunction
/structure load <name:string> <to:x y z> [rotation:Rotation] [mirror:Mirror] [animationMode:StructureAnimationMode] [animationSeconds:float] [includeEntities:Boolean] [includeBlocks:Boolean] [waterlogged:Boolean] [integrity:float] [seed:string]
```

//// html | div.result
///// define
`action`: <!-- md:samp StructureLoadAction -->

- 枚举类型。单值枚举，请直接使用`load`。

`name`: <!-- md:samp string -->

- 基本类型。

`to`: <!-- md:samp x y z -->

- 基本类型。

`rotation`: <!-- md:samp Rotation -->

- 枚举类型。枚举值如下：

|值|描述|
|---|---|
|`0_degrees`||
|`90_degrees`||
|`180_degrees`||
|`270_degrees`||


`mirror`: <!-- md:samp Mirror -->

- 枚举类型。枚举值如下：

|值|描述|
|---|---|
|`x`||
|`z`||
|`none`||
|`xz`||


`animationMode`: <!-- md:samp StructureAnimationMode -->

- 枚举类型。枚举值如下：

|值|描述|
|---|---|
|`block_by_block`||
|`layer_by_layer`||


`animationSeconds`: <!-- md:samp float -->

- 基本类型。

`includeEntities`: <!-- md:samp Boolean -->

- 枚举类型。枚举值如下：

|值|描述|
|---|---|
|`true`||
|`false`||


`includeBlocks`: <!-- md:samp Boolean -->

- 枚举类型。枚举值如下：

|值|描述|
|---|---|
|`true`||
|`false`||


`waterlogged`: <!-- md:samp Boolean -->

- 枚举类型。枚举值如下：

|值|描述|
|---|---|
|`true`||
|`false`||


`integrity`: <!-- md:samp float -->

- 基本类型。

`seed`: <!-- md:samp string -->

- 基本类型。


/////

////

///
