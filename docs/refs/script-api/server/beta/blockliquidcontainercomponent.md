# `BlockLiquidContainerComponent`

> 文档版本：1.21.0.21

`BlockLiquidContainerComponent`类，扩展自[`BlockComponent`](./blockcomponent.md)。液体容器方块的液体容器基组件。

## 属性

/// define
`fillLevel`


///

```js
fillLevel: int32;
```

/// html | div.result
//// define
`fillLevel`：`int32`

- 该液体容器当前的相对装填等级。


////

///


## 方法

/// define
`isValidLiquid`


///

检查该液体容器是否有效且装填内容与引用类型相同。

```js
isValidLiquid(): boolean
```

/// html | div.result
//// define
返回值：`boolean`

- 如果该液体容器有效且装填内容与引用类型相同，返回`true`(例如，一个方块未被加载，或它不再是一个液体容器方块，又或是装填有熔岩但目前引用的是药水容器组件，都不会返回`true`)。


////

///

