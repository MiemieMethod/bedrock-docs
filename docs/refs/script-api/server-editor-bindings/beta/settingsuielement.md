# `SettingsUIElement`

> 文档版本：1.21.0.21

`SettingsUIElement`类。script_api.@minecraft/server-editor-bindings.settingsuielement.description

## 属性

/// define
`initialValue`


///

```js
read-only initialValue: boolean | float | string | Vector3;
```

/// html | div.result
//// define
`initialValue`：`boolean`|`float`|`string`|[`Vector3`](../../server/beta/vector3.md)

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
`onChange`


///

```js
read-only onChange: (arg: boolean | float | string | Vector3) => boolean;
```

/// html | div.result
//// define
`onChange`：<code>(boolean | float | string | Vector3) =&gt; boolean</code>

- script_api.@minecraft/server-editor-bindings.settingsuielement.onchange.description


////

///


/// define
`options`


///

```js
read-only options: string[] | undefined;
```

/// html | div.result
//// define
`options`：`string[]`|`undefined`

- script_api.@minecraft/server-editor-bindings.settingsuielement.options.description


////

///


## 方法

/// define
`constructor`


///

script_api.@minecraft/server-editor-bindings.settingsuielement.constructor.description

```js
new constructor(name: string, initialValue: boolean | float | string | Vector3, onChange: (arg: boolean | float | string | Vector3) => boolean, min?: int32, max?: int32, options?: string[]): SettingsUIElement
```

/// html | div.result
//// define
`name`：`string`

- script_api.@minecraft/server-editor-bindings.settingsuielement.constructor.name.description


////

//// define
`initialValue`：`boolean`|`float`|`string`|[`Vector3`](../../server/beta/vector3.md)

- script_api.@minecraft/server-editor-bindings.settingsuielement.constructor.initialvalue.description


////

//// define
`onChange`：<code>(boolean | float | string | Vector3) =&gt; boolean</code>

- script_api.@minecraft/server-editor-bindings.settingsuielement.constructor.onchange.description


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
`options`：`string[]`|`undefined`

- script_api.@minecraft/server-editor-bindings.settingsuielement.constructor.options.description


////

//// define
返回值：[`SettingsUIElement`](./settingsuielement.md)

- script_api.@minecraft/server-editor-bindings.settingsuielement.constructor.return


////

///

