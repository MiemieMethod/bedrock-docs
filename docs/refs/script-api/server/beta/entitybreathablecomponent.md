# `EntityBreathableComponent`

> 文档版本：1.21.0.20

`EntityBreathableComponent`类，扩展自[`EntityComponent`](./entitycomponent.md)。

## 常量

/// define
`componentId`


///

```js
static read-only componentId = "minecraft:breathable";
```


## 属性

/// define
`breathesAir`


///

```js
read-only breathesAir: boolean;
```

/// html | div.result
//// define
`breathesAir`：`boolean`

- 属性。


////

///


/// define
`breathesLava`


///

```js
read-only breathesLava: boolean;
```

/// html | div.result
//// define
`breathesLava`：`boolean`

- 属性。


////

///


/// define
`breathesSolids`


///

```js
read-only breathesSolids: boolean;
```

/// html | div.result
//// define
`breathesSolids`：`boolean`

- 属性。


////

///


/// define
`breathesWater`


///

```js
read-only breathesWater: boolean;
```

/// html | div.result
//// define
`breathesWater`：`boolean`

- 属性。


////

///


/// define
`generatesBubbles`


///

```js
read-only generatesBubbles: boolean;
```

/// html | div.result
//// define
`generatesBubbles`：`boolean`

- 属性。


////

///


/// define
`inhaleTime`


///

```js
read-only inhaleTime: float;
```

/// html | div.result
//// define
`inhaleTime`：`float`

- 属性。


////

///


/// define
`suffocateTime`


///

```js
read-only suffocateTime: int32;
```

/// html | div.result
//// define
`suffocateTime`：`int32`

- 属性。


////

///


/// define
`totalSupply`


///

```js
read-only totalSupply: int32;
```

/// html | div.result
//// define
`totalSupply`：`int32`

- 属性。


////

///


## 方法

/// define
`getBreatheBlocks`


///

```js
getBreatheBlocks(): BlockPermutation[]
```

/// html | div.result
//// define
返回值：<code><a href="../blockpermutation/">BlockPermutation</a>[]</code>

- 返回值。


////

///


/// define
`getNonBreatheBlocks`


///

```js
getNonBreatheBlocks(): BlockPermutation[]
```

/// html | div.result
//// define
返回值：<code><a href="../blockpermutation/">BlockPermutation</a>[]</code>

- 返回值。


////

///


/// define
`setAirSupply`


///

```js
setAirSupply(value: int16): void
```

/// html | div.result
//// define
`value`：`int16`

- 参数1。


////

//// define
返回值：`void`

- 返回值。


////

///

