# `EntityProjectileComponent`

> 文档版本：1.21.0.20

`EntityProjectileComponent`类，扩展自`EntityComponent`。

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


/// define
`catchFireOnHurt`


///

```js
catchFireOnHurt: boolean;
```


/// define
`critParticlesOnProjectileHurt`


///

```js
critParticlesOnProjectileHurt: boolean;
```


/// define
`destroyOnProjectileHurt`


///

```js
destroyOnProjectileHurt: boolean;
```


/// define
`gravity`


///

```js
gravity: float;
```


/// define
`hitEntitySound`


///

```js
hitEntitySound: string | undefined;
```


/// define
`hitGroundSound`


///

```js
hitGroundSound: string | undefined;
```


/// define
`hitParticle`


///

```js
hitParticle: string | undefined;
```


/// define
`lightningStrikeOnHit`


///

```js
lightningStrikeOnHit: boolean;
```


/// define
`liquidInertia`


///

```js
liquidInertia: float;
```


/// define
`onFireTime`


///

```js
onFireTime: float;
```


/// define
`owner`


///

```js
owner: Entity | undefined;
```


/// define
`shouldBounceOnHit`


///

```js
shouldBounceOnHit: boolean;
```


/// define
`stopOnHit`


///

```js
stopOnHit: boolean;
```


## 方法

/// define
`shoot`


///

```js
shoot(velocity: Vector3, options?: ProjectileShootOptions): void
```

