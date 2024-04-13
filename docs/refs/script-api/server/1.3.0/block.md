# `Block`

> 文档版本：1.21.0.21

`Block`类。script_api.@minecraft/server.block.description

## 属性

/// define
`dimension`


///

```js
read-only dimension: Dimension;
```

/// html | div.result
//// define
`dimension`：[`Dimension`](./dimension.md)

- script_api.@minecraft/server.block.dimension.description


////

///


/// define
`location`


///

```js
read-only location: Vector3;
```

/// html | div.result
//// define
`location`：[`Vector3`](./vector3.md)

- script_api.@minecraft/server.block.location.description


////

///


/// define
`permutation`


///

```js
read-only permutation: BlockPermutation;
```

/// html | div.result
//// define
`permutation`：[`BlockPermutation`](./blockpermutation.md)

- script_api.@minecraft/server.block.permutation.description


////

///


/// define
`x`


///

```js
read-only x: int32;
```

/// html | div.result
//// define
`x`：`int32`

- script_api.@minecraft/server.block.x.description


////

///


/// define
`y`


///

```js
read-only y: int32;
```

/// html | div.result
//// define
`y`：`int32`

- script_api.@minecraft/server.block.y.description


////

///


/// define
`z`


///

```js
read-only z: int32;
```

/// html | div.result
//// define
`z`：`int32`

- script_api.@minecraft/server.block.z.description


////

///


## 方法

/// define
`getComponent`


///

script_api.@minecraft/server.block.getcomponent.description

```js
getComponent(componentId: string): BlockComponent | undefined
```

/// html | div.result
//// define
`componentId`：`string`

- script_api.@minecraft/server.block.getcomponent.componentid.description


////

//// define
返回值：[`BlockComponent`](./blockcomponent.md)|`undefined`

- script_api.@minecraft/server.block.getcomponent.return


////

///


/// define
`setPermutation`


///

script_api.@minecraft/server.block.setpermutation.description

```js
setPermutation(permutation: BlockPermutation): void
```

/// html | div.result
//// define
`permutation`：[`BlockPermutation`](./blockpermutation.md)

- script_api.@minecraft/server.block.setpermutation.permutation.description


////

//// define
返回值：`void`

- script_api.@minecraft/server.block.setpermutation.return


////

///

