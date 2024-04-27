# `BlockComponentRegistry`

> 文档版本：1.21.0.21

`BlockComponentRegistry`类。用于提供方块数据驱动自定义组件注册功能。

## 方法

/// define
`registerCustomComponent`


///

注册一个自定义方块组件。

```js
registerCustomComponent(name: string, customComponent: BlockCustomComponent): void
```

/// html | div.result
//// define
`name`：`string`

- 要注册的自定义组件的名称（必须带有命名空间）。


////

//// define
`customComponent`：[`BlockCustomComponent`](./blockcustomcomponent.md)

- 该组件绑定事件的集合。


////

//// define
返回值：`void`

- script_api.@minecraft/server.blockcomponentregistry.registercustomcomponent.return


////

///

