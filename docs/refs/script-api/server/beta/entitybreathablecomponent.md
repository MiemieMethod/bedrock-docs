# `EntityBreathableComponent`

> 文档版本：1.21.60.21

`EntityBreathableComponent`类，扩展自[`EntityComponent`](./entitycomponent.md)。script_api.@minecraft/server.entitybreathablecomponent.description

## 常量

/// define
`componentId`


///

```js
static read-only componentId = "minecraft:breathable";
```


## 属性

/// define
`airSupply`


///

```js
airSupply: int16;
```

/// html | div.result
//// define
`airSupply`：`int16`

- script_api.@minecraft/server.entitybreathablecomponent.airsupply.description


////

///


/// define
`breathesAir`


///

```js
read-only breathesAir: boolean;
```

/// html | div.result
//// define
`breathesAir`：`boolean`

- script_api.@minecraft/server.entitybreathablecomponent.breathesair.description


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

- script_api.@minecraft/server.entitybreathablecomponent.breatheslava.description


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

- script_api.@minecraft/server.entitybreathablecomponent.breathessolids.description


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

- script_api.@minecraft/server.entitybreathablecomponent.breatheswater.description


////

///


/// define
`canBreathe`


///

```js
read-only canBreathe: boolean;
```

/// html | div.result
//// define
`canBreathe`：`boolean`

- script_api.@minecraft/server.entitybreathablecomponent.canbreathe.description


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

- script_api.@minecraft/server.entitybreathablecomponent.generatesbubbles.description


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

- script_api.@minecraft/server.entitybreathablecomponent.inhaletime.description


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

- script_api.@minecraft/server.entitybreathablecomponent.suffocatetime.description


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

- script_api.@minecraft/server.entitybreathablecomponent.totalsupply.description


////

///


## 方法

/// define
`getBreatheBlocks`


///

script_api.@minecraft/server.entitybreathablecomponent.getbreatheblocks.description

```js
getBreatheBlocks(): BlockPermutation[]
```

/// html | div.result
//// define
返回值：<code><a href="../blockpermutation/">BlockPermutation</a>[]</code>

- script_api.@minecraft/server.entitybreathablecomponent.getbreatheblocks.return


////

///


/// define
`getNonBreatheBlocks`


///

script_api.@minecraft/server.entitybreathablecomponent.getnonbreatheblocks.description

```js
getNonBreatheBlocks(): BlockPermutation[]
```

/// html | div.result
//// define
返回值：<code><a href="../blockpermutation/">BlockPermutation</a>[]</code>

- script_api.@minecraft/server.entitybreathablecomponent.getnonbreatheblocks.return


////

///

