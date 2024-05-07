# `EntityEquippableComponent`

> 文档版本：1.21.0.24

`EntityEquippableComponent`类，扩展自[`EntityComponent`](./entitycomponent.md)。script_api.@minecraft/server.entityequippablecomponent.description

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

script_api.@minecraft/server.entityequippablecomponent.getequipment.description

```js
getEquipment(equipmentSlot: EquipmentSlot): ItemStack | undefined
```

/// html | div.result
//// define
`equipmentSlot`：[`EquipmentSlot`](./equipmentslot.md)

- script_api.@minecraft/server.entityequippablecomponent.getequipment.equipmentslot.description


////

//// define
返回值：[`ItemStack`](./itemstack.md)|`undefined`

- script_api.@minecraft/server.entityequippablecomponent.getequipment.return


////

///


/// define
`getEquipmentSlot`


///

script_api.@minecraft/server.entityequippablecomponent.getequipmentslot.description

```js
getEquipmentSlot(equipmentSlot: EquipmentSlot): ContainerSlot
```

/// html | div.result
//// define
`equipmentSlot`：[`EquipmentSlot`](./equipmentslot.md)

- script_api.@minecraft/server.entityequippablecomponent.getequipmentslot.equipmentslot.description


////

//// define
返回值：[`ContainerSlot`](./containerslot.md)

- script_api.@minecraft/server.entityequippablecomponent.getequipmentslot.return


////

///


/// define
`setEquipment`


///

script_api.@minecraft/server.entityequippablecomponent.setequipment.description

```js
setEquipment(equipmentSlot: EquipmentSlot, itemStack?: ItemStack): boolean
```

/// html | div.result
//// define
`equipmentSlot`：[`EquipmentSlot`](./equipmentslot.md)

- script_api.@minecraft/server.entityequippablecomponent.setequipment.equipmentslot.description


////

//// define
`itemStack`?：[`ItemStack`](./itemstack.md)＝`null`

- script_api.@minecraft/server.entityequippablecomponent.setequipment.itemstack.description


////

//// define
返回值：`boolean`

- script_api.@minecraft/server.entityequippablecomponent.setequipment.return


////

///

