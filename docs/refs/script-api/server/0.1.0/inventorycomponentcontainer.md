# `InventoryComponentContainer`

> 文档版本：1.21.0.20

`InventoryComponentContainer`类。

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

- 属性。


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

- 属性。


////

///


## 方法

/// define
`addItem`


///

```js
addItem(itemStack: ItemStack): void
```

/// html | div.result
//// define
`itemStack`：[`ItemStack`](./itemstack.md)

- 参数1。


////

//// define
返回值：`void`

- 返回值。


////

///


/// define
`getItem`


///

```js
getItem(slot: int32): ItemStack | undefined
```

/// html | div.result
//// define
`slot`：`int32`

- 参数1。


////

//// define
返回值：[`ItemStack`](./itemstack.md)|`undefined`

- 返回值。


////

///


/// define
`setItem`


///

```js
setItem(slot: int32, itemStack: ItemStack): void
```

/// html | div.result
//// define
`slot`：`int32`

- 参数1。


////

//// define
`itemStack`：[`ItemStack`](./itemstack.md)

- 参数2。


////

//// define
返回值：`void`

- 返回值。


////

///


/// define
`swapItems`


///

```js
swapItems(slot: int32, otherSlot: int32, otherContainer: Container): boolean
```

/// html | div.result
//// define
`slot`：`int32`

- 参数1。


////

//// define
`otherSlot`：`int32`

- 参数2。


////

//// define
`otherContainer`：[`Container`](./container.md)

- 参数3。


////

//// define
返回值：`boolean`

- 返回值。


////

///


/// define
`transferItem`


///

```js
transferItem(fromSlot: int32, toSlot: int32, toContainer: Container): boolean
```

/// html | div.result
//// define
`fromSlot`：`int32`

- 参数1。


////

//// define
`toSlot`：`int32`

- 参数2。


////

//// define
`toContainer`：[`Container`](./container.md)

- 参数3。


////

//// define
返回值：`boolean`

- 返回值。


////

///

