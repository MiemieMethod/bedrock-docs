# `/place`

> 文档版本：1.21.60.21

`/place`命令command.place.description

/// settings | 执行条件
该命令需要权限等级：`admin`|`2`。该命令需要开启作弊。
///

## 用法

/// tab | 重载1
```mcfunction
/place structure <structure:JigsawStructure> [pos:x y z] [ignoreStartHeight:Boolean] [keepJigsaws:Boolean]
```

//// html | div.result
command.place.1.description

///// define
`action`：<!-- md:samp PlaceStructureAction -->

- 枚举类型。command.enum.placestructureaction.description单值枚举，请直接使用`structure`。

`structure`：<!-- md:samp JigsawStructure -->

- 枚举类型。command.enum.jigsawstructure.description枚举值如下：

  |值|描述|
  |---|---|
  |`minecraft:trail_ruins`|command.enum.jigsawstructure.minecraft:trail_ruins|
  |`minecraft:trial_chambers`|command.enum.jigsawstructure.minecraft:trial_chambers|


`pos`：<!-- md:samp x y z -->

- 基本类型，可选。command.place.pos.description

`ignoreStartHeight`：<!-- md:samp Boolean -->

- 枚举类型，可选。command.enum.boolean.description枚举值如下：

  |值|描述|
  |---|---|
  |`true`|是|
  |`false`|否|


`keepJigsaws`：<!-- md:samp Boolean -->

- 枚举类型，可选。command.enum.boolean.description枚举值如下：

  |值|描述|
  |---|---|
  |`true`|是|
  |`false`|否|



/////

////

///

/// tab | 重载2
```mcfunction
/place jigsaw <pool:filepath> <jigsawTarget:string> <maxDepth:int> [pos:x y z] [keepJigsaws:Boolean]
```

//// html | div.result
command.place.2.description

///// define
`action`：<!-- md:samp PlaceJigsawAction -->

- 枚举类型。command.enum.placejigsawaction.description单值枚举，请直接使用`jigsaw`。

`pool`：<!-- md:samp filepath -->

- 基本类型。command.place.pool.description

`jigsawTarget`：<!-- md:samp string -->

- 基本类型。command.place.jigsawTarget.description

`maxDepth`：<!-- md:samp int -->

- 基本类型。command.place.maxDepth.description

`pos`：<!-- md:samp x y z -->

- 基本类型，可选。command.place.pos.description

`keepJigsaws`：<!-- md:samp Boolean -->

- 枚举类型，可选。command.enum.boolean.description枚举值如下：

  |值|描述|
  |---|---|
  |`true`|是|
  |`false`|否|



/////

////

///
