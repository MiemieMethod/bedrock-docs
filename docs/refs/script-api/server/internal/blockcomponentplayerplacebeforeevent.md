# `BlockComponentPlayerPlaceBeforeEvent`

> 文档版本：1.21.50.25

`BlockComponentPlayerPlaceBeforeEvent`类，扩展自[`BlockEvent`](./blockevent.md)。包含玩家放置方块前的事件信息。

## 属性

/// define
`cancel`


///

```js
cancel: boolean;
```

/// html | div.result
//// define
`cancel`：`boolean`

- 如果设置为`true`，则可取消本次方块放置事件。


////

///


/// define
`face`


///

```js
read-only face: Direction;
```

/// html | div.result
//// define
`face`：[`Direction`](./direction.md)

- 该方块被放置到的面（即玩家放置该方块时点击的面）。


////

///


/// define
`permutationToPlace`


///

```js
permutationToPlace: BlockPermutation;
```

/// html | div.result
//// define
`permutationToPlace`：[`BlockPermutation`](./blockpermutation.md)

- 该方块被放置时将要设置的置换。


////

///


/// define
`player`


///

```js
read-only player: Player | undefined;
```

/// html | div.result
//// define
`player`：[`Player`](./player.md)|`undefined`

- 正在放置该方块的玩家。


////

///

