# `WidgetGroup`

> 文档版本：1.21.60.21

`WidgetGroup`类。script_api.@minecraft/server-editor-bindings.widgetgroup.description

## 属性

/// define
`selectedWidgetCount`


///

```js
read-only selectedWidgetCount: int32;
```

/// html | div.result
//// define
`selectedWidgetCount`：`int32`

- script_api.@minecraft/server-editor-bindings.widgetgroup.selectedwidgetcount.description


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

- script_api.@minecraft/server-editor-bindings.widgetgroup.visible.description


////

///


/// define
`visibleBounds`


///

```js
visibleBounds: boolean;
```

/// html | div.result
//// define
`visibleBounds`：`boolean`

- script_api.@minecraft/server-editor-bindings.widgetgroup.visiblebounds.description


////

///


## 方法

/// define
`createWidget`


///

script_api.@minecraft/server-editor-bindings.widgetgroup.createwidget.description

```js
createWidget(location: Vector3, options?: WidgetCreateOptions): Widget
```

/// html | div.result
//// define
`location`：[`Vector3`](../../server/beta/vector3.md)

- script_api.@minecraft/server-editor-bindings.widgetgroup.createwidget.location.description


////

//// define
`options`?：[`WidgetCreateOptions`](./widgetcreateoptions.md)＝`null`

- script_api.@minecraft/server-editor-bindings.widgetgroup.createwidget.options.description


////

//// define
返回值：[`Widget`](./widget.md)

- script_api.@minecraft/server-editor-bindings.widgetgroup.createwidget.return


////

///


/// define
`delete`


///

script_api.@minecraft/server-editor-bindings.widgetgroup.delete.description

```js
delete(): void
```

/// html | div.result
//// define
返回值：`void`

- script_api.@minecraft/server-editor-bindings.widgetgroup.delete.return


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

