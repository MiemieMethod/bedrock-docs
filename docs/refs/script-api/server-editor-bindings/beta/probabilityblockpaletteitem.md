# `ProbabilityBlockPaletteItem`

> 文档版本：1.21.50.25

`ProbabilityBlockPaletteItem`类，扩展自[`IBlockPaletteItem`](./iblockpaletteitem.md)。script_api.@minecraft/server-editor-bindings.probabilityblockpaletteitem.description

## 方法

/// define
`addBlock`


///

script_api.@minecraft/server-editor-bindings.probabilityblockpaletteitem.addblock.description

```js
addBlock(block: BlockPermutation | BlockType | string, weight: int32): void
```

/// html | div.result
//// define
`block`：[`BlockPermutation`](../../server/beta/blockpermutation.md)|[`BlockType`](../../server/beta/blocktype.md)|`string`

- script_api.@minecraft/server-editor-bindings.probabilityblockpaletteitem.addblock.block.description


////

//// define
`weight`：`int32`∈[`1`, `100`]

- script_api.@minecraft/server-editor-bindings.probabilityblockpaletteitem.addblock.weight.description


////

//// define
返回值：`void`

- script_api.@minecraft/server-editor-bindings.probabilityblockpaletteitem.addblock.return


////

///


/// define
`constructor`


///

script_api.@minecraft/server-editor-bindings.probabilityblockpaletteitem.constructor.description

```js
new constructor(displayName?: string): ProbabilityBlockPaletteItem
```

/// html | div.result
//// define
`displayName`?：`string`＝`null`

- script_api.@minecraft/server-editor-bindings.probabilityblockpaletteitem.constructor.displayname.description


////

//// define
返回值：[`ProbabilityBlockPaletteItem`](./probabilityblockpaletteitem.md)

- script_api.@minecraft/server-editor-bindings.probabilityblockpaletteitem.constructor.return


////

///


/// define
`getBlocks`


///

script_api.@minecraft/server-editor-bindings.probabilityblockpaletteitem.getblocks.description

```js
getBlocks(): WeightedBlock[]
```

/// html | div.result
//// define
返回值：<code><a href="../weightedblock/">WeightedBlock</a>[]</code>

- script_api.@minecraft/server-editor-bindings.probabilityblockpaletteitem.getblocks.return


////

///


/// define
`removeBlockAt`


///

script_api.@minecraft/server-editor-bindings.probabilityblockpaletteitem.removeblockat.description

```js
removeBlockAt(index: int32): void
```

/// html | div.result
//// define
`index`：`int32`

- script_api.@minecraft/server-editor-bindings.probabilityblockpaletteitem.removeblockat.index.description


////

//// define
返回值：`void`

- script_api.@minecraft/server-editor-bindings.probabilityblockpaletteitem.removeblockat.return


////

///

