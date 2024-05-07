# `ItemStack`

> 文档版本：1.21.0.24

`ItemStack`类。script_api.@minecraft/server.itemstack.description

## 属性

/// define
`amount`


///

```js
amount: int32;
```

/// html | div.result
//// define
`amount`：`int32`

- script_api.@minecraft/server.itemstack.amount.description


////

///


/// define
`isStackable`


///

```js
read-only isStackable: boolean;
```

/// html | div.result
//// define
`isStackable`：`boolean`

- script_api.@minecraft/server.itemstack.isstackable.description


////

///


/// define
`keepOnDeath`


///

```js
keepOnDeath: boolean;
```

/// html | div.result
//// define
`keepOnDeath`：`boolean`

- script_api.@minecraft/server.itemstack.keepondeath.description


////

///


/// define
`lockMode`


///

```js
lockMode: ItemLockMode;
```

/// html | div.result
//// define
`lockMode`：[`ItemLockMode`](./itemlockmode.md)

- script_api.@minecraft/server.itemstack.lockmode.description


////

///


/// define
`maxAmount`


///

```js
read-only maxAmount: int32;
```

/// html | div.result
//// define
`maxAmount`：`int32`

- script_api.@minecraft/server.itemstack.maxamount.description


////

///


/// define
`nameTag`


///

```js
nameTag: string | undefined;
```

/// html | div.result
//// define
`nameTag`：`string`|`undefined`

- script_api.@minecraft/server.itemstack.nametag.description


////

///


/// define
`type`


///

```js
read-only type: ItemType;
```

/// html | div.result
//// define
`type`：[`ItemType`](./itemtype.md)

- script_api.@minecraft/server.itemstack.type.description


////

///


/// define
`typeId`


///

```js
read-only typeId: string;
```

/// html | div.result
//// define
`typeId`：`string`

- script_api.@minecraft/server.itemstack.typeid.description


////

///


## 方法

/// define
`clearDynamicProperties`


///

script_api.@minecraft/server.itemstack.cleardynamicproperties.description

```js
clearDynamicProperties(): void
```

/// html | div.result
//// define
返回值：`void`

- script_api.@minecraft/server.itemstack.cleardynamicproperties.return


////

///


/// define
`clone`


///

script_api.@minecraft/server.itemstack.clone.description

```js
clone(): ItemStack
```

/// html | div.result
//// define
返回值：[`ItemStack`](./itemstack.md)

- script_api.@minecraft/server.itemstack.clone.return


////

///


/// define
`constructor`


///

script_api.@minecraft/server.itemstack.constructor.description

```js
new constructor(itemType: ItemType | string, amount: int32): ItemStack
```

/// html | div.result
//// define
`itemType`：[`ItemType`](./itemtype.md)|`string`

- script_api.@minecraft/server.itemstack.constructor.itemtype.description


////

//// define
`amount`：`int32`＝`1`∈[`1`, `255`]

- script_api.@minecraft/server.itemstack.constructor.amount.description


////

//// define
返回值：[`ItemStack`](./itemstack.md)

- script_api.@minecraft/server.itemstack.constructor.return


////

///


/// define
`getCanDestroy`


///

script_api.@minecraft/server.itemstack.getcandestroy.description

```js
getCanDestroy(): string[]
```

/// html | div.result
//// define
返回值：`string[]`

- script_api.@minecraft/server.itemstack.getcandestroy.return


////

///


/// define
`getCanPlaceOn`


///

script_api.@minecraft/server.itemstack.getcanplaceon.description

```js
getCanPlaceOn(): string[]
```

/// html | div.result
//// define
返回值：`string[]`

- script_api.@minecraft/server.itemstack.getcanplaceon.return


////

///


/// define
`getComponent`


///

script_api.@minecraft/server.itemstack.getcomponent.description

```js
getComponent(componentId: string): ItemComponent | undefined
```

/// html | div.result
//// define
`componentId`：`string`

- script_api.@minecraft/server.itemstack.getcomponent.componentid.description


////

//// define
返回值：[`ItemComponent`](./itemcomponent.md)|`undefined`

- script_api.@minecraft/server.itemstack.getcomponent.return


////

///


/// define
`getComponents`


///

script_api.@minecraft/server.itemstack.getcomponents.description

```js
getComponents(): ItemComponent[]
```

/// html | div.result
//// define
返回值：<code><a href="../itemcomponent/">ItemComponent</a>[]</code>

- script_api.@minecraft/server.itemstack.getcomponents.return


////

///


/// define
`getDynamicProperty`


///

script_api.@minecraft/server.itemstack.getdynamicproperty.description

```js
getDynamicProperty(identifier: string): boolean | double | float | string | Vector3 | undefined
```

/// html | div.result
//// define
`identifier`：`string`

- script_api.@minecraft/server.itemstack.getdynamicproperty.identifier.description


////

//// define
返回值：`boolean`|`double`|`float`|`string`|[`Vector3`](./vector3.md)|`undefined`

- script_api.@minecraft/server.itemstack.getdynamicproperty.return


