# `Block`

> 文档版本：1.21.0.20

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
`isAir`


///

```js
read-only isAir: boolean;
```

/// html | div.result
//// define
`isAir`：`boolean`

- script_api.@minecraft/server.block.isair.description


////

///


/// define
`isLiquid`


///

```js
read-only isLiquid: boolean;
```

/// html | div.result
//// define
`isLiquid`：`boolean`

- script_api.@minecraft/server.block.isliquid.description


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
`above`


///

script_api.@minecraft/server.block.above.description

```js
above(steps: int32): Block | undefined
```

/// html | div.result
//// define
`steps`：`int32`

- script_api.@minecraft/server.block.steps.above.description


////

//// define
返回值：[`Block`](./block.md)|`undefined`

- script_api.@minecraft/server.block.above.return


////

///


/// define
`below`


///

script_api.@minecraft/server.block.below.description

```js
below(steps: int32): Block | undefined
```

/// html | div.result
//// define
`steps`：`int32`

- script_api.@minecraft/server.block.steps.below.description


////

//// define
返回值：[`Block`](./block.md)|`undefined`

- script_api.@minecraft/server.block.below.return


////

///


/// define
`bottomCenter`


///

script_api.@minecraft/server.block.bottomcenter.description

```js
bottomCenter(): Vector3
```

/// html | div.result
//// define
返回值：[`Vector3`](./vector3.md)

- script_api.@minecraft/server.block.bottomcenter.return


////

///


/// define
`center`


///

script_api.@minecraft/server.block.center.description

```js
center(): Vector3
```

/// html | div.result
//// define
返回值：[`Vector3`](./vector3.md)

- script_api.@minecraft/server.block.center.return


////

///


/// define
`east`


///

script_api.@minecraft/server.block.east.description

```js
east(steps: int32): Block | undefined
```

/// html | div.result
//// define
`steps`：`int32`

- script_api.@minecraft/server.block.steps.east.description


////

//// define
返回值：[`Block`](./block.md)|`undefined`

- script_api.@minecraft/server.block.east.return


////

///


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

- script_api.@minecraft/server.block.componentid.getcomponent.description


////

//// define
返回值：[`BlockComponent`](./blockcomponent.md)|`undefined`

- script_api.@minecraft/server.block.getcomponent.return


////

///


/// define
`getTags`


///

script_api.@minecraft/server.block.gettags.description

```js
getTags(): string[]
```

/// html | div.result
//// define
返回值：`string[]`

- script_api.@minecraft/server.block.gettags.return


////

///


/// define
`hasTag`


///

script_api.@minecraft/server.block.hastag.description

```js
hasTag(tag: string): boolean
```

/// html | div.result
//// define
`tag`：`string`

- script_api.@minecraft/server.block.tag.hastag.description


////

//// define
返回值：`boolean`

- script_api.@minecraft/server.block.hastag.return


////

///


/// define
`isValid`


///

script_api.@minecraft/server.block.isvalid.description

```js
isValid(): boolean
```

/// html | div.result
//// define
返回值：`boolean`

- script_api.@minecraft/server.block.isvalid.return


////

///


/// define
`north`


///

script_api.@minecraft/server.block.north.description

```js
north(steps: int32): Block | undefined
```

/// html | div.result
//// define
`steps`：`int32`

- script_api.@minecraft/server.block.steps.north.description


////

//// define
返回值：[`Block`](./block.md)|`undefined`

- script_api.@minecraft/server.block.north.return


////

///


/// define
`offset`


///

script_api.@minecraft/server.block.offset.description

```js
offset(offset: Vector3): Block | undefined
```

/// html | div.result
//// define
`offset`：[`Vector3`](./vector3.md)

- script_api.@minecraft/server.block.offset.offset.description


////

//// define
返回值：[`Block`](./block.md)|`undefined`

- script_api.@minecraft/server.block.offset.return


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

- script_api.@minecraft/server.block.permutation.setpermutation.description


////

//// define
返回值：`void`

- script_api.@minecraft/server.block.setpermutation.return


////

///


/// define
`south`


///

script_api.@minecraft/server.block.south.description

```js
south(steps: int32): Block | undefined
```

/// html | div.result
//// define
`steps`：`int32`

- script_api.@minecraft/server.block.steps.south.description


////

//// define
返回值：[`Block`](./block.md)|`undefined`

- script_api.@minecraft/server.block.south.return


////

///


/// define
`west`


///

script_api.@minecraft/server.block.west.description

```js
west(steps: int32): Block | undefined
```

/// html | div.result
//// define
`steps`：`int32`

- script_api.@minecraft/server.block.steps.west.description


////

//// define
返回值：[`Block`](./block.md)|`undefined`

- script_api.@minecraft/server.block.west.return


////

///

