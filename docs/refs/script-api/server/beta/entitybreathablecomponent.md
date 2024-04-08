# `EntityBreathableComponent`

> 文档版本：1.21.0.20

`EntityBreathableComponent`类，扩展自`EntityComponent`。

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


/// define
`breathesLava`


///

```js
read-only breathesLava: boolean;
```


/// define
`breathesSolids`


///

```js
read-only breathesSolids: boolean;
```


/// define
`breathesWater`


///

```js
read-only breathesWater: boolean;
```


/// define
`generatesBubbles`


///

```js
read-only generatesBubbles: boolean;
```


/// define
`inhaleTime`


///

```js
read-only inhaleTime: float;
```


/// define
`suffocateTime`


///

```js
read-only suffocateTime: int32;
```


/// define
`totalSupply`


///

```js
read-only totalSupply: int32;
```


## 方法

/// define
`getBreatheBlocks`


///

```js
getBreatheBlocks(): BlockPermutation[]
```

/// html | div.result

///


/// define
`getNonBreatheBlocks`


///

```js
getNonBreatheBlocks(): BlockPermutation[]
```

/// html | div.result

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

