# `ModalFormData`

> 文档版本：1.21.0.21

`ModalFormData`类。script_api.@minecraft/server-ui.modalformdata.description

## 方法

/// define
`constructor`


///

script_api.@minecraft/server-ui.modalformdata.constructor.description

```js
new constructor(): ModalFormData
```

/// html | div.result
//// define
返回值：[`ModalFormData`](./modalformdata.md)

- script_api.@minecraft/server-ui.modalformdata.constructor.return


////

///


/// define
`dropdown`


///

script_api.@minecraft/server-ui.modalformdata.dropdown.description

```js
dropdown(label: RawMessage | string, options: (RawMessage | string)[], defaultValueIndex?: int32): ModalFormData
```

/// html | div.result
//// define
`label`：[`RawMessage`](../../server/internal/rawmessage.md)|`string`

- script_api.@minecraft/server-ui.modalformdata.dropdown.label.description


////

//// define
`options`：`(RawMessage | string)[]`

- script_api.@minecraft/server-ui.modalformdata.dropdown.options.description


////

//// define
`defaultValueIndex`：`int32`|`undefined`

- script_api.@minecraft/server-ui.modalformdata.dropdown.defaultvalueindex.description


////

//// define
返回值：[`ModalFormData`](./modalformdata.md)

- script_api.@minecraft/server-ui.modalformdata.dropdown.return


////

///


/// define
`show`


///

script_api.@minecraft/server-ui.modalformdata.show.description

```js
show(player: Player): Promise<ModalFormResponse>
```

/// html | div.result
//// define
`player`：[`Player`](../../server/internal/player.md)

- script_api.@minecraft/server-ui.modalformdata.show.player.description


////

//// define
返回值：<code>Promise&lt;<a href="../modalformresponse/">ModalFormResponse</a>&gt;</code>

- script_api.@minecraft/server-ui.modalformdata.show.return


////

///


/// define
`slider`


///

script_api.@minecraft/server-ui.modalformdata.slider.description

```js
slider(label: RawMessage | string, minimumValue: float, maximumValue: float, valueStep: float, defaultValue?: float): ModalFormData
```

/// html | div.result
//// define
`label`：[`RawMessage`](../../server/internal/rawmessage.md)|`string`

- script_api.@minecraft/server-ui.modalformdata.slider.label.description


////

//// define
`minimumValue`：`float`

- script_api.@minecraft/server-ui.modalformdata.slider.minimumvalue.description


////

//// define
`maximumValue`：`float`

- script_api.@minecraft/server-ui.modalformdata.slider.maximumvalue.description


////

//// define
`valueStep`：`float`

- script_api.@minecraft/server-ui.modalformdata.slider.valuestep.description


////

//// define
`defaultValue`：`float`|`undefined`

- script_api.@minecraft/server-ui.modalformdata.slider.defaultvalue.description


////

//// define
返回值：[`ModalFormData`](./modalformdata.md)

- script_api.@minecraft/server-ui.modalformdata.slider.return


////

///


/// define
`submitButton`


///

script_api.@minecraft/server-ui.modalformdata.submitbutton.description

```js
submitButton(submitButtonText: RawMessage | string): ModalFormData
```

/// html | div.result
//// define
`submitButtonText`：[`RawMessage`](../../server/internal/rawmessage.md)|`string`

- script_api.@minecraft/server-ui.modalformdata.submitbutton.submitbuttontext.description


////

//// define
返回值：[`ModalFormData`](./modalformdata.md)

- script_api.@minecraft/server-ui.modalformdata.submitbutton.return


////

///


/// define
`textField`


///

script_api.@minecraft/server-ui.modalformdata.textfield.description

```js
textField(label: RawMessage | string, placeholderText: RawMessage | string, defaultValue?: RawMessage | string): ModalFormData
```

/// html | div.result
//// define
`label`：[`RawMessage`](../../server/internal/rawmessage.md)|`string`

- script_api.@minecraft/server-ui.modalformdata.textfield.label.description


////

//// define
`placeholderText`：[`RawMessage`](../../server/internal/rawmessage.md)|`string`

- script_api.@minecraft/server-ui.modalformdata.textfield.placeholdertext.description


////

//// define
`defaultValue`：[`RawMessage`](../../server/internal/rawmessage.md)|`string`|`undefined`

- script_api.@minecraft/server-ui.modalformdata.textfield.defaultvalue.description


////

//// define
返回值：[`ModalFormData`](./modalformdata.md)

- script_api.@minecraft/server-ui.modalformdata.textfield.return


////

///


/// define
`title`


///

script_api.@minecraft/server-ui.modalformdata.title.description

```js
title(titleText: RawMessage | string): ModalFormData
```

/// html | div.result
//// define
`titleText`：[`RawMessage`](../../server/internal/rawmessage.md)|`string`

- script_api.@minecraft/server-ui.modalformdata.title.titletext.description


////

//// define
返回值：[`ModalFormData`](./modalformdata.md)

- script_api.@minecraft/server-ui.modalformdata.title.return


////

///


/// define
`toggle`


///

script_api.@minecraft/server-ui.modalformdata.toggle.description

```js
toggle(label: RawMessage | string, defaultValue?: boolean): ModalFormData
```

/// html | div.result
//// define
`label`：[`RawMessage`](../../server/internal/rawmessage.md)|`string`

- script_api.@minecraft/server-ui.modalformdata.toggle.label.description


////

//// define
`defaultValue`：`boolean`|`undefined`

- script_api.@minecraft/server-ui.modalformdata.toggle.defaultvalue.description


////

//// define
返回值：[`ModalFormData`](./modalformdata.md)

- script_api.@minecraft/server-ui.modalformdata.toggle.return


////

///

