# `ProjectileHitBlockAfterEvent`

> 文档版本：1.21.60.21

`ProjectileHitBlockAfterEvent`类。script_api.@minecraft/server.projectilehitblockafterevent.description

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

- script_api.@minecraft/server.projectilehitblockafterevent.dimension.description


////

///


/// define
`hitVector`


///

```js
read-only hitVector: Vector3;
```

/// html | div.result
//// define
`hitVector`：[`Vector3`](./vector3.md)

- script_api.@minecraft/server.projectilehitblockafterevent.hitvector.description


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

- script_api.@minecraft/server.projectilehitblockafterevent.location.description


////

///


/// define
`projectile`


///

```js
read-only projectile: Entity;
```

/// html | div.result
//// define
`projectile`：[`Entity`](./entity.md)

- script_api.@minecraft/server.projectilehitblockafterevent.projectile.description


////

///


/// define
`source`


///

```js
read-only source: Entity | undefined;
```

/// html | div.result
//// define
`source`：[`Entity`](./entity.md)|`undefined`

- script_api.@minecraft/server.projectilehitblockafterevent.source.description


////

///


## 方法

/// define
`getBlockHit`


///

script_api.@minecraft/server.projectilehitblockafterevent.getblockhit.description

```js
getBlockHit(): BlockHitInformation
```

/// html | div.result
//// define
返回值：[`BlockHitInformation`](./blockhitinformation.md)

- script_api.@minecraft/server.projectilehitblockafterevent.getblockhit.return


////

///

