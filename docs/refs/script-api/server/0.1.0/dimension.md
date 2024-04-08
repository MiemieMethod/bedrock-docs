# `Dimension`

> 文档版本：1.21.0.20

`Dimension`类。

## 属性

/// define
`id`


///

```js
read-only id: string;
```

/// html | div.result
//// define
`id`：`string`

- 属性。


////

///


## 方法

/// define
`createExplosion`


///

```js
createExplosion(location: Location, radius: float, explosionOptions: ExplosionOptions): void
```

/// html | div.result
//// define
`location`：[`Location`](./location.md)

- 参数1。


////

//// define
`radius`：`float`

- 参数2。


////

//// define
`explosionOptions`：[`ExplosionOptions`](./explosionoptions.md)

- 参数3。


////

//// define
返回值：`void`

- 返回值。


////

///


/// define
`getBlock`


///

```js
getBlock(location: BlockLocation): Block
```

/// html | div.result
//// define
`location`：[`BlockLocation`](./blocklocation.md)

- 参数1。


////

//// define
返回值：[`Block`](./block.md)

- 返回值。


////

///


/// define
`getBlockFromRay`


///

```js
getBlockFromRay(location: Location, direction: Vector, options?: BlockRaycastOptions): Block | undefined
```

/// html | div.result
//// define
`location`：[`Location`](./location.md)

- 参数1。


////

//// define
`direction`：[`Vector`](./vector.md)

- 参数2。


////

//// define
`options`：[`BlockRaycastOptions`](./blockraycastoptions.md)|`undefined`

- 参数3。


////

//// define
返回值：[`Block`](./block.md)|`undefined`

- 返回值。


////

///


/// define
`getEntities`


///

```js
getEntities(options?: EntityQueryOptions): EntityIterator
```

/// html | div.result
//// define
`options`：[`EntityQueryOptions`](./entityqueryoptions.md)|`undefined`

- 参数1。


////

//// define
返回值：[`EntityIterator`](./entityiterator.md)

- 返回值。


////

///


/// define
`getEntitiesAtBlockLocation`


///

```js
getEntitiesAtBlockLocation(location: BlockLocation): Entity[]
```

/// html | div.result
//// define
`location`：[`BlockLocation`](./blocklocation.md)

- 参数1。


////

//// define
返回值：<code><a href="../entity/">Entity</a>[]</code>

- 返回值。


////

///


/// define
`getEntitiesFromRay`


///

```js
getEntitiesFromRay(location: Location, direction: Vector, options?: EntityRaycastOptions): Entity[]
```

/// html | div.result
//// define
`location`：[`Location`](./location.md)

- 参数1。


////

//// define
`direction`：[`Vector`](./vector.md)

- 参数2。


////

//// define
`options`：[`EntityRaycastOptions`](./entityraycastoptions.md)|`undefined`

- 参数3。


////

//// define
返回值：<code><a href="../entity/">Entity</a>[]</code>

- 返回值。


////

///


/// define
`getPlayers`


///

```js
getPlayers(options?: EntityQueryOptions): PlayerIterator
```

/// html | div.result
//// define
`options`：[`EntityQueryOptions`](./entityqueryoptions.md)|`undefined`

- 参数1。


////

//// define
返回值：[`PlayerIterator`](./playeriterator.md)

- 返回值。


////

///


/// define
`isEmpty`


///

```js
isEmpty(location: BlockLocation): boolean
```

/// html | div.result
//// define
`location`：[`BlockLocation`](./blocklocation.md)

- 参数1。


////

//// define
返回值：`boolean`

- 返回值。


////

///


/// define
`runCommand`


///

```js
runCommand(commandString: string): any
```

/// html | div.result
//// define
`commandString`：`string`

- 参数1。


////

//// define
返回值：`any`

- 返回值。


////

///


/// define
`spawnEntity`


///

```js
spawnEntity(identifier: string, location: BlockLocation | Location): Entity
```

/// html | div.result
//// define
`identifier`：`string`

- 参数1。


////

//// define
`location`：[`BlockLocation`](./blocklocation.md)|[`Location`](./location.md)

- 参数2。


////

//// define
返回值：[`Entity`](./entity.md)

- 返回值。


////

///


/// define
`spawnItem`


///

```js
spawnItem(item: ItemStack, location: BlockLocation | Location): Entity
```

/// html | div.result
//// define
`item`：[`ItemStack`](./itemstack.md)

- 参数1。


////

//// define
`location`：[`BlockLocation`](./blocklocation.md)|[`Location`](./location.md)

- 参数2。


////

//// define
返回值：[`Entity`](./entity.md)

- 返回值。


////

///


/// define
`spawnParticle`


///

```js
spawnParticle(effectName: string, location: Location, molangVariables: MolangVariableMap): void
```

/// html | div.result
//// define
`effectName`：`string`

- 参数1。


////

//// define
`location`：[`Location`](./location.md)

- 参数2。


////

//// define
`molangVariables`：[`MolangVariableMap`](./molangvariablemap.md)

- 参数3。


////

//// define
返回值：`void`

- 返回值。


////

///

