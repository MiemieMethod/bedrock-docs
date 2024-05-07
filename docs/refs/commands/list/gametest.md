# `/gametest`

> 文档版本：1.21.0.24

`/gametest`命令command.gametest.description

/// settings | 执行条件
该命令需要权限等级：`gamedirectors`|`1`。该命令需要开启作弊。
///

## 用法

/// tab | 重载1
```mcfunction
/gametest runthis
```

//// html | div.result
command.gametest.1.description

///// define
`mode`：<!-- md:samp GameTestModeRunThis -->

- 枚举类型。command.enum.gametestmoderunthis.description单值枚举，请直接使用`runthis`。


/////

////

///

/// tab | 重载2
```mcfunction
/gametest run <testName:string> [rotationSteps:int]
```

//// html | div.result
command.gametest.2.description

///// define
`mode`：<!-- md:samp GameTestModeRun -->

- 枚举类型。command.enum.gametestmoderun.description单值枚举，请直接使用`run`。

`testName`：<!-- md:samp GameTestName -->

- 软枚举类型。command.gametest.testName.description

`rotationSteps`：<!-- md:samp int -->

- 基本类型，可选。command.gametest.rotationSteps.description


/////

////

///

/// tab | 重载3
```mcfunction
/gametest run <testName:string> <stopOnFailure:Boolean> <repeatCount:int> [rotationSteps:int]
```

//// html | div.result
command.gametest.3.description

///// define
`mode`：<!-- md:samp GameTestModeRun -->

- 枚举类型。command.enum.gametestmoderun.description单值枚举，请直接使用`run`。

`testName`：<!-- md:samp GameTestName -->

- 软枚举类型。command.gametest.testName.description

`stopOnFailure`：<!-- md:samp Boolean -->

- 枚举类型。command.enum.boolean.description枚举值如下：

  |值|描述|
  |---|---|
  |`true`|是|
  |`false`|否|


`repeatCount`：<!-- md:samp int -->

- 基本类型。command.gametest.repeatCount.description

`rotationSteps`：<!-- md:samp int -->

- 基本类型，可选。command.gametest.rotationSteps.description


/////

////

///

/// tab | 重载4
```mcfunction
/gametest runset [tag:string] [rotationSteps:int]
```

//// html | div.result
command.gametest.4.description

///// define
`mode`：<!-- md:samp GameTestModeRunSet -->

- 枚举类型。command.enum.gametestmoderunset.description单值枚举，请直接使用`runset`。

`tag`：<!-- md:samp GameTestTag -->

- 软枚举类型，可选。command.gametest.tag.description

`rotationSteps`：<!-- md:samp int -->

- 基本类型，可选。command.gametest.rotationSteps.description


/////

////

///

/// tab | 重载5
```mcfunction
/gametest runsetuntilfail [tag:string] [rotationSteps:int]
```

//// html | div.result
command.gametest.5.description

///// define
`mode`：<!-- md:samp GameTestModeRunSetUntilFail -->

- 枚举类型。command.enum.gametestmoderunsetuntilfail.description单值枚举，请直接使用`runsetuntilfail`。

`tag`：<!-- md:samp GameTestTag -->

- 软枚举类型，可选。command.gametest.tag.description

`rotationSteps`：<!-- md:samp int -->

- 基本类型，可选。command.gametest.rotationSteps.description


/////

////

///

/// tab | 重载6
```mcfunction
/gametest clearall
```

//// html | div.result
command.gametest.6.description

///// define
`mode`：<!-- md:samp GameTestModeClearAll -->

- 枚举类型。command.enum.gametestmodeclearall.description单值枚举，请直接使用`clearall`。


/////

////

///

/// tab | 重载7
```mcfunction
/gametest pos
```

//// html | div.result
command.gametest.7.description

///// define
`mode`：<!-- md:samp GameTestModeShowPosition -->

- 枚举类型。command.enum.gametestmodeshowposition.description单值枚举，请直接使用`pos`。


/////

////

///

/// tab | 重载8
```mcfunction
/gametest create <testName:string> [width:int] [height:int] [depth:int]
```

//// html | div.result
command.gametest.8.description

///// define
`mode`：<!-- md:samp GameTestModeCreateTest -->

- 枚举类型。command.enum.gametestmodecreatetest.description单值枚举，请直接使用`create`。

`testName`：<!-- md:samp string -->

- 基本类型。command.gametest.testName.description

`width`：<!-- md:samp int -->

- 基本类型，可选。command.gametest.width.description

`height`：<!-- md:samp int -->

- 基本类型，可选。command.gametest.height.description

`depth`：<!-- md:samp int -->

- 基本类型，可选。command.gametest.depth.description


/////

////

///

/// tab | 重载9
```mcfunction
/gametest runthese
```

//// html | div.result
command.gametest.9.description

///// define
`mode`：<!-- md:samp GameTestRunNearbyTests -->

- 枚举类型。command.enum.gametestrunnearbytests.description单值枚举，请直接使用`runthese`。


/////

////

///

/// tab | 重载10
```mcfunction
/gametest stopall
```

//// html | div.result
command.gametest.10.description

///// define
`mode`：<!-- md:samp GameTestStopTests -->

- 枚举类型。command.enum.gameteststoptests.description单值枚举，请直接使用`stopall`。


/////

////

///
