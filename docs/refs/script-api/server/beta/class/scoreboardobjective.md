# `ScoreboardObjective`

> 文档版本：1.21.0.20

`ScoreboardObjective`类。

## 属性

/// define
`displayName`


///

```js
read-only displayName: string;
```


/// define
`id`


///

```js
read-only id: string;
```


## 方法

/// define
`addScore`


///

```js
addScore(participant: Entity | ScoreboardIdentity | string, scoreToAdd: int32): int32
```


/// define
`getParticipants`


///

```js
getParticipants(): ScoreboardIdentity[]
```


/// define
`getScore`


///

```js
getScore(participant: Entity | ScoreboardIdentity | string): int32 | undefined
```


/// define
`getScores`


///

```js
getScores(): ScoreboardScoreInfo[]
```


/// define
`hasParticipant`


///

```js
hasParticipant(participant: Entity | ScoreboardIdentity | string): boolean
```


/// define
`isValid`


///

```js
isValid(): boolean
```


/// define
`removeParticipant`


///

```js
removeParticipant(participant: Entity | ScoreboardIdentity | string): boolean
```


/// define
`setScore`


///

```js
setScore(participant: Entity | ScoreboardIdentity | string, score: int32): void
```

