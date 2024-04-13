# `PlayerInventoryComponentContainer`

> 文档版本：1.21.0.21

`PlayerInventoryComponentContainer`类。script_api.mojang-minecraft.playerinventorycomponentcontainer.description

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

- script_api.mojang-minecraft.playerinventorycomponentcontainer.emptyslotscount.description


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

- script_api.mojang-minecraft.playerinventorycomponentcontainer.size.description


////

///


## 方法

/// define
`addItem`


///

script_api.mojang-minecraft.playerinventorycomponentcontainer.additem.description

```js
addItem(itemStack: ItemStack): void
```

/// html | div.result
//// define
`itemStack`：[`ItemStack`](./itemstack.md)

- script_api.mojang-minecraft.playerinventorycomponentcontainer.additem.itemstack.description


////

//// define
返回值：`void`

- script_api.mojang-minecraft.playerinventorycomponentcontainer.additem.return


////

///


/// define
`getItem`


///

script_api.mojang-minecraft.playerinventorycomponentcontainer.getitem.description

```js
getItem(slot: int32): ItemStack | undefined
```

/// html | div.result
//// define
`slot`：`int32`

- script_api.mojang-minecraft.playerinventorycomponentcontainer.getitem.slot.description


////

//// define
返回值：[`ItemStack`](./itemstack.md)|`undefined`

- script_api.mojang-minecraft.playerinventorycomponentcontainer.getitem.return


////

///


/// define
`setItem`


///

script_api.mojang-minecraft.playerinventorycomponentcontainer.setitem.description

```js
setItem(slot: int32, itemStack: ItemStack): void
```

/// html | div.result
//// define
`slot`：`int32`

- script_api.mojang-minecraft.playerinventorycomponentcontainer.setitem.slot.description


////

//// define
`itemStack`：[`ItemStack`](./itemstack.md)

- script_api.mojang-minecraft.playerinventorycomponentcontainer.setitem.itemstack.description


////

//// define
返回值：`void`

- script_api.mojang-minecraft.playerinventorycomponentcontainer.setitem.return


////

///


/// define
`swapItems`


///

script_api.mojang-minecraft.playerinventorycomponentcontainer.swapitems.description

```js
swapItems(slot: int32, otherSlot: int32, otherContainer: Container): boolean
```

/// html | div.result
//// define
`slot`：`int32`

- script_api.mojang-minecraft.playerinventorycomponentcontainer.swapitems.slot.description


////

//// define
`otherSlot`：`int32`

- script_api.mojang-minecraft.playerinventorycomponentcontainer.swapitems.otherslot.description


////

//// define
`otherContainer`：[`Container`](./container.md)

- script_api.mojang-minecraft.playerinventorycomponentcontainer.swapitems.othercontainer.description


////

//// define
返回值：`boolean`

- script_api.mojang-minecraft.playerinventorycomponentcontainer.swapitems.return


////

///


/// define
`transferItem`


///

script_api.mojang-minecraft.playerinventorycomponentcontainer.transferitem.description

```js
transferItem(fromSlot: int32, toSlot: int32, toContainer: Container): boolean
```

/// html | div.result
//// define
`fromSlot`：`int32`

- script_api.mojang-minecraft.playerinventorycomponentcontainer.transferitem.fromslot.description


////

//// define
`toSlot`：`int32`

- script_api.mojang-minecraft.playerinventorycomponentcontainer.transferitem.toslot.description


////

//// define
`toContainer`：[`Container`](./container.md)

- script_api.mojang-minecraft.playerinventorycomponentcontainer.transferitem.tocontainer.description


////

//// define
返回值：`boolean`

- script_api.mojang-minecraft.playerinventorycomponentcontainer.transferitem.return


////

///

