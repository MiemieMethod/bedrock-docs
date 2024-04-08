# `ActionFormData`

> 文档版本：1.21.0.20

`ActionFormData`类。

## 方法

/// define
`body`


///

```js
body(bodyText: RawMessage | string): ActionFormData
```

/// html | div.result
//// define
`bodyText`：[`RawMessage`](../../server/1.8.0/rawmessage.md)|`string`

- 参数1。


////

//// define
返回值：[`ActionFormData`](./actionformdata.md)

- 返回值。


////

///


/// define
`button`


///

```js
button(text: RawMessage | string, iconPath?: string): ActionFormData
```

/// html | div.result
//// define
`text`：[`RawMessage`](../../server/1.8.0/rawmessage.md)|`string`

- 参数1。


////

//// define
`iconPath`：`string`|`undefined`

- 参数2。


////

//// define
返回值：[`ActionFormData`](./actionformdata.md)

- 返回值。


////

///


/// define
`constructor`


///

```js
new constructor(): ActionFormData
```

/// html | div.result
//// define
返回值：[`ActionFormData`](./actionformdata.md)

- 返回值。


////

///


/// define
`show`


///

```js
show(player: Player): Promise<ActionFormResponse>
```

/// html | div.result
//// define
`player`：[`Player`](../../server/1.8.0/player.md)

- 参数1。


////

//// define
返回值：<code>Promise&lt;<a href="../actionformresponse/">ActionFormResponse</a>&gt;</code>

- 返回值。


////

///


/// define
`title`


///

```js
title(titleText: RawMessage | string): ActionFormData
```

/// html | div.result
//// define
`titleText`：[`RawMessage`](../../server/1.8.0/rawmessage.md)|`string`

- 参数1。


////

//// define
返回值：[`ActionFormData`](./actionformdata.md)

- 返回值。


////

///

