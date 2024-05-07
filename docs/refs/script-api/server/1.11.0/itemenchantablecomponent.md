# `ItemEnchantableComponent`

> 文档版本：1.21.0.24

`ItemEnchantableComponent`类，扩展自[`ItemComponent`](./itemcomponent.md)。script_api.@minecraft/server.itemenchantablecomponent.description

## 常量

/// define
`componentId`


///

```js
static read-only componentId = "minecraft:enchantable";
```


## 属性

/// define
`slots`


///

```js
read-only slots: EnchantmentSlot[];
```

/// html | div.result
//// define
`slots`：<code><a href="../enchantmentslot/">EnchantmentSlot</a>[]</code>

- script_api.@minecraft/server.itemenchantablecomponent.slots.description


////

///


## 方法

/// define
`addEnchantment`


///

script_api.@minecraft/server.itemenchantablecomponent.addenchantment.description

```js
addEnchantment(enchantment: Enchantment): void
```

/// html | div.result
//// define
`enchantment`：[`Enchantment`](./enchantment.md)

- script_api.@minecraft/server.itemenchantablecomponent.addenchantment.enchantment.description


////

//// define
返回值：`void`

- script_api.@minecraft/server.itemenchantablecomponent.addenchantment.return


////

///


/// define
`addEnchantments`


///

script_api.@minecraft/server.itemenchantablecomponent.addenchantments.description

```js
addEnchantments(enchantments: Enchantment[]): void
```

/// html | div.result
//// define
`enchantments`：<code><a href="../enchantment/">Enchantment</a>[]</code>

- script_api.@minecraft/server.itemenchantablecomponent.addenchantments.enchantments.description


////

//// define
返回值：`void`

- script_api.@minecraft/server.itemenchantablecomponent.addenchantments.return


////

///


/// define
`canAddEnchantment`


///

script_api.@minecraft/server.itemenchantablecomponent.canaddenchantment.description

```js
canAddEnchantment(enchantment: Enchantment): boolean
```

/// html | div.result
//// define
`enchantment`：[`Enchantment`](./enchantment.md)

- script_api.@minecraft/server.itemenchantablecomponent.canaddenchantment.enchantment.description


////

//// define
返回值：`boolean`

- script_api.@minecraft/server.itemenchantablecomponent.canaddenchantment.return


////

///


/// define
`getEnchantment`


///

script_api.@minecraft/server.itemenchantablecomponent.getenchantment.description

```js
getEnchantment(enchantmentType: EnchantmentType | string): Enchantment | undefined
```

/// html | div.result
//// define
`enchantmentType`：[`EnchantmentType`](./enchantmenttype.md)|`string`

- script_api.@minecraft/server.itemenchantablecomponent.getenchantment.enchantmenttype.description


////

//// define
返回值：[`Enchantment`](./enchantment.md)|`undefined`

- script_api.@minecraft/server.itemenchantablecomponent.getenchantment.return


////

///


/// define
`getEnchantments`


///

script_api.@minecraft/server.itemenchantablecomponent.getenchantments.description

```js
getEnchantments(): Enchantment[]
```

/// html | div.result
//// define
返回值：<code><a href="../enchantment/">Enchantment</a>[]</code>

- script_api.@minecraft/server.itemenchantablecomponent.getenchantments.return


////

///


/// define
`hasEnchantment`


///

script_api.@minecraft/server.itemenchantablecomponent.hasenchantment.description

```js
hasEnchantment(enchantmentType: EnchantmentType | string): boolean
```

/// html | div.result
//// define
`enchantmentType`：[`EnchantmentType`](./enchantmenttype.md)|`string`

- script_api.@minecraft/server.itemenchantablecomponent.hasenchantment.enchantmenttype.description


////

//// define
返回值：`boolean`

- script_api.@minecraft/server.itemenchantablecomponent.hasenchantment.return


////

///


/// define
`removeAllEnchantments`


///

script_api.@minecraft/server.itemenchantablecomponent.removeallenchantments.description

```js
removeAllEnchantments(): void
```

/// html | div.result
//// define
返回值：`void`

- script_api.@minecraft/server.itemenchantablecomponent.removeallenchantments.return


////

///


/// define
`removeEnchantment`


///

script_api.@minecraft/server.itemenchantablecomponent.removeenchantment.description

```js
removeEnchantment(enchantmentType: EnchantmentType | string): void
```

/// html | div.result
//// define
`enchantmentType`：[`EnchantmentType`](./enchantmenttype.md)|`string`

- script_api.@minecraft/server.itemenchantablecomponent.removeenchantment.enchantmenttype.description


////

//// define
返回值：`void`

- script_api.@minecraft/server.itemenchantablecomponent.removeenchantment.return


////

///

