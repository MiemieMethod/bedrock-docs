# `BoundingBoxUtils`

> 文档版本：1.21.0.21

`BoundingBoxUtils`类。script_api.@minecraft/server.boundingboxutils.description

## 方法

/// define
`createValid`


///

script_api.@minecraft/server.boundingboxutils.createvalid.description

```js
static createValid(min: Vector3, max: Vector3): BoundingBox
```

/// html | div.result
//// define
`min`：[`Vector3`](./vector3.md)

- script_api.@minecraft/server.boundingboxutils.createvalid.min.description


////

//// define
`max`：[`Vector3`](./vector3.md)

- script_api.@minecraft/server.boundingboxutils.createvalid.max.description


////

//// define
返回值：[`BoundingBox`](./boundingbox.md)

- script_api.@minecraft/server.boundingboxutils.createvalid.return


////

///


/// define
`dilate`


///

script_api.@minecraft/server.boundingboxutils.dilate.description

```js
static dilate(box: BoundingBox, size: Vector3): BoundingBox
```

/// html | div.result
//// define
`box`：[`BoundingBox`](./boundingbox.md)

- script_api.@minecraft/server.boundingboxutils.dilate.box.description


////

//// define
`size`：[`Vector3`](./vector3.md)

- script_api.@minecraft/server.boundingboxutils.dilate.size.description


////

//// define
返回值：[`BoundingBox`](./boundingbox.md)

- script_api.@minecraft/server.boundingboxutils.dilate.return


////

///


/// define
`equals`


///

script_api.@minecraft/server.boundingboxutils.equals.description

```js
static equals(box: BoundingBox, other: BoundingBox): boolean
```

/// html | div.result
//// define
`box`：[`BoundingBox`](./boundingbox.md)

- script_api.@minecraft/server.boundingboxutils.equals.box.description


////

//// define
`other`：[`BoundingBox`](./boundingbox.md)

- script_api.@minecraft/server.boundingboxutils.equals.other.description


////

//// define
返回值：`boolean`

- script_api.@minecraft/server.boundingboxutils.equals.return


////

///


/// define
`expand`


///

script_api.@minecraft/server.boundingboxutils.expand.description

```js
static expand(box: BoundingBox, other: BoundingBox): BoundingBox
```

/// html | div.result
//// define
`box`：[`BoundingBox`](./boundingbox.md)

- script_api.@minecraft/server.boundingboxutils.expand.box.description


////

//// define
`other`：[`BoundingBox`](./boundingbox.md)

- script_api.@minecraft/server.boundingboxutils.expand.other.description


////

//// define
返回值：[`BoundingBox`](./boundingbox.md)

- script_api.@minecraft/server.boundingboxutils.expand.return


////

///


/// define
`getCenter`


///

script_api.@minecraft/server.boundingboxutils.getcenter.description

```js
static getCenter(box: BoundingBox): Vector3
```

/// html | div.result
//// define
`box`：[`BoundingBox`](./boundingbox.md)

- script_api.@minecraft/server.boundingboxutils.getcenter.box.description


////

//// define
返回值：[`Vector3`](./vector3.md)

- script_api.@minecraft/server.boundingboxutils.getcenter.return


////

///


/// define
`getIntersection`


///

script_api.@minecraft/server.boundingboxutils.getintersection.description

```js
static getIntersection(box: BoundingBox, other: BoundingBox): BoundingBox | undefined
```

/// html | div.result
//// define
`box`：[`BoundingBox`](./boundingbox.md)

- script_api.@minecraft/server.boundingboxutils.getintersection.box.description


////

//// define
`other`：[`BoundingBox`](./boundingbox.md)

- script_api.@minecraft/server.boundingboxutils.getintersection.other.description


////

//// define
返回值：[`BoundingBox`](./boundingbox.md)|`undefined`

- script_api.@minecraft/server.boundingboxutils.getintersection.return


////

///


/// define
`getSpan`


///

script_api.@minecraft/server.boundingboxutils.getspan.description

```js
static getSpan(box: BoundingBox): Vector3
```

/// html | div.result
//// define
`box`：[`BoundingBox`](./boundingbox.md)

- script_api.@minecraft/server.boundingboxutils.getspan.box.description


////

//// define
返回值：[`Vector3`](./vector3.md)

- script_api.@minecraft/server.boundingboxutils.getspan.return


////

///


/// define
`intersects`


///

script_api.@minecraft/server.boundingboxutils.intersects.description

```js
static intersects(box: BoundingBox, other: BoundingBox): boolean
```

/// html | div.result
//// define
`box`：[`BoundingBox`](./boundingbox.md)

- script_api.@minecraft/server.boundingboxutils.intersects.box.description


////

//// define
`other`：[`BoundingBox`](./boundingbox.md)

- script_api.@minecraft/server.boundingboxutils.intersects.other.description


////

//// define
返回值：`boolean`

- script_api.@minecraft/server.boundingboxutils.intersects.return


////

///


/// define
`isInside`


///

script_api.@minecraft/server.boundingboxutils.isinside.description

```js
static isInside(box: BoundingBox, pos: Vector3): boolean
```

/// html | div.result
//// define
`box`：[`BoundingBox`](./boundingbox.md)

- script_api.@minecraft/server.boundingboxutils.isinside.box.description


////

//// define
`pos`：[`Vector3`](./vector3.md)

- script_api.@minecraft/server.boundingboxutils.isinside.pos.description


////

//// define
返回值：`boolean`

- script_api.@minecraft/server.boundingboxutils.isinside.return


////

///


/// define
`isValid`


///

script_api.@minecraft/server.boundingboxutils.isvalid.description

```js
static isValid(box: BoundingBox): boolean
```

/// html | div.result
//// define
`box`：[`BoundingBox`](./boundingbox.md)

- script_api.@minecraft/server.boundingboxutils.isvalid.box.description


////

//// define
返回值：`boolean`

- script_api.@minecraft/server.boundingboxutils.isvalid.return


////

///


/// define
`translate`


///

script_api.@minecraft/server.boundingboxutils.translate.description

```js
static translate(box: BoundingBox, delta: Vector3): BoundingBox
```

/// html | div.result
//// define
`box`：[`BoundingBox`](./boundingbox.md)

- script_api.@minecraft/server.boundingboxutils.translate.box.description


////

//// define
`delta`：[`Vector3`](./vector3.md)

- script_api.@minecraft/server.boundingboxutils.translate.delta.description


////

//// define
返回值：[`BoundingBox`](./boundingbox.md)

- script_api.@minecraft/server.boundingboxutils.translate.return


////

///

