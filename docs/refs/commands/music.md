# `/music`

> 文档版本：1.20.80.24

`/music`命令Allows you to control playing music tracks.

/// note | 执行条件
该命令需要权限等级：`gamedirectors`|`1`。该命令需要开启作弊。
///

## 用法

/// tab | `重载1`
```mcfunction
/music queue <trackName:string> [volume:float] [fadeSeconds:float] [repeatMode:MusicRepeatMode]
```

//// html | div.result
///// define
`action`: <!-- md:samp MusicQueueAction -->

- 枚举类型。枚举值如下：

|值|描述|
|---|---|
|`queue`||


`trackName`: <!-- md:samp string -->

- 基本类型。

`volume`: <!-- md:samp float -->

- 基本类型。

`fadeSeconds`: <!-- md:samp float -->

- 基本类型。

`repeatMode`: <!-- md:samp MusicRepeatMode -->

- 枚举类型。枚举值如下：

|值|描述|
|---|---|
|`play_once`||
|`loop`||



/////

////

///

/// tab | `重载2`
```mcfunction
/music play <trackName:string> [volume:float] [fadeSeconds:float] [repeatMode:MusicRepeatMode]
```

//// html | div.result
///// define
`action`: <!-- md:samp MusicPlayAction -->

- 枚举类型。枚举值如下：

|值|描述|
|---|---|
|`play`||


`trackName`: <!-- md:samp string -->

- 基本类型。

`volume`: <!-- md:samp float -->

- 基本类型。

`fadeSeconds`: <!-- md:samp float -->

- 基本类型。

`repeatMode`: <!-- md:samp MusicRepeatMode -->

- 枚举类型。枚举值如下：

|值|描述|
|---|---|
|`play_once`||
|`loop`||



/////

////

///

/// tab | `重载3`
```mcfunction
/music stop [fadeSeconds:float]
```

//// html | div.result
///// define
`action`: <!-- md:samp MusicStopAction -->

- 枚举类型。枚举值如下：

|值|描述|
|---|---|
|`stop`||


`fadeSeconds`: <!-- md:samp float -->

- 基本类型。


/////

////

///

/// tab | `重载4`
```mcfunction
/music volume <volume:float>
```

//// html | div.result
///// define
`action`: <!-- md:samp MusicVolumeAction -->

- 枚举类型。枚举值如下：

|值|描述|
|---|---|
|`volume`||


`volume`: <!-- md:samp float -->

- 基本类型。


/////

////

///
