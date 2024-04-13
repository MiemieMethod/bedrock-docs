# `/resourceuri`

> 文档版本：1.21.0.21

`/resourceuri`命令command.resourceuri.description

/// settings | 执行条件
该命令需要权限等级：`gamedirectors`|`1`。该命令需要开启作弊。
///

## 用法

/// tab | 重载1
```mcfunction
/resourceuri
```

//// html | div.result
command.resourceuri.1.description

///// define

/////

////

///

/// tab | 重载2
```mcfunction
/resourceuri clear
```

//// html | div.result
command.resourceuri.2.description

///// define
`cmd`：<!-- md:samp ResourceActionClear -->

- 枚举类型。command.enum.resourceactionclear.description单值枚举，请直接使用`clear`。


/////

////

///

/// tab | 重载3
```mcfunction
/resourceuri default [uri:text]
```

//// html | div.result
command.resourceuri.3.description

///// define
`cmd`：<!-- md:samp ResourceActionDefault -->

- 枚举类型。command.enum.resourceactiondefault.description单值枚举，请直接使用`default`。

`uri`：<!-- md:samp text -->

- 基本类型，可选。command.resourceuri.uri.description


/////

////

///

/// tab | 重载4
```mcfunction
/resourceuri named <name:string> [uri:text]
```

//// html | div.result
command.resourceuri.4.description

///// define
`cmd`：<!-- md:samp ResourceActionNamed -->

- 枚举类型。command.enum.resourceactionnamed.description单值枚举，请直接使用`named`。

`name`：<!-- md:samp string -->

- 基本类型。command.resourceuri.name.description

`uri`：<!-- md:samp text -->

- 基本类型，可选。command.resourceuri.uri.description


/////

////

///
