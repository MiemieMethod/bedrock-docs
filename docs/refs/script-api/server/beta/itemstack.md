# `ItemStack`

> 文档版本：1.21.0.20

`ItemStack`类。

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
//// define
返回值：`void`

- 返回值。


////

///


/// define
`clone`


///

```js
clone(): ItemStack
```

/// html | div.result
//// define
返回值：[`ItemStack`](../itemstack.md)

- 返回值。


////

///


/// define
`constructor`


///

```js
new constructor(itemType: ItemType | string, amount: int32): ItemStack
```

/// html | div.result
//// define
`itemType`：[`ItemType`](../itemtype.md)|`string`

- 参数1。


////

//// define
`amount`：`int32`

- 参数2。


////

//// define
返回值：[`ItemStack`](../itemstack.md)

- 返回值。


////

///


/// define
`getCanDestroy`


///

```js
getCanDestroy(): string[]
```

/// html | div.result
//// define
返回值：`string[]`

- 返回值。


////

///


/// define
`getCanPlaceOn`


///

```js
getCanPlaceOn(): string[]
```

/// html | div.result
//// define
返回值：`string[]`

- 返回值。


////

///


/// define
`getComponent`


///

```js
getComponent(componentId: string): ItemComponent | undefined
```

/// html | div.result
//// define
`componentId`：`string`

- 参数1。


////

//// define
返回值：[`ItemComponent`](../itemcomponent.md)|`undefined`

- 返回值。


////

///


/// define
`getComponents`


///

```js
getComponents(): ItemComponent[]
```

/// html | div.result
//// define
返回值：<code><a href="../itemcomponent.md">ItemComponent</a>[]</code>

- 返回值。


////

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
返回值：`boolean`|`double`|`float`|`string`|[`Vector3`](../vector3.md)|`undefined`

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
//// define
返回值：`string[]`

- 返回值。


////

///


/// define
`getDynamicPropertyTotalByteCount`


///

```js
getDynamicPropertyTotalByteCount(): int32
```

/// html | div.result
//// define
返回值：`int32`

- 返回值。


////

///


/// define
`getLore`


///

```js
getLore(): string[]
```

/// html | div.result
//// define
返回值：`string[]`

- 返回值。


////

///


/// define
`getTags`


///

```js
getTags(): string[]
```

/// html | div.result
//// define
返回值：`string[]`

- 返回值。


////

///


/// define
`hasComponent`


///

```js
hasComponent(componentId: string): boolean
```

/// html | div.result
//// define
`componentId`：`string`

- 参数1。


////

//// define
返回值：`boolean`

- 返回值。


////

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
`itemStack`：[`ItemStack`](../itemstack.md)

- 参数1。


////

//// define
返回值：`boolean`

- 返回值。


////

///


/// define
`matches`


///

```js
matches(itemName: string, states?: Record<string, boolean | int32 | string>): boolean
```

/// html | div.result
//// define
`itemName`：`string`

- 参数1。


////

//// define
`states`：`Record<string, boolean | int32 | string>`|`undefined`

- 参数2。


////

//// define
返回值：`boolean`

- 返回值。


////

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
`value`：`boolean`|`double`|`float`|`string`|[`Vector3`](../vector3.md)|`undefined`

- 参数2。


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

