# `StructureManager`

> 文档版本：1.21.50.25

`StructureManager`类。script_api.@minecraft/server.structuremanager.description

## 方法

/// define
`createEmpty`


///

script_api.@minecraft/server.structuremanager.createempty.description

```js
createEmpty(identifier: string, size: Vector3, saveMode: StructureSaveMode): Structure
```

/// html | div.result
//// define
`identifier`：`string`

- script_api.@minecraft/server.structuremanager.createempty.identifier.description


////

//// define
`size`：[`Vector3`](./vector3.md)

- script_api.@minecraft/server.structuremanager.createempty.size.description


////

//// define
`saveMode`：[`StructureSaveMode`](./structuresavemode.md)＝`0`

- script_api.@minecraft/server.structuremanager.createempty.savemode.description


////

//// define
返回值：[`Structure`](./structure.md)

- script_api.@minecraft/server.structuremanager.createempty.return


////

///


/// define
`createFromWorld`


///

script_api.@minecraft/server.structuremanager.createfromworld.description

```js
createFromWorld(identifier: string, dimension: Dimension, from: Vector3, to: Vector3, options?: StructureCreateOptions): Structure
```

/// html | div.result
//// define
`identifier`：`string`

- script_api.@minecraft/server.structuremanager.createfromworld.identifier.description


////

//// define
`dimension`：[`Dimension`](./dimension.md)

- script_api.@minecraft/server.structuremanager.createfromworld.dimension.description


////

//// define
`from`：[`Vector3`](./vector3.md)

- script_api.@minecraft/server.structuremanager.createfromworld.from.description


////

//// define
`to`：[`Vector3`](./vector3.md)

- script_api.@minecraft/server.structuremanager.createfromworld.to.description


////

//// define
`options`?：[`StructureCreateOptions`](./structurecreateoptions.md)＝`null`

- script_api.@minecraft/server.structuremanager.createfromworld.options.description


////

//// define
返回值：[`Structure`](./structure.md)

- script_api.@minecraft/server.structuremanager.createfromworld.return


////

///


/// define
`delete`


///

script_api.@minecraft/server.structuremanager.delete.description

```js
delete(structure: string | Structure): boolean
```

/// html | div.result
//// define
`structure`：`string`|[`Structure`](./structure.md)

- script_api.@minecraft/server.structuremanager.delete.structure.description


////

//// define
返回值：`boolean`

- script_api.@minecraft/server.structuremanager.delete.return


////

///


/// define
`get`


///

script_api.@minecraft/server.structuremanager.get.description

```js
get(identifier: string): Structure | undefined
```

/// html | div.result
//// define
`identifier`：`string`

- script_api.@minecraft/server.structuremanager.get.identifier.description


////

//// define
返回值：[`Structure`](./structure.md)|`undefined`

- script_api.@minecraft/server.structuremanager.get.return


////

///


/// define
`getWorldStructureIds`


///

script_api.@minecraft/server.structuremanager.getworldstructureids.description

```js
getWorldStructureIds(): string[]
```

/// html | div.result
//// define
返回值：`string[]`

- script_api.@minecraft/server.structuremanager.getworldstructureids.return


////

///


/// define
`place`


///

script_api.@minecraft/server.structuremanager.place.description

```js
place(structure: string | Structure, dimension: Dimension, location: Vector3, options?: StructurePlaceOptions): void
```

/// html | div.result
//// define
`structure`：`string`|[`Structure`](./structure.md)

- script_api.@minecraft/server.structuremanager.place.structure.description


////

//// define
`dimension`：[`Dimension`](./dimension.md)

- script_api.@minecraft/server.structuremanager.place.dimension.description


////

//// define
`location`：[`Vector3`](./vector3.md)

- script_api.@minecraft/server.structuremanager.place.location.description


////

//// define
`options`?：[`StructurePlaceOptions`](./structureplaceoptions.md)＝`null`

- script_api.@minecraft/server.structuremanager.place.options.description


////

//// define
返回值：`void`

- script_api.@minecraft/server.structuremanager.place.return


////

///


/// define
`placeJigsaw`


///

script_api.@minecraft/server.structuremanager.placejigsaw.description

```js
placeJigsaw(pool: string, targetJigsaw: string, maxDepth: int32, dimension: Dimension, location: Vector3, options?: JigsawPlaceOptions): void
```

/// html | div.result
//// define
`pool`：`string`

- script_api.@minecraft/server.structuremanager.placejigsaw.pool.description


////

//// define
`targetJigsaw`：`string`

- script_api.@minecraft/server.structuremanager.placejigsaw.targetjigsaw.description


////

//// define
`maxDepth`：`int32`∈[`1`, `20`]

- script_api.@minecraft/server.structuremanager.placejigsaw.maxdepth.description


////

//// define
`dimension`：[`Dimension`](./dimension.md)

- script_api.@minecraft/server.structuremanager.placejigsaw.dimension.description


////

//// define
`location`：[`Vector3`](./vector3.md)

- script_api.@minecraft/server.structuremanager.placejigsaw.location.description


////

//// define
`options`?：[`JigsawPlaceOptions`](./jigsawplaceoptions.md)＝`null`

- script_api.@minecraft/server.structuremanager.placejigsaw.options.description


////

//// define
返回值：`void`

- script_api.@minecraft/server.structuremanager.placejigsaw.return


////

///


/// define
`placeJigsawStructure`


///

script_api.@minecraft/server.structuremanager.placejigsawstructure.description

```js
placeJigsawStructure(identifier: string, dimension: Dimension, location: Vector3, options?: JigsawStructurePlaceOptions): void
```

/// html | div.result
//// define
`identifier`：`string`

- script_api.@minecraft/server.structuremanager.placejigsawstructure.identifier.description


////

//// define
`dimension`：[`Dimension`](./dimension.md)

- script_api.@minecraft/server.structuremanager.placejigsawstructure.dimension.description


////

//// define
`location`：[`Vector3`](./vector3.md)

- script_api.@minecraft/server.structuremanager.placejigsawstructure.location.description


////

//// define
`options`?：[`JigsawStructurePlaceOptions`](./jigsawstructureplaceoptions.md)＝`null`

- script_api.@minecraft/server.structuremanager.placejigsawstructure.options.description


////

//// define
返回值：`void`

- script_api.@minecraft/server.structuremanager.placejigsawstructure.return


////

///