////

///


/// define
`getDynamicPropertyIds`


///

script_api.@minecraft/server.itemstack.getdynamicpropertyids.description

```js
getDynamicPropertyIds(): string[]
```

/// html | div.result
//// define
返回值：`string[]`

- script_api.@minecraft/server.itemstack.getdynamicpropertyids.return


////

///


/// define
`getDynamicPropertyTotalByteCount`


///

script_api.@minecraft/server.itemstack.getdynamicpropertytotalbytecount.description

```js
getDynamicPropertyTotalByteCount(): int32
```

/// html | div.result
//// define
返回值：`int32`

- script_api.@minecraft/server.itemstack.getdynamicpropertytotalbytecount.return


////

///


/// define
`getLore`


///

script_api.@minecraft/server.itemstack.getlore.description

```js
getLore(): string[]
```

/// html | div.result
//// define
返回值：`string[]`

- script_api.@minecraft/server.itemstack.getlore.return


////

///


/// define
`getTags`


///

script_api.@minecraft/server.itemstack.gettags.description

```js
getTags(): string[]
```

/// html | div.result
//// define
返回值：`string[]`

- script_api.@minecraft/server.itemstack.gettags.return


////

///


/// define
`hasComponent`


///

script_api.@minecraft/server.itemstack.hascomponent.description

```js
hasComponent(componentId: string): boolean
```

/// html | div.result
//// define
`componentId`：`string`

- script_api.@minecraft/server.itemstack.hascomponent.componentid.description


////

//// define
返回值：`boolean`

- script_api.@minecraft/server.itemstack.hascomponent.return


////

///


/// define
`hasTag`


///

script_api.@minecraft/server.itemstack.hastag.description

```js
hasTag(tag: string): boolean
```

/// html | div.result
//// define
`tag`：`string`

- script_api.@minecraft/server.itemstack.hastag.tag.description


////

//// define
返回值：`boolean`

- script_api.@minecraft/server.itemstack.hastag.return


////

///


/// define
`isStackableWith`


///

script_api.@minecraft/server.itemstack.isstackablewith.description

```js
isStackableWith(itemStack: ItemStack): boolean
```

/// html | div.result
//// define
`itemStack`：[`ItemStack`](./itemstack.md)

- script_api.@minecraft/server.itemstack.isstackablewith.itemstack.description


////

//// define
返回值：`boolean`

- script_api.@minecraft/server.itemstack.isstackablewith.return


////

///


/// define
`matches`


///

script_api.@minecraft/server.itemstack.matches.description

```js
matches(itemName: string, states?: Record<string, boolean | int32 | string>): boolean
```

/// html | div.result
//// define
`itemName`：`string`

- script_api.@minecraft/server.itemstack.matches.itemname.description


////

//// define
`states`?：`Record<string, boolean | int32 | string>`＝`null`

- script_api.@minecraft/server.itemstack.matches.states.description


////

//// define
返回值：`boolean`

- script_api.@minecraft/server.itemstack.matches.return


////

///


/// define
`setCanDestroy`


///

script_api.@minecraft/server.itemstack.setcandestroy.description

```js
setCanDestroy(blockIdentifiers?: string[]): void
```

/// html | div.result
//// define
`blockIdentifiers`?：`string[]`＝`null`

- script_api.@minecraft/server.itemstack.setcandestroy.blockidentifiers.description


////

//// define
返回值：`void`

- script_api.@minecraft/server.itemstack.setcandestroy.return


////

///


/// define
`setCanPlaceOn`


///

script_api.@minecraft/server.itemstack.setcanplaceon.description

```js
setCanPlaceOn(blockIdentifiers?: string[]): void
```

/// html | div.result
//// define
`blockIdentifiers`?：`string[]`＝`null`

- script_api.@minecraft/server.itemstack.setcanplaceon.blockidentifiers.description


////

//// define
返回值：`void`

- script_api.@minecraft/server.itemstack.setcanplaceon.return


////

///


/// define
`setDynamicProperty`


///

script_api.@minecraft/server.itemstack.setdynamicproperty.description

```js
setDynamicProperty(identifier: string, value?: boolean | double | float | string | Vector3): void
```

/// html | div.result
//// define
`identifier`：`string`

- script_api.@minecraft/server.itemstack.setdynamicproperty.identifier.description


////

//// define
`value`?：`boolean`|`double`|`float`|`string`|[`Vector3`](./vector3.md)＝`null`

- script_api.@minecraft/server.itemstack.setdynamicproperty.value.description


////

//// define
返回值：`void`

- script_api.@minecraft/server.itemstack.setdynamicproperty.return


////

///


/// define
`setLore`


///

script_api.@minecraft/server.itemstack.setlore.description

```js
setLore(loreList?: string[]): void
```

/// html | div.result
//// define
`loreList`?：`string[]`＝`null`

- script_api.@minecraft/server.itemstack.setlore.lorelist.description


////

//// define
返回值：`void`

- script_api.@minecraft/server.itemstack.setlore.return


////

///

