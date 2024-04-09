# `EntityEquippableComponent`

> 文档版本：1.21.0.20

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

- script_api.@minecraft/server.entityequippablecomponent.equipmentslot.getequipment.description


////

//// define
返回值：[`ItemStack`](./itemstack.md)|`undefined`

- script_api.@minecraft/server.entityequippablecomponent.getequipment.return


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

- script_api.@minecraft/server.entityequippablecomponent.equipmentslot.setequipment.description


////

//// define
`itemStack`：[`ItemStack`](./itemstack.md)|`undefined`

- script_api.@minecraft/server.entityequippablecomponent.itemstack.setequipment.description


////

//// define
返回值：`boolean`

- script_api.@minecraft/server.entityequippablecomponent.setequipment.return


////

///

