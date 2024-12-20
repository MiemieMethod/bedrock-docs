# `Structure`

> 文档版本：1.21.60.21

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

- script_api.@minecraft/server.structure.getblockpermutation.location.description


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

- script_api.@minecraft/server.structure.getiswaterlogged.location.description


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

- script_api.@minecraft/server.structure.saveas.identifier.description


////

//// define
`saveMode`：[`StructureSaveMode`](./structuresavemode.md)＝`1`

- script_api.@minecraft/server.structure.saveas.savemode.description


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
setBlockPermutation(location: Vector3, blockPermutation?: BlockPermutation): void
```

/// html | div.result
//// define
`location`：[`Vector3`](./vector3.md)

- script_api.@minecraft/server.structure.setblockpermutation.location.description


////

//// define
`blockPermutation`?：[`BlockPermutation`](./blockpermutation.md)＝`null`

- script_api.@minecraft/server.structure.setblockpermutation.blockpermutation.description


////

//// define
返回值：`void`

- script_api.@minecraft/server.structure.setblockpermutation.return


////

///

