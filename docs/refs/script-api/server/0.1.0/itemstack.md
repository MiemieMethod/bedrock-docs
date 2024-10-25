# `ItemStack`

> 文档版本：1.21.50.25

`ItemStack`类。script_api.mojang-minecraft.itemstack.description

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

- script_api.mojang-minecraft.itemstack.amount.description


////

///


/// define
`data`


///

```js
data: int32;
```

/// html | div.result
//// define
`data`：`int32`

- script_api.mojang-minecraft.itemstack.data.description


////

///


/// define
`id`


///

```js
read-only id: string;
```

/// html | div.result
//// define
`id`：`string`

- script_api.mojang-minecraft.itemstack.id.description


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

- script_api.mojang-minecraft.itemstack.nametag.description


////

///


## 方法

/// define
`constructor`


///

script_api.mojang-minecraft.itemstack.constructor.description

```js
new constructor(itemType: ItemType | string, amount: int32, data: int32): ItemStack
```

/// html | div.result
//// define
`itemType`：[`ItemType`](./itemtype.md)|`string`

- script_api.mojang-minecraft.itemstack.constructor.itemtype.description


////

//// define
`amount`：`int32`＝`1`∈[`0`, `255`]

- script_api.mojang-minecraft.itemstack.constructor.amount.description


////

//// define
`data`：`int32`＝`0`∈[`0`, `32767`]

- script_api.mojang-minecraft.itemstack.constructor.data.description


////

//// define
返回值：[`ItemStack`](./itemstack.md)

- script_api.mojang-minecraft.itemstack.constructor.return


////

///


/// define
`getComponent`


///

script_api.mojang-minecraft.itemstack.getcomponent.description

```js
getComponent(componentId: string): ItemComponent | undefined
```

/// html | div.result
//// define
`componentId`：`string`

- script_api.mojang-minecraft.itemstack.getcomponent.componentid.description


////

//// define
返回值：[`ItemComponent`](./itemcomponent.md)|`undefined`

- script_api.mojang-minecraft.itemstack.getcomponent.return


////

///


/// define
`getComponents`


///

script_api.mojang-minecraft.itemstack.getcomponents.description

```js
getComponents(): ItemComponent[]
```

/// html | div.result
//// define
返回值：<code><a href="../itemcomponent/">ItemComponent</a>[]</code>

- script_api.mojang-minecraft.itemstack.getcomponents.return


////

///


/// define
`getLore`


///

script_api.mojang-minecraft.itemstack.getlore.description

```js
getLore(): string[]
```

/// html | div.result
//// define
返回值：`string[]`

- script_api.mojang-minecraft.itemstack.getlore.return


////

///


/// define
`hasComponent`


///

script_api.mojang-minecraft.itemstack.hascomponent.description

```js
hasComponent(componentId: string): boolean
```

/// html | div.result
//// define
`componentId`：`string`

- script_api.mojang-minecraft.itemstack.hascomponent.componentid.description


////

//// define
返回值：`boolean`

- script_api.mojang-minecraft.itemstack.hascomponent.return


////

///


/// define
`setLore`


///

script_api.mojang-minecraft.itemstack.setlore.description

```js
setLore(loreList?: string[]): void
```

/// html | div.result
//// define
`loreList`?：`string[]`＝`null`

- script_api.mojang-minecraft.itemstack.setlore.lorelist.description


////

//// define
返回值：`void`

- script_api.mojang-minecraft.itemstack.setlore.return


////

///

