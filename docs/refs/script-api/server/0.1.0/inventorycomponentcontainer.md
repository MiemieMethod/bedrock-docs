# `InventoryComponentContainer`

> 文档版本：1.21.0.24

`InventoryComponentContainer`类。script_api.mojang-minecraft.inventorycomponentcontainer.description

## 属性

/// define
`emptySlotsCount`


///

```js
read-only emptySlotsCount: int32;
```

/// html | div.result
//// define
`emptySlotsCount`：`int32`

- script_api.mojang-minecraft.inventorycomponentcontainer.emptyslotscount.description


////

///


/// define
`size`


///

```js
read-only size: int32;
```

/// html | div.result
//// define
`size`：`int32`

- script_api.mojang-minecraft.inventorycomponentcontainer.size.description


////

///


## 方法

/// define
`addItem`


///

script_api.mojang-minecraft.inventorycomponentcontainer.additem.description

```js
addItem(itemStack: ItemStack): void
```

/// html | div.result
//// define
`itemStack`：[`ItemStack`](./itemstack.md)

- script_api.mojang-minecraft.inventorycomponentcontainer.additem.itemstack.description


////

//// define
返回值：`void`

- script_api.mojang-minecraft.inventorycomponentcontainer.additem.return


////

///


/// define
`getItem`


///

script_api.mojang-minecraft.inventorycomponentcontainer.getitem.description

```js
getItem(slot: int32): ItemStack | undefined
```

/// html | div.result
//// define
`slot`：`int32`

- script_api.mojang-minecraft.inventorycomponentcontainer.getitem.slot.description


////

//// define
返回值：[`ItemStack`](./itemstack.md)|`undefined`

- script_api.mojang-minecraft.inventorycomponentcontainer.getitem.return


////

///


/// define
`setItem`


///

script_api.mojang-minecraft.inventorycomponentcontainer.setitem.description

```js
setItem(slot: int32, itemStack: ItemStack): void
```

/// html | div.result
//// define
`slot`：`int32`

- script_api.mojang-minecraft.inventorycomponentcontainer.setitem.slot.description


////

//// define
`itemStack`：[`ItemStack`](./itemstack.md)

- script_api.mojang-minecraft.inventorycomponentcontainer.setitem.itemstack.description


////

//// define
返回值：`void`

- script_api.mojang-minecraft.inventorycomponentcontainer.setitem.return


////

///


/// define
`swapItems`


///

script_api.mojang-minecraft.inventorycomponentcontainer.swapitems.description

```js
swapItems(slot: int32, otherSlot: int32, otherContainer: Container): boolean
```

/// html | div.result
//// define
`slot`：`int32`

- script_api.mojang-minecraft.inventorycomponentcontainer.swapitems.slot.description


////

//// define
`otherSlot`：`int32`

- script_api.mojang-minecraft.inventorycomponentcontainer.swapitems.otherslot.description


////

//// define
`otherContainer`：[`Container`](./container.md)

- script_api.mojang-minecraft.inventorycomponentcontainer.swapitems.othercontainer.description


////

//// define
返回值：`boolean`

- script_api.mojang-minecraft.inventorycomponentcontainer.swapitems.return


////

///


/// define
`transferItem`


///

script_api.mojang-minecraft.inventorycomponentcontainer.transferitem.description

```js
transferItem(fromSlot: int32, toSlot: int32, toContainer: Container): boolean
```

/// html | div.result
//// define
`fromSlot`：`int32`

- script_api.mojang-minecraft.inventorycomponentcontainer.transferitem.fromslot.description


////

//// define
`toSlot`：`int32`

- script_api.mojang-minecraft.inventorycomponentcontainer.transferitem.toslot.description


////

//// define
`toContainer`：[`Container`](./container.md)

- script_api.mojang-minecraft.inventorycomponentcontainer.transferitem.tocontainer.description


////

//// define
返回值：`boolean`

- script_api.mojang-minecraft.inventorycomponentcontainer.transferitem.return


////

///

