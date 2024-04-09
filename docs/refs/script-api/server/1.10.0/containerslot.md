# `ContainerSlot`

> 文档版本：1.21.0.20

`ContainerSlot`类。script_api.@minecraft/server.containerslot.description

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

- script_api.@minecraft/server.containerslot.amount.description


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

- script_api.@minecraft/server.containerslot.isstackable.description


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

- script_api.@minecraft/server.containerslot.keepondeath.description


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

- script_api.@minecraft/server.containerslot.lockmode.description


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

- script_api.@minecraft/server.containerslot.maxamount.description


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

- script_api.@minecraft/server.containerslot.nametag.description


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

- script_api.@minecraft/server.containerslot.type.description


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

- script_api.@minecraft/server.containerslot.typeid.description


////

///


## 方法

/// define
`clearDynamicProperties`


///

script_api.@minecraft/server.containerslot.cleardynamicproperties.description

```js
clearDynamicProperties(): void
```

/// html | div.result
//// define
返回值：`void`

- script_api.@minecraft/server.containerslot.cleardynamicproperties.return


////

///


/// define
`getCanDestroy`


///

script_api.@minecraft/server.containerslot.getcandestroy.description

```js
getCanDestroy(): string[]
```

/// html | div.result
//// define
返回值：`string[]`

- script_api.@minecraft/server.containerslot.getcandestroy.return


////

///


/// define
`getCanPlaceOn`


///

script_api.@minecraft/server.containerslot.getcanplaceon.description

```js
getCanPlaceOn(): string[]
```

/// html | div.result
//// define
返回值：`string[]`

- script_api.@minecraft/server.containerslot.getcanplaceon.return


////

///


/// define
`getDynamicProperty`


///

script_api.@minecraft/server.containerslot.getdynamicproperty.description

```js
getDynamicProperty(identifier: string): boolean | double | float | string | Vector3 | undefined
```

/// html | div.result
//// define
`identifier`：`string`

- script_api.@minecraft/server.containerslot.identifier.getdynamicproperty.description


////

//// define
返回值：`boolean`|`double`|`float`|`string`|[`Vector3`](./vector3.md)|`undefined`

- script_api.@minecraft/server.containerslot.getdynamicproperty.return


////

///


/// define
`getDynamicPropertyIds`


///

script_api.@minecraft/server.containerslot.getdynamicpropertyids.description

```js
getDynamicPropertyIds(): string[]
```

/// html | div.result
//// define
返回值：`string[]`

- script_api.@minecraft/server.containerslot.getdynamicpropertyids.return


////

///


/// define
`getDynamicPropertyTotalByteCount`


///

script_api.@minecraft/server.containerslot.getdynamicpropertytotalbytecount.description

```js
getDynamicPropertyTotalByteCount(): int32
```

/// html | div.result
//// define
返回值：`int32`

- script_api.@minecraft/server.containerslot.getdynamicpropertytotalbytecount.return


////

///


/// define
`getItem`


///

script_api.@minecraft/server.containerslot.getitem.description

```js
getItem(): ItemStack | undefined
```

/// html | div.result
//// define
返回值：[`ItemStack`](./itemstack.md)|`undefined`

- script_api.@minecraft/server.containerslot.getitem.return


////

///


/// define
`getLore`


///

script_api.@minecraft/server.containerslot.getlore.description

```js
getLore(): string[]
```

/// html | div.result
//// define
返回值：`string[]`

- script_api.@minecraft/server.containerslot.getlore.return


////

///


/// define
`getTags`


///

script_api.@minecraft/server.containerslot.gettags.description

```js
getTags(): string[]
```

/// html | div.result
//// define
返回值：`string[]`

- script_api.@minecraft/server.containerslot.gettags.return


////

///


/// define
`hasItem`


///

script_api.@minecraft/server.containerslot.hasitem.description

```js
hasItem(): boolean
```

/// html | div.result
//// define
返回值：`boolean`

- script_api.@minecraft/server.containerslot.hasitem.return


////

///


/// define
`hasTag`


///

script_api.@minecraft/server.containerslot.hastag.description

```js
hasTag(tag: string): boolean
```

/// html | div.result
//// define
`tag`：`string`

- script_api.@minecraft/server.containerslot.tag.hastag.description


////

//// define
返回值：`boolean`

- script_api.@minecraft/server.containerslot.hastag.return


////

///


/// define
`isStackableWith`


///

script_api.@minecraft/server.containerslot.isstackablewith.description

```js
isStackableWith(itemStack: ItemStack): boolean
```

/// html | div.result
//// define
`itemStack`：[`ItemStack`](./itemstack.md)

- script_api.@minecraft/server.containerslot.itemstack.isstackablewith.description


////

//// define
返回值：`boolean`

- script_api.@minecraft/server.containerslot.isstackablewith.return


////

///


/// define
`isValid`


///

script_api.@minecraft/server.containerslot.isvalid.description

```js
isValid(): boolean
```

/// html | div.result
//// define
返回值：`boolean`

- script_api.@minecraft/server.containerslot.isvalid.return


////

///


/// define
`setCanDestroy`


///

script_api.@minecraft/server.containerslot.setcandestroy.description

```js
setCanDestroy(blockIdentifiers?: string[]): void
```

/// html | div.result
//// define
`blockIdentifiers`：`string[]`|`undefined`

- script_api.@minecraft/server.containerslot.blockidentifiers.setcandestroy.description


////

//// define
返回值：`void`

- script_api.@minecraft/server.containerslot.setcandestroy.return


////

///


/// define
`setCanPlaceOn`


///

script_api.@minecraft/server.containerslot.setcanplaceon.description

```js
setCanPlaceOn(blockIdentifiers?: string[]): void
```

/// html | div.result
//// define
`blockIdentifiers`：`string[]`|`undefined`

- script_api.@minecraft/server.containerslot.blockidentifiers.setcanplaceon.description


////

//// define
返回值：`void`

- script_api.@minecraft/server.containerslot.setcanplaceon.return


////

///


/// define
`setDynamicProperty`


///

script_api.@minecraft/server.containerslot.setdynamicproperty.description

```js
setDynamicProperty(identifier: string, value?: boolean | double | float | string | Vector3): void
```

/// html | div.result
//// define
`identifier`：`string`

- script_api.@minecraft/server.containerslot.identifier.setdynamicproperty.description


////

//// define
`value`：`boolean`|`double`|`float`|`string`|[`Vector3`](./vector3.md)|`undefined`

- script_api.@minecraft/server.containerslot.value.setdynamicproperty.description


////

//// define
返回值：`void`

- script_api.@minecraft/server.containerslot.setdynamicproperty.return


////

///


/// define
`setItem`


///

script_api.@minecraft/server.containerslot.setitem.description

```js
setItem(itemStack?: ItemStack): void
```

/// html | div.result
//// define
`itemStack`：[`ItemStack`](./itemstack.md)|`undefined`

- script_api.@minecraft/server.containerslot.itemstack.setitem.description


////

//// define
返回值：`void`

- script_api.@minecraft/server.containerslot.setitem.return


////

///


/// define
`setLore`


///

script_api.@minecraft/server.containerslot.setlore.description

```js
setLore(loreList?: string[]): void
```

/// html | div.result
//// define
`loreList`：`string[]`|`undefined`

- script_api.@minecraft/server.containerslot.lorelist.setlore.description


////

//// define
返回值：`void`

- script_api.@minecraft/server.containerslot.setlore.return


////

///

