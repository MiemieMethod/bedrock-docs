# `InventoryComponentContainer`

> 文档版本：1.21.0.20

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

- script_api.mojang-minecraft.inventorycomponentcontainer.itemstack.additem.description


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

- script_api.mojang-minecraft.inventorycomponentcontainer.slot.getitem.description


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

- script_api.mojang-minecraft.inventorycomponentcontainer.slot.setitem.description


////

//// define
`itemStack`：[`ItemStack`](./itemstack.md)

- script_api.mojang-minecraft.inventorycomponentcontainer.itemstack.setitem.description


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

- script_api.mojang-minecraft.inventorycomponentcontainer.slot.swapitems.description


////

//// define
`otherSlot`：`int32`

- script_api.mojang-minecraft.inventorycomponentcontainer.otherslot.swapitems.description


////

//// define
`otherContainer`：[`Container`](./container.md)

- script_api.mojang-minecraft.inventorycomponentcontainer.othercontainer.swapitems.description


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

- script_api.mojang-minecraft.inventorycomponentcontainer.fromslot.transferitem.description


////

//// define
`toSlot`：`int32`

- script_api.mojang-minecraft.inventorycomponentcontainer.toslot.transferitem.description


////

//// define
`toContainer`：[`Container`](./container.md)

- script_api.mojang-minecraft.inventorycomponentcontainer.tocontainer.transferitem.description


////

//// define
返回值：`boolean`

- script_api.mojang-minecraft.inventorycomponentcontainer.transferitem.return


////

///

