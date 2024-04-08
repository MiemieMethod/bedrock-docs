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


/// define
`clearObjectiveAtDisplaySlot`


///

```js
clearObjectiveAtDisplaySlot(displaySlotId: DisplaySlotId): ScoreboardObjective | undefined
```


/// define
`getObjective`


///

```js
getObjective(objectiveId: string): ScoreboardObjective | undefined
```


/// define
`getObjectiveAtDisplaySlot`


///

```js
getObjectiveAtDisplaySlot(displaySlotId: DisplaySlotId): ScoreboardObjectiveDisplayOptions | undefined
```


/// define
`getObjectives`


///

```js
getObjectives(): ScoreboardObjective[]
```


/// define
`getParticipants`


///

```js
getParticipants(): ScoreboardIdentity[]
```


/// define
`removeObjective`


///

```js
removeObjective(objectiveId: ScoreboardObjective | string): boolean
```


/// define
`setObjectiveAtDisplaySlot`


///

```js
setObjectiveAtDisplaySlot(displaySlotId: DisplaySlotId, objectiveDisplaySetting: ScoreboardObjectiveDisplayOptions): ScoreboardObjective | undefined
```

