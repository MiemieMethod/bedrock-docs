# `BlockFluidContainerComponent`

> 文档版本：1.21.60.21

`BlockFluidContainerComponent`类，扩展自[`BlockComponent`](./blockcomponent.md)。script_api.@minecraft/server.blockfluidcontainercomponent.description

## 常量

/// define
`componentId`


///

```js
static read-only componentId = "minecraft:fluidContainer";
```


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

- script_api.@minecraft/server.blockfluidcontainercomponent.filllevel.description


////

///


/// define
`fluidColor`


///

```js
fluidColor: RGBA;
```

/// html | div.result
//// define
`fluidColor`：[`RGBA`](./rgba.md)

- script_api.@minecraft/server.blockfluidcontainercomponent.fluidcolor.description


////

///


## 方法

/// define
`addDye`


///

script_api.@minecraft/server.blockfluidcontainercomponent.adddye.description

```js
addDye(dye: ItemType): void
```

/// html | div.result
//// define
`dye`：[`ItemType`](./itemtype.md)

- script_api.@minecraft/server.blockfluidcontainercomponent.adddye.dye.description


////

//// define
返回值：`void`

- script_api.@minecraft/server.blockfluidcontainercomponent.adddye.return


////

///


/// define
`getFluidType`


///

script_api.@minecraft/server.blockfluidcontainercomponent.getfluidtype.description

```js
getFluidType(): FluidType
```

/// html | div.result
//// define
返回值：[`FluidType`](./fluidtype.md)

- script_api.@minecraft/server.blockfluidcontainercomponent.getfluidtype.return


////

///


/// define
`setFluidType`


///

script_api.@minecraft/server.blockfluidcontainercomponent.setfluidtype.description

```js
setFluidType(fluidType: FluidType): void
```

/// html | div.result
//// define
`fluidType`：[`FluidType`](./fluidtype.md)

- script_api.@minecraft/server.blockfluidcontainercomponent.setfluidtype.fluidtype.description


////

//// define
返回值：`void`

- script_api.@minecraft/server.blockfluidcontainercomponent.setfluidtype.return


////

///


/// define
`setPotion`


///

script_api.@minecraft/server.blockfluidcontainercomponent.setpotion.description

```js
setPotion(itemStack: ItemStack): void
```

/// html | div.result
//// define
`itemStack`：[`ItemStack`](./itemstack.md)

- script_api.@minecraft/server.blockfluidcontainercomponent.setpotion.itemstack.description


////

//// define
返回值：`void`

- script_api.@minecraft/server.blockfluidcontainercomponent.setpotion.return


////

///

