# `ScoreboardObjective`

> 文档版本：1.21.0.24

`ScoreboardObjective`类。script_api.@minecraft/server.scoreboardobjective.description

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

- script_api.@minecraft/server.scoreboardobjective.displayname.description


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

- script_api.@minecraft/server.scoreboardobjective.id.description


////

///


## 方法

/// define
`addScore`


///

script_api.@minecraft/server.scoreboardobjective.addscore.description

```js
addScore(participant: Entity | ScoreboardIdentity | string, scoreToAdd: int32): int32
```

/// html | div.result
//// define
`participant`：[`Entity`](./entity.md)|[`ScoreboardIdentity`](./scoreboardidentity.md)|`string`

- script_api.@minecraft/server.scoreboardobjective.addscore.participant.description


////

//// define
`scoreToAdd`：`int32`

- script_api.@minecraft/server.scoreboardobjective.addscore.scoretoadd.description


////

//// define
返回值：`int32`

- script_api.@minecraft/server.scoreboardobjective.addscore.return


////

///


/// define
`getParticipants`


///

script_api.@minecraft/server.scoreboardobjective.getparticipants.description

```js
getParticipants(): ScoreboardIdentity[]
```

/// html | div.result
//// define
返回值：<code><a href="../scoreboardidentity/">ScoreboardIdentity</a>[]</code>

- script_api.@minecraft/server.scoreboardobjective.getparticipants.return


////

///


/// define
`getScore`


///

script_api.@minecraft/server.scoreboardobjective.getscore.description

```js
getScore(participant: Entity | ScoreboardIdentity | string): int32 | undefined
```

/// html | div.result
//// define
`participant`：[`Entity`](./entity.md)|[`ScoreboardIdentity`](./scoreboardidentity.md)|`string`

- script_api.@minecraft/server.scoreboardobjective.getscore.participant.description


////

//// define
返回值：`int32`|`undefined`

- script_api.@minecraft/server.scoreboardobjective.getscore.return


////

///


/// define
`getScores`


///

script_api.@minecraft/server.scoreboardobjective.getscores.description

```js
getScores(): ScoreboardScoreInfo[]
```

/// html | div.result
//// define
返回值：<code><a href="../scoreboardscoreinfo/">ScoreboardScoreInfo</a>[]</code>

- script_api.@minecraft/server.scoreboardobjective.getscores.return


////

///


/// define
`hasParticipant`


///

script_api.@minecraft/server.scoreboardobjective.hasparticipant.description

```js
hasParticipant(participant: Entity | ScoreboardIdentity | string): boolean
```

/// html | div.result
//// define
`participant`：[`Entity`](./entity.md)|[`ScoreboardIdentity`](./scoreboardidentity.md)|`string`

- script_api.@minecraft/server.scoreboardobjective.hasparticipant.participant.description


////

//// define
返回值：`boolean`

- script_api.@minecraft/server.scoreboardobjective.hasparticipant.return


////

///


/// define
`isValid`


///

script_api.@minecraft/server.scoreboardobjective.isvalid.description

```js
isValid(): boolean
```

/// html | div.result
//// define
返回值：`boolean`

- script_api.@minecraft/server.scoreboardobjective.isvalid.return


////

///


/// define
`removeParticipant`


///

script_api.@minecraft/server.scoreboardobjective.removeparticipant.description

```js
removeParticipant(participant: Entity | ScoreboardIdentity | string): boolean
```

/// html | div.result
//// define
`participant`：[`Entity`](./entity.md)|[`ScoreboardIdentity`](./scoreboardidentity.md)|`string`

- script_api.@minecraft/server.scoreboardobjective.removeparticipant.participant.description


////

//// define
返回值：`boolean`

- script_api.@minecraft/server.scoreboardobjective.removeparticipant.return


////

///


/// define
`setScore`


///

script_api.@minecraft/server.scoreboardobjective.setscore.description

```js
setScore(participant: Entity | ScoreboardIdentity | string, score: int32): void
```

/// html | div.result
//// define
`participant`：[`Entity`](./entity.md)|[`ScoreboardIdentity`](./scoreboardidentity.md)|`string`

- script_api.@minecraft/server.scoreboardobjective.setscore.participant.description


////

//// define
`score`：`int32`

- script_api.@minecraft/server.scoreboardobjective.setscore.score.description


////

//// define
返回值：`void`

- script_api.@minecraft/server.scoreboardobjective.setscore.return


////

///

