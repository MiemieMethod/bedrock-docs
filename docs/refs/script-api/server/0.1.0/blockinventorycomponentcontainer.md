# `BlockInventoryComponentContainer`

> 文档版本：1.21.0.20

`BlockInventoryComponentContainer`类。script_api.mojang-minecraft.blockinventorycomponentcontainer.description

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

- script_api.mojang-minecraft.blockinventorycomponentcontainer.emptyslotscount.description


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

- script_api.mojang-minecraft.blockinventorycomponentcontainer.size.description


////

///


## 方法

/// define
`addItem`


///

script_api.mojang-minecraft.blockinventorycomponentcontainer.additem.description

```js
addItem(itemStack: ItemStack): void
```

/// html | div.result
//// define
`itemStack`：[`ItemStack`](./itemstack.md)

- script_api.mojang-minecraft.blockinventorycomponentcontainer.additem.itemstack.description


////

//// define
返回值：`void`

- script_api.mojang-minecraft.blockinventorycomponentcontainer.additem.return


////

///


/// define
`getItem`


///

script_api.mojang-minecraft.blockinventorycomponentcontainer.getitem.description

```js
getItem(slot: int32): ItemStack | undefined
```

/// html | div.result
//// define
`slot`：`int32`

- script_api.mojang-minecraft.blockinventorycomponentcontainer.getitem.slot.description


////

//// define
返回值：[`ItemStack`](./itemstack.md)|`undefined`

- script_api.mojang-minecraft.blockinventorycomponentcontainer.getitem.return


////

///


/// define
`setItem`


///

script_api.mojang-minecraft.blockinventorycomponentcontainer.setitem.description

```js
setItem(slot: int32, itemStack: ItemStack): void
```

/// html | div.result
//// define
`slot`：`int32`

- script_api.mojang-minecraft.blockinventorycomponentcontainer.setitem.slot.description


////

//// define
`itemStack`：[`ItemStack`](./itemstack.md)

- script_api.mojang-minecraft.blockinventorycomponentcontainer.setitem.itemstack.description


////

//// define
返回值：`void`

- script_api.mojang-minecraft.blockinventorycomponentcontainer.setitem.return


////

///


/// define
`swapItems`


///

script_api.mojang-minecraft.blockinventorycomponentcontainer.swapitems.description

```js
swapItems(slot: int32, otherSlot: int32, otherContainer: Container): boolean
```

/// html | div.result
//// define
`slot`：`int32`

- script_api.mojang-minecraft.blockinventorycomponentcontainer.swapitems.slot.description


////

//// define
`otherSlot`：`int32`

- script_api.mojang-minecraft.blockinventorycomponentcontainer.swapitems.otherslot.description


////

//// define
`otherContainer`：[`Container`](./container.md)

- script_api.mojang-minecraft.blockinventorycomponentcontainer.swapitems.othercontainer.description


////

//// define
返回值：`boolean`

- script_api.mojang-minecraft.blockinventorycomponentcontainer.swapitems.return


////

///


/// define
`transferItem`


///

script_api.mojang-minecraft.blockinventorycomponentcontainer.transferitem.description

```js
transferItem(fromSlot: int32, toSlot: int32, toContainer: Container): boolean
```

/// html | div.result
//// define
`fromSlot`：`int32`

- script_api.mojang-minecraft.blockinventorycomponentcontainer.transferitem.fromslot.description


////

//// define
`toSlot`：`int32`

- script_api.mojang-minecraft.blockinventorycomponentcontainer.transferitem.toslot.description


////

//// define
`toContainer`：[`Container`](./container.md)

- script_api.mojang-minecraft.blockinventorycomponentcontainer.transferitem.tocontainer.description


////

//// define
返回值：`boolean`

- script_api.mojang-minecraft.blockinventorycomponentcontainer.transferitem.return


////

///

