# `Cursor`

> 文档版本：1.21.0.20

`Cursor`类。

## 属性

/// define
`faceDirection`


///

```js
read-only faceDirection: uint8;
```

/// html | div.result
//// define
`faceDirection`：`uint8`

- 属性。


////

///


/// define
`isVisible`


///

```js
read-only isVisible: boolean;
```

/// html | div.result
//// define
`isVisible`：`boolean`

- 属性。


////

///


## 方法

/// define
`getPosition`


///

```js
getPosition(): Vector3
```

/// html | div.result
//// define
返回值：[`Vector3`](../../server/beta/vector3.md)

- 返回值。


////

///


/// define
`getProperties`


///

```js
getProperties(): CursorProperties
```

/// html | div.result
//// define
返回值：[`CursorProperties`](./cursorproperties.md)

- 返回值。


////

///


/// define
`hide`


///

```js
hide(): void
```

/// html | div.result
//// define
返回值：`void`

- 返回值。


////

///


/// define
`moveBy`


///

```js
moveBy(offset: Vector3): Vector3
```

/// html | div.result
//// define
`offset`：[`Vector3`](../../server/beta/vector3.md)

- 参数1。


////

//// define
返回值：[`Vector3`](../../server/beta/vector3.md)

- 返回值。


////

///


/// define
`resetToDefaultState`


///

```js
resetToDefaultState(): void
```

/// html | div.result
//// define
返回值：`void`

- 返回值。


////

///


/// define
`setProperties`


///

```js
setProperties(properties: CursorProperties): void
```

/// html | div.result
//// define
`properties`：[`CursorProperties`](./cursorproperties.md)

- 参数1。


////

//// define
返回值：`void`

- 返回值。


////

///


/// define
`show`


///

```js
show(): void
```

/// html | div.result
//// define
返回值：`void`

- 返回值。


////

///

