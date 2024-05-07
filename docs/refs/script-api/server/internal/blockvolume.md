# `BlockVolume`

> 文档版本：1.21.0.24

`BlockVolume`类，扩展自[`BlockVolumeBase`](./blockvolumebase.md)。script_api.@minecraft/server.blockvolume.description

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

- script_api.@minecraft/server.blockvolume.from.description


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

- script_api.@minecraft/server.blockvolume.to.description


////

///


## 方法

/// define
`constructor`


///

script_api.@minecraft/server.blockvolume.constructor.description

```js
new constructor(from: Vector3, to: Vector3): BlockVolume
```

/// html | div.result
//// define
`from`：[`Vector3`](./vector3.md)

- script_api.@minecraft/server.blockvolume.constructor.from.description


////

//// define
`to`：[`Vector3`](./vector3.md)

- script_api.@minecraft/server.blockvolume.constructor.to.description


////

//// define
返回值：[`BlockVolume`](./blockvolume.md)

- script_api.@minecraft/server.blockvolume.constructor.return


////

///


/// define
`doesLocationTouchFaces`


///

script_api.@minecraft/server.blockvolume.doeslocationtouchfaces.description

```js
doesLocationTouchFaces(pos: Vector3): boolean
```

/// html | div.result
//// define
`pos`：[`Vector3`](./vector3.md)

- script_api.@minecraft/server.blockvolume.doeslocationtouchfaces.pos.description


////

//// define
返回值：`boolean`

- script_api.@minecraft/server.blockvolume.doeslocationtouchfaces.return


////

///


/// define
`doesVolumeTouchFaces`


///

script_api.@minecraft/server.blockvolume.doesvolumetouchfaces.description

```js
doesVolumeTouchFaces(other: BlockVolume): boolean
```

/// html | div.result
//// define
`other`：[`BlockVolume`](./blockvolume.md)

- script_api.@minecraft/server.blockvolume.doesvolumetouchfaces.other.description


////

//// define
返回值：`boolean`

- script_api.@minecraft/server.blockvolume.doesvolumetouchfaces.return


////

///


/// define
`intersects`


///

script_api.@minecraft/server.blockvolume.intersects.description

```js
intersects(other: BlockVolume): BlockVolumeIntersection
```

/// html | div.result
//// define
`other`：[`BlockVolume`](./blockvolume.md)

- script_api.@minecraft/server.blockvolume.intersects.other.description


////

//// define
返回值：[`BlockVolumeIntersection`](./blockvolumeintersection.md)

- script_api.@minecraft/server.blockvolume.intersects.return


////

///

