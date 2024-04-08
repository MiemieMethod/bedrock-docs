# `BrushShapeManager`

> 文档版本：1.21.0.20

`BrushShapeManager`类。

## 属性

/// define
`activeBrushShape`


///

```js
read-only activeBrushShape: BrushShape | undefined;
```

/// html | div.result
//// define
`activeBrushShape`：[`BrushShape`](./brushshape.md)|`undefined`

- 属性。


////

///


/// define
`activeBrushVolume`


///

```js
read-only activeBrushVolume: CompoundBlockVolume | undefined;
```

/// html | div.result
//// define
`activeBrushVolume`：[`CompoundBlockVolume`](../../server/beta/compoundblockvolume.md)|`undefined`

- 属性。


////

///


/// define
`brushShapeNames`


///

```js
read-only brushShapeNames: string[];
```

/// html | div.result
//// define
`brushShapeNames`：`string[]`

- 属性。


////

///


## 方法

/// define
`activateBrushShape`


///

```js
activateBrushShape(name: string): CompoundBlockVolume
```

/// html | div.result
//// define
`name`：`string`

- 参数1。


////

//// define
返回值：[`CompoundBlockVolume`](../../server/beta/compoundblockvolume.md)

- 返回值。


////

///


/// define
`getSettingsUIElements`


///

```js
getSettingsUIElements(brushName: string): SettingsUIElement[]
```

/// html | div.result
//// define
`brushName`：`string`

- 参数1。


////

//// define
返回值：<code><a href="../settingsuielement/">SettingsUIElement</a>[]</code>

- 返回值。


////

///


/// define
`registerBrushShape`


///

```js
registerBrushShape(brushShape: BrushShape): void
```

/// html | div.result
//// define
`brushShape`：[`BrushShape`](./brushshape.md)

- 参数1。


////

//// define
返回值：`void`

- 返回值。


////

///


/// define
`uiSettingValueChanged`


///

```js
uiSettingValueChanged(elementName: string, newValue: boolean | int32): void
```

/// html | div.result
//// define
`elementName`：`string`

- 参数1。


////

//// define
`newValue`：`boolean`|`int32`

- 参数2。


////

//// define
返回值：`void`

- 返回值。


////

///

