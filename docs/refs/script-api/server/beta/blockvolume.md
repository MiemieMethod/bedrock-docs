# `BlockVolume`

> 文档版本：1.21.0.20

`BlockVolume`类，扩展自`[`BlockVolumeBase`](./blockvolumebase.md)`。

## 属性

/// define
`from`


///

```js
from: Vector3;
```

/// html | div.result
//// define
`from`：[`Vector3`](./vector3.md)

- 属性。


////

///


/// define
`to`


///

```js
to: Vector3;
```

/// html | div.result
//// define
`to`：[`Vector3`](./vector3.md)

- 属性。


////

///


## 方法

/// define
`constructor`


///

```js
new constructor(from: Vector3, to: Vector3): BlockVolume
```

/// html | div.result
//// define
`from`：[`Vector3`](./vector3.md)

- 参数1。


////

//// define
`to`：[`Vector3`](./vector3.md)

- 参数2。


////

//// define
返回值：[`BlockVolume`](./blockvolume.md)

- 返回值。


////

///


/// define
`doesLocationTouchFaces`


///

```js
doesLocationTouchFaces(pos: Vector3): boolean
```

/// html | div.result
//// define
`pos`：[`Vector3`](./vector3.md)

- 参数1。


////

//// define
返回值：`boolean`

- 返回值。


////

///


/// define
`doesVolumeTouchFaces`


///

```js
doesVolumeTouchFaces(other: BlockVolume): boolean
```

/// html | div.result
//// define
`other`：[`BlockVolume`](./blockvolume.md)

- 参数1。


////

//// define
返回值：`boolean`

- 返回值。


////

///


/// define
`intersects`


///

```js
intersects(other: BlockVolume): BlockVolumeIntersection
```

/// html | div.result
//// define
`other`：[`BlockVolume`](./blockvolume.md)

- 参数1。


////

//// define
返回值：[`BlockVolumeIntersection`](./blockvolumeintersection.md)

- 返回值。


////

///

