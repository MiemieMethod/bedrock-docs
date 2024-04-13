# `/structure`

> 文档版本：1.21.0.21

`/structure`命令command.structure.description

/// settings | 执行条件
该命令需要权限等级：`gamedirectors`|`1`。该命令需要开启作弊。
///

## 用法

/// tab | 重载1
```mcfunction
/structure save <name:string> <from:x y z> <to:x y z> [saveMode:StructureSaveMode]
```

//// html | div.result
command.structure.1.description

///// define
`action`：<!-- md:samp StructureSaveAction -->

- 枚举类型。command.enum.structuresaveaction.description单值枚举，请直接使用`save`。

`name`：<!-- md:samp string -->

- 基本类型。command.structure.name.description

`from`：<!-- md:samp x y z -->

- 基本类型。command.structure.from.description

`to`：<!-- md:samp x y z -->

- 基本类型。command.structure.to.description

`saveMode`：<!-- md:samp StructureSaveMode -->

- 枚举类型，可选。command.enum.structuresavemode.description枚举值如下：

  |值|描述|
  |---|---|
  |`disk`|command.enum.structuresavemode.disk|
  |`memory`|command.enum.structuresavemode.memory|



/////

////

///

/// tab | 重载2
```mcfunction
/structure save <name:string> <from:x y z> <to:x y z> [includeEntities:Boolean] [saveMode:StructureSaveMode] [includeBlocks:Boolean]
```

//// html | div.result
command.structure.2.description

///// define
`action`：<!-- md:samp StructureSaveAction -->

- 枚举类型。command.enum.structuresaveaction.description单值枚举，请直接使用`save`。

`name`：<!-- md:samp string -->

- 基本类型。command.structure.name.description

`from`：<!-- md:samp x y z -->

- 基本类型。command.structure.from.description

`to`：<!-- md:samp x y z -->

- 基本类型。command.structure.to.description

`includeEntities`：<!-- md:samp Boolean -->

- 枚举类型，可选。command.enum.boolean.description枚举值如下：

  |值|描述|
  |---|---|
  |`true`|是|
  |`false`|否|


`saveMode`：<!-- md:samp StructureSaveMode -->

- 枚举类型，可选。command.enum.structuresavemode.description枚举值如下：

  |值|描述|
  |---|---|
  |`disk`|command.enum.structuresavemode.disk|
  |`memory`|command.enum.structuresavemode.memory|


`includeBlocks`：<!-- md:samp Boolean -->

- 枚举类型，可选。command.enum.boolean.description枚举值如下：

  |值|描述|
  |---|---|
  |`true`|是|
  |`false`|否|



/////

////

///

/// tab | 重载3
```mcfunction
/structure delete <name:string>
```

//// html | div.result
command.structure.3.description

///// define
`action`：<!-- md:samp StructureDeleteAction -->

- 枚举类型。command.enum.structuredeleteaction.description单值枚举，请直接使用`delete`。

`name`：<!-- md:samp string -->

- 基本类型。command.structure.name.description


/////

////

///

/// tab | 重载4
```mcfunction
/structure load <name:string> <to:x y z> [rotation:Rotation] [mirror:Mirror] [includeEntities:Boolean] [includeBlocks:Boolean] [integrity:float] [seed:string]
```

//// html | div.result
<!-- md:version command * 21 true true -->
command.structure.4.description

///// define
`action`：<!-- md:samp StructureLoadAction -->

- 枚举类型。command.enum.structureloadaction.description单值枚举，请直接使用`load`。

`name`：<!-- md:samp string -->

- 基本类型。command.structure.name.description

`to`：<!-- md:samp x y z -->

- 基本类型。command.structure.to.description

`rotation`：<!-- md:samp Rotation -->

- 枚举类型，可选。command.enum.rotation.description枚举值如下：

  |值|描述|
  |---|---|
  |`0_degrees`|command.enum.rotation.0_degrees|
  |`90_degrees`|command.enum.rotation.90_degrees|
  |`180_degrees`|command.enum.rotation.180_degrees|
  |`270_degrees`|command.enum.rotation.270_degrees|


`mirror`：<!-- md:samp Mirror -->

