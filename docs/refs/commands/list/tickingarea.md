# `/tickingarea`

> 文档版本：1.21.0.21

`/tickingarea`命令command.tickingarea.description

/// settings | 执行条件
该命令需要权限等级：`gamedirectors`|`1`。该命令需要开启作弊。
///

## 用法

/// tab | 重载1
```mcfunction
/tickingarea add <from:x y z> <to:x y z> [name:string] [preload:Boolean]
```

//// html | div.result
command.tickingarea.1.description

///// define
`mode`：<!-- md:samp TickingAreaModeAdd -->

- 枚举类型。command.enum.tickingareamodeadd.description单值枚举，请直接使用`add`。

`from`：<!-- md:samp x y z -->

- 基本类型。command.tickingarea.from.description

`to`：<!-- md:samp x y z -->

- 基本类型。command.tickingarea.to.description

`name`：<!-- md:samp string -->

- 基本类型，可选。command.tickingarea.name.description

`preload`：<!-- md:samp Boolean -->

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
/tickingarea add circle <center:x y z> <radius:int> [name:string] [preload:Boolean]
```

//// html | div.result
command.tickingarea.2.description

///// define
`mode`：<!-- md:samp TickingAreaModeAdd -->

- 枚举类型。command.enum.tickingareamodeadd.description单值枚举，请直接使用`add`。

`circle`：<!-- md:samp AddTickingAreaType -->

- 枚举类型。command.enum.addtickingareatype.description单值枚举，请直接使用`circle`。

`center`：<!-- md:samp x y z -->

- 基本类型。command.tickingarea.center.description

`radius`：<!-- md:samp int -->

- 基本类型。command.tickingarea.radius.description

`name`：<!-- md:samp string -->

- 基本类型，可选。command.tickingarea.name.description

`preload`：<!-- md:samp Boolean -->

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
/tickingarea remove <position:x y z>
```

//// html | div.result
command.tickingarea.3.description

///// define
`mode`：<!-- md:samp TickingAreaModeRemove -->

- 枚举类型。command.enum.tickingareamoderemove.description单值枚举，请直接使用`remove`。

`position`：<!-- md:samp x y z -->

- 基本类型。command.tickingarea.position.description


/////

////

///

/// tab | 重载4
```mcfunction
/tickingarea remove <name:string>
```

//// html | div.result
command.tickingarea.4.description

///// define
`mode`：<!-- md:samp TickingAreaModeRemove -->

- 枚举类型。command.enum.tickingareamoderemove.description单值枚举，请直接使用`remove`。

`name`：<!-- md:samp string -->

- 基本类型。command.tickingarea.name.description


/////

////

///

/// tab | 重载5
```mcfunction
/tickingarea remove_all
```

//// html | div.result
command.tickingarea.5.description

///// define
`mode`：<!-- md:samp TickingAreaModeRemoveAll -->

- 枚举类型。command.enum.tickingareamoderemoveall.description单值枚举，请直接使用`remove_all`。


/////

////

///

/// tab | 重载6
```mcfunction
/tickingarea list all-dimensions
```

//// html | div.result
command.tickingarea.6.description

///// define
`mode`：<!-- md:samp TickingAreaModeList -->

- 枚举类型。command.enum.tickingareamodelist.description单值枚举，请直接使用`list`。

`all-dimensions`：<!-- md:samp AllDimensions -->

- 枚举类型，可选。command.enum.alldimensions.description单值枚举，请直接使用`all-dimensions`。


/////

////

///

/// tab | 重载7
```mcfunction
/tickingarea preload <position:x y z> [preload:Boolean]
```

//// html | div.result
command.tickingarea.7.description

///// define
`mode`：<!-- md:samp TickingAreaModePreload -->

- 枚举类型。command.enum.tickingareamodepreload.description单值枚举，请直接使用`preload`。

`position`：<!-- md:samp x y z -->

- 基本类型。command.tickingarea.position.description

`preload`：<!-- md:samp Boolean -->

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
/tickingarea preload <name:string> [preload:Boolean]
```

//// html | div.result
command.tickingarea.8.description

///// define
`mode`：<!-- md:samp TickingAreaModePreload -->

- 枚举类型。command.enum.tickingareamodepreload.description单值枚举，请直接使用`preload`。

`name`：<!-- md:samp string -->

- 基本类型。command.tickingarea.name.description

`preload`：<!-- md:samp Boolean -->

- 枚举类型，可选。command.enum.boolean.description枚举值如下：

  |值|描述|
  |---|---|
  |`true`|是|
  |`false`|否|



/////

////

///
