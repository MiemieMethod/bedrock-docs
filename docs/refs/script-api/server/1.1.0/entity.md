# `Entity`

> 文档版本：1.21.0.20

`Entity`类。

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

- 属性。


////

///


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


/// define
`location`


///

```js
read-only location: Vector3;
```

/// html | div.result
//// define
`location`：[`Vector3`](./vector3.md)

- 属性。


////

///


/// define
`nameTag`


///

```js
nameTag: string;
```

/// html | div.result
//// define
`nameTag`：`string`

- 属性。


////

///


/// define
`typeId`


///

```js
read-only typeId: string;
```

/// html | div.result
//// define
`typeId`：`string`

- 属性。


////

///


## 方法

/// define
`getHeadLocation`


///

```js
getHeadLocation(): Vector3
```

/// html | div.result
//// define
返回值：[`Vector3`](./vector3.md)

- 返回值。


////

///


/// define
`getVelocity`


///

```js
getVelocity(): Vector3
```

/// html | div.result
//// define
返回值：[`Vector3`](./vector3.md)

- 返回值。


////

///


/// define
`getViewDirection`


///

```js
getViewDirection(): Vector3
```

/// html | div.result
//// define
返回值：[`Vector3`](./vector3.md)

- 返回值。


////

///


/// define
`runCommandAsync`


///

```js
runCommandAsync(commandString: string): Promise<CommandResult>
```

/// html | div.result
//// define
`commandString`：`string`

- 参数1。


////

//// define
返回值：<code>Promise&lt;<a href="../commandresult/">CommandResult</a>&gt;</code>

- 返回值。


////

///

