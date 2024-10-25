# `Structure`

> 文档版本：1.21.50.25

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

