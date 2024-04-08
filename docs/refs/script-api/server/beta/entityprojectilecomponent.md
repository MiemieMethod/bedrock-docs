# `EntityProjectileComponent`

> 文档版本：1.21.0.20

`EntityProjectileComponent`类，扩展自[`EntityComponent`](./entitycomponent.md)。

## 常量

/// define
`componentId`


///

```js
static read-only componentId = "minecraft:projectile";
```


## 属性

/// define
`airInertia`


///

```js
airInertia: float;
```

/// html | div.result
//// define
`airInertia`：`float`

- 属性。


////

///


/// define
`catchFireOnHurt`


///

```js
catchFireOnHurt: boolean;
```

/// html | div.result
//// define
`catchFireOnHurt`：`boolean`

- 属性。


////

///


/// define
`critParticlesOnProjectileHurt`


///

```js
critParticlesOnProjectileHurt: boolean;
```

/// html | div.result
//// define
`critParticlesOnProjectileHurt`：`boolean`

- 属性。


////

///


/// define
`destroyOnProjectileHurt`


///

```js
destroyOnProjectileHurt: boolean;
```

/// html | div.result
//// define
`destroyOnProjectileHurt`：`boolean`

- 属性。


////

///


/// define
`gravity`


///

```js
gravity: float;
```

/// html | div.result
//// define
`gravity`：`float`

- 属性。


////

///


/// define
`hitEntitySound`


///

```js
hitEntitySound: string | undefined;
```

/// html | div.result
//// define
`hitEntitySound`：`string`|`undefined`

- 属性。


////

///


/// define
`hitGroundSound`


///

```js
hitGroundSound: string | undefined;
```

/// html | div.result
//// define
`hitGroundSound`：`string`|`undefined`

- 属性。


////

///


/// define
`hitParticle`


///

```js
hitParticle: string | undefined;
```

/// html | div.result
//// define
`hitParticle`：`string`|`undefined`

- 属性。


////

///


/// define
`lightningStrikeOnHit`


///

```js
lightningStrikeOnHit: boolean;
```

/// html | div.result
//// define
`lightningStrikeOnHit`：`boolean`

- 属性。


////

///


/// define
`liquidInertia`


///

```js
liquidInertia: float;
```

/// html | div.result
//// define
`liquidInertia`：`float`

- 属性。


////

///


/// define
`onFireTime`


///

```js
onFireTime: float;
```

/// html | div.result
//// define
`onFireTime`：`float`

- 属性。


////

///


/// define
`owner`


///

```js
owner: Entity | undefined;
```

/// html | div.result
//// define
`owner`：[`Entity`](./entity.md)|`undefined`

- 属性。


////

///


/// define
`shouldBounceOnHit`


///

```js
shouldBounceOnHit: boolean;
```

/// html | div.result
//// define
`shouldBounceOnHit`：`boolean`

- 属性。


////

///


/// define
`stopOnHit`


///

```js
stopOnHit: boolean;
```

/// html | div.result
//// define
`stopOnHit`：`boolean`

- 属性。


////

///


## 方法

/// define
`shoot`


///

```js
shoot(velocity: Vector3, options?: ProjectileShootOptions): void
```

/// html | div.result
//// define
`velocity`：[`Vector3`](./vector3.md)

- 参数1。


////

//// define
`options`：[`ProjectileShootOptions`](./projectileshootoptions.md)|`undefined`

- 参数2。


////

//// define
返回值：`void`

- 返回值。


////

///

