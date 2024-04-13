# `BlockPermutation`

> 文档版本：1.21.0.21

`BlockPermutation`类。script_api.@minecraft/server.blockpermutation.description

## 属性

/// define
`type`


///

```js
read-only type: BlockType;
```

/// html | div.result
//// define
`type`：[`BlockType`](./blocktype.md)

- script_api.@minecraft/server.blockpermutation.type.description


////

///


## 方法

/// define
`getAllStates`


///

script_api.@minecraft/server.blockpermutation.getallstates.description

```js
getAllStates(): Record<string, boolean | int32 | string>
```

/// html | div.result
//// define
返回值：`Record<string, boolean | int32 | string>`

- script_api.@minecraft/server.blockpermutation.getallstates.return


////

///


/// define
`getItemStack`


///

script_api.@minecraft/server.blockpermutation.getitemstack.description

```js
getItemStack(amount: int32): ItemStack | undefined
```

/// html | div.result
//// define
`amount`：`int32`

- script_api.@minecraft/server.blockpermutation.getitemstack.amount.description


////

//// define
返回值：[`ItemStack`](./itemstack.md)|`undefined`

- script_api.@minecraft/server.blockpermutation.getitemstack.return


////

///


/// define
`getState`


///

script_api.@minecraft/server.blockpermutation.getstate.description

```js
getState(stateName: string): boolean | int32 | string | undefined
```

/// html | div.result
//// define
`stateName`：`string`

- script_api.@minecraft/server.blockpermutation.getstate.statename.description


////

//// define
返回值：`boolean`|`int32`|`string`|`undefined`

- script_api.@minecraft/server.blockpermutation.getstate.return


////

///


/// define
`getTags`


///

script_api.@minecraft/server.blockpermutation.gettags.description

```js
getTags(): string[]
```

/// html | div.result
//// define
返回值：`string[]`

- script_api.@minecraft/server.blockpermutation.gettags.return


////

///


/// define
`hasTag`


///

script_api.@minecraft/server.blockpermutation.hastag.description

```js
hasTag(tag: string): boolean
```

/// html | div.result
//// define
`tag`：`string`

- script_api.@minecraft/server.blockpermutation.hastag.tag.description


////

//// define
返回值：`boolean`

- script_api.@minecraft/server.blockpermutation.hastag.return


////

///


/// define
`matches`


///

script_api.@minecraft/server.blockpermutation.matches.description

```js
matches(blockName: string, states?: Record<string, boolean | int32 | string>): boolean
```

/// html | div.result
//// define
`blockName`：`string`

- script_api.@minecraft/server.blockpermutation.matches.blockname.description


////

//// define
`states`：`Record<string, boolean | int32 | string>`|`undefined`

- script_api.@minecraft/server.blockpermutation.matches.states.description


////

//// define
返回值：`boolean`

- script_api.@minecraft/server.blockpermutation.matches.return


////

///


/// define
`resolve`


///

script_api.@minecraft/server.blockpermutation.resolve.description

```js
static resolve(blockName: string, states?: Record<string, boolean | int32 | string>): BlockPermutation
```

/// html | div.result
//// define
`blockName`：`string`

- script_api.@minecraft/server.blockpermutation.resolve.blockname.description


////

//// define
`states`：`Record<string, boolean | int32 | string>`|`undefined`

- script_api.@minecraft/server.blockpermutation.resolve.states.description


////

//// define
返回值：[`BlockPermutation`](./blockpermutation.md)

- script_api.@minecraft/server.blockpermutation.resolve.return


////

///


/// define
`withState`


///

script_api.@minecraft/server.blockpermutation.withstate.description

```js
withState(name: string, value: boolean | int32 | string): BlockPermutation
```

/// html | div.result
//// define
`name`：`string`

- script_api.@minecraft/server.blockpermutation.withstate.name.description


////

//// define
`value`：`boolean`|`int32`|`string`

- script_api.@minecraft/server.blockpermutation.withstate.value.description


////

//// define
返回值：[`BlockPermutation`](./blockpermutation.md)

- script_api.@minecraft/server.blockpermutation.withstate.return


////

///

