# `Scoreboard`

> 文档版本：1.21.0.20

`Scoreboard`类。script_api.mojang-minecraft.scoreboard.description

## 方法

/// define
`getObjective`


///

script_api.mojang-minecraft.scoreboard.getobjective.description

```js
getObjective(objectiveId: string): ScoreboardObjective | undefined
```

/// html | div.result
//// define
`objectiveId`：`string`

- script_api.mojang-minecraft.scoreboard.objectiveid.getobjective.description


////

//// define
返回值：[`ScoreboardObjective`](./scoreboardobjective.md)|`undefined`

- script_api.mojang-minecraft.scoreboard.getobjective.return


////

///


/// define
`getObjectives`


///

script_api.mojang-minecraft.scoreboard.getobjectives.description

```js
getObjectives(): ScoreboardObjective[]
```

/// html | div.result
//// define
返回值：<code><a href="../scoreboardobjective/">ScoreboardObjective</a>[]</code>

- script_api.mojang-minecraft.scoreboard.getobjectives.return


////

///


/// define
`getParticipants`


///

script_api.mojang-minecraft.scoreboard.getparticipants.description

```js
getParticipants(): ScoreboardIdentity[]
```

/// html | div.result
//// define
返回值：<code><a href="../scoreboardidentity/">ScoreboardIdentity</a>[]</code>

- script_api.mojang-minecraft.scoreboard.getparticipants.return


////

///

