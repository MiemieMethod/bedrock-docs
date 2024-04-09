# `ScoreboardObjective`

> 文档版本：1.21.0.20

`ScoreboardObjective`类。script_api.mojang-minecraft.scoreboardobjective.description

## 属性

/// define
`displayName`


///

```js
read-only displayName: string;
```

/// html | div.result
//// define
`displayName`：`string`

- script_api.mojang-minecraft.scoreboardobjective.displayname.description


////

///


/// define
`id`


///

```js
read-only id: string;
```

/// html | div.result
//// define
`id`：`string`

- script_api.mojang-minecraft.scoreboardobjective.id.description


////

///


## 方法

/// define
`getParticipants`


///

script_api.mojang-minecraft.scoreboardobjective.getparticipants.description

```js
getParticipants(): ScoreboardIdentity[]
```

/// html | div.result
//// define
返回值：<code><a href="../scoreboardidentity/">ScoreboardIdentity</a>[]</code>

- script_api.mojang-minecraft.scoreboardobjective.getparticipants.return


////

///


/// define
`getScore`


///

script_api.mojang-minecraft.scoreboardobjective.getscore.description

```js
getScore(participant: Entity | ScoreboardIdentity | string): int32 | undefined
```

/// html | div.result
//// define
`participant`：[`Entity`](./entity.md)|[`ScoreboardIdentity`](./scoreboardidentity.md)|`string`

- script_api.mojang-minecraft.scoreboardobjective.participant.getscore.description


////

//// define
返回值：`int32`|`undefined`

- script_api.mojang-minecraft.scoreboardobjective.getscore.return


////

///


/// define
`getScores`


///

script_api.mojang-minecraft.scoreboardobjective.getscores.description

```js
getScores(): ScoreboardScoreInfo[]
```

/// html | div.result
//// define
返回值：<code><a href="../scoreboardscoreinfo/">ScoreboardScoreInfo</a>[]</code>

- script_api.mojang-minecraft.scoreboardobjective.getscores.return


////

///

