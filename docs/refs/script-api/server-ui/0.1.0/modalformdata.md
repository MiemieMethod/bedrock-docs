# `ModalFormData`

> 文档版本：1.21.60.21

`ModalFormData`类。script_api.mojang-minecraft-ui.modalformdata.description

## 方法

/// define
`constructor`


///

script_api.mojang-minecraft-ui.modalformdata.constructor.description

```js
new constructor(): ModalFormData
```

/// html | div.result
//// define
返回值：[`ModalFormData`](./modalformdata.md)

- script_api.mojang-minecraft-ui.modalformdata.constructor.return


////

///


/// define
`dropdown`


///

script_api.mojang-minecraft-ui.modalformdata.dropdown.description

```js
dropdown(label: string, options: string[], defaultValueIndex?: int32): ModalFormData
```

/// html | div.result
//// define
`label`：`string`

- script_api.mojang-minecraft-ui.modalformdata.dropdown.label.description


////

//// define
`options`：`string[]`

- script_api.mojang-minecraft-ui.modalformdata.dropdown.options.description


////

//// define
`defaultValueIndex`?：`int32`＝`null`

- script_api.mojang-minecraft-ui.modalformdata.dropdown.defaultvalueindex.description


////

//// define
返回值：[`ModalFormData`](./modalformdata.md)

- script_api.mojang-minecraft-ui.modalformdata.dropdown.return


////

///


/// define
`icon`


///

script_api.mojang-minecraft-ui.modalformdata.icon.description

```js
icon(iconPath: string): ModalFormData
```

/// html | div.result
//// define
`iconPath`：`string`

- script_api.mojang-minecraft-ui.modalformdata.icon.iconpath.description


////

//// define
返回值：[`ModalFormData`](./modalformdata.md)

- script_api.mojang-minecraft-ui.modalformdata.icon.return


////

///


/// define
`show`


///

script_api.mojang-minecraft-ui.modalformdata.show.description

```js
show(player: Player): Promise<ModalFormResponse>
```

/// html | div.result
//// define
`player`：[`Player`](../../server/0.1.0/player.md)

- script_api.mojang-minecraft-ui.modalformdata.show.player.description


////

//// define
返回值：<code>Promise&lt;<a href="../modalformresponse/">ModalFormResponse</a>&gt;</code>

- script_api.mojang-minecraft-ui.modalformdata.show.return


////

///


/// define
`slider`


///

script_api.mojang-minecraft-ui.modalformdata.slider.description

```js
slider(label: string, minimumValue: float, maximumValue: float, valueStep: float, defaultValue?: float): ModalFormData
```

/// html | div.result
//// define
`label`：`string`

- script_api.mojang-minecraft-ui.modalformdata.slider.label.description


////

//// define
`minimumValue`：`float`

- script_api.mojang-minecraft-ui.modalformdata.slider.minimumvalue.description


////

//// define
`maximumValue`：`float`

- script_api.mojang-minecraft-ui.modalformdata.slider.maximumvalue.description


////

//// define
`valueStep`：`float`

- script_api.mojang-minecraft-ui.modalformdata.slider.valuestep.description


////

//// define
`defaultValue`?：`float`＝`null`

- script_api.mojang-minecraft-ui.modalformdata.slider.defaultvalue.description


////

//// define
返回值：[`ModalFormData`](./modalformdata.md)

- script_api.mojang-minecraft-ui.modalformdata.slider.return


////

///


/// define
`textField`


///

script_api.mojang-minecraft-ui.modalformdata.textfield.description

```js
textField(label: string, placeholderText: string, defaultValue?: string): ModalFormData
```

/// html | div.result
//// define
`label`：`string`

- script_api.mojang-minecraft-ui.modalformdata.textfield.label.description


////

//// define
`placeholderText`：`string`

- script_api.mojang-minecraft-ui.modalformdata.textfield.placeholdertext.description


////

//// define
`defaultValue`?：`string`＝`null`

- script_api.mojang-minecraft-ui.modalformdata.textfield.defaultvalue.description


////

//// define
返回值：[`ModalFormData`](./modalformdata.md)

- script_api.mojang-minecraft-ui.modalformdata.textfield.return


////

///


/// define
`title`


///

script_api.mojang-minecraft-ui.modalformdata.title.description

```js
title(titleText: string): ModalFormData
```

/// html | div.result
//// define
`titleText`：`string`

- script_api.mojang-minecraft-ui.modalformdata.title.titletext.description


////

//// define
返回值：[`ModalFormData`](./modalformdata.md)

- script_api.mojang-minecraft-ui.modalformdata.title.return


////

///


/// define
`toggle`


///

script_api.mojang-minecraft-ui.modalformdata.toggle.description

```js
toggle(label: string, defaultValue?: boolean): ModalFormData
```

/// html | div.result
//// define
`label`：`string`

- script_api.mojang-minecraft-ui.modalformdata.toggle.label.description


////

//// define
`defaultValue`?：`boolean`＝`null`

- script_api.mojang-minecraft-ui.modalformdata.toggle.defaultvalue.description


////

//// define
返回值：[`ModalFormData`](./modalformdata.md)

- script_api.mojang-minecraft-ui.modalformdata.toggle.return


////

///

