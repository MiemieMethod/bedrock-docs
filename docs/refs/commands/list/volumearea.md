# `/volumearea`

> 文档版本：1.21.0.24

`/volumearea`命令command.volumearea.description

/// settings | 执行条件
该命令需要权限等级：`gamedirectors`|`1`。该命令需要开启作弊。
///

## 用法

/// tab | 重载1
```mcfunction
/volumearea add <identifier:string> <from:x y z> <to:x y z> [name:string]
```

//// html | div.result
command.volumearea.1.description

///// define
`mode`：<!-- md:samp VolumeAreaAdd -->

- 枚举类型。command.enum.volumeareaadd.description单值枚举，请直接使用`add`。

`identifier`：<!-- md:samp string -->

- 基本类型。command.volumearea.identifier.description

`from`：<!-- md:samp x y z -->

- 基本类型。command.volumearea.from.description

`to`：<!-- md:samp x y z -->

- 基本类型。command.volumearea.to.description

`name`：<!-- md:samp string -->

- 基本类型，可选。command.volumearea.name.description


/////

////

///

/// tab | 重载2
```mcfunction
/volumearea remove <name:string>
```

//// html | div.result
command.volumearea.2.description

///// define
`mode`：<!-- md:samp VolumeAreaRemove -->

- 枚举类型。command.enum.volumearearemove.description单值枚举，请直接使用`remove`。

`name`：<!-- md:samp string -->

- 基本类型。command.volumearea.name.description


/////

////

///

/// tab | 重载3
```mcfunction
/volumearea remove <position:x y z>
```

//// html | div.result
command.volumearea.3.description

///// define
`mode`：<!-- md:samp VolumeAreaRemove -->

- 枚举类型。command.enum.volumearearemove.description单值枚举，请直接使用`remove`。

`position`：<!-- md:samp x y z -->

- 基本类型。command.volumearea.position.description


/////

////

///

/// tab | 重载4
```mcfunction
/volumearea remove_all
```

//// html | div.result
command.volumearea.4.description

///// define
`mode`：<!-- md:samp VolumeAreaRemoveAll -->

- 枚举类型。command.enum.volumearearemoveall.description单值枚举，请直接使用`remove_all`。


/////

////

///

/// tab | 重载5
```mcfunction
/volumearea list all-dimensions
```

//// html | div.result
command.volumearea.5.description

///// define
`mode`：<!-- md:samp VolumeAreaList -->

- 枚举类型。command.enum.volumearealist.description单值枚举，请直接使用`list`。

`all-dimensions`：<!-- md:samp VolumeAreaAllDimensions -->

- 枚举类型，可选。command.enum.volumeareaalldimensions.description单值枚举，请直接使用`all-dimensions`。


/////

////

///
