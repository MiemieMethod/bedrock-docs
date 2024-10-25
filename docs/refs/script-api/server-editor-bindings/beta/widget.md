# `Widget`

> 文档版本：1.21.50.25

`Widget`类。script_api.@minecraft/server-editor-bindings.widget.description

## 属性

/// define
`collisionOffset`


///

```js
collisionOffset: Vector3;
```

/// html | div.result
//// define
`collisionOffset`：[`Vector3`](../../server/beta/vector3.md)

- script_api.@minecraft/server-editor-bindings.widget.collisionoffset.description


////

///


/// define
`collisionRadius`


///

```js
collisionRadius: float;
```

/// html | div.result
//// define
`collisionRadius`：`float`

- script_api.@minecraft/server-editor-bindings.widget.collisionradius.description


////

///


/// define
`location`


///

```js
location: Vector3;
```

/// html | div.result
//// define
`location`：[`Vector3`](../../server/beta/vector3.md)

- script_api.@minecraft/server-editor-bindings.widget.location.description


////

///


/// define
`selectable`


///

```js
read-only selectable: boolean;
```

/// html | div.result
//// define
`selectable`：`boolean`

- script_api.@minecraft/server-editor-bindings.widget.selectable.description


////

///


/// define
`selected`


///

```js
selected: boolean;
```

/// html | div.result
//// define
`selected`：`boolean`

- script_api.@minecraft/server-editor-bindings.widget.selected.description


////

///


/// define
`showBoundingBox`


///

```js
showBoundingBox: boolean;
```

/// html | div.result
//// define
`showBoundingBox`：`boolean`

- script_api.@minecraft/server-editor-bindings.widget.showboundingbox.description


////

///


/// define
`showCollisionRadius`


///

```js
showCollisionRadius: boolean;
```

/// html | div.result
//// define
`showCollisionRadius`：`boolean`

- script_api.@minecraft/server-editor-bindings.widget.showcollisionradius.description


////

///


/// define
`snapToBlockLocation`


///

```js
snapToBlockLocation: boolean;
```

/// html | div.result
//// define
`snapToBlockLocation`：`boolean`

- script_api.@minecraft/server-editor-bindings.widget.snaptoblocklocation.description


////

///


/// define
`visible`


///

```js
visible: boolean;
```

/// html | div.result
//// define
`visible`：`boolean`

- script_api.@minecraft/server-editor-bindings.widget.visible.description


////

///


## 方法

/// define
`addEntityComponent`


///

script_api.@minecraft/server-editor-bindings.widget.addentitycomponent.description

```js
addEntityComponent(componentName: string, actorNameId: string, options?: WidgetComponentEntityOptions): WidgetComponentEntity
```

/// html | div.result
//// define
`componentName`：`string`

- script_api.@minecraft/server-editor-bindings.widget.addentitycomponent.componentname.description


////

//// define
`actorNameId`：`string`

- script_api.@minecraft/server-editor-bindings.widget.addentitycomponent.actornameid.description


////

//// define
`options`?：[`WidgetComponentEntityOptions`](./widgetcomponententityoptions.md)＝`null`

- script_api.@minecraft/server-editor-bindings.widget.addentitycomponent.options.description


////

//// define
返回值：[`WidgetComponentEntity`](./widgetcomponententity.md)

- script_api.@minecraft/server-editor-bindings.widget.addentitycomponent.return


////

///


/// define
`addGizmoComponent`


///

script_api.@minecraft/server-editor-bindings.widget.addgizmocomponent.description

```js
addGizmoComponent(componentName: string, options?: WidgetComponentGizmoOptions): WidgetComponentGizmo
```

/// html | div.result
//// define
`componentName`：`string`

- script_api.@minecraft/server-editor-bindings.widget.addgizmocomponent.componentname.description


////

//// define
`options`?：[`WidgetComponentGizmoOptions`](./widgetcomponentgizmooptions.md)＝`null`

- script_api.@minecraft/server-editor-bindings.widget.addgizmocomponent.options.description


////

//// define
返回值：[`WidgetComponentGizmo`](./widgetcomponentgizmo.md)

- script_api.@minecraft/server-editor-bindings.widget.addgizmocomponent.return


////

///


/// define
`addGuideComponent`


///

script_api.@minecraft/server-editor-bindings.widget.addguidecomponent.description

```js
addGuideComponent(componentName: string, options?: WidgetComponentGuideOptions): WidgetComponentGuide
```

/// html | div.result
//// define
`componentName`：`string`

- script_api.@minecraft/server-editor-bindings.widget.addguidecomponent.componentname.description


////

//// define
`options`?：[`WidgetComponentGuideOptions`](./widgetcomponentguideoptions.md)＝`null`

- script_api.@minecraft/server-editor-bindings.widget.addguidecomponent.options.description


////

//// define
返回值：[`WidgetComponentGuide`](./widgetcomponentguide.md)

- script_api.@minecraft/server-editor-bindings.widget.addguidecomponent.return


////

///


/// define
`addRenderPrimitiveComponent`


///

script_api.@minecraft/server-editor-bindings.widget.addrenderprimitivecomponent.description

```js
addRenderPrimitiveComponent(componentName: string, primitiveType: WidgetComponentRenderPrimitiveAxialSphere | WidgetComponentRenderPrimitiveBox | WidgetComponentRenderPrimitiveDisc | WidgetComponentRenderPrimitiveLine, options?: WidgetComponentRenderPrimitiveOptions): WidgetComponentRenderPrimitive
```

