# `BrushShapeManager`

> 文档版本：1.21.60.21

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
`brushShapeList`


///

```js
read-only brushShapeList: BrushShape[];
```

/// html | div.result
//// define
`brushShapeList`：<code><a href="../brushshape/">BrushShape</a>[]</code>

- script_api.@minecraft/server-editor-bindings.brushshapemanager.brushshapelist.description


////

///


## 方法

/// define
`activateBrushTool`


///

script_api.@minecraft/server-editor-bindings.brushshapemanager.activatebrushtool.description

```js
activateBrushTool(): void
```

/// html | div.result
//// define
返回值：`void`

- script_api.@minecraft/server-editor-bindings.brushshapemanager.activatebrushtool.return


////

///


/// define
`beginPainting`


///

script_api.@minecraft/server-editor-bindings.brushshapemanager.beginpainting.description

```js
beginPainting(onComplete: (arg: PaintCompletionState) => void): void
```

/// html | div.result
//// define
`onComplete`：<code>(<a href="../paintcompletionstate/">PaintCompletionState</a>) =&gt; void</code>

- script_api.@minecraft/server-editor-bindings.brushshapemanager.beginpainting.oncomplete.description


////

//// define
返回值：`void`

- script_api.@minecraft/server-editor-bindings.brushshapemanager.beginpainting.return


////

///


/// define
`deactivateBrushTool`


///

script_api.@minecraft/server-editor-bindings.brushshapemanager.deactivatebrushtool.description

```js
deactivateBrushTool(): void
```

/// html | div.result
//// define
返回值：`void`

- script_api.@minecraft/server-editor-bindings.brushshapemanager.deactivatebrushtool.return


////

///


/// define
`endPainting`


///

script_api.@minecraft/server-editor-bindings.brushshapemanager.endpainting.description

```js
endPainting(cancelled: boolean): void
```

/// html | div.result
//// define
`cancelled`：`boolean`

- script_api.@minecraft/server-editor-bindings.brushshapemanager.endpainting.cancelled.description


////

//// define
返回值：`void`

- script_api.@minecraft/server-editor-bindings.brushshapemanager.endpainting.return


////

///


/// define
`getBrushShapeOffset`


///

script_api.@minecraft/server-editor-bindings.brushshapemanager.getbrushshapeoffset.description

```js
getBrushShapeOffset(): Vector3
```

/// html | div.result
//// define
返回值：[`Vector3`](../../server/beta/vector3.md)

- script_api.@minecraft/server-editor-bindings.brushshapemanager.getbrushshapeoffset.return


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
`setBrushMask`


///

script_api.@minecraft/server-editor-bindings.brushshapemanager.setbrushmask.description

```js
setBrushMask(mask: BlockMaskList): void
```

/// html | div.result
//// define
`mask`：[`BlockMaskList`](./blockmasklist.md)

- script_api.@minecraft/server-editor-bindings.brushshapemanager.setbrushmask.mask.description


////

//// define
返回值：`void`

- script_api.@minecraft/server-editor-bindings.brushshapemanager.setbrushmask.return


////

///


/// define
`setBrushShape`


///

script_api.@minecraft/server-editor-bindings.brushshapemanager.setbrushshape.description

```js
setBrushShape(shape: Vector3[] | CompoundBlockVolume): void
```

/// html | div.result
//// define
`shape`：<code><a href="../../../server/beta/vector3/">Vector3</a>[]</code>|[`CompoundBlockVolume`](../../server/beta/compoundblockvolume.md)

- script_api.@minecraft/server-editor-bindings.brushshapemanager.setbrushshape.shape.description


////

//// define
返回值：`void`

- script_api.@minecraft/server-editor-bindings.brushshapemanager.setbrushshape.return


////

///


/// define
`setBrushShapeOffset`


///

script_api.@minecraft/server-editor-bindings.brushshapemanager.setbrushshapeoffset.description

```js
setBrushShapeOffset(offset: Vector3): void
```

/// html | div.result
//// define
`offset`：[`Vector3`](../../server/beta/vector3.md)

