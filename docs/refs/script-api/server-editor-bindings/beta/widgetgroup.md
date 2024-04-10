# `WidgetGroup`

> 文档版本：1.21.0.20

`WidgetGroup`类。script_api.@minecraft/server-editor-bindings.widgetgroup.description

## 属性

/// define
`valid`


///

```js
read-only valid: boolean;
```

/// html | div.result
//// define
`valid`：`boolean`

- script_api.@minecraft/server-editor-bindings.widgetgroup.valid.description


////

///


## 方法

/// define
`areAnySelected`


///

script_api.@minecraft/server-editor-bindings.widgetgroup.areanyselected.description

```js
areAnySelected(): boolean
```

/// html | div.result
//// define
返回值：`boolean`

- script_api.@minecraft/server-editor-bindings.widgetgroup.areanyselected.return


////

///


/// define
`createCustomWidget`


///

script_api.@minecraft/server-editor-bindings.widgetgroup.createcustomwidget.description

```js
createCustomWidget(customEntityName: string, location: Vector3, rotation?: Vector2, options?: CustomWidgetCreateOptions): CustomWidget
```

/// html | div.result
//// define
`customEntityName`：`string`

- script_api.@minecraft/server-editor-bindings.widgetgroup.createcustomwidget.customentityname.description


////

//// define
`location`：[`Vector3`](../../server/beta/vector3.md)

- script_api.@minecraft/server-editor-bindings.widgetgroup.createcustomwidget.location.description


////

//// define
`rotation`：[`Vector2`](../../server/beta/vector2.md)|`undefined`

- script_api.@minecraft/server-editor-bindings.widgetgroup.createcustomwidget.rotation.description


////

//// define
`options`：[`CustomWidgetCreateOptions`](./customwidgetcreateoptions.md)|`undefined`

- script_api.@minecraft/server-editor-bindings.widgetgroup.createcustomwidget.options.description


////

//// define
返回值：[`CustomWidget`](./customwidget.md)

- script_api.@minecraft/server-editor-bindings.widgetgroup.createcustomwidget.return


////

///


/// define
`deleteWidget`


///

script_api.@minecraft/server-editor-bindings.widgetgroup.deletewidget.description

```js
deleteWidget(widgetToDelete: Widget): void
```

/// html | div.result
//// define
`widgetToDelete`：[`Widget`](./widget.md)

- script_api.@minecraft/server-editor-bindings.widgetgroup.deletewidget.widgettodelete.description


////

//// define
返回值：`void`

- script_api.@minecraft/server-editor-bindings.widgetgroup.deletewidget.return


////

///


/// define
`deselectAllWidgets`


///

script_api.@minecraft/server-editor-bindings.widgetgroup.deselectallwidgets.description

```js
deselectAllWidgets(): void
```

/// html | div.result
//// define
返回值：`void`

- script_api.@minecraft/server-editor-bindings.widgetgroup.deselectallwidgets.return


////

///


/// define
`getIsVisible`


///

script_api.@minecraft/server-editor-bindings.widgetgroup.getisvisible.description

```js
getIsVisible(): boolean
```

/// html | div.result
//// define
返回值：`boolean`

- script_api.@minecraft/server-editor-bindings.widgetgroup.getisvisible.return


////

///


/// define
`moveSelectedWidgets`


///

script_api.@minecraft/server-editor-bindings.widgetgroup.moveselectedwidgets.description

```js
moveSelectedWidgets(delta: Vector3): void
```

/// html | div.result
//// define
`delta`：[`Vector3`](../../server/beta/vector3.md)

- script_api.@minecraft/server-editor-bindings.widgetgroup.moveselectedwidgets.delta.description


////

//// define
返回值：`void`

- script_api.@minecraft/server-editor-bindings.widgetgroup.moveselectedwidgets.return


////

///


/// define
`selectAllWidgets`


///

script_api.@minecraft/server-editor-bindings.widgetgroup.selectallwidgets.description

```js
selectAllWidgets(): void
```

/// html | div.result
//// define
返回值：`void`

- script_api.@minecraft/server-editor-bindings.widgetgroup.selectallwidgets.return


////

///


/// define
`setIsVisible`


///

script_api.@minecraft/server-editor-bindings.widgetgroup.setisvisible.description

```js
setIsVisible(isVisible: boolean): void
```

/// html | div.result
//// define
`isVisible`：`boolean`

- script_api.@minecraft/server-editor-bindings.widgetgroup.setisvisible.isvisible.description


////

//// define
返回值：`void`

- script_api.@minecraft/server-editor-bindings.widgetgroup.setisvisible.return


////

///

