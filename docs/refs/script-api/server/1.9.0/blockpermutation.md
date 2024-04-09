# `BlockPermutation`

> 文档版本：1.21.0.20

`BlockPermutation`类。script_api.@minecraft/server.blockpermutation.description

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
`getState`


///

script_api.@minecraft/server.blockpermutation.getstate.description

```js
getState(stateName: string): boolean | int32 | string | undefined
```

/// html | div.result
//// define
`stateName`：`string`

- script_api.@minecraft/server.blockpermutation.statename.getstate.description


////

//// define
返回值：`boolean`|`int32`|`string`|`undefined`

- script_api.@minecraft/server.blockpermutation.getstate.return


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

- script_api.@minecraft/server.blockpermutation.blockname.matches.description


////

//// define
`states`：`Record<string, boolean | int32 | string>`|`undefined`

- script_api.@minecraft/server.blockpermutation.states.matches.description


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

- script_api.@minecraft/server.blockpermutation.blockname.resolve.description


////

//// define
`states`：`Record<string, boolean | int32 | string>`|`undefined`

- script_api.@minecraft/server.blockpermutation.states.resolve.description


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

- script_api.@minecraft/server.blockpermutation.name.withstate.description


////

//// define
`value`：`boolean`|`int32`|`string`

- script_api.@minecraft/server.blockpermutation.value.withstate.description


////

//// define
返回值：[`BlockPermutation`](./blockpermutation.md)

- script_api.@minecraft/server.blockpermutation.withstate.return


////

///