- script_api.@minecraft/server-editor-bindings.brushshapemanager.setbrushshapeoffset.offset.description


////

//// define
返回值：`void`

- script_api.@minecraft/server-editor-bindings.brushshapemanager.setbrushshapeoffset.return


////

///


/// define
`setBrushShapeVisible`


///

script_api.@minecraft/server-editor-bindings.brushshapemanager.setbrushshapevisible.description

```js
setBrushShapeVisible(visible: boolean): void
```

/// html | div.result
//// define
`visible`：`boolean`

- script_api.@minecraft/server-editor-bindings.brushshapemanager.setbrushshapevisible.visible.description


////

//// define
返回值：`void`

- script_api.@minecraft/server-editor-bindings.brushshapemanager.setbrushshapevisible.return


////

///


/// define
`setFlattenHeight`


///

script_api.@minecraft/server-editor-bindings.brushshapemanager.setflattenheight.description

```js
setFlattenHeight(flattenHeight: int32): void
```

/// html | div.result
//// define
`flattenHeight`：`int32`

- script_api.@minecraft/server-editor-bindings.brushshapemanager.setflattenheight.flattenheight.description


////

//// define
返回值：`void`

- script_api.@minecraft/server-editor-bindings.brushshapemanager.setflattenheight.return


////

///


/// define
`setFlattenRadius`


///

script_api.@minecraft/server-editor-bindings.brushshapemanager.setflattenradius.description

```js
setFlattenRadius(flattenRadius: int32): void
```

/// html | div.result
//// define
`flattenRadius`：`int32`

- script_api.@minecraft/server-editor-bindings.brushshapemanager.setflattenradius.flattenradius.description


////

//// define
返回值：`void`

- script_api.@minecraft/server-editor-bindings.brushshapemanager.setflattenradius.return


////

///


/// define
`setTerrainStrength`


///

script_api.@minecraft/server-editor-bindings.brushshapemanager.setterrainstrength.description

```js
setTerrainStrength(terrainStrength: int32): void
```

/// html | div.result
//// define
`terrainStrength`：`int32`

- script_api.@minecraft/server-editor-bindings.brushshapemanager.setterrainstrength.terrainstrength.description


////

//// define
返回值：`void`

- script_api.@minecraft/server-editor-bindings.brushshapemanager.setterrainstrength.return


////

///


/// define
`singlePaint`


///

script_api.@minecraft/server-editor-bindings.brushshapemanager.singlepaint.description

```js
singlePaint(onComplete: (arg: PaintCompletionState) => void): void
```

/// html | div.result
//// define
`onComplete`：<code>(<a href="../paintcompletionstate/">PaintCompletionState</a>) =&gt; void</code>

- script_api.@minecraft/server-editor-bindings.brushshapemanager.singlepaint.oncomplete.description


////

//// define
返回值：`void`

- script_api.@minecraft/server-editor-bindings.brushshapemanager.singlepaint.return


////

///


/// define
`switchBrushPaintMode`


///

script_api.@minecraft/server-editor-bindings.brushshapemanager.switchbrushpaintmode.description

```js
switchBrushPaintMode(paintMode: PaintMode): void
```

/// html | div.result
//// define
`paintMode`：[`PaintMode`](./paintmode.md)

- script_api.@minecraft/server-editor-bindings.brushshapemanager.switchbrushpaintmode.paintmode.description


////

//// define
返回值：`void`

- script_api.@minecraft/server-editor-bindings.brushshapemanager.switchbrushpaintmode.return


////

///


/// define
`switchBrushShape`


///

script_api.@minecraft/server-editor-bindings.brushshapemanager.switchbrushshape.description

```js
switchBrushShape(name: string): CompoundBlockVolume
```

/// html | div.result
//// define
`name`：`string`

- script_api.@minecraft/server-editor-bindings.brushshapemanager.switchbrushshape.name.description


////

//// define
返回值：[`CompoundBlockVolume`](../../server/beta/compoundblockvolume.md)

- script_api.@minecraft/server-editor-bindings.brushshapemanager.switchbrushshape.return


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

