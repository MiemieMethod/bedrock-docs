# `ItemEnchantableComponent`

> 文档版本：1.21.0.20

`ItemEnchantableComponent`类，扩展自`ItemComponent`。

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


## 方法

/// define
`addEnchantment`


///

```js
addEnchantment(enchantment: Enchantment): void
```


/// define
`addEnchantments`


///

```js
addEnchantments(enchantments: Enchantment[]): void
```


/// define
`canAddEnchantment`


///

```js
canAddEnchantment(enchantment: Enchantment): boolean
```


/// define
`getEnchantment`


///

```js
getEnchantment(enchantmentType: EnchantmentType | string): Enchantment | undefined
```


/// define
`getEnchantments`


///

```js
getEnchantments(): Enchantment[]
```


/// define
`hasEnchantment`


///

```js
hasEnchantment(enchantmentType: EnchantmentType | string): boolean
```


/// define
`removeAllEnchantments`


///

```js
removeAllEnchantments(): void
```


/// define
`removeEnchantment`


///

```js
removeEnchantment(enchantmentType: EnchantmentType | string): void
```

