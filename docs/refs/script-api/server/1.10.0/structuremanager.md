# `StructureManager`

> 文档版本：1.21.60.21

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

