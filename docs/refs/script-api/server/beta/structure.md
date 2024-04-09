# `Structure`

> 文档版本：1.21.0.20

`Structure`类。script_api.@minecraft/server.structure.description

## 属性

/// define
`id`


///

```js
read-only id: string;
```

/// html | div.result
//// define
`id`：`string`

- script_api.@minecraft/server.structure.id.description


////

///


/// define
`size`


///

```js
read-only size: Vector3;
```

/// html | div.result
//// define
`size`：[`Vector3`](./vector3.md)

- script_api.@minecraft/server.structure.size.description


////

///


## 方法

/// define
`getBlockPermutation`


///

script_api.@minecraft/server.structure.getblockpermutation.description

```js
getBlockPermutation(location: Vector3): BlockPermutation | undefined
```

/// html | div.result
//// define
`location`：[`Vector3`](./vector3.md)

- script_api.@minecraft/server.structure.location.getblockpermutation.description


////

//// define
返回值：[`BlockPermutation`](./blockpermutation.md)|`undefined`

- script_api.@minecraft/server.structure.getblockpermutation.return


////

///


/// define
`getIsWaterlogged`


///

script_api.@minecraft/server.structure.getiswaterlogged.description

```js
getIsWaterlogged(location: Vector3): boolean
```

/// html | div.result
//// define
`location`：[`Vector3`](./vector3.md)

- script_api.@minecraft/server.structure.location.getiswaterlogged.description


////

//// define
返回值：`boolean`

- script_api.@minecraft/server.structure.getiswaterlogged.return


////

///


/// define
`isValid`


///

script_api.@minecraft/server.structure.isvalid.description

```js
isValid(): boolean
```

/// html | div.result
//// define
返回值：`boolean`

- script_api.@minecraft/server.structure.isvalid.return


////

///


/// define
`saveAs`


///

script_api.@minecraft/server.structure.saveas.description

```js
saveAs(identifier: string, saveMode: StructureSaveMode): Structure
```

/// html | div.result
//// define
`identifier`：`string`

- script_api.@minecraft/server.structure.identifier.saveas.description


////

//// define
`saveMode`：[`StructureSaveMode`](./structuresavemode.md)

- script_api.@minecraft/server.structure.savemode.saveas.description


////

//// define
返回值：[`Structure`](./structure.md)

- script_api.@minecraft/server.structure.saveas.return


////

///


/// define
`saveToWorld`


///

script_api.@minecraft/server.structure.savetoworld.description

```js
saveToWorld(): void
```

/// html | div.result
//// define
返回值：`void`

- script_api.@minecraft/server.structure.savetoworld.return


////

///


/// define
`setBlockPermutation`


///

script_api.@minecraft/server.structure.setblockpermutation.description

```js
setBlockPermutation(location: Vector3, blockPermutation?: BlockPermutation, waterlogged: boolean): void
```

/// html | div.result
//// define
`location`：[`Vector3`](./vector3.md)

- script_api.@minecraft/server.structure.location.setblockpermutation.description


////

//// define
`blockPermutation`：[`BlockPermutation`](./blockpermutation.md)|`undefined`

- script_api.@minecraft/server.structure.blockpermutation.setblockpermutation.description


////

//// define
`waterlogged`：`boolean`

- script_api.@minecraft/server.structure.waterlogged.setblockpermutation.description


////

//// define
返回值：`void`

- script_api.@minecraft/server.structure.setblockpermutation.return


////

///

