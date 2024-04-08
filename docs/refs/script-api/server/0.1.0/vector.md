# `Vector`

> 文档版本：1.21.0.20

`Vector`类。

## 常量

/// define
`back`


///

```js
static read-only back: Vector;
```

/// html | div.result
//// define
`back`：[`Vector`](./vector.md)

- 常量。


////

///


/// define
`down`


///

```js
static read-only down: Vector;
```

/// html | div.result
//// define
`down`：[`Vector`](./vector.md)

- 常量。


////

///


/// define
`forward`


///

```js
static read-only forward: Vector;
```

/// html | div.result
//// define
`forward`：[`Vector`](./vector.md)

- 常量。


////

///


/// define
`left`


///

```js
static read-only left: Vector;
```

/// html | div.result
//// define
`left`：[`Vector`](./vector.md)

- 常量。


////

///


/// define
`one`


///

```js
static read-only one: Vector;
```

/// html | div.result
//// define
`one`：[`Vector`](./vector.md)

- 常量。


////

///


/// define
`right`


///

```js
static read-only right: Vector;
```

/// html | div.result
//// define
`right`：[`Vector`](./vector.md)

- 常量。


////

///


/// define
`up`


///

```js
static read-only up: Vector;
```

/// html | div.result
//// define
`up`：[`Vector`](./vector.md)

- 常量。


////

///


/// define
`zero`


///

```js
static read-only zero: Vector;
```

/// html | div.result
//// define
`zero`：[`Vector`](./vector.md)

- 常量。


////

///


## 属性

/// define
`x`


///

```js
x: float;
```

/// html | div.result
//// define
`x`：`float`

- 属性。


////

///


/// define
`y`


///

```js
y: float;
```

/// html | div.result
//// define
`y`：`float`

- 属性。


////

///


/// define
`z`


///

```js
z: float;
```

/// html | div.result
//// define
`z`：`float`

- 属性。


////

///


## 方法

/// define
`add`


///

```js
static add(a: Vector, b: Vector): Vector
```

/// html | div.result
//// define
`a`：[`Vector`](./vector.md)

- 参数1。


////

//// define
`b`：[`Vector`](./vector.md)

- 参数2。


////

//// define
返回值：[`Vector`](./vector.md)

- 返回值。


////

///


/// define
`constructor`


///

```js
new constructor(x: float, y: float, z: float): Vector
```

/// html | div.result
//// define
`x`：`float`

- 参数1。


////

//// define
`y`：`float`

- 参数2。


////

//// define
`z`：`float`

- 参数3。


////

//// define
返回值：[`Vector`](./vector.md)

- 返回值。


////

///


/// define
`cross`


///

```js
static cross(a: Vector, b: Vector): Vector
```

/// html | div.result
//// define
`a`：[`Vector`](./vector.md)

- 参数1。


////

//// define
`b`：[`Vector`](./vector.md)

- 参数2。


////

//// define
返回值：[`Vector`](./vector.md)

- 返回值。


////

///


/// define
`distance`


///

```js
static distance(a: Vector, b: Vector): float
```

/// html | div.result
//// define
`a`：[`Vector`](./vector.md)

- 参数1。


////

//// define
`b`：[`Vector`](./vector.md)

- 参数2。


////

//// define
返回值：`float`

- 返回值。


////

///


/// define
`divide`


///

```js
static divide(a: Vector, b: float | Vector): Vector
```

/// html | div.result
//// define
`a`：[`Vector`](./vector.md)

- 参数1。


////

//// define
`b`：`float`|[`Vector`](./vector.md)

- 参数2。


////

//// define
返回值：[`Vector`](./vector.md)

- 返回值。


////

///


/// define
`equals`


///

```js
equals(other: Vector): boolean
```

/// html | div.result
//// define
`other`：[`Vector`](./vector.md)

- 参数1。


////

//// define
返回值：`boolean`

- 返回值。


////

///


/// define
`length`


///

```js
length(): float
```

/// html | div.result
//// define
返回值：`float`

- 返回值。


////

///


/// define
`lerp`


///

```js
static lerp(a: Vector, b: Vector, t: float): Vector
```

/// html | div.result
//// define
`a`：[`Vector`](./vector.md)

- 参数1。


////

//// define
`b`：[`Vector`](./vector.md)

- 参数2。


////

//// define
`t`：`float`

- 参数3。


////

//// define
返回值：[`Vector`](./vector.md)

- 返回值。


////

///


/// define
`max`


///

```js
static max(a: Vector, b: Vector): Vector
```

/// html | div.result
//// define
`a`：[`Vector`](./vector.md)

- 参数1。


////

//// define
`b`：[`Vector`](./vector.md)

- 参数2。


////

//// define
返回值：[`Vector`](./vector.md)

- 返回值。


////

///


/// define
`min`


///

```js
static min(a: Vector, b: Vector): Vector
```

/// html | div.result
//// define
`a`：[`Vector`](./vector.md)

- 参数1。


////

//// define
`b`：[`Vector`](./vector.md)

- 参数2。


////

//// define
返回值：[`Vector`](./vector.md)

- 返回值。


////

///


/// define
`multiply`


///

```js
static multiply(a: Vector, b: float | Vector): Vector
```

/// html | div.result
//// define
`a`：[`Vector`](./vector.md)

- 参数1。


////

//// define
`b`：`float`|[`Vector`](./vector.md)

- 参数2。


////

//// define
返回值：[`Vector`](./vector.md)

- 返回值。


////

///


/// define
`normalized`


///

```js
normalized(): Vector
```

/// html | div.result
//// define
返回值：[`Vector`](./vector.md)

- 返回值。


////

///


/// define
`slerp`


///

```js
static slerp(a: Vector, b: Vector, t: float): Vector
```

/// html | div.result
//// define
`a`：[`Vector`](./vector.md)

- 参数1。


////

//// define
`b`：[`Vector`](./vector.md)

- 参数2。


////

//// define
`t`：`float`

- 参数3。


////

//// define
返回值：[`Vector`](./vector.md)

- 返回值。


////

///


/// define
`subtract`


///

```js
static subtract(a: Vector, b: Vector): Vector
```

/// html | div.result
//// define
`a`：[`Vector`](./vector.md)

- 参数1。


////

//// define
`b`：[`Vector`](./vector.md)

- 参数2。


////

//// define
返回值：[`Vector`](./vector.md)

- 返回值。


////

///

