# `EntityEquippableComponent`

> 文档版本：1.21.0.20

`EntityEquippableComponent`类，扩展自[`EntityComponent`](./entitycomponent.md)。

## 常量

/// define
`componentId`


///

```js
static read-only componentId = "minecraft:equippable";
```


## 方法

/// define
`getEquipment`


///

```js
getEquipment(equipmentSlot: EquipmentSlot): ItemStack | undefined
```

/// html | div.result
//// define
`equipmentSlot`：[`EquipmentSlot`](./equipmentslot.md)

- 参数1。


////

//// define
返回值：[`ItemStack`](./itemstack.md)|`undefined`

- 返回值。


////

///


/// define
`getEquipmentSlot`


///

```js
getEquipmentSlot(equipmentSlot: EquipmentSlot): ContainerSlot
```

/// html | div.result
//// define
`equipmentSlot`：[`EquipmentSlot`](./equipmentslot.md)

- 参数1。


////

//// define
返回值：[`ContainerSlot`](./containerslot.md)

- 返回值。


////

///


/// define
`setEquipment`


///

```js
setEquipment(equipmentSlot: EquipmentSlot, itemStack?: ItemStack): boolean
```

/// html | div.result
//// define
`equipmentSlot`：[`EquipmentSlot`](./equipmentslot.md)

- 参数1。


////

//// define
`itemStack`：[`ItemStack`](./itemstack.md)|`undefined`

- 参数2。


////

//// define
返回值：`boolean`

- 返回值。


////

///

