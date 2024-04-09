# `ItemStack`

> 文档版本：1.21.0.20

`ItemStack`类。script_api.@minecraft/server.itemstack.description

## 属性

/// define
`amount`


///

```js
read-only amount: int32;
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
read-only keepOnDeath: boolean;
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
read-only lockMode: ItemLockMode;
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
read-only nameTag: string | undefined;
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
`constructor`


///

script_api.@minecraft/server.itemstack.constructor.description

```js
new constructor(itemType: ItemType | string, amount: int32): ItemStack
```

/// html | div.result
//// define
`itemType`：[`ItemType`](./itemtype.md)|`string`

- script_api.@minecraft/server.itemstack.itemtype.constructor.description


////

//// define
`amount`：`int32`

- script_api.@minecraft/server.itemstack.amount.constructor.description


////

//// define
返回值：[`ItemStack`](./itemstack.md)

- script_api.@minecraft/server.itemstack.constructor.return


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

- script_api.@minecraft/server.itemstack.componentid.getcomponent.description


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
`hasComponent`


///

script_api.@minecraft/server.itemstack.hascomponent.description

```js
hasComponent(componentId: string): boolean
```

/// html | div.result
//// define
`componentId`：`string`

- script_api.@minecraft/server.itemstack.componentid.hascomponent.description


////

//// define
返回值：`boolean`

- script_api.@minecraft/server.itemstack.hascomponent.return


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

- script_api.@minecraft/server.itemstack.itemstack.isstackablewith.description


////

//// define
返回值：`boolean`

- script_api.@minecraft/server.itemstack.isstackablewith.return


////

///

