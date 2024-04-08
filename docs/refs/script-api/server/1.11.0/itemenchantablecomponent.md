# `ItemEnchantableComponent`

> 文档版本：1.21.0.20

`ItemEnchantableComponent`类，扩展自[`ItemComponent`](./itemcomponent.md)。

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

- 属性。


////

///


## 方法

/// define
`addEnchantment`


///

```js
addEnchantment(enchantment: Enchantment): void
```

/// html | div.result
//// define
`enchantment`：[`Enchantment`](./enchantment.md)

- 参数1。


////

//// define
返回值：`void`

- 返回值。


////

///


/// define
`addEnchantments`


///

```js
addEnchantments(enchantments: Enchantment[]): void
```

/// html | div.result
//// define
`enchantments`：<code><a href="../enchantment/">Enchantment</a>[]</code>

- 参数1。


////

//// define
返回值：`void`

- 返回值。


////

///


/// define
`canAddEnchantment`


///

```js
canAddEnchantment(enchantment: Enchantment): boolean
```

/// html | div.result
//// define
`enchantment`：[`Enchantment`](./enchantment.md)

- 参数1。


////

//// define
返回值：`boolean`

- 返回值。


////

///


/// define
`getEnchantment`


///

```js
getEnchantment(enchantmentType: EnchantmentType | string): Enchantment | undefined
```

/// html | div.result
//// define
`enchantmentType`：[`EnchantmentType`](./enchantmenttype.md)|`string`

- 参数1。


////

//// define
返回值：[`Enchantment`](./enchantment.md)|`undefined`

- 返回值。


////

///


/// define
`getEnchantments`


///

```js
getEnchantments(): Enchantment[]
```

/// html | div.result
//// define
返回值：<code><a href="../enchantment/">Enchantment</a>[]</code>

- 返回值。


////

///


/// define
`hasEnchantment`


///

```js
hasEnchantment(enchantmentType: EnchantmentType | string): boolean
```

/// html | div.result
//// define
`enchantmentType`：[`EnchantmentType`](./enchantmenttype.md)|`string`

- 参数1。


////

//// define
返回值：`boolean`

- 返回值。


////

///


/// define
`removeAllEnchantments`


///

```js
removeAllEnchantments(): void
```

/// html | div.result
//// define
返回值：`void`

- 返回值。


////

///


/// define
`removeEnchantment`


///

```js
removeEnchantment(enchantmentType: EnchantmentType | string): void
```

/// html | div.result
//// define
`enchantmentType`：[`EnchantmentType`](./enchantmenttype.md)|`string`

- 参数1。


////

//// define
返回值：`void`

- 返回值。


////

///

