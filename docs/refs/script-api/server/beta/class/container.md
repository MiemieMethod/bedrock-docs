# `Container`

> 文档版本：1.21.0.20

`Container`类。

## 属性

/// define
emptySlotsCount

- ```js
read-only emptySlotsCount: int32
```



///


/// define
size

- ```js
read-only size: int32
```



///


## 方法

/// define
addItem

- ```js
addItem(itemStack: ItemStack): ItemStack | undefined
```



///


/// define
clearAll

- ```js
clearAll(): void
```



///


/// define
getItem

- ```js
getItem(slot: int32): ItemStack | undefined
```



///


/// define
getSlot

- ```js
getSlot(slot: int32): ContainerSlot
```



///


/// define
isValid

- ```js
isValid(): boolean
```



///


/// define
moveItem

- ```js
moveItem(fromSlot: int32, toSlot: int32, toContainer: Container): void
```



///


/// define
setItem

- ```js
setItem(slot: int32, itemStack?: ItemStack): void
```



///


/// define
swapItems

- ```js
swapItems(slot: int32, otherSlot: int32, otherContainer: Container): void
```



///


/// define
transferItem

- ```js
transferItem(fromSlot: int32, toContainer: Container): ItemStack | undefined
```



///

