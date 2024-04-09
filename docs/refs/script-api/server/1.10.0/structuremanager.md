# `StructureManager`

> 文档版本：1.21.0.20

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

- script_api.@minecraft/server.structuremanager.identifier.createempty.description


////

//// define
`size`：[`Vector3`](./vector3.md)

- script_api.@minecraft/server.structuremanager.size.createempty.description


////

//// define
`saveMode`：[`StructureSaveMode`](./structuresavemode.md)

- script_api.@minecraft/server.structuremanager.savemode.createempty.description


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

- script_api.@minecraft/server.structuremanager.structure.delete.description


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

- script_api.@minecraft/server.structuremanager.identifier.get.description


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

- script_api.@minecraft/server.structuremanager.structure.place.description


////

//// define
`dimension`：[`Dimension`](./dimension.md)

- script_api.@minecraft/server.structuremanager.dimension.place.description


////

//// define
`location`：[`Vector3`](./vector3.md)

- script_api.@minecraft/server.structuremanager.location.place.description


////

//// define
`options`：[`StructurePlaceOptions`](./structureplaceoptions.md)|`undefined`

- script_api.@minecraft/server.structuremanager.options.place.description


////

//// define
返回值：`void`

- script_api.@minecraft/server.structuremanager.place.return


////

///

