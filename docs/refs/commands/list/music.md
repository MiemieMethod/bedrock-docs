# `/music`

> 文档版本：1.21.50.25

`/music`命令command.music.description

/// settings | 执行条件
该命令需要权限等级：`gamedirectors`|`1`。该命令需要开启作弊。
///

## 用法

/// tab | 重载1
```mcfunction
/music queue <trackName:string> [volume:float] [fadeSeconds:float] [repeatMode:MusicRepeatMode]
```

//// html | div.result
command.music.1.description

///// define
`action`：<!-- md:samp MusicQueueAction -->

- 枚举类型。command.enum.musicqueueaction.description单值枚举，请直接使用`queue`。

`trackName`：<!-- md:samp string -->

- 基本类型。command.music.trackName.description

`volume`：<!-- md:samp float -->

- 基本类型，可选。command.music.volume.description

`fadeSeconds`：<!-- md:samp float -->

- 基本类型，可选。command.music.fadeSeconds.description

`repeatMode`：<!-- md:samp MusicRepeatMode -->

- 枚举类型，可选。command.enum.musicrepeatmode.description枚举值如下：

  |值|描述|
  |---|---|
  |`play_once`|command.enum.musicrepeatmode.play_once|
  |`loop`|command.enum.musicrepeatmode.loop|



/////

////

///

/// tab | 重载2
```mcfunction
/music play <trackName:string> [volume:float] [fadeSeconds:float] [repeatMode:MusicRepeatMode]
```

//// html | div.result
command.music.2.description

///// define
`action`：<!-- md:samp MusicPlayAction -->

- 枚举类型。command.enum.musicplayaction.description单值枚举，请直接使用`play`。

`trackName`：<!-- md:samp string -->

- 基本类型。command.music.trackName.description

`volume`：<!-- md:samp float -->

- 基本类型，可选。command.music.volume.description

`fadeSeconds`：<!-- md:samp float -->

- 基本类型，可选。command.music.fadeSeconds.description

`repeatMode`：<!-- md:samp MusicRepeatMode -->

- 枚举类型，可选。command.enum.musicrepeatmode.description枚举值如下：

  |值|描述|
  |---|---|
  |`play_once`|command.enum.musicrepeatmode.play_once|
  |`loop`|command.enum.musicrepeatmode.loop|



/////

////

///

/// tab | 重载3
```mcfunction
/music stop [fadeSeconds:float]
```

//// html | div.result
command.music.3.description

///// define
`action`：<!-- md:samp MusicStopAction -->

- 枚举类型。command.enum.musicstopaction.description单值枚举，请直接使用`stop`。

`fadeSeconds`：<!-- md:samp float -->

- 基本类型，可选。command.music.fadeSeconds.description


/////

////

///

/// tab | 重载4
```mcfunction
/music volume <volume:float>
```

//// html | div.result
command.music.4.description

///// define
`action`：<!-- md:samp MusicVolumeAction -->

- 枚举类型。command.enum.musicvolumeaction.description单值枚举，请直接使用`volume`。

`volume`：<!-- md:samp float -->

- 基本类型。command.music.volume.description


/////

////

///
