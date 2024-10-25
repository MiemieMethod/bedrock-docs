# `/teleport`

> 文档版本：1.21.50.25

`/teleport`命令command.teleport.description

/// settings | 执行条件
该命令需要权限等级：`gamedirectors`|`1`。该命令需要开启作弊。
///

/// info | 别名
该命令还可以使用以下别名：`/tp`。
///

## 用法

/// tab | 重载1
```mcfunction
/teleport <destination:x y z> [checkForBlocks:Boolean]
```

//// html | div.result
command.teleport.1.description

///// define
`destination`：<!-- md:samp x y z -->

- 基本类型。command.teleport.destination.description

`checkForBlocks`：<!-- md:samp Boolean -->

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
/teleport <destination:x y z> [yRot:value] [xRot:value] [checkForBlocks:Boolean]
```

//// html | div.result
command.teleport.2.description

///// define
`destination`：<!-- md:samp x y z -->

- 基本类型。command.teleport.destination.description

`yRot`：<!-- md:samp value -->

- 基本类型，可选。command.teleport.yRot.description

`xRot`：<!-- md:samp value -->

- 基本类型，可选。command.teleport.xRot.description

`checkForBlocks`：<!-- md:samp Boolean -->

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
/teleport <destination:x y z> facing <lookAtPosition:x y z> [checkForBlocks:Boolean]
```

//// html | div.result
command.teleport.3.description

///// define
`destination`：<!-- md:samp x y z -->

- 基本类型。command.teleport.destination.description

`facing`：<!-- md:samp TeleportFacing -->

- 枚举类型。command.enum.teleportfacing.description单值枚举，请直接使用`facing`。

`lookAtPosition`：<!-- md:samp x y z -->

- 基本类型。command.teleport.lookAtPosition.description

`checkForBlocks`：<!-- md:samp Boolean -->

- 枚举类型，可选。command.enum.boolean.description枚举值如下：

  |值|描述|
  |---|---|
  |`true`|是|
  |`false`|否|



/////

////

///

/// tab | 重载4
```mcfunction
/teleport <destination:x y z> facing <lookAtEntity:target> [checkForBlocks:Boolean]
```

//// html | div.result
command.teleport.4.description

///// define
`destination`：<!-- md:samp x y z -->

- 基本类型。command.teleport.destination.description

`facing`：<!-- md:samp TeleportFacing -->

- 枚举类型。command.enum.teleportfacing.description单值枚举，请直接使用`facing`。

`lookAtEntity`：<!-- md:samp target -->

- 基本类型。command.teleport.lookAtEntity.description

`checkForBlocks`：<!-- md:samp Boolean -->

- 枚举类型，可选。command.enum.boolean.description枚举值如下：

  |值|描述|
  |---|---|
  |`true`|是|
  |`false`|否|



/////

////

///

/// tab | 重载5
```mcfunction
/teleport <victim:target> <destination:x y z> [yRot:value] [xRot:value] [checkForBlocks:Boolean]
```

//// html | div.result
command.teleport.5.description

///// define
`victim`：<!-- md:samp target -->

- 基本类型。command.teleport.victim.description

`destination`：<!-- md:samp x y z -->

- 基本类型。command.teleport.destination.description

`yRot`：<!-- md:samp value -->

- 基本类型，可选。command.teleport.yRot.description

`xRot`：<!-- md:samp value -->

- 基本类型，可选。command.teleport.xRot.description

`checkForBlocks`：<!-- md:samp Boolean -->

- 枚举类型，可选。command.enum.boolean.description枚举值如下：

  |值|描述|
  |---|---|
  |`true`|是|
  |`false`|否|



/////

////

///

/// tab | 重载6
```mcfunction
/teleport <victim:target> <destination:x y z> [checkForBlocks:Boolean]
```

//// html | div.result
command.teleport.6.description

///// define
`victim`：<!-- md:samp target -->

- 基本类型。command.teleport.victim.description

`destination`：<!-- md:samp x y z -->

- 基本类型。command.teleport.destination.description

`checkForBlocks`：<!-- md:samp Boolean -->

- 枚举类型，可选。command.enum.boolean.description枚举值如下：

  |值|描述|
  |---|---|
  |`true`|是|
  |`false`|否|



/////

////

///

/// tab | 重载7
```mcfunction
/teleport <victim:target> <destination:x y z> facing <lookAtPosition:x y z> [checkForBlocks:Boolean]
```

//// html | div.result
command.teleport.7.description

///// define
`victim`：<!-- md:samp target -->

- 基本类型。command.teleport.victim.description

`destination`：<!-- md:samp x y z -->

- 基本类型。command.teleport.destination.description

`facing`：<!-- md:samp TeleportFacing -->

- 枚举类型。command.enum.teleportfacing.description单值枚举，请直接使用`facing`。

`lookAtPosition`：<!-- md:samp x y z -->

- 基本类型。command.teleport.lookAtPosition.description

`checkForBlocks`：<!-- md:samp Boolean -->

- 枚举类型，可选。command.enum.boolean.description枚举值如下：

  |值|描述|
  |---|---|
  |`true`|是|
  |`false`|否|



/////

////

///

/// tab | 重载8
```mcfunction
/teleport <victim:target> <destination:x y z> facing <lookAtEntity:target> [checkForBlocks:Boolean]
```

//// html | div.result
command.teleport.8.description

///// define
`victim`：<!-- md:samp target -->

- 基本类型。command.teleport.victim.description

`destination`：<!-- md:samp x y z -->

- 基本类型。command.teleport.destination.description

`facing`：<!-- md:samp TeleportFacing -->

- 枚举类型。command.enum.teleportfacing.description单值枚举，请直接使用`facing`。

`lookAtEntity`：<!-- md:samp target -->

- 基本类型。command.teleport.lookAtEntity.description

`checkForBlocks`：<!-- md:samp Boolean -->

- 枚举类型，可选。command.enum.boolean.description枚举值如下：

  |值|描述|
  |---|---|
  |`true`|是|
  |`false`|否|



/////

////

///

/// tab | 重载9
```mcfunction
/teleport <destination:target>
```

//// html | div.result
command.teleport.9.description

///// define
`destination`：<!-- md:samp target -->

- 基本类型。command.teleport.destination.description


/////

////

///

/// tab | 重载10
```mcfunction
/teleport <victim:target> <destination:target> [checkForBlocks:Boolean]
```

//// html | div.result
command.teleport.10.description

///// define
`victim`：<!-- md:samp target -->

- 基本类型。command.teleport.victim.description

`destination`：<!-- md:samp target -->

- 基本类型。command.teleport.destination.description

`checkForBlocks`：<!-- md:samp Boolean -->

- 枚举类型，可选。command.enum.boolean.description枚举值如下：

  |值|描述|
  |---|---|
  |`true`|是|
  |`false`|否|



/////

////

///