- 枚举类型，可选。command.enum.mirror.description枚举值如下：

  |值|描述|
  |---|---|
  |`x`|command.enum.mirror.x|
  |`z`|command.enum.mirror.z|
  |`none`|command.enum.mirror.none|
  |`xz`|command.enum.mirror.xz|


`includeEntities`：<!-- md:samp Boolean -->

- 枚举类型，可选。command.enum.boolean.description枚举值如下：

  |值|描述|
  |---|---|
  |`true`|是|
  |`false`|否|


`includeBlocks`：<!-- md:samp Boolean -->

- 枚举类型，可选。command.enum.boolean.description枚举值如下：

  |值|描述|
  |---|---|
  |`true`|是|
  |`false`|否|


`integrity`：<!-- md:samp float -->

- 基本类型，可选。command.structure.integrity.description

`seed`：<!-- md:samp string -->

- 基本类型，可选。command.structure.seed.description


/////

////

///

/// tab | 重载5
```mcfunction
/structure load <name:string> <to:x y z> [rotation:Rotation] [mirror:Mirror] [animationMode:StructureAnimationMode] [animationSeconds:float] [includeEntities:Boolean] [includeBlocks:Boolean] [integrity:float] [seed:string]
```

//// html | div.result
<!-- md:version command * 21 true true -->
command.structure.5.description

///// define
`action`：<!-- md:samp StructureLoadAction -->

- 枚举类型。command.enum.structureloadaction.description单值枚举，请直接使用`load`。

`name`：<!-- md:samp string -->

- 基本类型。command.structure.name.description

`to`：<!-- md:samp x y z -->

- 基本类型。command.structure.to.description

`rotation`：<!-- md:samp Rotation -->

- 枚举类型，可选。command.enum.rotation.description枚举值如下：

  |值|描述|
  |---|---|
  |`0_degrees`|command.enum.rotation.0_degrees|
  |`90_degrees`|command.enum.rotation.90_degrees|
  |`180_degrees`|command.enum.rotation.180_degrees|
  |`270_degrees`|command.enum.rotation.270_degrees|


`mirror`：<!-- md:samp Mirror -->

- 枚举类型，可选。command.enum.mirror.description枚举值如下：

  |值|描述|
  |---|---|
  |`x`|command.enum.mirror.x|
  |`z`|command.enum.mirror.z|
  |`none`|command.enum.mirror.none|
  |`xz`|command.enum.mirror.xz|


`animationMode`：<!-- md:samp StructureAnimationMode -->

- 枚举类型，可选。command.enum.structureanimationmode.description枚举值如下：

  |值|描述|
  |---|---|
  |`block_by_block`|command.enum.structureanimationmode.block_by_block|
  |`layer_by_layer`|command.enum.structureanimationmode.layer_by_layer|


`animationSeconds`：<!-- md:samp float -->

- 基本类型，可选。command.structure.animationSeconds.description

`includeEntities`：<!-- md:samp Boolean -->

- 枚举类型，可选。command.enum.boolean.description枚举值如下：

  |值|描述|
  |---|---|
  |`true`|是|
  |`false`|否|


`includeBlocks`：<!-- md:samp Boolean -->

- 枚举类型，可选。command.enum.boolean.description枚举值如下：

  |值|描述|
  |---|---|
  |`true`|是|
  |`false`|否|


`integrity`：<!-- md:samp float -->

- 基本类型，可选。command.structure.integrity.description

`seed`：<!-- md:samp string -->

- 基本类型，可选。command.structure.seed.description


/////

////

///

/// tab | 重载6
```mcfunction
/structure load <name:string> <to:x y z> [rotation:Rotation] [mirror:Mirror] [includeEntities:Boolean] [includeBlocks:Boolean] [waterlogged:Boolean] [integrity:float] [seed:string]
```

//// html | div.result
<!-- md:version command 22 * true true -->
command.structure.6.description

///// define
`action`：<!-- md:samp StructureLoadAction -->

- 枚举类型。command.enum.structureloadaction.description单值枚举，请直接使用`load`。

`name`：<!-- md:samp string -->

- 基本类型。command.structure.name.description

`to`：<!-- md:samp x y z -->

- 基本类型。command.structure.to.description

`rotation`：<!-- md:samp Rotation -->

