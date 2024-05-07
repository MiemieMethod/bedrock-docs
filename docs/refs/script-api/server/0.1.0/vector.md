# `Vector`

> 文档版本：1.21.0.24

`Vector`类。script_api.mojang-minecraft.vector.description

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

- script_api.mojang-minecraft.vector.back.description


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

- script_api.mojang-minecraft.vector.down.description


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

- script_api.mojang-minecraft.vector.forward.description


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

- script_api.mojang-minecraft.vector.left.description


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

- script_api.mojang-minecraft.vector.one.description


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

- script_api.mojang-minecraft.vector.right.description


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

- script_api.mojang-minecraft.vector.up.description


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

- script_api.mojang-minecraft.vector.zero.description


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

- script_api.mojang-minecraft.vector.x.description


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

- script_api.mojang-minecraft.vector.y.description


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

- script_api.mojang-minecraft.vector.z.description


////

///


## 方法

/// define
`add`


///

script_api.mojang-minecraft.vector.add.description

```js
static add(a: Vector, b: Vector): Vector
```

/// html | div.result
//// define
`a`：[`Vector`](./vector.md)

- script_api.mojang-minecraft.vector.add.a.description


////

//// define
`b`：[`Vector`](./vector.md)

- script_api.mojang-minecraft.vector.add.b.description


////

//// define
返回值：[`Vector`](./vector.md)

- script_api.mojang-minecraft.vector.add.return


////

///


/// define
`constructor`


///

script_api.mojang-minecraft.vector.constructor.description

```js
new constructor(x: float, y: float, z: float): Vector
```

/// html | div.result
//// define
`x`：`float`

- script_api.mojang-minecraft.vector.constructor.x.description


////

//// define
`y`：`float`

- script_api.mojang-minecraft.vector.constructor.y.description


////

//// define
`z`：`float`

- script_api.mojang-minecraft.vector.constructor.z.description


////

//// define
返回值：[`Vector`](./vector.md)

- script_api.mojang-minecraft.vector.constructor.return


////

///


/// define
`cross`


///

script_api.mojang-minecraft.vector.cross.description

```js
static cross(a: Vector, b: Vector): Vector
```

/// html | div.result
//// define
`a`：[`Vector`](./vector.md)

- script_api.mojang-minecraft.vector.cross.a.description


////

//// define
`b`：[`Vector`](./vector.md)

- script_api.mojang-minecraft.vector.cross.b.description


////

//// define
返回值：[`Vector`](./vector.md)

- script_api.mojang-minecraft.vector.cross.return


////

///


/// define
`distance`


///

script_api.mojang-minecraft.vector.distance.description

```js
static distance(a: Vector, b: Vector): float
```

/// html | div.result
//// define
`a`：[`Vector`](./vector.md)

- script_api.mojang-minecraft.vector.distance.a.description


////

//// define
`b`：[`Vector`](./vector.md)

- script_api.mojang-minecraft.vector.distance.b.description


////

//// define
返回值：`float`

- script_api.mojang-minecraft.vector.distance.return


////

///


/// define
`divide`


///

script_api.mojang-minecraft.vector.divide.description

```js
static divide(a: Vector, b: float | Vector): Vector
```

/// html | div.result
//// define
`a`：[`Vector`](./vector.md)

- script_api.mojang-minecraft.vector.divide.a.description


////

//// define
`b`：`float`|[`Vector`](./vector.md)

- script_api.mojang-minecraft.vector.divide.b.description


////

//// define
返回值：[`Vector`](./vector.md)

- script_api.mojang-minecraft.vector.divide.return


////

///


/// define
`equals`


///

script_api.mojang-minecraft.vector.equals.description

```js
equals(other: Vector): boolean
```

/// html | div.result
//// define
`other`：[`Vector`](./vector.md)

- script_api.mojang-minecraft.vector.equals.other.description


////

//// define
返回值：`boolean`

- script_api.mojang-minecraft.vector.equals.return


