# `Container`

> 文档版本：1.21.60.21

`Container`类。script_api.@minecraft/server.container.description

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

- script_api.@minecraft/server.container.emptyslotscount.description


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

- script_api.@minecraft/server.container.size.description


////

///


## 方法

/// define
`addItem`


///

script_api.@minecraft/server.container.additem.description

```js
addItem(itemStack: ItemStack): ItemStack | undefined
```

/// html | div.result
//// define
`itemStack`：[`ItemStack`](./itemstack.md)

- script_api.@minecraft/server.container.additem.itemstack.description


////

//// define
返回值：[`ItemStack`](./itemstack.md)|`undefined`

- script_api.@minecraft/server.container.additem.return


////

///


/// define
`clearAll`


///

script_api.@minecraft/server.container.clearall.description

```js
clearAll(): void
```

/// html | div.result
//// define
返回值：`void`

- script_api.@minecraft/server.container.clearall.return


////

///


/// define
`getItem`


///

script_api.@minecraft/server.container.getitem.description

```js
getItem(slot: int32): ItemStack | undefined
```

/// html | div.result
//// define
`slot`：`int32`

- script_api.@minecraft/server.container.getitem.slot.description


////

//// define
返回值：[`ItemStack`](./itemstack.md)|`undefined`

- script_api.@minecraft/server.container.getitem.return


////

///


/// define
`moveItem`


///

script_api.@minecraft/server.container.moveitem.description

```js
moveItem(fromSlot: int32, toSlot: int32, toContainer: Container): void
```

/// html | div.result
//// define
`fromSlot`：`int32`

- script_api.@minecraft/server.container.moveitem.fromslot.description


////

//// define
`toSlot`：`int32`

- script_api.@minecraft/server.container.moveitem.toslot.description


////

//// define
`toContainer`：[`Container`](./container.md)

- script_api.@minecraft/server.container.moveitem.tocontainer.description


////

//// define
返回值：`void`

- script_api.@minecraft/server.container.moveitem.return


////

///


/// define
`setItem`


///

script_api.@minecraft/server.container.setitem.description

```js
setItem(slot: int32, itemStack?: ItemStack): void
```

/// html | div.result
//// define
`slot`：`int32`

- script_api.@minecraft/server.container.setitem.slot.description


////

//// define
`itemStack`?：[`ItemStack`](./itemstack.md)＝`null`

- script_api.@minecraft/server.container.setitem.itemstack.description


////

//// define
返回值：`void`

- script_api.@minecraft/server.container.setitem.return


////

///


/// define
`swapItems`


///

script_api.@minecraft/server.container.swapitems.description

```js
swapItems(slot: int32, otherSlot: int32, otherContainer: Container): void
```

/// html | div.result
//// define
`slot`：`int32`

- script_api.@minecraft/server.container.swapitems.slot.description


////

//// define
`otherSlot`：`int32`

- script_api.@minecraft/server.container.swapitems.otherslot.description


////

//// define
`otherContainer`：[`Container`](./container.md)

- script_api.@minecraft/server.container.swapitems.othercontainer.description


////

//// define
返回值：`void`

- script_api.@minecraft/server.container.swapitems.return


////

///


/// define
`transferItem`


///

script_api.@minecraft/server.container.transferitem.description

```js
transferItem(fromSlot: int32, toContainer: Container): ItemStack | undefined
```

/// html | div.result
//// define
`fromSlot`：`int32`

- script_api.@minecraft/server.container.transferitem.fromslot.description


////

//// define
`toContainer`：[`Container`](./container.md)

- script_api.@minecraft/server.container.transferitem.tocontainer.description


////

//// define
返回值：[`ItemStack`](./itemstack.md)|`undefined`

- script_api.@minecraft/server.container.transferitem.return


////

///