- 枚举类型，可选。command.enum.rotation.description枚举值如下：

  |值|描述|
  |---|---|
  |`0_degrees`|command.enum.rotation.0_degrees|
  |`90_degrees`|command.enum.rotation.90_degrees|
  |`180_degrees`|command.enum.rotation.180_degrees|
  |`270_degrees`|command.enum.rotation.270_degrees|


`mirror`：<!-- md:samp Mirror -->

- 枚举类型，可选。command.enum.mirror.description枚举值如下：

  |值|描述|
  |---|---|
  |`x`|command.enum.mirror.x|
  |`z`|command.enum.mirror.z|
  |`none`|command.enum.mirror.none|
  |`xz`|command.enum.mirror.xz|


`includeEntities`：<!-- md:samp Boolean -->

- 枚举类型，可选。command.enum.boolean.description枚举值如下：

  |值|描述|
  |---|---|
  |`true`|是|
  |`false`|否|


`includeBlocks`：<!-- md:samp Boolean -->

- 枚举类型，可选。command.enum.boolean.description枚举值如下：

  |值|描述|
  |---|---|
  |`true`|是|
  |`false`|否|


`waterlogged`：<!-- md:samp Boolean -->

- 枚举类型，可选。command.enum.boolean.description枚举值如下：

  |值|描述|
  |---|---|
  |`true`|是|
  |`false`|否|


`integrity`：<!-- md:samp float -->

- 基本类型，可选。command.structure.integrity.description

`seed`：<!-- md:samp string -->

- 基本类型，可选。command.structure.seed.description


/////

////

///

/// tab | 重载7
```mcfunction
/structure load <name:string> <to:x y z> [rotation:Rotation] [mirror:Mirror] [animationMode:StructureAnimationMode] [animationSeconds:float] [includeEntities:Boolean] [includeBlocks:Boolean] [waterlogged:Boolean] [integrity:float] [seed:string]
```

//// html | div.result
<!-- md:version command 22 * true true -->
command.structure.7.description

///// define
`action`：<!-- md:samp StructureLoadAction -->

- 枚举类型。command.enum.structureloadaction.description单值枚举，请直接使用`load`。

`name`：<!-- md:samp string -->

- 基本类型。command.structure.name.description

`to`：<!-- md:samp x y z -->

- 基本类型。command.structure.to.description

`rotation`：<!-- md:samp Rotation -->

- 枚举类型，可选。command.enum.rotation.description枚举值如下：

  |值|描述|
  |---|---|
  |`0_degrees`|command.enum.rotation.0_degrees|
  |`90_degrees`|command.enum.rotation.90_degrees|
  |`180_degrees`|command.enum.rotation.180_degrees|
  |`270_degrees`|command.enum.rotation.270_degrees|


`mirror`：<!-- md:samp Mirror -->

- 枚举类型，可选。command.enum.mirror.description枚举值如下：

  |值|描述|
  |---|---|
  |`x`|command.enum.mirror.x|
  |`z`|command.enum.mirror.z|
  |`none`|command.enum.mirror.none|
  |`xz`|command.enum.mirror.xz|


`animationMode`：<!-- md:samp StructureAnimationMode -->

- 枚举类型，可选。command.enum.structureanimationmode.description枚举值如下：

  |值|描述|
  |---|---|
  |`block_by_block`|command.enum.structureanimationmode.block_by_block|
  |`layer_by_layer`|command.enum.structureanimationmode.layer_by_layer|


`animationSeconds`：<!-- md:samp float -->

- 基本类型，可选。command.structure.animationSeconds.description

`includeEntities`：<!-- md:samp Boolean -->

- 枚举类型，可选。command.enum.boolean.description枚举值如下：

  |值|描述|
  |---|---|
  |`true`|是|
  |`false`|否|


`includeBlocks`：<!-- md:samp Boolean -->

- 枚举类型，可选。command.enum.boolean.description枚举值如下：

  |值|描述|
  |---|---|
  |`true`|是|
  |`false`|否|


`waterlogged`：<!-- md:samp Boolean -->

- 枚举类型，可选。command.enum.boolean.description枚举值如下：

  |值|描述|
  |---|---|
  |`true`|是|
  |`false`|否|


`integrity`：<!-- md:samp float -->

- 基本类型，可选。command.structure.integrity.description

`seed`：<!-- md:samp string -->

- 基本类型，可选。command.structure.seed.description


/////

////

///
