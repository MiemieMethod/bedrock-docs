# `ModalFormData`

> 文档版本：1.21.0.20

`ModalFormData`类。

## 方法

/// define
`constructor`


///

```js
new constructor(): ModalFormData
```

/// html | div.result
//// define
返回值：[`ModalFormData`](./modalformdata.md)

- 返回值。


////

///


/// define
`dropdown`


///

```js
dropdown(label: string, options: string[], defaultValueIndex?: int32): ModalFormData
```

/// html | div.result
//// define
`label`：`string`

- 参数1。


////

//// define
`options`：`string[]`

- 参数2。


////

//// define
`defaultValueIndex`：`int32`|`undefined`

- 参数3。


////

//// define
返回值：[`ModalFormData`](./modalformdata.md)

- 返回值。


////

///


/// define
`icon`


///

```js
icon(iconPath: string): ModalFormData
```

/// html | div.result
//// define
`iconPath`：`string`

- 参数1。


////

//// define
返回值：[`ModalFormData`](./modalformdata.md)

- 返回值。


////

///


/// define
`show`


///

```js
show(player: Player): Promise<ModalFormResponse>
```

/// html | div.result
//// define
`player`：[`Player`](../../server/0.1.0/player.md)

- 参数1。


////

//// define
返回值：<code>Promise&lt;<a href="../modalformresponse/">ModalFormResponse</a>&gt;</code>

- 返回值。


////

///


/// define
`slider`


///

```js
slider(label: string, minimumValue: float, maximumValue: float, valueStep: float, defaultValue?: float): ModalFormData
```

/// html | div.result
//// define
`label`：`string`

- 参数1。


////

//// define
`minimumValue`：`float`

- 参数2。


////

//// define
`maximumValue`：`float`

- 参数3。


////

//// define
`valueStep`：`float`

- 参数4。


////

//// define
`defaultValue`：`float`|`undefined`

- 参数5。


////

//// define
返回值：[`ModalFormData`](./modalformdata.md)

- 返回值。


////

///


/// define
`textField`


///

```js
textField(label: string, placeholderText: string, defaultValue?: string): ModalFormData
```

/// html | div.result
//// define
`label`：`string`

- 参数1。


////

//// define
`placeholderText`：`string`

- 参数2。


////

//// define
`defaultValue`：`string`|`undefined`

- 参数3。


////

//// define
返回值：[`ModalFormData`](./modalformdata.md)

- 返回值。


////

///


/// define
`title`


///

```js
title(titleText: string): ModalFormData
```

/// html | div.result
//// define
`titleText`：`string`

- 参数1。


////

//// define
返回值：[`ModalFormData`](./modalformdata.md)

- 返回值。


////

///


/// define
`toggle`


///

```js
toggle(label: string, defaultValue?: boolean): ModalFormData
```

/// html | div.result
//// define
`label`：`string`

- 参数1。


////

//// define
`defaultValue`：`boolean`|`undefined`

- 参数2。


////

//// define
返回值：[`ModalFormData`](./modalformdata.md)

- 返回值。


////

///

