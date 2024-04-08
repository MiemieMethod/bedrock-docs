# `BoundingBoxUtils`

> 文档版本：1.21.0.20

`BoundingBoxUtils`类。

## 方法

/// define
`createValid`


///

```js
static createValid(min: Vector3, max: Vector3): BoundingBox
```

/// html | div.result
//// define
`min`：[`Vector3`](./vector3.md)

- 参数1。


////

//// define
`max`：[`Vector3`](./vector3.md)

- 参数2。


////

//// define
返回值：[`BoundingBox`](./boundingbox.md)

- 返回值。


////

///


/// define
`dilate`


///

```js
static dilate(box: BoundingBox, size: Vector3): BoundingBox
```

/// html | div.result
//// define
`box`：[`BoundingBox`](./boundingbox.md)

- 参数1。


////

//// define
`size`：[`Vector3`](./vector3.md)

- 参数2。


////

//// define
返回值：[`BoundingBox`](./boundingbox.md)

- 返回值。


////

///


/// define
`equals`


///

```js
static equals(box: BoundingBox, other: BoundingBox): boolean
```

/// html | div.result
//// define
`box`：[`BoundingBox`](./boundingbox.md)

- 参数1。


////

//// define
`other`：[`BoundingBox`](./boundingbox.md)

- 参数2。


////

//// define
返回值：`boolean`

- 返回值。


////

///


/// define
`expand`


///

```js
static expand(box: BoundingBox, other: BoundingBox): BoundingBox
```

/// html | div.result
//// define
`box`：[`BoundingBox`](./boundingbox.md)

- 参数1。


////

//// define
`other`：[`BoundingBox`](./boundingbox.md)

- 参数2。


////

//// define
返回值：[`BoundingBox`](./boundingbox.md)

- 返回值。


////

///


/// define
`getCenter`


///

```js
static getCenter(box: BoundingBox): Vector3
```

/// html | div.result
//// define
`box`：[`BoundingBox`](./boundingbox.md)

- 参数1。


////

//// define
返回值：[`Vector3`](./vector3.md)

- 返回值。


////

///


/// define
`getIntersection`


///

```js
static getIntersection(box: BoundingBox, other: BoundingBox): BoundingBox | undefined
```

/// html | div.result
//// define
`box`：[`BoundingBox`](./boundingbox.md)

- 参数1。


////

//// define
`other`：[`BoundingBox`](./boundingbox.md)

- 参数2。


////

//// define
返回值：[`BoundingBox`](./boundingbox.md)|`undefined`

- 返回值。


////

///


/// define
`getSpan`


///

```js
static getSpan(box: BoundingBox): Vector3
```

/// html | div.result
//// define
`box`：[`BoundingBox`](./boundingbox.md)

- 参数1。


////

//// define
返回值：[`Vector3`](./vector3.md)

- 返回值。


////

///


/// define
`intersects`


///

```js
static intersects(box: BoundingBox, other: BoundingBox): boolean
```

/// html | div.result
//// define
`box`：[`BoundingBox`](./boundingbox.md)

- 参数1。


////

//// define
`other`：[`BoundingBox`](./boundingbox.md)

- 参数2。


////

//// define
返回值：`boolean`

- 返回值。


////

///


/// define
`isInside`


///

```js
static isInside(box: BoundingBox, pos: Vector3): boolean
```

/// html | div.result
//// define
`box`：[`BoundingBox`](./boundingbox.md)

- 参数1。


////

//// define
`pos`：[`Vector3`](./vector3.md)

- 参数2。


////

//// define
返回值：`boolean`

- 返回值。


////

///


/// define
`isValid`


///

```js
static isValid(box: BoundingBox): boolean
```

/// html | div.result
//// define
`box`：[`BoundingBox`](./boundingbox.md)

- 参数1。


////

//// define
返回值：`boolean`

- 返回值。


////

///


/// define
`translate`


///

```js
static translate(box: BoundingBox, delta: Vector3): BoundingBox
```

/// html | div.result
//// define
`box`：[`BoundingBox`](./boundingbox.md)

- 参数1。


////

//// define
`delta`：[`Vector3`](./vector3.md)

- 参数2。


////

//// define
返回值：[`BoundingBox`](./boundingbox.md)

- 返回值。


////

///

