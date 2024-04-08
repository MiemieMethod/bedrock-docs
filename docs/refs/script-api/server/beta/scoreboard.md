# `Scoreboard`

> 文档版本：1.21.0.20

`Scoreboard`类。

## 方法

/// define
`addObjective`


///

```js
addObjective(objectiveId: string, displayName?: string): ScoreboardObjective
```

/// html | div.result
//// define
`objectiveId`：`string`

- 参数1。


////

//// define
`displayName`：`string`|`undefined`

- 参数2。


////

//// define
返回值：[`ScoreboardObjective`](./scoreboardobjective.md)

- 返回值。


////

///


/// define
`clearObjectiveAtDisplaySlot`


///

```js
clearObjectiveAtDisplaySlot(displaySlotId: DisplaySlotId): ScoreboardObjective | undefined
```

/// html | div.result
//// define
`displaySlotId`：[`DisplaySlotId`](./displayslotid.md)

- 参数1。


////

//// define
返回值：[`ScoreboardObjective`](./scoreboardobjective.md)|`undefined`

- 返回值。


////

///


/// define
`getObjective`


///

```js
getObjective(objectiveId: string): ScoreboardObjective | undefined
```

/// html | div.result
//// define
`objectiveId`：`string`

- 参数1。


////

//// define
返回值：[`ScoreboardObjective`](./scoreboardobjective.md)|`undefined`

- 返回值。


////

///


/// define
`getObjectiveAtDisplaySlot`


///

```js
getObjectiveAtDisplaySlot(displaySlotId: DisplaySlotId): ScoreboardObjectiveDisplayOptions | undefined
```

/// html | div.result
//// define
`displaySlotId`：[`DisplaySlotId`](./displayslotid.md)

- 参数1。


////

//// define
返回值：[`ScoreboardObjectiveDisplayOptions`](./scoreboardobjectivedisplayoptions.md)|`undefined`

- 返回值。


////

///


/// define
`getObjectives`


///

```js
getObjectives(): ScoreboardObjective[]
```

/// html | div.result

///


/// define
`getParticipants`


///

```js
getParticipants(): ScoreboardIdentity[]
```

/// html | div.result

///


/// define
`removeObjective`


///

```js
removeObjective(objectiveId: ScoreboardObjective | string): boolean
```

/// html | div.result
//// define
`objectiveId`：ScoreboardObjective|string

- 参数1。


////

//// define
返回值：`boolean`

- 返回值。


////

///


/// define
`setObjectiveAtDisplaySlot`


///

```js
setObjectiveAtDisplaySlot(displaySlotId: DisplaySlotId, objectiveDisplaySetting: ScoreboardObjectiveDisplayOptions): ScoreboardObjective | undefined
```

/// html | div.result
//// define
`displaySlotId`：[`DisplaySlotId`](./displayslotid.md)

- 参数1。


////

//// define
`objectiveDisplaySetting`：[`ScoreboardObjectiveDisplayOptions`](./scoreboardobjectivedisplayoptions.md)

- 参数2。


////

//// define
返回值：[`ScoreboardObjective`](./scoreboardobjective.md)|`undefined`

- 返回值。


////

///

