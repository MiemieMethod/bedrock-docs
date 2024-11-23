# `Scoreboard`

> 文档版本：1.21.60.21

`Scoreboard`类。script_api.@minecraft/server.scoreboard.description

## 方法

/// define
`addObjective`


///

script_api.@minecraft/server.scoreboard.addobjective.description

```js
addObjective(objectiveId: string, displayName?: string): ScoreboardObjective
```

/// html | div.result
//// define
`objectiveId`：`string`

- script_api.@minecraft/server.scoreboard.addobjective.objectiveid.description


////

//// define
`displayName`?：`string`＝`null`

- script_api.@minecraft/server.scoreboard.addobjective.displayname.description


////

//// define
返回值：[`ScoreboardObjective`](./scoreboardobjective.md)

- script_api.@minecraft/server.scoreboard.addobjective.return


////

///


/// define
`clearObjectiveAtDisplaySlot`


///

script_api.@minecraft/server.scoreboard.clearobjectiveatdisplayslot.description

```js
clearObjectiveAtDisplaySlot(displaySlotId: DisplaySlotId): ScoreboardObjective | undefined
```

/// html | div.result
//// define
`displaySlotId`：[`DisplaySlotId`](./displayslotid.md)

- script_api.@minecraft/server.scoreboard.clearobjectiveatdisplayslot.displayslotid.description


////

//// define
返回值：[`ScoreboardObjective`](./scoreboardobjective.md)|`undefined`

- script_api.@minecraft/server.scoreboard.clearobjectiveatdisplayslot.return


////

///


/// define
`getObjective`


///

script_api.@minecraft/server.scoreboard.getobjective.description

```js
getObjective(objectiveId: string): ScoreboardObjective | undefined
```

/// html | div.result
//// define
`objectiveId`：`string`

- script_api.@minecraft/server.scoreboard.getobjective.objectiveid.description


////

//// define
返回值：[`ScoreboardObjective`](./scoreboardobjective.md)|`undefined`

- script_api.@minecraft/server.scoreboard.getobjective.return


////

///


/// define
`getObjectiveAtDisplaySlot`


///

script_api.@minecraft/server.scoreboard.getobjectiveatdisplayslot.description

```js
getObjectiveAtDisplaySlot(displaySlotId: DisplaySlotId): ScoreboardObjectiveDisplayOptions | undefined
```

/// html | div.result
//// define
`displaySlotId`：[`DisplaySlotId`](./displayslotid.md)

- script_api.@minecraft/server.scoreboard.getobjectiveatdisplayslot.displayslotid.description


////

//// define
返回值：[`ScoreboardObjectiveDisplayOptions`](./scoreboardobjectivedisplayoptions.md)|`undefined`

- script_api.@minecraft/server.scoreboard.getobjectiveatdisplayslot.return


////

///


/// define
`getObjectives`


///

script_api.@minecraft/server.scoreboard.getobjectives.description

```js
getObjectives(): ScoreboardObjective[]
```

/// html | div.result
//// define
返回值：<code><a href="../scoreboardobjective/">ScoreboardObjective</a>[]</code>

- script_api.@minecraft/server.scoreboard.getobjectives.return


////

///


/// define
`getParticipants`


///

script_api.@minecraft/server.scoreboard.getparticipants.description

```js
getParticipants(): ScoreboardIdentity[]
```

/// html | div.result
//// define
返回值：<code><a href="../scoreboardidentity/">ScoreboardIdentity</a>[]</code>

- script_api.@minecraft/server.scoreboard.getparticipants.return


////

///


/// define
`removeObjective`


///

script_api.@minecraft/server.scoreboard.removeobjective.description

```js
removeObjective(objectiveId: ScoreboardObjective | string): boolean
```

/// html | div.result
//// define
`objectiveId`：[`ScoreboardObjective`](./scoreboardobjective.md)|`string`

- script_api.@minecraft/server.scoreboard.removeobjective.objectiveid.description


////

//// define
返回值：`boolean`

- script_api.@minecraft/server.scoreboard.removeobjective.return


////

///


/// define
`setObjectiveAtDisplaySlot`


///

script_api.@minecraft/server.scoreboard.setobjectiveatdisplayslot.description

```js
setObjectiveAtDisplaySlot(displaySlotId: DisplaySlotId, objectiveDisplaySetting: ScoreboardObjectiveDisplayOptions): ScoreboardObjective | undefined
```

/// html | div.result
//// define
`displaySlotId`：[`DisplaySlotId`](./displayslotid.md)

- script_api.@minecraft/server.scoreboard.setobjectiveatdisplayslot.displayslotid.description


////

//// define
`objectiveDisplaySetting`：[`ScoreboardObjectiveDisplayOptions`](./scoreboardobjectivedisplayoptions.md)

- script_api.@minecraft/server.scoreboard.setobjectiveatdisplayslot.objectivedisplaysetting.description


////

//// define
返回值：[`ScoreboardObjective`](./scoreboardobjective.md)|`undefined`

- script_api.@minecraft/server.scoreboard.setobjectiveatdisplayslot.return


////

///

