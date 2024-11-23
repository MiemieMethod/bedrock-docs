# `DataStoreModalToolContainer`

> 文档版本：1.21.60.21

`DataStoreModalToolContainer`类。script_api.@minecraft/server-editor-bindings.datastoremodaltoolcontainer.description

## 属性

/// define
`toolActivationChanged`


///

```js
read-only toolActivationChanged: DataStoreModalToolActivationChangedEventSignal;
```

/// html | div.result
//// define
`toolActivationChanged`：[`DataStoreModalToolActivationChangedEventSignal`](./datastoremodaltoolactivationchangedeventsignal.md)

- script_api.@minecraft/server-editor-bindings.datastoremodaltoolcontainer.toolactivationchanged.description


////

///


## 方法

/// define
`getSelectedTool`


///

script_api.@minecraft/server-editor-bindings.datastoremodaltoolcontainer.getselectedtool.description

```js
getSelectedTool(): string | undefined
```

/// html | div.result
//// define
返回值：`string`|`undefined`

- script_api.@minecraft/server-editor-bindings.datastoremodaltoolcontainer.getselectedtool.return


////

///


/// define
`getToolPayload`


///

script_api.@minecraft/server-editor-bindings.datastoremodaltoolcontainer.gettoolpayload.description

```js
getToolPayload(id: string): string
```

/// html | div.result
//// define
`id`：`string`

- script_api.@minecraft/server-editor-bindings.datastoremodaltoolcontainer.gettoolpayload.id.description


////

//// define
返回值：`string`

- script_api.@minecraft/server-editor-bindings.datastoremodaltoolcontainer.gettoolpayload.return


////

///


/// define
`getToolProperty`


///

script_api.@minecraft/server-editor-bindings.datastoremodaltoolcontainer.gettoolproperty.description

```js
getToolProperty(id: string, property: string): boolean | float | string | undefined
```

/// html | div.result
//// define
`id`：`string`

- script_api.@minecraft/server-editor-bindings.datastoremodaltoolcontainer.gettoolproperty.id.description


////

//// define
`property`：`string`

- script_api.@minecraft/server-editor-bindings.datastoremodaltoolcontainer.gettoolproperty.property.description


////

//// define
返回值：`boolean`|`float`|`string`|`undefined`

- script_api.@minecraft/server-editor-bindings.datastoremodaltoolcontainer.gettoolproperty.return


////

///


/// define
`hasToolPayload`


///

script_api.@minecraft/server-editor-bindings.datastoremodaltoolcontainer.hastoolpayload.description

```js
hasToolPayload(id: string): boolean
```

/// html | div.result
//// define
`id`：`string`

- script_api.@minecraft/server-editor-bindings.datastoremodaltoolcontainer.hastoolpayload.id.description


////

//// define
返回值：`boolean`

- script_api.@minecraft/server-editor-bindings.datastoremodaltoolcontainer.hastoolpayload.return


////

///


/// define
`hasToolProperty`


///

script_api.@minecraft/server-editor-bindings.datastoremodaltoolcontainer.hastoolproperty.description

```js
hasToolProperty(id: string, property: string): boolean
```

/// html | div.result
//// define
`id`：`string`

- script_api.@minecraft/server-editor-bindings.datastoremodaltoolcontainer.hastoolproperty.id.description


////

//// define
`property`：`string`

- script_api.@minecraft/server-editor-bindings.datastoremodaltoolcontainer.hastoolproperty.property.description


////

//// define
返回值：`boolean`

- script_api.@minecraft/server-editor-bindings.datastoremodaltoolcontainer.hastoolproperty.return


////

///


/// define
`registerTool`


///

script_api.@minecraft/server-editor-bindings.datastoremodaltoolcontainer.registertool.description

```js
registerTool(id: string, payload: string): void
```

/// html | div.result
//// define
`id`：`string`

- script_api.@minecraft/server-editor-bindings.datastoremodaltoolcontainer.registertool.id.description


////

//// define
`payload`：`string`

- script_api.@minecraft/server-editor-bindings.datastoremodaltoolcontainer.registertool.payload.description


////

//// define
返回值：`void`

- script_api.@minecraft/server-editor-bindings.datastoremodaltoolcontainer.registertool.return


////

///


/// define
`unregisterTool`


///

script_api.@minecraft/server-editor-bindings.datastoremodaltoolcontainer.unregistertool.description

```js
unregisterTool(id: string): void
```

/// html | div.result
//// define
`id`：`string`

- script_api.@minecraft/server-editor-bindings.datastoremodaltoolcontainer.unregistertool.id.description


////

//// define
返回值：`void`

- script_api.@minecraft/server-editor-bindings.datastoremodaltoolcontainer.unregistertool.return


////

///


/// define
`updateRegisteredTool`


///

script_api.@minecraft/server-editor-bindings.datastoremodaltoolcontainer.updateregisteredtool.description

```js
updateRegisteredTool(id: string, payload: string): void
```

/// html | div.result
//// define
`id`：`string`

- script_api.@minecraft/server-editor-bindings.datastoremodaltoolcontainer.updateregisteredtool.id.description


////

//// define
`payload`：`string`

- script_api.@minecraft/server-editor-bindings.datastoremodaltoolcontainer.updateregisteredtool.payload.description


////

//// define
返回值：`void`

- script_api.@minecraft/server-editor-bindings.datastoremodaltoolcontainer.updateregisteredtool.return


////

///


/// define
`updateRegisteredToolProperty`


///

script_api.@minecraft/server-editor-bindings.datastoremodaltoolcontainer.updateregisteredtoolproperty.description

```js
updateRegisteredToolProperty(id: string, payload: string, property: string): void
```

/// html | div.result
//// define
`id`：`string`

- script_api.@minecraft/server-editor-bindings.datastoremodaltoolcontainer.updateregisteredtoolproperty.id.description


////

//// define
`payload`：`string`

- script_api.@minecraft/server-editor-bindings.datastoremodaltoolcontainer.updateregisteredtoolproperty.payload.description


////

//// define
`property`：`string`

- script_api.@minecraft/server-editor-bindings.datastoremodaltoolcontainer.updateregisteredtoolproperty.property.description


////

//// define
返回值：`void`

- script_api.@minecraft/server-editor-bindings.datastoremodaltoolcontainer.updateregisteredtoolproperty.return


////

///


/// define
`updateSelectedTool`


///

script_api.@minecraft/server-editor-bindings.datastoremodaltoolcontainer.updateselectedtool.description

```js
updateSelectedTool(toolId?: string): void
```

/// html | div.result
//// define
`toolId`?：`string`＝`null`

- script_api.@minecraft/server-editor-bindings.datastoremodaltoolcontainer.updateselectedtool.toolid.description


////

//// define
返回值：`void`

- script_api.@minecraft/server-editor-bindings.datastoremodaltoolcontainer.updateselectedtool.return


////

///

