# `BlockComponentPlayerDestroyEvent`

> 文档版本：1.21.50.25

`BlockComponentPlayerDestroyEvent`类，扩展自[`BlockEvent`](./blockevent.md)。包含被玩家破坏的方块的信息。

## 属性

/// define
`destroyedBlockPermutation`


///

```js
read-only destroyedBlockPermutation: BlockPermutation;
```

/// html | div.result
//// define
`destroyedBlockPermutation`：[`BlockPermutation`](./blockpermutation.md)

- 被玩家破坏的方块的置换。


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

- 破坏该方块的玩家。


////

///

