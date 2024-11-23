# `InputService`

> 文档版本：1.21.60.21

`InputService`类。script_api.@minecraft/server-editor-bindings.inputservice.description

## 方法

/// define
`focusViewport`


///

script_api.@minecraft/server-editor-bindings.inputservice.focusviewport.description

```js
focusViewport(): void
```

/// html | div.result
//// define
返回值：`void`

- script_api.@minecraft/server-editor-bindings.inputservice.focusviewport.return


////

///


/// define
`registerKeyBinding`


///

script_api.@minecraft/server-editor-bindings.inputservice.registerkeybinding.description

```js
registerKeyBinding(contextId: string, bindingId: string, key: int32, modifier: InputModifier, info: InputBindingInfo): void
```

/// html | div.result
//// define
`contextId`：`string`

- script_api.@minecraft/server-editor-bindings.inputservice.registerkeybinding.contextid.description


////

//// define
`bindingId`：`string`

- script_api.@minecraft/server-editor-bindings.inputservice.registerkeybinding.bindingid.description


////

//// define
`key`：`int32`

- script_api.@minecraft/server-editor-bindings.inputservice.registerkeybinding.key.description


////

//// define
`modifier`：[`InputModifier`](./inputmodifier.md)

- script_api.@minecraft/server-editor-bindings.inputservice.registerkeybinding.modifier.description


////

//// define
`info`：[`InputBindingInfo`](./inputbindinginfo.md)

- script_api.@minecraft/server-editor-bindings.inputservice.registerkeybinding.info.description


////

//// define
返回值：`void`

- script_api.@minecraft/server-editor-bindings.inputservice.registerkeybinding.return


////

///


/// define
`unregisterKeyBinding`


///

script_api.@minecraft/server-editor-bindings.inputservice.unregisterkeybinding.description

```js
unregisterKeyBinding(controlId: string, bindingId: string): void
```

/// html | div.result
//// define
`controlId`：`string`

- script_api.@minecraft/server-editor-bindings.inputservice.unregisterkeybinding.controlid.description


////

//// define
`bindingId`：`string`

- script_api.@minecraft/server-editor-bindings.inputservice.unregisterkeybinding.bindingid.description


////

//// define
返回值：`void`

- script_api.@minecraft/server-editor-bindings.inputservice.unregisterkeybinding.return


////

///