/// html | div.result
//// define
`componentName`：`string`

- script_api.@minecraft/server-editor-bindings.widget.addrenderprimitivecomponent.componentname.description


////

//// define
`primitiveType`：[`WidgetComponentRenderPrimitiveAxialSphere`](./widgetcomponentrenderprimitiveaxialsphere.md)|[`WidgetComponentRenderPrimitiveBox`](./widgetcomponentrenderprimitivebox.md)|[`WidgetComponentRenderPrimitiveDisc`](./widgetcomponentrenderprimitivedisc.md)|[`WidgetComponentRenderPrimitiveLine`](./widgetcomponentrenderprimitiveline.md)

- script_api.@minecraft/server-editor-bindings.widget.addrenderprimitivecomponent.primitivetype.description


////

//// define
`options`?：[`WidgetComponentRenderPrimitiveOptions`](./widgetcomponentrenderprimitiveoptions.md)＝`null`

- script_api.@minecraft/server-editor-bindings.widget.addrenderprimitivecomponent.options.description


////

//// define
返回值：[`WidgetComponentRenderPrimitive`](./widgetcomponentrenderprimitive.md)

- script_api.@minecraft/server-editor-bindings.widget.addrenderprimitivecomponent.return


////

///


/// define
`addSplineComponent`


///

script_api.@minecraft/server-editor-bindings.widget.addsplinecomponent.description

```js
addSplineComponent(componentName: string, options?: WidgetComponentSplineOptions): WidgetComponentSpline
```

/// html | div.result
//// define
`componentName`：`string`

- script_api.@minecraft/server-editor-bindings.widget.addsplinecomponent.componentname.description


////

//// define
`options`?：[`WidgetComponentSplineOptions`](./widgetcomponentsplineoptions.md)＝`null`

- script_api.@minecraft/server-editor-bindings.widget.addsplinecomponent.options.description


////

//// define
返回值：[`WidgetComponentSpline`](./widgetcomponentspline.md)

- script_api.@minecraft/server-editor-bindings.widget.addsplinecomponent.return


////

///


/// define
`addTextComponent`


///

script_api.@minecraft/server-editor-bindings.widget.addtextcomponent.description

```js
addTextComponent(componentName: string, label: string, options?: WidgetComponentTextOptions): WidgetComponentText
```

/// html | div.result
//// define
`componentName`：`string`

- script_api.@minecraft/server-editor-bindings.widget.addtextcomponent.componentname.description


////

//// define
`label`：`string`

- script_api.@minecraft/server-editor-bindings.widget.addtextcomponent.label.description


////

//// define
`options`?：[`WidgetComponentTextOptions`](./widgetcomponenttextoptions.md)＝`null`

- script_api.@minecraft/server-editor-bindings.widget.addtextcomponent.options.description


////

//// define
返回值：[`WidgetComponentText`](./widgetcomponenttext.md)

- script_api.@minecraft/server-editor-bindings.widget.addtextcomponent.return


////

///


/// define
`delete`


///

script_api.@minecraft/server-editor-bindings.widget.delete.description

```js
delete(): void
```

/// html | div.result
//// define
返回值：`void`

- script_api.@minecraft/server-editor-bindings.widget.delete.return


////

///


/// define
`deleteComponent`


///

script_api.@minecraft/server-editor-bindings.widget.deletecomponent.description

```js
deleteComponent(componentOrName: string | WidgetComponentBase): void
```

/// html | div.result
//// define
`componentOrName`：`string`|[`WidgetComponentBase`](./widgetcomponentbase.md)

- script_api.@minecraft/server-editor-bindings.widget.deletecomponent.componentorname.description


////

//// define
返回值：`void`

- script_api.@minecraft/server-editor-bindings.widget.deletecomponent.return


////

///


/// define
`getComponent`


///

script_api.@minecraft/server-editor-bindings.widget.getcomponent.description

```js
getComponent(componentName: string): WidgetComponentBase
```

/// html | div.result
//// define
`componentName`：`string`

- script_api.@minecraft/server-editor-bindings.widget.getcomponent.componentname.description


////

//// define
返回值：[`WidgetComponentBase`](./widgetcomponentbase.md)

- script_api.@minecraft/server-editor-bindings.widget.getcomponent.return


////

///


/// define
`getComponents`


///

script_api.@minecraft/server-editor-bindings.widget.getcomponents.description

```js
getComponents(): WidgetComponentBase[]
```

/// html | div.result
//// define
返回值：<code><a href="../widgetcomponentbase/">WidgetComponentBase</a>[]</code>

- script_api.@minecraft/server-editor-bindings.widget.getcomponents.return


////

///


/// define
`setStateChangeEvent`


///

script_api.@minecraft/server-editor-bindings.widget.setstatechangeevent.description

```js
setStateChangeEvent(eventFunction?: (arg: WidgetStateChangeEventData) => void): void
```

/// html | div.result
//// define
`eventFunction`?：<code>(<a href="../widgetstatechangeeventdata/">WidgetStateChangeEventData</a>) =&gt; void</code>＝`null`

- script_api.@minecraft/server-editor-bindings.widget.setstatechangeevent.eventfunction.description


////

//// define
返回值：`void`

- script_api.@minecraft/server-editor-bindings.widget.setstatechangeevent.return


////

///

