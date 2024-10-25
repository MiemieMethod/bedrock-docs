# `Block`

> 文档版本：1.21.50.25

`Block`类。script_api.mojang-minecraft.block.description

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

- script_api.mojang-minecraft.block.dimension.description


////

///


/// define
`id`


///

```js
read-only id: string;
```

/// html | div.result
//// define
`id`：`string`

- script_api.mojang-minecraft.block.id.description


////

///


/// define
`isEmpty`


///

```js
read-only isEmpty: boolean;
```

/// html | div.result
//// define
`isEmpty`：`boolean`

- script_api.mojang-minecraft.block.isempty.description


////

///


/// define
`isWaterlogged`


///

```js
isWaterlogged: boolean;
```

/// html | div.result
//// define
`isWaterlogged`：`boolean`

- script_api.mojang-minecraft.block.iswaterlogged.description


////

///


/// define
`location`


///

```js
read-only location: BlockLocation;
```

/// html | div.result
//// define
`location`：[`BlockLocation`](./blocklocation.md)

- script_api.mojang-minecraft.block.location.description


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

- script_api.mojang-minecraft.block.permutation.description


////

///


/// define
`type`


///

```js
read-only type: BlockType;
```

/// html | div.result
//// define
`type`：[`BlockType`](./blocktype.md)

- script_api.mojang-minecraft.block.type.description


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

- script_api.mojang-minecraft.block.x.description


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

- script_api.mojang-minecraft.block.y.description


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

- script_api.mojang-minecraft.block.z.description


////

///


## 方法

/// define
`getComponent`


///

script_api.mojang-minecraft.block.getcomponent.description

```js
getComponent(componentName: string): BlockComponent | undefined
```

/// html | div.result
//// define
`componentName`：`string`

- script_api.mojang-minecraft.block.getcomponent.componentname.description


////

//// define
返回值：[`BlockComponent`](./blockcomponent.md)|`undefined`

- script_api.mojang-minecraft.block.getcomponent.return


////

///


/// define
`getTags`


///

script_api.mojang-minecraft.block.gettags.description

```js
getTags(): string[]
```

/// html | div.result
//// define
返回值：`string[]`

- script_api.mojang-minecraft.block.gettags.return


////

///


/// define
`hasTag`


///

script_api.mojang-minecraft.block.hastag.description

```js
hasTag(tag: string): boolean
```

/// html | div.result
//// define
`tag`：`string`

- script_api.mojang-minecraft.block.hastag.tag.description


////

//// define
返回值：`boolean`

- script_api.mojang-minecraft.block.hastag.return


////

///


/// define
`setPermutation`


///

script_api.mojang-minecraft.block.setpermutation.description

```js
setPermutation(permutation: BlockPermutation): void
```

/// html | div.result
//// define
`permutation`：[`BlockPermutation`](./blockpermutation.md)

- script_api.mojang-minecraft.block.setpermutation.permutation.description


////

//// define
返回值：`void`

- script_api.mojang-minecraft.block.setpermutation.return


////

///


/// define
`setType`


///

script_api.mojang-minecraft.block.settype.description

```js
setType(blockType: BlockType): void
```

/// html | div.result
//// define
`blockType`：[`BlockType`](./blocktype.md)

- script_api.mojang-minecraft.block.settype.blocktype.description


////

//// define
返回值：`void`

- script_api.mojang-minecraft.block.settype.return


////

///

