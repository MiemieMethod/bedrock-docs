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
dropdown(label: RawMessage | string, options: RawMessage | string[], defaultValueIndex?: int32): ModalFormData
```

/// html | div.result
//// define
`label`：[`RawMessage`](../../server/1.8.0/rawmessage.md)|`string`

- 参数1。


////

//// define
`options`：`RawMessage | string[]`

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
`show`


///

```js
show(player: Player): Promise<ModalFormResponse>
```

/// html | div.result
//// define
`player`：[`Player`](../../server/1.8.0/player.md)

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
slider(label: RawMessage | string, minimumValue: float, maximumValue: float, valueStep: float, defaultValue?: float): ModalFormData
```

/// html | div.result
//// define
`label`：[`RawMessage`](../../server/1.8.0/rawmessage.md)|`string`

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
`submitButton`


///

```js
submitButton(submitButtonText: RawMessage | string): ModalFormData
```

/// html | div.result
//// define
`submitButtonText`：[`RawMessage`](../../server/1.8.0/rawmessage.md)|`string`

- 参数1。


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
textField(label: RawMessage | string, placeholderText: RawMessage | string, defaultValue?: RawMessage | string): ModalFormData
```

/// html | div.result
//// define
`label`：[`RawMessage`](../../server/1.8.0/rawmessage.md)|`string`

- 参数1。


////

//// define
`placeholderText`：[`RawMessage`](../../server/1.8.0/rawmessage.md)|`string`

- 参数2。


////

//// define
`defaultValue`：[`RawMessage`](../../server/1.8.0/rawmessage.md)|`string`|`undefined`

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
title(titleText: RawMessage | string): ModalFormData
```

/// html | div.result
//// define
`titleText`：[`RawMessage`](../../server/1.8.0/rawmessage.md)|`string`

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
toggle(label: RawMessage | string, defaultValue?: boolean): ModalFormData
```

/// html | div.result
//// define
`label`：[`RawMessage`](../../server/1.8.0/rawmessage.md)|`string`

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

