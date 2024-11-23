# `WidgetComponentSpline`

> 文档版本：1.21.60.21

`WidgetComponentSpline`类，扩展自[`WidgetComponentBase`](./widgetcomponentbase.md)。script_api.@minecraft/server-editor-bindings.widgetcomponentspline.description

## 属性

/// define
`splineType`


///

```js
splineType: SplineType;
```

/// html | div.result
//// define
`splineType`：[`SplineType`](./splinetype.md)

- script_api.@minecraft/server-editor-bindings.widgetcomponentspline.splinetype.description


////

///


## 方法

/// define
`getControlPoints`


///

script_api.@minecraft/server-editor-bindings.widgetcomponentspline.getcontrolpoints.description

```js
getControlPoints(): Widget[]
```

/// html | div.result
//// define
返回值：<code><a href="../widget/">Widget</a>[]</code>

- script_api.@minecraft/server-editor-bindings.widgetcomponentspline.getcontrolpoints.return


////

///


/// define
`getInterpolatedPoints`


///

script_api.@minecraft/server-editor-bindings.widgetcomponentspline.getinterpolatedpoints.description

```js
getInterpolatedPoints(maxPointsPerControlSegment?: int32): Vector3[]
```

/// html | div.result
//// define
`maxPointsPerControlSegment`?：`int32`＝`null`

- script_api.@minecraft/server-editor-bindings.widgetcomponentspline.getinterpolatedpoints.maxpointspercontrolsegment.description


////

//// define
返回值：<code><a href="../../../server/beta/vector3/">Vector3</a>[]</code>

- script_api.@minecraft/server-editor-bindings.widgetcomponentspline.getinterpolatedpoints.return


////

///


/// define
`setControlPoints`


///

script_api.@minecraft/server-editor-bindings.widgetcomponentspline.setcontrolpoints.description

```js
setControlPoints(widgetList: Widget[]): void
```

/// html | div.result
//// define
`widgetList`：<code><a href="../widget/">Widget</a>[]</code>

- script_api.@minecraft/server-editor-bindings.widgetcomponentspline.setcontrolpoints.widgetlist.description


////

//// define
返回值：`void`

- script_api.@minecraft/server-editor-bindings.widgetcomponentspline.setcontrolpoints.return


////

///

