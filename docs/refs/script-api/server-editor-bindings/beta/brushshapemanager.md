# `BrushShapeManager`

> 文档版本：1.21.0.24

`BrushShapeManager`类。script_api.@minecraft/server-editor-bindings.brushshapemanager.description

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

- script_api.@minecraft/server-editor-bindings.brushshapemanager.activebrushshape.description


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

- script_api.@minecraft/server-editor-bindings.brushshapemanager.activebrushvolume.description


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

- script_api.@minecraft/server-editor-bindings.brushshapemanager.brushshapenames.description


////

///


## 方法

/// define
`activateBrushShape`


///

script_api.@minecraft/server-editor-bindings.brushshapemanager.activatebrushshape.description

```js
activateBrushShape(name: string): CompoundBlockVolume
```

/// html | div.result
//// define
`name`：`string`

- script_api.@minecraft/server-editor-bindings.brushshapemanager.activatebrushshape.name.description


////

//// define
返回值：[`CompoundBlockVolume`](../../server/beta/compoundblockvolume.md)

- script_api.@minecraft/server-editor-bindings.brushshapemanager.activatebrushshape.return


////

///


/// define
`getSettingsUIElements`


///

script_api.@minecraft/server-editor-bindings.brushshapemanager.getsettingsuielements.description

```js
getSettingsUIElements(brushName: string): SettingsUIElement[]
```

/// html | div.result
//// define
`brushName`：`string`

- script_api.@minecraft/server-editor-bindings.brushshapemanager.getsettingsuielements.brushname.description


////

//// define
返回值：<code><a href="../settingsuielement/">SettingsUIElement</a>[]</code>

- script_api.@minecraft/server-editor-bindings.brushshapemanager.getsettingsuielements.return


////

///


/// define
`registerBrushShape`


///

script_api.@minecraft/server-editor-bindings.brushshapemanager.registerbrushshape.description

```js
registerBrushShape(name: string, icon: string, rebuild: () => CompoundBlockVolume, getSettingsUIElements: () => SettingsUIElement[]): void
```

/// html | div.result
//// define
`name`：`string`

- script_api.@minecraft/server-editor-bindings.brushshapemanager.registerbrushshape.name.description


////

//// define
`icon`：`string`

- script_api.@minecraft/server-editor-bindings.brushshapemanager.registerbrushshape.icon.description


////

//// define
`rebuild`：<code>() =&gt; <a href="../../../server/beta/compoundblockvolume/">CompoundBlockVolume</a></code>

- script_api.@minecraft/server-editor-bindings.brushshapemanager.registerbrushshape.rebuild.description


////

//// define
`getSettingsUIElements`：<code>() =&gt; SettingsUIElement[]</code>

- script_api.@minecraft/server-editor-bindings.brushshapemanager.registerbrushshape.getsettingsuielements.description


////

//// define
返回值：`void`

- script_api.@minecraft/server-editor-bindings.brushshapemanager.registerbrushshape.return


////

///


/// define
`uiSettingValueChanged`


///

script_api.@minecraft/server-editor-bindings.brushshapemanager.uisettingvaluechanged.description

```js
uiSettingValueChanged(elementName: string, newValue: boolean | float | string | Vector3): boolean
```

/// html | div.result
//// define
`elementName`：`string`

- script_api.@minecraft/server-editor-bindings.brushshapemanager.uisettingvaluechanged.elementname.description


////

//// define
`newValue`：`boolean`|`float`|`string`|[`Vector3`](../../server/beta/vector3.md)

- script_api.@minecraft/server-editor-bindings.brushshapemanager.uisettingvaluechanged.newvalue.description


////

//// define
返回值：`boolean`

- script_api.@minecraft/server-editor-bindings.brushshapemanager.uisettingvaluechanged.return


////

///

