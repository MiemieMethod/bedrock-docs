# `BlockComponentPlayerInteractEvent`

> 文档版本：1.21.0.21

`BlockComponentPlayerInteractEvent`类，扩展自[`BlockEvent`](./blockevent.md)。包含被玩家互动的方块的信息。

## 属性

/// define
`face`


///

```js
read-only face: Direction;
```

/// html | div.result
//// define
`face`：[`Direction`](./direction.md)

- 该方块参与互动的面。


////

///


/// define
`faceLocation`


///

```js
read-only faceLocation: Vector3 | undefined;
```

/// html | div.result
//// define
`faceLocation`：[`Vector3`](./vector3.md)|`undefined`

- 玩家互动时点击的位置（以该方块底部西北角顶点为坐标原点）。


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

- 互动该方块的玩家。


////

///

