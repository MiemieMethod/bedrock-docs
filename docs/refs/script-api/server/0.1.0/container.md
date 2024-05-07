# `Container`

> 文档版本：1.21.0.24

`Container`类。script_api.mojang-minecraft.container.description

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

- script_api.mojang-minecraft.container.emptyslotscount.description


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

- script_api.mojang-minecraft.container.size.description


////

///


## 方法

/// define
`addItem`


///

script_api.mojang-minecraft.container.additem.description

```js
addItem(itemStack: ItemStack): void
```

/// html | div.result
//// define
`itemStack`：[`ItemStack`](./itemstack.md)

- script_api.mojang-minecraft.container.additem.itemstack.description


////

//// define
返回值：`void`

- script_api.mojang-minecraft.container.additem.return


////

///


/// define
`getItem`


///

script_api.mojang-minecraft.container.getitem.description

```js
getItem(slot: int32): ItemStack | undefined
```

/// html | div.result
//// define
`slot`：`int32`

- script_api.mojang-minecraft.container.getitem.slot.description


////

//// define
返回值：[`ItemStack`](./itemstack.md)|`undefined`

- script_api.mojang-minecraft.container.getitem.return


////

///


/// define
`setItem`


///

script_api.mojang-minecraft.container.setitem.description

```js
setItem(slot: int32, itemStack: ItemStack): void
```

/// html | div.result
//// define
`slot`：`int32`

- script_api.mojang-minecraft.container.setitem.slot.description


////

//// define
`itemStack`：[`ItemStack`](./itemstack.md)

- script_api.mojang-minecraft.container.setitem.itemstack.description


////

//// define
返回值：`void`

- script_api.mojang-minecraft.container.setitem.return


////

///


/// define
`swapItems`


///

script_api.mojang-minecraft.container.swapitems.description

```js
swapItems(slot: int32, otherSlot: int32, otherContainer: Container): boolean
```

/// html | div.result
//// define
`slot`：`int32`

- script_api.mojang-minecraft.container.swapitems.slot.description


////

//// define
`otherSlot`：`int32`

- script_api.mojang-minecraft.container.swapitems.otherslot.description


////

//// define
`otherContainer`：[`Container`](./container.md)

- script_api.mojang-minecraft.container.swapitems.othercontainer.description


////

//// define
返回值：`boolean`

- script_api.mojang-minecraft.container.swapitems.return


////

///


/// define
`transferItem`


///

script_api.mojang-minecraft.container.transferitem.description

```js
transferItem(fromSlot: int32, toSlot: int32, toContainer: Container): boolean
```

/// html | div.result
//// define
`fromSlot`：`int32`

- script_api.mojang-minecraft.container.transferitem.fromslot.description


////

//// define
`toSlot`：`int32`

- script_api.mojang-minecraft.container.transferitem.toslot.description


////

//// define
`toContainer`：[`Container`](./container.md)

- script_api.mojang-minecraft.container.transferitem.tocontainer.description


////

//// define
返回值：`boolean`

- script_api.mojang-minecraft.container.transferitem.return


////

///

