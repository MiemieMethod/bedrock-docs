# `EntityProjectileComponent`

> 文档版本：1.21.0.20

`EntityProjectileComponent`类，扩展自[`EntityComponent`](./entitycomponent.md)。script_api.@minecraft/server.entityprojectilecomponent.description

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

- script_api.@minecraft/server.entityprojectilecomponent.airinertia.description


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

- script_api.@minecraft/server.entityprojectilecomponent.catchfireonhurt.description


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

- script_api.@minecraft/server.entityprojectilecomponent.critparticlesonprojectilehurt.description


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

- script_api.@minecraft/server.entityprojectilecomponent.destroyonprojectilehurt.description


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

- script_api.@minecraft/server.entityprojectilecomponent.gravity.description


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

- script_api.@minecraft/server.entityprojectilecomponent.hitentitysound.description


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

- script_api.@minecraft/server.entityprojectilecomponent.hitgroundsound.description


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

- script_api.@minecraft/server.entityprojectilecomponent.hitparticle.description


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

- script_api.@minecraft/server.entityprojectilecomponent.lightningstrikeonhit.description


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

- script_api.@minecraft/server.entityprojectilecomponent.liquidinertia.description


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

- script_api.@minecraft/server.entityprojectilecomponent.onfiretime.description


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

- script_api.@minecraft/server.entityprojectilecomponent.owner.description


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

- script_api.@minecraft/server.entityprojectilecomponent.shouldbounceonhit.description


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

- script_api.@minecraft/server.entityprojectilecomponent.stoponhit.description


////

///


## 方法

/// define
`shoot`


///

script_api.@minecraft/server.entityprojectilecomponent.shoot.description

```js
shoot(velocity: Vector3, options?: ProjectileShootOptions): void
```

/// html | div.result
//// define
`velocity`：[`Vector3`](./vector3.md)

- script_api.@minecraft/server.entityprojectilecomponent.shoot.velocity.description


////

//// define
`options`：[`ProjectileShootOptions`](./projectileshootoptions.md)|`undefined`

- script_api.@minecraft/server.entityprojectilecomponent.shoot.options.description


////

//// define
返回值：`void`

- script_api.@minecraft/server.entityprojectilecomponent.shoot.return


////

///

