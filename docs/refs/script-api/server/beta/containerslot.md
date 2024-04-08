# `ContainerSlot`

> 文档版本：1.21.0.20

`ContainerSlot`类。

## 属性

/// define
`amount`


///

```js
amount: int32;
```


/// define
`isStackable`


///

```js
read-only isStackable: boolean;
```


/// define
`keepOnDeath`


///

```js
keepOnDeath: boolean;
```


/// define
`lockMode`


///

```js
lockMode: ItemLockMode;
```


/// define
`maxAmount`


///

```js
read-only maxAmount: int32;
```


/// define
`nameTag`


///

```js
nameTag: string | undefined;
```


/// define
`type`


///

```js
read-only type: ItemType;
```


/// define
`typeId`


///

```js
read-only typeId: string;
```


## 方法

/// define
`clearDynamicProperties`


///

```js
clearDynamicProperties(): void
```

/// html | div.result

///


/// define
`getCanDestroy`


///

```js
getCanDestroy(): string[]
```

/// html | div.result

///


/// define
`getCanPlaceOn`


///

```js
getCanPlaceOn(): string[]
```

/// html | div.result

///


/// define
`getDynamicProperty`


///

```js
getDynamicProperty(identifier: string): boolean | double | float | string | Vector3 | undefined
```

/// html | div.result
//// define
`identifier`：`string`

- 参数1。


////

//// define
返回值：boolean|double|float|string|Vector3|`undefined`

- 返回值。


////

///


/// define
`getDynamicPropertyIds`


///

```js
getDynamicPropertyIds(): string[]
```

/// html | div.result

///


/// define
`getDynamicPropertyTotalByteCount`


///

```js
getDynamicPropertyTotalByteCount(): int32
```

/// html | div.result

///


/// define
`getItem`


///

```js
getItem(): ItemStack | undefined
```

/// html | div.result

///


/// define
`getLore`


///

```js
getLore(): string[]
```

/// html | div.result

///


/// define
`getTags`


///

```js
getTags(): string[]
```

/// html | div.result

///


/// define
`hasItem`


///

```js
hasItem(): boolean
```

/// html | div.result

///


/// define
`hasTag`


///

```js
hasTag(tag: string): boolean
```

/// html | div.result
//// define
`tag`：`string`

- 参数1。


////

//// define
返回值：`boolean`

- 返回值。


////

///


/// define
`isStackableWith`


///

```js
isStackableWith(itemStack: ItemStack): boolean
```

/// html | div.result
//// define
`itemStack`：[`ItemStack`](./itemstack.md)

- 参数1。


////

//// define
返回值：`boolean`

- 返回值。


////

///


/// define
`isValid`


///

```js
isValid(): boolean
```

/// html | div.result

///


/// define
`setCanDestroy`


///

```js
setCanDestroy(blockIdentifiers?: string[]): void
```

/// html | div.result
//// define
`blockIdentifiers`：`string[]`|`undefined`

- 参数1。


////

//// define
返回值：`void`

- 返回值。


////

///


/// define
`setCanPlaceOn`


///

```js
setCanPlaceOn(blockIdentifiers?: string[]): void
```

/// html | div.result
//// define
`blockIdentifiers`：`string[]`|`undefined`

- 参数1。


////

//// define
返回值：`void`

- 返回值。


////

///


/// define
`setDynamicProperty`


///

```js
setDynamicProperty(identifier: string, value?: boolean | double | float | string | Vector3): void
```

/// html | div.result
//// define
`identifier`：`string`

- 参数1。


////

//// define
`value`：boolean|double|float|string|Vector3|`undefined`

- 参数2。


////

//// define
返回值：`void`

- 返回值。


////

///


/// define
`setItem`


///

```js
setItem(itemStack?: ItemStack): void
```

/// html | div.result
//// define
`itemStack`：[`ItemStack`](./itemstack.md)|`undefined`

- 参数1。


////

//// define
返回值：`void`

- 返回值。


////

///


/// define
`setLore`


///

```js
setLore(loreList?: string[]): void
```

/// html | div.result
//// define
`loreList`：`string[]`|`undefined`

- 参数1。


////

//// define
返回值：`void`

- 返回值。


////

///

