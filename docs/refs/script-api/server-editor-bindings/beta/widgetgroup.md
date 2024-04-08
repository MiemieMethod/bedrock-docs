# `WidgetGroup`

> 文档版本：1.21.0.20

`WidgetGroup`类。

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

- 属性。


////

///


## 方法

/// define
`areAnySelected`


///

```js
areAnySelected(): boolean
```

/// html | div.result
//// define
返回值：`boolean`

- 返回值。


////

///


/// define
`createCustomWidget`


///

```js
createCustomWidget(customEntityName: string, location: Vector3, rotation?: Vector2, options?: CustomWidgetCreateOptions): CustomWidget
```

/// html | div.result
//// define
`customEntityName`：`string`

- 参数1。


////

//// define
`location`：[`Vector3`](../../server/beta/vector3.md)

- 参数2。


////

//// define
`rotation`：[`Vector2`](../../server/beta/vector2.md)|`undefined`

- 参数3。


////

//// define
`options`：[`CustomWidgetCreateOptions`](./customwidgetcreateoptions.md)|`undefined`

- 参数4。


////

//// define
返回值：[`CustomWidget`](./customwidget.md)

- 返回值。


////

///


/// define
`deleteWidget`


///

```js
deleteWidget(widgetToDelete: Widget): void
```

/// html | div.result
//// define
`widgetToDelete`：[`Widget`](./widget.md)

- 参数1。


////

//// define
返回值：`void`

- 返回值。


////

///


/// define
`deselectAllWidgets`


///

```js
deselectAllWidgets(): void
```

/// html | div.result
//// define
返回值：`void`

- 返回值。


////

///


/// define
`getIsVisible`


///

```js
getIsVisible(): boolean
```

/// html | div.result
//// define
返回值：`boolean`

- 返回值。


////

///


/// define
`moveSelectedWidgets`


///

```js
moveSelectedWidgets(delta: Vector3): void
```

/// html | div.result
//// define
`delta`：[`Vector3`](../../server/beta/vector3.md)

- 参数1。


////

//// define
返回值：`void`

- 返回值。


////

///


/// define
`selectAllWidgets`


///

```js
selectAllWidgets(): void
```

/// html | div.result
//// define
返回值：`void`

- 返回值。


////

///


/// define
`setIsVisible`


///

```js
setIsVisible(isVisible: boolean): void
```

/// html | div.result
//// define
`isVisible`：`boolean`

- 参数1。


////

//// define
返回值：`void`

- 返回值。


////

///

