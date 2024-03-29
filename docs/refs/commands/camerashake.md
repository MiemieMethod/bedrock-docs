# `/camerashake`

> 文档版本：1.20.80.24

`/camerashake`命令Applies shaking to the players' camera with a specified intensity and duration.

/// note | 执行条件
该命令需要权限等级：`gamedirectors`|`1`。该命令需要开启作弊。
///

## 用法

/// tab | 重载1
```mcfunction
/camerashake add <player:target> [intensity:float] [seconds:float] [shakeType:CameraShakeType]
```

//// html | div.result
///// define
`action`: <!-- md:samp CameraShakeActionAdd -->

- 枚举类型。枚举值如下：

|值|描述|
|---|---|
|`add`||


`player`: <!-- md:samp target -->

- 基本类型。

`intensity`: <!-- md:samp float -->

- 基本类型。

`seconds`: <!-- md:samp float -->

- 基本类型。

`shakeType`: <!-- md:samp CameraShakeType -->

- 枚举类型。枚举值如下：

|值|描述|
|---|---|
|`positional`||
|`rotational`||



/////

////

///

/// tab | 重载2
```mcfunction
/camerashake stop [player:target]
```

//// html | div.result
///// define
`action`: <!-- md:samp CameraShakeActionStop -->

- 枚举类型。枚举值如下：

|值|描述|
|---|---|
|`stop`||


`player`: <!-- md:samp target -->

- 基本类型。


/////

////

///
