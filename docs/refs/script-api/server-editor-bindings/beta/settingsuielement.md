# `SettingsUIElement`

> 文档版本：1.21.0.20

`SettingsUIElement`类。script_api.@minecraft/server-editor-bindings.settingsuielement.description

## 属性

/// define
`initialValue`


///

```js
read-only initialValue: boolean | int32;
```

/// html | div.result
//// define
`initialValue`：`boolean`|`int32`

- script_api.@minecraft/server-editor-bindings.settingsuielement.initialvalue.description


////

///


/// define
`max`


///

```js
read-only max: int32 | undefined;
```

/// html | div.result
//// define
`max`：`int32`|`undefined`

- script_api.@minecraft/server-editor-bindings.settingsuielement.max.description


////

///


/// define
`min`


///

```js
read-only min: int32 | undefined;
```

/// html | div.result
//// define
`min`：`int32`|`undefined`

- script_api.@minecraft/server-editor-bindings.settingsuielement.min.description


////

///


/// define
`name`


///

```js
read-only name: string;
```

/// html | div.result
//// define
`name`：`string`

- script_api.@minecraft/server-editor-bindings.settingsuielement.name.description


////

///


/// define
`valueChanged`


///

```js
read-only valueChanged: (arg: boolean | int32) => void | undefined;
```

/// html | div.result
//// define
`valueChanged`：<code>(boolean | int32) =&gt; void</code>|`undefined`

- script_api.@minecraft/server-editor-bindings.settingsuielement.valuechanged.description


////

///


## 方法

/// define
`constructor`


///

script_api.@minecraft/server-editor-bindings.settingsuielement.constructor.description

```js
new constructor(name: string, initialValue: boolean | int32, min?: int32, max?: int32, valueChanged?: (arg: boolean | int32) => void): SettingsUIElement
```

/// html | div.result
//// define
`name`：`string`

- script_api.@minecraft/server-editor-bindings.settingsuielement.constructor.name.description


////

//// define
`initialValue`：`boolean`|`int32`

- script_api.@minecraft/server-editor-bindings.settingsuielement.constructor.initialvalue.description


////

//// define
`min`：`int32`|`undefined`

- script_api.@minecraft/server-editor-bindings.settingsuielement.constructor.min.description


////

//// define
`max`：`int32`|`undefined`

- script_api.@minecraft/server-editor-bindings.settingsuielement.constructor.max.description


////

//// define
`valueChanged`：<code>(boolean | int32) =&gt; void</code>|`undefined`

- script_api.@minecraft/server-editor-bindings.settingsuielement.constructor.valuechanged.description


////

//// define
返回值：[`SettingsUIElement`](./settingsuielement.md)

- script_api.@minecraft/server-editor-bindings.settingsuielement.constructor.return


////

///

