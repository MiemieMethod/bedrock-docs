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

/// html | div.result
//// define
`participant`：[`Entity`](../entity.md)|[`ScoreboardIdentity`](../scoreboardidentity.md)|`string`

- 参数1。


////

//// define
`scoreToAdd`：`int32`

- 参数2。


////

//// define
返回值：`int32`

- 返回值。


////

///


/// define
`getParticipants`


///

```js
getParticipants(): ScoreboardIdentity[]
```

/// html | div.result
//// define
返回值：<code><a href="../scoreboardidentity/">ScoreboardIdentity</a>[]</code>

- 返回值。


////

///


/// define
`getScore`


///

```js
getScore(participant: Entity | ScoreboardIdentity | string): int32 | undefined
```

/// html | div.result
//// define
`participant`：[`Entity`](../entity.md)|[`ScoreboardIdentity`](../scoreboardidentity.md)|`string`

- 参数1。


////

//// define
返回值：`int32`|`undefined`

- 返回值。


////

///


/// define
`getScores`


///

```js
getScores(): ScoreboardScoreInfo[]
```

/// html | div.result
//// define
返回值：<code><a href="../scoreboardscoreinfo/">ScoreboardScoreInfo</a>[]</code>

- 返回值。


////

///


/// define
`hasParticipant`


///

```js
hasParticipant(participant: Entity | ScoreboardIdentity | string): boolean
```

/// html | div.result
//// define
`participant`：[`Entity`](../entity.md)|[`ScoreboardIdentity`](../scoreboardidentity.md)|`string`

- 参数1。


////

//// define
返回值：`boolean`

- 返回值。


////

///


/// define
`isValid`


///

```js
isValid(): boolean
```

/// html | div.result
//// define
返回值：`boolean`

- 返回值。


////

///


/// define
`removeParticipant`


///

```js
removeParticipant(participant: Entity | ScoreboardIdentity | string): boolean
```

/// html | div.result
//// define
`participant`：[`Entity`](../entity.md)|[`ScoreboardIdentity`](../scoreboardidentity.md)|`string`

- 参数1。


////

//// define
返回值：`boolean`

- 返回值。


////

///


/// define
`setScore`


///

```js
setScore(participant: Entity | ScoreboardIdentity | string, score: int32): void
```

/// html | div.result
//// define
`participant`：[`Entity`](../entity.md)|[`ScoreboardIdentity`](../scoreboardidentity.md)|`string`

- 参数1。


////

//// define
`score`：`int32`

- 参数2。


////

//// define
返回值：`void`

- 返回值。


////

///

