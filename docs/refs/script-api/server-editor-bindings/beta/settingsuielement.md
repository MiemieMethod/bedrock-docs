# `SettingsUIElement`

> 文档版本：1.21.0.20

`SettingsUIElement`类。

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

- 属性。


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

- 属性。


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

- 属性。


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

- 属性。


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

- 属性。


////

///


## 方法

/// define
`constructor`


///

```js
new constructor(name: string, initialValue: boolean | int32, min?: int32, max?: int32, valueChanged?: (arg: boolean | int32) => void): SettingsUIElement
```

/// html | div.result
//// define
`name`：`string`

- 参数1。


////

//// define
`initialValue`：`boolean`|`int32`

- 参数2。


////

//// define
`min`：`int32`|`undefined`

- 参数3。


////

//// define
`max`：`int32`|`undefined`

- 参数4。


////

//// define
`valueChanged`：<code>(boolean | int32) =&gt; void</code>|`undefined`

- 参数5。


////

//// define
返回值：[`SettingsUIElement`](./settingsuielement.md)

- 返回值。


////

///

