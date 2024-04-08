# `EntityEquippableComponent`

> 文档版本：1.21.0.20

`EntityEquippableComponent`类，扩展自`EntityComponent`。

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


/// define
`getEquipmentSlot`


///

```js
getEquipmentSlot(equipmentSlot: EquipmentSlot): ContainerSlot
```


/// define
`setEquipment`


///

```js
setEquipment(equipmentSlot: EquipmentSlot, itemStack?: ItemStack): boolean
```