////

///


/// define
`length`


///

script_api.mojang-minecraft.vector.length.description

```js
length(): float
```

/// html | div.result
//// define
返回值：`float`

- script_api.mojang-minecraft.vector.length.return


////

///


/// define
`lerp`


///

script_api.mojang-minecraft.vector.lerp.description

```js
static lerp(a: Vector, b: Vector, t: float): Vector
```

/// html | div.result
//// define
`a`：[`Vector`](./vector.md)

- script_api.mojang-minecraft.vector.lerp.a.description


////

//// define
`b`：[`Vector`](./vector.md)

- script_api.mojang-minecraft.vector.lerp.b.description


////

//// define
`t`：`float`

- script_api.mojang-minecraft.vector.lerp.t.description


////

//// define
返回值：[`Vector`](./vector.md)

- script_api.mojang-minecraft.vector.lerp.return


////

///


/// define
`max`


///

script_api.mojang-minecraft.vector.max.description

```js
static max(a: Vector, b: Vector): Vector
```

/// html | div.result
//// define
`a`：[`Vector`](./vector.md)

- script_api.mojang-minecraft.vector.max.a.description


////

//// define
`b`：[`Vector`](./vector.md)

- script_api.mojang-minecraft.vector.max.b.description


////

//// define
返回值：[`Vector`](./vector.md)

- script_api.mojang-minecraft.vector.max.return


////

///


/// define
`min`


///

script_api.mojang-minecraft.vector.min.description

```js
static min(a: Vector, b: Vector): Vector
```

/// html | div.result
//// define
`a`：[`Vector`](./vector.md)

- script_api.mojang-minecraft.vector.min.a.description


////

//// define
`b`：[`Vector`](./vector.md)

- script_api.mojang-minecraft.vector.min.b.description


////

//// define
返回值：[`Vector`](./vector.md)

- script_api.mojang-minecraft.vector.min.return


////

///


/// define
`multiply`


///

script_api.mojang-minecraft.vector.multiply.description

```js
static multiply(a: Vector, b: float | Vector): Vector
```

/// html | div.result
//// define
`a`：[`Vector`](./vector.md)

- script_api.mojang-minecraft.vector.multiply.a.description


////

//// define
`b`：`float`|[`Vector`](./vector.md)

- script_api.mojang-minecraft.vector.multiply.b.description


////

//// define
返回值：[`Vector`](./vector.md)

- script_api.mojang-minecraft.vector.multiply.return


////

///


/// define
`normalized`


///

script_api.mojang-minecraft.vector.normalized.description

```js
normalized(): Vector
```

/// html | div.result
//// define
返回值：[`Vector`](./vector.md)

- script_api.mojang-minecraft.vector.normalized.return


////

///


/// define
`slerp`


///

script_api.mojang-minecraft.vector.slerp.description

```js
static slerp(a: Vector, b: Vector, t: float): Vector
```

/// html | div.result
//// define
`a`：[`Vector`](./vector.md)

- script_api.mojang-minecraft.vector.slerp.a.description


////

//// define
`b`：[`Vector`](./vector.md)

- script_api.mojang-minecraft.vector.slerp.b.description


////

//// define
`t`：`float`

- script_api.mojang-minecraft.vector.slerp.t.description


////

//// define
返回值：[`Vector`](./vector.md)

- script_api.mojang-minecraft.vector.slerp.return


////

///


/// define
`subtract`


///

script_api.mojang-minecraft.vector.subtract.description

```js
static subtract(a: Vector, b: Vector): Vector
```

/// html | div.result
//// define
`a`：[`Vector`](./vector.md)

- script_api.mojang-minecraft.vector.subtract.a.description


////

//// define
`b`：[`Vector`](./vector.md)

- script_api.mojang-minecraft.vector.subtract.b.description


////

//// define
返回值：[`Vector`](./vector.md)

- script_api.mojang-minecraft.vector.subtract.return


////

///

