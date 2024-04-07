# `ContainerSlot`

> 文档版本：1.21.0.20

`ContainerSlot`类。

## 属性

/// define
amount

- ```js
amount: int32
```



///


/// define
isStackable

- ```js
read-only isStackable: boolean
```



///


/// define
keepOnDeath

- ```js
keepOnDeath: boolean
```



///


/// define
lockMode

- ```js
lockMode: ItemLockMode
```



///


/// define
maxAmount

- ```js
read-only maxAmount: int32
```



///


/// define
nameTag

- ```js
nameTag: string | undefined
```



///


/// define
type

- ```js
read-only type: ItemType
```



///


/// define
typeId

- ```js
read-only typeId: string
```



///


## 方法

/// define
clearDynamicProperties

- ```js
clearDynamicProperties(): void
```



///


/// define
getCanDestroy

- ```js
getCanDestroy(): string[]
```



///


/// define
getCanPlaceOn

- ```js
getCanPlaceOn(): string[]
```



///


/// define
getDynamicProperty

- ```js
getDynamicProperty(identifier: string): boolean | double | float | string | Vector3 | undefined
```



///


/// define
getDynamicPropertyIds

- ```js
getDynamicPropertyIds(): string[]
```



///


/// define
getDynamicPropertyTotalByteCount

- ```js
getDynamicPropertyTotalByteCount(): int32
```



///


/// define
getItem

- ```js
getItem(): ItemStack | undefined
```



///


/// define
getLore

- ```js
getLore(): string[]
```



///


/// define
getTags

- ```js
getTags(): string[]
```



///


/// define
hasItem

- ```js
hasItem(): boolean
```



///


/// define
hasTag

- ```js
hasTag(tag: string): boolean
```



///


/// define
isStackableWith

- ```js
isStackableWith(itemStack: ItemStack): boolean
```



///


/// define
isValid

- ```js
isValid(): boolean
```



///


/// define
setCanDestroy

- ```js
setCanDestroy(blockIdentifiers?: string[]): void
```



///


/// define
setCanPlaceOn

- ```js
setCanPlaceOn(blockIdentifiers?: string[]): void
```



///


/// define
setDynamicProperty

- ```js
setDynamicProperty(identifier: string, value?: boolean | double | float | string | Vector3): void
```



///


/// define
setItem

- ```js
setItem(itemStack?: ItemStack): void
```



///


/// define
setLore

- ```js
setLore(loreList?: string[]): void
```



///

